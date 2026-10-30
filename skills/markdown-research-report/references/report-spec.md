# Research report specification

## Report structure

Use only sections relevant to the corpus, usually:

1. Title and mandatory reader/directory warning
2. Abstract or executive summary
3. Corpus scope and analysis method
4. Analytical framework
5. State of the art by research theme
6. Cross-cutting limitations and evidence gaps
7. Research directions and priorities
8. Executable technical roadmap
9. Conclusions
10. Evidence matrix or literature appendix
11. References

Prefer synthesis paragraphs that compare multiple sources. Use a table only when it makes repeated mappings or comparisons clearer.

## Citation format

- Use sequential numeric citations: `[1]`, `[2,4]`, `[3–5]`.
- Number sources by first appearance and reuse the same number everywhere.
- Put the citation directly after the supported claim and before trailing explanatory text when needed.
- Add citations to table cells containing literature-derived claims.
- Attach citations to all percentages, error metrics, dimensions, dates, sample sizes, performance improvements, and named findings.
- Attach citations to research directions that arise from documented gaps. If a direction is an original synthesis, write “本报告建议” or equivalent and cite the evidence motivating it.

## Reference format

Use one consistent scientific format. A practical form is:

```text
[1] Author A, Author B, et al. [Source title](./sources/S01.pdf)[J]. Journal, year, volume(issue): pages/article. DOI: ...
```

Use `[C]`, `[R]`, `[D]`, `[EB/OL]`, or another suitable type when the source is not a journal article. Omit unavailable fields rather than guessing them.

## Typora-compatible mathematics

Use Typora-compatible dollar delimiters throughout the report:

- Inline formula: `$h(x)=a+bx$`
- Display formula:

  ```markdown
  $$
  h(x)=a+bx
  $$
  ```

Each display delimiter must be exactly `$$` on a standalone line. Keep a blank line before the opening delimiter and after the closing delimiter. Do not emit `\(...\)` or `\[...\]`. Do not put a formula in a fenced code block when it is intended to render.

## Relative-link format

Resolve links from the Markdown file's directory, not from the workspace root.

Preferred portable layout:

```text
delivery-root/
├─ research-report.md
└─ sources/
   ├─ S01.pdf
   ├─ S02.docx
   └─ ...
```

Add a `<small>` warning directly below every report title. When documents are packaged under `sources/`, use:

```html
<small>阅读与目录注意事项：推荐使用 Typora 阅读本报告；部分 Markdown 阅读器可能无法正确启动链接的 PDF 等外部文献文件。请勿修改本报告、`sources` 目录及其中源文件的相对位置和文件名，否则文献链接将失效。本报告须位于交付根目录，`sources` 目录须与本报告同级。</small>
```

Preferred link:

```markdown
[Source title](./sources/S01.pdf)
```

If descriptive names must be preserved, encode unsafe ASCII characters while keeping slashes:

```markdown
[Source title](./sources/Long%20source%20title%20%28final%29.docx)
```

Never emit:

```markdown
[Source](file:///C:/Users/name/Desktop/project/source.pdf)
[Source](C:\Users\name\Desktop\project\source.pdf)
```

## Archive decision

Treat organization as a distinct, opt-in operation:

- “Read these documents and write a report” does not authorize moving or renaming files.
- “Organize/archive/classify these source files” authorizes an archive plan and in-scope file operations.
- “Create a portable package” authorizes copying or renaming into a short-path package after confirming the package root if needed.

## Quality assurance

Before delivery:

- Confirm every included source document was processed or explicitly excluded.
- Confirm the mandatory `<small>` warning appears immediately below the main title and names Typora.
- Confirm inline formulas use `$...$`, display formulas use paired standalone `$$` delimiters, and no `\(...\)` or `\[...\]` math delimiters remain outside code.
- Confirm references are continuous and every citation identifier exists.
- Confirm every quantitative claim has a same-sentence or same-cell citation.
- Confirm each bibliography link is relative and resolves after URI decoding.
- Confirm the report remains valid after the common root is moved or zipped.
- Confirm no absolute local path, tool token, placeholder, or fabricated metadata remains.
