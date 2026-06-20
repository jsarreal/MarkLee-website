import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import dome  # noqa: E402


def _write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def test_build_extracts_local_refs(tmp_path):
    root = str(tmp_path)
    _write(os.path.join(root, "index.html"),
           '<link href="css/style.css"><a href="about.html">x</a><img src="https://x/y.png">')
    graph = dome.build(root=root)
    assert graph["index.html"] == ["about.html", "css/style.css"]


def test_build_ignores_external_and_anchors(tmp_path):
    root = str(tmp_path)
    _write(os.path.join(root, "a.html"),
           '<a href="#top">t</a><a href="mailto:x@y.com">m</a><a href="https://z">z</a>')
    graph = dome.build(root=root)
    assert graph["a.html"] == []


def test_build_strips_query_and_fragment(tmp_path):
    root = str(tmp_path)
    _write(os.path.join(root, "p.html"), '<a href="contact.html?ref=1#form">c</a>')
    graph = dome.build(root=root)
    assert graph["p.html"] == ["contact.html"]


def test_query_ap_returns_files_plus_one_hop(tmp_path):
    root = str(tmp_path)
    _write(os.path.join(root, "index.html"), '<link href="css/style.css">')
    _write(os.path.join(root, "css/style.css"), "body{}")
    dome.write_dome(dome.build(root=root), path=os.path.join(root, "substrate/dome.json"))
    _write(os.path.join(root, "substrate/aps.json"), json.dumps({"home": ["index.html"]}))
    res = dome.query_ap("home",
                        aps_path=os.path.join(root, "substrate/aps.json"),
                        dome_path=os.path.join(root, "substrate/dome.json"),
                        root=root)
    assert res == ["css/style.css", "index.html"]


def test_query_ap_unknown_raises(tmp_path):
    root = str(tmp_path)
    _write(os.path.join(root, "substrate/dome.json"), "{}")
    _write(os.path.join(root, "substrate/aps.json"), json.dumps({"home": ["index.html"]}))
    import pytest
    with pytest.raises(KeyError):
        dome.query_ap("nope",
                      aps_path=os.path.join(root, "substrate/aps.json"),
                      dome_path=os.path.join(root, "substrate/dome.json"),
                      root=root)
