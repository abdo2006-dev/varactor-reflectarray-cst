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
