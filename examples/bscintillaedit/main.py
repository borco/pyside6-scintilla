"""Minimal QMainWindow built around the portable BScintillaEdit widget.

Demonstrates BScintillaEdit's drop-in API:
- toolbar toggles for lineNumbersVisible, lineWrapped, lineEndVisible, readOnly
- toolbutton menus for picking the end-of-line representation glyph and colour

Run with:
    uv run python examples/bscintillaedit/main.py
"""

import sys
from typing import Final

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QToolBar, QToolButton

from bscintillaedit import EOL_REPRESENTATION_APPEARANCE, EOL_REPRESENTATION_COLOUR, BScintillaEdit

SAMPLE_TEXT = """\
pyside6-scintilla: BScintillaEdit example

BScintillaEdit is a single-file, drop-in replacement for the old
bscintillaedit package's widget (see examples/bscintillaedit/bscintillaedit.py
and its README for the full API and porting instructions).

Use the toolbar to toggle line numbers, line wrapping, end-of-line markers,
read-only mode, and block editing, and to pick how the end-of-line marker
is drawn.

With "Block Edit" on, hold Alt and drag (or use Alt+Shift+Arrow) to make a
rectangular selection, then type to edit every selected line at once.

one
two
three
four
five
"""

EOL_GLYPHS: Final = ("↩", "¶", "↵", "⏎", "␊")
"""Glyphs offered in the "End of Line" toolbar menu, passed to `setRepresentation("\\n", ...)`."""

EOL_COLOURS: Final = (
    ("Default", EOL_REPRESENTATION_COLOUR),
    ("Red", 0xFF0000FF),
    ("Green", 0xFF00FF00),
    ("Blue", 0xFFFF0000),
    ("Gray", 0xFF808080),
)
"""Colours (ARGB, as packed by `setRepresentationColour`) offered in the "EOL Colour" toolbar menu.

The first entry restores `BScintillaEdit`'s default end-of-line colour.
"""


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("pyside6-scintilla: BScintillaEdit example")
        self.resize(800, 600)

        self.__editor: Final = BScintillaEdit()
        self.setCentralWidget(self.__editor)
        self.__editor.setText(SAMPLE_TEXT)
        self.__editor.setLineNumbersVisible(True)

        self.__eol_colour = EOL_REPRESENTATION_COLOUR

        self.__setup_toolbar()

    def __setup_toolbar(self) -> None:
        toolbar = QToolBar("Main")
        self.addToolBar(toolbar)

        toggle_line_numbers_action = QAction("Line Numbers", self)
        toggle_line_numbers_action.setCheckable(True)
        toggle_line_numbers_action.setChecked(bool(self.__editor.lineNumbersVisible))
        toggle_line_numbers_action.toggled.connect(self.__editor.setLineNumbersVisible)
        toolbar.addAction(toggle_line_numbers_action)

        toggle_line_wrapped_action = QAction("Wrap Lines", self)
        toggle_line_wrapped_action.setCheckable(True)
        toggle_line_wrapped_action.setChecked(bool(self.__editor.lineWrapped))
        toggle_line_wrapped_action.toggled.connect(self.__editor.setLineWrapped)
        toolbar.addAction(toggle_line_wrapped_action)

        toggle_line_end_visible_action = QAction("Show EOL", self)
        toggle_line_end_visible_action.setCheckable(True)
        toggle_line_end_visible_action.setChecked(bool(self.__editor.lineEndVisible))
        toggle_line_end_visible_action.toggled.connect(self.__editor.setLineEndVisible)
        toolbar.addAction(toggle_line_end_visible_action)

        toggle_read_only_action = QAction("Read Only", self)
        toggle_read_only_action.setCheckable(True)
        toggle_read_only_action.setChecked(bool(self.__editor.readOnly))
        toggle_read_only_action.toggled.connect(self.__editor.setReadOnly)
        toolbar.addAction(toggle_read_only_action)

        toggle_block_edit_action = QAction("Block Edit", self)
        toggle_block_edit_action.setCheckable(True)
        toggle_block_edit_action.setChecked(bool(self.__editor.blockEditEnabled))
        toggle_block_edit_action.toggled.connect(self.__editor.setBlockEditEnabled)
        toolbar.addAction(toggle_block_edit_action)

        toolbar.addSeparator()
        toolbar.addWidget(self.__setup_eol_glyph_button())
        toolbar.addWidget(self.__setup_eol_colour_button())

    def __setup_eol_glyph_button(self) -> QToolButton:
        """A toolbutton with a menu for picking the end-of-line representation glyph."""
        button = QToolButton(self)
        button.setText("End of Line")
        button.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)

        menu = QMenu(button)
        for glyph in EOL_GLYPHS:
            action = QAction(glyph, menu)
            action.triggered.connect(lambda _checked=False, glyph=glyph: self.__set_eol_glyph(glyph))
            menu.addAction(action)
        button.setMenu(menu)

        return button

    def __setup_eol_colour_button(self) -> QToolButton:
        """A toolbutton with a menu for picking the end-of-line representation colour."""
        button = QToolButton(self)
        button.setText("EOL Colour")
        button.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)

        menu = QMenu(button)
        for name, colour in EOL_COLOURS:
            action = QAction(name, menu)
            action.triggered.connect(lambda _checked=False, colour=colour: self.__set_eol_colour(colour))
            menu.addAction(action)
        button.setMenu(menu)

        return button

    def __set_eol_glyph(self, glyph: str) -> None:
        """Change the end-of-line representation glyph, keeping its current colour.

        `setRepresentation` resets the representation's colour/appearance to
        Scintilla's plain default, so re-apply the tracked colour afterwards.
        """
        self.__editor.setRepresentation("\n", glyph)
        self.__editor.setRepresentationColour("\n", self.__eol_colour)
        self.__editor.setRepresentationAppearance("\n", EOL_REPRESENTATION_APPEARANCE)

    def __set_eol_colour(self, colour: int) -> None:
        """Change the end-of-line representation colour, keeping its current glyph."""
        self.__eol_colour = colour
        self.__editor.setRepresentationColour("\n", colour)
        self.__editor.setRepresentationAppearance("\n", EOL_REPRESENTATION_APPEARANCE)


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
