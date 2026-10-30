from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote


REFERENCE_HEADING = re.compile(r"^##\s+(?:参考文献|References)\s*$", re.M | re.I)
REFERENCE_ENTRY = re.compile(r"^\[(\d+)\]\s+", re.M)
CITATION = re.compile(
    r"\[((?:\d+\s*(?:[-–—]\s*\d+)?)(?:\s*,\s*\d+\s*(?:[-–—]\s*\d+)?)*)\]"
)
SOURCE_LINK = re.compile(
    r"\]\((\./[^\r\n)]*?\.(?:pdf|docx?|md|txt|rtf|odt|html?|epub))\)", re.I
)
NUMERIC_CLAIM = re.compile(r"%|±|\b(?:RMSE|RMSD|MAE|RMS)\b", re.I)
LEGACY_MATH_DELIMITER = re.compile(r"\\(?:\[|\]|\(|\))")


def expand_citation(content: str) -> set[int]:
    ids: set[int] = set()
    for part in content.split(","):
        part = part.strip()
        match = re.fullmatch(r"(\d+)\s*[-–—]\s*(\d+)", part)
        if match:
            start, end = map(int, match.groups())
            if start > end:
                raise ValueError(f"reversed citation range: {part}")
            ids.update(range(start, end + 1))
        else:
            ids.add(int(part))
    return ids


def is_absolute_or_file_uri(target: str) -> bool:
    decoded = unquote(target)
    return (
        decoded.lower().startswith("file:")
        or bool(re.match(r"^[A-Za-z]:[\\/]", decoded))
        or decoded.startswith("/")
        or decoded.startswith("\\\\")
    )


def strip_code_for_math_validation(text: str) -> list[tuple[int, str]]:
    """Return non-code Markdown lines with inline code removed."""

    retained: list[tuple[int, str]] = []
    in_fence = False
    fence_marker = ""
    for line_no, line in enumerate(text.splitlines(), 1):
        stripped = line.lstrip()
        if not in_fence and (stripped.startswith("```") or stripped.startswith("~~~")):
            in_fence = True
            fence_marker = stripped[:3]
            continue
        if in_fence:
            if stripped.startswith(fence_marker):
                in_fence = False
                fence_marker = ""
            continue
        retained.append((line_no, re.sub(r"`[^`\r\n]*`", "", line)))
    return retained


def validate_typora_math(text: str) -> list[str]:
    """Validate Typora-compatible Markdown math delimiters."""

    errors: list[str] = []
    display_open_line: int | None = None
    for line_no, line in strip_code_for_math_validation(text):
        legacy = LEGACY_MATH_DELIMITER.search(line)
        if legacy:
            errors.append(
                f"legacy math delimiter {legacy.group(0)!r} at line {line_no}; "
                "use $...$ inline or standalone $$ blocks"
            )

        if "$$" not in line:
            if display_open_line is None:
                unescaped = re.sub(r"\\\$", "", line)
                if unescaped.count("$") % 2:
                    errors.append(
                        f"unpaired inline $ delimiter at line {line_no}: "
                        f"{line.strip()}"
                    )
            continue
        if line.strip() != "$$":
            errors.append(
                f"display math delimiter must be standalone at line {line_no}: "
                f"{line.strip()}"
            )
            continue
        if display_open_line is None:
            display_open_line = line_no
        else:
            display_open_line = None

    if display_open_line is not None:
        errors.append(f"unclosed display math block opened at line {display_open_line}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate citations and portable source links in a Markdown research report.")
    parser.add_argument("report", type=Path)
    parser.add_argument("--require-links", action="store_true", help="Require one local source link per reference entry.")
    args = parser.parse_args()

    report = args.report.resolve()
    text = report.read_text(encoding="utf-8-sig")
    errors: list[str] = []
    warnings: list[str] = []
    errors.extend(validate_typora_math(text))

    heading = REFERENCE_HEADING.search(text)
    if not heading:
        errors.append("missing '## 参考文献' or '## References' heading")
        body, references = text, ""
    else:
        body, references = text[: heading.start()], text[heading.end() :]

    first_lines = text.splitlines()[:8]
    title_area = "\n".join(first_lines)
    if "<small>" not in title_area or "Typora" not in title_area:
        errors.append("missing mandatory <small> Typora/directory warning directly below the main title")

    ref_ids = [int(value) for value in REFERENCE_ENTRY.findall(references)]
    expected = list(range(1, len(ref_ids) + 1))
    if ref_ids != expected:
        errors.append(f"reference numbers are not continuous from 1: {ref_ids}")

    cited: set[int] = set()
    for match in CITATION.finditer(body):
        try:
            cited.update(expand_citation(match.group(1)))
        except ValueError as exc:
            errors.append(str(exc))

    unknown = sorted(cited - set(ref_ids))
    if unknown:
        errors.append(f"citations without reference entries: {unknown}")
    uncited = sorted(set(ref_ids) - cited)
    if uncited:
        warnings.append(f"reference entries not cited in report body: {uncited}")

    links = SOURCE_LINK.findall(references)
    if args.require_links and len(links) != len(ref_ids):
        errors.append(f"expected {len(ref_ids)} relative source links, found {len(links)}")

    for target in links:
        if is_absolute_or_file_uri(target):
            errors.append(f"non-portable source link: {target}")
            continue
        decoded = unquote(target)
        resolved = (report.parent / Path(decoded)).resolve()
        if not resolved.is_file():
            errors.append(f"missing source target: {target} -> {resolved}")

    for line_no, line in enumerate(body.splitlines(), 1):
        if NUMERIC_CLAIM.search(line) and not CITATION.search(line):
            errors.append(f"numeric claim without same-line citation at line {line_no}: {line.strip()}")

    forbidden = re.findall(r"(?:file:///|[A-Za-z]:\\Users\\|TODO|待补|\{\{[^}]+\}\})", text, re.I)
    if forbidden:
        errors.append(f"forbidden absolute path or placeholder found: {sorted(set(forbidden))}")

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    print(
        f"Checked {report}: {len(ref_ids)} references, {len(cited)} cited ids, "
        f"{len(links)} source links, {len(errors)} errors, {len(warnings)} warnings."
    )
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
