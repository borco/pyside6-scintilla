"""Minimal QMainWindow built around the portable BScintillaEdit widget.

Demonstrates:
- BScintillaEdit's defaults (fixed-width font, line-number margin)
- a toolbar button that shows/hides the line-number margin

Run with:
    uv run python examples/bscintillaedit/main.py
"""

import sys
from typing import Final

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar

from bscintillaedit import BScintillaEdit

SAMPLE_TEXT = """\
pyside6-scintilla: BScintillaEdit example

BScintillaEdit is a single-file, portable ScintillaEdit subclass meant to
be copied into your own project (see examples/bscintillaedit/bscintillaedit.py).

It sets a fixed-width font and shows a line-number margin by default.
Use the "Line Numbers" toolbar button to toggle the margin.

one
two
three
four
five
"""


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("pyside6-scintilla: BScintillaEdit example")
        self.resize(800, 600)

        self.__editor: Final = BScintillaEdit()
        self.setCentralWidget(self.__editor)
        self.__editor.setText(SAMPLE_TEXT)

        self.__setup_toolbar()

    def __setup_toolbar(self) -> None:
        toolbar = QToolBar("Main")
        self.addToolBar(toolbar)

        toggle_line_numbers_action = QAction("Line Numbers", self)
        toggle_line_numbers_action.setCheckable(True)
        toggle_line_numbers_action.setChecked(self.__editor.lineNumbersVisible())
        toggle_line_numbers_action.toggled.connect(self.__editor.setLineNumbersVisible)
        toolbar.addAction(toggle_line_numbers_action)


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
