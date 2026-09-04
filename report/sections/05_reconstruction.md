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
