---
name: markdown-research-report
description: Create evidence-based Markdown research summary reports from user-provided literature in PDF, DOCX, Markdown, TXT, RTF, HTML, and similar document formats, with structured synthesis, numbered in-text citations, complete references, and portable relative links to source files. Use when Codex must review a document corpus and produce a literature review, state-of-the-art report, research framework, gap analysis, or future research agenda. Archive, rename, move, or classify source files only when the user explicitly requests file organization.
---

# Markdown Research Report

## Core workflow

1. Inventory all supplied source documents and any user-provided notes or prior summaries.
2. Read each format with its appropriate document workflow. Extract title, authors, year, venue, DOI, abstract, methods, quantitative results, limitations, and conclusions. For PDF or visually structured documents, inspect representative rendered pages when layout, equations, tables, or figures affect interpretation.
3. Separate source literature from official manuals, user-authored drafts, duplicates, presentations, and supplementary material.
4. Build an evidence matrix before drafting. Assign each unique source one stable reference number in order of first citation.
5. Synthesize across sources instead of writing isolated paper summaries. Organize by research problem, method, evidence, limitation, and opportunity.
6. Draft from `assets/research-report-template.md`, adapting headings to the domain. Keep the mandatory `<small>` reader and directory warning directly below the main title. Format mathematics for Typora: use `$...$` for inline formulas and standalone `$$` lines around display formulas; never use `\(...\)` or `\[...\]`.
7. Apply the citation and link rules in `references/report-spec.md`.
8. Run `scripts/validate_report.py` against the final Markdown report and fix every error before delivery.

## Evidence rules

- Cite every quantitative value, comparison, accuracy claim, sample count, date-sensitive result, named method attribution, research-area statement, limitation, and literature-derived research direction.
- Place citations immediately after the supported sentence or clause using `[1]`, `[2,4]`, or `[3–5]`.
- Cite proposed directions with the studies that motivate them. Clearly label genuinely new recommendations as this report's synthesis.
- Do not cite a source that does not directly support the claim.
- Do not invent missing authors, venues, years, pages, or DOIs. Mark unavailable metadata explicitly.
- Keep reference numbering continuous and consistent between body, evidence tables, and bibliography.

## Typora mathematics

- Write inline mathematics as `$expression$`, with both delimiters on the same line.
- Write display mathematics as:

  ```markdown
  $$
  expression
  $$
  ```

- Put each display `$$` delimiter on its own line and leave a blank line before the opening delimiter and after the closing delimiter.
- Do not use `\(...\)`, `\[...\]`, or a fenced code block for rendered mathematics.
- Keep units and surrounding prose outside math delimiters unless they are part of the mathematical expression.
- Before delivery, confirm every display delimiter is paired and run `scripts/validate_report.py`.

## Portable source links

- Link the title in each bibliography entry to its local source document when the report and sources will be delivered together.
- Use paths relative to the report file. Never use drive letters, user-home paths, `file:///`, or workspace-specific absolute paths.
- Use forward slashes. Encode spaces as `%20`, literal parentheses as `%28` and `%29`, `#` as `%23`, `?` as `%3F`, and `%` as `%25`.
- Keep paths short. For maximum Windows and Markdown-reader compatibility, prefer a package such as `sources/S01.pdf`, `sources/S02.docx`, and map identifiers to full titles in the bibliography.
- Put a `<small>` note immediately below every report title. State that the documented directory structure and file names must not be changed, recommend Typora for reading, and warn that other Markdown readers may fail to launch linked PDFs or other external source files. Include the concrete required relative structure whenever local source links are present.
- Validate every decoded target from the report's actual location before delivery.

## Optional archive branch

Do not move, rename, copy into a new hierarchy, or classify the source documents unless the user explicitly asks for organization or a portable package.

When organization is requested:

1. Propose or infer a reversible classification based on the dominant research question.
2. Preserve non-paper files and user-authored outputs unless explicitly included.
3. Prevent overwrites and verify all sources before moving.
4. Create a Markdown index with links relative to the index file.
5. Put a `<small>` directory-structure note below the index title.
6. Verify file counts and all relative targets after changes.

When organization is not requested, leave the corpus untouched and place the report where its relative links can resolve. If that placement is unknown, request it or deliver the report without local links while explaining the constraint.

## Deliverables

- Produce the research report in Markdown unless the user requests another format.
- Put references at the end of the report.
- If a portable package is requested, keep the report and linked source tree under one common root.
- Report the source count, excluded material, citation count, link count, and validation result in the handoff.

## Resources

- Read `references/report-spec.md` for the detailed format, citation, link, and QA specification.
- Copy and adapt `assets/research-report-template.md` when starting a report.
- Run `python scripts/validate_report.py REPORT.md --require-links` when bibliography source links are required; omit `--require-links` when local links were not requested or cannot be packaged.
