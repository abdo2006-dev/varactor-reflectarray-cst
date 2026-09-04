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
