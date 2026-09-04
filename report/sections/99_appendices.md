## Appendix A. Parameter table

Every value is marked with its origin: `published` for a value from the source
design, `derived` for a value computed from published values by a formula in the
model, `inferred` for a value read from a published figure rather than a table,
and `assumed` for a value chosen by this project because the source does not
give it.

### A.1 Cell and stack

| Parameter | Value | Origin |
|---|---:|---|
| `cellX`, `cellY` | 7 mm | published |
| `sub1`, `sub2`, `sub3` | 0.254 mm | published |
| `sub4`, `sub5` | 0.127 mm | published |
| `cuOuter` | 0.035 mm | inferred from the source layer stack, not re-verified |
| `cuInner` | 0.018 mm | inferred from the source layer stack, not re-verified |
| `epsAstra` | 3 | substrate material specification |
| `tanDAstra` | 0.0017 | substrate material specification |
| `fRef` | 26.104 GHz | published |

### A.2 Reflecting structure

| Parameter | Baseline | Current | Origin |
|---|---:|---:|---|
| `patchW` | 2.225 mm | 2.225 mm | published |
| `slotW` | 0.26 mm | 0.35 mm | published baseline, current value chosen for the sensitivity study |
| `slotL` | 2.275 mm | 2.32 mm | published baseline, current value chosen for the sensitivity study |
| `lineW` | 0.33 mm | 0.33 mm | published |
| `lineV` | 1.11 mm | 1.13 mm | published baseline, current value chosen for the sensitivity study |
| `lineS` | 0.20 mm | 0.20 mm | published |

The three current values are project test points, not published dimensions. See
Section 6.4.

### A.3 Layer z coordinates

Every level is derived from the substrate and copper thicknesses.

| Parameter | Formula | Value (mm) |
|---|---|---:|
| `zPatchBottom` | 0 | 0 |
| `zPatchTop` | `zPatchBottom + cuOuter` | +0.035 |
| `zL2Top` | `-sub1` | -0.254 |
| `zL2Bottom` | `zL2Top - cuOuter` | -0.289 |
| `zL3Top` | `zL2Bottom - sub2` | -0.543 |
| `zL3Bottom` | `zL3Top - cuInner` | -0.561 |
| `zL4Top` | `zL3Bottom - sub3` | -0.815 |
| `zL4Bottom` | `zL4Top - cuInner` | -0.833 |
| `zL5Top` | `zL4Bottom - sub4` | -0.960 |
| `zL5Bottom` | `zL5Top - cuOuter` | -0.995 |
| `zL6Top` | `zL5Bottom - sub5` | -1.122 |
| `zL6Bottom` | `zL6Top - cuOuter` | -1.157 |

The `cuOuter` thickness on Layers 5 and 6 is assumed, not confirmed. See
Section 9.1.

### A.4 Blind via and clearance

| Parameter | Value | Origin |
|---|---:|---|
| `viaX` | 0 | derived, on the stripline centreline |
| `viaY` | 0 | derived, the junction that divides the stripline into `Lv` and `Ls` |
| `viaZtop` | `zL3Bottom` = -0.561 mm | derived |
| `viaZbottom` | `zL6Top` = -1.122 mm | derived |
| `viaD` | 0.20 mm | assumed |
| `viaClearD` | 0.50 mm | assumed |

### A.5 Bias-T

| Parameter | Value | Origin |
|---|---:|---|
| `Bl` | 0.25 mm | published, bias-line width |
| `Bd` | 1.6 mm | published, offset from the junction to the stub apex |
| `Bw` | 1.3 mm | published, radial-stub half-span |
| `Bh` | 1.13 mm | published, horizontal offset to the chord endpoint line |
| `stubR` | `sqrt(Bh^2 + Bw^2)` = 1.7225 mm | derived from the figure interpretation in Section 5.4 |
| `stubHalfAng` | `atan(Bw/Bh)` = 49.0018 deg | derived |
| Branch direction | +x | assumed, mirror convention |

The mapping of `Bw` and `Bh` onto the sector profile is inferred from the
published figure, not stated in the source text. An earlier interpretation using
`stubR = Bh` and a half-chord of `Bw/2` was rejected. See Appendix D.

### A.6 Varactor

| Parameter | Value | Origin |
|---|---:|---|
| `capY` | `-lineV + lineW/2` | derived. The varactor terminal-pair centre |
| `varPadW` | 0.2155 mm | assumed, from the MACOM package outline |
| `varPadL` | 0.1905 mm | assumed, from the MACOM package outline |
| `varTermSep` | 0.4185 mm | assumed, from the MACOM package outline |
| Terminal gap | 0.228 mm | derived from the pad geometry |
| `Cmin` | 0.025 pF | varactor tuning range, confirm against the source |
| `Cmax` | 0.19 pF | varactor tuning range, confirm against the source |
| `varC` baseline | 0.10 pF | chosen midpoint for the baseline runs |
| `R`, `L` | 0, 0 | modelling simplification |

