"""Portable, single-file `BScintillaEdit` drop-in replacement.

A `ScintillaEdit` subclass that exposes the same Qt properties, signals, and
slots as the old, now-archived `bscintillaedit` PyPI package's
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
3. That's it — same properties/signals/slots/spelling and the same defaults
   as the old widget, so existing code keeps working unchanged.

Run the demo with:
    uv run python examples/bscintillaedit/main.py
"""

from typing import Final

from PySide6.QtCore import Property, Signal, Slot
from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QWidget

from pyside6_scintilla import Scintilla, ScintillaEdit

LINE_NUMBER_MARGIN: Final = 0
"""Margin index used for the line-number margin."""

SYMBOL_MARGIN: Final = 1
"""Margin index used for the (hidden) symbol/breakpoint margin."""

EOL_REPRESENTATION_COLOUR: Final = 0xFFC0C0FF
"""Default colour (ARGB) used for the "↩" end-of-line representation glyph."""

EOL_REPRESENTATION_APPEARANCE: Final = 0x10  # SC_REPRESENTATION_COLOUR
"""Default appearance flags used for the "↩" end-of-line representation glyph."""


class BScintillaEdit(ScintillaEdit):
    """A `ScintillaEdit` that's a drop-in replacement for the old `bscintillaedit` package's widget."""

    lineEndVisibleChanged = Signal(bool)
    lineNumbersVisibleChanged = Signal(bool)
    lineWrappedChanged = Signal(bool)
    readOnlyChanged = Signal(bool)
    textChanged = Signal(str)
    blockEditEnabledChanged = Signal(bool)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        fixed_font = QFontDatabase.systemFont(QFontDatabase.SystemFont.FixedFont)
        self.styleSetFont(Scintilla.StylesCommon.Default, fixed_font.family())
        self.styleClearAll()

        self.setCodePage(65001)  # SC_CP_UTF8: interpret/encode text as UTF-8

        # Normalize line endings to LF, matching the old widget's setup().
        self.setEOLMode(2)  # SC_EOL_LF
        self.convertEOLs(2)  # SC_EOL_LF

        # Hide the non-folding symbol margin.
        self.setMarginWidthN(SYMBOL_MARGIN, 0)

        # Pre-style the line-number margin; stays hidden until lineNumbersVisible is set.
        self.setMarginTypeN(LINE_NUMBER_MARGIN, Scintilla.MarginType.Number)
        self.styleSetBack(Scintilla.StylesCommon.LineNumber, 0xA0A0A0)

        # Represent line endings as a visible "↩" glyph when lineEndVisible is on.
        self.setRepresentation("\n", "↩")
        self.setRepresentationColour("\n", EOL_REPRESENTATION_COLOUR)
        self.setRepresentationAppearance("\n", EOL_REPRESENTATION_APPEARANCE)

        # ScintillaEditBase.modified's Scintilla::Position/FoldLevel-typed parameters
        # can't be marshalled to a Python slot; get_doc().modified carries the same
        # notification with plain-int parameters instead. Keep a reference: the
        # returned ScintillaDocument has no Qt parent and stops emitting once dropped.
        self.__suppress_modified = False
        self.__doc = self.get_doc()
        self.__doc.modified.connect(self.__on_modified)

    def __lineEndVisible(self) -> bool:
        """Whether end-of-line characters are shown as visible glyphs."""
        return self.viewEOL()

    @Slot(bool)
    def setLineEndVisible(self, visible: bool) -> None:
        """Show or hide end-of-line characters."""
        if visible == self.viewEOL():
            return
        self.setViewEOL(visible)
        self.lineEndVisibleChanged.emit(visible)

    def __lineNumbersVisible(self) -> bool:
        """Whether the line-number margin is currently shown."""
        return self.marginWidthN(LINE_NUMBER_MARGIN) > 0

    @Slot(bool)
    def setLineNumbersVisible(self, visible: bool) -> None:
        """Show or hide the line-number margin."""
        if visible == self.__lineNumbersVisible():
            return

        def margin_width() -> int:
            """Pixel width that fits the current number of lines, plus a little padding."""
            digits = max(2, len(str(self.lineCount())))
            return self.textWidth(Scintilla.StylesCommon.LineNumber, "9" * digits) + 4

        self.setMarginWidthN(LINE_NUMBER_MARGIN, margin_width() if visible else 0)
        self.lineNumbersVisibleChanged.emit(visible)

    def __lineWrapped(self) -> bool:
        """Whether long lines are wrapped instead of scrolling horizontally."""
        return self.wrapMode() != 0  # SC_WRAP_NONE

    @Slot(bool)
    def setLineWrapped(self, wrapped: bool) -> None:
        """Enable or disable line wrapping."""
        if wrapped == self.__lineWrapped():
            return
        self.setWrapMode(3 if wrapped else 0)  # SC_WRAP_WHITESPACE / SC_WRAP_NONE
        self.lineWrappedChanged.emit(wrapped)

    def __readOnly(self) -> bool:
        """Whether the editor rejects further edits."""
        return super().readOnly()

    @Slot(bool)
    def setReadOnly(self, readOnly: bool) -> None:
        """Set whether the editor rejects further edits."""
        if readOnly == super().readOnly():
            return
        super().setReadOnly(readOnly)
        self.readOnlyChanged.emit(readOnly)

    def __text(self) -> str:
        """The editor's full contents."""
        return bytes(self.getText(self.textLength() + 1).data()).rstrip(b"\x00").decode("utf-8")

    @Slot(str)
    def setText(self, text: str) -> None:
        """Replace the editor's full contents."""
        if text == self.__text():
            return

        was_read_only = super().readOnly()
        if was_read_only:
            super().setReadOnly(False)

        # Replacing the contents fires both a delete and an insert modified
        # notification; suppress __on_modified's emission for those and emit
        # textChanged exactly once below, with the final text.
        self.__suppress_modified = True
        try:
            super().setText(text)
        finally:
            self.__suppress_modified = False

        self.setSavePoint()
        self.emptyUndoBuffer()

        if was_read_only:
            super().setReadOnly(True)

        self.textChanged.emit(text)

    @Slot()
    def clear(self) -> None:
        """Replace the editor's contents with an empty string."""
        self.setText("")

    def __blockEditEnabled(self) -> bool:
        """Whether block (rectangular) selection and block editing are enabled."""
        return self.additionalSelectionTyping()

    @Slot(bool)
    def setBlockEditEnabled(self, enabled: bool) -> None:
        """Enable or disable block (rectangular) selection and block editing.

        Alt+drag or Alt+Shift+Arrow then makes a rectangular selection, and
        typing edits every selected line at once. Not part of the old
        widget's API — new, additive functionality.
        """
        if enabled == self.__blockEditEnabled():
            return
        self.setMouseSelectionRectangularSwitch(enabled)
        self.setMultipleSelection(enabled)
        self.setAdditionalSelectionTyping(enabled)
        self.setVirtualSpaceOptions(
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

    lineEndVisible = Property(bool, __lineEndVisible, setLineEndVisible, notify=lineEndVisibleChanged)
    lineNumbersVisible = Property(bool, __lineNumbersVisible, setLineNumbersVisible, notify=lineNumbersVisibleChanged)
    lineWrapped = Property(bool, __lineWrapped, setLineWrapped, notify=lineWrappedChanged)
    readOnly = Property(bool, __readOnly, setReadOnly, notify=readOnlyChanged)  # type: ignore[assignment]
    text = Property(str, __text, setText, notify=textChanged)
    blockEditEnabled = Property(bool, __blockEditEnabled, setBlockEditEnabled, notify=blockEditEnabledChanged)
