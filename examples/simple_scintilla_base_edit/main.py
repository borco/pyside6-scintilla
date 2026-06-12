"""Minimal QMainWindow built around a ScintillaEditBase central widget.

Demonstrates:
- a toolbar button that shows/hides the line-number margin
- enabling block (rectangular) selection and block (multi-line) editing

Run with:
    uv run python examples/simple_scintilla_base_edit/main.py
"""

import sys
from typing import Final

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar

from pyside6_scintilla import Scintilla, ScintillaEditBase

LINE_NUMBER_MARGIN = 0

SAMPLE_TEXT = """\
pyside6-scintilla: simple ScintillaEditBase example

Use the "Line Numbers" toolbar button to show/hide this margin.

Block selection / block editing is enabled:
  - Hold Alt and drag with the mouse, or use Alt+Shift+Arrow keys, to
    make a rectangular (block) selection.
  - Typing while a rectangular/multiple selection is active edits every
    selected line at once.

one
two
three
four
five
"""


def line_number_margin_width(editor: ScintillaEditBase) -> int:
    """Pixel width that fits the current number of lines, plus a little padding."""
    line_count = editor.send(Scintilla.Message.GetLineCount)
    digits = max(2, len(str(line_count)))
    return editor.sends(Scintilla.Message.TextWidth, Scintilla.StylesCommon.LineNumber, "9" * digits) + 4


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("pyside6-scintilla: simple ScintillaEditBase example")
        self.resize(800, 600)

        self.__editor: Final = ScintillaEditBase()
        self.setCentralWidget(self.__editor)

        self.__setup_editor()
        self.__setup_toolbar()

    def __setup_editor(self) -> None:
        editor = self.__editor
        message = Scintilla.Message

        editor.sends(message.SetText, 0, SAMPLE_TEXT)

        # Line-number margin, shown by default.
        editor.send(message.SetMarginTypeN, LINE_NUMBER_MARGIN, Scintilla.MarginType.Number)
        editor.send(message.SetMarginWidthN, LINE_NUMBER_MARGIN, line_number_margin_width(editor))

        # Block (rectangular) selection and block editing: Alt+drag or
        # Alt+Shift+Arrow makes a rectangular selection, and typing applies
        # to every line of a multiple/rectangular selection at once.
        editor.send(message.SetMouseSelectionRectangularSwitch, 1)
        editor.send(message.SetMultipleSelection, 1)
        editor.send(message.SetAdditionalSelectionTyping, 1)
        editor.send(
            message.SetVirtualSpaceOptions,
            Scintilla.VirtualSpace.RectangularSelection | Scintilla.VirtualSpace.UserAccessible,
        )

    def __setup_toolbar(self) -> None:
        toolbar = QToolBar("Main")
        self.addToolBar(toolbar)

        self.__toggle_line_numbers_action = QAction("Line Numbers", self)
        self.__toggle_line_numbers_action.setCheckable(True)
        self.__toggle_line_numbers_action.setChecked(True)
        self.__toggle_line_numbers_action.toggled.connect(self.__toggle_line_numbers)
        toolbar.addAction(self.__toggle_line_numbers_action)

    def __toggle_line_numbers(self, checked: bool) -> None:
        editor = self.__editor
        width = line_number_margin_width(editor) if checked else 0
        editor.send(Scintilla.Message.SetMarginWidthN, LINE_NUMBER_MARGIN, width)


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
