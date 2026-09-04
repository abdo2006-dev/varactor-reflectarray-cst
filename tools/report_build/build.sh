#!/usr/bin/env bash
# Build the DOCX and PDF deliverables reproducibly.
#
#   ./tools/report_build/build.sh
#
# Requires python-docx and PyMuPDF (both pip-installable) and LibreOffice for
# the PDF conversion. No network access is used.
#
# Two passes are run. The first produces a PDF whose page numbers are then read
# back, so that the contents, list of figures and list of tables carry correct
# page numbers in the second pass. This avoids relying on a field refresh.
set -euo pipefail

cd "$(dirname "$0")/../.."
ROOT="$PWD"
OUT="$ROOT/deliverables"
BASE="Varactor_Reflectarray_CST_Report_Working_Draft"
DOCX="$OUT/$BASE.docx"
PDF="$OUT/$BASE.pdf"
WORK="$OUT/.build"

SOFFICE="${SOFFICE:-/Applications/LibreOffice.app/Contents/MacOS/soffice}"
[ -x "$SOFFICE" ] || SOFFICE="$(command -v soffice)"

mkdir -p "$OUT" "$WORK"

echo "==> pass 1: render without page numbers"
python3 tools/report_build/build_docx.py "$DOCX"

echo "==> pass 1: convert to PDF"
"$SOFFICE" --headless --norestore --convert-to pdf --outdir "$WORK" "$DOCX" >/dev/null

echo "==> derive page map"
python3 tools/report_build/page_map.py \
    "$WORK/$BASE.pdf" "$OUT/$BASE.outline.json" "$WORK/page_map.json"

echo "==> pass 2: render with page numbers"
python3 tools/report_build/build_docx.py "$DOCX" "$WORK/page_map.json"

echo "==> pass 2: convert to PDF"
"$SOFFICE" --headless --norestore --convert-to pdf --outdir "$OUT" "$DOCX" >/dev/null

echo "==> markdown mirror"
python3 tools/report_build/build_markdown.py report/report_working_draft.md

echo "==> done"
ls -la "$DOCX" "$PDF"
