# Varactor-loaded 26 GHz reflectarray unit cell

A full-wave CST reconstruction of a varactor-tuned, six-layer reflectarray unit
cell for K-band operation near 26 GHz, and an investigation into why the
reconstructed element does not reproduce the capacitance-dependent phase
response its reference design reports.

Simulation only. No hardware was fabricated and no measurement was made.

## Read the report

- [Working draft, PDF](deliverables/Varactor_Reflectarray_CST_Report_Working_Draft.pdf)
- [Working draft, DOCX](deliverables/Varactor_Reflectarray_CST_Report_Working_Draft.docx)

A working engineering document, not a finished thesis. The main text is kept
short while the investigation is open; the detailed branch history sits in the
appendices and in `docs/experiment_log.md`. The abstract and conclusion will be
written once the electromagnetic characterisation is complete.

## The engineering problem

A reconfigurable reflectarray steers a beam by controlling the reflection phase
of each element in a periodic surface. At millimetre-wave frequencies that
usually means loading a resonant element with a varactor diode, so a DC bias
shifts the resonance and therefore the reflected phase.

The element has to do two things at once. It must present a strong,
controllable resonance to the incident field, and it must carry DC bias to every
diode without letting the bias network disturb the RF path. The reference design
solves both by burying the resonator between the slot layer and the ground
plane, putting the diode behind the ground plane, reaching it through a blind
via, and feeding it through a bias-T made from a quarter-wave line and a radial
stub.

Rebuilding that element from published dimensions is the problem this project
took on.

## Current architecture

Six conductor layers on five substrates, in a 7 mm by 7 mm periodic cell:

| Layer | Function |
|---|---|
| L1 | Patch, receives the incident field |
| L2 | Slot layer, couples into the resonator |
| L3 | Stripline resonator and bias-T branch |
| L4 | Ground, with a clearance for the blind via |
| L5 | Bias-voltage supply routing |
| L6 | Varactor terminals and local routing |

A blind via carries the RF node from the Layer-3 stripline through the ground
clearance down to a Layer-6 terminal pad. An ideal lumped capacitor bridges the
gap to a second, isolated pad, which the Layer-5 bias routing reaches through a
local interlayer via.

*[Figure placeholder: plan view of the four RF layers]*

*[Figure placeholder: six-layer stack, side or exploded view]*

*[Figure placeholder: bias network detail, blind via and varactor terminals]*

## Skills demonstrated

Parametric electromagnetic modelling in CST Studio Suite 2023: multilayer PCB
geometry driven entirely by named parameters and formulas, Boolean construction
with a replayable history, and interlayer features built and verified one at a
time.

Periodic-structure simulation: unit-cell boundaries with Floquet port
excitation, propagating mode identification, and co-polarised reflection
extraction at normal incidence.

Numerical verification rather than assumed correctness: adaptive tetrahedral
refinement with an explicit acceptance criterion, energy balance checks, and
broadband interpolation error checks, applied before any result is interpreted.

Component-level validation: confirming that a lumped tuning element is actually
excited by the RF solution, by comparing its monitored terminal impedance
against ideal capacitive reactance.

Structured debugging of a negative result: five candidate explanations
formulated from source material, each isolated into its own model branch, each
tested with a converged endpoint pair, and each recorded with its evidence
whether it succeeded or not.

Reproducible technical documentation: a claims ledger separating confirmed
results from assumptions, hypotheses and planned work; an experiment log; and a
figure manifest that fixes each caption to its source configuration.

## Numerical verification approach

Nothing is interpreted until it converges. A run is accepted for comparison only
when the adaptive tetrahedral refinement drives the maximum change in all
S-parameters between passes to approximately 0.01 or below, with a minimum of 3
and a maximum of 8 passes.

