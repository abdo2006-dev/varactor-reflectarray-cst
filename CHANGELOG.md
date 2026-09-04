# Changelog

All notable changes to this repository. Newest first.

The format follows the spirit of Keep a Changelog. Because this repository is a
research record rather than a released product, entries also note when a claim
changed status in `docs/claims_ledger.md`.

## [Unreleased]

### Added

- Repository structure, `.gitignore` covering CST solver output and virtual
  machine artefacts, and an MIT licence.
- `docs/project_state.md` recording the current geometry
  (`lineV = 1.13`, `slotW = 0.35`, `slotL = 2.32 mm`), the 26.104 GHz reference
  frequency, the approximately 25.6 to 26.6 GHz simulated interval, the 0.025
  and 0.19 pF capacitance endpoints, the current confirmed result, the open
  hypothesis and the next experiment.
- `docs/claims_ledger.md` with 14 confirmed claims, 2 source claims, 7
  reconstruction assumptions, 7 rejected hypotheses, 2 open hypotheses, 3
  planned experiments and 5 recorded evidence gaps.
- `docs/experiment_log.md` covering the Stage-A baseline, the Stage-B
  construction and endpoint tests, six topology hypotheses, the field audit and
  the three-step geometry sensitivity sequence.
- `docs/figure_manifest.md` specifying 8 main-text figures and 3 appendix
  figures with their required captions and source configurations. All are
  pending. Figure 7 is blocked on missing per-variant records.
- Report sections 1 to 11, references and appendices A to F, with
  `report/assemble.sh` to rebuild `report/report.md` from them.
- Recruiter-facing `README.md`.
- `cst/README.md` explaining the checkpoint convention and why `.cst` files are
  not committed.
- `references/README.md` with the design source citations and an open citation
  TODO list.

### Notes on claim status at this revision

- The `slotL = 2.32 mm` endpoint experiment is recorded as confirmed and as
  having produced no tuning at the target frequency.
- The proposal that the capacitance-sensitive region lies above 26.6 GHz is
  recorded as a hypothesis with low confidence. No simulation above 26.6 GHz
  exists.
- The abstract, Section 8 and Section 11 are marked provisional.
