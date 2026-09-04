# Reconstruction, bias-network integration, and electromagnetic evaluation of a varactor-loaded 26 GHz reflectarray unit cell

Author: Abdulrahman Ahmad
Undergraduate project, Electrical and Computer Engineering
Simulation environment: CST Studio Suite 2023, university Teaching License
Document status: working draft
Date: 2026-09-04

Repository: `varactor-reflectarray-cst`
Evidence files: `docs/claims_ledger.md`, `docs/experiment_log.md`,
`docs/project_state.md`, `docs/figure_manifest.md`

---

## Abstract

**Provisional.** This abstract describes an investigation that is still open and
will be rewritten when the experiments in Section 10 return results.

This report documents a full-wave reconstruction of a varactor-loaded, six-layer
reflectarray unit cell for K-band operation near 26 GHz, and an investigation
into why the reconstructed element does not reproduce the capacitance-dependent
reflection-phase response the reference design reports. The element couples an
incident field from a patch, through a slot, into a buried stripline resonator,
and loads that resonator with a varactor reached through a blind via on the far
side of the ground plane. A bias-T built from a quarter-wavelength line and a
radial stub feeds the diode.

The model was built in CST Studio Suite 2023 as parameterised geometry, solved
with the frequency-domain solver on an adaptive tetrahedral mesh, with periodic
unit-cell boundaries and a two-mode Floquet excitation at normal incidence over
approximately 25.6 to 26.6 GHz. Runs are accepted for comparison only when the
maximum change in all S-parameters between adaptive passes falls to
approximately 0.01 or below.

Two verification results are reported. The model is numerically sound: accepted
runs meet the convergence criterion, broadband interpolation error is
negligible, and energy balance stays close to unity across most of the interval.
The tuning element is electrically valid: its terminal voltage-to-current ratio
near 26.1 GHz is approximately 33 ohm at 0.19 pF against an ideal capacitive
reactance of approximately 32 ohm, and approximately 240 to 245 ohm at 0.025 pF
against approximately 244 ohm.

Against that, the element does not tune. On the current geometry, with
`lineV = 1.13 mm`, `slotW = 0.35 mm` and `slotL = 2.32 mm`, both capacitance
endpoints converge and their reflection-phase curves remain almost coincident at
the 26.104 GHz reference frequency, with some additional separation appearing
only near the upper end of the simulated interval. The same behaviour occurs in
every topology variant tested, including a simplified baseline, a truncated
stripline, an added Layer-5 reference plane, and a rebuilt bias network. Each of
those was tested with a converged endpoint pair and rejected.

Two hypotheses remain open: that the capacitance-sensitive region lies above the
26.6 GHz upper simulation boundary, and that the aperture coupling into the
buried resonator is too weak for the varactor to influence the reflected field.
Neither is established. The next experiment is a wider-frequency endpoint
diagnostic on unchanged geometry.

No hardware was fabricated and no measurement was made. All results are
simulation results.

---

## Contents

1. Introduction
2. Design basis and engineering objectives
3. Unit-cell architecture and modelling assumptions
4. CST simulation methodology and numerical verification
5. Reconstruction and bias-network integration
6. Electromagnetic results and controlled experiments
7. Field and surface-current diagnostics
8. Current engineering interpretation (provisional)
9. Limitations
10. Next experimental work
11. Conclusion (provisional)

References

Appendix A. Parameter table
Appendix B. Solver configuration
Appendix C. Additional convergence evidence
Appendix D. Geometry development and rejected diagnostic variants
Appendix E. Additional field results
Appendix F. Experiment ledger

---


## 1. Introduction

Reconfigurable reflectarrays steer a beam by controlling the reflection phase of
each element in a periodic surface rather than by moving the antenna. At
millimetre-wave frequencies the usual way to make an element reconfigurable is
to load a resonant structure with a varactor diode, so that a DC bias voltage
shifts the element's resonance and therefore its reflected phase. An element of
this kind has to solve two problems at once. It must present a strong,
controllable resonance to the incident field, and it must carry a DC bias to
every diode without letting the bias network disturb the RF path.

This report documents a full-wave reconstruction of one such element in CST
Studio Suite 2023. The reference design is the varactor-loaded, six-layer
reflectarray unit cell reported by Harz et al. for K-band 5G metrology near
26 GHz [CITATION REQUIRED, Harz 2020; Harz and Kleine-Ostmann 2022]. The element
couples an incident field from a top patch, through a slot, into a buried
stripline resonator, and loads that resonator with a varactor placed on the far
side of the ground plane, reached through a blind via. A bias-T built from a
quarter-wavelength line and a radial stub feeds the diode.

The work has two purposes. The first is to build a numerically defensible model
of that element from the published dimensions, so that the reflection phase can
later be characterised against capacitance and exported for array-level study.
The second, which has become the dominant activity, is to explain why the
reconstructed model does not reproduce the capacitance-dependent phase response
that the source design reports.

The current state of that investigation is straightforward to state. The model
converges. The lumped varactor is electrically active and behaves like an ideal
capacitor of the specified value. Yet moving the capacitance across its full
range from 0.025 pF to 0.19 pF changes the reflected phase near 26.104 GHz by an
amount too small to be useful. Section 6 gives the simulated behaviour, Section 8
gives the current reading of what it means, and Section 9 states what this model
cannot establish either way.

This report therefore describes a reconstruction and discrepancy analysis, not a
successful reproduction. It is written so that a reader can tell, for every
statement, whether it comes from a published source, from a converged
simulation, from a screenshot read by eye, from a modelling assumption, or from
a hypothesis that has not been tested. Section 4.6 sets out that classification
and the repository keeps a claims ledger that records the evidence behind each
statement individually.

No hardware was fabricated and no measurement was made. Every result in this
report is a simulation result.


## 2. Design basis and engineering objectives

### 2.1 Reference unit-cell concept

