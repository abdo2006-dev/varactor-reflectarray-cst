# Varactor-tuned 26 GHz reflectarray unit cell — CST reconstruction

A full-wave CST reconstruction of a varactor-tuned, six-layer reflectarray unit
cell for K-band operation near 26 GHz, and an open investigation into why its
tunable resonance does not sit where the reference design puts it.

The current reconstruction shows capacitance-dependent resonant behaviour, but
the tunable resonant region is displaced above the intended 26.104 GHz operating
point.

**Status: in progress.** Simulation only. No hardware was fabricated and no
measurement was made. The published tuning at 26.104 GHz has **not** been
reproduced. What has been established, and what has not, is set out below and
recorded claim by claim in [`docs/claims_ledger.md`](docs/claims_ledger.md).

---

## 1. The published device

A reconfigurable reflectarray steers a beam by controlling the reflection phase
of each element in a periodic surface. At millimetre-wave frequencies that
usually means loading a resonant element with a varactor diode, so a DC bias
shifts the resonance and therefore the reflected phase.

The element has to do two things at once. It must present a strong, controllable
resonance to the incident field, and it must carry DC bias to every diode
without letting the bias network disturb the RF path. The reference design
solves both by burying the resonator between the slot layer and the ground
plane, putting the diode behind the ground plane, reaching it through a blind
via, and feeding it through a bias-T made from a quarter-wave line and a radial
stub.

![Published unit-cell layout](figures/source/fig01_harz2022_element_layout.png)

