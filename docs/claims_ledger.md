# Claims ledger

Every claim the report is allowed to make appears here first. If a statement is
not in this ledger, the report must not assert it.

Last updated: 2026-09-04 (revised after direct verification against both source PDFs)

## Field definitions

**Status**

- `confirmed`: supported by a recorded simulation or a direct model inspection.
- `provisional`: supported, but the supporting evidence is approximate or the
  wording may change once better evidence exists.
- `hypothesis`: a proposed explanation. No evidence establishes it.
- `rejected`: tested and not supported. Kept so the same idea is not retried.
- `planned`: an experiment that has been specified but not run.

**Kind** is `numerical` when the claim carries a number, `qualitative` otherwise.

**Precision** is `exact` for values read from a parameter list, a dialog or a
solver log, and `screenshot estimated` for values read off a plot by eye.

**Confidence** is the author's judgement: `high`, `medium` or `low`.

---

## Confirmed claims

### CL-01 Six-layer stack

**Claim.** The unit cell is modelled in CST 2023 as a six-conductor-layer stack
on a 7 mm by 7 mm periodic cell: patch (L1), slot layer (L2), stripline and
bias-T (L3), ground (L4), bias-voltage routing (L5), varactor layer (L6),
separated by three 0.254 mm substrates and two 0.127 mm substrates.
**Evidence.** Model parameter list and z-coordinate formulas recorded in the
project continuity notes.
**Configuration.** All branches from the Stage-B reconstruction onward.
**Kind.** numerical. **Precision.** exact. **Confidence.** high.
**Status.** confirmed.

### CL-02 Substrate material definition

**Claim.** All five substrates use a material named `Astra_MT77`, defined as a
normal dielectric with relative permittivity 3 and electric loss tangent
0.0017, with a material reference frequency of 26.104 GHz and a fit range of
25.6 to 26.6 GHz.
**Evidence.** Material dialog inspection in CST 2023.
**Kind.** numerical. **Precision.** exact. **Confidence.** high.
**Status.** confirmed.

### CL-03 Conductors are perfect electric conductor

**Claim.** Every conductor in the model is assigned PEC. Conductor loss is
therefore absent from the model by construction.
**Evidence.** Material assignment check on `L1_Patch`, `L3_Stripline`,
`L4_Ground` and the later `RF_Bias` solids.
**Kind.** qualitative. **Precision.** exact. **Confidence.** high.
**Status.** confirmed.

### CL-04 Periodic boundary and Floquet configuration

**Claim.** The model uses unit-cell boundaries on Xmin, Xmax, Ymin and Ymax and
open (add space) boundaries on Zmin and Zmax, at normal incidence
(`theta = 0`, `phi = 0`), with two propagating Floquet modes, TE(0,0) and
TM(0,0). Higher orders are evanescent across the simulated interval.
**Evidence.** Boundary dialog and Floquet mode table inspection.
**Kind.** qualitative. **Precision.** exact. **Confidence.** high.
**Status.** confirmed.

### CL-05 Reflection coefficient used for the phase comparison

**Claim.** `SZmax(1),Zmax(1)` is the co-polarised reflection term used for every
phase comparison in this project. In the Stage-A capacitance test the orthogonal
term `SZmax(2),Zmax(2)` was nearly insensitive to capacitance.
**Evidence.** Stage-A capacitance endpoint comparison.
**Kind.** qualitative. **Precision.** screenshot estimated. **Confidence.** high
for the choice of term, medium for the insensitivity of mode 2.
**Status.** confirmed.

### CL-06 Convergence criterion

**Claim.** A run is accepted for an endpoint comparison when the adaptive
tetrahedral refinement drives `Maximum Delta All S-Parameters` to approximately
0.01 or below, with a minimum of 3 and a maximum of 8 passes.
**Evidence.** Adaptive-mesh properties dialog and the per-branch convergence
plots.
**Kind.** numerical. **Precision.** exact. **Confidence.** high.
**Status.** confirmed.

