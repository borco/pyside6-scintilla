"""Portable, single-file `BScintillaEdit` drop-in replacement.

A `QScrollArea` wrapping a `ScintillaEdit`, exposing the same Qt properties,
signals, and slots as the old, now-archived `bscintillaedit` PyPI package's
`BScintillaEdit(QScrollArea)` widget — `lineEndVisible`, `lineNumbersVisible`,
`lineWrapped`, `readOnly`, `text` (with their `*Changed` signals and setter
slots) and `clear()` — with the same out-of-the-box defaults (LF line
endings, hidden symbol margin, styled line-number margin, "↩" end-of-line
glyph).

Source / docs: https://borco.github.io/pyside6-scintilla/examples/bscintillaedit/

Porting from the old `bscintillaedit` package
----------------------------------------------
1. Copy this file into your project.
2. Change `from bscintillaedit import BScintillaEdit` to
   `from .bscintillaedit import BScintillaEdit` (or wherever you placed it).
3. That's it — same base class, properties, signals, slots, and spelling,
   and the same defaults as the old widget, so existing code keeps working
   unchanged. The wrapped `ScintillaEdit` is available as `.editor`, for
   anything not covered by the properties below.

Run the demo with:
    uv run python examples/bscintillaedit/main.py
"""

from collections.abc import Callable
from typing import TYPE_CHECKING, Any, Final, Generic, TypeVar

from PySide6.QtCore import Property, Signal, Slot
from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QFrame, QScrollArea, QWidget

from pyside6_scintilla import Scintilla, ScintillaEdit

LINE_NUMBER_MARGIN: Final = 0
"""Margin index used for the line-number margin."""

SYMBOL_MARGIN: Final = 1
"""Margin index used for the (hidden) symbol/breakpoint margin."""

EOL_REPRESENTATION_COLOUR: Final = 0xFFC0C0FF
"""Default colour (ARGB) used for the "↩" end-of-line representation glyph."""

EOL_REPRESENTATION_APPEARANCE: Final = 0x10  # SC_REPRESENTATION_COLOUR
"""Default appearance flags used for the "↩" end-of-line representation glyph."""

_T = TypeVar("_T")


class TypedProperty(Property, Generic[_T]):
    """`QtCore.Property` with a typed `__init__`/`__get__`/`__set__` for IDE hover/type-checking.

    `QtCore.Property`'s stub doesn't declare `__get__`/`__set__`, so type
    checkers show plain `Property` attributes instead of their declared type,
    with no docstring. This subclass adds no real behavior — `__init__` just
    forwards to `QtCore.Property`, and the `__get__`/`__set__` declarations
    only exist for type checkers (`if TYPE_CHECKING`). `_T` is inferred from
    the `type: type[_T]` argument, so `TypedProperty(bool, ...)` is enough —
    no `TypedProperty[bool](...)` subscript needed.

    No runtime overhead vs. plain `Property`: `__init__` only adds one extra
    forwarding call at class-definition time (once per property, not per
    access), and `__get__`/`__set__` are `Property`'s own inherited
    implementations — the `TYPE_CHECKING` block doesn't exist at runtime.
    """

    def __init__(
        self,
        type: type[_T],  # noqa: A002 -- matches QtCore.Property's parameter name
        fget: Callable[[Any], _T] | None = None,
        fset: Callable[[Any, _T], None] | None = None,
        notify: Signal | None = None,
        doc: str = "",
    ) -> None:
        super().__init__(type, fget, fset, notify=notify, doc=doc)

    if TYPE_CHECKING:

        def __get__(self, instance: object, owner: type | None = None) -> _T: ...
        def __set__(self, instance: object, value: _T) -> None: ...


