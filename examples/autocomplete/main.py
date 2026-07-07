"""Word autocompletion driven by a static keyword list.

`pyside6-scintilla` exposes Scintilla's autocompletion messages directly
(`autoCShow`, `autoCSetIgnoreCase`, ...) rather than a high-level wrapper like
QScintilla's `QsciAPIs`, so this example shows how to wire those messages up
yourself. Scintilla filters the list we hand it by the already-typed prefix
and keeps the popup in sync as more characters are typed, so all we do is:
- watch the `charAdded` signal,
- work out the word fragment under the caret,
- and call `autoCShow()` with the full keyword list once enough has been
  typed. Scintilla inserts the chosen word on Tab/Enter automatically.

A Ctrl+Space shortcut explicitly (re)opens the popup -- handy after
dismissing it with Esc, or to complete a word mid-way.

The `autoCompleteSelection` / `autoCompleteCancelled` signals are wired up
purely to show how to react to the outcome (e.g. for logging or call tips).

Run with:
    uv run python examples/autocomplete/main.py
"""

import sys
from typing import Final

from PySide6.QtGui import QFontDatabase, QKeySequence, QShortcut
from PySide6.QtWidgets import QApplication, QMainWindow, QStatusBar

from pyside6_scintilla import Scintilla, ScintillaEdit

# Show the popup as soon as this many word characters have been typed.
COMPLETION_THRESHOLD: Final = 1

# The words offered for completion. In a real editor these might come from a
# lexer's keyword sets, the symbols in the open document, or a language
# server; here they are just a static, illustrative list. Scintilla wants the
# list sorted (by byte value, case-insensitively here) to match items.
KEYWORDS: Final = sorted(
    [
        "and",
        "as",
        "assert",
        "async",
        "await",
        "break",
        "class",
        "continue",
        "def",
        "del",
        "elif",
        "else",
        "except",
        "finally",
        "for",
        "from",
        "global",
        "if",
        "import",
        "in",
        "is",
        "lambda",
        "nonlocal",
        "not",
        "or",
        "pass",
        "raise",
        "return",
        "try",
        "while",
        "with",
        "yield",
        "print",
        "range",
        "len",
        "enumerate",
        "zip",
        "map",
        "filter",
        "sorted",
        "reversed",
        "isinstance",
        "hasattr",
        "getattr",
    ],
    key=str.lower,
)

# Characters that make up a "word" for completion purposes. Kept in sync with
# what Scintilla considers word characters via SCI_SETWORDCHARS below.
WORD_CHARS: Final = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

SAMPLE_TEXT = """\
pyside6-scintilla: autocomplete example

Start typing a Python-ish keyword below (e.g. "de", "imp", "ret") and an
autocompletion popup appears once one word character has been entered.

- Up/Down to move through the list.
- Tab or Enter to accept the highlighted word.
- Esc to dismiss the popup; Ctrl+Space to reopen it.

The status bar reports each selection or cancellation.

"""


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("pyside6-scintilla: autocomplete example")
        self.resize(800, 600)

        self.__editor: Final = ScintillaEdit()
        self.setCentralWidget(self.__editor)

        self.__status: Final = QStatusBar()
        self.setStatusBar(self.__status)
        self.__status.showMessage("Type to trigger autocompletion.")

        self.__setup_editor()
        self.__setup_autocomplete()

    def __setup_editor(self) -> None:
        editor = self.__editor

        # Fixed-width font, as is conventional for a code editor.
        fixed_font = QFontDatabase.systemFont(QFontDatabase.SystemFont.FixedFont)
        editor.styleSetFont(Scintilla.StylesCommon.Default, fixed_font.family())
        editor.styleClearAll()

        editor.setText(SAMPLE_TEXT)
        editor.gotoPos(editor.length())

    def __setup_autocomplete(self) -> None:
        editor = self.__editor

        # Match words case-insensitively, so typing "DE" still offers "def".
        # This is QScintilla's setAutoCompletionCaseSensitivity(False).
        editor.autoCSetIgnoreCase(True)

        # Don't auto-insert when only a single item matches -- let the user
        # confirm, so the popup behaviour is easy to observe in this example.
        editor.autoCSetChooseSingle(False)

        # Keep the popup up if the prefix stops matching, rather than cancelling
        # abruptly; Scintilla re-filters as more characters are typed.
        editor.autoCSetCancelAtStart(False)

        # Tell Scintilla which characters make up a word, so its
        # wordStartPosition() below agrees with our KEYWORDS.
        editor.setWordChars(WORD_CHARS)

        editor.charAdded.connect(self.__on_char_added)
        editor.autoCompleteSelection.connect(self.__on_selection)
        editor.autoCompleteCancelled.connect(self.__on_cancelled)

        # Ctrl+Space explicitly (re)opens the popup, e.g. after dismissing it
        # with Esc, or in the middle of an already-typed word. QScintilla wires
        # this to its standard SCI_AUTOCSHOW invocation too.
        show_completion = QShortcut(QKeySequence("Ctrl+Space"), editor)
        show_completion.activated.connect(self.__show_completion)

    def __on_char_added(self, ch: int) -> None:
        """Show/refresh the completion popup as the user types a word."""
        # Only react to word characters; typing a space or punctuation should
        # not (re)open the popup. An explicit Ctrl+Space (below) has no such
        # threshold and can open the popup with nothing typed yet.
        if chr(ch) not in WORD_CHARS:
            return
        self.__show_completion(threshold=COMPLETION_THRESHOLD)

    def __show_completion(self, threshold: int = 0) -> None:
        """Show the completion popup for the word fragment under the caret.

        `threshold` is the minimum number of already-typed word characters
        required: `COMPLETION_THRESHOLD` when typing, but 0 for an explicit
        Ctrl+Space so the full list appears even at a word boundary.
        """
        editor = self.__editor
        current_pos = editor.currentPos()
        # Start of the word fragment under the caret. `onlyWordCharacters=True`
        # walks back over WORD_CHARS from the caret.
        word_start = editor.wordStartPosition(current_pos, True)
        length_entered = current_pos - word_start
        if length_entered < threshold:
            return

        # Hand Scintilla the whole list; it filters by the typed prefix and
        # keeps the selection in sync as further characters arrive. The list is
        # a single space-separated string (the default item separator).
        editor.autoCShow(length_entered, " ".join(KEYWORDS))

    def __on_selection(self, position: int, text: str) -> None:
        """React to the user accepting an item (before it's inserted)."""
        self.__status.showMessage(f"Completed: {text!r} at position {position}")

    def __on_cancelled(self) -> None:
        """React to the user dismissing the popup (Esc, or typing past a match)."""
        self.__status.showMessage("Autocompletion cancelled.")


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
