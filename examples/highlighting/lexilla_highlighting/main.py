"""Minimal QMainWindow showing real C++ syntax highlighting via Lexilla.

Wires a lexilla-created "cpp" lexer into a ScintillaEdit via SCI_SETILEXER
(setILexer()) -- the cross-binding pointer path described in lexilla-py's
docs/specs/mission.md "Cross-binding integration" decision. Unlike this
repo's own pygments_highlighting/tree_sitter_highlighting examples, no
re-tokenizing glue code is needed here: once the lexer is wired up,
Scintilla calls its Lex()/Fold() itself whenever the editor needs to
(re)style text.

Run with:
    uv run python examples/highlighting/lexilla_highlighting/main.py
"""

import sys
from typing import Final

from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QApplication, QMainWindow
from pyside6_scintilla import Scintilla, ScintillaEdit

from lexilla import Language, create_lexer

# SCE_C_* style numbers the "cpp" lexer assigns, from Lexilla's own
# SciLexer.h -- lexilla-py doesn't bind these (they're Lexilla's, not
# Scintilla's, and out of this project's scope; see lexilla-py's
# docs/specs/mission.md). Only the subset styled below is listed.
SCE_C_DEFAULT = 0
SCE_C_COMMENT = 1
SCE_C_COMMENTLINE = 2
SCE_C_COMMENTDOC = 3
SCE_C_NUMBER = 4
SCE_C_WORD = 5
SCE_C_STRING = 6
SCE_C_PREPROCESSOR = 9
SCE_C_OPERATOR = 10
SCE_C_IDENTIFIER = 11

# Fold margin -- the second default margin (index 0 is the line-number
# margin set up below; margin 1 is what Scintilla creates with the
# Scintilla.MarginType.Symbol type out of the box).
MARGIN_FOLD: Final = 1

# The classic "boxes" fold-margin marker set (as seen in SciTE/Notepad++):
# all 7 of Scintilla's reserved fold-marker slots, one per tree position --
# leaving any of these undefined falls back to a default circle marker on
# every line in a fold body, not just header lines.
FOLD_MARKERS: Final = {
    Scintilla.MarkerOutline.FolderOpen: Scintilla.MarkerSymbol.BoxMinus,
    Scintilla.MarkerOutline.Folder: Scintilla.MarkerSymbol.BoxPlus,
    Scintilla.MarkerOutline.FolderSub: Scintilla.MarkerSymbol.VLine,
    Scintilla.MarkerOutline.FolderTail: Scintilla.MarkerSymbol.LCorner,
    Scintilla.MarkerOutline.FolderEnd: Scintilla.MarkerSymbol.BoxPlusConnected,
    Scintilla.MarkerOutline.FolderOpenMid: Scintilla.MarkerSymbol.BoxMinusConnected,
    Scintilla.MarkerOutline.FolderMidTail: Scintilla.MarkerSymbol.TCorner,
}

# Show the fold margin and let clicking it toggle the fold, without wiring
# up the marginClicked signal by hand.
AUTOMATIC_FOLD_SHOW_AND_CLICK: Final = Scintilla.AutomaticFold.Show | Scintilla.AutomaticFold.Click

# (red, green, blue) per style -- packed to Scintilla's 0xBBGGRR colour
# format by rgb() below, at the point of use.
STYLE_COLORS: Final = {
    SCE_C_DEFAULT: (0x00, 0x00, 0x00),
    SCE_C_COMMENT: (0x80, 0x80, 0x80),
    SCE_C_COMMENTLINE: (0x80, 0x80, 0x80),
    SCE_C_COMMENTDOC: (0x80, 0x80, 0x80),
    SCE_C_NUMBER: (0x80, 0x00, 0x80),
    SCE_C_WORD: (0x00, 0x00, 0x80),
    SCE_C_STRING: (0x00, 0x80, 0x00),
    SCE_C_PREPROCESSOR: (0x80, 0x40, 0x00),
    SCE_C_OPERATOR: (0x40, 0x40, 0x40),
    SCE_C_IDENTIFIER: (0x00, 0x00, 0x00),
}

# Word list 0 ("Primary keywords and identifiers", per
# Lexer.describe_word_list_sets()) -- styled as SCE_C_WORD above.
CPP_KEYWORDS: Final = (
    "alignas alignof auto bool break case catch char class const constexpr "
    "continue default delete do double else enum explicit export extern "
    "false float for friend goto if inline int long mutable namespace new "
    "noexcept nullptr operator private protected public register return "
    "short signed sizeof static struct switch template this throw true try "
    "typedef typename union unsigned using virtual void volatile while"
)

SAMPLE_TEXT: Final = """\
// lexilla-py: cpp lexer wired into pyside6-scintilla via SCI_SETILEXER
#include <cstdio>

class Greeter {
public:
    explicit Greeter(const char *name) : name_(name) {}

    void greet() const {
        std::printf("Hello, %s! (%d reasons to say hi)\\n", name_, 1 + 2);
    }

private:
    const char *name_;
};

int main() {
    Greeter("world").greet();
    return 0;
}
"""


def rgb(red: int, green: int, blue: int) -> int:
    """Pack an 8-bit RGB triple into Scintilla's 0xBBGGRR colour format."""
    return red | (green << 8) | (blue << 16)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("lexilla-py: cpp lexer in pyside6-scintilla")
        self.resize(800, 600)

        self.__editor: Final = ScintillaEdit()
        self.setCentralWidget(self.__editor)
        self.__setup_editor()

    def __setup_editor(self) -> None:
        editor = self.__editor

        fixed_font = QFontDatabase.systemFont(QFontDatabase.SystemFont.FixedFont)
        for style, (red, green, blue) in STYLE_COLORS.items():
            editor.styleSetFont(style, fixed_font.family())
            editor.styleSetFore(style, rgb(red, green, blue))
        editor.styleSetBold(SCE_C_WORD, True)
        editor.styleSetItalic(SCE_C_COMMENT, True)
        editor.styleSetItalic(SCE_C_COMMENTLINE, True)
        editor.styleSetItalic(SCE_C_COMMENTDOC, True)

        # create_lexer() returns a Lexer that owns the underlying ILexer5
        # until detach() hands it to Scintilla -- after this, the editor
        # (not lexer) owns its lifetime, and Lexer.pointer/other methods
        # must not be used again. "fold" must be set on the lexer itself
        # (it controls whether Fold() computes fold levels at all), so set
        # it before detaching.
        lexer = create_lexer(Language.CPP)
        assert lexer is not None
        lexer.property_set("fold", "1")
        editor.setILexer(lexer.detach())
        editor.setKeyWords(0, CPP_KEYWORDS)

        editor.setText(SAMPLE_TEXT)
        editor.colourise(0, -1)

        editor.setMarginWidthN(0, 40)
        editor.setMarginTypeN(0, Scintilla.MarginType.Number)

        self.__setup_folding(editor)

    def __setup_folding(self, editor: ScintillaEdit) -> None:
        editor.setMarginTypeN(MARGIN_FOLD, Scintilla.MarginType.Symbol)
        editor.setMarginMaskN(MARGIN_FOLD, Scintilla.MaskFolders)
        editor.setMarginWidthN(MARGIN_FOLD, 16)
        editor.setMarginSensitiveN(MARGIN_FOLD, True)
        for marker_number, marker_symbol in FOLD_MARKERS.items():
            editor.markerDefine(marker_number, marker_symbol)

        # Shows the fold margin and toggles a fold on click, without any
        # signal/slot code.
        editor.setAutomaticFold(AUTOMATIC_FOLD_SHOW_AND_CLICK)


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
