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


def query_ap(name, aps_path=APS_PATH, dome_path=DOME_PATH, root=ROOT):
    with open(aps_path, encoding="utf-8") as f:
        aps = json.load(f)
    if name not in aps:
        raise KeyError(name)
    with open(dome_path, encoding="utf-8") as f:
        graph = json.load(f)
    files = set()
    for pattern in aps[name]:
        for hit in glob.glob(os.path.join(root, pattern), recursive=True):
            files.add(os.path.relpath(hit, root))
    for f_ in list(files):
        for ref in graph.get(f_, []):
            files.add(ref)
    return sorted(files)


def _main(argv):
    if argv[:1] == ["build"]:
        write_dome(build())
        print(f"wrote {os.path.relpath(DOME_PATH, ROOT)}")
        return 0
    if argv[:2] == ["query", "ap"] and len(argv) >= 3:
        for f in query_ap(argv[2]):
            print(f)
        return 0
    print("usage: dome.py build | query ap <name>", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
