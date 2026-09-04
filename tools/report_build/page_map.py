# -*- coding: utf-8 -*-
"""
Derive a heading/figure/table -> page-number map from a rendered PDF.

build.sh renders the DOCX once without page numbers, converts it, runs this to
find where everything landed, then rebuilds the DOCX with the numbers filled in.
This keeps the contents, list of figures and list of tables correct in both the
DOCX and the PDF without depending on a field update at open time.
"""
import json
import re
import sys

import pymupdf

HEADER_MARK = "CST reconstruction of a varactor-tunable 26 GHz reflectarray unit cell"


def norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def main(pdf_path, outline_path, out_path):
    outline = json.load(open(outline_path))
    doc = pymupdf.open(pdf_path)

    pages = [norm(doc[i].get_text()) for i in range(len(doc))]

    # Page one of the main matter restarts numbering at 1. The running header is
    # only present in that section, so the first page carrying it is report
    # page 1. Searching for the first heading instead would match the contents.
    offset = 0
    for i, txt in enumerate(pages):
        if norm(HEADER_MARK) in txt:
            offset = i
            break

    def find(label, skip_front=True):
        start = offset if skip_front else 0
        for i in range(start, len(pages)):
            if norm(label) in pages[i]:
                return i - offset + 1
        return None

    page_map = {}
    for level, text, key in outline["toc"]:
        if key == "refs":
            n = find("References")
        else:
            n = find(text)
        if n:
            page_map[key] = n
    for level, text, key in outline["figures"] + outline["tables"]:
        n = find(text.split("  ")[0] + ".")
        if n:
            page_map[key] = n

    json.dump(page_map, open(out_path, "w"), indent=1)
    print("page map: %d entries over %d pages (front matter %d)"
          % (len(page_map), len(doc) - offset, offset))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3]))