The reference element is a six-layer printed circuit board. The published
description assigns the layers as follows: the first four layers form the
reflecting structure, and the last two route bias signals to the varactor diode
[CITATION REQUIRED, Harz and Kleine-Ostmann 2022]. The precursor paper labels the
individual copper layers as patch, slot, stripline with bias-T, ground,
bias-voltage supply, and varactor diode [CITATION REQUIRED, Harz et al. 2020].

Electrically the element works in three stages. An incident plane wave excites
the top patch. The patch couples through a slot in the second copper layer into
a stripline on the third layer, which is buried between the slot layer and the
ground plane. That stripline is the resonator. It is divided by a blind via into
two sections whose published dimensions are named `Ls` and `Lv`: the short
section supplies inductive reactance, and the longer section together with the
varactor supplies the capacitive load that sets the phase range. The blind via
passes through a clearance in the ground plane and carries the RF node to the
lower layers, where the varactor sits. Changing the varactor capacitance
therefore changes the loading on the resonator, which moves the resonance and
shifts the phase of the reflected wave.

The bias network is the part of the design that makes this practical in an
array. The published design uses a bias-T consisting of a quarter-wavelength
line and a radial-stub shunt, so that the DC path can reach the diode while the
stub-plus-transformer combination presents a high impedance at the RF junction.
The source reports a maximum simulated phase shift of about 337 degrees for its
optimised element. That figure is a property of the published design. It is not
a result of this work, and no part of this report claims to have reproduced it.

### 2.2 Engineering objectives

The project set out to do the following.

Build a parametric CST model of the element in which every published dimension
appears as a named parameter, so that geometry changes are controlled rather
than manual. Establish that the model is numerically trustworthy, by checking
the periodic boundary and Floquet mode configuration, the energy balance, and
the convergence of the adaptive mesh, before drawing any conclusion from its
output. Verify that the tuning element itself behaves as intended, separately
from whether the surrounding structure responds to it. Characterise the
reflection magnitude and phase against capacitance and frequency, and build a
phase-versus-capacitance relation from that characterisation.

The last objective is the one that has not been reached. It requires a usable
phase response to characterise, and the reconstructed element does not yet
provide one. The project's active objective is therefore narrower: identify
where the reconstruction and the published design diverge, using controlled
experiments rather than untracked parameter adjustment.

A secondary objective governs how the work is recorded. Every dimension in the
model is one of three things: a value published by the source, a value inferred
from a published figure, or a value chosen by this project because the source
does not give it. The report keeps those categories separate throughout. Section
3.3 and Appendix A identify which is which.

### 2.3 Target operating region

The model is evaluated at normal incidence over a narrow band around the design
frequency.

| Quantity | Value |
|---|---|
| Reference frequency `fRef` | 26.104 GHz |
| Simulated interval | approximately 25.6 to 26.6 GHz |
| Unit cell | 7 mm by 7 mm, periodic in x and y |
| Incidence | `theta = 0`, `phi = 0` |
| Capacitance endpoints | 0.025 pF and 0.19 pF |

The simulated interval is not an arbitrary choice. It is the frequency range
over which the substrate material model is fitted, so results outside it would
be extrapolations of the dielectric definition as well as of the geometry. This
becomes relevant in Section 10, where the next planned experiment requires a
wider sweep.

Normal incidence keeps the Floquet mode set small and the computational cost low
enough for the available hardware, which is a 16 GB laptop running CST inside a
Windows virtual machine with roughly 6 to 8 GB available to the solver. Oblique
incidence is a later study and is not covered here.


## 3. Unit-cell architecture and modelling assumptions

### 3.1 Multilayer stack

The model is built as a stack of six conductor layers separated by five
dielectric layers, all inside a 7 mm by 7 mm periodic cell. The top of the patch
metallisation is the z origin, and every other level is derived from it by a
formula rather than entered as a number, so that changing a substrate thickness
propagates through the whole stack.

*[Figure 1 placeholder: plan view of the four RF layers. Current geometry,
`lineV = 1.13 mm`, `slotW = 0.35 mm`, `slotL = 2.32 mm`, 7 mm cell. See
`docs/figure_manifest.md`.]*

*[Figure 2 placeholder: exploded or side view of the six conductor layers and
five substrates, annotated with the z coordinates of the table below.]*

| Layer | Function | Top z (mm) | Bottom z (mm) | Copper thickness |
|---|---|---:|---:|---|
| L1 | Patch | +0.035 | 0 | `cuOuter` = 0.035 mm |
| L2 | Slot layer, four pieces | -0.254 | -0.289 | `cuOuter` |
| L3 | Stripline resonator and bias-T | -0.543 | -0.561 | `cuInner` = 0.018 mm |
| L4 | Ground, with via clearance | -0.815 | -0.833 | `cuInner` |
| L5 | Bias-voltage supply routing | -0.960 | -0.995 | `cuOuter`, assumed |
| L6 | Varactor terminals and local routing | -1.122 | -1.157 | `cuOuter`, assumed |

Substrates 1 to 3, between L1 and L4, are each 0.254 mm thick. Substrates 4 and
5, between L4 and L6, are each 0.127 mm thick.

The copper thickness used for Layers 5 and 6 is a reconstruction assumption. It
was carried over from the upper-layer interpretation rather than confirmed
against the source, and it has not been sensitivity-tested. Section 9 lists it
among the assumptions that would need to be resolved before any claim of exact
reproduction.

The blind via runs from the underside of the Layer-3 stripline down to the
Layer-6 conductor, passing through a circular clearance cut in the Layer-4
ground so that it does not short to ground. Neither the via drill diameter nor
the clearance diameter is published in the material reviewed for this work. The
model uses `viaD = 0.20 mm` and `viaClearD = 0.50 mm`, both chosen by this
project.

### 3.2 Materials

All five substrates are assigned a single material definition named
`Astra_MT77`, entered in CST as a normal dielectric.

