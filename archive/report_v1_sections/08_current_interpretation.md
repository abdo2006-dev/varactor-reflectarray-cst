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
