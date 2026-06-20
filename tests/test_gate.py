import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import gate  # noqa: E402


def _write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def test_check_html_refs_flags_missing(tmp_path):
    root = str(tmp_path)
    _write(os.path.join(root, "index.html"), '<link href="css/missing.css">')
    problems = gate.check_html_refs(root=root)
    assert any("missing.css" in p for p in problems)


def test_check_html_refs_ok_when_present(tmp_path):
    root = str(tmp_path)
    _write(os.path.join(root, "index.html"), '<link href="css/style.css">')
    _write(os.path.join(root, "css/style.css"), "body{}")
    assert gate.check_html_refs(root=root) == []


def test_check_provenance_ok_with_issue_and_session():
    msg = "feat: tweak headline\n\nIssue: #14\nSession: abc123"
    assert gate.check_provenance(msg) == []


def test_check_provenance_flags_both_when_missing():
    problems = gate.check_provenance("feat: tweak headline")
    assert len(problems) == 2