| Property | Value |
|---|---|
| Relative permittivity | 3 |
| Electric loss tangent | 0.0017 |
| Material reference frequency | 26.104 GHz |
| Fit range | 25.6 to 26.6 GHz |

Every conductor in the model, including the patch, the slot layer, the
stripline, the ground plane, the blind via, the varactor terminal pads and the
whole bias network, is assigned perfect electric conductor. The model therefore
contains no conductor loss at all. This is a deliberate simplification for a
reconstruction baseline, and it has a specific consequence for how the results
are read: the near-unity reflection magnitude reported in Section 6.1 partly
reflects the absence of ohmic loss and should not be compared directly with a
measured reflection magnitude.

### 3.3 Idealised varactor model

The varactor is modelled as a CST lumped network element rather than as a
physical device.

| Property | Value |
|---|---|
| Name | `StageB_Ideal_Varactor` |
| Type | series RLC |
| Series resistance `R` | 0 |
| Series inductance `L` | 0 |
| Capacitance `C` | `varC * 1e-12` F |
| Endpoints | the facing edges of the two Layer-6 terminal pads, separated by 0.228 mm |
| Monitors | voltage and current enabled |

The element bridges the gap between an RF-side pad, which the blind via reaches,
and a DC-side pad, which the Layer-5 bias routing reaches through a local
interlayer via. Only the lumped element connects the two pads. No metal bridges
the gap.

Four properties of a real varactor are absent from this model. There is no
series resistance, so the element is lossless. There is no package or lead
inductance, so there is no self-resonance. There is no bias-dependent
capacitance law, so `varC` is set directly rather than derived from a control
voltage. And there is no package body, so the physical volume the diode would
occupy above the board is not present in the electromagnetic problem.

The terminal pad geometry is itself an approximation. The source does not
publish a PCB land pattern for the diode. The pads were therefore sized from the
outline of the MACOM MAVR-011020-1411 flip-chip package: `varPadW = 0.2155 mm`
across x, `varPadL = 0.1905 mm` along y, and a terminal-centre separation of
`varTermSep = 0.4185 mm`. These are device package dimensions used in place of
an unknown pad geometry, not published PCB dimensions.

Section 6.2 establishes that this idealised element is electrically active and
that its terminal impedance matches ideal capacitor reactance at both endpoints.
That validation is about the element, not about the structure around it.


## 4. CST simulation methodology and numerical verification

### 4.1 Frequency-domain and Floquet configuration

The element is solved with the CST frequency-domain solver on a tetrahedral
mesh, using a broadband general-purpose sweep over approximately 25.6 to
26.6 GHz.

The unit cell is made infinite in the plane by unit-cell boundary conditions on
Xmin, Xmax, Ymin and Ymax. The Zmin and Zmax boundaries are open with added
space. Excitation is by Floquet ports at normal incidence, `theta = 0` and
`phi = 0`.

Two propagating Floquet modes are used. The mode table identifies them as
TE(0,0) and TM(0,0); every higher order is evanescent across the simulated
interval, which is expected for a 7 mm cell at 26 GHz. Every phase comparison in
this report uses the co-polarised term `SZmax(1),Zmax(1)`. That choice was made
during the Stage-A diagnostics, where the orthogonal term `SZmax(2),Zmax(2)` was
found to be nearly insensitive to capacitance and therefore useless as a tuning
indicator.

### 4.2 Adaptive tetrahedral mesh

Mesh refinement is adaptive. The solver starts from an initial tetrahedral mesh,
solves, refines where the error indicator is largest, and repeats. Refinement is
configured with a minimum of 3 and a maximum of 8 passes.

Two practical rules govern mesh reuse between runs. When only `varC` changes, the
geometry is unchanged and the converged mesh is reused, which makes the endpoint
comparison a genuine one-variable experiment. When geometry changes, the mesh is
discarded and rebuilt, because reusing a mesh refined for a different structure
would carry an unknown bias into the comparison.

### 4.3 Convergence criterion

A run is accepted when `Maximum Delta All S-Parameters` falls to approximately
0.01 or below.

This threshold is tighter than it may appear, because of what the runs are used
for. The quantity being compared between capacitance states is a phase
difference that has repeatedly turned out to be of the order of one degree. A
numerical uncertainty comparable to that difference would make the comparison
meaningless. The 0.01 criterion was introduced for exactly this reason after an
early Stage-B baseline stopped at about 0.0119 on a looser threshold, and runs
that fail it are re-refined rather than interpreted.

Two consequences follow, and both have applied in practice. A run above the
threshold is not used in an endpoint comparison even when its curve looks
plausible. And when a solver run stops early because the active threshold in the
adaptive-mesh dialog was still set to a looser value, the run is repeated with
the correct setting rather than accepted.

*[Figure 4 placeholder: adaptive convergence for one endpoint run of the current
geometry, `Maximum Delta All S-Parameters` against pass number, with the 0.01
criterion marked. The horizontal axis is `Pass`. This is a convergence plot, not
a frequency response.]*

Appendix C collects the per-branch convergence records.

### 4.4 Broadband interpolation

The broadband sweep computes the response at a set of adaptively chosen sample
frequencies and interpolates between them, reporting an interpolation error as
it goes. In every branch recorded here that error becomes small, of the order of
a few parts in a thousand or less, by the end of the sweep. The interpolation is
therefore not a source of uncertainty in the results, and where a run failed to
meet the acceptance criterion the cause was mesh convergence rather than
frequency interpolation.

### 4.5 Field monitors

Field monitors are used as diagnostics rather than as results in their own
right. Two are defined at the reference frequency of 26.104 GHz: electric field
magnitude, and surface current density.

Two rules apply to reading them. Both capacitance states must use the same fixed
colour scale and the same camera position, or the comparison shows the scaling
rather than the physics. And a plot whose scale is set far below the maximum in
the data saturates to a single colour and carries no information; an
observation made from a saturated plot is a display artefact, not a measurement.
Section 7 applies both rules.

