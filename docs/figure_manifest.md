# Figure manifest

Generated to match the working draft in `deliverables/`. Every figure the
report references is listed with the caption it must carry, the model
configuration it must come from, and its current status.

Regenerate the deliverables with `tools/report_build/build.sh` after adding an
image, so that captions and numbering cannot drift from the source result.

## Rules

1. A plot with `Pass` on the horizontal axis is an adaptive-convergence plot. It
   is never described as a frequency response.
2. A plot with `Frequency / GHz` on the horizontal axis is a frequency response.
   Its caption states the capacitance state and the geometry.
3. Every caption names the configuration: the three controlled geometry values,
   the capacitance, the frequency interval where relevant, and the source result
   or checkpoint file.
4. A field plot caption states the colour-scale range, because a saturated scale
   carries no information.
5. Reproduced source figures carry their attribution in the caption. See
   `figures/source/ATTRIBUTION.md`.

## Main-text figures

### Figure 1

**Status.** present, `figures/source/fig01_harz2022_element_layout.png`

**Caption.** Published layout of the reference antenna element, showing the unit-cell extent X and Y, the patch width Pw, the coupling slot Sw and Sl, the stripline width Lw and its two resonant lengths Lv and Ls, the blind via, the varactor diode position, and the bias line with the radial stub dimensioned by Bl, Bd, Bw and Bh. Reproduced from Harz and Kleine-Ostmann [2], Fig. 1, under the Creative Commons Attribution 4.0 licence.

### Figure 2

**Status.** present, `figures/source/fig02_harz2022_layer_structure.png`

**Caption.** Published six-layer structure of the reference antenna element. The patch sits on layer one, the coupling aperture is the gap in the layer-two conductor, the resonant stripline is on layer three, layer four is the ground plane, and the blind via carries the resonant path down to the varactor on layer six. Reproduced from Harz and Kleine-Ostmann [2], Fig. 2, under the Creative Commons Attribution 4.0 licence.

### Figure 3

**Status.** **required, not yet available**

**What must be captured or exported.** Isometric view of the reconstructed unit cell in CST Studio Suite 2023, with the substrate stack shown semi-transparent so that all six conductor layers, the blind via and the varactor terminal pads are visible. Capture from the current geometry checkpoint (lineV = 1.13 mm, slotW = 0.35 mm, slotL = 2.32 mm).

**Save to.** `figures/cst/cst_iso.png`, then set `path` for `cst_iso` in
`tools/report_build/report_content.py` and rebuild.

**Caption.** Reconstructed unit cell in CST Studio Suite 2023. The model is a 7 mm by 7 mm periodic cell containing six perfect-electric-conductor layers separated by five Astra MT77 substrates, with an ideal lumped capacitor across the layer-six terminal pads representing the varactor.

### Figure 4

**Status.** **required, not yet available**

**What must be captured or exported.** Layer-by-layer or exploded composite view of the reconstruction, one panel per conductor layer L1 to L6, all at the same scale and camera orientation, so that the reconstruction can be compared panel by panel against Figure 1. Capture from the same checkpoint as Figure 3.

**Save to.** `figures/cst/cst_layers.png`, then set `path` for `cst_layers` in
`tools/report_build/report_content.py` and rebuild.

**Caption.** Layer-by-layer view of the reconstruction. L1 carries the square patch, L2 is a conductor sheet interrupted by the rectangular coupling aperture, L3 carries the resonant stripline together with the bias-T branch and radial stub, L4 is the ground plane with a circular clearance around the blind via, L5 carries the DC supply trace, and L6 carries the varactor terminal pads.

### Figure 5

**Status.** **required, not yet available**

**What must be captured or exported.** Export of the CST adaptive-mesh convergence plot, Maximum Delta All S-Parameters against pass number, for one accepted endpoint run on the current geometry. The horizontal axis must read Pass. State in the caption which capacitance state the run belongs to and the final delta value from the solver log rather than from the plot.

**Save to.** `figures/cst/convergence.png`, then set `path` for `convergence` in
`tools/report_build/report_content.py` and rebuild.

**Caption.** Representative adaptive tetrahedral mesh convergence for one accepted endpoint run on the current geometry. The horizontal axis is the refinement pass number, not frequency. The acceptance criterion used throughout this project is a final Maximum Delta All S-Parameters of approximately 0.01 or below.

### Figure 6

**Status.** **required, not yet available**

**What must be captured or exported.** Overlay of the reflection phase of SZmax(1),Zmax(1) against frequency for varC = 0.025 pF and varC = 0.19 pF on the current geometry over approximately 25.6 to 26.6 GHz, with 26.104 GHz marked. Export the underlying numerical data at the same time so that the separation can be stated in degrees.

