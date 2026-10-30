---
name: scientific-code-documentation
description: Write or restructure READMEs for scientific code projects, including project/directory navigation and module explanations mapping equations, symbols, code, and applicability conditions. Use for 科研代码说明, 论文复现文档, and hierarchical README design; not for manuscript drafting, literature reviews, or experiment reports.
---

# Scientific Code Documentation

Choose the document level first. Project and major-directory READMEs provide concise navigation; module READMEs explain how scientific methods are implemented. In module explanations, keep usage and data summaries brief and give the main space to equations, variable mappings, implementation choices, and conditions. Follow the project's documentation contract and the user's requested depth. See [structure and method examples](references/structure.md) when designing or restructuring a document.

## Route by document level

For a project root, describe the project briefly, show the top-level structure, and link the major-directory READMEs. A source-directory index lists implemented modules and their module READMEs; it can hold shared environment and external-source dependency details. Documentation and output indexes group existing entries by stable task, using a concise table of purpose, current location, and reading entry point. Do not insert module equations, duplicate interfaces, or summarize experimental conclusions into navigation pages.

Inspect current files before linking. Use actual paths when a task has no dedicated folder; do not present planned folders as current or create empty symmetric trees. Keep cycles, cruises, runs, and parameter branches within stable tasks rather than creating per-run READMEs. Link shared resources from one maintained location. Navigation work does not authorize moving files or changing executable paths.

## Ground the explanation

For module explanations, read the relevant module, public entry points, numerical routines, and existing method documentation. Consult the primary paper or official specification for formula provenance. Existing notes are leads, not a substitute for checking disputed or newly asserted formulas. If primary evidence is unavailable, qualify the affected attribution; do not invent equation numbers or present a local choice as the author's method. Navigation-only work needs targeted inspection of directory contents and existing entry points, not a fresh review of scientific methods.

Separate source facts: code determines current executable behavior; the paper determines published methods and assumptions; neither silently overrides the other. Documentation work does not authorize fixing algorithms or rerunning experiments.

## Connect mathematics to implementation

For each consequential computational step, explain the source equation, actual computation, symbol-to-variable correspondence, relevant units/shapes/signs, and exact function in a linked source file. Include discretization and solver choices when they change interpretation. Use function names as durable locators rather than relying on line numbers alone.

Place validity checks, thresholds, degeneracies, singularities, missing-data behavior, and failure handling beside the step they affect. Distinguish published requirements, equivalent transformations, numerical approximations, and local choices. Do not mechanically give every step a table or narrate every source line.

## Keep documents focused

Use the module README as the entry point for current method behavior. Keep long derivations, full schemas, service configuration, and experiment findings in their appropriate existing documents; add a focused reference only if needed to retain useful detail. Update affected links when relocating content, and maintain each fact in one authoritative place.

Do not add experiment results, accuracy rankings, or validation-report chapters to implementation READMEs. Preserve existing code docstring conventions. Document reused external source dependencies with their location, caller, purpose, and configuration; do not vendor them merely to make documentation self-contained.

## Finish proportionately

For navigation, check descriptions and links to actual modules, documents, directories, and reports. For changed method explanations, check formulas, symbol mappings, signatures/defaults, branch conditions, and citations against their sources. Existing tests may help interpret behavior but do not belong as a mandatory README section. Do not create a test suite or rerun scientific processing for a documentation-only change. Remove empty sections and scaffold placeholders. Report changed documentation and any remaining source uncertainty concisely.