### 4.6 Result-classification rules

Every statement in this report falls into one of the following categories, and
the wording is chosen so that the category is recoverable from the sentence.

**Confirmed geometry or configuration.** A dimension, material property,
boundary setting or solver setting read directly from the CST model or its
dialogs. Reported as fact.

**Confirmed numerical result.** A value recorded from a solver output, such as a
convergence delta or an energy balance. Reported as fact, with the run
identified.

**Confirmed electromagnetic observation.** A qualitative behaviour seen
consistently across converged runs, such as the reflection magnitude staying
near 0 dB. Reported as fact.

**Approximate screenshot observation.** A value read off a plot by eye rather
than from a data export. Always introduced with "approximately" and never
combined arithmetically with an exact value without saying so. Most phase
readings in this report are of this type.

**Reconstruction assumption.** A dimension or topology choice the project made
because the source does not give it. Always named as an assumption at the point
of use, and listed in Appendix A and Section 9.

**Rejected hypothesis.** A proposed explanation that was tested and not
supported. Recorded with its evidence in Appendix D, so that it is not retried.

**Current hypothesis.** A proposed explanation that has not been tested. Stated
as a hypothesis, never as a finding, and paired with the experiment that would
test it.

**Planned experiment.** Work that is specified but not run. Never reported in
the past tense and never given a result.

The repository holds a claims ledger in `docs/claims_ledger.md` that assigns
each significant claim an identifier, its evidence, its precision, a confidence
level, and one of these statuses. Where this report makes a load-bearing
statement, the ledger entry behind it can be checked.


## 5. Reconstruction and bias-network integration

The model was built in two stages. Stage A reconstructed the four upper layers
with a simplified tuning element, to establish a working solver configuration.
Stage B replaced that simplification with the six-layer structure and the bias
network. This section records how the geometry was built and, more usefully,
where the first construction was wrong and what corrected it.

### 5.1 Baseline RF reconstruction

Stage A contains the patch, the four pieces that form the slot layer, the
Layer-3 stripline and the Layer-4 ground plane, on three 0.254 mm substrates.
The tuning element was a series capacitor connected directly between the
underside of the stripline and the top of the ground plane.

That topology is simple to build and simple to verify, and it did what a
baseline is supposed to do: it validated the boundary conditions, the Floquet
mode identification, the material definitions and the solver settings against a
structure with few places to hide an error. It also failed its own success
criterion. Section 6.3 gives the numbers.

The failure is informative rather than surprising. A capacitor tied straight
from the resonator to ground is not the published network. In the reference
design the RF node leaves the stripline through a blind via, crosses the ground
plane, and meets the diode on the far side, with the bias-T branching from the
RF junction rather than sitting in series with the diode. Stage A collapses all
of that into one element between two conductors. Stage B exists to build it
properly.

Stage A was frozen at that point and kept as a diagnostic reference. No dense
capacitance sweep was run on it.

### 5.2 Blind via and ground clearance

Stage B first extended the stack downward, adding Substrate 4 and Substrate 5 at
0.127 mm each and parameterising the Layer-5 and Layer-6 z coordinates from the
existing formulas.

A circular clearance was then cut through the Layer-4 ground copper using a
Boolean subtraction, and a PEC cylinder was created as `Blind_Via`, spanning
from the underside of the Layer-3 stripline down to the Layer-6 level and
passing concentrically through that clearance. The via therefore contacts the
stripline at the top and the Layer-6 conductor at the bottom, with an annular
gap isolating it from ground.

Both dimensions here are project choices. The via diameter of 0.20 mm and the
clearance diameter of 0.50 mm are not published in the material reviewed for
this work. They were parameterised rather than hard-coded so that they can be
sensitivity-tested later.

The clearance was verified after every subsequent parametric update, because a
Boolean cut driven by a moving parameter can leave a stale hole behind if the
history does not replay cleanly. The check is that exactly one clearance exists
in Layer 4 and that it stays concentric with the via.

*[Figure 3 placeholder: bias network detail showing the blind via, the Layer-4
clearance, the Layer-6 varactor terminal pads with the lumped-element markers,
the Layer-5 DC supply trace, and the Layer-3 bias-T branch with its radial
stub.]*

### 5.3 Lower routing and varactor terminals

The lower network was built as a chain of separately named PEC solids so that
each connection could be inspected on its own.

On Layer 6, an RF-side trace runs from the blind via to an RF-side terminal pad.
A second, electrically isolated DC-side pad faces it across a 0.228 mm gap. The
lumped varactor bridges that gap and nothing else does. The pad dimensions come
from the MACOM package outline described in Section 3.3, because the source does
not publish a land pattern.

The DC side then needs a path to a bias supply. Layer 5 carries a narrow trace
of width `Bl = 0.25 mm` running from the DC pad position to the cell boundary in
the negative y direction, and a short local via connects that trace down to the
Layer-6 DC pad. The via is given deliberate overlap through both copper
thicknesses so that the PEC pieces make robust contact rather than touching at a
mathematical surface. The direction of the Layer-5 trace is a routing choice
made to avoid crossing the Layer-6 RF trace, and the diameter and position of
the local via are project choices, not published dimensions.

The connectivity check that matters here has four parts: the blind via reaches
the RF pad, the local DC via lands inside the DC pad, neither via touches the
other pad, and no metal crosses the varactor gap. A single accidental overlap
anywhere in this chain would short the tuning element and produce exactly the
insensitivity the project is trying to explain, which is why the check is
repeated after each parametric update rather than done once.

### 5.4 Bias-T development

The bias-T went through the most revision of any part of the model, and its
history is worth recording because two of the intermediate versions were
plausible and wrong.