### CL-07 Stage-A numerical health

**Claim.** In the Stage-A baseline at `varC = 0.10 pF` near 26.104 GHz, the
energy balance was about 0.994 on `Zmax(1)` and about 0.9998 on `Zmax(2)`, and
the adaptive refinement ended near a maximum S-parameter delta of about 0.008.
**Evidence.** Stage-A balance plot and adaptive convergence plot.
**Kind.** numerical. **Precision.** screenshot estimated, except the delta value
of about 0.00811 which was also recorded numerically.
**Confidence.** medium. **Status.** confirmed.

### CL-08 Stage-A capacitance response

**Claim.** In the Stage-A model the reflection phase of `SZmax(1),Zmax(1)` near
26.104 GHz was approximately -26, -27 and -28 degrees at 0.025, 0.10 and
0.19 pF. The total phase change across the full capacitance range was therefore
of the order of a few degrees.
**Evidence.** Overlaid Stage-A endpoint phase plots.
**Kind.** numerical. **Precision.** screenshot estimated. **Confidence.** medium
on the individual values, high on the conclusion that the change is only a few
degrees. **Status.** confirmed.

### CL-09 Lumped varactor electrical validation

**Claim.** The Stage-B ideal lumped varactor is excited by the RF solution and
its voltage-to-current ratio near 26.1 GHz agrees with the reactance of an ideal
capacitor at both endpoint capacitances.

| `varC` | Current magnitude | Voltage magnitude | Impedance magnitude | Ideal reactance `1/(2*pi*f*C)` at 26.1 GHz |
|---:|---:|---:|---:|---:|
| 0.19 pF | approx. 5.6 mA | approx. 0.184 V | approx. 33 ohm | approx. 32 ohm |
| 0.025 pF | approx. 1.9 mA | approx. 0.46 V | approx. 240 to 245 ohm | approx. 244 ohm |

**Evidence.** CST lumped-element voltage and current monitor results, read from
plots in dBA and dBV (-45 dBA / -14.7 dBV and -54.5 dBA / -6.8 dBV) and
converted.
**Configuration.** Stage-B geometry, `StageB_Ideal_Varactor`, 25.6 to 26.6 GHz.
**Kind.** numerical. **Precision.** screenshot estimated.
**Confidence.** medium on the individual magnitudes, high on the conclusion that
the element is active and responds correctly to the parameter change.
**Status.** confirmed.

### CL-10 Stage-B baseline numerical health

**Claim.** The Stage-B baseline at `varC = 0.10 pF` reached a maximum
S-parameter delta of about 0.0089 by pass 6, after about 0.0119 at pass 3. The
energy balance was about 0.995 near the reference frequency and fell to about
0.983 at 26.6 GHz.
**Evidence.** Stage-B convergence and balance plots.
**Kind.** numerical. **Precision.** screenshot estimated.
**Confidence.** medium. **Status.** confirmed.

### CL-11 Blind-via anchor coordinate

**Claim.** With the Layer-3 stripline defined as `Ymin = -lineV`,
`Ymax = +lineS`, placing the blind via at `viaY = 0` divides that conductor into
the two published resonant dimensions `Lv` and `Ls`. The coordinate is therefore
internally consistent with the published parameterisation.
**Evidence.** CST history and parameter audit of `L3_Stripline`.
**Kind.** qualitative. **Precision.** exact. **Confidence.** high for internal
consistency, medium for source fidelity. **Status.** confirmed.

### CL-12 Current endpoint result

