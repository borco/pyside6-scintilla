"""Regenerate `src/pyside6_scintilla/_pyside6_scintilla.pyi`.

`shiboken6-genpyi` generates a `.pyi` stub for `_pyside6_scintilla`, giving
Pylance/mypy/ruff full signatures and autocomplete for `Scintilla.*` and
`ScintillaEditBase`. Running it directly on the built extension fails for two
reasons that don't affect PySide6's own `pyside6-genpyi` (see "Type stubs" in
docs/BINDINGS.md):

1. genpyi re-imports the extension from a bare path, bypassing
   `pyside6_scintilla/__init__.py`'s `import PySide6.QtWidgets` DLL-path
   setup -- without that import happening first, the bare re-import fails
   with "DLL load failed".
2. genpyi's `find_imports()` references a `PySide6` global that only
   `PySide6.support.generate_pyi` sets up (via `global PySide6; import
   PySide6`) before calling it. The generic `shiboken6-genpyi` entry point
   never sets it, so it raises `NameError: name 'PySide6' is not defined`.

After generation, this script also:

- Aliases `Scintilla.Position`/`sptr_t`/`uptr_t` to `int`. These are
  primitive typedefs, not nested types, but genpyi emits them as
  `Scintilla.Position`-style forward references that wouldn't otherwise
  resolve.
- Stitches the `# ...` doc comments from
  `src/scintilla/include/Scintilla.iface` into `Scintilla.Message` enum
  members as docstrings, so they show up as hover docs.

Run after rebuilding the extension (`make install` or `uv sync
--reinstall-package pyside6-scintilla`), and whenever `bindings.xml`/
`bindings.h` change the public API surface.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Final

REPO_ROOT: Final = Path(__file__).resolve().parent.parent
PACKAGE_DIR: Final = REPO_ROOT / "src" / "pyside6_scintilla"
IFACE_PATH: Final = REPO_ROOT / "src" / "scintilla" / "include" / "Scintilla.iface"
PYI_PATH: Final = PACKAGE_DIR / "_pyside6_scintilla.pyi"

# Matches the `fun`/`get`/`set`/`evt` feature lines in Scintilla.iface, e.g.
# "fun void AddText=2001(position length, string text)" -> "AddText".
FEATURE_RE: Final = re.compile(r"^(?:fun|get|set|evt)\s+\S+\s+(\w+)=")

# Matches a genpyi-generated enum member line, e.g. "        AddText  = 0x7d1".
MEMBER_RE: Final = re.compile(r"^(\s+)(\w+)\s*= 0x[0-9a-fA-F]+\n?$")

PRIMITIVE_ALIASES: Final = (
    "\n"
    "    # Position/sptr_t/uptr_t are primitive typedefs (plain `int` at runtime),\n"
    "    # not nested types -- but genpyi emits forward references like\n"
    "    # 'Scintilla.Position' for them. Alias to int so those resolve.\n"
    "    Position = int\n"
    "    sptr_t = int\n"
    "    uptr_t = int\n"
)


def parse_iface_docs(iface_path: Path) -> dict[str, str]:
    """Map Scintilla.iface `fun`/`get`/`set`/`evt` feature names to their `# ` doc comments.

    A doc comment only documents a feature if it's on the line immediately
    above it, matching how Scintilla.iface is written -- a blank line (or
    anything else) in between discards it.
    """
    docs: dict[str, str] = {}
    pending: list[str] = []
    for line in iface_path.read_text().splitlines():
        if line.startswith("# "):
            pending.append(line[2:].rstrip())
            continue
        if pending:
            match = FEATURE_RE.match(line)
            if match:
                docs[match.group(1)] = " ".join(pending)
            pending.clear()
    return docs


def add_primitive_aliases(text: str) -> str:
    """Insert int aliases for Position/sptr_t/uptr_t right after `class Scintilla(...)`."""
    return text.replace(
        "class Scintilla(Shiboken.Object):\n",
        "class Scintilla(Shiboken.Object):\n" + PRIMITIVE_ALIASES,
        1,
    )


def add_message_docstrings(text: str, docs: dict[str, str]) -> str:
    """Insert each Scintilla.iface doc comment as a docstring after the Message member it documents."""
    out: list[str] = []
    in_message_enum = False
    for line in text.splitlines(keepends=True):
        if line.startswith("    class Message(enum.IntEnum):"):
            in_message_enum = True
        elif in_message_enum and line.startswith("    class "):
            in_message_enum = False
        out.append(line)
        if in_message_enum:
            match = MEMBER_RE.match(line)
            if match:
                indent, name = match.group(1), match.group(2)
                doc = docs.get(name)
                if doc:
                    out.append(f'{indent}r"""{doc}"""\n')
    return "".join(out)


def run_genpyi() -> None:
    """Run shiboken6-genpyi against the built extension, with the PySide6 workarounds applied."""
    import pyside6_scintilla._pyside6_scintilla as extension
    import PySide6
    import shiboken6  # noqa: F401 -- side effect: makes `shibokensupport` importable
    from shibokensupport.signature.lib import pyi_generator

    pyi_generator.PySide6 = PySide6  # workaround 2, see module docstring
    sys.argv = ["shiboken6-genpyi", extension.__file__, "--outpath", str(PACKAGE_DIR)]
    pyi_generator.main()


def main() -> None:
    """Generate `_pyside6_scintilla.pyi`, then post-process it in place."""
    run_genpyi()
    text = PYI_PATH.read_text()
    text = add_primitive_aliases(text)
    text = add_message_docstrings(text, parse_iface_docs(IFACE_PATH))
    PYI_PATH.write_text(text)


if __name__ == "__main__":
    main()
