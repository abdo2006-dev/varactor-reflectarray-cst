# Figure manifest

Generated from `tools/report_build/report_content.py` by
`tools/report_build/build_manifest.py`. Every figure the report references is
listed with the caption it must carry, the model configuration it must come
from, and its current status.

Add an image, point the figure's `path` at it, then rerun this script and
`tools/report_build/build.sh`, so that captions and numbering cannot drift from
the source result.

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
6. The short form in the `short` field is what the report's list of figures
   prints. The full caption below is what appears under the figure.

## Main-text figures

### Figure 1

**Status.** present, `figures/source/fig01_harz2022_element_layout.png`

**Reserved height.** 4.15 in

**List-of-figures entry.** Published layout of the reference element

**Caption.** Published layout of the reference antenna element, showing the unit-cell extent X and Y, the patch width Pw, the coupling slot Sw and Sl, the stripline width Lw and its two resonant lengths Lv and Ls, the blind via, the varactor diode position, and the bias line with the radial stub dimensioned by Bl, Bd, Bw and Bh. Reproduced from Harz and Kleine-Ostmann [3], Fig. 1, under the Creative Commons Attribution 4.0 licence.

### Figure 2

**Status.** present, `figures/source/fig02_harz2022_layer_structure.png`

**Reserved height.** 1.35 in

**List-of-figures entry.** Published six-layer architecture

**Caption.** Published six-layer structure of the reference antenna element. The patch sits on layer one, the coupling aperture is the gap in the layer-two conductor, the resonant stripline is on layer three, layer four is the ground plane, and the blind via carries the resonant path down to the varactor on layer six. Reproduced from Harz and Kleine-Ostmann [3], Fig. 2, under the Creative Commons Attribution 4.0 licence.

### Figure 3

**Status.** present, `figures/model/model_isometric.png`

**Reserved height.** 3.00 in

**List-of-figures entry.** CST reconstruction of the unit cell

**Caption.** Reconstructed unit cell in CST Studio Suite 2023, shown inside the bounding box of the periodic simulation domain. The model is a 7 mm by 7 mm cell containing six perfect-electric-conductor layers separated by five Astra MT77 substrates, with an ideal lumped capacitor across the layer-six terminal pads representing the varactor. The substrates are drawn semi-transparent and the square layer-one patch is visible on the front face; the open space above and below the stack is the region through which the Floquet excitation enters and leaves.

### Figure 4

**Status.** present, `figures/model/model_layer_stack.png`

**Reserved height.** 3.00 in

**List-of-figures entry.** Conductor layers of the reconstruction, seen in depth

**Caption.** The same model viewed close to edge-on, so that the conductor layers are separated in depth rather than superimposed. Reading downward: the square patch on L1, the L2 conductor interrupted by the rectangular coupling aperture, the L3 stripline with its bias-T branch and radial stub, the L4 ground plane with the circular clearance around the blind via, and the L5 and L6 routing carrying the lumped varactor, visible below the stack. This is a single oblique capture rather than a per-layer exploded set, so the layers are identified by their depth order, not shown in isolation.

### Figure 5

**Status.** present, `figures/model/model_via_detail.png`

**Reserved height.** 2.90 in

**List-of-figures entry.** Blind via through the ground-plane clearance

**Caption.** The blind via crossing the layer-four ground plane. The circular clearance around the via, drawn here as the light ring, is what keeps the resonant path isolated from the ground plane as it passes through it. The lumped element representing the varactor is the darker collar on the lower part of the via, at the layer-six terminal pads. The clearance diameter is not published and is a reconstruction assumption; see Appendix F.

### Figure 6

**Status.** present, `figures/model/model_bias_network_detail_2.png`

**Reserved height.** 2.20 in

**List-of-figures entry.** Bias network with the surrounding layers hidden

