# Experiment log

One row per controlled experiment or model branch, in the order the work was
done. "Outcome" records what was observed, not what was hoped for.

Convergence figures are the final `Maximum Delta All S-Parameters` reported by
the adaptive tetrahedral refinement. The acceptance criterion is CL-06 in
[claims_ledger.md](claims_ledger.md).

Values marked "approx." were read from a plot rather than from a log file.

---

## Stage A: simplified reflection stack

Stage A modelled the four upper layers only. The tuning element was a series
capacitor placed directly between the Layer-3 stripline and the Layer-4 ground.

| ID | Configuration | Convergence | Outcome |
|---|---|---|---|
| A-01 | `varC = 0.10 pF`, 25.6 to 26.6 GHz, normal incidence | approx. 0.008 | Baseline solved. Energy balance approx. 0.994 on Zmax(1), approx. 0.9998 on Zmax(2) near 26.104 GHz. Phase of `SZmax(1),Zmax(1)` approx. -27 deg at the reference frequency. |
| A-02 | `varC = 0.025 pF` | not separately recorded | Phase approx. -26 deg near 26.104 GHz. |
| A-03 | `varC = 0.19 pF` | not separately recorded | Phase approx. -28 deg near 26.104 GHz. `SZmax(2),Zmax(2)` nearly insensitive to capacitance. |

**Stage-A conclusion.** Total phase change across the full capacitance range is
of the order of a few degrees. The simplified stripline-to-ground capacitor
topology is not an adequate representation of the published network. Stage A was
frozen as a diagnostic reference and no dense capacitance sweep was run.

---

## Stage B: full six-layer reconstruction

Stage B added Layers 5 and 6, the blind via and its ground clearance, the
varactor terminal pads and the bias network, and moved the lumped capacitor onto
the Layer-6 terminal pair.

### Construction checkpoints (no simulation)

| ID | Step | Outcome |
|---|---|---|
| B-C1 | Substrates 4 and 5 created, Layer-5 and Layer-6 z-coordinates parameterised | Accepted |
| B-C2 | Circular clearance cut through `L4_Ground` | Accepted |
| B-C3 | `Blind_Via` created as PEC, spanning `zL3Bottom` to `zL6Top`, concentric in the clearance | Accepted after a top-view and side-view check |
| B-C4 | Layer-6 RF trace, RF-side and DC-side varactor pads created | Accepted |
| B-C5 | `StageB_Ideal_Varactor` defined across the Layer-6 pad gap, series RLC, `R = 0`, `L = 0`, `C = varC * 1e-12 F`, voltage and current monitor enabled | Accepted |
| B-C6 | Stage-A lumped element removed from the Stage-B branch | Accepted. Exactly one active lumped element remains |

### Simulated branches

| ID | Branch | Configuration | Convergence | Outcome |
|---|---|---|---|---|
| B-01 | First solve | `varC = 0.10 pF` | approx. 0.0119 at pass 3 | Reflection magnitude near 0 dB, smooth phase. Above the 0.01 criterion, so not accepted for an endpoint comparison. |
| B-02 | Baseline, refinement extended | `varC = 0.10 pF` | approx. 0.0089 at pass 6 | Accepted. Energy balance approx. 0.995 near 26.104 GHz, falling to approx. 0.983 at 26.6 GHz. |
| B-03 | Endpoint high | `varC = 0.19 pF` | approx. 0.009 at pass 6 | Accepted. |
| B-04 | Endpoint low, first attempt | `varC = 0.025 pF` | approx. 0.0138 at pass 5 | Rejected for comparison. Refinement continued. |
| B-05 | Endpoint low, refined | `varC = 0.025 pF` | below 0.01 | Accepted. |
| B-06 | Endpoint comparison | B-03 against B-05 | n/a | Phase curves almost identical: approx. -26 deg near 26.1 GHz and approx. -41 deg near 26.6 GHz in both states. Magnitude curves also nearly coincident. |
| B-07 | Lumped-element diagnostic | B-03 and B-05 results, `1D Results / Lumped Elements` | n/a | Voltage and current monitors give a terminal impedance magnitude of approx. 33 ohm at 0.19 pF and approx. 240 to 245 ohm at 0.025 pF, against ideal capacitive reactances of approx. 32 and approx. 244 ohm. The element is active and responds correctly to the parameter change. See CL-09. |

---

## Topology hypotheses tested

Each of these changed exactly one aspect of the model and ran the same endpoint
pair.

| ID | Branch | Hypothesis | Convergence (0.025 / 0.19 pF) | Outcome |
|---|---|---|---|---|
| H-01 | v014, Layer-3 termination | Truncating the Layer-3 stripline at the blind via recovers tuning | approx. 0.0089 / approx. 0.0093 | Rejected. Curves stayed almost coincident. See CL-R1. |
| H-02 | v015, Layer-5 reference plane | A missing Layer-5 reference plane prevents the radial stub from behaving as a microstrip structure | approx. 0.0098 to 0.010 / approx. 0.0087 | Rejected. Separation only approx. 1 to 1.5 deg at 26.6 GHz. A later source check also removed the plane on fidelity grounds. See CL-R2. |
| H-03 | v016, explicit quarter-wave transformer | The bias-side straight segment is too short to be the published quarter-wave transformer | not run | Specified, then superseded by the H-04 source audit before it was simulated. |
| H-04 | v017, source-topology rebuild | The bias-T belongs on Layer 3 as a branch from the RF junction, with the DC side routed through Layer 5 | approx. 0.0094 / approx. 0.007 | Rejected as the missing tuning mechanism. Separation approx. 1 deg near the upper band edge. The topology corrections were kept for source-fidelity reasons. See CL-R7. |
| H-05 | v018, via anchored at `capY` | Moving the blind via to `capY` restores the resonant loading | not run | Rejected before simulation. The change collided the via with the varactor gap, because `capY` is the varactor terminal-pair centre. See CL-R3. |
| H-06 | v019, resonant-path audit | An audit rather than a change | n/a | The Layer-3 primitive is internally consistent with the published `Lv` and `Ls` split. No gross patch, slot or stripline misalignment was visible. No geometry branch was created from it. |

