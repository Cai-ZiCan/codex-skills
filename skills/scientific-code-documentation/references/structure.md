# Structure and method examples

## Navigation levels

| Level | Contents |
|---|---|
| Project root | Brief project description, top-level directory tree, links to major-directory READMEs, brief external-data location note |
| Source directory | Purpose, module/functionality/subdirectory/README table, shared environment and source dependencies |
| Documentation directory | Stable-task/content/current-entry table, plus shared specifications and reference resources |
| Output directory | Stable-task/result-content/current-location/reading-entry table and concise retention rules |

Link real existing locations. A task index can group files that are not yet physically colocated. Do not invent planned links or move data while creating navigation. Task and output trees need not have matching empty folders. Runs and parameter branches belong below stable tasks, with shared resources referenced rather than copied.

## Default module structure

Adapt this sequence to the task; omit inapplicable material rather than creating empty headings.

1. Purpose: responsibility, upstream/downstream consumers, reproduced part of the source method.
2. Entry point: essential environment and one short invocation, with links for other modes.
3. Inputs/outputs: only algorithm-essential shapes, units, reference conventions, and missing values; link full schemas.
4. Method and implementation: the main content, ordered by computational dependency.
5. Applicability and differences: normally one short paragraph; attach detailed conditions to their steps.
6. Dependencies and references: a concise list of packages, reused source modules, and primary sources.

Keep module-specific facts in the project, not in this general skill. Adapt [Diátaxis](https://diataxis.fr/) for document responsibilities and [NumPy/SciPy](https://numpydoc.readthedocs.io/en/stable/format.html) for mathematical notes and references. They do not themselves supply a paper-to-code correspondence standard.

## Example: a discrete derivative

State the implemented expression $s_i=(h_{i+1}-h_i)/d_i$. Identify the linked routine, map $h$ to its input height array and $d$ to the computed distance, specify units, and identify where the result is located. Describe adjacency and missing-value rules only if the actual routine imposes them. If uncertainty is propagated under independence, state that assumption beside the variance expression.

If a later method uses the negative derivative, explain that conversion where it occurs. A numerical equivalence or sign convention is not evidence that the paper's authors used the same internal implementation.

## Example: a solver or local threshold

Present a weighted least-squares objective and map the observation vector, design matrix, and weights to code. Explain whether the implementation uses QR, SVD, or explicit small-matrix expressions. Put rank checks, conditioning limits, and fallback behavior here. Label a default threshold as a local setting unless its source is confirmed.

Useful details answer “what quantity is computed, where, how, and under which conditions.” Result tables, test outcomes, benchmark rankings, and scientific conclusions belong in reports.
