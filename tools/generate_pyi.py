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
- Adds typed, documented attributes for `Scintilla.InvalidPosition`,
  `CpUtf8`, `MarkerMax`, `MaskHistory`, `MaskFolders`, `MaxMargin`,
  `FontSizeMultiplier`, `TimeForever`, `KeywordsetMax`, and `IndicatorMax` --
  `ScintillaTypes.h`'s free-standing `constexpr` constants, runtime-accessible
  but otherwise entirely absent from the stub, since genpyi only stitches
  enum members from a wrapped namespace. See
  `SCINTILLA_NAMESPACE_CONSTANTS_DOCS` below.
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
- Adds a class docstring to `ScintillaEditBase`, and a docstring to each of
  its ~37 notification signals (`modified`, `charAdded`, `updateUi`, ...) and
  its `notifyParent`/`event_command`/`scrollHorizontal`/`scrollVertical`
  slots and Qt virtual-method overrides -- hand-transcribed from
  `ScintillaEditBase.cpp`/`.h` and the "Notifications" section of
  `ScintillaDoc.html`, since none of these have `Scintilla.iface` doc
  comments. See `SCINTILLA_EDIT_BASE_CLASS_DOC`, `SCINTILLA_EDIT_BASE_SIGNAL_DOCS`,
  and `SCINTILLA_EDIT_BASE_OVERRIDE_DOCS` below.
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

# Matches a genpyi-generated Qt signal attribute, e.g.
# "    notify  : typing.ClassVar[Signal] = ... # notify(Scintilla::NotificationData*)".
SIGNAL_RE: Final = re.compile(r"^(\s+)(\w+)\s*: typing\.ClassVar\[Signal\] = \.\.\.(?: #.*)?\n?$")

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

# ScintillaTypes.h's free-standing `constexpr` constants (Position/int-typed,
# not enum members) -- shiboken still exposes these as plain `Scintilla.<Name>`
# int attributes (see scintilla_wrapper.cpp's PyDict_SetItemString calls), but
# genpyi's stub generation only stitches enum members from a wrapped
# namespace, so these are otherwise entirely missing from the stub. Values
# are the actual runtime ints, not always the source's hex literal -- e.g.
# MaskFolders's `0xFE000000` doesn't fit in a 32-bit signed int, so it wraps
# to a negative value at runtime. Docs are from the `#` comment (if any)
# above the matching `val SC_.../INDIC_...` line in Scintilla.iface, or
# hand-written where there is none.
SCINTILLA_NAMESPACE_CONSTANTS_DOCS: Final[dict[str, tuple[int, str]]] = {
    "InvalidPosition": (
        -1,
        "Sentinel returned by position-returning `Scintilla.Message` values when there is no match or no valid position.",
    ),
    "CpUtf8": (
        65001,
        "Code page value enabling UTF-8 mode, e.g. via `Scintilla.Message.SetCodePage`. Same value as Windows' `CP_UTF8`.",
    ),
    "MarkerMax": (31, "Highest valid marker number -- up to 32 markers (0-31) can be set per line."),
    "MaskHistory": (
        0x01E00000,
        "Bitmask (0x01E00000) isolating the change-history bits of a line's marker/margin mask.",
    ),
    "MaskFolders": (
        -33554432,
        "Bitmask (0xFE000000) isolating the fold-level bits of a line's marker/margin mask. Too large for a "
        "32-bit signed int, so its runtime value wraps to negative.",
    ),
    "MaxMargin": (4, "Highest valid margin index -- up to 5 margins (0-4) can be shown."),
    "FontSizeMultiplier": (
        100,
        "Scintilla stores font sizes as hundredths of a point internally; divide a fractional size (e.g. from "
        "`Scintilla.Message.StyleGetSizeFractional`) by this to get points.",
    ),
    "TimeForever": (10000000, 'Sentinel meaning "no timeout", e.g. for `Scintilla.Message.SetMouseDwellTime`.'),
    "KeywordsetMax": (8, "Highest valid `keywordSet` index accepted by `Scintilla.Message.SetKeyWords`."),
    "IndicatorMax": (43, "Highest valid indicator number."),
}

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