**Claim.** On the `lineV = 1.13`, `slotW = 0.35`, `slotL = 2.32` geometry, both
capacitance endpoints satisfy the approximately 0.01 convergence criterion. The
two reflection-phase curves remain almost coincident near 26.104 GHz. Some
additional separation appears near the upper end of the simulated interval,
around 26.5 to 26.6 GHz. The test did not produce tuning at the target
frequency.
**Evidence.** Latest endpoint comparison on the current geometry.
**Configuration.** `varC = 0.025 pF` and `varC = 0.19 pF`, approximately
25.6 to 26.6 GHz, `fRef = 26.104 GHz`.
**Kind.** qualitative, with a numerical convergence statement.
**Precision.** screenshot estimated for the curve separation.
**Confidence.** high. **Status.** confirmed.

### CL-13 Surface-current distribution at the reference frequency

**Claim.** In the field-monitor run at `varC = 0.025 pF` and 26.104 GHz, the
surface-current magnitude maximum was about 392.368 A/m, located near
`(x, y, z) = (1.138, -0.130, -0.254) mm`, which is the Layer-2 top level.
Rescaling the plot to a 0 to 5 A/m range showed that the current on the
Layer-3 resonant path is of the order of a few A/m.
**Evidence.** CST surface-current monitor result and its reported maximum
position.
**Kind.** numerical. **Precision.** the maximum value and position are exact as
reported by CST. The few-A/m statement about the resonant path is a
screenshot-derived reading.
**Confidence.** high for the maximum, medium for the resonant-path level.
**Status.** confirmed.

### CL-14 Reflection magnitude

**Claim.** In every converged Stage-B branch, the magnitude of
`SZmax(1),Zmax(1)` stays close to 0 dB across 25.6 to 26.6 GHz, and the
endpoint magnitude curves separate by only a few hundredths of a dB at the upper
band edge.
**Evidence.** Endpoint magnitude overlays for the Stage-B branches.
**Kind.** qualitative. **Precision.** screenshot estimated.
**Confidence.** high. **Status.** confirmed.

---

## Source claims (properties of the published design, not of this model)

### CL-S1 Published simulated phase-shift range

**Claim.** Harz and Kleine-Ostmann (2022) state that the main goal of their
optimisation was a wide phase-shift range, "resulting in a maximum simulated
phase shift of 337 degrees".
**Evidence.** Verified directly against the publisher PDF, Section 2,
"Reflectarray element", page 216.
**Kind.** numerical. **Precision.** exact as quoted. **Confidence.** high.
**Status.** confirmed as a quotation of the source.

**Note.** The earlier precursor element in Harz et al. (2020) reports a
simulated adjustable phase range of 340 degrees for a different element. See
CL-S9. The two numbers belong to two different designs and must not be
interchanged.

### CL-S2 Published bias-T description

**Claim.** The source design describes the bias-T as a quarter-wavelength line
plus a radial-stub shunt, with `Bl = 0.25`, `Bd = 1.6`, `Bw = 1.3` and
`Bh = 1.13` mm.
**Evidence.** Source table values recorded in the continuity notes.
**Kind.** numerical. **Precision.** exact as quoted. **Confidence.** high.
**Status.** confirmed as a quotation of the source.

### CL-S3 Published element dimensions

**Claim.** Table 1 of Harz and Kleine-Ostmann (2022), "Dimensions of the antenna
element", gives the following values.

| Symbol | Value | Symbol | Value | Symbol | Value |
|---|---:|---|---:|---|---:|
| X | 7.0 mm | Sw | 0.26 mm | Sl | 2.275 mm |
| Y | 7.0 mm | Lw | 0.33 mm | Ls | 0.2 mm |
| Pw | 2.225 mm | Lv | 1.11 mm | Bl | 0.25 mm |
| Bd | 1.6 mm | Bw | 1.3 mm | Bh | 1.13 mm |

**Evidence.** Verified directly against the publisher PDF, Table 1, page 217.
**Consequence.** Every one of these values is reproduced exactly by the
reconstruction baseline. The mapping is X to `cellX`, Y to `cellY`, Pw to
`patchW`, Sw to `slotW`, Sl to `slotL`, Lw to `lineW`, Lv to `lineV`, Ls to
`lineS`, and Bl, Bd, Bw, Bh directly. The reconstruction baseline is therefore
dimensionally faithful to the published element in every dimension the source
publishes.
**Kind.** numerical. **Precision.** exact. **Confidence.** high.
**Status.** confirmed as a quotation of the source.

