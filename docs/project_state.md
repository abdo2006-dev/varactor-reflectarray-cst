# Project state

Last updated: 2026-09-05

This file records the current authoritative state of the CST model. It is the
first file to read when resuming work. Where an earlier project note conflicts
with this file, this file wins.

## Simulation environment

| Item | Value |
|---|---|
| Solver package | CST Studio Suite 2023, university Teaching License |
| Host | MacBook Pro, 16 GB RAM |
| Guest | Windows 11 ARM virtual machine, roughly 6 to 8 GB available to CST |
| Solver | Frequency domain, tetrahedral mesh, broadband sweep |

## Current geometry under test

| Parameter | Value | Status |
|---|---:|---|
| `lineV` | 1.13 mm | current controlled value |
| `slotW` | 0.35 mm | current controlled value |
| `slotL` | 2.32 mm | current controlled value |
| `lineW` | 0.33 mm | unchanged from the reconstruction baseline |
| `lineS` | 0.20 mm | unchanged from the reconstruction baseline |
| `viaX`, `viaY` | 0, 0 | locked (see [claims_ledger.md](claims_ledger.md), CL-11) |
| `cellX`, `cellY` | 7 mm, 7 mm | unchanged |

The values of `lineV`, `slotW` and `slotL` above are the endpoint of the
geometry sensitivity sequence described in
[experiment_log.md](experiment_log.md). They are project-chosen test values, not
values published by the source design.

## Current reference frequency

`fRef = 26.104 GHz`

## Current simulated frequency interval

Approximately 25.6 to 26.6 GHz. This interval is also the material fit range
declared for `Astra_MT77` in the model.

## Current endpoint capacitances

| State | Value |
|---|---:|
| `Cmin` | 0.025 pF |
| `Cmax` | 0.19 pF |

## Current confirmed result

Both endpoint simulations on the `slotL = 2.32 mm` geometry satisfy the
project's current adaptive-mesh convergence criterion of approximately 0.01 on
the maximum change in all S-parameters between passes.

The two endpoint reflection-phase curves remain almost coincident near
26.104 GHz. Some additional separation appears near the upper end of the
simulated interval, around 26.5 to 26.6 GHz.

The `slotL = 2.32 mm` test did not produce tuning at the target frequency.

## Current hypothesis

The stronger capacitance-sensitive region may lie above the present 26.6 GHz
upper simulation boundary. This is a hypothesis. No simulation above 26.6 GHz
has been run, so nothing in this repository establishes that a resonance exists
there.

## Next experiment

A wider-frequency endpoint diagnostic on the unchanged
`lineV = 1.13`, `slotW = 0.35`, `slotL = 2.32` geometry, run at both
capacitance endpoints, before any further geometry modification.

Exact new frequency bounds: to be decided. They have not been chosen and have
not been run. Extending the sweep also requires re-checking the `Astra_MT77`
material fit range, which is currently declared over 25.6 to 26.6 GHz.

## Source verification status

Both source papers were read directly from the publisher PDFs during the
2026-09-04 report restructure, and the following are now confirmed rather than
carried forward from notes.

- Table 1 of the 2022 paper publishes X, Y, Pw, Sw, Sl, Lw, Lv, Ls, Bl, Bd, Bw
  and Bh. The reconstruction baseline reproduces every one of them exactly. See
  [claims_ledger.md](claims_ledger.md), CL-S3.
- `fRef = 26.104 GHz` and the 25.6 to 26.6 GHz interval are inherited from the
  source's own waveguide-simulator measurement, not chosen independently. See
  CL-S7.
- The published simulated phase shift is 337 degrees for the 2022 element. The
  340 degrees figure belongs to the different 2020 precursor element and the two
  must not be interchanged. See CL-S1 and CL-S9.
- Both papers are distributed under CC BY 4.0, so their figures may be reproduced
  with attribution. See CL-S10 and `figures/source/ATTRIBUTION.md`.
- The varactor part variant is unresolved. The 2022 paper prints
  `MAVR-011020-111`, the 2020 paper prints `MAVR-011020-141`, and the pad
  geometry in the model came from an outline recorded as `MAVR-011020-1411`.
  Only the third is a catalogued MACOM part; the manufacturer's mechanical
  outline could not be retrieved, so the pad dimensions remain an unproven
  assumption. See CL-S6.
- The conductor layer of the bias-T is *not* assigned by the 2022 source. Its
  text and its layer-structure figure give no layer number, and the Layer-3
  label comes from the 2020 precursor's stack-up, which describes a different
  element and whose own text places the bias-T behind the ground layer. The
  model's Layer-3 placement is therefore a reconstruction interpretation. See
  CL-S11 and CL-A8.
- Two model parameter names could not be confirmed: the substrate permittivity
  parameter is recorded as both `espAstra` and `epsAstra`, and `stubHalfH` is
  recorded as both 1.3 mm and `Bw/2`. No CST parameter export exists on the
  build machine. Appendix A of the report flags both rather than guessing.

## Standing rules

1. One controlled change per branch. Change geometry or capacitance, not both.
2. Every branch keeps its own CST checkpoint file. Converged endpoint files are
   never overwritten.
3. A run is not usable for an endpoint comparison until its adaptive-mesh delta
   meets the criterion in [claims_ledger.md](claims_ledger.md), CL-06.
4. An assumed dimension stays labelled as an assumption until a primary source
   confirms it.
5. No dense capacitance sweep until an endpoint pair shows meaningful phase
   separation.
6. A parameter name that the model records disagree about is flagged in the
   report, not silently corrected, until a CST parameter export settles it.
