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
