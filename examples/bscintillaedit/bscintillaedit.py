"""Portable, single-file `BScintillaEdit` convenience subclass.

A spiritual successor to the old Windows-only `bscintillaedit` PyPI package
(see `docs/mission.md`), but as a single file meant to be copied straight
into another project rather than installed as a package: a `ScintillaEdit`
with a fixed-width font and a line-number margin set up out of the box.

Run the demo with:
    uv run python examples/bscintillaedit/main.py
"""

from typing import Final

from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QWidget

from pyside6_scintilla import Scintilla, ScintillaEdit

_LINE_NUMBER_MARGIN: Final = 0


def _line_number_margin_width(editor: ScintillaEdit) -> int:
    """Pixel width that fits the current number of lines, plus a little padding."""
    digits = max(2, len(str(editor.lineCount())))
    return editor.textWidth(Scintilla.StylesCommon.LineNumber, "9" * digits) + 4


class BScintillaEdit(ScintillaEdit):
    """A `ScintillaEdit` with sane defaults: fixed-width font and a line-number margin."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        fixed_font = QFontDatabase.systemFont(QFontDatabase.SystemFont.FixedFont)
        self.styleSetFont(Scintilla.StylesCommon.Default, fixed_font.family())
        self.styleClearAll()

        self.setMarginTypeN(_LINE_NUMBER_MARGIN, Scintilla.MarginType.Number)
        self.setLineNumbersVisible(True)

    def setLineNumbersVisible(self, visible: bool) -> None:
        """Show or hide the line-number margin."""
        width = _line_number_margin_width(self) if visible else 0
        self.setMarginWidthN(_LINE_NUMBER_MARGIN, width)

    def lineNumbersVisible(self) -> bool:
        """Whether the line-number margin is currently shown."""
        return self.marginWidthN(_LINE_NUMBER_MARGIN) > 0