The published description is consistent: a quarter-wavelength line plus a radial
stub shunt, with `Bl = 0.25 mm`, `Bd = 1.6 mm`, `Bw = 1.3 mm` and
`Bh = 1.13 mm`. What the published material does not fix, at least in the form
reviewed here, is the mapping from those four numbers onto a CAD profile.

The radial stub was first built as a circular sector of radius `Bh` with a
half-chord of `Bw/2`, opening along the negative y direction as a continuation
of the bias line. Both parts of that reading were wrong. Re-examining the source
top view showed that the stub branches laterally from the bias line rather than
continuing it, so the sector opens toward +x. Re-examining the dimension
placement showed that `Bh` is the horizontal offset from the bias-line axis to
the chord endpoint line and `Bw` is a half-span, not a full height, which makes
the sector radius `sqrt(Bh^2 + Bw^2)`, about 1.722 mm, with a half-angle of
about 49 degrees. The corrected fan spans about 2.6 mm in y and reaches about
1.72 mm laterally from its apex, which fits inside the 7 mm cell.

Neither incorrect profile was extruded into a solid. Both were caught at the
curve stage, which cost a redraw rather than a rebuild.

The layer assignment took longer to settle. Section 5.5 covers it.

### 5.5 Important geometry and topology corrections

Four corrections changed the model materially. Each is recorded with what
prompted it, because in each case the earlier version was self-consistent and
would have gone unnoticed without a source check.

**The bias-T belongs on Layer 3, as a branch.** The bias-T was first built on
Layer 3, then moved to Layer 6 on the reading that all phase-control components
sit behind the ground plane, then moved back to Layer 3 when the precursor
source's layer stack was found to label the Layer-3 copper explicitly as
stripline and bias-T. The decisive point is topological rather than
geometrical: the source shows the bias-T branching from the high-frequency
junction, with the quarter-wave line transforming the radial stub's short into
an open at that junction. The Layer-6 version had placed the bias network in
series with the varactor, along the path from the diode to the supply. That is a
different circuit. It was excluded from the model rather than deleted, so the
comparison remains available.

**Layer 5 is bias-voltage routing, not a ground plane.** A full PEC reference
plane was added on Layer 5, with a clearance around the blind via, on the
reasoning that the Layer-6 radial stub could not behave as a microstrip
structure without one. The same source check that relocated the bias-T also
identified Layer 5 as a bias-voltage-supply layer. The plane was removed and
replaced by the narrow supply trace described in Section 5.3. Section 6 records
what the plane did to the results while it was present, which was very little.

**The blind via sits at the junction, not at the end of the resonator.** The via
position moved several times between the junction of the two stripline sections
and the far end of the longer section. It is now locked at `viaY = 0`, and the
reason is internal as well as source-based: with the Layer-3 stripline spanning
`-lineV` to `+lineS`, placing the via at the origin divides the conductor into
exactly the two published resonant dimensions. Any other position leaves those
two numbers unaccounted for.

**`capY` is the varactor centre, not the via centre.** A later attempt to anchor
the via at `capY = -lineV + lineW/2` was motivated by the observation that this
coordinate is derived from the resonator geometry rather than chosen freely.
Updating the model showed why the derivation exists: `capY` is the centre of the
varactor terminal pair, and moving the via there drove it into the varactor gap
and produced overlapping solids. The attempt was abandoned before simulation.
The coordinate is genuinely tied to the resonator, but it locates the tuning
element, not the interlayer transition.

Appendix D records the geometry of each rejected variant.


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


## 7. Field and surface-current diagnostics

S-parameters describe what leaves the structure. They do not say where the
energy went inside it. When an element converges, contains an electrically valid
tuning component, and still fails to tune, the next useful question is whether
the incident field is reaching the resonant path at all. Field monitors answer
that question directly.

### 7.1 Method

Two monitors were defined at the reference frequency of 26.104 GHz on the field
audit branch: electric field magnitude and surface current density. The geometry
was not modified for the audit, and the run used the same solver configuration
as the endpoint tests.

Reading these plots requires care with the colour scale, and the audit produced
one clear example of why. The electric-field plot saturates to a single colour
when the scale maximum is set far below the maximum in the data. A saturated
plot shows the scale, not the field, and no physical conclusion can be drawn
from it. The E-field capture from this run is unusable for that reason and is
excluded from the report until it is regenerated on a fixed non-saturating
range.

### 7.2 Surface-current distribution at 26.104 GHz

The surface-current result at `varC = 0.025 pF` is usable and gives the most
specific diagnostic evidence the project currently has.

CST reports the surface-current magnitude maximum as approximately 392.368 A/m,
located near `(x, y, z) = (1.138, -0.130, -0.254) mm`. The z coordinate places
that maximum at the Layer-2 top level, which is the slot layer.

On the default scale, the resonant path is invisible: everything except the
region around the maximum renders at the bottom of the range. Rescaling the plot
manually to a fixed 0 to 5 A/m range brings out a visible gradient along the
Layer-3 stripline and the lower routing. The rescaling is what makes the reading
quantitative rather than impressionistic. It shows that the current on the
resonant path is of the order of a few A/m while the global maximum is several
hundred A/m, a difference of roughly two orders of magnitude.

*[Figure 8 placeholder: surface-current magnitude at 26.104 GHz on a fixed
0 to 5 A/m scale. Field-audit branch, `varC = 0.025 pF`. Caption must state the
global maximum of approximately 392.368 A/m and its position at the Layer-2
level, so that the fixed scale is not mistaken for the full range of the data.]*

### 7.3 What the distribution does and does not establish

The confirmed observation is narrow: at 26.104 GHz and at the low-capacitance
endpoint, the surface current is concentrated at the slot layer, and the
Layer-3 resonant path carries current roughly two orders of magnitude smaller.

That is consistent with weak coupling from the patch and slot into the buried
stripline, which would explain the whole picture: an incident field that mostly
reflects off the upper structure, a resonator that is only lightly excited, and
a varactor that is electrically active on a branch with little influence over
the total reflected field.