### CL-S4 Published substrate material

**Claim.** The source selected Isola Astra MT77 "because it allows the
realization of buried and blind vias as well", and states that the material is
"specified with a permittivity of 3.0 and a loss factor of 0.0017 up to 20 GHz".
The same material is used for all layers so that no mechanical tension bows or
twists the board.
**Evidence.** Verified directly against the publisher PDF, Section 2, page 216.
**Note.** The published specification is quoted only up to 20 GHz, while the
element operates near 26 GHz. The source applies the same numbers at 26 GHz, and
this model follows that choice. This is a source-level extrapolation, not a
modelling error introduced here.
**Kind.** numerical. **Precision.** exact as quoted. **Confidence.** high.
**Status.** confirmed as a quotation of the source.

### CL-S5 Published dielectric thicknesses

**Claim.** "The thickness of the dielectric material for the first, the second,
and the third layer is 254 micrometres. All other layers have a thickness of
127 micrometres."
**Evidence.** Verified directly against the publisher PDF, Section 2, page 216.
**Consequence.** This confirms `sub1 = sub2 = sub3 = 0.254 mm` and
`sub4 = sub5 = 0.127 mm` in the model.
**Kind.** numerical. **Precision.** exact as quoted. **Confidence.** high.
**Status.** confirmed as a quotation of the source.

### CL-S6 Published varactor device and capacitance range

**Claim.** The 2022 source selects a MACOM flip-chip varactor diode with "a
capacitance in the range from 0.025 to 0.19 pF obtained by a control voltage
between 0 and 15 V", and states that the manufacturer does not provide
equivalent-circuit parameters.
**Evidence.** Verified directly against the publisher PDF, Section 2, page 216.
**Consequence.** This is the origin of `Cmin = 0.025 pF` and `Cmax = 0.19 pF`.
**Ambiguity.** The 2022 paper names the part MAVR-011020-111. The 2020 precursor
names MAVR-011020-141 for the same capacitance range. The reconstruction pad
geometry in CL-A4 was taken from a package outline recorded as
MAVR-011020-1411. These three part numbers are not identical and the difference
has not been resolved against a manufacturer datasheet.
**Kind.** numerical. **Precision.** exact as quoted. **Confidence.** high for
the capacitance range, low for the exact part variant.
**Status.** confirmed as a quotation of the source, with an open ambiguity.

### CL-S7 Published measured phase behaviour and the origin of the reference frequency

**Claim.** In the 2022 waveguide-simulator measurement the control voltage was
varied from 0 to 15 V and phase and loss were measured "over the frequency band
from 25.6 to 26.6 GHz". Within a 100 MHz bandwidth the maximum phase change
range is between 308 and 336 degrees. At 26.104 GHz specifically, "the phase
change range at this frequency is 322 degrees".
**Evidence.** Verified directly against the publisher PDF, Section 3, page 217.
**Consequence.** This is the origin of both `fRef = 26.104 GHz` and the
25.6 to 26.6 GHz simulated interval used throughout this project. Neither was
chosen arbitrarily.
**Important.** These are measured values for fabricated hardware in a waveguide
simulator, obtained at a tilted incidence angle of 21.4 degrees. They are not
unit-cell simulation results and are not comparable term by term with the
normal-incidence simulations in this project.
**Kind.** numerical. **Precision.** exact as quoted. **Confidence.** high.
**Status.** confirmed as a quotation of the source.

### CL-S8 Published bias-T description and decoupling

