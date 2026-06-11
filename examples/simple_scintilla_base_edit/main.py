"""Minimal QMainWindow built around a ScintillaEditBase central widget.

Demonstrates:
- a toolbar button that shows/hides the line-number margin
- enabling block (rectangular) selection and block (multi-line) editing

Run with:
    uv run python examples/simple_scintilla_base_edit/main.py
"""

import sys

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar

from pyside6_scintilla import Scintilla, ScintillaEditBase

# Not yet exposed as wrapped enums (see docs/BINDINGS.md) -- raw values from
# src/scintilla/include/Scintilla.h.
SC_MARGIN_NUMBER = 1
SCVS_RECTANGULARSELECTION = 1
SCVS_USERACCESSIBLE = 2
STYLE_LINENUMBER = 33

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


def _line_number_margin_width(editor: ScintillaEditBase) -> int:
    """Pixel width that fits the current number of lines, plus a little padding."""
    line_count = editor.send(int(Scintilla.Message.GetLineCount))
    digits = max(2, len(str(line_count)))
    return editor.sends(int(Scintilla.Message.TextWidth), STYLE_LINENUMBER, "9" * digits) + 4


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyside6-scintilla: simple ScintillaEditBase example")
        self.resize(800, 600)

        self.editor = ScintillaEditBase()
        self.setCentralWidget(self.editor)

        self._setup_editor()
        self._setup_toolbar()

    def _setup_editor(self) -> None:
        editor = self.editor
        message = Scintilla.Message

        editor.sends(int(message.SetText), 0, SAMPLE_TEXT)

        # Line-number margin, shown by default.
        editor.send(int(message.SetMarginTypeN), LINE_NUMBER_MARGIN, SC_MARGIN_NUMBER)
        editor.send(int(message.SetMarginWidthN), LINE_NUMBER_MARGIN, _line_number_margin_width(editor))

        # Block (rectangular) selection and block editing: Alt+drag or
        # Alt+Shift+Arrow makes a rectangular selection, and typing applies
        # to every line of a multiple/rectangular selection at once.
        editor.send(int(message.SetMouseSelectionRectangularSwitch), 1)
        editor.send(int(message.SetMultipleSelection), 1)
        editor.send(int(message.SetAdditionalSelectionTyping), 1)
        editor.send(int(message.SetVirtualSpaceOptions), SCVS_RECTANGULARSELECTION | SCVS_USERACCESSIBLE)

    def _setup_toolbar(self) -> None:
        toolbar = QToolBar("Main")
        self.addToolBar(toolbar)

        self.toggle_line_numbers_action = QAction("Line Numbers", self)
        self.toggle_line_numbers_action.setCheckable(True)
        self.toggle_line_numbers_action.setChecked(True)
        self.toggle_line_numbers_action.toggled.connect(self._toggle_line_numbers)
        toolbar.addAction(self.toggle_line_numbers_action)

    def _toggle_line_numbers(self, checked: bool) -> None:
        editor = self.editor
        width = _line_number_margin_width(editor) if checked else 0
        editor.send(int(Scintilla.Message.SetMarginWidthN), LINE_NUMBER_MARGIN, width)


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
