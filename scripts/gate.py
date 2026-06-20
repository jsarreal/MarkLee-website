#!/usr/bin/env python3
"""Integrity gate: validate a change before it is accepted.

    python3 scripts/gate.py [path-to-commit-msg]

Checks: every local HTML reference resolves to a real file; if a commit-message
path is given, it carries the provenance footer.
"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dome  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def check_html_refs(root=ROOT):
    problems = []
    for path in glob.glob(os.path.join(root, "**", "*.html"), recursive=True):
        rel = os.path.relpath(path, root)
        for ref in dome._refs_in_html(path, root=root):
            if not os.path.exists(os.path.join(root, ref)):
                problems.append(f"{rel}: missing reference -> {ref}")
    return problems


_ISSUE_RE = re.compile(r'^Issue:\s*#?\d+\s*$', re.M)
_SESSION_RE = re.compile(r'^Session:\s*\S+', re.M)


def check_provenance(message):
    problems = []
    if not _ISSUE_RE.search(message):
        problems.append("missing 'Issue: #<n>' footer")
    if not _SESSION_RE.search(message):
        problems.append("missing 'Session: <id>' footer")
    return problems


def _main(argv):
    problems = check_html_refs()
    if argv and os.path.exists(argv[0]):
        with open(argv[0], encoding="utf-8") as f:
            problems += check_provenance(f.read())
    if problems:
        print("GATE FAIL:", file=sys.stderr)
        for p in problems:
            print("  - " + p, file=sys.stderr)
        return 1
    print("GATE OK")
    return 0


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
