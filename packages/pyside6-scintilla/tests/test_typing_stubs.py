"""Regression test for `_pyside6_scintilla.pyi` typing bugs, not a `tools/generate_pyi.py` unit test.

genpyi references the stub's own classes in ways pyright can't resolve -- a
bare `import _pyside6_scintilla` self-import, and base classes qualified as
`pyside6_scintilla._pyside6_scintilla.<Name>`. Either silently turns the
reference into `Unknown`, which then also poisons every method
`ScintillaEdit`/`ScintillaEditBase` inherit through those bases (e.g.
`setText()`, `markerDefine()`). `fix_self_references()` in
`tools/generate_pyi.py` fixes this; this test pins the actual
pyright-observed behavior so a future genpyi regeneration can't silently
reintroduce it.
"""

import json
import re
import subprocess
import sys
import textwrap
from pathlib import Path

# Matches pyright's `--outputjson` reveal_type message, e.g.
# 'Type of "editor.get_doc()" is "ScintillaDocument"'.
REVEAL_TYPE_RE = re.compile(r'^Type of ".*" is "(?P<type>[^"]*)"$')

PACKAGE_ROOT = Path(__file__).resolve().parent.parent

CHECK_SCRIPT = textwrap.dedent("""\
    from pyside6_scintilla import ScintillaEdit

    editor = ScintillaEdit()
    reveal_type(editor.get_doc())
    reveal_type(editor.setText("x"))
    reveal_type(editor.markerDefine(0, 0))
    reveal_type(editor.getText())
    reveal_type(editor.get_doc().get_char_range(0, 1))
    """)


def test_get_doc_and_inherited_methods_resolve_real_types(tmp_path: Path) -> None:
    """Pyright must report real types for these calls, never `Unknown`."""
    script = tmp_path / "check_types.py"
    script.write_text(CHECK_SCRIPT)

    result = subprocess.run(
        [sys.executable, "-m", "pyright", "--outputjson", str(script)],
        capture_output=True,
        text=True,
        cwd=PACKAGE_ROOT,
    )
    report = json.loads(result.stdout)

    resolved_types = [
        match.group("type") for d in report["generalDiagnostics"] if (match := REVEAL_TYPE_RE.match(d["message"]))
    ]

    assert resolved_types == ["ScintillaDocument", "None", "None", "str", "str"]
