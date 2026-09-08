# Project state

Last updated: 2026-09-08

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
| `patchW` | 2.30 mm | current controlled value; **departs from the published `Pw` = 2.225 mm** |
| `slotW` | 0.35 mm | current controlled value; published `Sw` = 0.26 mm |
| `slotL` | 2.32 mm | current controlled value; published `Sl` = 2.275 mm |
| `lineV` | 1.13 mm | current controlled value; published `Lv` = 1.11 mm |
| `lineW` | 0.33 mm | unchanged from the reconstruction baseline |
| `lineS` | 0.20 mm | unchanged from the reconstruction baseline |
| `viaX`, `viaY` | 0, 0 | locked (see [claims_ledger.md](claims_ledger.md), CL-11) |
| `cellX`, `cellY` | 7 mm, 7 mm | unchanged |

The values of `patchW`, `slotW`, `slotL` and `lineV` above are diagnostic
settings reached by the sensitivity sequence in
[experiment_log.md](experiment_log.md). **They are not optimised dimensions and
they are not the values published by the source design**, which are listed
beside them. Four of the eleven published dimensions are therefore currently
displaced by choice; the reconstruction baseline in
[claims_ledger.md](claims_ledger.md) CL-S3 still reproduces all eleven exactly.

## Current reference frequency

`fRef = 26.104 GHz`

## Current simulated frequency interval

Approximately **25.5 to 28 GHz**, widened from the earlier 25.6 to 26.6 GHz
interval by the G-04 diagnostic below.

The `Astra_MT77` material fit range in the model is still declared over 25.6 to
26.6 GHz, so the sweep now extends beyond the range the material model was fitted
for. The response above 26.6 GHz is therefore a diagnostic indication of where a
capacitance-sensitive feature sits, not a quantitative prediction, and the fit
range must be re-declared before any number is taken from that region.

## Current endpoint capacitances

| State | Value |
|---|---:|
| `Cmin` | 0.025 pF |
| `Cmax` | 0.19 pF |

## Current confirmed result

The wide-frequency endpoint diagnostic (G-04, runs 17 and 18) has been run on the
current geometry at both capacitance endpoints over approximately 25.5 to 28 GHz.

**The varactor does influence the electromagnetic resonance of the complete unit
cell.** Over the wider interval the two endpoint responses are no longer close
everywhere: a capacitance-sensitive resonant region appears near **26.8 GHz**,
where changing `varC` shifts both the reflection-magnitude dip and the rapid
phase transition associated with it. That is a whole-cell effect, and it is the
first direct evidence in this project that the tuning element reaches the
reflected field rather than only being electrically active at its own terminals.

**The published tuning at 26.104 GHz has still not been reproduced.** Near the
intended operating frequency the two endpoint phase responses remain close. The
capacitance-sensitive feature is displaced above the intended operating point,
which is a different situation from the earlier one — the mechanism is now
visible, but it is at the wrong frequency.

**No tuning range in degrees may be read from these plots.** The phase shown by
CST wraps at plus or minus 180 degrees, so a screenshot cannot support a
300-degree-class claim in either direction. The published 337-degree simulated
figure and the 322-degree measured figure remain untouched targets, not results.

## Current hypothesis

The earlier hypothesis CL-H1 — that the stronger capacitance-sensitive region
lies above the previous 26.6 GHz boundary — is now **supported** by G-04, at
approximately 26.8 GHz. What remains open is why the feature sits there rather
than at 26.104 GHz. The candidates are the reconstruction assumptions
(CL-A1 to CL-A8), the four displaced geometry values listed above, weak aperture
coupling (CL-H2), and the ideal-capacitor representation of the varactor. None
of these is established, and they are not ranked.

## Next experiment

1. **Numerical export of the complex S-parameter data** for both endpoints over
   the wide interval, replacing screenshot reading with exported values.
2. **Phase unwrapping and a matched-frequency phase-difference calculation**, so
   the capacitance-dependent phase change can be stated in degrees at a stated
   frequency instead of being read off a wrapped plot.
3. **Re-declaration of the `Astra_MT77` material fit range** to cover the widened
   sweep, before any quantitative result is taken from above 26.6 GHz.
4. **Targeted tests of the reconstruction hypotheses**, beginning with the
   assumed via and ground-clearance dimensions (CL-P3), to see which of them
   moves the resonant feature toward 26.104 GHz.

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
  build machine. Appendix A of the report flags both rather than guessing, and
  holds them in Table A.2 with the other entries that cannot be placed in the
  current model. A direct CST parameter export would settle them.

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