---

## Field diagnostics

| ID | Configuration | Outcome |
|---|---|---|
| F-01 | v019 field audit, `varC = 0.025 pF`, E-field and surface-current monitors at 26.104 GHz | Surface-current maximum approx. 392.368 A/m at approx. `(1.138, -0.130, -0.254) mm`, which is the Layer-2 top level. Rescaling to 0 to 5 A/m shows the Layer-3 resonant path carrying current of the order of a few A/m. The E-field plot saturates on a low colour scale, which is a display artefact and carries no physical information. See CL-13. |
| F-02 | Same monitors at `varC = 0.19 pF` | Planned, not run. See CL-P2. |

---

## Geometry sensitivity sequence

After the topology hypotheses were exhausted, the work moved to varying the
published resonator dimensions directly. Each variant changed one parameter from
the reconstruction baseline and re-ran the endpoint pair.

| ID | Parameter | Baseline | Value tested | Outcome |
|---|---|---:|---:|---|
| G-01 | `slotW` | 0.26 mm | 0.35 mm | Did not produce tuning at the target frequency. Per-run convergence and phase values are not in the supplied record. |
| G-02 | `lineV` | 1.11 mm | 1.13 mm | Did not produce tuning at the target frequency. Per-run convergence and phase values are not in the supplied record. |
| G-03 | `slotL` | 2.275 mm | 2.32 mm | See below. |

G-01 and G-02 are recorded here because their parameter values carry forward
into the current geometry. Their individual numerical records are an
acknowledged evidence gap.

---

## G-03 (superseded as the current experiment)

| Item | Value |
|---|---|
| ID | G-03 |
| Geometry | `lineV = 1.13 mm`, `slotW = 0.35 mm`, `slotL = 2.32 mm` |
| Capacitance states | 0.025 pF and 0.19 pF |
| Frequency interval | approximately 25.6 to 26.6 GHz |
| Reference frequency | 26.104 GHz |
| Convergence | Both endpoints satisfy the approximately 0.01 criterion. The two individual delta values are not in the supplied record. |
| Outcome | The endpoint reflection-phase curves remain almost coincident near 26.104 GHz. Some additional separation appears near 26.5 to 26.6 GHz. No tuning at the target frequency. |

---

## Current experiment: G-04, wide-frequency endpoint diagnostic

This is the experiment CL-P1 specified. Geometry was held fixed and only the
frequency interval was widened, so the comparison against G-03 is a
one-variable change.

| Item | Value |
|---|---|
| ID | G-04 |
| Runs | Run 17 (`varC = 0.19 pF`), Run 18 (`varC = 0.025 pF`) |
| Geometry | `patchW = 2.30 mm`, `slotL = 2.32 mm`, `slotW = 0.35 mm`, `lineV = 1.13 mm` |
| Capacitance states | 0.19 pF (run 17) and 0.025 pF (run 18) |
| Frequency interval | approximately 25.5 to 28 GHz |
| Reference frequency | 26.104 GHz |
| Plot convention | red = 0.19 pF, green = 0.025 pF |

### Outcome

- Near 26.104 GHz the two endpoint phase responses remain close, as in G-03.
- Over the widened interval a **capacitance-sensitive resonant region appears
  near 26.8 GHz**. Changing `varC` shifts the reflection-magnitude dip and the
  rapid phase transition associated with it.
- The varactor therefore influences the electromagnetic resonance of the
  complete unit cell, not only the impedance at its own terminals.
- The tunable resonance is **displaced above** the intended 26.104 GHz operating
  point. **The published tuning at 26.104 GHz is not reproduced.**
- The CST phase display **wraps at plus or minus 180 degrees**. No tuning range
  in degrees is claimed from these plots.

### Record status

`patchW = 2.30 mm` departs from the published `Pw` = 2.225 mm. It is carried
here as recorded for runs 17 and 18. The branch in which `patchW` was first
moved off its published value was not logged separately, which is a further
instance of the per-variant record gap already listed in
[claims_ledger.md](claims_ledger.md).

Per-run convergence deltas for runs 17 and 18 are not in the supplied record.
The numerical S-parameter export for these runs has not been made, so the
outcome above is read from plots.

---

## Next experiment

1. Numerical export of the complex S-parameter data for runs 17 and 18 over the
   wide interval.
2. Phase unwrapping, then a phase-difference calculation between the two states
   at matched frequencies, so the tuning can be stated in degrees.
3. Re-declaration of the `Astra_MT77` material fit range, currently 25.6 to
   26.6 GHz, before any quantitative result is taken from the 26.8 GHz region.
4. Targeted tests of the reconstruction hypotheses, starting with CL-P3.
