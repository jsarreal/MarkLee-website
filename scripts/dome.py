#!/usr/bin/env python3
"""Dome: a small file-reference graph + Attachment Point (AP) queries for the substrate.

    python3 scripts/dome.py build            # write substrate/dome.json
    python3 scripts/dome.py query ap <name>  # print the file neighborhood for AP <name>
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOME_PATH = os.path.join(ROOT, "substrate", "dome.json")
APS_PATH = os.path.join(ROOT, "substrate", "aps.json")

_REF_RE = re.compile(r'(?:href|src)\s*=\s*"([^"]+)"')


def _is_local(ref):
    return not ref.startswith(("http://", "https://", "//", "mailto:", "tel:", "#", "data:"))


def _refs_in_html(path, root=ROOT):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    base = os.path.dirname(path)
    out = set()
    for raw in _REF_RE.findall(text):
        ref = raw.split("#")[0].split("?")[0]
        if not ref or not _is_local(ref):
            continue
        resolved = os.path.normpath(os.path.join(base, ref))
        out.add(os.path.relpath(resolved, root))
    return sorted(out)


def build(root=ROOT):
    graph = {}
    for path in glob.glob(os.path.join(root, "**", "*.html"), recursive=True):
        rel = os.path.relpath(path, root)
        graph[rel] = _refs_in_html(path, root=root)
    return graph


def write_dome(graph, path=DOME_PATH):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(graph, f, indent=2, sort_keys=True)
        f.write("\n")
