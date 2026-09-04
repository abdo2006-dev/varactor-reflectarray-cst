# Figure manifest

Every figure the report references is listed here with the caption it must
carry, the model configuration it must come from, and its current status.

No figure files have been produced yet. Every entry below is `required`. The
report contains a placeholder at each figure position and states the
configuration in the caption, so that the caption cannot drift from the source
result once the image is added.

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
5. Debug screenshots and individual per-branch convergence runs belong in the
   appendices, not in the main text.

## Main-text figures

| No. | Subject | Target path | Source configuration | Status |
|---|---|---|---|---|
| 1 | Plan view of the four RF layers: patch, slot layer, stripline with bias-T branch, ground with via clearance | `figures/architecture/fig01_unit_cell_plan.*` | Current geometry, `lineV = 1.13`, `slotW = 0.35`, `slotL = 2.32 mm`, 7 mm cell | required |
| 2 | Exploded or side view of the six conductor layers and five substrates, annotated with the z coordinates | `figures/architecture/fig02_layer_stack.*` | Same model, dimensions from Appendix A | required |
| 3 | Bias network detail: blind via, Layer-4 clearance, Layer-6 varactor terminal pads and lumped-element markers, Layer-5 DC supply trace, Layer-3 bias-T branch and radial stub | `figures/geometry/fig03_bias_network.*` | Same model | required |
| 4 | Adaptive convergence, `Maximum Delta All S-Parameters` against pass number, with the 0.01 criterion marked | `figures/convergence/fig04_convergence.*` | One endpoint run of the current geometry. Horizontal axis is `Pass`, not frequency | required |
| 5 | Reflection phase of `SZmax(1),Zmax(1)` against frequency, both capacitance endpoints overlaid | `figures/results/fig05_endpoint_phase.*` | Current geometry, `varC = 0.025` and `0.19 pF`, approximately 25.6 to 26.6 GHz, `fRef = 26.104 GHz` marked | required |
| 6 | Reflection magnitude of `SZmax(1),Zmax(1)` against frequency, both capacitance endpoints overlaid | `figures/results/fig06_endpoint_magnitude.*` | Same runs as Figure 5 | required |
| 7 | Endpoint phase separation compared across the geometry-sensitivity variants | `figures/results/fig07_geometry_sensitivity.*` | Requires the archived per-variant results for `slotW` and `lineV`. See the evidence gap in the claims ledger | required, blocked |
| 8 | Surface-current magnitude at 26.104 GHz on a fixed 0 to 5 A/m scale, with the global maximum stated in the caption | `figures/fields/fig08_surface_current.*` | Field-audit run, `varC = 0.025 pF`, monitor at 26.104 GHz | required |

## Appendix figures

| No. | Subject | Target path | Status |
|---|---|---|---|
| C.1 | Per-branch adaptive-convergence plots for the accepted Stage-B and hypothesis branches | `figures/convergence/appendix/` | required |
| D.1 | Geometry of the rejected diagnostic variants, one view each | `figures/geometry/appendix/` | required |
| E.1 | E-field magnitude at 26.104 GHz on a fixed non-saturating scale | `figures/fields/appendix/` | required. The existing capture saturates and must be regenerated before use |

## Blocking notes

- Figure 7 cannot be produced from the current record. The per-variant
  results for the `slotW` and `lineV` experiments are not archived in this
  repository.
- Figure E.1 cannot use the existing capture. A fixed range starting near
  0 to 10000 V/m is needed, with the same camera position as the surface-current
  plot.
- Figure 8 needs its 0.19 pF counterpart before the report can say anything
  about how the field distribution changes with capacitance. That run is
  planned, not done.