**Save to.** `figures/cst/endpoint_phase.png`, then set `path` for `endpoint_phase` in
`tools/report_build/report_content.py` and rebuild.

**Caption.** Reflection phase of the co-polarised term SZmax(1),Zmax(1) at the two capacitance endpoints on the current geometry (lineV = 1.13 mm, slotW = 0.35 mm, slotL = 2.32 mm), over approximately 25.6 to 26.6 GHz. Both runs satisfy the convergence criterion of Section 5.3. The reference frequency 26.104 GHz is marked.

### Figure 7

**Status.** **required, not yet available**

**What must be captured or exported.** Surface-current magnitude plot at 26.104 GHz from the field-audit run at varC = 0.025 pF, rescaled to a fixed 0 to 5 A/m range so that the layer-three resonant path is visible. Use a camera position that can be repeated for the planned 0.19 pF counterpart.

**Save to.** `figures/cst/surface_current.png`, then set `path` for `surface_current` in
`tools/report_build/report_content.py` and rebuild.

**Caption.** Surface-current magnitude at 26.104 GHz for varC = 0.025 pF, plotted on a fixed 0 to 5 A/m colour scale so that the resonant path is visible. The global maximum reported by the solver for this run is 392.368 A/m, located at approximately (1.138, -0.130, -0.254) mm, which is the layer-two level. The fixed scale saturates the aperture region by construction and the plot is therefore a qualitative distribution, not a calibrated field export.

## Appendix figures

### Figure C.1

**Status.** **required, not yet available**

**What must be captured or exported.** Per-branch adaptive-convergence plots for the accepted Stage-B and diagnostic branches listed in Table C.1, one panel per branch, all with Pass on the horizontal axis.

**Save to.** `figures/cst/convergence_appendix.png`, then set `path` for `convergence_appendix` in
`tools/report_build/report_content.py` and rebuild.

**Caption.** Per-branch adaptive-mesh convergence records for the branches in Table C.1.

### Figure D.1

**Status.** present, `figures/source/figD1_harz2020_biasT_dimensions.png`

**Caption.** Bias-T dimensions and port definitions for the 2020 precursor element. The radial stub branches laterally from the bias line rather than continuing along it, which is the reading that corrected the stub orientation and dimensioning in this reconstruction. Note that the numerical dimensions belong to the 2020 element and not to the element reconstructed here. Reproduced from Harz et al. [1], Fig. 5, under the Creative Commons Attribution 4.0 licence.

### Figure E.1

**Status.** **required, not yet available**

**What must be captured or exported.** Overlay of the reflection magnitude of SZmax(1),Zmax(1) against frequency at varC = 0.025 pF and 0.19 pF on the current geometry, same runs as Figure 6.

**Save to.** `figures/cst/magnitude_appendix.png`, then set `path` for `magnitude_appendix` in
`tools/report_build/report_content.py` and rebuild.

**Caption.** Reflection magnitude at the two capacitance endpoints on the current geometry, same runs as Figure 6. Discussed in Section 7.2.

### Figure E.2

**Status.** **required, not yet available**

**What must be captured or exported.** Electric-field magnitude at 26.104 GHz on a fixed non-saturating scale, starting near 0 to 10000 V/m, with the same camera position as Figure 7. The existing capture saturates and carries no information, so it must be regenerated before use.

**Save to.** `figures/cst/efield_appendix.png`, then set `path` for `efield_appendix` in
`tools/report_build/report_content.py` and rebuild.

**Caption.** Electric-field magnitude at 26.104 GHz for varC = 0.025 pF on a fixed non-saturating colour scale.

## Blocked items

- The geometry-sensitivity comparison that the previous report revision listed as
  Figure 7 has been dropped from the main text. The per-variant results for the
  `slotW` and `lineV` branches were never archived, so the figure cannot be
  produced. Section 7.3 of the report presents those branches as a short table
  instead, and the missing records are recorded as an evidence gap in
  `claims_ledger.md`.
- Figure E.2 cannot use the existing electric-field capture, which saturates. A
  fixed range starting near 0 to 10000 V/m is needed, with the same camera
  position as Figure 7.
- Figure 7 needs its 0.19 pF counterpart before the report can say anything about
  how the field distribution changes with capacitance. That run is planned, not
  done. See CL-P2.

## Note on availability

No CST screenshot or result export exists anywhere on the build machine. The
model and its results live in the Windows virtual machine that runs CST, so every
figure marked required above has to be captured there and copied into
`figures/cst/`. The report reserves correctly sized placeholder boxes for them,
so the page layout will not shift much when the images arrive.
