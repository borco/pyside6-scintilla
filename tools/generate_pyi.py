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
- Widens `ScintillaEditBase.sends`'s `s` parameter, and `ScintillaEdit`'s
  other `const char *` parameters (e.g. `setText`/`addText`/`insertText`),
  to also accept `str`. shiboken's `const char *` converter accepts a Python
  `str` (UTF-8 encoded) at runtime, but genpyi only types these as
  `bytes | bytearray | memoryview` (optionally `| None`).
- Adds hand-written docstrings to `ScintillaEditBase.send`/`sends` -- the two
  entry points users actually call, but genpyi only emits their bare
  signatures (no Qt docstrings exist for them since they're not Qt
  overrides). See `SEND_DOCS` below.
- Resolves `ScintillaEdit`'s `'sptr_t'`/`'Scintilla.sptr_t'`/
  `'Scintilla.uptr_t'` forward references to `int`. genpyi inconsistently
  emits these as unresolvable quoted forward refs across its ~780 typed
  methods (genpyi prints "UNRECOGNIZED: 'sptr_t'" warnings for these).

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

# Same `const char *` widening as SENDS_OLD/SENDS_NEW above, but for
# ScintillaEdit's ~50 non-optional `const char *` parameters (e.g.
# setText/addText/insertText), which genpyi types as plain
# `bytes | bytearray | memoryview` with no `| None`. The negative lookahead
# avoids re-widening SENDS_NEW once it's already been applied.
CONST_CHAR_PTR_RE: Final = re.compile(r"bytes \| bytearray \| memoryview(?! \| str)")
CONST_CHAR_PTR_NEW: Final = "bytes | bytearray | memoryview | str"

# genpyi inconsistently resolves ScintillaEdit's ~780 `sptr_t`/`uptr_t`
# (Scintilla::sptr_t/uptr_t, "intptr_t"/"uintptr_t"-like typedefs) parameter
# and return types -- sometimes as the aliased `Scintilla.sptr_t`/
# `Scintilla.uptr_t` forms PRIMITIVE_ALIASES resolves, but often as bare
# unresolvable forward-ref strings (genpyi prints "UNRECOGNIZED: 'sptr_t'"
# warnings for these). These quoted forms always mean `int`.
SPTR_UPTR_FORWARD_REF_RE: Final = re.compile(r"'(?:Scintilla\.)?[su]ptr_t'")

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


# Matches the `fun`/`get`/`set` feature lines in Scintilla.iface that
# WidgetGen.py turns into ScintillaEdit methods, e.g.
# "get pointer GetDocPointer=2357(,)" -> ("get", "GetDocPointer").
WIDGET_FEATURE_RE: Final = re.compile(r"^(fun|get|set)\s+\S+\s+(\w+)=")


# Hand-transcribed from ScintillaEdit.cpp's hand-written methods (not
# generated from Scintilla.iface): TextReturner, find_text/findText,
# get_text_range/textRange, get_doc/set_doc, format_range/formatRange.
# Applied before the Scintilla.iface-derived docs below, so these take
# precedence over the generic iface docs for FindText/FormatRange (which
# normalise to the same findText/formatRange method names).
SCINTILLA_EDIT_HELPER_DOCS: Final = {
    "TextReturner": (
        "Send `message` with `wParam`, passing a buffer as its `lParam`, and return the buffer.\n\n"
        "        Used internally for messages whose result is a string, e.g. `getText`/`getLine`."
    ),
    "find_text": (
        "Search for `text` between `cpMin` and `cpMax` using `flags` (`Scintilla.FindOption` values).\n\n"
        "        Returns the `(start, end)` position of the match, or `(-1, cpMax)` if not found."
    ),
    "findText": "Alias for `find_text`.",
    "get_text_range": "Return the document's text between `start` and `end`.",
    "textRange": "Alias for `get_text_range`.",
    "get_doc": (
        "Return a new `ScintillaDocument` wrapping this editor's current document.\n\n"
        "        Pass it to another `ScintillaEdit`'s `set_doc` to share the document between views.\n\n"
        "        The returned object has no Qt parent, so it's kept alive only by your Python "
        "reference to it -- if you let it go, its `modified`/`save_point`/etc. signals stop firing "
        "(the underlying document itself stays alive as long as an editor is using it)."
    ),
    "set_doc": (
        "Make this editor display `doc`.\n\n"
        "        The document isn't copied -- multiple `ScintillaEdit` widgets can share it this way."
    ),
    "format_range": (
        "Render the document between `range_start` and `range_end` for printing.\n\n"
        "        Draws onto `target` (and lays out using `measure`) within `print_rect`/`page_rect`. "
        "If `draw` is false, only measures. Returns the position after the last formatted character."
    ),
    "formatRange": "Alias for `format_range`.",
}

