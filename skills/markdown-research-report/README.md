# markdown-research-report

将 PDF、DOCX、Markdown、TXT 等文献材料整理为具有论文式交叉引用、完整参考文献和可移植源文件链接的 Markdown 研究总结报告。

## 核心能力

- 读取并综合多种格式的文献材料，而非逐篇机械摘要。
- 生成研究现状、分析框架、关键限制、研究空白、研究方向和技术路线。
- 使用连续顺序编码引用，如 `[1]`、`[2,4]`、`[3–5]`。
- 为定量数据、比较结论、方法归属、研究内容和研究方向配置就近引用。
- 在文末生成统一格式的参考文献，并将题名链接到本地源文件。
- 使用相对路径构建可压缩、可转发的文献包。
- 通过脚本检查引用连续性、定量结论引用和源文件链接。
- 仅在用户明确提出时整理、分类、移动或重命名文献文件。

## 支持的输入

包括但不限于：

- PDF
- DOCX / DOC
- Markdown
- TXT / RTF
- HTML
- ODT
- EPUB

实际读取能力取决于当前 Codex 环境中可用的文档处理工具和技能。

## 默认输出

默认生成 Markdown 研究总结报告。典型结构包括：

1. 摘要
2. 文献范围与分析方法
3. 分析框架
4. 分主题研究现状
5. 关键限制与研究空白
6. 建议的研究方向
7. 技术路线与优先级
8. 综合结论
9. 文献证据矩阵
10. 参考文献

## 强制格式要求

每份报告的主标题下方必须显示一段小字，提醒阅读器兼容性和目录约束。例如：

```html
<small>阅读与目录注意事项：推荐使用 Typora 阅读本报告；部分 Markdown 阅读器可能无法正确启动链接的 PDF 等外部文献文件。请勿修改本报告、`sources` 目录及其中源文件的相对位置和文件名，否则文献链接将失效。本报告须位于交付根目录，`sources` 目录须与本报告同级。</small>
```

## 引用规则

- 按正文首次出现顺序分配文献编号。
- 相同文献在全文中始终复用同一编号。
- 每项定量数据、误差指标、样本数量、性能提升和比较结论都必须引用来源。
- 文献支持的研究内容、限制与研究方向必须就近引用。
- 报告原创建议应明确写为“本报告建议”等表述，同时引用其证据基础。
- 不得猜测缺失的作者、年份、期刊、页码或 DOI。

## 可移植链接

推荐交付结构：

```text
delivery-root/
├─ research-report.md
└─ sources/
   ├─ S01.pdf
   ├─ S02.docx
   └─ ...
```

参考文献链接示例：

```markdown
[1] Author. [Source title](./sources/S01.pdf)[J]. Journal, 2026.
```

不得使用盘符、用户目录或 `file:///` 绝对链接。为提高 Windows 和 Markdown 阅读器兼容性，建议采用 `S01.pdf`、`S02.docx` 等短英文文件名。

## 安装

将整个 `markdown-research-report` 文件夹复制到个人 Codex 技能目录：

```text
%USERPROFILE%\.codex\skills\markdown-research-report
```

重新启动或刷新 Codex 后即可发现该技能。

## 使用

显式调用：

```text
使用 $markdown-research-report 阅读这些文献并生成研究现状与研究方向报告。
```

其他示例：

```text
使用 $markdown-research-report 综合此文件夹下的 PDF 和 DOCX，生成带交叉引用的 Markdown 综述。
```

```text
使用 $markdown-research-report 生成可压缩转发的报告包，并整理文献目录。
```

最后一个示例明确要求整理文献，因此技能可以执行归档分支；仅要求“阅读并写报告”时，技能不会移动或重命名源文件。

## 验证报告

验证脚本仅使用 Python 标准库。运行：

```powershell
python scripts/validate_report.py path\to\research-report.md --require-links
```

脚本检查：

- 参考文献编号是否从 1 连续排列。
- 正文引用是否存在对应参考文献。
- 定量结论所在行是否包含引用。
- 每条参考文献是否具有相对源文件链接。
- URI 解码后的源文件是否真实存在。
- 是否残留绝对路径、`file:///` 或模板占位符。
- 主标题下是否包含 Typora 与目录结构提醒。

## Skill 目录

```text
markdown-research-report/
├─ SKILL.md
├─ README.md
├─ agents/
│  └─ openai.yaml
├─ assets/
│  └─ research-report-template.md
├─ references/
│  └─ report-spec.md
└─ scripts/
   └─ validate_report.py
```

其中：

- `SKILL.md`：Codex 执行流程与核心约束。
- `assets/research-report-template.md`：报告起始模板。
- `references/report-spec.md`：引用、链接、归档和质量规范。
- `scripts/validate_report.py`：确定性质量检查工具。

## 阅读器建议

推荐使用 Typora 打开最终报告。VS Code、部分浏览器预览器或其他 Markdown 阅读器可能将 PDF、DOCX 等文件交给外部程序，因路径编码或文件关联问题导致打开失败；这不一定表示相对路径本身无效。