**Caption.** The bias network with the substrates and the sheet conductors hidden, so that the routing can be followed. The blind via descends from the layer-three stripline, through its ground-plane clearance, to the terminal pads carrying the lumped varactor; the bias line continues away from the junction and the radial stub branches laterally from it. This lateral branching, rather than a stub continuing along the bias line, is the reading taken from Figure 1 and supported by Figure D.1.

### Figure 7

**Status.** **required, not yet available**

**What must be captured or exported.** Export of the CST adaptive-mesh convergence plot, Maximum Delta All S-Parameters against pass number, for one accepted endpoint run on the current geometry. The horizontal axis must read Pass. State in the caption which capacitance state the run belongs to and the final delta value from the solver log rather than from the plot.

**Save to.** `figures/cst/convergence.png`, then set `path` for `convergence` in
`tools/report_build/report_content.py` and rebuild.

**Reserved height.** 2.90 in

**List-of-figures entry.** Representative adaptive-mesh convergence

**Caption.** Representative adaptive tetrahedral mesh convergence for one accepted endpoint run on the current geometry. The horizontal axis is the refinement pass number, not frequency. The acceptance criterion used throughout this project is a final Maximum Delta All S-Parameters of approximately 0.01 or below.

### Figure 8

**Status.** present, `figures/results/g04_reflection_magnitude.png`

**Reserved height.** 2.35 in

**List-of-figures entry.** Endpoint reflection magnitude, wide sweep

**Caption.** Reflection magnitude of SZmax(1),Zmax(1) at the two capacitance endpoints on the current diagnostic geometry, over approximately 25.5 to 28 GHz. Red is varC = 0.19 pF (run 17) and green is varC = 0.025 pF (run 18). A single resonant dip appears near 26.8 GHz and moves with capacitance: approximately 26.86 GHz and -3.3 dB at 0.19 pF against approximately 26.78 GHz and -3.6 dB at 0.025 pF, a shift of roughly 0.08 GHz. This is the clearest evidence in this project that the varactor reaches the resonance of the complete unit cell. Both figures are read from the plot rather than exported from the solver, and the sweep extends beyond the declared Astra MT77 material fit range of 25.6 to 26.6 GHz, so the region is a diagnostic indication rather than a quantitative prediction.

### Figure 9

**Status.** present, `figures/results/g04_reflection_phase.png`

**Reserved height.** 2.35 in

**List-of-figures entry.** Endpoint reflection phase, wide sweep

**Caption.** Reflection phase of the co-polarised term SZmax(1),Zmax(1) at the two capacitance endpoints on the current diagnostic geometry (patchW = 2.30 mm, slotL = 2.32 mm, slotW = 0.35 mm, lineV = 1.13 mm), over approximately 25.5 to 28 GHz. Red is varC = 0.19 pF and green is varC = 0.025 pF. Near the intended 26.104 GHz operating frequency the two traces are drawn on top of one another at approximately -24 degrees and no separation is measurable. They become distinguishable at about 26.3 GHz and reach roughly 7 degrees apart at 26.5 GHz and 13 degrees at 26.6 GHz, before each wraps through the rapid transition that accompanies its own resonance: near 26.85 GHz at 0.19 pF and near 26.77 GHz at 0.025 pF. The displayed phase wraps at plus or minus 180 degrees, so the apparent excursion between the two wrap points is an artefact of the display and no tuning range in degrees is quantified from this plot.

### Figure 10

**Status.** **required, not yet available**

**What must be captured or exported.** Surface-current magnitude plot at 26.104 GHz from the field-audit run at varC = 0.025 pF, rescaled to a fixed 0 to 5 A/m range so that the layer-three resonant path is visible. Use a camera position that can be repeated for the planned 0.19 pF counterpart.

**Save to.** `figures/cst/surface_current.png`, then set `path` for `surface_current` in
`tools/report_build/report_content.py` and rebuild.

**Reserved height.** 3.20 in

**List-of-figures entry.** Surface-current distribution at 26.104 GHz

