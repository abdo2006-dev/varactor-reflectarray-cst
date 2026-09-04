# Initial repository and report brief

Date: 2026-09-04
Tool: Claude Code

This file records the operative constraints given for the first build of this
repository. It is a record of instructions, not of results.

## Role and task

Act as technical-report engineer and repository maintainer for an undergraduate
Electrical and Computer Engineering CST microwave project. Create the repository
and begin a professor-facing and recruiter-facing technical report on a
varactor-loaded multilayer reflectarray metasurface unit cell around 26 GHz.

## Evidence discipline

The report must stay grounded in supplied project evidence and must keep the
following categories distinct: confirmed geometry and configuration; confirmed
numerical results; confirmed electromagnetic observations; approximate
screenshot observations; reconstruction assumptions; rejected diagnostic
hypotheses; current engineering hypotheses; unfinished work; planned
experiments.

Hard prohibitions:

- Never turn an assumption into a fact.
- Never turn a planned experiment into a completed result.
- Never claim successful tunability unless supplied simulation evidence
  demonstrates it.
- Never imply hardware fabrication or measurement.
- Never fabricate references. Use `[CITATION REQUIRED, ...]` markers instead.

Where the historical continuity plan conflicts with a later entry or with the
current project delta, the newest explicit evidence wins.

## Authoritative delta at the time of this build

Current controlled geometry: `lineV = 1.13 mm`, `slotW = 0.35 mm`,
`slotL = 2.32 mm`. Capacitance endpoints 0.025 pF and 0.19 pF. Reference
frequency 26.104 GHz. Simulated interval approximately 25.6 to 26.6 GHz.

Both endpoint simulations satisfy the approximately 0.01 adaptive-mesh
convergence criterion. The endpoint reflection-phase curves remain almost
coincident near 26.104 GHz, with some additional separation near approximately
26.5 to 26.6 GHz. The `slotL = 2.32 mm` test did not produce target-frequency
tuning.

Current hypothesis: the stronger capacitance-sensitive region may lie above the
current 26.6 GHz simulation boundary. This is a hypothesis, not a confirmed
fact.

Next planned experiment: a wider-frequency endpoint diagnostic on the same
geometry, before any further geometry modification. The exact wider sweep limits
have not been finalised or run and must not be invented.

## Report constraints

Working title: "Reconstruction, Bias-Network Integration, and Electromagnetic
Evaluation of a Varactor-Loaded 26 GHz Reflectarray Unit Cell". The title must
not promise demonstrated wide-range phase tunability.

Anti-redundancy: each major fact has one primary location. Methodology explains
how simulations were performed, Results reports what was observed,
Interpretation explains what the results mean, Limitations explains what the
model cannot establish, and Next Experimental Work explains what will be tested
next. Cross-reference rather than repeat, and do not end every subsection with a
miniature conclusion.

Writing: precise technical prose, active voice where natural, consistent
terminology, variables defined once. Avoid inflated words such as
"groundbreaking", "crucial", "pivotal", "remarkable", "showcases",
"underscores", "plays a vital role" and "it is important to note" unless
technically required. Do not force ideas into groups of three. Do not write
generic paragraph endings; state the actual engineering consequence instead.

Keep the abstract, the interpretation wording and the conclusion explicitly
provisional. Draft the stable sections now rather than leaving them empty
because simulations are continuing.

Figures: roughly 6 to 9 strong main-text figures, not a wall of raw screenshots.
Every figure carries a number, a precise caption, the parameter configuration,
the capacitance and frequency where relevant, and the source result file. A
graph with `Pass` on its horizontal axis is a convergence plot and is never
called a frequency response.

## Repository constraints

Private repository named `varactor-reflectarray-cst`. Do not commit solver
caches, temporary mesh files, large generated result directories, virtual
machine files or CST backups. Do not commit licensed software components or
source-paper PDFs without permission. Explain the large-file policy in
`cst/README.md` and use Git LFS if `.cst` files are ever committed.

The README is recruiter-facing but technically honest, significantly shorter
than the report, and must not advertise successful tuning.

## Final passes required

Apply an anti-redundancy editing pass, then apply the Humanizer skill principles
conservatively as a final editing pass on drafted prose. The Humanizer must not
change scientific meaning: it may not add data, add citations, invent
explanations, strengthen conclusions, remove technical qualifications, or
convert hypotheses into findings. After the pass, re-audit every claim against
the supplied evidence, and search the repository for unsupported language such
as "successful tuning", "optimized", "reproduced", "demonstrated tunability",
"360 degrees" and "resonance above 26.6".

Do not make additional CST design decisions, invent new simulation results, or
start the wider-frequency simulation. This task is documentation and repository
creation only.
