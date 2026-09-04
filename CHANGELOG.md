# Changelog

All notable changes to this repository. Newest first.

The format follows the spirit of Keep a Changelog. Because this repository is a
research record rather than a released product, entries also note when a claim
changed status in `docs/claims_ledger.md`.

## Report restructured as a concise academic working draft

Branch `report/academic-restructure-v2`.

### Changed

- The report was rebuilt around the engineering narrative rather than around the
  order the debugging happened in: reference design, operating principle,
  reconstruction, parameterisation, numerical model, verification, current
  status, ongoing work. Main text is sections 1 to 10, roughly 14 pages
  including figures.
- The DOCX and PDF in `deliverables/` are now the documents intended for
  readers. Markdown is kept only as a generated mirror for readable diffs.
- Standalone main-text sections for the slot-width, `lineV` and slot-length
  experiments were removed. Section 7.3 covers all three in one paragraph and a
  four-column table, and the branch history moved to Appendix D.
- The abstract is now a marked placeholder, and the conclusion was replaced by a
  short interim status section, because the investigation is still open.

### Added

- `tools/report_build/`, a reproducible two-pass build. The first pass renders
  the DOCX and converts it with LibreOffice, the second re-renders it with page
  numbers read back from that PDF, so the contents, list of figures and list of
  tables are correct without a field refresh.
- Appendix A, a 71-entry inventory of every named CST parameter with its
  expression, resolved value, purpose and origin.
- Figures 1 and 2, reproduced from the 2022 source paper, and Figure D.1 from
  the 2020 precursor. Both papers are CC BY 4.0, verified from page 1 of each
  publisher PDF. Attribution is in `figures/source/ATTRIBUTION.md`.
- Bordered, correctly sized placeholder boxes for the five figures that require
  CST captures, each naming what must be exported.

### Claim status changes

- CL-S1 moved from provisional to confirmed. The 337 degree simulated phase
  shift was verified in Section 2 of the 2022 paper.
- CL-S3 to CL-S10 added, recording what the source papers actually publish. The
  most consequential is CL-S3: Table 1 of the 2022 paper publishes twelve
  dimensions and the reconstruction baseline reproduces every one exactly.
- CL-S7 records that `fRef = 26.104 GHz` and the 25.6 to 26.6 GHz interval come
  from the source's own waveguide-simulator measurement, so neither was an
  arbitrary project choice.
- CL-S9 records that the 2020 element is a different design, with an 8 mm cell
  on a different substrate and a 340 degree phase range. The 337 and 340 degree
  figures belong to different elements and were previously at risk of being
  conflated.
- CL-A6 upgraded: the bias-line and radial-stub arrangement is confirmed against
  Figure 1 of the 2022 paper rather than assumed. Only the sign convention
  remains a modelling choice.
- CL-S6 records a new open ambiguity. The two papers name different varactor
  part variants and the pad geometry in the model came from a third.
- Evidence gap 5, re-verification of CL-S1, is closed. Two new gaps replace it:
  the varactor part variant, and the incidence angle used in the source's own
  unit-cell simulation.

### Removed from the main text

- The geometry-sensitivity comparison figure. The per-variant records for the
  `slotW` and `lineV` branches were never archived, so it cannot be produced.

### Preserved

- `archive/report_v1_longform.md` and `archive/report_v1_sections/` hold the
  previous revision in full.

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
- Report sections 1 to 11, references and appendices A to F, with an assembly
  script to rebuild the document from them. Both are now in `archive/`.
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