It does not establish that explanation, for two reasons. A resonator can carry
modest current relative to a driven aperture and still dominate the reflected
phase, so a two-order-of-magnitude ratio is suggestive rather than decisive.
And the observation exists at one capacitance state only. The comparison that
would carry weight is between the two endpoints on identical geometry: if the
resonant-path current is essentially the same at 0.025 pF and 0.19 pF, the
varactor is not materially loading the excited resonator, and coupling becomes
the leading explanation. If the resonant-path current changes substantially
between the states while the reflected phase does not, the problem lies
somewhere between the resonator and the far field rather than in the coupling.

That comparison has not been run. Section 10 specifies it.


## 8. Current engineering interpretation

**Provisional.** This section interprets an investigation that is still open. It
will be revised when the experiments in Section 10 return results.

### 8.1 What the evidence constrains

Three findings, taken together, narrow the problem considerably.

The model is numerically sound. Every branch used for an endpoint comparison
meets the convergence criterion, the broadband interpolation error is negligible,
and the energy balance is close to unity across most of the interval. Whatever is
wrong is not a meshing or sampling artefact.

The tuning element works. Section 6.2 shows the lumped varactor drawing current,
developing voltage, and presenting a terminal impedance that matches ideal
capacitive reactance at both endpoints. It is not open, not shorted, and not
being ignored by the solver.

The structure does not respond to it. Section 6.3 shows the reflected phase at
26.104 GHz essentially unchanged across a capacitance range that the reference
design uses to produce a phase shift of about 337 degrees.

The gap is therefore between the varactor terminals and the far field, not
inside the element and not in the numerics. Something in the reconstructed
structure is decoupling a working tuning element from the reflected wave.

### 8.2 Where the fault is not

The elimination is worth stating explicitly, because it represents most of the
work done.

The fault is not the simplified Stage-A topology, which was replaced. It is not
the length of the Layer-3 stripline below the via, which was truncated and
tested. It is not a missing Layer-5 reference plane, which was added and tested.
It is not the layer assignment of the bias-T or the routing of the DC side,
which were rebuilt to match the source description and tested. It is not the
blind-via anchor coordinate, which is internally consistent with the published
resonator split and whose alternative produces a geometrically invalid model.

Each of those was a plausible reading of the published material, and each was
tested with a converged endpoint pair rather than judged by eye. None of them
changed the result by more than about a degree.

### 8.3 The two open hypotheses

**The capacitance-sensitive region may lie above the simulated interval.** On the
current geometry the endpoint curves separate slightly more near 26.5 to
26.6 GHz than near the reference frequency. The response across the whole window
is smooth and monotonic in both magnitude and phase, with no feature that looks
like a resonance inside it. Both observations are consistent with a resonance
that sits above 26.6 GHz, with the simulated window seeing only its lower
skirt.

This is a hypothesis and the evidence for it is weak. A slight increase in
separation at the edge of a window is also what a numerical trend near a
degrading energy balance looks like, and the balance does fall toward 0.983 at
26.6 GHz. Nothing in this work establishes that a resonance exists above
26.6 GHz, because nothing above 26.6 GHz has been simulated. The hypothesis is
worth testing precisely because it is cheap to test and would change the
interpretation of every result in Section 6.

**The aperture coupling into the resonator may be weak.** Section 7 shows the
surface current concentrated at the slot layer with the Layer-3 resonant path
carrying roughly two orders of magnitude less. If the incident field is largely
reflecting from the upper structure without exciting the buried stripline, the
varactor would behave exactly as observed: electrically alive on a branch that
has little say in the total reflected field.

This hypothesis has a specific weakness noted in Section 7.3. Current magnitude
on a resonant path is not the same thing as that path's influence on the
reflected phase, and the observation exists at one capacitance state only.

### 8.4 How the two hypotheses relate

They are not exclusive, and one may be a symptom of the other. A resonator whose
resonance sits above the simulated window would be off-resonance at 26.104 GHz,
and an off-resonance element accepts less energy through its coupling aperture.
The weak resonant-path current in Section 7 would then be a consequence of a
misplaced resonance rather than an independent coupling defect.

If that reading is right, both observations have a single cause, and the
frequency diagnostic in Section 10 would reveal it directly. If a wider sweep
shows a capacitance-dependent resonance above 26.6 GHz, the remaining work is to
bring that resonance down to the design frequency by correcting whichever
dimension or assumption is displacing it. If a wider sweep shows no such
resonance anywhere, the coupling hypothesis stands on its own and the
investigation moves to the patch, slot and stripline coupling geometry.

Ordering the wider-frequency diagnostic first is a judgement about cost rather
than about likelihood. It requires no geometry change, it reuses a validated
configuration, and its outcome discriminates between the two hypotheses either
way.

### 8.5 The reconstruction limit

One structural possibility deserves naming, because no amount of further
iteration on this model would resolve it.

The reconstruction depends on dimensions the published material does not
provide: the via and clearance diameters, the lower copper thicknesses, the
varactor land pattern, and the local interlayer DC connection. Each is currently
a project assumption. Any one of them could displace a resonance or detune a
coupling path, and none has been sensitivity-tested. It is possible that the
published information is not sufficient, on its own, to rebuild an element that
behaves as reported.

That would be a finding about reproducibility rather than a failure of the
model, and it is a legitimate outcome for this project. It should not be claimed
yet. The assumptions have not been bounded, and until they are, the difference
between "the source is underdetermined" and "the reconstruction has a mistake in
it that has not been found" cannot be settled from the evidence in this report.


## 9. Limitations

This section states what the model cannot establish. It is not a list of
observed results, which are in Section 6, nor of proposed explanations, which
are in Section 8.

### 9.1 Undetermined dimensions

Five quantities in the model are project choices rather than published values.

