#!/usr/bin/env bash
# Rebuild report.md from the files in sections/.
# The section files are the single source of truth. Edit those, then run this.
set -euo pipefail
cd "$(dirname "$0")"

OUT=report.md
: > "$OUT"

for f in sections/00_front_matter.md \
         sections/01_introduction.md \
         sections/02_design_objectives.md \
         sections/03_architecture_modeling.md \
         sections/04_simulation_methodology.md \
         sections/05_reconstruction.md \
         sections/06_results.md \
         sections/07_field_analysis.md \
         sections/08_current_interpretation.md \
         sections/09_limitations.md \
         sections/10_future_work.md \
         sections/11_conclusion.md \
         sections/98_references.md \
         sections/99_appendices.md ; do
  cat "$f" >> "$OUT"
  printf '\n\n' >> "$OUT"
done

echo "Wrote $OUT ($(wc -l < "$OUT") lines)"
