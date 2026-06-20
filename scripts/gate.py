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