| Quantity | Value used | Basis |
|---|---|---|
| Blind-via diameter `viaD` | 0.20 mm | chosen. Not published in the reviewed material |
| Ground-clearance diameter `viaClearD` | 0.50 mm | chosen. Not published in the reviewed material |
| Layer-5 and Layer-6 copper thickness | 0.035 mm | carried over from the upper-layer interpretation, not confirmed |
| Varactor terminal pads | 0.2155 by 0.1905 mm, 0.4185 mm separation | MACOM MAVR-011020-1411 package outline used in place of an unpublished PCB land pattern |
| Local Layer-5 to Layer-6 DC via and route | 0.20 mm diameter, negative-y trace | chosen for routing convenience |

None has been sensitivity-tested. The model therefore cannot distinguish a
result that follows from the published design from one that follows from these
choices, and no statement in this report may be read as validating any of them.

The bias-branch direction is a sixth choice, but a benign one: the +x and -x
branches are mirror images in a structure that is otherwise symmetric about that
axis, so it is a CAD convention rather than an electrical assumption.

### 9.2 Idealisations in the varactor model

The tuning element is an ideal series capacitance with zero resistance and zero
inductance. A physical varactor at 26 GHz has series resistance that sets the
element Q, package and interconnect inductance that can produce a self-resonance
within or near the band of interest, and a capacitance that follows a bias
characteristic rather than being set directly. The package body itself is also
absent from the electromagnetic problem.

The consequence runs in one direction and is worth being precise about. These
omissions would degrade a real element's performance relative to the model, so
they cannot explain a model that under-performs. They do mean that the model
cannot predict achievable phase range, insertion loss, or tuning linearity for a
physical device, and that any future phase-versus-capacitance relation derived
from it describes the ideal case only.

### 9.3 Idealisations in the electromagnetic model

Every conductor is PEC, so the model contains no ohmic loss. The near-unity
reflection magnitude reported in Section 6.1 is therefore partly a property of
the idealisation and is not comparable to a measured magnitude.

The substrate uses a single dielectric definition with a fit range of 25.6 to
26.6 GHz. Results outside that interval would extrapolate the material model as
well as the geometry, which constrains the design of the wider sweep in
Section 10.

The structure is infinitely periodic at normal incidence. Edge effects, mutual
coupling variation across a finite array, and the response at oblique incidence
are all outside what this model represents.

### 9.4 Precision of the recorded evidence

Most phase and impedance values in this report were read from CST plots rather
than exported as data. They are stated as approximate throughout and should not
be treated as publication-quality numbers.

Three specific gaps affect what can be claimed. The two adaptive-mesh delta
values for the current geometry's endpoint pair are not individually recorded,
only the statement that both meet the criterion. The additional endpoint
separation near 26.5 to 26.6 GHz has not been quantified in degrees. And the
per-variant numerical records for the slot-width and `lineV` sensitivity runs
are missing, which is why Section 6.4 quotes no values for them and why Figure 7
cannot yet be produced.

Building the phase-versus-capacitance relation the project needs will require
exported S-parameter data rather than screenshots, and that export has not been
set up.

### 9.5 Scope of the sensitivity study

The geometry study in Section 6.4 tested one value of each of three parameters,
applied cumulatively, with changes small relative to the dimensions themselves.
It establishes that those three points do not tune. It does not bound the
parameter space, does not isolate the effect of any single dimension, and cannot
show that the resonator dimensions are irrelevant to the problem.

### 9.6 Frequency coverage

No simulation has been run outside approximately 25.6 to 26.6 GHz. The model
therefore cannot say whether a capacitance-dependent resonance exists above
26.6 GHz. The hypothesis in Section 8.3 is a reading of behaviour at the edge of
the simulated window, and the window itself is the limitation.

### 9.7 No hardware

Nothing in this project was fabricated or measured. Every result is a simulation
result, and no statement here can be read as an experimental confirmation of
either the reconstructed model or the published design.


## 10. Next experimental work

The experiments below are specified but not run. None of them has a result.
They are ordered so that each one's outcome determines whether the next is
worth doing.

### 10.1 Wider-frequency endpoint diagnostic

This is the immediate next experiment and it comes before any further geometry
change.

Run both capacitance endpoints, 0.025 pF and 0.19 pF, on the unchanged current
geometry, over a frequency interval wider than 25.6 to 26.6 GHz. Change nothing
else: the same boundaries, the same Floquet configuration, the same normal
incidence, the same convergence criterion.

The exact bounds have not been chosen. One constraint needs resolving before the
run: the substrate material definition is fitted over 25.6 to 26.6 GHz, so a
wider sweep either extrapolates the dielectric model or requires the fit range to
be extended, and the report must say which was done.

The Floquet mode set is not expected to be a constraint over any plausible
widening. At normal incidence the first higher order in a 7 mm cell begins to
propagate only when the cell period approaches a free-space wavelength, near
43 GHz. The mode table should still be confirmed for the chosen interval rather
than assumed, but the two-mode configuration should hold.

The experiment is decisive in both directions. If a capacitance-dependent
resonance appears above 26.6 GHz, the element tunes and the remaining problem is
that its resonance is in the wrong place, which is a question about dimensions
and assumptions. If no such feature appears anywhere in the wider interval, the
hypothesis in Section 8.3 is rejected and the investigation moves to coupling.

### 10.2 Capacitance comparison of the field monitors

Repeat the E-field and surface-current monitors at 26.104 GHz on the current
geometry at `varC = 0.19 pF`, and compare against the existing 0.025 pF result.

Both plots must use the same fixed colour scale and the same camera position.
The surface-current comparison uses the 0 to 5 A/m range that made the resonant
path visible in the first run. The E-field plot needs a fixed non-saturating
range, starting near 0 to 10000 V/m, because the existing capture saturates and
carries no information.

