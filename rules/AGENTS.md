# Global Agent Working Agreement

These are the default working rules for all local projects. Follow higher-priority system and safety requirements and the user's current request. Project guidance may add project-specific paths, commands, and domain constraints, but should not silently expand the task.

## 1. Scope, efficiency, and stopping

- Complete the requested task with the smallest useful set of reads, edits, tool calls, and context.
- Prefer targeted inspection, minimal edits, existing utilities, and directly relevant tests.
- Do not add infrastructure, abstractions, migrations, registries, logging systems, caches, or future-facing features unless the task requires them.
- Do not turn a small request into a repository-wide cleanup, refactor, audit, or documentation campaign.
- Stop when the requested change is implemented, the directly relevant checks pass, and no concrete unresolved risk remains.
- Avoid repeated explanations, repeated file reads, full logs, full diffs, and large search output. Report conclusions and necessary evidence only.

## 2. Lean verification

Use the smallest verification that directly establishes the correctness of the requested change.

- Start with direct checks: inspect the changed location, parse the edited configuration, import or compile the affected code, confirm required fields, or inspect the key output.
- Run focused tests only when the change has executable behavior. Do not default to a full test suite for a local change.
- Broaden verification only after a failure, another change, a concrete cross-module risk, or an explicit user request.
- Once relevant checks pass, do not repeat or broaden them without new evidence.
- Do not create tests that merely mirror a reversible, low-impact implementation.

Unless the user explicitly requests it in the current task, do not create, compute, update, validate, or depend on:

- SHA, MD5, checksums, file or content fingerprints;
- checksum lists or before-and-after hash comparisons;
- manifests, artifact registries, provenance or lineage records;
- signatures, tamper-evidence systems, or duplicate integrity evidence;
- repository-wide scans intended only to prove that unrelated files did not change.

The presence of an existing hash, manifest, or artifact system does not authorize its automatic use, repair, extension, or use as a completion gate. Leave existing mechanisms unchanged unless the user asks to remove or migrate them. If a requested operation is technically hard-wired to such a mechanism, briefly identify the dependency instead of silently bypassing, fabricating, or redesigning it.

Do not verify verification evidence unless the task changes the verifier itself. Before any full-repository scan, full test matrix, or integrity audit, identify the concrete error it is expected to detect; otherwise skip it.

## 3. File and directory governance

- Treat a cohesive module with a clear responsibility and stable interface as the primary unit of organization.
- Put new work in the closest existing module. Do not create a top-level directory for a single function, one-off experiment, or temporary result.
- Before creating a file, classify it as source, configuration, test, documentation, input data, persistent output, log, cache, or temporary data, then use the project's existing location for that class.
- Keep project roots clean. Do not place temporary scripts, debug output, intermediate images, downloads, caches, or ad hoc backups in the root.
- Use an existing temporary location or the operating system's temporary directory for transient files.
- Do not create names such as `backup`, `final_v2`, or `latest_copy` as a substitute for version control.
- When moving or renaming files, update only directly affected imports, configuration paths, commands, and documentation links, then perform targeted checks.

## 4. Module and algorithm documentation

A stable module should have a concise colocated README when users or maintainers need an entry point. It should describe the module's responsibility and boundary, main files, public entry points, inputs and outputs, important dependencies, data flow, consumers, and links to deeper design documents.

Update module documentation only when responsibility, public behavior, interfaces, data contracts, dependencies, commands, or directory structure change. Internal refactoring with no maintained fact change does not require a documentation edit.

Core algorithm modules must have detailed design documentation. This includes machine-learning models, feature engineering, preprocessing, losses, training and inference strategies, sampling, probability models, coordinate or numerical algorithms, core metrics, and other logic that materially determines correctness.

Machine-learning model documentation should cover, where applicable: purpose, input and output shapes, architecture, component responsibilities, features and targets, loss, training and inference behavior, initialization and randomness, key hyperparameters, assumptions, limitations, preprocessing dependencies, and differences from baselines or related models.