---

## Appendix B. Solver configuration

| Setting | Value |
|---|---|
| Package | CST Studio Suite 2023, university Teaching License |
| Solver | Frequency domain, general purpose |
| Mesh | Tetrahedral, adaptive refinement |
| Sweep | Broadband, with interpolation |
| Frequency interval | approximately 25.6 to 26.6 GHz |
| Xmin, Xmax, Ymin, Ymax | Unit cell |
| Zmin, Zmax | Open, add space |
| Excitation | Floquet ports, normal incidence |
| `theta`, `phi` | 0, 0 |
| Propagating Floquet modes | 2: TE(0,0) and TM(0,0) |
| Reflection term used | `SZmax(1),Zmax(1)` |
| Adaptive minimum passes | 3 |
| Adaptive maximum passes | 8 |
| Adaptive criterion | `All S-Parameters` threshold approximately 0.01 |
| Lumped-element monitors | Voltage and current enabled on `StageB_Ideal_Varactor` |
| Field monitors | E-field magnitude and surface current density at 26.104 GHz |

Mesh reuse follows the rule in Section 4.2: reuse when only `varC` changes,
rebuild when geometry changes.

Host environment: MacBook Pro with 16 GB RAM, running CST inside a Windows 11
ARM virtual machine with roughly 6 to 8 GB available to the solver. This
constrains the model to a single periodic unit cell and rules out large
full-wave array simulations.

---

## Appendix C. Additional convergence evidence

Final `Maximum Delta All S-Parameters` for each run used in the report. The
acceptance criterion is approximately 0.01. Values are as reported by the
adaptive refinement.

| Run | Geometry | `varC` | Final delta | Accepted |
|---|---|---:|---:|---|
| Stage-A baseline | Stage A | 0.10 pF | approx. 0.008 | yes |
| Stage-B first solve | Stage B | 0.10 pF | approx. 0.0119 at pass 3 | no, refined further |
| Stage-B baseline | Stage B | 0.10 pF | approx. 0.0089 at pass 6 | yes |
| Stage-B endpoint high | Stage B | 0.19 pF | approx. 0.009 at pass 6 | yes |
| Stage-B endpoint low, first attempt | Stage B | 0.025 pF | approx. 0.0138 at pass 5 | no, refined further |
| Stage-B endpoint low, refined | Stage B | 0.025 pF | below 0.01 | yes |
| Layer-3 termination | v014 | 0.025 pF | approx. 0.0089 | yes |
| Layer-3 termination | v014 | 0.19 pF | approx. 0.0093 | yes |
| Layer-5 reference plane | v015 | 0.025 pF | approx. 0.0098 to 0.010 | yes, borderline |
| Layer-5 reference plane | v015 | 0.19 pF | approx. 0.0087 | yes |
| Source-topology rebuild | v017 | 0.025 pF | approx. 0.0094 | yes |
| Source-topology rebuild | v017 | 0.19 pF | approx. 0.007 | yes |
| Current geometry | `slotL = 2.32` | 0.025 pF | meets the criterion, value not individually recorded | yes |
| Current geometry | `slotL = 2.32` | 0.19 pF | meets the criterion, value not individually recorded | yes |

Two entries above document runs that were rejected on convergence grounds and
re-refined rather than interpreted. The Stage-B first solve stopped at 0.0119 on
a looser active threshold, and the first low-capacitance endpoint attempt rose
to about 0.041 at pass 4 before falling to about 0.0138 at pass 5, which is why
it was continued rather than accepted.

Energy balance was checked alongside convergence. In the Stage-A baseline it was
approximately 0.994 on `Zmax(1)` and approximately 0.9998 on `Zmax(2)` near
26.104 GHz. In the Stage-B baseline it was approximately 0.995 near the
reference frequency, falling to approximately 0.983 at 26.6 GHz.

*[Appendix figure C.1 placeholder: per-branch adaptive-convergence plots. Each
has `Pass` on the horizontal axis and is a convergence record, not a frequency
response.]*

---

## Appendix D. Geometry development and rejected diagnostic variants

Each entry records a version of the model that was built or specified and then
set aside. They are kept so that the same idea is not retried without new
evidence.

### D.1 Stage-A stripline-to-ground capacitor

The tuning capacitor was placed directly between the underside of the Layer-3
stripline and the top of the Layer-4 ground. Rejected because the published
network routes the RF node through a blind via to a diode behind the ground
plane, with the bias-T branching from the RF junction. Endpoint phase change
across the full capacitance range was of the order of a few degrees.

