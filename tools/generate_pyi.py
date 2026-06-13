"""Regenerate `src/pyside6_scintilla/_pyside6_scintilla.pyi`.

`shiboken6-genpyi` generates a `.pyi` stub for `_pyside6_scintilla`, giving
Pylance/mypy/ruff full signatures and autocomplete for `Scintilla.*` and
`ScintillaEditBase`. Running it directly on the built extension fails for two
reasons that don't affect PySide6's own `pyside6-genpyi` (see "Type stubs" in
docs/bindings.md):

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
  `src/scintilla/include/Scintilla.iface` into `Scintilla.Message` and
  `Scintilla.CharacterSource` enum members as docstrings, so they show up as
  hover docs.
- Stitches hand-transcribed docs for `Scintilla.VirtualSpace`, `Update`, and
  `ModificationFlags` members. These have no per-member `# ...` comments in
  `Scintilla.iface`, but do have per-member tables in
  `src/scintilla/doc/ScintillaDoc.html` -- see `VIRTUAL_SPACE_DOCS`,
  `UPDATE_DOCS`, and `MODIFICATION_FLAGS_DOCS` below.
- Widens `ScintillaEditBase.sends`'s `s` parameter to also accept `str`.
  shiboken's `const char *` converter accepts a Python `str` (UTF-8 encoded)
  at runtime, but genpyi only types it as `bytes | bytearray | memoryview |
  None`.
- Adds hand-written docstrings to `ScintillaEditBase.send`/`sends` -- the two
  entry points users actually call, but genpyi only emits their bare
  signatures (no Qt docstrings exist for them since they're not Qt
  overrides). See `SEND_DOCS` below.

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

# Matches a genpyi-generated one-line method stub, e.g.
# "    def send(self, iMessage: int, /, ...) -> int: ...".
METHOD_RE: Final = re.compile(r"^(\s+)def (\w+)\(.*\) -> .+: \.\.\.\n?$")

# genpyi's resolution of `send`/`sends`' `sptr_t`/`uptr_t` return and `lParam`
# types is inconsistent across regenerations -- sometimes `int` directly (the
# desired form below), sometimes an unresolvable `'sptr_t'`/
# `typing.Optional[ForwardRef('sptr_t')]` forward ref (genpyi prints
# "UNRECOGNIZED: 'sptr_t'" warnings for these two methods when this happens).
SEND_LINE_RE: Final = re.compile(r"^    def send\(self,.*\) -> .+: \.\.\.$", re.M)
SEND_SIGNATURE: Final = (
    "    def send(self, iMessage: int, /, wParam: int | None = ..., lParam: int | None = ...) -> int: ..."
)
SENDS_LINE_RE: Final = re.compile(r"^    def sends\(self,.*\) -> .+: \.\.\.$", re.M)
SENDS_SIGNATURE: Final = (
    "    def sends(self, iMessage: int, /, wParam: int | None = ..., "
    "s: bytes | bytearray | memoryview | None = ...) -> int: ..."
)

# Matches Scintilla.iface's "enu CharacterSource=SC_CHARACTERSOURCE_" line, capturing
# the value-name prefix ("SC_CHARACTERSOURCE_") shared by its `val` lines.
CHARACTER_SOURCE_ENU_RE: Final = re.compile(r"^enu CharacterSource=(\w+)")

# Matches a `val <PREFIXED_NAME>=<value>` line, e.g. "val SC_CHARACTERSOURCE_DIRECT_INPUT=0".
VAL_RE: Final = re.compile(r"^val (\w+)=")

# genpyi types `const char *` parameters as bytes-like only; shiboken's
# converter also accepts `str` (UTF-8 encoded) at runtime.
SENDS_OLD: Final = "s: bytes | bytearray | memoryview | None = ..."
SENDS_NEW: Final = "s: bytes | bytearray | memoryview | str | None = ..."

PRIMITIVE_ALIASES: Final = (
    "\n"
    "    # Position/sptr_t/uptr_t are primitive typedefs (plain `int` at runtime),\n"
    "    # not nested types -- but genpyi emits forward references like\n"
    "    # 'Scintilla.Position' for them. Alias to int so those resolve.\n"
    "    Position = int\n"
    "    sptr_t = int\n"
    "    uptr_t = int\n"
)

# Hand-transcribed from the "Virtual space options" table in
# src/scintilla/doc/ScintillaDoc.html (SCVS_* constants). Scintilla.iface has
# no per-member `# ` comments for this enum.
VIRTUAL_SPACE_DOCS: Final = {
    "None_": "The default: no virtual space.",
    "RectangularSelection": "Virtual space is enabled for rectangular selections.",
    "UserAccessible": "Virtual space is enabled for user actions such as right arrow key or clicking beyond line end.",
    "NoWrapLineStart": "Left arrow does not wrap to the previous line.",
}

# Hand-transcribed from the SCI_UPDATEUI notification's "Update flags" table
# in src/scintilla/doc/ScintillaDoc.html (SC_UPDATE_* constants).
UPDATE_DOCS: Final = {
    "None_": "Value without any changes.",
    "Content": "Contents, styling or markers may have been changed.",
    "Selection": "Selection may have been changed.",
    "VScroll": "May have scrolled vertically.",
    "HScroll": "May have scrolled horizontally.",
}

# Hand-transcribed from the SCN_MODIFIED notification's "Modify notification
# type flags" table in src/scintilla/doc/ScintillaDoc.html (SC_MOD_*/
# SC_PERFORMED_*/SC_MULTI*/SC_STARTACTION constants).
MODIFICATION_FLAGS_DOCS: Final = {
    "None_": "Base value with no fields valid. Will not occur but is useful in tests.",
    "InsertText": "Text has been inserted into the document.",
    "DeleteText": "Text has been removed from the document.",
    "ChangeStyle": "A style change has occurred.",
    "ChangeFold": "A folding change has occurred.",
    "User": "Information: the operation was done by the user.",
    "Undo": "Information: this was the result of an Undo.",
    "Redo": "Information: this was the result of a Redo.",
    "MultiStepUndoRedo": "This is part of a multi-step Undo or Redo transaction.",
    "LastStepInUndoRedo": "This is the final step in an Undo or Redo transaction.",
    "ChangeMarker": "One or more markers has changed in a line.",
    "BeforeInsert": "Text is about to be inserted into the document.",
    "BeforeDelete": "Text is about to be deleted from the document.",
    "MultilineUndoRedo": "This is part of an Undo or Redo with multi-line changes.",
    "StartAction": "Set on a SC_PERFORMED_USER action that is the first or only step in an undo transaction.",
    "ChangeIndicator": "An indicator has been added or removed from a range of text.",
    "ChangeLineState": "A line state has changed because SCI_SETLINESTATE was called.",
    "ChangeMargin": "A text margin has changed.",
    "ChangeAnnotation": "An annotation has changed.",
    "Container": "Set on actions that the container stored into the undo stack with SCI_ADDUNDOACTION.",
    "LexerState": "The internal state of a lexer has changed over a range.",
    "InsertCheck": "Text is about to be inserted; the handler may change it via SCI_CHANGEINSERTION.",
    "ChangeTabStops": "The explicit tab stops on a line have changed because SCI_CLEARTABSTOPS or SCI_ADDTABSTOP was called.",
    "ChangeEOLAnnotation": "An EOL annotation has changed.",
    "EventMaskAll": "Mask for all valid flags; the default mask state set by SCI_SETMODEVENTMASK.",
}


# Hand-written -- ScintillaEditBase.send/sends are this binding's two entry
# points for the ~800 Scintilla.Message commands, but they're plain C++
# methods (not Qt overrides), so genpyi emits only their bare signatures.
SEND_DOCS: Final = {
    "send": (
        "Send a message to the underlying Scintilla editor and return its result.\n\n"
        "        `iMessage` is usually a `Scintilla.Message` value, e.g. "
        "`Scintilla.Message.GetTextLength`. `wParam` and `lParam` are that message's "
        "two generic parameters, interpreted as documented for the message in the "
        "upstream Scintilla documentation."
    ),
    "sends": (
        "Like `send`, but pass `s` as the message's string `lParam`.\n\n"
        "        Use this for messages whose `lParam` is a string, e.g. "
        "`Scintilla.Message.AddText` or `Scintilla.Message.SetText`. `s` accepts "
        "`bytes`, `bytearray`, `memoryview`, or `str` (encoded as UTF-8)."
    ),
}


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


def parse_character_source_docs(iface_path: Path) -> dict[str, str]:
    """Map Scintilla.CharacterSource member names to their `# ` doc comments in Scintilla.iface.

    Unlike Message, CharacterSource's entries are `val SC_CHARACTERSOURCE_X_Y=N` lines
    rather than CamelCase feature names -- strip the `SC_CHARACTERSOURCE_` prefix and
    convert the remainder to the CamelCase name genpyi assigns the enum member (e.g.
    SC_CHARACTERSOURCE_DIRECT_INPUT -> DirectInput).
    """

    def to_pascal_case(snake: str) -> str:
        """Convert a SCREAMING_SNAKE_CASE `.iface` value suffix to genpyi's CamelCase enum member name.

        E.g. "DIRECT_INPUT" -> "DirectInput", "IME_RESULT" -> "ImeResult".
        """
        return "".join(word.capitalize() for word in snake.split("_"))

    docs: dict[str, str] = {}
    prefix: str | None = None
    pending: list[str] = []
    for line in iface_path.read_text().splitlines():
        enu_match = CHARACTER_SOURCE_ENU_RE.match(line)
        if enu_match:
            # The preceding comment (if any) documents the enum itself, not its
            # first member -- discard it.
            prefix = enu_match.group(1)
            pending.clear()
            continue
        if line.startswith("# "):
            pending.append(line[2:].rstrip())
            continue
        if prefix is not None:
            val_match = VAL_RE.match(line)
            if val_match and val_match.group(1).startswith(prefix):
                if pending:
                    docs[to_pascal_case(val_match.group(1)[len(prefix) :])] = " ".join(pending)
            else:
                prefix = None
        pending.clear()
    return docs


def add_primitive_aliases(text: str) -> str:
    """Insert int aliases for Position/sptr_t/uptr_t right after `class Scintilla(...)`."""
    return text.replace(
        "class Scintilla(Shiboken.Object):\n",
        "class Scintilla(Shiboken.Object):\n" + PRIMITIVE_ALIASES,
        1,
    )


def add_enum_docstrings(text: str, enum_class: str, docs: dict[str, str]) -> str:
    """Insert each doc comment as a docstring after the member of `Scintilla.<enum_class>` it documents."""
    out: list[str] = []
    in_enum = False
    class_line = f"    class {enum_class}(enum.IntEnum):"
    for line in text.splitlines(keepends=True):
        if line.startswith(class_line):
            in_enum = True
        elif in_enum and line.startswith("    class "):
            in_enum = False
        out.append(line)
        if in_enum:
            match = MEMBER_RE.match(line)
            if match:
                indent, name = match.group(1), match.group(2)
                doc = docs.get(name)
                if doc:
                    out.append(f'{indent}r"""{doc}"""\n')
    return "".join(out)


def normalize_send_signatures(text: str) -> str:
    """Force `ScintillaEditBase.send`/`sends` back to their `int`-based signatures.

    See `SEND_LINE_RE`/`SENDS_LINE_RE` above for why this is needed.
    """
    text = SEND_LINE_RE.sub(SEND_SIGNATURE, text, count=1)
    text = SENDS_LINE_RE.sub(SENDS_SIGNATURE, text, count=1)
    return text


def add_method_docstrings(text: str, class_name: str, docs: dict[str, str]) -> str:
    """Expand `def <name>(...) -> T: ...` one-liners in `class_name` into a body with a docstring."""
    out: list[str] = []
    in_class = False
    class_line = f"class {class_name}("
    for line in text.splitlines(keepends=True):
        if line.startswith(class_line):
            in_class = True
        elif in_class and line.startswith("class "):
            in_class = False
        if in_class:
            match = METHOD_RE.match(line)
            if match:
                indent, name = match.group(1), match.group(2)
                doc = docs.get(name)
                if doc:
                    signature = line.rstrip("\n").removesuffix(" ...")
                    out.append(f'{signature}\n{indent}    r"""{doc}"""\n')
                    continue
        out.append(line)
    return "".join(out)


def widen_sends_string_param(text: str) -> str:
    """Add `str` to `ScintillaEditBase.sends`'s `s` parameter type."""
    return text.replace(SENDS_OLD, SENDS_NEW, 1)


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
    text = normalize_send_signatures(text)
    text = add_primitive_aliases(text)
    text = add_enum_docstrings(text, "Message", parse_iface_docs(IFACE_PATH))
    text = add_enum_docstrings(text, "CharacterSource", parse_character_source_docs(IFACE_PATH))
    text = add_enum_docstrings(text, "VirtualSpace", VIRTUAL_SPACE_DOCS)
    text = add_enum_docstrings(text, "Update", UPDATE_DOCS)
    text = add_enum_docstrings(text, "ModificationFlags", MODIFICATION_FLAGS_DOCS)
    text = add_method_docstrings(text, "ScintillaEditBase", SEND_DOCS)
    text = widen_sends_string_param(text)
    PYI_PATH.write_text(text)


if __name__ == "__main__":
    main()
