"""Minimal QMainWindow showing real C++ syntax highlighting via Lexilla.

Wires a lexilla-created "cpp" lexer into a ScintillaEdit via lexilla's
set_lexer() glue (which itself calls SCI_SETILEXER/setILexer()) -- the
cross-binding pointer path described in lexilla-py's docs/specs/mission.md
"Cross-binding integration" decision. Unlike this repo's own
pygments_highlighting/tree_sitter_highlighting examples, no re-tokenizing
glue code is needed here: once the lexer is wired up, Scintilla calls its
Lex()/Fold() itself whenever the editor needs to (re)style text.

Run with:
    uv run python examples/highlighting/lexilla_highlighting/main.py
"""

import sys
from dataclasses import dataclass
from typing import Final

from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QApplication, QMainWindow
from pyside6_scintilla import Scintilla, ScintillaEdit

from lexilla import Language, create_lexer
from lexilla.pyside6_scintilla import set_lexer

# Scintilla starts with 5 margins, plain slots numbered 0..Scintilla.MaxMargin
# (4) -- editor.setMargins(n) can allocate more/fewer. A margin index by
# itself means nothing; setMarginTypeN()/setMarginWidthN()/etc. below are
# what actually give a slot a role (line numbers, symbols, folding, ...),
# so there's no Scintilla or pyside6-scintilla enum for "the line-number
# margin" or "the fold margin" -- only for what you *do* with a slot once
# picked (e.g. Scintilla.MarginType, used below). By convention (not
# enforced by Scintilla) margin 0 defaults to line numbers and margin 1 to
# non-folding symbols, which is why this example reuses them for the same
# roles instead of inventing its own numbering.
#
# To add a third margin -- e.g. for git-blame/revision text, or a separate
# bookmark margin distinct from the fold margin -- pick an unused index
# (2, 3, or 4 here) and give it a role the same way: setMarginTypeN() with
# Scintilla.MarginType.Text/RText for application-drawn text (see
# marginSetText()), or another Symbol margin with its own setMarginMaskN()
# (e.g. Scintilla.MaskHistory instead of MaskFolders) so its markers don't
# collide with the fold margin's.
MARGIN_LINE_NUMBER: Final = 0
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


@dataclass(frozen=True)
class StyleSpec:
    """Visuals for one named style; color is an (red, green, blue) triple."""

    color: tuple[int, int, int]
    bold: bool = False
    italic: bool = False


# Visuals per style, keyed by the cpp lexer's own symbolic style names (e.g.
# "SCE_C_DEFAULT"). Neither the SCE_C_* numbers nor their names are bound as
# constants by lexilla-py -- each lexer defines its own style set, and
# binding all of them is out of lexilla-py's scope (see its
# docs/specs/mission.md) -- so a plain string is the only handle available;
# there is no enum member to import instead. Resolved to the cpp lexer's
# actual style numbers at runtime in __setup_editor() via
# Lexer.named_styles()/name_of_style(), and checked there against typos
# since nothing else (type checker, linter) can catch a bad key here. To see
# the full list of names/descriptions a lexer exposes, run e.g.:
#   from lexilla import Language, create_lexer
#   lexer = create_lexer(Language.CPP)
#   for s in range(lexer.named_styles()):
#       print(s, lexer.name_of_style(s), lexer.description_of_style(s))
#
# The (red, green, blue) colors below are this example's own palette choice
# -- not Lexilla or Scintilla values -- packed to Scintilla's 0xBBGGRR
# format by rgb() below, at the point of use.
STYLES_BY_NAME: Final = {
    "SCE_C_DEFAULT": StyleSpec((0x00, 0x00, 0x00)),
    "SCE_C_COMMENT": StyleSpec((0x80, 0x80, 0x80), italic=True),
    "SCE_C_COMMENTLINE": StyleSpec((0x80, 0x80, 0x80), italic=True),
    "SCE_C_COMMENTDOC": StyleSpec((0x80, 0x80, 0x80), italic=True),
    "SCE_C_NUMBER": StyleSpec((0x80, 0x00, 0x80)),
    "SCE_C_WORD": StyleSpec((0x00, 0x00, 0x80), bold=True),
    "SCE_C_STRING": StyleSpec((0x00, 0x80, 0x00)),
    "SCE_C_PREPROCESSOR": StyleSpec((0x80, 0x40, 0x00)),
    "SCE_C_OPERATOR": StyleSpec((0x40, 0x40, 0x40)),
    "SCE_C_IDENTIFIER": StyleSpec((0x00, 0x00, 0x00)),
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
// lexilla-py: cpp lexer wired into pyside6-scintilla via set_lexer()
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

        # create_lexer() returns a Lexer that owns the underlying ILexer5
        # until detach() (called by set_lexer() below) hands it to
        # Scintilla -- after that, the editor (not lexer) owns its
        # lifetime, and Lexer.pointer/other methods must not be used
        # again. Resolve style names to numbers, and set "fold" (which
        # controls whether Fold() computes fold levels at all), before
        # that handoff.
        lexer = create_lexer(Language.CPP)
        assert lexer is not None
        style_by_name = {lexer.name_of_style(style): style for style in range(lexer.named_styles())}
        # STYLES_BY_NAME's keys are plain strings (see its comment above for
        # why), so a typo there would otherwise only surface as a KeyError
        # below, off in the styling loop with no hint of the actual cause.
        unknown_names = STYLES_BY_NAME.keys() - style_by_name.keys()
        assert not unknown_names, f"unknown cpp lexer style names: {sorted(unknown_names)}"

        fixed_font = QFontDatabase.systemFont(QFontDatabase.SystemFont.FixedFont)
        for name, spec in STYLES_BY_NAME.items():
            style = style_by_name[name]
            editor.styleSetFont(style, fixed_font.family())
            editor.styleSetFore(style, rgb(*spec.color))
            if spec.bold:
                editor.styleSetBold(style, True)
            if spec.italic:
                editor.styleSetItalic(style, True)

        lexer.property_set("fold", "1")
        set_lexer(editor, lexer)
        editor.setKeyWords(0, CPP_KEYWORDS)

        editor.setText(SAMPLE_TEXT)
        editor.colourise(0, -1)

        editor.setMarginWidthN(MARGIN_LINE_NUMBER, 40)
        editor.setMarginTypeN(MARGIN_LINE_NUMBER, Scintilla.MarginType.Number)

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
