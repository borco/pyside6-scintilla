"""Minimal QMainWindow showing Python syntax highlighting driven by Pygments.

The actual styling logic lives in pygments_highlighter.py (PygmentsHighlighter),
which can be copied into your own project on its own.

Run with:
    uv run python examples/highlighting/pygments_highlighting/main.py
"""

import sys
from typing import Final

from pygments.lexers.python import PythonLexer
from pygments_highlighter import PygmentsHighlighter
from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QApplication, QMainWindow

from pyside6_scintilla import ScintillaEdit

SAMPLE_TEXT = '''\
"""pyside6-scintilla: Pygments syntax highlighting example."""

import sys


class Greeter:
    """Says hello, the long way round."""

    def __init__(self, name: str = "world") -> None:
        self.name = name

    def greet(self) -> str:
        # f-strings, decorators, and numbers all get their own style below.
        return f"Hello, {self.name}! ({1 + 2} reasons to say hi)"


if __name__ == "__main__":
    print(Greeter(sys.argv[1] if len(sys.argv) > 1 else "world").greet())
'''


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("pyside6-scintilla: Pygments syntax highlighting example")
        self.resize(800, 600)

        self.__editor: Final = ScintillaEdit()
        self.setCentralWidget(self.__editor)
        self.__editor.setText(SAMPLE_TEXT)

        fixed_font = QFontDatabase.systemFont(QFontDatabase.SystemFont.FixedFont)
        # Parented to self - no need to keep a reference here.
        PygmentsHighlighter(self.__editor, PythonLexer(), fixed_font, self)


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
