# -*- coding: utf-8 -*-
"""
Regenerate docs/figure_manifest.md from the report content.

    python3 tools/report_build/build_manifest.py

The manifest used to be maintained by hand, which let its captions drift from
the ones the report actually prints. Generating it from report_content.py keeps
the two in step, so the capture instructions always describe the figure the
current draft expects.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import report_content as C
from build_docx import APP_FIG_LABEL

OUT = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "docs", "figure_manifest.md")

HEAD = """# Figure manifest

Generated from `tools/report_build/report_content.py` by
`tools/report_build/build_manifest.py`. Every figure the report references is
listed with the caption it must carry, the model configuration it must come
from, and its current status.

Add an image, point the figure's `path` at it, then rerun this script and
`tools/report_build/build.sh`, so that captions and numbering cannot drift from
the source result.

## Rules

1. A plot with `Pass` on the horizontal axis is an adaptive-convergence plot. It
   is never described as a frequency response.
2. A plot with `Frequency / GHz` on the horizontal axis is a frequency response.
   Its caption states the capacitance state and the geometry.
3. Every caption names the configuration: the three controlled geometry values,
   the capacitance, the frequency interval where relevant, and the source result
   or checkpoint file.
4. A field plot caption states the colour-scale range, because a saturated scale
   carries no information.
5. Reproduced source figures carry their attribution in the caption. See
   `figures/source/ATTRIBUTION.md`.
6. The short form in the `short` field is what the report's list of figures
   prints. The full caption below is what appears under the figure.
"""

TAIL = """## Blocked items

- The geometry-sensitivity comparison that the first report revision listed as a
  figure has been dropped from the main text. The per-variant results for the
  `slotW` and `lineV` branches were never archived, so the figure cannot be
  produced. Section 7.3 of the report presents those branches as a short table
  instead, and the missing records are recorded as an evidence gap in
  `claims_ledger.md`.
- Figure E.2 cannot use the existing electric-field capture, which saturates. A
  fixed range starting near 0 to 10000 V/m is needed, with the same camera
  position as Figure 7.
- Figure 7 needs its 0.19 pF counterpart before the report can say anything about
  how the field distribution changes with capacitance. That run is planned, not
  done. See CL-P2.

## Note on availability

No CST screenshot or result export exists anywhere on the build machine. The
model and its results live in the Windows virtual machine that runs CST, so every
figure marked required above has to be captured there and copied into
`figures/cst/`. The report reserves correctly sized placeholder boxes for them,
so the page layout will not shift much when the images arrive.
"""


def entry(label, key, spec):
    out = ["### %s\n" % label]
    if spec.get("path"):
        out.append("**Status.** present, `%s`\n" % spec["path"])
    else:
        out.append("**Status.** **required, not yet available**\n")
        out.append("**What must be captured or exported.** %s\n" % spec["need"])
        out.append("**Save to.** `figures/cst/%s.png`, then set `path` for `%s` in\n"
                   "`tools/report_build/report_content.py` and rebuild.\n" % (key, key))
    out.append("**Reserved height.** %.2f in\n" % spec["height"])
    if spec.get("short"):
        out.append("**List-of-figures entry.** %s\n" % spec["short"])
    out.append("**Caption.** %s\n" % spec["caption"])
    return "\n".join(out)


def main():
    # Walk the body and the appendices in render order so the numbering here is
    # the numbering the report prints.
    main_keys = [b[1] for b in C.BODY if b[0] == "fig"]
    app = []
    for letter, title, blocks in C.APPENDICES:
        for b in blocks:
            if b[0] in ("fig", "afig"):
                app.append(b[1])

    parts = [HEAD, "## Main-text figures\n"]
    for i, k in enumerate(main_keys, 1):
        parts.append(entry("Figure %d" % i, k, C.FIGURES[k]))
    parts.append("## Appendix figures\n")
    for k in app:
        spec = C.FIGURES[k] if k in C.FIGURES else C.APPENDIX_FIGURES[k]
        parts.append(entry(APP_FIG_LABEL[k], k, spec))
    parts.append(TAIL)

    with open(os.path.abspath(OUT), "w") as fh:
        fh.write("\n".join(parts))
    print("wrote docs/figure_manifest.md (%d main, %d appendix)"
          % (len(main_keys), len(app)))


if __name__ == "__main__":
    main()
