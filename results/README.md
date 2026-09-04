# Results

Exported numerical results from the CST runs.

## Layout

`raw/` holds data exactly as CST exported it, with no editing. One
subdirectory per run, named after the branch and capacitance state used in
`docs/experiment_log.md`.

`processed/` holds derived data: overlays, phase differences between endpoint
states, and any unwrapped phase. Every processed file names the raw files it
came from.

## Current status

Both directories are empty.

The results in the report were read from CST plots rather than exported, and are
stated as approximate throughout. That is a known limitation, recorded in
Section 9.4 of the report and as an evidence gap in `docs/claims_ledger.md`.

Setting up the S-parameter export is listed as prerequisite work in Section 10.4
of the report. It should be done before the next endpoint pair is run, so that
run produces data rather than screenshots.

## What to export, when the export is set up

For each capacitance state, across the simulated interval:

- magnitude of `SZmax(1),Zmax(1)` in dB against frequency
- phase of `SZmax(1),Zmax(1)` in degrees against frequency
- energy balance against frequency
- the final adaptive-mesh delta for the run

Record alongside each export: the geometry values `lineV`, `slotW`, `slotL`, the
capacitance, the frequency interval, and the checkpoint filename.