class BScintillaEdit(QScrollArea):
    """A `QScrollArea` wrapping a `ScintillaEdit`, a drop-in replacement for the old `bscintillaedit` package's widget."""

    lineEndVisibleChanged = Signal(bool)
    lineNumbersVisibleChanged = Signal(bool)
    lineWrappedChanged = Signal(bool)
    readOnlyChanged = Signal(bool)
    textChanged = Signal(str)
    blockEditEnabledChanged = Signal(bool)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        # The wrapped editor: the ~780 inherited `SCI_*` methods are available
        # directly on `.editor` for anything not covered by the properties below.
        self.editor: Final = ScintillaEdit(self)

        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setWidget(self.editor)
        self.setWidgetResizable(True)
        self.setFocusProxy(self.editor)

        fixed_font = QFontDatabase.systemFont(QFontDatabase.SystemFont.FixedFont)
        self.editor.styleSetFont(Scintilla.StylesCommon.Default, fixed_font.family())
        self.editor.styleClearAll()

        self.editor.setCodePage(65001)  # SC_CP_UTF8: interpret/encode text as UTF-8

        # Normalize line endings to LF, matching the old widget's setup().
        self.editor.setEOLMode(2)  # SC_EOL_LF
        self.editor.convertEOLs(2)  # SC_EOL_LF

        # Hide the non-folding symbol margin.
        self.editor.setMarginWidthN(SYMBOL_MARGIN, 0)

        # Pre-style the line-number margin; stays hidden until lineNumbersVisible is set.
        self.editor.setMarginTypeN(LINE_NUMBER_MARGIN, Scintilla.MarginType.Number)
        self.editor.styleSetBack(Scintilla.StylesCommon.LineNumber, 0xA0A0A0)

        # Represent line endings as a visible "↩" glyph when lineEndVisible is on.
        self.editor.setRepresentation("\n", "↩")
        self.editor.setRepresentationColour("\n", EOL_REPRESENTATION_COLOUR)
        self.editor.setRepresentationAppearance("\n", EOL_REPRESENTATION_APPEARANCE)

        # ScintillaEditBase.modified's Scintilla::Position/FoldLevel-typed parameters
        # can't be marshalled to a Python slot; get_doc().modified carries the same
        # notification with plain-int parameters instead. Keep a reference: the
        # returned ScintillaDocument has no Qt parent and stops emitting once dropped.
        self.__suppress_modified = False
        self.__doc = self.editor.get_doc()
        self.__doc.modified.connect(self.__on_modified)

    def __lineEndVisible(self) -> bool:
        """Whether end-of-line characters are shown as visible glyphs."""
        return self.editor.viewEOL()

    @Slot(bool)
    def setLineEndVisible(self, visible: bool) -> None:
        """Show or hide end-of-line characters."""
        if visible == self.editor.viewEOL():
            return
        self.editor.setViewEOL(visible)
        self.lineEndVisibleChanged.emit(visible)

    def __lineNumbersVisible(self) -> bool:
        """Whether the line-number margin is currently shown."""
        return self.editor.marginWidthN(LINE_NUMBER_MARGIN) > 0

    @Slot(bool)
    def setLineNumbersVisible(self, visible: bool) -> None:
        """Show or hide the line-number margin."""
        if visible == self.__lineNumbersVisible():
            return

        def margin_width() -> int:
            """Pixel width that fits the current number of lines, plus a little padding."""
            digits = max(2, len(str(self.editor.lineCount())))
            return self.editor.textWidth(Scintilla.StylesCommon.LineNumber, "9" * digits) + 4

        self.editor.setMarginWidthN(LINE_NUMBER_MARGIN, margin_width() if visible else 0)
        self.lineNumbersVisibleChanged.emit(visible)

    def __lineWrapped(self) -> bool:
        """Whether long lines are wrapped instead of scrolling horizontally."""
        return self.editor.wrapMode() != 0  # SC_WRAP_NONE

    @Slot(bool)
    def setLineWrapped(self, wrapped: bool) -> None:
        """Enable or disable line wrapping."""
        if wrapped == self.__lineWrapped():
            return
        self.editor.setWrapMode(3 if wrapped else 0)  # SC_WRAP_WHITESPACE / SC_WRAP_NONE
        self.lineWrappedChanged.emit(wrapped)

    def __readOnly(self) -> bool:
        """Whether the editor rejects further edits."""
        return self.editor.readOnly()

    @Slot(bool)
    def setReadOnly(self, readOnly: bool) -> None:
        """Set whether the editor rejects further edits."""
        if readOnly == self.editor.readOnly():
            return
        self.editor.setReadOnly(readOnly)
        self.readOnlyChanged.emit(readOnly)

    def __text(self) -> str:
        """The editor's full contents."""
        return bytes(self.editor.getText(self.editor.textLength() + 1).data()).rstrip(b"\x00").decode("utf-8")

    @Slot(str)
    def setText(self, text: str) -> None:
        """Replace the editor's full contents."""
        if text == self.__text():
            return

        was_read_only = self.editor.readOnly()
        if was_read_only:
            self.editor.setReadOnly(False)

        # Replacing the contents fires both a delete and an insert modified
        # notification; suppress __on_modified's emission for those and emit
        # textChanged exactly once below, with the final text.
        self.__suppress_modified = True
        try:
            self.editor.setText(text)
        finally:
            self.__suppress_modified = False

        self.editor.setSavePoint()
        self.editor.emptyUndoBuffer()

        if was_read_only:
            self.editor.setReadOnly(True)

        self.textChanged.emit(text)

    @Slot()
    def clear(self) -> None:
        """Replace the editor's contents with an empty string."""
        self.setText("")

    def __blockEditEnabled(self) -> bool:
        """Whether block (rectangular) selection and block editing are enabled."""
        return self.editor.additionalSelectionTyping()

    @Slot(bool)
    def setBlockEditEnabled(self, enabled: bool) -> None:
        """Enable or disable block (rectangular) selection and block editing.

        Alt+drag or Alt+Shift+Arrow then makes a rectangular selection, and
        typing edits every selected line at once. Not part of the old
        widget's API — new, additive functionality.
        """
        if enabled == self.__blockEditEnabled():
            return
        self.editor.setMouseSelectionRectangularSwitch(enabled)
        self.editor.setMultipleSelection(enabled)
        self.editor.setAdditionalSelectionTyping(enabled)
        self.editor.setVirtualSpaceOptions(
            Scintilla.VirtualSpace.RectangularSelection | Scintilla.VirtualSpace.UserAccessible
            if enabled
            else Scintilla.VirtualSpace.None_
        )
        self.blockEditEnabledChanged.emit(enabled)

    def __on_modified(self, _position: int, modificationType: int, *_args: object) -> None:
        """Keep the `text` property in sync by emitting `textChanged` on edits."""
        if self.__suppress_modified:
            return
        insert_or_delete = Scintilla.ModificationFlags.InsertText | Scintilla.ModificationFlags.DeleteText
        if modificationType & insert_or_delete and self.receivers("2textChanged(QString)") > 0:
            self.textChanged.emit(self.text)

    lineEndVisible = TypedProperty(bool, __lineEndVisible, setLineEndVisible, notify=lineEndVisibleChanged)
    lineNumbersVisible = TypedProperty(
        bool, __lineNumbersVisible, setLineNumbersVisible, notify=lineNumbersVisibleChanged
    )
    lineWrapped = TypedProperty(bool, __lineWrapped, setLineWrapped, notify=lineWrappedChanged)
    readOnly = TypedProperty(bool, __readOnly, setReadOnly, notify=readOnlyChanged)
    text = TypedProperty(str, __text, setText, notify=textChanged)
    blockEditEnabled = TypedProperty(bool, __blockEditEnabled, setBlockEditEnabled, notify=blockEditEnabledChanged)
