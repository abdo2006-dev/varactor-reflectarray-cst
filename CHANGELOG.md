# Changelog

All notable changes to this repository. Newest first.

The format follows the spirit of Keep a Changelog. Because this repository is a
research record rather than a released product, entries also note when a claim
changed status in `docs/claims_ledger.md`.

## Working-report technical wording

Branch `report/academic-restructure-v2`. A small correction pass over the
wording of the corrected draft. No section was added or removed, no page
architecture changed and no technical value changed.

### Changed

- Section 2.1 now attributes the statement that every active and biasing
  component sits behind the ground layer to the 2020 precursor, and separates it
  from the 2022 element reconstructed here, whose bias-T layer the source does
  not assign. Section 3.4's uncertainty wording is untouched.
- Section 4.3 no longer ranks the reconstruction assumptions by likelihood. They
  are described as potential contributors whose influence has not been
  sensitivity-tested.
- Section 7.4 no longer states that the layer-three current is roughly two
  orders of magnitude below the global maximum. That maximum is solver-reported
  and the layer-three level was read off a fixed-scale plot, so the two do not
  support a ratio. The solver value 392.368 A/m and its position are retained.
- Appendix A was split. Table A.1 holds the 67 parameters believed to belong to
  the current reconstruction; Table A.2 holds the 12 entries that are pre-rebuild
  captures, superseded constructions, disputed names or unverified historical
  names. All 79 parameter names are preserved. Both tables state that a direct
  CST parameter export is still needed before A.1 can be called authoritative.
- The Appendix D entry for the source-topology rebuild no longer says the
  retained topology corrections were kept for source-fidelity reasons. The
  Layer-3 bias-T placement is named as the current reconstruction interpretation
  and tracked as an unresolved ambiguity. CL-R7 updated to match.
- Figure D.1's caption now states that the figure was used as supporting
  evidence for the qualitative bias-T topology and the lateral stub orientation,
  and that its numerical dimensions belong to the 2020 precursor and were not
  transferred as dimensions of the 2022 cell.

### Fixed

- Appendix subsection headings render as A.1 and A.2 rather than taking the
  main-text counter. They are deliberately kept out of the contents: two more
  entries pushed a single line of it onto a page of its own.

## Academic layout and source-ambiguity corrections

Branch `report/academic-restructure-v2`. A targeted correction pass over the
restructured draft; the v2 architecture is unchanged.

### Changed

- Section 4.2 and its table were removed. Table 1 already carried the published
  value, the current value and the status for each displaced parameter, so the
  subsection restated what the table above it said. One sentence under Table 1
  now names the three temporary investigation settings. Tables renumbered.
- Wording that read as though the *current* model reproduced all published
  geometry was corrected throughout Sections 4, 8 and 10 and in `README.md`. The
  accurate statement is that the baseline implements every published dimension
  and that the current diagnostic checkpoint departs from three of them by
  design.
- Section 3.4 was rewritten. The Layer-3 bias-T placement is now presented as a
  reconstruction interpretation rather than a published assignment, with the
  evidence on both sides stated.
- Appendix A was redesigned with separate baseline and current columns, so a
  value produced at the baseline is never shown as the value at the present
  checkpoint. Values derived from `lineV` now carry both. The inventory grew
  from 71 to 79 parameters after checking names against the model records.
- Section 7.3 stayed compact; no experiment detail was restored to the main
  text.
- A conservative prose pass removed text that repeated a caption or a later
  section, in Sections 1, 2.1, 2.3, 3.1, 5.2, 5.3, 5.4, 6.2, 7.1, 7.2, 7.4 and
  9. Main-body prose is about 4200 words over 14 pages.

### Added

- Reference [1], Huang and Encinar, *Reflectarray Antennas*, Wiley-IEEE Press,
  2008, cited once in the Introduction for the general reflectarray concept. Its
  details were transcribed from the reference lists of the two source papers,
  which both cite it. All other citations shifted by one.
- `tools/report_build/build_manifest.py`, which regenerates
  `docs/figure_manifest.md` from the report content so captions cannot drift.
- Claims `CL-S11` (the 2022 source assigns no conductor layer to the bias-T) and
  `CL-S12` (the foundational reference). New assumption `CL-A8` records the
  Layer-3 bias-T placement as an open interpretation.
- Evidence gaps 7 to 10: the bias-T layer, the `espAstra` / `epsAstra` spelling,
  the disputed `stubHalfH`, and the pre-rebuild Layer-6 bias parameters.

### Fixed

- List-of-figures entries were truncated mid-number, because they were cut at
  the first full stop of the caption. Figures and tables now carry an explicit
  short form for the lists; the full caption still appears under the figure.
- Front-matter page numbers were wrong for some entries. The page map located a
  figure by its label alone, which matched a prose cross-reference at the end of
  a sentence first. It now matches the opening words of the rendered caption.
  All 60 entries were re-checked against the printed pages after the final
  build.
- The nomenclature no longer spills a single entry onto a near-empty page: the
  short list entries let the lists and the nomenclature share one page, and the
  rows are bound together.
- Table columns no longer collapse. Tables now declare a fixed layout, so a long
  cell cannot widen its column and squeeze short words into broken letters.
- A long table can no longer break immediately after its header or just before
  its last row.
- A figure placeholder no longer strands its caption on the following page. The
  box and its caption are rows of one table, because keep-with-next binds row to
  row here but does not bind a table to the paragraph after it.

### Verified

- The MACOM part strings. `MAVR-011020-111` (2022) and `MAVR-011020-141` (2020)
  were read from the publisher PDFs; neither appears in the manufacturer or
  distributor catalogues. `MAVR-011020-1411`, the outline the model's pad
  geometry came from, is a catalogued flip-chip hyperabrupt varactor rated
  0.025 pF at 15 V, but its mechanical outline could not be retrieved, so
  correspondence is unproven and the CST pad geometry is unchanged.
- The bias-T layer evidence, by reading both papers in full and inspecting
  Figure 1 of the 2020 paper and Figure 2 of the 2022 paper as rendered images.
- The 26-page PDF, page by page: front matter, every figure page, the parameter
  tables, the equation, the references and every appendix.

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