*Published reference unit-cell layout from Harz et al., reproduced under
CC BY 4.0.* Harz and Kleine-Ostmann [2], Fig. 1, doi:
[10.5194/ars-19-215-2022](https://doi.org/10.5194/ars-19-215-2022).
*The unit-cell extent X and Y, the patch width Pw,
the coupling slot Sw and Sl, the stripline width Lw with its two resonant
lengths Lv and Ls, the blind via, the varactor position, and the bias line with
its radial stub dimensioned by Bl, Bd, Bw and Bh.*

![Published six-layer architecture](figures/source/fig02_harz2022_layer_structure.png)

*Published six-layer architecture from Harz et al., reproduced under
CC BY 4.0.* Harz and Kleine-Ostmann [2], Fig. 2, doi:
[10.5194/ars-19-215-2022](https://doi.org/10.5194/ars-19-215-2022).
*The patch sits on layer one, the coupling aperture
is the gap in the layer-two conductor, the resonant stripline is on layer three,
layer four is the ground plane, and the blind via carries the resonant path down
to the varactor on layer six.*

Both source papers are open access under the Creative Commons Attribution 4.0
licence, verified from page 1 of each publisher PDF. See
[`figures/source/ATTRIBUTION.md`](figures/source/ATTRIBUTION.md).

## 2. What I reconstructed

The model reconstructs the six-layer published architecture in CST Studio Suite
2023 as a 7 mm by 7 mm periodic unit cell. Published dimensions were used where
available; dimensions not reported by the paper are tracked explicitly as
reconstruction assumptions in [`docs/claims_ledger.md`](docs/claims_ledger.md),
CL-A1 to CL-A8.

<!-- FIGURES-MODEL-START -->
<!-- FIGURES-MODEL-END -->

| Layer | Function |
|---|---|
| L1 | Patch, receives the incident field |
| L2 | Slot layer, couples into the resonator |
| L3 | Stripline resonator and bias-T branch |
| L4 | Ground, with a clearance for the blind via |
| L5 | Bias-voltage supply routing |
| L6 | Varactor terminals and local routing |

A blind via carries the RF node from the layer-3 stripline through the ground
clearance down to a layer-6 terminal pad. An ideal lumped capacitor bridges the
gap to a second, isolated pad, which the layer-5 bias routing reaches through a
local interlayer via.

## 3. How it should work

    varactor capacitance
      -> loading of the buried stripline resonator
      -> shift of the element resonance
      -> change in the phase of the reflected wave

Build an array of these and a per-element control voltage steers the beam. The
source reports a simulated phase shift of 337 degrees for this element and a
measured phase-change range of 322 degrees at 26.104 GHz in a waveguide
simulator at 21.4 degrees incidence. Those two figures are not directly
comparable with each other, and neither is a result of this project — they are
the targets it is working toward.

## 4. Current model parameters

The geometry of the current endpoint pair, runs 17 and 18. The two runs share
one geometry and differ only in `varC`.

| Parameter | Meaning | Published | Runs 17 / 18 |
|---|---|---:|---:|
| `patchW` | square patch width | 2.225 mm (Pw) | 2.30 mm |
| `slotW` | coupling-slot width | 0.26 mm (Sw) | 0.35 mm |
| `slotL` | coupling-slot length | 2.275 mm (Sl) | 2.32 mm |
| `lineV` | resonant stripline length below the via | 1.11 mm (Lv) | 1.13 mm |
| `varC` | varactor capacitance | — | 0.19 pF (run 17) / 0.025 pF (run 18) |

**These are diagnostic settings, not optimised dimensions, and not a claim of
exact reproduction of the published geometry.** Four published dimensions,
including the patch width, are deliberately displaced from their published
values as part of the sensitivity sequence in
[`docs/experiment_log.md`](docs/experiment_log.md); the displacement is a
diagnostic deviation, not a correction to the source. The reconstruction
baseline reproduces all eleven published dimensions exactly (CL-S3). The full
inventory of every named parameter, with its published value, its current value
and its origin, is Appendix A of the report.

## 5. What is verified

- **The numerical solution is converged.** A run is accepted for comparison only
  when adaptive tetrahedral refinement drives the maximum change in all
  S-parameters between passes to approximately 0.01 or below. Runs that miss the
  criterion are re-refined, not interpreted, and two are recorded as rejected on
  those grounds. When only the capacitance changes the converged mesh is reused,
  so an endpoint pair is a genuine one-variable experiment.
- **The tuning element is electrically active.** Its monitored terminal
  impedance near 26.1 GHz is about 33 ohm at 0.19 pF against an ideal capacitive
  reactance of about 32 ohm, and about 240 to 245 ohm at 0.025 pF against about
  244 ohm. The element is excited, is not shorted across its terminal gap, and
  responds to the capacitance parameter. This validates the component, not the
  circuit around it.
- **The varactor reaches the resonance of the whole cell.** Over a widened
  sweep, changing the capacitance moves a resonant feature of the complete unit
  cell — see §6. This is the stronger statement, and it is new.
- **Connectivity and topology.** The blind via connects the layers it should and
  is isolated through the ground-plane clearance, RF and DC routes are separated
  as intended, and the via divides the stripline into the two published resonant
  lengths.

## 6. Current result

The endpoint pair was first run over the 25.6 to 26.6 GHz interval inherited
from the source measurement, where the two capacitance states produced almost
coincident phase curves. That interval was the source's choice, not one selected
to find this element's capacitance-sensitive region, so the pair was re-run on
unchanged geometry over approximately **25.5 to 28 GHz** (runs 17 and 18).

<!-- FIGURES-RESULTS-START -->
<!-- FIGURES-RESULTS-END -->

**What the wider sweep shows.** Near the intended 26.104 GHz operating frequency
the two endpoint responses remain close. But a **capacitance-sensitive resonant
region appears near 26.8 GHz**: changing `varC` shifts the magnitude dip and the
rapid phase transition that goes with it. The varactor is therefore influencing
the electromagnetic resonance of the complete unit cell, which the terminal
impedance check alone could not establish.

**What it does not show.** The tunable resonance is displaced above the intended
operating point, so **the published tuning at 26.104 GHz has not been
reproduced**. And no tuning range in degrees is claimed here: the phase CST
displays wraps at plus or minus 180 degrees, so no 300-degree-class figure can
be read from these plots. The sweep also extends past the Astra MT77 material
fit range declared in the model, 25.6 to 26.6 GHz, so the 26.8 GHz region is a
diagnostic indication of where the feature sits rather than a quantitative
prediction.

## 7. What is unresolved

Why the capacitance-sensitive feature sits near 26.8 GHz rather than at
26.104 GHz. The candidates are the unpublished dimensions the reconstruction had
to assume, the four published dimensions currently displaced by the diagnostic
sequence, weak aperture coupling into the resonator, and the ideal-capacitor
representation of the varactor. **None is established and they are not ranked.**

The reconstruction also depends on quantities the published material does not
provide: the blind-via and ground-clearance diameters, the lower copper
thicknesses, the varactor land pattern, and the local interlayer DC connection.
Each is a documented assumption and none has been sensitivity-tested. The tuning
element is an ideal capacitor with no series resistance, no package inductance
and no bias characteristic, so the model cannot predict achievable phase range
or loss for a physical device.

## 8. What was already tested

Each branch changed one thing, ran to convergence, and was recorded with its
outcome — including the failures, so the same idea is not retried. Rejected with
converged endpoint pairs: a simplified baseline topology; a truncated stripline
below the via; a missing layer-5 reference plane; two readings of the bias
network's layer assignment and routing; two interpretations of the radial-stub
dimensions and orientation; and an alternative blind-via anchor coordinate.
Single-parameter adjustments to the slot width, the stripline length and the
slot length were tried in sequence and none recovered tuning at the reference
frequency.

None of these establishes that the feature it changed is electrically
unimportant. Full record: [`docs/experiment_log.md`](docs/experiment_log.md) and
[`docs/claims_ledger.md`](docs/claims_ledger.md) CL-R1 to CL-R7.

## 9. What comes next

1. **Numerical export** of the complex S-parameter data for both endpoints over
   the wide interval, replacing plot reading with exported values.
2. **Phase unwrapping**, then a phase-difference calculation between the two
   capacitance states **at matched frequencies**, so the tuning can finally be
   stated in degrees at a stated frequency.
3. **Re-declaration of the Astra MT77 material fit range** to cover the widened
   sweep, before any quantitative value is taken from the 26.8 GHz region.
4. **Targeted tests of the reconstruction hypotheses**, starting with a
   sensitivity test of the assumed via and ground-clearance dimensions, then a
   field-monitor comparison between the two capacitance states, then returning
   the displaced published dimensions one at a time.

## 10. Repository structure

```
docs/
  project_state.md       current geometry, result, hypothesis, next experiment
  experiment_log.md      one entry per controlled experiment or model branch
  claims_ledger.md       every claim with its evidence, precision and status
  figure_manifest.md     every report figure with its caption and configuration
report/
  report_working_draft.md  generated Markdown mirror of the report
deliverables/            the report as DOCX and PDF
tools/report_build/      reproducible two-pass report build
figures/
  source/                figures reproduced from the source papers, CC BY 4.0
  model/                 views of the CST reconstruction
  results/               simulated reflection response
cst/                     how the CST checkpoint files are handled
references/              source list and citation status
results/                 raw and processed numerical exports
archive/                 the superseded first revision of the report, in full
```

The report's single source of truth is `tools/report_build/report_content.py`.
Edit it, then run `tools/report_build/build.sh` to regenerate the DOCX, the PDF,
the Markdown mirror and the figure manifest together, so captions and numbering
cannot drift from the results they describe.

## 11. Sources

[1] J. Huang and J. A. Encinar, *Reflectarray Antennas*. New York, NY, USA:
Wiley-IEEE Press, 2008, doi: [10.1002/9780470178775](https://doi.org/10.1002/9780470178775).

[2] T. Harz and T. Kleine-Ostmann, "Measurement and optimization of a
continuously tunable 10 x 10 reflectarray antenna for 5G metrology in the
K-band," *Advances in Radio Science*, vol. 19, pp. 215–220, 2022,
doi: [10.5194/ars-19-215-2022](https://doi.org/10.5194/ars-19-215-2022).
Open access, CC BY 4.0.

[3] T. Harz, T. Kleine-Ostmann, and T. Schrader, "Design of a continuously
tunable reflectarray element for 5G metrology in the k-band," *Advances in Radio
Science*, vol. 18, pp. 1–5, 2020,
doi: [10.5194/ars-18-1-2020](https://doi.org/10.5194/ars-18-1-2020).
Open access, CC BY 4.0.

The source PDFs are not committed to this repository. Figures reproduced from
[2] carry their attribution in
[`figures/source/ATTRIBUTION.md`](figures/source/ATTRIBUTION.md).

## 12. Notes on this repository

The code and documentation here are MIT licensed; see [`LICENSE`](LICENSE).
Reproduced source figures remain under CC BY 4.0 and are attributed as such.

The report and this documentation were drafted with AI assistance. Every
technical statement derives from the CST model or from the cited papers, and
[`docs/claims_ledger.md`](docs/claims_ledger.md) records the evidence and
status of each.
