## 6. Electromagnetic results and controlled experiments

All results in this section come from converged runs unless the text says
otherwise. Values introduced with "approximately" were read from plots rather
than exported, following the classification in Section 4.6.

### 6.1 Baseline electromagnetic response

The Stage-A baseline at `varC = 0.10 pF` solved cleanly. Near 26.104 GHz the
energy balance was approximately 0.994 on `Zmax(1)` and approximately 0.9998 on
`Zmax(2)`, and the adaptive refinement ended near a maximum S-parameter delta of
about 0.008. The reflection phase of `SZmax(1),Zmax(1)` was approximately
-27 degrees at the reference frequency.

The Stage-B baseline, on the full six-layer structure at the same capacitance,
behaves similarly. Its first run reached a maximum S-parameter delta of about
0.0119 at pass 3, which is above the acceptance criterion; extending the
refinement brought it to about 0.0089 by pass 6, and that run was accepted. Its
energy balance is approximately 0.995 near the reference frequency and falls to
approximately 0.983 at 26.6 GHz. The balance degrading toward the top of the
band is consistent across branches and is a reason to treat the upper band edge
as the least reliable part of the interval.

Two features of the response are consistent across every converged Stage-B
branch, including the current geometry. The magnitude of `SZmax(1),Zmax(1)`
stays close to 0 dB across 25.6 to 26.6 GHz. The phase is smooth and monotonic
across the same interval, without the rapid excursion that would indicate a
resonance inside the simulated window.

Both observations need a caveat that Section 3.2 anticipates. The model has no
conductor loss and a low-loss dielectric, so near-unity reflection magnitude is
partly a property of the idealisation. A magnitude near 0 dB is therefore weak
evidence about the physical element, but the absence of any magnitude feature
across the band is still informative: a strongly resonant element would normally
show one.

*[Figure 5 placeholder: reflection phase of `SZmax(1),Zmax(1)` against
frequency, both capacitance endpoints overlaid. Current geometry,
`lineV = 1.13 mm`, `slotW = 0.35 mm`, `slotL = 2.32 mm`, `varC = 0.025` and
`0.19 pF`, approximately 25.6 to 26.6 GHz, with `fRef = 26.104 GHz` marked.]*

*[Figure 6 placeholder: reflection magnitude of `SZmax(1),Zmax(1)` against
frequency for the same two runs.]*

### 6.2 Varactor electrical validation

Before drawing any conclusion from the weak phase response, it is necessary to
rule out the simplest explanation: that CST is not exciting the lumped element
at all. A capacitor that is open, disconnected or shorted would produce exactly
the observed insensitivity, and would do so without any error message.

The test uses the voltage and current monitors on `StageB_Ideal_Varactor`. If
the element is behaving as an ideal series capacitor, the ratio of terminal
voltage magnitude to terminal current magnitude at a given frequency should
equal the capacitive reactance `1 / (2 * pi * f * C)`, and it should change by
roughly a factor of 7.6 between the two endpoint capacitances.

Readings were taken at approximately 26.1 GHz from the monitor plots, which
report in dBA and dBV.

| `varC` | Current, dBA | Voltage, dBV | Current magnitude | Voltage magnitude | Impedance magnitude | Ideal reactance |
|---:|---:|---:|---:|---:|---:|---:|
| 0.19 pF | approx. -45 | approx. -14.7 | approx. 5.6 mA | approx. 0.184 V | approx. 33 ohm | approx. 32 ohm |
| 0.025 pF | approx. -54.5 | approx. -6.8 | approx. 1.9 mA | approx. 0.46 V | approx. 240 to 245 ohm | approx. 244 ohm |

The agreement is close at both endpoints, and the ratio between them tracks the
capacitance ratio. The current also falls and the voltage rises as capacitance
decreases, which is consistent with a fixed excitation driving a larger
reactance.

This establishes three things. The element is being excited by the RF solution
rather than sitting in a dead branch. It is not shorted by accidental metal
across the terminal gap, which was a live concern given the number of separate
PEC solids in the lower network. And it responds numerically to the `varC`
parameter, so the capacitance change is reaching the solver.

The values are screenshot readings and should be treated as approximate. The
conclusion does not depend on their precision: an element that was inactive
would be wrong by orders of magnitude, not by a few ohms.

What this test does not establish is that the varactor is loading the resonator.
It measures the element, not its influence on the structure around it. That
distinction is the pivot of the whole investigation, and Section 8 returns to
it.

### 6.3 Endpoint capacitance comparison

The endpoint test is the project's decision criterion. Two runs differ only in
`varC`, one at 0.025 pF and one at 0.19 pF, on identical geometry with a reused
mesh. If the element tunes, the two reflection-phase curves separate. If they do
not separate, the element does not tune, whatever else is true of the model.

The result has been the same in every branch tested.

