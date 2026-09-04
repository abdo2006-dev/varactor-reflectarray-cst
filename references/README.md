# References

## Source material policy

The source PDFs are not committed to this repository. They are published
articles held under the terms their publishers set, and redistributing them
through a code repository is not something this project has permission to do.
The `.gitignore` excludes `references/pdf/` and `*.pdf` for that reason.

The PDFs are held locally, outside this repository, in the project's source
library.

## Design source

The reference design for this reconstruction is the varactor-tuned reflectarray
element reported in the two articles below. Both are open-access articles in
*Advances in Radio Science*.

[1] T. Harz, T. Kleine-Ostmann, and T. Schrader, "Design of a continuously
tunable reflectarray element for 5G metrology in the k-band," *Advances in Radio
Science*, vol. 18, pp. 1 to 5, Dec. 2020, doi: 10.5194/ars-18-1-2020.

[2] T. Harz and T. Kleine-Ostmann, "Measurement and optimization of a
continuously tunable 10 x 10 reflectarray antenna for 5G metrology in the
K-band," *Advances in Radio Science*, vol. 19, pp. 215 to 220, Jan. 2022,
doi: 10.5194/ars-19-215-2022.

These details come from the project's existing verified source index. They have
not been re-checked against the PDFs during this repository build.

## Other sources used

[3] MACOM MAVR-011020-1411 flip-chip varactor diode datasheet, Case Style 1500.
Used only for package outline dimensions, to approximate a PCB land pattern the
design source does not publish. See report Section 3.3.

[4] Dassault Systemes, CST Studio Suite 2023. University Teaching License.

## Citation TODO

Nothing in this list may be replaced with a plausible-looking substitute. If a
detail is unknown, it stays marked.

- [ ] Confirm the bibliographic details of [1] and [2] against the PDFs.
- [ ] Attach a figure or table number to every in-text use of [1] and [2]. The
      report currently carries `[CITATION REQUIRED, ...]` markers at each such
      point. The statements that need them are the layer assignment, the
      description of the resonant mechanism and the roles of `Ls` and `Lv`, the
      bias-T description, the `Bl`, `Bd`, `Bw` and `Bh` values, and the reported
      maximum simulated phase shift of about 337 degrees.
- [ ] Re-verify the 337 degree figure directly against [2]. It is currently
      recorded as provisional in `docs/claims_ledger.md`, entry CL-S1.
- [ ] Add the revision number and access date for the MACOM datasheet [3].
- [ ] Add the citation form the university licence expects for CST [4].
- [ ] Decide the citation style for the final report. The current entries are
      IEEE-like but have not been made consistent.
