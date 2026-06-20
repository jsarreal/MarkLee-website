import os


def test_manifest_has_required_sections():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(root, "MANIFEST.md"), encoding="utf-8") as f:
        text = f.read()
    for header in [
        "# MANIFEST",
        "## Attachment points",
        "## How to make an edit",
        "## Tier classification",
        "## Provenance",
        "## Clean as you cook",
    ]:
        assert header in text, f"missing section: {header}"
