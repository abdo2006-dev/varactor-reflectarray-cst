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