**Claim.** The 2022 source describes the bias-T as consisting of "a
quarter-wavelength stripline transformer and a microstrip radial stub shunt",
where the radial shunt generates a short and the quarter-wavelength transformer
converts it into an open circuit at the junction to the high-frequency
stripline. With one radial stub shunt a decoupling of 36 dB was accomplished.
The 2020 precursor reports over 39 dB for its own bias-T and transmission losses
below 0.1 dB.
**Evidence.** Verified directly against both publisher PDFs, 2022 Section 2
page 216 and 2020 Section 3 page 3.
**Kind.** numerical. **Precision.** exact as quoted. **Confidence.** high.
**Status.** confirmed as a quotation of the source.

### CL-S9 The 2020 precursor element is a different design

**Claim.** The element in Harz et al. (2020) is not the element reconstructed
here. It uses an 8 mm by 8 mm unit cell, a Rogers RT5870 substrate with relative
permittivity 2.33 at 10 GHz, a 2.5 mm by 2.5 mm patch, a 2.5 mm slot length with
0.26 mm slot width, a stripline width of 0.5 mm, Lw of 0.8 mm and Lv of 1.5 mm,
and reports a simulated adjustable phase range of 340 degrees.
**Evidence.** Verified directly against the publisher PDF, Sections 2 and 4,
pages 2 and 4.
**Consequence.** The 2020 paper is used in this project only for its
explanation of the operating principle and for its bias-T port definition and
dimensioning figure. Its numerical dimensions must never be mixed with the 2022
Table 1 values that the reconstruction follows.
**Kind.** numerical. **Precision.** exact as quoted. **Confidence.** high.
**Status.** confirmed as a quotation of the source.

### CL-S10 Published licence terms

**Claim.** Both source articles carry the statement "This work is distributed
under the Creative Commons Attribution 4.0 License" on page 1.
**Evidence.** Read directly from page 1 of each publisher PDF.
**Consequence.** Figures may be reproduced in this report with attribution.
See `figures/source/ATTRIBUTION.md`.
**Kind.** qualitative. **Precision.** exact. **Confidence.** high.
**Status.** confirmed.

---

## Reconstruction assumptions

None of these are published values. Each must be sensitivity-tested before any
claim of exact reproduction.

### CL-A1 Blind-via diameter

`viaD = 0.20 mm`. Not published in the reviewed material.
**Status.** provisional assumption. **Confidence.** low.

### CL-A2 Ground-clearance diameter

`viaClearD = 0.50 mm`. Not published in the reviewed material.
**Status.** provisional assumption. **Confidence.** low.

### CL-A3 Lower copper thickness

Layers 5 and 6 use `cuOuter = 0.035 mm`, carried over from the upper-layer
interpretation rather than confirmed against the source.
**Status.** provisional assumption. **Confidence.** low.

### CL-A4 Varactor terminal geometry

The Layer-6 terminal pads use the MACOM MAVR-011020-1411 flip-chip package
outline as an approximation: `varPadW = 0.2155`, `varPadL = 0.1905`,
`varTermSep = 0.4185 mm`. The source does not publish a PCB land pattern for the
diode, so these are device-package dimensions used in place of an unknown pad
geometry.
**Status.** provisional assumption. **Confidence.** low.

### CL-A5 Local Layer-5 to Layer-6 DC interconnect

The diameter, position and route of the local DC via that connects the
Layer-5 bias trace to the isolated Layer-6 DC pad are chosen, not published.
**Status.** provisional assumption. **Confidence.** low.

### CL-A6 Bias-branch direction

In the model the Layer-3 bias line runs from the via junction toward -Y and the
radial stub opens laterally toward +X at a distance `Bd` along it.
**Update after direct source inspection.** Figure 1 of Harz and Kleine-Ostmann
(2022) shows exactly this arrangement: the bias line continues away from the
patch along the stripline axis and the radial stub branches sideways from it.
The relative arrangement is therefore source-supported rather than assumed. The
absolute sign in the model's coordinate frame remains a convention, and the
mirrored layout is electrically equivalent at normal incidence.
**Status.** arrangement confirmed against the source figure; the sign
convention remains a modelling choice. **Confidence.** high for the
arrangement, high that the sign is immaterial.