The comparison discriminates between the readings set out in Section 7.3. If the
resonant-path current is essentially unchanged between the two states, the
varactor is not materially loading the excited resonator. If it changes
substantially while the reflected phase does not, the problem lies between the
resonator and the far field.

### 10.3 Sensitivity test of the assumed dimensions

Vary the assumed quantities listed in Section 9.1 around their current values
and record the effect on the reflection response. The via diameter and the
ground-clearance diameter are the first candidates, because they sit directly in
the RF path between the resonator and the tuning element.

The purpose is to bound the error these assumptions introduce. Until that bound
exists, the report cannot distinguish an underdetermined source from an
undiscovered mistake in the reconstruction, which is the distinction Section 8.5
identifies as unresolved.

### 10.4 Data export and phase characterisation

Replace screenshot readings with exported S-parameter data for magnitude and
phase across the simulated interval, at each capacitance state.

This is a prerequisite rather than an experiment. It removes the precision limit
described in Section 9.4, allows the endpoint separation to be quantified in
degrees instead of described, and is the input to the phase-versus-capacitance
relation the project needs. It should be set up before the next endpoint pair is
run, so that run produces data rather than pictures.

### 10.5 Conditional work

The following depend on an earlier experiment succeeding and are listed so that
the path forward is visible, not because they are scheduled.

A dense capacitance sweep across 0.025 to 0.19 pF, with denser sampling wherever
the phase transitions sharply, becomes worthwhile only once an endpoint pair
shows meaningful separation. Running one before that would spend compute on
producing a flat line at higher resolution.

A phase-versus-capacitance lookup relation, and the array-level and
curved-surface studies that would use it, all depend on that sweep.

If the wider-frequency diagnostic and the field comparison both fail to identify
a mechanism, and the assumption sensitivity test shows the response is not
strongly sensitive to the undetermined dimensions, the appropriate step is to
document the reconstruction as underdetermined by the available published
information and seek expert review on the remaining ambiguity, rather than
continue geometry iteration.


## 11. Conclusion

**Provisional.** The investigation this report describes is open. The wording
here will change when the experiments in Section 10 return results, and the
final conclusion should not be quoted from this draft.

A varactor-loaded six-layer reflectarray unit cell for approximately 26 GHz has
been reconstructed in CST Studio Suite 2023 from published dimensions, with the
reflecting structure, the blind via and its ground clearance, the varactor
terminals and the bias network all built as parameterised geometry. The model
runs at normal incidence over approximately 25.6 to 26.6 GHz with periodic
boundaries and a two-mode Floquet excitation.

The model is numerically verified. Every run used for a comparison meets an
adaptive-mesh criterion of approximately 0.01 on the maximum change in all
S-parameters, the broadband interpolation error is negligible, and the energy
balance stays close to unity across most of the interval. The tuning element is
independently verified: its terminal voltage-to-current ratio matches ideal
capacitive reactance at both endpoint capacitances, approximately 33 ohm against
32 ohm at 0.19 pF and approximately 240 to 245 ohm against 244 ohm at 0.025 pF.

The reconstructed element does not tune. Across the full capacitance range from
0.025 pF to 0.19 pF, the reflected phase at 26.104 GHz changes by an amount too
small to be useful, on the current geometry and on every topology variant
tested. The reference design reports a maximum simulated phase shift of about
337 degrees; nothing in this work approaches that at the design frequency.

Five candidate explanations have been tested and rejected with converged
endpoint pairs rather than by inspection: the simplified baseline topology, the
length of the stripline below the via, a missing Layer-5 reference plane, the
layer assignment and routing of the bias network, and the blind-via anchor
coordinate. Two hypotheses remain open. The capacitance-sensitive region may lie
above the 26.6 GHz upper simulation boundary, and the aperture coupling into the
buried resonator may be too weak for the varactor to influence the reflected
field. They may share a cause.

The next experiment is a wider-frequency endpoint diagnostic on unchanged
geometry, which discriminates between the two hypotheses without committing to
either.

What the project has established so far is a verified model, a verified tuning
element, a documented reconstruction with its assumptions separated from its
published inputs, and a bounded set of remaining explanations. What it has not
established is why the element does not tune. That question is the current work.


## References

The two Harz references below are the design source for this project. The
bibliographic details are taken from the project's existing verified source
index. They are marked as requiring confirmation because they have not been
re-checked against the PDFs during this report build, and because the specific
figures, tables and statements cited in the text have not yet been given page or
figure numbers.

[1] T. Harz, T. Kleine-Ostmann, and T. Schrader, "Design of a continuously
tunable reflectarray element for 5G metrology in the k-band," *Advances in Radio
Science*, vol. 18, pp. 1 to 5, Dec. 2020, doi: 10.5194/ars-18-1-2020.
[CITATION REQUIRED, confirm against PDF and add figure and section numbers for
each in-text use]

[2] T. Harz and T. Kleine-Ostmann, "Measurement and optimization of a
continuously tunable 10 x 10 reflectarray antenna for 5G metrology in the
K-band," *Advances in Radio Science*, vol. 19, pp. 215 to 220, Jan. 2022,
doi: 10.5194/ars-19-215-2022.
[CITATION REQUIRED, confirm against PDF and add figure and table numbers for
each in-text use]

[3] MACOM, MAVR-011020-1411 flip-chip varactor diode datasheet, Case Style 1500.
[CITATION REQUIRED, add revision and access date. Used only for package outline
dimensions, see Section 3.3]

[4] Dassault Systemes, CST Studio Suite 2023.
[CITATION REQUIRED, add the citation form the university licence expects]

### Citation status

No reference in this list was generated from memory. Items [1] and [2] come from
the project's verified source index and the corresponding PDFs are held locally.
Items [3] and [4] identify sources that were used but whose full bibliographic
details have not been recorded.

Every in-text `[CITATION REQUIRED, ...]` marker indicates a specific statement
that needs a page, figure or table number attached before the report is
submitted. `references/README.md` tracks the outstanding items.


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