| Branch | Convergence, 0.025 / 0.19 pF | Phase separation near 26.1 GHz |
|---|---|---|
| Stage A, simplified topology | approx. 0.008 baseline | a few degrees across the full range: approx. -26, -27 and -28 deg at 0.025, 0.10 and 0.19 pF |
| Stage B, first full reconstruction | below 0.01 / approx. 0.009 | negligible. Both approx. -26 deg at 26.1 GHz and approx. -41 deg at 26.6 GHz |
| Layer-3 termination variant | approx. 0.0089 / approx. 0.0093 | negligible |
| Layer-5 reference-plane variant | approx. 0.0098 to 0.010 / approx. 0.0087 | negligible near 26.1 GHz, approx. 1 to 1.5 deg at 26.6 GHz |
| Source-topology rebuild | approx. 0.0094 / approx. 0.007 | negligible, approx. 1 deg near the upper band edge |
| Current geometry, `slotL = 2.32 mm` | both satisfy the approx. 0.01 criterion | almost coincident near 26.104 GHz, with some additional separation near 26.5 to 26.6 GHz |

Two things are worth separating here. The first is that every one of these runs
is numerically acceptable, so the flat result is not an artefact of an
under-refined mesh. The second is that the separation, where it appears at all,
appears at the top of the simulated interval rather than at the design
frequency.

The corresponding magnitude curves behave the same way. Across every converged
branch the two endpoint magnitude traces separate by only a few hundredths of a
dB, and only near the upper band edge.

The separation at the upper band edge is a visual observation of a trend, not a
measurement. It has not been quantified in degrees in any branch. Section 8
discusses what it might mean and Section 10 gives the experiment that would
settle it. Section 6.4.3 records the current geometry's endpoint result in full.

The reference design reports a maximum simulated phase shift of about
337 degrees [CITATION REQUIRED, Harz and Kleine-Ostmann 2022]. The reconstructed
element does not approach that at the design frequency in any branch tested.

### 6.4 Geometry sensitivity study

With the topology hypotheses exhausted, the investigation moved to the resonator
dimensions themselves. The reasoning is that if the topology is right and the
element still does not tune, the resonance may simply be in the wrong place, and
the published dimensions are the parameters that place it.

Each variant changed one dimension from the reconstruction baseline and re-ran
the endpoint pair with a fresh mesh, since geometry changed.

#### 6.4.1 Slot-width sensitivity

The slot width was increased from the baseline `slotW = 0.26 mm` to
`slotW = 0.35 mm`. The slot is the coupling aperture between the patch and the
buried stripline, so widening it changes how strongly the incident field reaches
the resonator.

The change did not produce tuning at the target frequency, and the value was
carried forward into the subsequent variants. The per-run convergence deltas and
phase readings for this variant are not in the archived record for this
repository, so no numerical result is quoted for it. This is recorded as an
evidence gap in `docs/claims_ledger.md` rather than reconstructed from memory.

#### 6.4.2 lineV sensitivity

The longer stripline section was increased from `lineV = 1.11 mm` to
`lineV = 1.13 mm`. This is the section that, together with the varactor, sets
the capacitive load on the resonator, so it is the dimension most directly tied
to the phase range in the published description.

The change did not produce tuning at the target frequency. As with the slot
width, the per-run numerical record is missing and no values are quoted.

The small size of the change is worth noting for later work: 0.02 mm on 1.11 mm
is under two per cent, so this variant tested a nearby point rather than
exploring the parameter.

#### 6.4.3 Slot-length sensitivity

The slot length was increased from `slotL = 2.275 mm` to `slotL = 2.32 mm`, on
the geometry that already carried `slotW = 0.35 mm` and `lineV = 1.13 mm`. This
is the current model and the experiment with the fullest record.

Both capacitance endpoints satisfy the approximately 0.01 convergence criterion.
The two endpoint reflection-phase curves remain almost coincident near
26.104 GHz. Some additional separation appears near the upper end of the
simulated interval, around 26.5 to 26.6 GHz.

The `slotL = 2.32 mm` test did not produce tuning at the target frequency.

#### 6.4.4 Sensitivity-study summary

*[Figure 7 placeholder: endpoint phase separation compared across the geometry
sensitivity variants. Blocked: the archived per-variant results for the
`slotW` and `lineV` experiments are not available. See
`docs/figure_manifest.md`.]*

Three single-parameter changes, applied cumulatively, moved the element from
`slotW = 0.26`, `lineV = 1.11`, `slotL = 2.275 mm` to `slotW = 0.35`,
`lineV = 1.13`, `slotL = 2.32 mm`. None of them produced capacitance-dependent
phase tuning at 26.104 GHz.

The study is limited in a way that matters for interpreting it. Each variant
tested one value of one parameter rather than a range, the changes were small
relative to the dimensions themselves, and they were applied cumulatively rather
than independently, so the current geometry is not a controlled variation on the
baseline in any single parameter. The study is therefore evidence that these
particular three points do not tune. It is not evidence that the resonator
dimensions are irrelevant, and it does not bound how far the geometry would have
to move before the behaviour changed.

The one positive signal to come out of the sequence is the separation appearing
near the top of the band rather than at the design frequency. That observation
drives the current hypothesis in Section 8 and the experiment in Section 10.