# Hand-transcribed from ScintillaDocument.h/.cpp -- ScintillaDocument's
# methods aren't generated from Scintilla.iface, so genpyi emits only their
# bare signatures.
SCINTILLA_DOCUMENT_DOCS: Final = {
    "__init__": (
        "Wrap a Scintilla document buffer, creating a new empty one unless `pdoc_` is given.\n\n"
        "        `pdoc_` is a native document pointer, as returned by `pointer()` -- pass it to "
        "share an existing document, e.g. one obtained via `ScintillaEdit.get_doc()`."
    ),
    "pointer": "Return the underlying native document pointer, for sharing with another `ScintillaDocument`.",
    "line_from_position": "Return the line containing position `pos`.",
    "is_cr_lf": "Return whether the line ending at `pos` is CR+LF, as opposed to a lone CR or LF.",
    "delete_chars": "Delete `len` characters starting at `pos`. Returns whether anything was deleted.",
    "undo": "Undo one action from the undo history. Returns the position of the start of the change.",
    "redo": "Redo one action from the undo history. Returns the position of the start of the change.",
    "can_undo": "Return whether there is an action to undo.",
    "can_redo": "Return whether there is an action to redo.",
    "delete_undo_history": "Discard the undo history.",
    "set_undo_collection": "Enable or disable collection of undo actions. Returns the previous setting.",
    "is_collecting_undo": "Return whether undo actions are being collected.",
    "begin_undo_action": (
        "Start a sequence of actions that is undone/redone as a single unit.\n\n"
        "        If `coalesceWithPrior`, merge it with the previous undo action when possible."
    ),
    "end_undo_action": "End a sequence of actions started by `begin_undo_action`.",
    "set_save_point": "Mark the document's current state as unmodified (the save point).",
    "is_save_point": "Return whether the document is at its save point (unmodified since `set_save_point`).",
    "set_read_only": "Set whether the document refuses modification.",
    "is_read_only": "Return whether the document refuses modification.",
    "insert_string": "Insert `str` at `position`.",
    "get_char_range": "Return `length` bytes of the document's text starting at `position`.",
    "style_at": "Return the style byte at `position`.",
    "line_start": "Return the position of the start of line `lineno`.",
    "line_end": "Return the position of the end of line `lineno`, before any line ending characters.",
    "line_end_position": "Return the position of the end of the line containing `pos`, before any line ending characters.",
    "length": "Return the number of bytes in the document.",
    "lines_total": "Return the number of lines in the document.",
    "start_styling": "Set the styling position to `position`; subsequent `set_style_for` calls style from there.",
    "set_style_for": (
        "Set the next `length` bytes from the current styling position (see `start_styling`) to `style`.\n\n"
        "        Returns whether successful."
    ),
    "get_end_styled": "Return the position up to which the document has been styled.",
    "ensure_styled_to": "Ensure the document is styled up to at least `position`, emitting `style_needed` as needed.",
    "set_current_indicator": "Set the indicator used by subsequent `decoration_fill_range` calls.",
    "decoration_fill_range": (
        "Set `fillLength` bytes starting at `position` to `value` for the current indicator "
        "(see `set_current_indicator`)."
    ),
    "decorations_value_at": "Return the value of indicator `indic` at `position`.",
    "decorations_start": "Return the start of the run of indicator `indic` that includes `position`.",
    "decorations_end": "Return the end of the run of indicator `indic` that includes `position`.",
    "get_code_page": "Return the code page used to interpret the document's bytes as characters.",
    "set_code_page": "Set the code page used to interpret the document's bytes as characters.",
    "get_eol_mode": "Return the line ending type (`Scintilla.EndOfLine` value) used for new lines.",
    "set_eol_mode": "Set the line ending type (`Scintilla.EndOfLine` value) used for new lines.",
    "move_position_outside_char": (
        "Move `pos` outside of a multi-byte character towards `move_dir`.\n\n"
        "        If `check_line_end`, also move it outside of a line ending."
    ),
    "get_character": "Return the character at `pos`.",
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


def parse_widget_method_docs(iface_path: Path) -> dict[str, str]:
    """Map ScintillaEdit Python method names to their `# ` doc comments in Scintilla.iface.

    `WidgetGen.py` derives each method's name from its `fun`/`get`/`set` feature name via its
    `normalisedName()` (qtStyle): lowercase the first letter, and for `get` features additionally
    strip a leading `Get` (e.g. "GetDocPointer" -> "docPointer", "SetDocPointer" -> "setDocPointer",
    "AddText" -> "addText"). Not every feature passes WidgetGen's `checkTypes()` and becomes an
    actual method -- entries for features that weren't generated are simply unused.
    """
    docs: dict[str, str] = {}
    pending: list[str] = []
    for line in iface_path.read_text().splitlines():
        if line.startswith("# "):
            pending.append(line[2:].rstrip())
            continue
        if pending:
            match = WIDGET_FEATURE_RE.match(line)
            if match:
                feat, name = match.groups()
                if feat == "get":
                    name = name.replace("Get", "")
                docs[name[0].lower() + name[1:]] = " ".join(pending)
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


def widen_const_char_ptr_params(text: str) -> str:
    """Add `str` to `ScintillaEdit`'s other `const char *` parameter types. See CONST_CHAR_PTR_RE."""
    return CONST_CHAR_PTR_RE.sub(CONST_CHAR_PTR_NEW, text)


def resolve_sptr_uptr_forward_refs(text: str) -> str:
    """Replace unresolved `'sptr_t'`/`'Scintilla.sptr_t'`/`'Scintilla.uptr_t'` forward refs with `int`. See SPTR_UPTR_FORWARD_REF_RE."""
    return SPTR_UPTR_FORWARD_REF_RE.sub("int", text)


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
    text = add_method_docstrings(text, "ScintillaEdit", SCINTILLA_EDIT_HELPER_DOCS)
    text = add_method_docstrings(text, "ScintillaEdit", parse_widget_method_docs(IFACE_PATH))
    text = add_method_docstrings(text, "ScintillaDocument", SCINTILLA_DOCUMENT_DOCS)
    text = widen_sends_string_param(text)
    text = widen_const_char_ptr_params(text)
    text = resolve_sptr_uptr_forward_refs(text)
    PYI_PATH.write_text(text)


if __name__ == "__main__":
    main()
