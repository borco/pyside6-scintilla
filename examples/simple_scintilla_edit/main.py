"""Minimal QMainWindow built around a ScintillaEdit central widget.

Contrasts with `simple_scintilla_base_edit`, which uses ScintillaEditBase's
raw `send`/`sends` message API: this example uses ScintillaEdit's typed,
per-message methods (e.g. `setText()`, `lineCount()`, `gotoLine()`) instead.

Demonstrates:
- a toolbar button that shows/hides the line-number margin
- a "Go to Line" toolbar action

Run with:
    uv run python examples/simple_scintilla_edit/main.py
"""

import sys
from typing import Final

from PySide6.QtGui import QAction, QFontDatabase
from PySide6.QtWidgets import QApplication, QInputDialog, QMainWindow, QToolBar

from pyside6_scintilla import Scintilla, ScintillaEdit

LINE_NUMBER_MARGIN = 0

SAMPLE_TEXT = """\
pyside6-scintilla: simple ScintillaEdit example

Use the "Line Numbers" toolbar button to show/hide this margin, and
"Go to Line" to jump to a line by number.

one
two
three
four
five
"""


def line_number_margin_width(editor: ScintillaEdit) -> int:
    """Pixel width that fits the current number of lines, plus a little padding."""
    digits = max(2, len(str(editor.lineCount())))
    return editor.textWidth(Scintilla.StylesCommon.LineNumber, "9" * digits) + 4


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("pyside6-scintilla: simple ScintillaEdit example")
        self.resize(800, 600)

        self.__editor: Final = ScintillaEdit()
        self.setCentralWidget(self.__editor)

        self.__setup_editor()
        self.__setup_toolbar()

    def __setup_editor(self) -> None:
        editor = self.__editor

        # Use the platform's default fixed-width font instead of Scintilla's
        # built-in default (a proportional font), as is conventional for a
        # code editor.
        fixed_font = QFontDatabase.systemFont(QFontDatabase.SystemFont.FixedFont)
        editor.styleSetFont(Scintilla.StylesCommon.Default, fixed_font.family())
        editor.styleClearAll()

        editor.setText(SAMPLE_TEXT)

        # Line-number margin, shown by default.
        editor.setMarginTypeN(LINE_NUMBER_MARGIN, Scintilla.MarginType.Number)
        editor.setMarginWidthN(LINE_NUMBER_MARGIN, line_number_margin_width(editor))

    def __setup_toolbar(self) -> None:
        toolbar = QToolBar("Main")
        self.addToolBar(toolbar)

        self.__toggle_line_numbers_action = QAction("Line Numbers", self)
        self.__toggle_line_numbers_action.setCheckable(True)
        self.__toggle_line_numbers_action.setChecked(True)
        self.__toggle_line_numbers_action.toggled.connect(self.__toggle_line_numbers)
        toolbar.addAction(self.__toggle_line_numbers_action)

        goto_line_action = QAction("Go to Line...", self)
        goto_line_action.triggered.connect(self.__goto_line)
        toolbar.addAction(goto_line_action)

    def __toggle_line_numbers(self, checked: bool) -> None:
        editor = self.__editor
        width = line_number_margin_width(editor) if checked else 0
        editor.setMarginWidthN(LINE_NUMBER_MARGIN, width)

    def __goto_line(self) -> None:
        editor = self.__editor
        line_count = editor.lineCount()
        current_line = editor.lineFromPosition(editor.currentPos()) + 1

        line, ok = QInputDialog.getInt(self, "Go to Line", "Line number:", current_line, 1, line_count)
        if ok:
            editor.gotoLine(line - 1)


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
