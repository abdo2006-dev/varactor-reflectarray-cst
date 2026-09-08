#!/usr/bin/env python3
"""Public-repository hygiene gate for this repository.

Run before publishing. It checks the things that are easy to get wrong in a repo
that is read by people outside the project: broken links, leaked local paths,
credentials, editor and OS debris, licensed source PDFs, and internal workflow
material that a reader does not need and should not have to step over.

It checks the *tracked* tree, because that is what is published.

    python3 tools/check_public_repo.py

Exit status is 0 when every check passes and 1 otherwise.
"""
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# A markdown inline link or image whose target is a local relative path.
LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")

SECRETS = [
    (re.compile(r"(?i)\b(api[_-]?key|secret|passwd|password)\b\s*[:=]\s*\S"), "credential assignment"),
    (re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._\-]{16,}"), "bearer token"),
    (re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}"), "GitHub token"),
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "private key"),
]

# Directories whose whole point is internal workflow. A public reader needs none
# of them to understand the physics, the geometry, the numerical setup or the
# results, and a prompt archive in particular reads as workspace debris.
FORBIDDEN_DIRS = ("prompts/",)

FORBIDDEN_NAMES = (".DS_Store", "Thumbs.db", "desktop.ini")
FORBIDDEN_SUFFIXES = (".pyc", ".pyo")

# PDFs that may be published: our own generated report. Anything else -- in
# particular a publisher's article PDF -- must not be in the tree.
PDF_ALLOWED = re.compile(r"^deliverables/.*\.pdf$")

TEXT_SUFFIXES = {".md", ".py", ".sh", ".txt", ".yml", ".yaml", ".json", ".cff", ".csv"}


def tracked():
    out = subprocess.run(["git", "-C", str(ROOT), "ls-files"],
                         capture_output=True, text=True, check=True).stdout
    return [p for p in out.splitlines() if p]


def main():
    files = tracked()
    fails = []
    checks = 0

    def check(ok, msg):
        nonlocal checks
        checks += 1
        if not ok:
            fails.append(msg)

    for f in files:
        name = pathlib.Path(f).name
        check(name not in FORBIDDEN_NAMES, f"OS/editor debris tracked: {f}")
        check(pathlib.Path(f).suffix not in FORBIDDEN_SUFFIXES, f"compiled artefact tracked: {f}")
        check("__pycache__" not in f, f"__pycache__ tracked: {f}")
        for d in FORBIDDEN_DIRS:
            check(not f.startswith(d), f"internal workflow directory tracked: {f}")
        if f.lower().endswith(".pdf"):
            check(bool(PDF_ALLOWED.match(f)),
                  f"PDF outside deliverables/ tracked -- is this a publisher file? {f}")

    for f in files:
        p = ROOT / f
        if p.suffix.lower() not in TEXT_SUFFIXES or not p.is_file():
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        # Assembled at runtime so this file does not match its own pattern.
        home_roots = ("/" + "Users" + "/", "/" + "home" + "/")
        check(not any(h in text for h in home_roots),
              f"local absolute path in {f}")

        for pat, what in SECRETS:
            check(not pat.search(text), f"possible {what} in {f}")

        if p.suffix == ".md":
            for target in LINK.findall(text):
                if re.match(r"^(https?:|mailto:|#)", target):
                    continue
                resolved = (p.parent / target.split("#")[0]).resolve()
                check(resolved.exists(), f"broken link in {f} -> {target}")

    print(f"{checks} checks over {len(files)} tracked files")
    if fails:
        print(f"\n{len(fails)} FAILED:")
        for m in fails:
            print("  -", m)
        return 1
    print("PUBLIC REPOSITORY CHECK PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