### CL-A7 Ideal varactor model

The varactor is a series RLC lumped element with `R = 0`, `L = 0` and
`C = varC * 1e-12 F`. Package parasitics, series resistance, lead inductance and
the capacitance-versus-bias characteristic of a real diode are all absent.
**Status.** deliberate modelling simplification. **Confidence.** high that this
is what the model contains. **Status.** confirmed as a model property,
provisional as a representation of the physical device.

---

## Rejected hypotheses

### CL-R1 Layer-3 termination at the blind via

**Hypothesis.** Truncating `L3_Stripline` so that it ends at the blind via
(`Ymin = 0`) would recover capacitance-dependent tuning.
**Result.** Both endpoints converged (maximum S-parameter delta about 0.0089 at
0.025 pF and about 0.0093 at 0.19 pF). The phase curves stayed almost
coincident, around -26 degrees near 26.1 GHz and -40 to -42 degrees near
26.6 GHz. **Status.** rejected. **Confidence.** high.

### CL-R2 Missing Layer-5 ground reference plane

**Hypothesis.** Adding a full PEC reference plane on Layer 5, with a clearance
around the blind via, would make the Layer-6 radial stub behave as the intended
microstrip structure and recover tuning.
**Result.** Both endpoints converged (about 0.0098 to 0.010 at 0.025 pF and
about 0.0087 at 0.19 pF). Phase separation stayed at about 1 to 1.5 degrees at
26.6 GHz and was negligible near 26.1 GHz. A later source check also found that
Layer 5 is a bias-voltage-supply layer rather than a ground plane, so the plane
was excluded from the model on source grounds as well.
**Status.** rejected. **Confidence.** high.

### CL-R3 Blind via anchored at `capY`

**Hypothesis.** Setting `viaY = capY = -0.945 mm` would restore the resonant
loading, because `capY = -lineV + lineW/2` ties that coordinate to the resonant
stripline geometry.
**Result.** Rejected before simulation. The parameter relationships make `capY`
the centre of the varactor terminal pair (`varCenterY = capY`), so the change
drove the blind via into the varactor gap and produced overlapping lower-layer
solids. No valid geometry existed to simulate.
**Status.** rejected. **Confidence.** high.

### CL-R4 Bias-T on Layer 6

**Hypothesis.** The quarter-wave transformer and radial stub belong on Layer 6,
in series between the varactor DC terminal and the DC supply.
**Result.** Rejected on source grounds. The precursor source labels the Layer-3
copper as stripline and bias-T, and describes the bias-T as a branch from the
high-frequency junction rather than a series continuation through the varactor.
The Layer-6 bias-T was excluded and rebuilt on Layer 3.
**Status.** rejected. **Confidence.** medium to high.

### CL-R5 Radial-stub dimension interpretation using `Bw/2`

**Hypothesis.** The radial stub has radius `Bh` and half-height `Bw/2`.
**Result.** Superseded by a re-reading of the source figure, in which `Bh` is the
horizontal offset from the bias-line axis to the chord endpoint line and `Bw` is
a half-span rather than a full height. The corrected sector uses
`stubR = sqrt(Bh^2 + Bw^2)` and a half-angle of about 49 degrees.
**Status.** rejected. **Confidence.** medium.

### CL-R6 Radial stub opening toward -Y

**Hypothesis.** The radial stub fans out along the negative Y direction,
continuing the bias line.
**Result.** Superseded. The source top view shows the stub branching laterally
from the bias line. The corrected sector opens toward +X.
**Status.** rejected. **Confidence.** medium.

### CL-R7 Source-topology rebuild recovers tuning

