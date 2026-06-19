"""Minimal QMainWindow showing Python syntax highlighting and folding driven by tree-sitter.

The actual styling/folding logic lives in tree_sitter_highlighter.py
(TreeSitterHighlighter), which can be copied into your own project on its
own.

Run with:
    uv run python examples/highlighting/tree_sitter_highlighting/main.py
"""

import sys
from typing import Final

import tree_sitter_python
from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QApplication, QMainWindow
from tree_sitter import Language
from tree_sitter_highlighter import TreeSitterHighlighter

from pyside6_scintilla import ScintillaEdit

SAMPLE_TEXT = '''\
"""pyside6-scintilla: tree-sitter syntax highlighting example."""

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

# A minimal highlight query, hand-written for this example rather than
# pulled from nvim-treesitter's full python/highlights.scm - covers the
# capture names TreeSitterHighlighter maps to a style in CAPTURE_STYLES.
HIGHLIGHTS_QUERY = """
(comment) @comment
(string) @string
(integer) @number
(float) @number
(true) @keyword
(false) @keyword
(none) @keyword
(function_definition name: (identifier) @function)
(class_definition name: (identifier) @class)
(call function: (identifier) @function)
(call function: (attribute attribute: (identifier) @function))
[
  "and" "as" "assert" "async" "await" "break" "class" "continue" "def" "del"
  "elif" "else" "except" "finally" "for" "from" "global" "if" "import" "in"
  "is" "lambda" "nonlocal" "not" "or" "pass" "raise" "return" "try" "while"
  "with" "yield"
] @keyword
"""


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("pyside6-scintilla: tree-sitter syntax highlighting example")
        self.resize(800, 600)

        self.__editor: Final = ScintillaEdit()
        self.setCentralWidget(self.__editor)
        self.__editor.setText(SAMPLE_TEXT)

        fixed_font = QFontDatabase.systemFont(QFontDatabase.SystemFont.FixedFont)
        language = Language(tree_sitter_python.language())
        # Parented to self - no need to keep a reference here.
        TreeSitterHighlighter(self.__editor, language, HIGHLIGHTS_QUERY, fixed_font, self)


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
