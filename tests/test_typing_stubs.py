"""Regression test for a `_pyside6_scintilla.pyi` typing bug, not a `tools/generate_pyi.py` unit test.

genpyi self-imports the extension as a bare `import _pyside6_scintilla`,
which pyright can't resolve -- the module only exists as the submodule
`pyside6_scintilla._pyside6_scintilla`. That silently turned every
`_pyside6_scintilla.<Name>` reference -- `ScintillaEdit.get_doc()`'s return
type, and `ScintillaEditFixed`'s base class -- into `Unknown`, which then
also poisoned every method `ScintillaEdit`/`ScintillaEditBase` inherit
through those bases (e.g. `setText()`, `markerDefine()`). `fix_self_import()`
in `tools/generate_pyi.py` rewrites the import to fix this; this test pins
the actual pyright-observed behavior so a future genpyi regeneration can't
silently reintroduce it.
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

REPO_ROOT = Path(__file__).resolve().parent.parent

CHECK_SCRIPT = textwrap.dedent("""\
    from pyside6_scintilla import ScintillaEdit

    editor = ScintillaEdit()
    reveal_type(editor.get_doc())
    reveal_type(editor.setText("x"))
    reveal_type(editor.markerDefine(0, 0))
    """)


def test_get_doc_and_inherited_methods_resolve_real_types(tmp_path: Path) -> None:
    """Pyright must report real types for these calls, never `Unknown`."""
    script = tmp_path / "check_types.py"
    script.write_text(CHECK_SCRIPT)

    result = subprocess.run(
        [sys.executable, "-m", "pyright", "--outputjson", str(script)],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    report = json.loads(result.stdout)

    resolved_types = [
        match.group("type") for d in report["generalDiagnostics"] if (match := REVEAL_TYPE_RE.match(d["message"]))
    ]

    assert resolved_types == ["ScintillaDocument", "None", "None"]