Keep colocated READMEs authoritative for current module interfaces and usage. Use central documentation for cross-module architecture, research design, and extended derivations. Do not duplicate the same detailed text in both places.

## 5. Data, output, and log documentation

- Maintain documentation by stable data or product type, not by run or batch.
- Batches with the same schema, units, source semantics, and processing rules share one document.
- Data documentation should describe relevant fields, types, units, meaning, source, coordinate and time conventions, missing values, granularity, splits, preprocessing, scaling, readers, and consumers. Do not add hashes by default.
- Every persistent output type must have one discoverable type-level description covering its purpose, generation entry point, structure, fields or arrays, units, naming, upstream inputs, downstream consumers, overwrite policy, and retention or cleanup policy.
- Do not copy the same README into every output run directory. Transient caches, intermediate files, and debug artifacts do not require permanent documentation.
- Maintain one reading guide per stable log type, or one project-wide guide when the format is shared. Explain the producer, generation conditions, levels, timestamps, common fields, run identifiers, normal completion and failure signals, location, retention, and suggested troubleshooting order.

## 6. Current-state documentation

Documentation must describe the current valid state, not the sequence of past edits.

- When a requirement changes, rewrite the affected text in place as if the current design had always been intended.
- Remove obsolete assumptions, headings, examples, commands, links, conclusions, compatibility notes, and negative qualifiers created by the old design.
- Avoid patch-style language such as “new version,” “now changed,” “no longer,” or “without X” unless the absence itself is a user-relevant contract.
- Record history only in a dedicated changelog or history document when the user requests it or long-term traceability is part of the product.
- Maintain each fact in one authoritative place. Root READMEs provide navigation, colocated READMEs describe local interfaces, and central documents explain cross-cutting architecture or research.
- Do not create a work record, completion note, auxiliary README, or documentation edit merely to prove that a task was performed.
- After editing documentation, check only the affected document or section for obsolete terms, contradictions, commands, and links, then stop.

## 7. Python defaults

- Follow the existing repository style. Use `snake_case` for functions and variables, `PascalCase` for classes, and `UPPER_SNAKE_CASE` for constants unless the project specifies otherwise.
- Except for extremely short, obvious, low-value private helpers, functions and methods should have complete parameter and return type annotations and a Google-style docstring proportional to their importance and complexity.
- Public APIs and functions in core, model, data-processing, training, inference, evaluation, and other correctness-critical modules require type annotations and meaningful docstrings.
- Document relevant arguments, returns, exceptions, shapes, units, state changes, side effects, assumptions, and examples. Omit empty or inapplicable docstring sections.
- Comments should explain non-obvious decisions, invariants, boundary cases, and temporary constraints, not restate the code.
- Separate pure computation from stateful orchestration when this improves reuse, testing, or clarity. Do not mechanically convert every function into a module-level pure function or `staticmethod`.
- Use schema-driven parsing only when multiple related formats genuinely benefit from a shared engine; do not impose it on simple parsing tasks.

## 8. Complexity and file size

- Split complex or long implementations by coherent responsibility, especially when one function mixes input, validation, computation, persistence, and reporting.
- Human-maintained source files should normally remain at or below 500 physical lines. At about 400 lines, review whether a responsibility-based split would improve the design. Files over 500 lines should normally be refactored when they are newly created or materially changed.
- Do not scan or refactor the entire repository solely to enforce the line limit.
- Generated code, stable declarative tables or schemas, framework-required monolithic files, and rare cases where splitting would damage cohesion or create cyclic dependencies may exceed the limit for a concrete technical reason.
- Do not create meaningless helper files or tiny functions merely to satisfy a line count.

## 9. Completion and reporting

- Confirm that the requested implementation is complete and contains no task-scoped placeholders.
- Run only the checks proportionate to the change and report failures accurately.
- Update documentation only when a maintained current fact changed.
- In the final response, state the outcome, the directly relevant verification, and any documentation changed. Keep it concise.
