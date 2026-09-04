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