**Caption.** Surface-current magnitude at 26.104 GHz for varC = 0.025 pF, plotted on a fixed 0 to 5 A/m colour scale so that the resonant path is visible. The global maximum reported by the solver for this run is 392.368 A/m, located at approximately (1.138, -0.130, -0.254) mm, which is the layer-two level. The fixed scale saturates the aperture region by construction and the plot is therefore a qualitative distribution, not a calibrated field export.

## Appendix figures

### Figure C.1

**Status.** **required, not yet available**

**What must be captured or exported.** Per-branch adaptive-convergence plots for the accepted Stage-B and diagnostic branches listed in Table C.1, one panel per branch, all with Pass on the horizontal axis.

**Save to.** `figures/cst/convergence_appendix.png`, then set `path` for `convergence_appendix` in
`tools/report_build/report_content.py` and rebuild.

**Reserved height.** 2.60 in

**List-of-figures entry.** Convergence records for diagnostic branches

**Caption.** Per-branch adaptive-mesh convergence records for the branches in Table C.1.

### Figure D.1

**Status.** present, `figures/source/figD1_harz2020_biasT_dimensions.png`

**Reserved height.** 3.30 in

**List-of-figures entry.** Bias-T geometry of the 2020 precursor element

**Caption.** Bias-T dimensions and port definitions for the 2020 precursor element. The radial stub branches laterally from the bias line rather than continuing along it. The figure was used as supporting evidence for the qualitative bias-T topology and for the lateral orientation of the radial stub. Its numerical dimensions belong to the 2020 precursor element and were not transferred as dimensions of the 2022 cell reconstructed here. Reproduced from Harz et al. [2], Fig. 5, under the Creative Commons Attribution 4.0 licence.

### Figure E.1

**Status.** present, `figures/model/model_side_view.png`

**Reserved height.** 2.70 in

**List-of-figures entry.** Assembled cell seen from the side

**Caption.** The assembled cell viewed from the side within its simulation domain. The five substrates and the conductor layers are seen in section, with the lumped varactor on the far side of the ground plane.

### Figure E.2

**Status.** present, `figures/model/model_front.png`

**Reserved height.** 2.60 in

**List-of-figures entry.** Front view of the model

**Caption.** Front view, looking into the stack along the propagation axis. The layer-three stripline, the blind via, the lumped varactor and the laterally branching radial stub are visible through the semi-transparent conductors. The view label is part of the original screen capture.

### Figure E.3

**Status.** present, `figures/model/model_back.png`

**Reserved height.** 2.60 in

**List-of-figures entry.** Back view of the model

**Caption.** Back view along the same axis, showing the lower conductor layers and the pad pair that carries the varactor. The view label is part of the original screen capture.

### Figure E.4

**Status.** present, `figures/model/model_bias_network_detail_1.png`

**Reserved height.** 2.10 in

**List-of-figures entry.** Bias network from a second angle

**Caption.** The bias network of Figure 6 from a second angle, with the ground-plane clearance ring around the blind via more clearly separated from the radial stub.

### Figure E.5

**Status.** **required, not yet available**

**What must be captured or exported.** Electric-field magnitude at 26.104 GHz on a fixed non-saturating scale, starting near 0 to 10000 V/m, with the same camera position as Figure 10. The existing capture saturates and carries no information, so it must be regenerated before use.

**Save to.** `figures/cst/efield_appendix.png`, then set `path` for `efield_appendix` in
`tools/report_build/report_content.py` and rebuild.

**Reserved height.** 2.30 in

**List-of-figures entry.** Electric-field distribution at 26.104 GHz

**Caption.** Electric-field magnitude at 26.104 GHz for varC = 0.025 pF on a fixed non-saturating colour scale.

## Blocked items

- The geometry-sensitivity comparison that the first report revision listed as a
  figure has been dropped from the main text. The per-variant results for the
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
