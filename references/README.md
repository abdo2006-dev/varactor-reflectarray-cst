# References

## Source material policy

The source PDFs are not committed to this repository. They are published
articles held under the terms their publishers set, and redistributing them
through a code repository is not something this project has permission to do.
The `.gitignore` excludes `references/pdf/` and `*.pdf` for that reason.

The PDFs are held locally, outside this repository, in the project's source
library.

Numbering here is local to this file. The report numbers its own reference list
in citation order, which is not the same order.

## Foundational reference

[0] J. Huang and J. A. Encinar, *Reflectarray Antennas*, M. E. El-Hawary, Ed.
New York, NY, USA: Wiley-IEEE Press, 2008, doi: 10.1002/9780470178775.

Used for general reflectarray background only. Both design-source articles cite
it, and these details were transcribed from their reference lists. The book
itself has not been consulted.

## Design source

The reference design for this reconstruction is the varactor-tuned reflectarray
element reported in the two articles below. Both are open-access articles in
*Advances in Radio Science*, distributed under CC BY 4.0.

[1] T. Harz, T. Kleine-Ostmann, and T. Schrader, "Design of a continuously
tunable reflectarray element for 5G metrology in the k-band," *Advances in Radio
Science*, vol. 18, pp. 1 to 5, Dec. 2020, doi: 10.5194/ars-18-1-2020.

[2] T. Harz and T. Kleine-Ostmann, "Measurement and optimization of a
continuously tunable 10 x 10 reflectarray antenna for 5G metrology in the
K-band," *Advances in Radio Science*, vol. 19, pp. 215 to 220, Jan. 2022,
doi: 10.5194/ars-19-215-2022.

Both PDFs were read in full on 2026-09-04 and their details, dimension table,
phase figures, material specification and licence terms were verified directly.
See `docs/claims_ledger.md`, entries CL-S1 to CL-S12.

## Other sources used

[3] MACOM MAVR-011020-1411 flip-chip varactor diode datasheet, recorded here as
Case Style 1500. Used only for package outline dimensions, to approximate a PCB
land pattern the design source does not publish.

**Unresolved.** [1] prints `MAVR-011020-141` and [2] prints `MAVR-011020-111`.
Neither string was found in MACOM or distributor catalogues on 2026-09-05.
`MAVR-011020-1411` is catalogued, as a flip-chip hyperabrupt varactor rated
0.025 pF at 1 MHz and 15 V, which matches the capacitance range both papers
quote; its mechanical outline could not be retrieved, so the correspondence
between the outline used here and the part the papers name is unproven. See
`docs/claims_ledger.md`, CL-S6, and Appendix F, item 1, of the report.

[4] Dassault Systemes, CST Studio Suite 2023. University Teaching License.

## Citation TODO

Nothing in this list may be replaced with a plausible-looking substitute. If a
detail is unknown, it stays marked.

- [x] Confirm the bibliographic details of [1] and [2] against the PDFs. Done
      2026-09-04.
- [x] Attach a figure or table number to every in-text use of [1] and [2]. Done;
      no `[CITATION REQUIRED]` marker remains in the report.
- [x] Re-verify the 337 degree figure directly against [2]. Done; CL-S1 is
      confirmed, and the 340 degree figure belongs to the different element of
      [1].
- [ ] Resolve the part variant of [3], then add its revision number and access
      date. Until then the pad dimensions stay an explicit assumption.
- [ ] Retrieve the mechanical outline drawing for whichever variant is correct
      and compare it with `varPadW`, `varPadL` and `varTermSep`.
- [ ] Confirm the page range of the Hannan and Balfour 1965 article. The
      reference list of [2] prints an implausible one, so the report gives no
      page range for it.
- [ ] Add the citation form the university licence expects for CST [4].
- [ ] Decide the citation style for the final report. The current entries are
      IEEE-like but have not been made consistent.