**Hypothesis.** Rebuilding the bias-T on Layer 3 as a branch, excluding the
Layer-6 bias-T and the Layer-5 ground plane, and routing the DC side through a
separate Layer-5 supply trace and a local interlayer via would recover tuning.
**Result.** Both endpoints converged (about 0.0094 at 0.025 pF and about 0.007
at 0.19 pF). The phase curves stayed almost coincident, separating by about
1 degree near the upper band edge.
**Status.** rejected as the missing mechanism. The topology corrections
themselves are retained, because they were made for source-fidelity reasons
independent of their effect on tuning. **Confidence.** high.

---

## Open hypotheses

### CL-H1 Capacitance-sensitive region above the simulated interval

**Hypothesis.** The stronger capacitance-sensitive or resonant region of the
current geometry lies above the present 26.6 GHz upper simulation boundary.
**Basis.** On the current geometry the endpoint curves separate slightly more
near 26.5 to 26.6 GHz than near 26.104 GHz. That is a weak trend at the edge of
the simulated interval.
**What would test it.** CL-P1.
**Status.** hypothesis. **Confidence.** low. Nothing in this repository
establishes that a resonance exists above 26.6 GHz.

### CL-H2 Weak aperture coupling into the resonant stripline

**Hypothesis.** The incident field couples only weakly from the patch and slot
into the Layer-3 resonant stripline, so changing the varactor capacitance has
little effect on the externally reflected phase even though the lumped element
is electrically active.
**Basis.** CL-13. The surface-current maximum sits at the Layer-2 level and is
two orders of magnitude larger than the current on the resonant path. This is
consistent with the hypothesis but does not establish it, because a resonant
path can carry modest current and still control the reflected phase.
**What would test it.** CL-P2, and a comparison of the resonant-path current
between capacitance states.
**Status.** hypothesis. **Confidence.** low to medium.

---

## Planned work

### CL-P1 Wider-frequency endpoint diagnostic

Run both capacitance endpoints on the unchanged current geometry over a
frequency interval wider than 25.6 to 26.6 GHz, before any further geometry
change. The bounds have not been chosen. Extending the sweep requires
re-checking the `Astra_MT77` material fit range.
**Status.** planned. Not run.

### CL-P2 Capacitance comparison of the field monitors

Repeat the E-field and surface-current monitors at 26.104 GHz on the same
geometry at `varC = 0.19 pF` and compare against the existing 0.025 pF result,
using the same fixed colour scale and camera position.
**Status.** planned. Not run. Only the 0.025 pF field result exists.

### CL-P3 Sensitivity test of the assumed via dimensions

Vary `viaD` and `viaClearD` around their assumed values and record the effect on
the reflection response, to bound the error introduced by CL-A1 and CL-A2.
**Status.** planned. Not run.

---

## Evidence gaps

These are things the report must not assert because the supporting record is
missing.

1. Per-variant numerical records for the `slotW` and `lineV` sensitivity runs.
   The initial and final parameter values are known. The individual convergence
   deltas and phase readings for the intermediate variants are not in the
   supplied evidence. See [experiment_log.md](experiment_log.md).
2. Exact adaptive-mesh delta values for the current `slotL = 2.32 mm` endpoint
   pair. The evidence states that both satisfy the approximately 0.01 criterion
   but does not give the two numbers.
3. Numerical phase separation, in degrees, between the current endpoint curves
   at 26.5 to 26.6 GHz. Described as some additional separation, not measured.
4. Any result above 26.6 GHz. None exists.
5. The exact varactor part variant. See the ambiguity recorded in CL-S6.
6. The incidence angle used in the source's own unit-cell simulation. The 2022
   paper states that the element was optimised in a unit-cell configuration but
   does not give the incidence angle for that simulation. This project uses
   normal incidence. The published measurement, by contrast, used a waveguide
   simulator at 21.4 degrees.

Gap 5 of the previous revision, independent re-verification of CL-S1 against the
source PDF, is now closed. See CL-S1.