### D.2 Radial stub with `stubR = Bh` and half-chord `Bw/2`

Built as a curve, never extruded. Superseded by a re-reading of the published
figure in which `Bh` is a horizontal offset and `Bw` a half-span, giving
`stubR = sqrt(Bh^2 + Bw^2)`.

### D.3 Radial stub opening along negative y

Built as a curve, never extruded. Superseded by the published top view, which
shows the stub branching laterally from the bias line. The corrected sector
opens toward +x.

### D.4 Bias-T on Layer 3, first version

Built and united, then set aside as a template when a source statement placed
the phase-control components behind the ground plane. Later reinstated on Layer
3 after the precursor layer stack was found to label the Layer-3 copper as
stripline and bias-T. The intermediate Layer-6 version is D.5.

### D.5 Bias-T on Layer 6

A quarter-wave segment and radial stub placed on Layer 6, in series between the
varactor DC terminal and the supply. Rejected on source grounds: the published
bias-T is a branch from the high-frequency junction, not a series continuation
through the diode. Excluded from the simulation rather than deleted.

### D.6 Layer-3 termination at the blind via, v014

The Layer-3 stripline truncated to `Ymin = 0` so that no copper extends below
the junction. Both endpoints converged, at approximately 0.0089 and 0.0093.
Phase curves stayed almost coincident, approximately -26 degrees near 26.1 GHz
and -40 to -42 degrees near 26.6 GHz. Rejected.

### D.7 Layer-5 full ground reference plane, v015

A full PEC plane on Layer 5 with a clearance around the blind via. Both
endpoints converged, at approximately 0.0098 to 0.010 and 0.0087. Separation
reached only about 1 to 1.5 degrees at 26.6 GHz. Rejected, and separately
removed on source grounds when Layer 5 was identified as bias-voltage routing.

### D.8 Explicit quarter-wave transformer branch, v016

Specified after an audit found the bias-side straight segment to be about
0.3505 mm rather than the published `Bd = 1.6 mm`. Superseded by the D.9 source
audit before it was simulated. No result exists.

### D.9 Source-topology rebuild, v017

Bias-T rebuilt on Layer 3 as a branch from the RF junction, Layer-6 bias-T and
Layer-5 ground plane excluded, DC side routed through a Layer-5 supply trace and
a local interlayer via. Both endpoints converged, at approximately 0.0094 and
0.007. Separation approximately 1 degree near the upper band edge. Rejected as
the missing tuning mechanism, but the topology corrections were kept because
they were made for source-fidelity reasons.

### D.10 Blind via anchored at `capY`, v018

Rejected before simulation. `capY` is the varactor terminal-pair centre, so
setting `viaY = capY` drove the blind via into the varactor gap and produced
overlapping lower-layer solids. No valid geometry existed to solve.

*[Appendix figure D.1 placeholder: one geometry view per rejected variant.]*

---

## Appendix E. Additional field results

The field audit produced one usable result and one unusable one.

**Surface current at 26.104 GHz, `varC = 0.025 pF`.** Maximum approximately
392.368 A/m at approximately `(1.138, -0.130, -0.254) mm`, which is the Layer-2
top level. On a fixed 0 to 5 A/m scale, the Layer-3 resonant path shows a
visible gradient at the few-A/m level. Discussed in Section 7.2.

**E-field at 26.104 GHz, `varC = 0.025 pF`.** The capture saturates because its
colour-scale maximum was set far below the maximum in the data. It carries no
physical information and is not included here. It must be regenerated on a
fixed non-saturating range, starting near 0 to 10000 V/m, using the same camera
position as the surface-current plot.

The corresponding 0.19 pF field results do not exist. Until they do, no
statement can be made about how the field distribution changes with
capacitance. See Section 10.2.

*[Appendix figure E.1 placeholder: E-field magnitude at 26.104 GHz on a fixed
non-saturating scale. Blocked pending regeneration.]*

---

## Appendix F. Experiment ledger

The full experiment record is maintained in the repository rather than in this
document, so that it stays current between report revisions.

`docs/experiment_log.md` holds one entry per controlled experiment or model
branch, in the order the work was done, with the configuration, the final
convergence value and the observed outcome.

`docs/claims_ledger.md` holds one entry per significant claim, with its
evidence, the configuration it came from, whether it is numerical or
qualitative, whether it is exact or estimated from a screenshot, a confidence
level, and a status of confirmed, provisional, hypothesis, rejected or planned.
It also records the known evidence gaps.

`docs/project_state.md` holds the current authoritative geometry, frequency
interval, capacitance endpoints, confirmed result, open hypothesis and next
experiment.

`docs/figure_manifest.md` holds the required figure list with the caption and
source configuration each figure must carry.
