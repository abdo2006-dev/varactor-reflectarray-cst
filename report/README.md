# Report source

The documents intended for readers are in [`../deliverables/`](../deliverables):

- `Varactor_Reflectarray_CST_Report_Working_Draft.docx`
- `Varactor_Reflectarray_CST_Report_Working_Draft.pdf`

## How the report is built

The report text lives in [`../tools/report_build/report_content.py`](../tools/report_build/report_content.py)
as structured data, separate from the code that renders it. That keeps captions
tied to the configuration they came from and stops the DOCX, the PDF and the
Markdown mirror from drifting apart.

```bash
./tools/report_build/build.sh
```

The build runs two passes. The first renders the DOCX and converts it, the second
re-renders it with the page numbers read back from that PDF, so the contents,
list of figures and list of tables are correct in the PDF without needing a field
refresh. The DOCX still uses real Word styles and stays editable.

Requirements: `python-docx`, `PyMuPDF`, and LibreOffice for the PDF conversion.
No network access is used and no font files are embedded or redistributed.

## Markdown mirror

[`report_working_draft.md`](report_working_draft.md) is generated so that report
changes show up as readable diffs. It is not the deliverable and should not be
edited by hand.

## Previous revision

The longform revision that preceded the academic restructure is preserved in
[`../archive/`](../archive):

- `report_v1_longform.md`, the assembled document
- `report_v1_sections/`, its per-section sources and assembly script

It was archived rather than deleted because it carries the detailed chronological
material that the current main text deliberately summarises. The authoritative
record of that history is [`../docs/experiment_log.md`](../docs/experiment_log.md).