# Hand-transcribed from the relevant `SCI_*` message descriptions in
# src/scintilla/doc/ScintillaDoc.html for each of the 63 `enum class`es bound
# in bindings.xml that have neither `Scintilla.iface` doc comments (like
# Message/CharacterSource above) nor a dedicated hand-transcribed dict (like
# VirtualSpace/Update/ModificationFlags above). Maps enum name -> (class
# docstring or None, {member name: docstring}); members with nothing beyond
# their name in ScintillaDoc.html are simply omitted from the inner dict --
# unlike source comments elsewhere in this codebase, these become end-user
# hover docs in an IDE, so the bar is "as helpful as possible without being
# verbose," not "omit anything an identifier already implies."
ENUM_DOCS: Final[dict[str, tuple[str | None, dict[str, str]]]] = {
    "Accessibility": (
        "Controls whether accessibility (screen reader) support is enabled, set with "
        "`SCI_SETACCESSIBILITY`/`SCI_GETACCESSIBILITY`.",
        {},
    ),
    "Alpha": (
        "Translucency level used by alpha-blended drawing such as marker and selection layers.",
        {
            "Transparent": "Value 0; completely transparent.",
            "Opaque": "Value 255; fully opaque.",
            "NoAlpha": "Legacy value (256) meaning drawing is performed opaquely directly on the base layer; "
            "prefer choosing a layer via the `Layer`-based APIs instead.",
        },
    ),
    "AnnotationVisible": (
        "Display mode for line annotations, set with `SCI_ANNOTATIONSETVISIBLE`/`SCI_ANNOTATIONGETVISIBLE`.",
        {
            "Hidden": "Annotations are not displayed.",
            "Standard": "Annotations are drawn left justified with no adornment.",
            "Boxed": "Annotations are indented to match the text and are surrounded by a box.",
            "Indented": "Annotations are indented to match the text.",
        },
    ),
    "AutoCompleteOption": (
        "Options controlling autocompletion list display and selection behaviour, set with "
        "`SCI_AUTOCSETOPTIONS`.",
        {
            "FixedSize": "On Win32 only, uses a fixed-size list instead of one resizable by the user; also "
            "avoids a header rectangle above the list.",
            "SelectFirstItem": "Always selects the first item in the list regardless of the entered text; "
            "useful when the application's autocompletion logic already sorts so the best match is on top. "
            "Without this option, Scintilla selects the item matching the entered text.",
        },
    ),
    "AutomaticFold": (
        "Bit flags choosing which parts of fold-handling behaviour Scintilla performs automatically instead "
        "of relying on the container, set with `SCI_SETAUTOMATICFOLD`.",
        {
            "Show": "Automatically shows lines as needed, avoiding the `SCN_NEEDSHOWN` notification.",
            "Click": "Handles clicks in the fold margin automatically, avoiding the `SCN_MARGINCLICK` "
            "notification for folding margins.",
            "Change": "Shows lines as needed when the fold structure changes; `SCN_MODIFIED` is still sent "
            "unless disabled by the container.",
        },
    ),
    "Bidirectional": (
        "Selects the default text direction for bidirectional (e.g. Arabic/Hebrew) text support, set with "
        "`SCI_SETBIDIRECTIONAL`.",
        {
            "Disabled": "Bidirectional support is off; also the value returned by `SCI_GETBIDIRECTIONAL` if a "
            "previous `SCI_SETBIDIRECTIONAL` call failed.",
            "L2R": "Left-to-right is the default direction. Currently the only mode with actual bidirectional "
            "display support (experimental, Win32 DirectWrite and macOS Cocoa only); only UTF-8 documents show "
            "bidirectional behaviour.",
            "R2L": "Right-to-left is the default direction. Reserved for future implementation; not yet "
            "functional.",
        },
    ),
    "CaretPolicy": (
        "Bit flags controlling how the caret is kept in view, passed as the `caretPolicy` argument to "
        "`SCI_SETXCARETPOLICY`/`SCI_SETYCARETPOLICY` together with a `caretSlop` value.",
        {
            "Slop": "Enables a slop value (`caretSlop`) defining an unwanted zone near the margins (pixels for "
            "vertical margins, lines for horizontal margins) that the caret is kept out of, so surrounding "
            "context stays visible.",
            "Strict": "Strictly enforces the slop policy: the caret is centred on the display if no slop is "
            "set, and cannot enter the unwanted zone if slop is set.",
            "Even": "If NOT set, the left/bottom unwanted zones are extended to match the right/top ones "
            "(asymmetrical), favouring visibility of line starts and the lines following the caret.",
            "Jumps": "Moves the display more energetically so the caret can travel further in one direction "
            "before the policy reapplies.",
        },
    ),
    "CaretSticky": (
        "Controls when the caret's horizontal position on a line is remembered when moving between lines, set "
        "with `SCI_SETCARETSTICKY`.",
        {
            "Off": "Default: all text changes and caret position changes remember the caret's new horizontal "
            "position when moving to a different line.",
            "On": "Only moving the caret directly via mouse or keyboard updates the remembered horizontal "
            "position; text changes do not.",
            "WhiteSpace": "Behaves like `Off` except when only space/tab characters are inserted -- in that one "
            "case the horizontal position is not updated.",
        },
    ),
    "CaretStyle": (
        "Caret drawing style, set with `SCI_SETCARETSTYLE`; separate bit ranges select insert-mode, "
        "overtype-mode, and curses-mode appearance.",
        {
            "Invisible": "Carets are not drawn at all.",
            "Line": "Draws insertion carets as lines; the default.",
            "Block": "Draws insertion carets as blocks.",
            "OverstrikeBar": "Draws an overstrike caret as a bar; the default for overtype mode (shares value "
            "0 with `Invisible`, but applies to the separate overtype-mode bit, not the insert-mode bits).",
            "InsMask": "Mask (lower 4 bits) isolating the insert-mode caret style bits.",
            "OverstrikeBlock": "Draws an overstrike caret as a block; OR with one of the insert-mode styles "
            "(`Line`/`Block`/`Invisible`).",
            "Curses": "Draws additional (non-main) carets as blocks for environments, such as a terminal, "
            "that cannot draw them otherwise; the main caret is left to the terminal.",
            "BlockAfter": "When the caret end of a range is at the end of the selection and a block caret "
            "style is chosen, draws the block outside the selection instead of inside; OR with `Block` or "
            "`Curses`.",
        },
    ),
    "CaseInsensitiveBehaviour": (
        "Controls how case-insensitive autocompletion selects among matching entries, set with "
        "`SCI_AUTOCSETCASEINSENSITIVEBEHAVIOUR`.",
        {
            "RespectCase": "Default: even with case-insensitive autocompletion, still selects the first list "
            "entry that matches the entered text in a case-sensitive way.",
            "IgnoreCase": "Ignores case entirely when selecting the matching autocompletion entry.",
        },
    ),
    "CaseVisible": (
        "Forces how a style's text is displayed (upper/lower/camel case) without altering the stored text, "
        "set with `SCI_STYLESETCASE`.",
        {"Mixed": "Displays text normally, unmodified."},
    ),
    "ChangeHistoryOption": (
        "Bit flags enabling change-history tracking and how it is displayed, set with "
        "`SCI_SETCHANGEHISTORY`.",
        {
            "Disabled": "Default: change history is turned off.",
            "Enabled": "Tracks changes to the document.",
            "Markers": "Displays changes in the margin using the `MarkerOutline` history markers.",
            "Indicators": "Displays changes in the text using the `IndicatorNumbers` history indicators.",
        },
    ),
    "CharacterSet": (
        "Character set used to display a style's text (independent of document encoding), set with "
        "`SCI_STYLESETCHARACTERSET`; useful for comments/string literals in a different language than the "
        "rest of the document. This binding's Qt platform layer (`PlatQt.cpp`) maps each value to a Qt "
        "`QTextCodec` name, so support depends only on which codecs Qt ships, not on the OS -- unlike "
        "Scintilla's native GTK/Cocoa/Win32 ports, where support and code-page mapping vary by platform.",
        {
            "Default": 'Maps to the "ISO 8859-1" (Latin-1) codec; the default character set used by styles '
            "unless changed.",
            "Ansi": 'Not mapped to a codec by this binding\'s Qt platform layer -- falls back to the same '
            '"ISO 8859-1" codec as `Default` regardless of platform.',
            "Symbol": "Not mapped to a codec by this binding's Qt platform layer -- falls back to the same "
            '"ISO 8859-1" codec as `Default` regardless of platform.',
            "Mac": 'Maps to the "Apple Roman" codec.',
            "ShiftJis": 'Maps to the "Shift-JIS" codec.',
            "Hangul": 'Maps to the "CP949" codec.',
            "Johab": "Not mapped to a codec by this binding's Qt platform layer -- falls back to the same "
            '"ISO 8859-1" codec as `Default` regardless of platform.',
            "GB2312": 'Maps to the "GB18030-0" codec.',
            "ChineseBig5": 'Maps to the "Big5" codec.',
            "Greek": 'Maps to the "ISO 8859-7" codec.',
            "Turkish": 'Maps to the "ISO 8859-9" codec.',
            "Vietnamese": 'Maps to the "Windows-1258" codec.',
            "Hebrew": 'Maps to the "ISO 8859-8" codec.',
            "Arabic": 'Maps to the "ISO 8859-6" codec.',
            "Baltic": 'Maps to the "ISO 8859-13" codec.',
            "Russian": 'Maps to the "KOI8-R" codec.',
            "Thai": 'Maps to the "TIS-620" codec.',
            "EastEurope": 'Maps to the "ISO 8859-2" codec.',
            "Oem": "Not mapped to a codec by this binding's Qt platform layer -- falls back to the same "
            '"ISO 8859-1" codec as `Default` regardless of platform.',
            "Oem866": "Not mapped to a codec by this binding's Qt platform layer -- falls back to the same "
            '"ISO 8859-1" codec as `Default` regardless of platform.',
            "Iso8859_15": 'Maps to the "ISO 8859-15" (Latin-9) codec.',
            "Cyrillic": 'Maps to the "Windows-1251" codec.',
        },
    ),
    # CharacterSource already gets its per-member docs from Scintilla.iface's
    # `# ` comments, via parse_character_source_docs() in main() -- this
    # entry only adds the class-level summary that mechanism doesn't produce.
    "CharacterSource": (
        "Identifies how a character was entered, reported as `NotificationData.characterSource` on the "
        "`SCN_CHARADDED` notification -- only available via the raw `notify` signal, since the typed "
        "`charAdded` signal only carries the character code.",
        {},
    ),
    "CompletionMethods": (
        "Identifies how an autocompletion list selection was triggered, reported as the "
        "`listCompletionMethod` field of `SCN_AUTOCSELECTION`/`SCN_AUTOCCOMPLETED` notifications.",
        {
            "FillUp": "A fillup character (see `SCI_AUTOCSETFILLUPS`) triggered the completion; the "
            "character used is reported separately.",
            "DoubleClick": "A double-click on a list item triggered the completion.",
            "Tab": "The Tab key, or `SCI_TAB`, triggered the completion.",
            "Newline": "A newline, or `SCI_NEWLINE`, triggered the completion.",
            "Command": "The `SCI_AUTOCSELECT` message triggered the completion.",
            "SingleChoice": "There was only a single choice in the list and 'choose single' mode was "
            "active, as set by `SCI_AUTOCSETCHOOSESINGLE`.",
        },
    ),
    "CursorShape": (
        "Mouse cursor shape shown over the editor or a margin, set with "
        "`SCI_SETCURSOR`/`SCI_SETMARGINCURSORN`.",
        {
            "Normal": "The normal pointer cursor; also the value returned by `SCI_GETCURSOR` if no cursor "
            "type has been set.",
            "Wait": "The wait cursor, shown when the mouse is over (or captured by) Scintilla and Scintilla "
            "is busy.",
            "ReverseArrow": "A reversed arrow, normally shown over margins by default.",
        },
    ),
    "DocumentOption": (
        "Bit flags chosen when creating a document with `SCI_CREATEDOCUMENT`, affecting memory allocation and "
        "performance.",
        {
            "StylesNone": "Stops allocation of memory for per-character styles, treating the whole document "
            "as style 0; saves significant memory. Lexers may still style visually via indicators. Often "
            "combined with the null lexer for documents too large to lex efficiently.",
            "TextLarge": "Allows the document to be larger than 2 GB, for 64-bit executables.",
        },
    ),
    "EOLAnnotationVisible": (
        "Display mode and decoration style for end-of-line annotations, set with "
        "`SCI_EOLANNOTATIONSETVISIBLE`/`SCI_EOLANNOTATIONGETVISIBLE`.",
        {
            "Hidden": "End-of-line annotations are not displayed.",
            "Standard": "Drawn left justified with no adornment.",
            "Boxed": "Drawn surrounded by a box.",
            "Stadium": "Surrounded with a ◖stadium◗ -- a rectangle with rounded ends.",
            "FlatCircle": "Surrounded with a |shape◗ -- flat left end, curved right end.",
            "AngleCircle": "Surrounded with a ◄shape◗ -- angled left end, curved right end.",
            "CircleFlat": "Surrounded with a ◖shape| -- curved left end, flat right end.",
            "Flats": "Surrounded with a |shape| -- flat on both ends.",
            "AngleFlat": "Surrounded with a ◄shape| -- angled left end, flat right end.",
            "CircleAngle": "Surrounded with a ◖shape▶ -- curved left end, angled right end.",
            "FlatAngle": "Surrounded with a |shape▶ -- flat left end, angled right end.",
            "Angles": "Surrounded with a ◄shape▶ -- angled on both ends.",
        },
    ),
    "EdgeVisualStyle": (
        "Used with `SCI_SETEDGEMODE`/`SCI_GETEDGEMODE` to control how the long-line edge marker is displayed.",
        {
            "None_": "Long lines are not marked. This is the default state.",
            "Line": "Draws a vertical line at the column set by `SCI_SETEDGECOLUMN`; works well for "
            "monospaced fonts but may not align well with proportional fonts.",
            "Background": "Changes the background colour of characters after the column limit; recommended "
            "for proportional fonts.",
            "MultiLine": "Like `Line` but draws a configurable set of vertical lines simultaneously, using an "
            "independent dataset configured via the `SCI_MULTIEDGE*` messages.",
        },
    ),
    "Element": (
        "Identifies a visual element (selection, caret, whitespace, fold/hidden line, etc.) whose colour can "
        "be get/set with `SCI_SETELEMENTCOLOUR`/`SCI_GETELEMENTCOLOUR`.",
        {
            "List": "Text colour in autocompletion lists; on Win32 this is currently provided by the "
            "platform layer.",
            "ListBack": "Background colour of autocompletion lists; on Win32 this is currently provided by "
            "the platform layer.",
            "ListSelected": "Text colour of the selected item in autocompletion lists; on Win32 this is "
            "currently provided by the platform layer.",
            "ListSelectedBack": "Background colour of the selected item in autocompletion lists; on Win32 "
            "this is currently provided by the platform layer.",
            "SelectionText": "Overrides the default selection text colour.",
            "SelectionBack": "Overrides the default selection background colour; can be drawn translucently "
            "(see `SCI_SETSELECTIONLAYER`) or opaquely.",
            "SelectionAdditionalText": "Text colour used for additional selections (multiple/rectangular "
            "selection) alongside the main selection.",
            "SelectionAdditionalBack": "Background colour used for additional selections (multiple/"
            "rectangular selection) alongside the main selection.",
            "SelectionSecondaryText": "On X11/Wayland, used instead of the main selection colours when "
            "another application has taken over the 'primary selection'; commonly grey.",
            "SelectionSecondaryBack": "On X11/Wayland, used instead of the main selection colours when "
            "another application has taken over the 'primary selection'; commonly grey.",
            "SelectionInactiveText": "Colour used for the selection when the window has lost keyboard focus, "
            "customarily greyed out.",
            "SelectionInactiveBack": "Colour used for the selection when the window has lost keyboard focus, "
            "customarily greyed out.",
            "SelectionInactiveAdditionalText": "Colour for additional (multiple) selections when unfocused; "
            "if not explicitly set, falls back to `SelectionInactiveText`.",
            "SelectionInactiveAdditionalBack": "Colour for additional (multiple) selections when unfocused; "
            "if not explicitly set, falls back to `SelectionInactiveBack`.",
            "Caret": "Colour of the text caret for the main selection; allows setting caret translucency, "
            "unlike the discouraged `SCI_SETCARETFORE`.",
            "CaretAdditional": "Colour of the caret for additional (multiple) selections.",
            "CaretLineBack": "Background colour of the line containing the caret; can be drawn translucently "
            "(`SCI_SETCARETLINELAYER`) or opaquely, with the highest priority over other background colours "
            "such as markers when drawn opaquely.",
            "WhiteSpace": "Overrides the lexer-determined foreground colour of visible whitespace globally.",
            "WhiteSpaceBack": "Overrides the lexer-determined background colour of visible whitespace "
            "globally.",
            "HotSpotActive": "Text colour of an active hot spot.",
            "HotSpotActiveBack": "Background colour of an active hot spot.",
            "FoldLine": "Colour of the lines drawn in the text area to indicate folds (set via "
            "`SCI_SETFOLDFLAGS`); if not set, the `StylesCommon.Default` foreground colour is used.",
            "HiddenLine": "If set, draws a horizontal line in this colour to indicate hidden lines (from "
            "`SCI_HIDELINES`); a fold line drawn at the same position takes precedence.",
        },
    ),
    "EndOfLine": (
        "Selects the line-ending character sequence used by `SCI_SETEOLMODE`/`SCI_CONVERTEOLS`.",
        {},
    ),
    "FindOption": (
        "Flags (combinable by OR-ing) controlling how `SCI_SEARCHINTARGET` and related search messages match "
        "text, set via `SCI_SETSEARCHFLAGS`.",
        {
            "None_": "Default setting is a case-insensitive literal match.",
            "WholeWord": "A match only occurs if the characters before and after are not word characters, as "
            "defined by `SCI_SETWORDCHARS`.",
            "MatchCase": "A match only occurs with text that matches the case of the search string.",
            "WordStart": "A match only occurs if the character immediately before the match is not a word "
            "character (unlike `WholeWord`, the character after is not checked).",
            "RegExp": "Interpret the search string as a regular expression, using Scintilla's base "
            "implementation unless combined with `Cxx11RegEx`; matches never span multiple lines.",
            "Posix": "Treat the regular expression in a more POSIX-compatible manner by interpreting bare "
            "'(' and ')' as tagged sections rather than requiring '\\(' and '\\)'; has no effect when "
            "`Cxx11RegEx` is set.",
            "Cxx11RegEx": "Use the C++11 <regex> library instead of Scintilla's basic regular expressions, "
            "with ECMAScript semantics and Unicode-aware behaviour on UTF-8 documents; requires `RegExp` to "
            "also be set, and returns -1 with status `Status.RegEx` if the expression is invalid.",
        },
    ),
    "FocusChange": (
        "Notification codes sent to the container for `SCEN_CHANGE`/`SCEN_SETFOCUS`/`SCEN_KILLFOCUS` events.",
        {
            "Killfocus": "Fired when Scintilla loses focus.",
            "Setfocus": "Fired when Scintilla receives focus.",
            "Change": "Fired when the text (not the styling) of the document changes; carries no further "
            "detail -- use the `modified` signal/`SCN_MODIFIED` for more detailed change information.",
        },
    ),
    "FoldAction": (
        "Action to perform on a fold point, used with `SCI_FOLDLINE`, `SCI_FOLDCHILDREN`, and "
        "`SCI_FOLDALL`.",
        {
            "Toggle": "Toggles between contracted and expanded; for `SCI_FOLDALL`, the first fold header in "
            "the document is examined to decide whether to expand or contract the whole document.",
            "ContractEveryLevel": "Used only with `SCI_FOLDALL`; can be combined (OR-ed) with `Contract` or "
            "`Toggle` to contract all fold levels instead of only the top level.",
        },
    ),
    "FoldDisplayTextStyle": (
        "Controls how fold-tag text (set via `SCI_TOGGLEFOLDSHOWTEXT`/`SCI_SETDEFAULTFOLDDISPLAYTEXT`) is "
        "rendered, via `SCI_FOLDDISPLAYTEXTSETSTYLE`.",
        {
            "Hidden": "Do not display the fold text tags. This is the default.",
            "Boxed": "Display the fold text tags with a box drawn around them.",
        },
    ),
    "FoldFlag": (
        "Bit flags controlling where fold-indicator lines are drawn in the text area, set with "
        "`SCI_SETFOLDFLAGS`.",
        {
            "LineBeforeExpanded": "Draws a line above the fold header when it is expanded.",
            "LineBeforeContracted": "Draws a line above the fold header when it is not expanded.",
            "LineAfterExpanded": "Draws a line below the fold header when it is expanded.",
            "LineAfterContracted": "Draws a line below the fold header when it is not expanded.",
            "LevelNumbers": "Displays hexadecimal fold levels in the line margin to aid debugging of "
            "folding; cannot be combined with `LineState`.",
            "LineState": "Displays hexadecimal line state in the line margin to aid debugging of lexing and "
            "folding; cannot be used together with `LevelNumbers`.",
        },
    ),
    # FoldLevel was already bound before this batch of 63 (like KeyMod/MarginType/
    # StylesCommon/Notification below) but never documented; added here for the
    # same reason as those.
    "FoldLevel": (
        "A line's fold level and associated flags, set/got with `SCI_SETFOLDLEVEL`/`SCI_GETFOLDLEVEL` as a "
        "single 32-bit value combining a level number with flag bits.",
        {
            "None_": "A default level that may occur before folding is applied.",
            "Base": "The initial fold level assigned to a line, allowing unsigned arithmetic on levels "
            "below it.",
            "NumberMask": "Mask (0xFFF) isolating the level-number portion from the flag bits; the level "
            "number itself ranges from 0 to this mask.",
            "WhiteFlag": "Indicates the line is blank, so it should be treated as part of the preceding "
            "section (e.g. not a fold point) even if its level number suggests otherwise.",
            "HeaderFlag": "Indicates the line is a header, i.e. a fold point; OR this into the level when "
            "calling `SCI_SETFOLDLEVEL`.",
        },
    ),
    "FontQuality": (
        "Controls the antialiasing method used to render fonts, set/got via "
        "`SCI_SETFONTQUALITY`/`SCI_GETFONTQUALITY` (Windows only at present).",
        {
            "QualityDefault": "The backward-compatible default antialiasing behaviour.",
            "QualityMask": "Mask (0xF) isolating the bits used for the quality value.",
        },
    ),
    "FontStretch": (
        "Horizontal stretch/condensation of a font's glyphs, set with `SCI_STYLESETSTRETCH`; corresponds to "
        "a horizontal magnification between 50% and 200%, though most fonts/platforms only support 2-3 of "
        "these values well.",
        {
            "UltraCondensed": "Corresponds to 50% horizontal width.",
            "ExtraCondensed": "Corresponds to 62.5% horizontal width.",
            "Condensed": "Corresponds to 75% horizontal width; one of the best-supported stretch values along "
            "with `Normal` and `Expanded`.",
            "SemiCondensed": "Corresponds to 87.5% horizontal width.",
            "Normal": "Corresponds to 100% horizontal width (no stretch); one of the best-supported stretch "
            "values along with `Condensed` and `Expanded`.",
            "SemiExpanded": "Corresponds to 112.5% horizontal width.",
            "Expanded": "Corresponds to 125% horizontal width; one of the best-supported stretch values along "
            "with `Condensed` and `Normal`.",
            "ExtraExpanded": "Corresponds to 150% horizontal width.",
            "UltraExpanded": "Corresponds to 200% horizontal width.",
        },
    ),
    "FontWeight": (
        "Font boldness/weight, set with `SCI_STYLESETWEIGHT`; any value from 1 (very light) to 999 (very "
        "heavy) is accepted, though fonts typically only support 2-4 distinct weights.",
        {
            "Normal": "Standard weight (400); selected by `SCI_STYLESETBOLD` when its boolean argument is "
            "false.",
            "SemiBold": "Semi-bold weight (600), between `Normal` and `Bold`.",
            "Bold": "Bold weight (700); selected by `SCI_STYLESETBOLD` when its boolean argument is true.",
        },
    ),
    "IMEInteraction": (
        "Selects how the platform's Input Method Editor (for Chinese, Japanese, or Korean text entry) is "
        "displayed, set with `SCI_SETIMEINTERACTION`.",
        {
            "Windowed": "The IME is shown as a separate window above Scintilla, like in other applications.",
            "Inline": "The IME is displayed by Scintilla itself as text; works better with rectangular/"
            "multiple selection. Scintilla may ignore this setting in some cases, e.g. it may only be "
            "supported for certain languages.",
        },
    ),
    "IdleStyling": (
        "Controls whether syntax styling of text outside the immediately visible area is deferred to an "
        "idle-time background task, set with `SCI_SETIDLESTYLING`.",
        {
            "None_": "Default: styling is performed for all currently visible text before displaying it, "
            "which may make scrolling slow on very large files.",
            "ToVisible": "A small amount of styling is done before display, then the rest of the visible "
            "text is styled incrementally in the background; text may briefly appear uncoloured.",
            "AfterVisible": "Text after the currently visible portion is also styled in the background "
            "during idle time.",
            "All": "Styles text both before and after the visible portion in the background during idle "
            "time.",
        },
    ),
    "IndentView": (
        "Controls how far indentation guides extend on blank/empty lines, set with "
        "`SCI_SETINDENTATIONGUIDES`.",
        {
            "None_": "No indentation guides are shown (turns the feature off).",
            "Real": "Indentation guides are shown only inside real (actual) indentation white space on a "
            "line.",
            "LookForward": "Indentation guides extend beyond the actual indentation up to the level of the "
            "next non-empty line.",
            "LookBoth": "Indentation guides extend up to whichever of the next or previous non-empty line "
            "has the greater indentation level; recommended for most languages.",
        },
    ),
    "IndicFlag": (
        "Flags controlling indicator colouring behaviour, set/got with "
        "`SCI_INDICSETFLAGS`/`SCI_INDICGETFLAGS`.",
        {
            "None_": "Default: the indicator uses its configured fore colour.",
            "ValueFore": "The indicator's colour is taken from the per-character indicator value (see "
            "`IndicValue`) rather than its fore setting, allowing many colours for a single indicator.",
        },
    ),
    "IndicValue": (
        "Masks for packing an RGB colour into the indicator value used with `SCI_SETINDICATORVALUE` when "
        "`IndicFlag.ValueFore` is set.",
        {
            "Mask": "Mask (0xFFFFFF) used to extract the RGB colour portion from an indicator value.",
            "Bit": "Bit (0x1000000) OR-ed into the RGB colour to mark it as a per-character indicator colour "
            "value.",
        },
    ),
    "IndicatorNumbers": (
        "Identifies the indicator number ranges reserved for containers, IME, and change-history use, as "
        "passed to the `SCI_INDIC*` messages.",
        {
            "Container": "First indicator number in the range reserved for use by containers; indicators "
            "0-7 are reserved for lexers.",
            "Ime": "First indicator number reserved for IME (Input Method Editor) indicators.",
            "ImeMax": "Last indicator number reserved for IME indicators.",
            "HistoryRevertedToOriginInsertion": "Indicator for text that was deleted and saved but then "
            "reverted to its original state; the text has not been saved to disk.",
            "HistoryRevertedToOriginDeletion": "Indicator for text that was inserted and saved but then "
            "reverted to its original state; there is text on disk that is missing.",
            "HistorySavedInsertion": "Indicator for text that was inserted and saved; this text is the same "
            "as on disk.",
            "HistorySavedDeletion": "Indicator for text that was deleted and saved; this range is the same "
            "as on disk.",
            "HistoryModifiedInsertion": "Indicator for text that was inserted but not yet saved.",
            "HistoryModifiedDeletion": "Indicator for text that was deleted but not yet saved.",
            "HistoryRevertedToModifiedInsertion": "Indicator for text that was deleted and saved but then "
            "reverted, though not to its original state; the text has not been saved to disk.",
            "HistoryRevertedToModifiedDeletion": "Indicator for text that was inserted and saved but then "
            "reverted, though not to its original state; there is text on disk that is missing.",
            "Max": "The last valid indicator number.",
        },
    ),
    "IndicatorStyle": (
        "Visual appearance of an indicator, set with `SCI_INDICSETSTYLE` and used to highlight text such as "
        "syntax errors, deprecated names, or URLs.",
        {
            "Plain": "Underlined with a single, straight line.",
            "Squiggle": "A squiggly underline; requires 3 pixels of descender space.",
            "TT": "A line of small T shapes.",
            "Diagonal": "Diagonal hatching.",
            "Hidden": "An indicator with no visual effect, useful for tracking content invisibly.",
            "Box": "A rectangle drawn around the text.",
            "RoundBox": "A translucent rectangle with rounded corners around the text; fill and outline "
            "alpha are controlled with `SCI_INDICSETALPHA`/`SCI_INDICSETOUTLINEALPHA`.",
            "StraightBox": "Like `RoundBox` but with square corners; does not colour the top pixel of the "
            "line so indicators on contiguous lines stay visually distinct.",
            "Dash": "A dashed underline.",
            "Dots": "A dotted underline.",
            "SquiggleLow": "Like `Squiggle` but only 2 vertical pixels tall, so it fits under small fonts.",
            "DotBox": "A dotted rectangle drawn with alternating alpha/outline-alpha translucency.",
            "SquigglePixmap": "A pixmap-based version of `Squiggle` for performance; appearance is worse than "
            "`Squiggle` on macOS HiDPI.",
            "CompositionThick": "A 2-pixel-thick underline near the bottom of the line, resembling the target "
            "style used in Asian language input composition.",
            "CompositionThin": "A 1-pixel-thick underline just above the bottom of the line, resembling "
            "non-target ranges in Asian language input composition.",
            "FullBox": "Like `StraightBox` but covers the entire character area, including the top pixel.",
            "TextFore": "Changes the text colour to the indicator's foreground colour instead of drawing a "
            "decoration.",
            "Point": "Draws a small triangle below the start of the indicator range.",
            "PointCharacter": "Draws a small triangle below the centre of the first character of the "
            "indicator range.",
            "PointTop": "Draws a small triangle above the start of the indicator range.",
            "Gradient": "A vertical gradient from the indicator colour/alpha at top fading to fully "
            "transparent at bottom.",
            "GradientCentre": "A vertical gradient with the colour/alpha centred in the middle, fading to "
            "fully transparent at both top and bottom.",
        },
    ),
    # KeyMod was already bound before this batch of 63 (like FoldLevel above and
    # MarginType/StylesCommon/Notification below) but never documented; added
    # here for the same reason as those.
    "KeyMod": (
        "Modifier-key flags (combinable by OR-ing) used alongside a `Keys` code in a `keyDefinition` passed "
        "to `SCI_ASSIGNCMDKEY`/`SCI_CLEARCMDKEY` for custom key bindings.",
        {
            "Norm": "No modifiers; useful as the zero value when building a key-binding table.",
            "Super": "A system-dependent modifier key, such as the Windows key on Windows or the GTK "
            "'Super'/Meta key on Linux.",
            "Meta": "On macOS, the Mac Control key is mapped to this modifier (while the Mac Command key is "
            "mapped to `Ctrl`).",
        },
    ),
    "Keys": (
        "Virtual key codes used in a `keyDefinition` (with `KeyMod` modifiers) passed to "
        "`SCI_ASSIGNCMDKEY`/`SCI_CLEARCMDKEY` for custom key bindings.",
        {"Prior": "Page Up key.", "Next": "Page Down key."},
    ),
    "Layer": (
        "Controls whether a background effect (selection or caret-line background) is drawn opaquely on the "
        "base layer or translucently under/over the text, used by `SCI_SETSELECTIONLAYER`/"
        "`SCI_SETCARETLINELAYER`.",
        {
            "Base": "Draw the background opaquely on the base layer.",
            "UnderText": "Draw the background translucently under the text; does not work in single-phase "
            "drawing mode (`PhasesDraw.One`) since there is no under-text phase.",
            "OverText": "Draw the background translucently over the text.",
        },
    ),
    "LineCache": (
        "Controls which lines have their layout (wrapping/positions) cached, set with "
        "`SCI_SETLAYOUTCACHE`.",
        {
            "None_": "No lines are cached.",
            "Caret": "Only the line containing the caret is cached; this is the default.",
            "Page": "The visible lines plus the line containing the caret are cached.",
            "Document": "All lines in the document are cached.",
        },
    ),
    "LineCharacterIndexType": (
        "Identifies which line/character position index is active, used with "
        "`SCI_GETLINECHARACTERINDEX`/`SCI_ALLOCATELINECHARACTERINDEX`; only supported for UTF-8 documents.",
        {
            "None_": "No line-character index is active.",
            "Utf32": "Index by whole (UTF-32) characters.",
            "Utf16": "Index by UTF-16 code units.",
        },
    ),
    "LineEndType": (
        "Selects whether only ASCII line endings or also Unicode line endings are recognized, used with "
        "`SCI_SETLINEENDTYPESALLOWED`/`SCI_GETLINEENDTYPESSUPPORTED`; Unicode mode is ineffective unless the "
        "active lexer also supports it.",
        {
            "Default": "Only ASCII line ends (CR, LF, CRLF) are interpreted.",
            "Unicode": "Unicode line-ending characters are also interpreted, if the lexer supports it.",
        },
    ),
    "MarginOption": (
        "Bit flags for `SCI_SETMARGINOPTIONS` that control margin click behaviour.",
        {
            "SubLineSelect": "Clicking the margin in front of a wrapped line selects only that sub-line "
            "instead of the whole wrapped line.",
        },
    ),
    # MarginType was already bound before this batch of 63 (like FoldLevel/
    # KeyMod above and StylesCommon/Notification below) but never documented;
    # added here for the same reason as those.
    "MarginType": (
        "The kind of content a margin shows, set with `SCI_SETMARGINTYPEN`; by convention margin 0 is used "
        "for line numbers and the next two for symbols.",
        {
            "Symbol": "A symbol margin, e.g. for markers (breakpoints, bookmarks).",
            "Number": "A line-number margin.",
            "Back": "A symbol margin whose background colour matches `StylesCommon.Default`'s background.",
            "Fore": "A symbol margin whose background colour matches `StylesCommon.Default`'s foreground.",
            "Text": "A margin showing application-defined text, set with `SCI_MARGINSETTEXT`.",
            "RText": "Like `Text`, but right-justified.",
            "Colour": "A symbol margin whose background colour is set explicitly with "
            "`SCI_SETMARGINBACKN`.",
        },
    ),
    "MarkerOutline": (
        "Marker numbers reserved by Scintilla for change-history tracking and folding margin symbols, used "
        "with `SCI_MARKERDEFINE`.",
        {
            "HistoryRevertedToOrigin": "Marks a line that was changed and saved but then reverted to its "
            "original state; the line differs from its on-disk state.",
            "HistorySaved": "Marks a line that was modified and saved; the line matches its on-disk state.",
            "HistoryModified": "Marks a line that was modified but not yet saved; the line differs from its "
            "on-disk state.",
            "HistoryRevertedToModified": "Marks a line that was changed and saved but then reverted, though "
            "not to its original state; the line differs from its on-disk state.",
            "Folder": "Marks a line where a closed fold is present; pair with `FolderOpen` using a symbol "
            "like Plus/Minus or Arrow/ArrowDown.",
            "FolderOpen": "Marks a line where an open fold is present; pair with `Folder`.",
            "FolderEnd": "In the flattened-tree folding style: a closed fold header nested inside another "
            "fold, so it needs a tree connector below it (e.g. `MarkerSymbol.CirclePlusConnected`).",
            "FolderOpenMid": "In the flattened-tree folding style: an open fold header nested inside "
            "another fold, so it needs a tree connector below it (e.g. "
            "`MarkerSymbol.CircleMinusConnected`).",
            "FolderMidTail": "In the flattened-tree folding style: the last child line of a fold that is "
            "itself nested inside another fold, combining a corner with a continuing connector for the "
            "parent (e.g. `MarkerSymbol.TCornerCurve`).",
            "FolderTail": "In the flattened-tree folding style: the last child line of a top-level fold "
            "(e.g. `MarkerSymbol.LCornerCurve`).",
            "FolderSub": "In the flattened-tree folding style: a child line of a fold that is neither the "
            "first nor last, drawn as a plain vertical connector (e.g. `MarkerSymbol.VLine`).",
        },
    ),
    "MarkerSymbol": (
        "Symbol drawn for a given marker number in the selection margin, assigned with `SCI_MARKERDEFINE`; "
        "by default all 32 markers use `Circle`.",
        {
            "Background": "Changes only the background colour of the line, drawing no symbol.",
            "FullRect": "Mirrors `Background` but changes only the margin background colour instead of the "
            "line.",
            "Underline": "Draws an underline across the text rather than a margin symbol.",
            "Empty": "An invisible symbol, useful for tracking line movement programmatically.",
            "Available": "A convention applications can use to indicate that a marker number is free for "
            "plugins to allocate.",
            "Character": "Add a Unicode code point to this base value (10000) to use that character as the "
            "marker, e.g. `Character + 9637`.",
            "Pixmap": "Used automatically when a marker is defined via `SCI_MARKERDEFINEPIXMAP`.",
            "RgbaImage": "Used automatically when a marker is defined via `SCI_MARKERDEFINERGBAIMAGE`.",
            "Bar": "Drawn first/underneath all other markers regardless of marker number, since bars often "
            "span multiple lines (e.g. change history) while other markers mark individual lines.",
        },
    ),
    "MultiAutoComplete": (
        "Controls whether autocompleted text is inserted into just the main selection or into every "
        "selection, set with `SCI_AUTOCSETMULTI`.",
        {
            "Once": "Autocompleted text goes into only the main selection; this is the default.",
            "Each": "Autocompleted text is inserted into each selection.",
        },
    ),
    "MultiPaste": (
        "Controls whether pasted text goes into just the main selection or into every selection, set with "
        "`SCI_SETMULTIPASTE`.",
        {
            "Once": "Pasted text goes into only the main selection; this is the default.",
            "Each": "Pasted text is inserted into each selection.",
        },
    ),
    # Notification was already bound before this batch of 63 (like FoldLevel/
    # KeyMod/MarginType above) but never documented; added here for the same
    # reason as those. Most values have a corresponding typed signal on
    # ScintillaEditBase (see SCINTILLA_EDIT_BASE_SIGNAL_DOCS below) that
    # delivers the same notification without needing this enum directly --
    # noted on each member where one exists. The few without one are only
    # reachable via the raw `notify` signal's `NotificationData.nmhdr.code`.
    "Notification": (
        "Identifies which Scintilla notification (`SCN_*`) a `NotificationData` carries, as "
        "`NotificationData.nmhdr.code` -- delivered via the raw `notify` signal, or (for most values) a "
        "corresponding typed signal on `ScintillaEditBase` that carries the same notification already "
        "unpacked into typed parameters.",
        {
            "StyleNeeded": "Corresponds to the `styleNeeded` signal.",
            "CharAdded": "Corresponds to the `charAdded` signal.",
            "SavePointReached": "Corresponds to the `savePointChanged` signal with `dirty=False`.",
            "SavePointLeft": "Corresponds to the `savePointChanged` signal with `dirty=True`.",
            "ModifyAttemptRO": "Corresponds to the `modifyAttemptReadOnly` signal.",
            "Key": "Corresponds to the `key` signal.",
            "DoubleClick": "Corresponds to the `doubleClick` signal.",
            "UpdateUI": "Corresponds to the `updateUi` signal.",
            "Modified": "Corresponds to the `modified` signal.",
            "MacroRecord": "Corresponds to the `macroRecord` signal.",
            "MarginClick": "Corresponds to the `marginClicked` signal.",
            "NeedShown": "Corresponds to the `needShown` signal.",
            "Painted": "Corresponds to the `painted` signal.",
            "UserListSelection": "Corresponds to the `userListSelection` signal.",
            "URIDropped": "Corresponds to the `uriDropped` signal.",
            "DwellStart": "Corresponds to the `dwellStart` signal.",
            "DwellEnd": "Corresponds to the `dwellEnd` signal.",
            "Zoom": "Corresponds to the `zoom` signal.",
            "HotSpotClick": "Corresponds to the `hotSpotClick` signal.",
            "HotSpotDoubleClick": "Corresponds to the `hotSpotDoubleClick` signal.",
            "CallTipClick": "Corresponds to the `callTipClick` signal.",
            "AutoCSelection": "Corresponds to the `autoCompleteSelection` signal.",
            "IndicatorClick": "The mouse was clicked over an indicator; no typed signal exists for this -- "
            "only reachable via the raw `notify` signal.",
            "IndicatorRelease": "The mouse button was released after a click over an indicator; no typed "
            "signal exists for this -- only reachable via the raw `notify` signal.",
            "AutoCCancelled": "Corresponds to the `autoCompleteCancelled` signal.",
            "AutoCCharDeleted": "A character was deleted from an active autocompletion word; no typed "
            "signal exists for this -- only reachable via the raw `notify` signal.",
            "HotSpotReleaseClick": "The mouse button was released after a click on hotspot-styled text; no "
            "typed signal exists for this -- only reachable via the raw `notify` signal.",
            "FocusIn": "Corresponds to the `focusChanged` signal with `focused=True`.",
            "FocusOut": "Corresponds to the `focusChanged` signal with `focused=False`.",
            "AutoCCompleted": "Autocompleted text has just been inserted; no typed signal exists for this "
            "-- only reachable via the raw `notify` signal.",
            "MarginRightClick": "The mouse was right-clicked in a sensitive margin; no typed signal exists "
            "for this -- only reachable via the raw `notify` signal.",
            "AutoCSelectionChange": "The current selection in an autocompletion list changed without being "
            "chosen; no typed signal exists for this -- only reachable via the raw `notify` signal.",
        },
    ),
    "Ordering": (
        "Controls how the autocompletion list passed to `SCI_AUTOCSHOW` is ordered, set with "
        "`SCI_AUTOCSETORDER` before showing the list.",
        {
            "PreSorted": "The default; requires the application to supply the list already in alphabetical "
            "sorted order.",
            "PerformSort": "Scintilla sorts the list itself; takes additional time compared to `PreSorted`.",
            "Custom": "The application provides the list in a priority order other than alphabetical; "
            "requires extra processing to build a sorted index.",
        },
    ),
    "PhasesDraw": (
        "Selects the drawing order/strategy for the text area, trading speed against correctly rendering "
        "overlapping pixels, set with `SCI_SETPHASESDRAW`.",
        {
            "One": "Deprecated single-phase drawing: each run of characters is drawn with its background in "
            "one pass, which can let a following run's background cut off an overhanging character. Should "
            "not be used by applications.",
            "Two": "The default: draws all line backgrounds first, then all text in transparent mode; lines "
            "never overlap, so extreme ascenders/descenders are clipped.",
            "Multiple": "Draws the whole area multiple times, layering backgrounds then text without "
            "clipping to line boundaries, allowing extreme ascenders/descenders to overflow into adjacent "
            "lines; slower than `Two`, and incompatible with buffered drawing.",
        },
    ),
    "PopUp": (
        "Controls when the built-in default context/edit menu is shown, set with `SCI_USEPOPUP`.",
        {
            "Never": "Never show the default editing menu; context-menu messages are passed to the parent "
            "window instead.",
            "All": "Show the default editing menu when clicking anywhere on the Scintilla window.",
            "Text": "Show the default editing menu only when clicking on the text area.",
        },
    ),
    "PrintOption": (
        "Colour mode used when printing the document, set with `SCI_SETPRINTCOLOURMODE`; useful for saving "
        "ink/toner when the editor uses a dark screen theme.",
        {
            "Normal": "Default: prints using the current screen colours, except line-number margins print "
            "on a white background.",
            "InvertLight": "Inverts the lightness of all colours and prints on a white background, saving "
            "ink for dark screen themes.",
            "BlackOnWhite": "Prints all text as black on a white background.",
            "ColourOnWhite": "Prints everything in its own colour on a white background.",
            "ColourOnWhiteDefaultBG": "Prints everything in its own foreground colour, but all styles up to "
            "and including the line-number style print on a white background.",
            "ScreenColours": "Prints using the current screen colours for both foreground and background; "
            "the only mode that does not force the line-number margin background to white.",
        },
    ),
    "RepresentationAppearance": (
        "Flags controlling how a character representation set with `SCI_SETREPRESENTATION` is drawn, used "
        "with `SCI_SETREPRESENTATIONAPPEARANCE`.",
        {
            "Plain": "Draws the representation text with no decoration.",
            "Blob": "Draws the representation text inverted inside a rounded rectangle (a small badge); "
            "this is the default appearance.",
            "Colour": "If set, the representation is drawn in the colour set for it; if a colour is set but "
            "this flag is not, the representation shows in the colour of the underlying text instead.",
        },
    ),
    "SelectionMode": (
        "The selection mode used by `SCI_SETSELECTIONMODE`/`SCI_CHANGESELECTIONMODE`/`SCI_GETSELECTIONMODE`, "
        "controlling how caret moves extend the selection.",
        {
            "Stream": "Regular, contiguous text selection.",
            "Rectangle": "Rectangular (column) selection.",
            "Lines": "Selection extended by whole lines.",
            "Thin": "The mode entered automatically after typing into a rectangular selection, ensuring no "
            "characters remain selected.",
        },
    ),
    "Status": (
        "Error/warning status codes returned by `SCI_GETSTATUS` and set by `SCI_SETSTATUS`; values 1-999 "
        "are errors and `WarnStart` (1000) and above are warnings.",
        {
            "Ok": "No failures.",
            "Failure": "Generic failure.",
            "BadAlloc": "Memory is exhausted.",
            "OutsideDocument": "An operation was attempted on a position that is outside the document.",
            "WarnStart": "The threshold at and above which status codes are warnings rather than errors.",
            "RegEx": "The regular expression is invalid; returned when the C++11 <regex> engine is selected "
            "and given a malformed pattern.",
        },
    ),
    # StylesCommon was already bound before this batch of 63 (like FoldLevel/
    # KeyMod/MarginType/Notification above) but never documented; added here
    # for the same reason as those.
    "StylesCommon": (
        "Predefined style numbers with special meaning, used with `SCI_STYLESETFORE` and friends; lexer "
        "styles occupy 0 to `Max`, and `SCI_STYLECLEARALL` resets every style to `Default`'s attributes.",
        {
            "Default": "The attributes every style is reset to by `SCI_STYLECLEARALL`.",
            "LineNumber": "Attributes of the line-number margin's text; its background colour also sets "
            "the background of any margin not used for folding (see `SCI_SETMARGINMASKN`).",
            "BraceLight": "Attributes used to highlight a matched brace, via `SCI_BRACEHIGHLIGHT`, and its "
            "corresponding indentation guide via `SCI_SETHIGHLIGHTGUIDE`.",
            "BraceBad": "Attributes used to mark an unmatched brace, via `SCI_BRACEBADLIGHT`.",
            "ControlChar": "Font used when drawing control characters; only font/size/bold/italic/"
            "character-set attributes apply, not colour -- see also `SCI_SETCONTROLCHARSYMBOL`.",
            "IndentGuide": "Foreground/background colours used when drawing indentation guides.",
            "CallTip": "Attributes for call tips when `SCI_CALLTIPUSESTYLE` is used; otherwise call tips use "
            "`Default`. Only font face/size, foreground/background colour, and character set apply.",
            "FoldDisplayText": "Attributes for text tags attached to folded text.",
            "LastPredefined": "The last predefined style number (39), so client code can discover the "
            "range of predefined styles without hardcoding it.",
            "Max": "The highest style number that can be set (255); styles between `LastPredefined` and "
            "this value are free for lexers/applications to use.",
        },
    ),
    "Supports": (
        "Feature flags queried with `SCI_SUPPORTSFEATURE` to check which drawing/measurement capabilities "
        "the current platform supports.",
        {
            "LineDrawsFinal": "Whether drawing a line draws its final position; only false on Win32 GDI.",
            "PixelDivisions": "Whether logical pixels are larger than physical pixels (sub-pixel positioning "
            "is possible); currently only true for macOS Cocoa with 'retina' displays.",
            "FractionalStrokeWidth": "Whether lines can be drawn with fractional widths like 1.5 or 0.5 "
            "pixels.",
            "TranslucentStroke": "Whether translucent lines, polygons, ellipses, and text can be drawn (e.g. "
            "true for Direct2D, false for GDI).",
            "PixelModification": "Whether individual pixels can be modified; false for character-cell "
            "platforms like curses.",
            "ThreadSafeMeasureWidths": "Whether text measurement can be safely performed concurrently on "
            "multiple threads.",
        },
    ),
    "TabDrawMode": (
        "How tab characters are drawn when white space is made visible, set with `SCI_SETTABDRAWMODE`.",
        {
            "LongArrow": "The default mode: an arrow stretching until the tabstop.",
            "StrikeOut": "A horizontal line stretching until the tabstop.",
            "ControlChar": "Drawn as a control code according to the configured character representation, "
            "without any indentation.",
        },
    ),
    "Technology": (
        "The drawing API/technology used for rendering, set with `SCI_SETTECHNOLOGY`; choices beyond "
        "`Default` are Windows-specific DirectWrite variants.",
        {
            "Default": "Use the older GDI API, compatible with all versions of Windows including Vista and "
            "XP.",
            "DirectWrite": "Use the Direct2D and DirectWrite APIs for higher quality antialiased drawing "
            "(Windows 7+).",
            "DirectWriteRetain": "Request that the frame is retained after being presented, which may "
            "prevent drawing failures on some cards and drivers.",
            "DirectWriteDC": "Use DirectWrite to draw into a GDI DC; may work for remote access/RDP "
            "sessions.",
            "DirectWrite1": "Use DirectWrite in a lower-level way that manages graphics state more "
            "explicitly.",
        },
    ),
    "TypeProperty": (
        "How to interpret the string value of a named lexer property (set via `SCI_SETPROPERTY`), as "
        "reported by `SCI_PROPERTYTYPE` -- all property values are passed as plain strings regardless of "
        "type. Only available for newer lexers; a companion to `SCI_PROPERTYNAMES` (lists property names) "
        "and `SCI_DESCRIBEPROPERTY` (a human-readable description), e.g. for building a generic lexer "
        "property editor.",
        {
            "Boolean": 'The property\'s string value is "0" or "1".',
            "Integer": "The property's string value is a number.",
            "String": "The property's string value is arbitrary text.",
        },
    ),
    "UndoFlags": (
        "Flags passed to `SCI_ADDUNDOACTION` controlling how a container-supplied undo action interacts with "
        "coalescing of other undo actions.",
        {
            "MayCoalesce": "The container action may be coalesced together with surrounding insertion/"
            "deletion actions into a single compound action.",
        },
    ),
    "UndoSelectionHistoryOption": (
        "Controls whether selection (and scroll position) state is restored when performing undo/redo, set "
        "with `SCI_SETUNDOSELECTIONHISTORY`.",
        {
            "Disabled": "The default: undo selection history turned off.",
            "Enabled": "Restore the selection for each undo and redo.",
            "Scroll": "Also restore the vertical scroll position; has no effect unless combined with "
            "`Enabled`.",
        },
    ),
    "VisiblePolicy": (
        "Flags for `SCI_SETVISIBLEPOLICY` controlling vertical positioning when "
        "`SCI_ENSUREVISIBLEENFORCEPOLICY` is called; operates like the caret's vertical policy "
        "(`SCI_SETYCARETPOLICY`).",
        {
            "Slop": "Defines an unwanted zone, a number of lines near the vertical margins where the target "
            "line should not end up, keeping it within visible context.",
            "Strict": "Enforces the slop policy strictly: the line is centred on the display if no slop "
            "value is set, and cannot land in the unwanted zone if one is set.",
        },
    ),
    "WhiteSpace": (
        "The white-space display mode set with `SCI_SETVIEWWS`/`SCI_GETVIEWWS`, controlling whether spaces "
        "and tabs are drawn as visible dots and arrows.",
        {
            "Invisible": "The normal display mode: white space is displayed as an empty background colour.",
            "VisibleAlways": "White space characters are always drawn as dots and arrows.",
            "VisibleAfterIndent": "Indentation white space is displayed normally, but after the first "
            "visible character on the line, white space is shown as dots and arrows.",
            "VisibleOnlyInIndent": "Only the white space used for indentation is displayed as dots and "
            "arrows; white space elsewhere on the line is shown normally.",
        },
    ),
    "Wrap": (
        "The line-wrap mode set with `SCI_SETWRAPMODE` (and, partially, `SCI_SETPRINTWRAPMODE`).",
        {
            "None_": "Disables line wrapping.",
            "Word": "Wraps on word or style boundaries; if a word is longer than a line it is still wrapped "
            "before the line end.",
            "Char": "Wraps between any characters; preferred for Asian languages where there is no white "
            "space between words. Not supported for printing.",
            "WhiteSpace": "Wraps on whitespace boundaries.",
        },
    ),
    "WrapIndentMode": (
        "Controls how wrapped sublines of a line are indented relative to the first subline, set with "
        "`SCI_SETWRAPINDENTMODE`.",
        {
            "Fixed": "Wrapped sublines are aligned to the left of the window plus the amount set by "
            "`SCI_SETWRAPSTARTINDENT` (the default mode).",
            "Same": "Wrapped sublines are aligned to the first subline's indent.",
            "Indent": "Wrapped sublines are aligned to the first subline's indent plus one more level of "
            "indentation.",
            "DeepIndent": "Wrapped sublines are aligned to the first subline's indent plus two more levels "
            "of indentation.",
        },
    ),
    "WrapVisualFlag": (
        "Bit flags for `SCI_SETWRAPVISUALFLAGS` controlling which visual indicators are drawn to show a line "
        "has wrapped.",
        {
            "End": "Draws a visual flag at the end of each wrapped subline.",
            "Start": "Draws a visual flag at the start of each wrapped subline; the subline is indented by "
            "at least 1 to make room for the flag.",
            "Margin": "Draws a visual flag in the line-number margin.",
        },
    ),
    "WrapVisualLocation": (
        "Set with `SCI_SETWRAPVISUALFLAGSLOCATION`, controls where wrap visual flags are drawn relative to "
        "the text versus the window border.",
        {
            "Default": "Visual flags are drawn near the border.",
            "EndByText": "The end-of-subline visual flag is drawn near the text instead of the border.",
            "StartByText": "The start-of-subline visual flag is drawn near the text instead of the border.",
        },
    ),
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

# Hand-written class docstring for ScintillaDocument -- genpyi has nothing to
# stitch a class docstring from, since this is the binding's own class, not a
# Qt class.
SCINTILLA_DOCUMENT_CLASS_DOC: Final = (
    "Wraps a Scintilla document buffer independently of any `ScintillaEdit` view.\n\n"
    "    Obtain one from an existing editor via `ScintillaEdit.get_doc()` (and share it "
    "with another editor via `set_doc()`), or construct one standalone to hold text "
    "off-screen. Exposes a subset of `ScintillaEdit`'s editing/undo API directly on the "
    "buffer, plus `modified`/`save_point`/etc. signals."
)


# Hand-transcribed from WatcherHelper's Notify*() overrides in
# ScintillaDocument.cpp and Document::CheckReadOnly()/SetErrorStatus() in
# Document.cxx -- these mirror a subset of ScintillaEditBase's notifications
# (see SCINTILLA_EDIT_BASE_SIGNAL_DOCS) but aren't Qt overrides and have no
# Scintilla.iface `evt` doc comments, so genpyi gives them no docstring.
SCINTILLA_DOCUMENT_SIGNAL_DOCS: Final = {
    "modify_attempt": "An edit was attempted while the document is read-only (SCN_MODIFYATTEMPTRO).",
    "save_point": "The document entered (`True`) or left (`False`) its save point (SCN_SAVEPOINTREACHED/SCN_SAVEPOINTLEFT).",
    "modified": (
        "The document's text or styling changed, or is about to (SCN_MODIFIED). `modification_type` "
        "is a `Scintilla.ModificationFlags` bitmask describing what; `text` holds the inserted/deleted "
        "bytes for `Scintilla.ModificationFlags.InsertText`/`DeleteText`."
    ),
    "style_needed": (
        "Container-lexer styling is needed up to `pos` (SCN_STYLENEEDED). Only sent if "
        "`Scintilla.Message.SetILexer` was passed `None`."
    ),
    "error_occurred": (
        "An internal error occurred while editing the document. `status` is one of Scintilla's "
        "internal `Scintilla.Status` codes (e.g. out-of-memory or a malformed regular expression)."
    ),
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


# Hand-written class docstring for ScintillaEditBase -- genpyi has nothing to
# stitch a class docstring from, since this is the binding's own widget, not
# a Qt class.
SCINTILLA_EDIT_BASE_CLASS_DOC: Final = (
    "Qt widget exposing Scintilla's editor core via the raw `Scintilla.Message` API.\n\n"
    "    `send`/`sends` send any message; `notify` and the typed signals below "
    "(`modified`, `charAdded`, `updateUi`, ...) deliver Scintilla's notifications. "
    "For a typed method per message, use the `ScintillaEdit` subclass instead."
)


# Hand-transcribed from the "Notifications" section of ScintillaDoc.html and
# ScintillaEditBase.cpp's notifyParent()/emit call sites -- Scintilla.iface
# has no doc comments for these `evt` lines, and they're Qt signals, not Qt
# overrides, so genpyi gives them no docstring either.
SCINTILLA_EDIT_BASE_SIGNAL_DOCS: Final = {
    "aboutToCopy": (
        "Emitted just before selected text is copied to the clipboard, with the `QMimeData` "
        "about to be placed there.\n\n"
        "        Connect to add extra formats (e.g. rich text) to `data` before it's copied."
    ),
    "autoCompleteCancelled": "The user cancelled an active autocompletion list (SCN_AUTOCCANCELLED).",
    "autoCompleteSelection": (
        "The user selected `text` from an autocompletion list, before it's inserted "
        "(SCN_AUTOCSELECTION). `position` is the start of the word being completed.\n\n"
        "        Call `Scintilla.Message.AutoCCancel` during this signal to stop the automatic insertion."
    ),
    "buttonPressed": "A mouse button was pressed over the editor.",
    "buttonReleased": "A mouse button was released over the editor.",
    "callTipClick": "The user clicked the visible call tip (SCN_CALLTIPCLICK).",
    "charAdded": (
        "The user typed an ordinary character that was inserted into the text (SCN_CHARADDED). "
        "`ch` is its character code -- a Unicode code point in UTF-8 mode."
    ),
    "command": (
        "Emitted for compatibility with other Scintilla front-ends' command notifications, e.g. "
        "alongside `notifyChange` with `wParam`/`lParam` encoding `SCEN_CHANGE` and the control id."
    ),
    "doubleClick": "The mouse was double-clicked at `position` on `line` (SCN_DOUBLECLICK).",
    "dwellEnd": (
        "The mouse pointer, which had been dwelling, moved or other activity ended the dwell "
        "(SCN_DWELLEND). `x`/`y` are where the dwell occurred."
    ),
    "dwellStart": (
        "The mouse pointer has rested at `(x, y)` for the dwell period set with "
        "`Scintilla.Message.SetMouseDwellTime` (SCN_DWELLSTART)."
    ),
    "focusChanged": "The editor gained (`True`) or lost (`False`) keyboard focus (SCN_FOCUSIN/SCN_FOCUSOUT).",
    "horizontalRangeChanged": "The horizontal scrollbar's range changed to `max` with page size `page`.",
    "horizontalScrolled": "The view scrolled horizontally; `value` is the new horizontal scroll position.",
    "hotSpotClick": (
        "The user clicked text styled with the hotspot attribute, at `position`, with `modifiers` "
        "held down (SCN_HOTSPOTCLICK)."
    ),
    "hotSpotDoubleClick": "Like `hotSpotClick`, but for a double-click (SCN_HOTSPOTDOUBLECLICK).",
    "key": (
        "Reports a key press not consumed by Scintilla (SCN_KEY). Only emitted on GTK, and only "
        "for Alt/Ctrl-modified keys below 256 -- prefer `keyPressed` for a portable signal."
    ),
    "keyPressed": "A key was pressed over the editor, after Scintilla has had a chance to handle it.",
    "linesAdded": "The number of lines in the document changed by `linesAdded` (negative if lines were removed).",
    "macroRecord": (
        "A recordable action occurred while macro recording is enabled "
        "(`Scintilla.Message.StartRecord`, SCN_MACRORECORD). `message`/`wParam`/`lParam` are the "
        "message to replay."
    ),
    "marginClicked": (
        "The mouse was clicked in a margin marked sensitive with "
        "`Scintilla.Message.SetMarginSensitiveN` (SCN_MARGINCLICK). `position` is the start of the "
        "clicked line and `margin` its index."
    ),
    "modified": (
        "The document's text or styling changed, or is about to (SCN_MODIFIED). `type` is a "
        "`Scintilla.ModificationFlags` bitmask describing what; `text` holds the inserted/deleted "
        "bytes for `Scintilla.ModificationFlags.InsertText`/`DeleteText`."
    ),
    "modifyAttemptReadOnly": "The user tried to edit the document while it is read-only (SCN_MODIFYATTEMPTRO).",
    "needShown": (
        "A range of currently-hidden lines should be made visible, e.g. with "
        "`Scintilla.Message.EnsureVisible` (SCN_NEEDSHOWN)."
    ),
    "notify": (
        "Delivers every Scintilla notification, before the typed signals above are emitted for it.\n\n"
        "        See the `NotificationData` lifetime caveat in docs/bindings.md -- prefer a typed "
        "signal where one exists."
    ),
    "notifyChange": "The document was modified; emitted alongside `command` for compatibility.",
    "painted": "Painting has just completed (SCN_PAINTED).",
    "resized": "The widget was resized.",
    "savePointChanged": (
        "The document entered (`True`) or left (`False`) its save point (SCN_SAVEPOINTREACHED/SCN_SAVEPOINTLEFT)."
    ),
    "styleNeeded": (
        "Container-lexer styling is needed up to `position` (SCN_STYLENEEDED). Only sent if "
        "`Scintilla.Message.SetILexer` was passed `None`."
    ),
    "textAreaClicked": "The text area was clicked on `line`, with `modifiers` held down.",
    "updateUi": (
        "The text, styling, selection, or scroll position may have changed (SCN_UPDATEUI). "
        "`updated` is a `Scintilla.Update` bitmask of what changed since the previous notification."
    ),
    "uriDropped": "The user dragged a URI such as a file path onto the editor (SCN_URIDROPPED, GTK only).",
    "userListSelection": (
        "The user selected an item from a user list shown with `Scintilla.Message.UserListShow` "
        "(SCN_USERLISTSELECTION)."
    ),
    "verticalRangeChanged": "The vertical scrollbar's range changed to `max` with page size `page`.",
    "verticalScrolled": "The view scrolled vertically; `value` is the new top visible line.",
    "zoom": "The zoom level changed to `zoom`, e.g. via `Scintilla.Message.SetZoom` (SCN_ZOOM).",
}


# Hand-transcribed from ScintillaEditBase.cpp -- notifyParent/event_command
# are plain slots (not Qt overrides), and the Qt virtual-method overrides
# below have no Scintilla-specific docs anywhere, so genpyi emits only bare
# signatures for all of them.
SCINTILLA_EDIT_BASE_OVERRIDE_DOCS: Final = {
    "notifyParent": (
        "Internal slot: receives a raw Scintilla notification and emits `notify`, plus the "
        "corresponding typed signal above (e.g. `modified`, `charAdded`, `updateUi`)."
    ),
    "event_command": "Internal slot: emits `command(wParam, lParam)` for compatibility with other Scintilla front-ends.",
    "scrollHorizontal": "Scroll the view horizontally to `value`, e.g. from a connected `QScrollBar`.",
    "scrollVertical": "Scroll the view vertically to `value` (the top visible line), e.g. from a connected `QScrollBar`.",
    "contextMenuEvent": "Reimplemented from `QWidget`: shows Scintilla's built-in right-click context menu.",
    "dragEnterEvent": "Reimplemented from `QWidget`: accepts drags carrying text or URLs, for drag-and-drop editing.",
    "dragLeaveEvent": "Reimplemented from `QWidget`: cancels the drop-position indicator drawn by `dragMoveEvent`.",
    "dragMoveEvent": "Reimplemented from `QWidget`: moves the drop-position indicator as a drag tracks over the editor.",
    "dropEvent": "Reimplemented from `QWidget`: inserts the dropped text (or file URIs), completing a drag-and-drop edit.",
    "event": (
        "Reimplemented from `QObject`: routes `QEvent.Type.KeyPress` to `keyPressEvent` directly, "
        "bypassing Qt's tab-focus handling so Scintilla sees Tab/Backtab as editing keys."
    ),
    "focusInEvent": "Reimplemented from `QWidget`: tells Scintilla it gained keyboard focus (SCN_FOCUSIN, `focusChanged(True)`).",
    "focusOutEvent": "Reimplemented from `QWidget`: tells Scintilla it lost keyboard focus (SCN_FOCUSOUT, `focusChanged(False)`).",
    "inputMethodEvent": "Reimplemented from `QWidget`: forwards input-method composition/commit events to Scintilla for IME text entry.",
    "inputMethodQuery": "Reimplemented from `QWidget`: reports caret geometry, font, and surrounding text to the input method.",
    "keyPressEvent": (
        "Reimplemented from `QWidget`: translates the key event into a Scintilla command (caret "
        "movement, deletion, character insertion, ...) and emits `keyPressed`."
    ),
    "leaveEvent": "Reimplemented from `QWidget`: tells Scintilla the mouse left the editor, clearing any hover state.",
    "mouseDoubleClickEvent": "Reimplemented from `QWidget`: Scintilla does its own double-click detection from `mousePressEvent`.",
    "mouseMoveEvent": "Reimplemented from `QWidget`: updates the selection while dragging, and hover/dwell state.",
    "mousePressEvent": "Reimplemented from `QWidget`: positions the caret or starts a selection, and emits `buttonPressed`.",
    "mouseReleaseEvent": (
        "Reimplemented from `QWidget`: ends a selection drag and emits `textAreaClicked` and `buttonReleased`."
    ),
    "paintEvent": "Reimplemented from `QWidget`: repaints the visible document.",
    "resizeEvent": "Reimplemented from `QWidget`: updates Scintilla's view size and scrollbars, and emits `resized`.",
    "scrollContentsBy": (
        "Reimplemented from `QAbstractScrollArea`: a no-op -- Scintilla repaints the viewport "
        "itself rather than blitting it."
    ),
    "wheelEvent": "Reimplemented from `QWidget`: scrolls the view, or changes zoom when Ctrl is held.",
}


def parse_iface_docs(iface_path: Path) -> dict[str, str]:
    """Map Scintilla.iface `fun`/`get`/`set`/`evt` feature names to their `# ` doc comments.

    A doc comment only documents a feature if it's on the line immediately
    above it, matching how Scintilla.iface is written -- a blank line (or
    anything else) in between discards it.
    """
    docs: dict[str, str] = {}
    pending: list[str] = []
    for line in iface_path.read_text(encoding="utf-8").splitlines():
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
    for line in iface_path.read_text(encoding="utf-8").splitlines():
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
    for line in iface_path.read_text(encoding="utf-8").splitlines():
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


def add_namespace_constants(text: str) -> str:
    """Insert typed, documented `Scintilla.<Name>` attributes for SCINTILLA_NAMESPACE_CONSTANTS_DOCS.

    Inserted right after the primitive aliases (must run after
    `add_primitive_aliases`), since genpyi never emits these at all -- see
    SCINTILLA_NAMESPACE_CONSTANTS_DOCS above for why.
    """
    lines = [
        "\n"
        "    # ScintillaTypes.h's free-standing constexpr constants -- not enum\n"
        "    # members, but real Scintilla.<Name> attributes at runtime.\n"
    ]
    for name, (value, doc) in SCINTILLA_NAMESPACE_CONSTANTS_DOCS.items():
        lines.append(f"    {name}: typing.Final = {value!r}\n")
        lines.append(f'    r"""{doc}"""\n')
    return text.replace(PRIMITIVE_ALIASES, PRIMITIVE_ALIASES + "".join(lines), 1)


def add_enum_docstrings(
    text: str,
    enum_class: str,
    docs: dict[str, str],
    class_doc: str | None = None,
) -> str:
    """Insert `class_doc` after `Scintilla.<enum_class>`'s header, then each doc in `docs` after the member it documents."""
    out: list[str] = []
    in_enum = False
    class_line = f"    class {enum_class}(enum.IntEnum):"
    for line in text.splitlines(keepends=True):
        if line.startswith(class_line):
            in_enum = True
            out.append(line)
            if class_doc:
                out.append(f'        r"""{class_doc}"""\n')
            continue
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


def add_class_docstring(text: str, class_name: str, doc: str) -> str:
    """Insert `doc` as a docstring on the line after `class {class_name}(...):`."""
    pattern = re.compile(rf"^(class {re.escape(class_name)}\(.*\):\n)", re.M)
    return pattern.sub(lambda m: m.group(1) + f'    r"""{doc}"""\n', text, count=1)


def add_signal_docstrings(text: str, class_name: str, docs: dict[str, str]) -> str:
    """Insert each doc as a docstring after the `ClassVar[Signal]` attribute it documents, within `class_name`."""
    out: list[str] = []
    in_class = False
    class_line = f"class {class_name}("
    for line in text.splitlines(keepends=True):
        if line.startswith(class_line):
            in_class = True
        elif in_class and line.startswith("class "):
            in_class = False
        out.append(line)
        if in_class:
            match = SIGNAL_RE.match(line)
            if match:
                indent, name = match.group(1), match.group(2)
                doc = docs.get(name)
                if doc:
                    out.append(f'{indent}r"""{doc}"""\n')
    return "".join(out)


def fix_self_import(text: str) -> str:
    """Rewrite genpyi's bare `import _pyside6_scintilla` to the real dotted module path.

    genpyi derives the self-import from the extension's runtime `__name__`
    (bare `_pyside6_scintilla`, since shiboken doesn't qualify compiled
    extension module names with their parent package), not from where the
    stub is actually installed (`pyside6_scintilla/_pyside6_scintilla.pyi`,
    i.e. submodule `pyside6_scintilla._pyside6_scintilla`). Pyright can't
    resolve a bare top-level `_pyside6_scintilla` import, so every
    `_pyside6_scintilla.<Name>` reference -- return types like
    `ScintillaEdit.get_doc()`, and base classes like
    `ScintillaEditFixed(_pyside6_scintilla.ScintillaEdit)` -- silently
    resolves to `Unknown`, along with every member a subclass inherits
    through one of those unresolved bases.
    """
    return text.replace(
        "import _pyside6_scintilla\n",
        "import pyside6_scintilla._pyside6_scintilla as _pyside6_scintilla\n",
        1,
    )


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
    text = PYI_PATH.read_text(encoding="utf-8")
    text = fix_self_import(text)
    text = normalize_send_signatures(text)
    text = add_primitive_aliases(text)
    text = add_namespace_constants(text)
    text = add_enum_docstrings(text, "Message", parse_iface_docs(IFACE_PATH))
    text = add_enum_docstrings(text, "CharacterSource", parse_character_source_docs(IFACE_PATH))
    text = add_enum_docstrings(text, "VirtualSpace", VIRTUAL_SPACE_DOCS)
    text = add_enum_docstrings(text, "Update", UPDATE_DOCS)
    text = add_enum_docstrings(
        text,
        "ModificationFlags",
        MODIFICATION_FLAGS_DOCS,
        class_doc=(
            "Bitmask describing what kind of document change occurred, delivered as the `type`/"
            "`modification_type` parameter of `ScintillaEditBase.modified`/`ScintillaDocument.modified` "
            "(SCN_MODIFIED), and used to filter which kinds of modification get reported at all via "
            "`SCI_SETMODEVENTMASK`/`SCI_GETMODEVENTMASK`."
        ),
    )
    for enum_name, (class_doc, member_docs) in ENUM_DOCS.items():
        text = add_enum_docstrings(text, enum_name, member_docs, class_doc=class_doc)
    text = add_class_docstring(text, "ScintillaEditBase", SCINTILLA_EDIT_BASE_CLASS_DOC)
    text = add_class_docstring(text, "ScintillaDocument", SCINTILLA_DOCUMENT_CLASS_DOC)
    text = add_signal_docstrings(text, "ScintillaDocument", SCINTILLA_DOCUMENT_SIGNAL_DOCS)
    text = add_signal_docstrings(text, "ScintillaEditBase", SCINTILLA_EDIT_BASE_SIGNAL_DOCS)
    # ScintillaEditBaseFixed/ScintillaEditFixed only redeclare the signals
    # scintilla_signal_fixes.h re-emits with plain-int signatures (see
    # docs/bindings.md) -- add_signal_docstrings only matches `ClassVar[Signal]`
    # lines that exist in the target class body, so reusing the same dict here
    # documents just those masked/visible ones, not all ~37.
    text = add_signal_docstrings(text, "ScintillaEditBaseFixed", SCINTILLA_EDIT_BASE_SIGNAL_DOCS)
    text = add_signal_docstrings(text, "ScintillaEditFixed", SCINTILLA_EDIT_BASE_SIGNAL_DOCS)
    text = add_method_docstrings(text, "ScintillaEditBase", SEND_DOCS)
    text = add_method_docstrings(text, "ScintillaEditBase", SCINTILLA_EDIT_BASE_OVERRIDE_DOCS)
    text = add_method_docstrings(text, "ScintillaEdit", SCINTILLA_EDIT_HELPER_DOCS)
    text = add_method_docstrings(text, "ScintillaEdit", parse_widget_method_docs(IFACE_PATH))
    text = add_method_docstrings(text, "ScintillaDocument", SCINTILLA_DOCUMENT_DOCS)
    text = widen_sends_string_param(text)
    text = widen_const_char_ptr_params(text)
    text = resolve_sptr_uptr_forward_refs(text)
    PYI_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