That threshold is deliberately tight for the comparison being made. The quantity
under test is a phase difference between two capacitance states that has
repeatedly turned out to be of the order of a degree, so a numerical uncertainty
of similar size would make the comparison meaningless. Runs that miss the
criterion are re-refined, not interpreted, and two are recorded in the report as
having been rejected on those grounds.

Mesh reuse follows the same logic. When only the capacitance changes, the
converged mesh is reused so the endpoint pair is a genuine one-variable
experiment. When geometry changes, the mesh is rebuilt.

## Current findings

The reconstruction is dimensionally faithful. Every dimension the reference
design publishes, twelve in total, is reproduced exactly by the model, checked
directly against the source paper's dimension table rather than against notes.

The model is numerically sound. Accepted runs meet the convergence criterion,
broadband interpolation error is negligible, and energy balance stays close to
unity across most of the simulated interval.

The tuning element is electrically valid. Its monitored terminal impedance near
26.1 GHz is approximately 33 ohm at 0.19 pF against an ideal capacitive
reactance of approximately 32 ohm, and approximately 240 to 245 ohm at 0.025 pF
against approximately 244 ohm. The element is excited, is not shorted across its
terminal gap, and responds to the capacitance parameter.

Numerically converged endpoint simulations currently show limited
capacitance-dependent phase separation near the 26.104 GHz reference frequency.
Ongoing work is focused on locating the capacitance-sensitive region and
identifying the remaining discrepancy between the reconstructed model and the
intended tuning response.

Five candidate explanations have been tested and rejected with converged
endpoint pairs: a simplified baseline topology, a truncated stripline below the
via, a missing Layer-5 reference plane, the layer assignment and routing of the
bias network, and an alternative blind-via anchor coordinate.

## Current limitation

The reconstruction depends on several dimensions the published material does not
provide: the blind-via and ground-clearance diameters, the lower copper
thicknesses, the varactor land pattern, and the local interlayer DC connection.
Each is currently a documented project assumption, and none has been
sensitivity-tested. Until they are bounded, the model cannot distinguish an
underdetermined source from an undiscovered reconstruction error.

The tuning element is also an ideal capacitor with no series resistance, no
package inductance and no bias characteristic, so the model cannot predict
achievable phase range or loss for a physical device.

## Repository structure

```
deliverables/            the DOCX and PDF report, the documents meant for readers
docs/
  project_state.md       current geometry, result, hypothesis, next experiment
  experiment_log.md      one entry per controlled experiment or model branch
  claims_ledger.md       every claim with its evidence, precision and status
  figure_manifest.md     required figures with captions and source configuration
tools/report_build/
  report_content.py      the report text, as structured data
  build_docx.py          renders it to a styled, editable DOCX
  build_markdown.py      renders the Markdown mirror
  build.sh               two-pass build of both deliverables
report/
  report_working_draft.md  generated Markdown mirror, for readable diffs
figures/
  source/                figures reproduced from the CC BY source papers
  cst/                   CST captures and exports, as they become available
results/                 raw and processed numerical exports
cst/                     how the CST checkpoint files are handled
references/              source list and citation TODO
archive/                 the longform revision that preceded the restructure
prompts/claude_code/     prompts used while building this repository
```

Edit `tools/report_build/report_content.py`, then run
`tools/report_build/build.sh` to regenerate the DOCX, the PDF and the Markdown
mirror together.

## Project status

Active investigation. The report is a working draft. Its abstract is a marked
placeholder and its closing section is an interim status rather than a
conclusion; both will be written once the investigation reaches a result.

Every dimension the reference design publishes is reproduced exactly by the
model, verified directly against the source papers. What has not been recovered
is the capacitance-dependent phase behaviour those papers report.

The next experiment is a wider-frequency endpoint diagnostic on unchanged
geometry, to test whether the capacitance-sensitive region lies above the
present 26.6 GHz upper simulation boundary. No result exists above that
boundary.

See `docs/project_state.md` for the authoritative current state and
`docs/claims_ledger.md` for what the evidence does and does not support.
