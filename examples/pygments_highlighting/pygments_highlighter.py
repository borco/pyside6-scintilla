"""Drives ScintillaEdit styling from a Pygments lexer.

pyside6-scintilla doesn't wrap a lexer binding, so there's no SCI_SETLEXER
to flip on. PygmentsHighlighter instead re-tokenizes the editor's text with
a Pygments lexer on every edit and applies the resulting styles manually via
ScintillaEdit's raw SCI_STYLE* messages (styleSetFore(), startStyling(),
setStyling(), ...). Has no dependencies beyond pyside6-scintilla and
pygments - copy this file straight into your own project.
"""

from typing import Final

from pygments.lexer import Lexer
from pygments.token import Comment, Keyword, Literal, Name, Operator, String, _TokenType
from PySide6.QtCore import QObject
from PySide6.QtGui import QFont

from pyside6_scintilla import ScintillaEdit

# Style numbers below Scintilla.StylesCommon.Default (32) are free for our
# own use.
STYLE_DEFAULT: Final = 0
STYLE_KEYWORD: Final = 1
STYLE_NAME_BUILTIN: Final = 2
STYLE_NAME_FUNCTION: Final = 3
STYLE_NAME_CLASS: Final = 4
STYLE_STRING: Final = 5
STYLE_NUMBER: Final = 6
STYLE_COMMENT: Final = 7
STYLE_OPERATOR: Final = 8

# Most specific token type first: style_for_token() below picks the first
# entry where the tokenizer's token is contained in the listed token (the
# documented way to match Pygments token subtypes, e.g. Keyword.Namespace
# in Keyword).
TOKEN_STYLES: Final = [
    (Name.Builtin, STYLE_NAME_BUILTIN),
    (Name.Function, STYLE_NAME_FUNCTION),
    (Name.Class, STYLE_NAME_CLASS),
    (Keyword, STYLE_KEYWORD),
    (String, STYLE_STRING),
    (Literal.Number, STYLE_NUMBER),
    (Comment, STYLE_COMMENT),
    (Operator, STYLE_OPERATOR),
]


# (red, green, blue) per style -- packed to Scintilla's 0xBBGGRR colour
# format by rgb() below, at the point of use.
STYLE_COLORS: Final = {
    STYLE_DEFAULT: (0x00, 0x00, 0x00),
    STYLE_KEYWORD: (0x00, 0x00, 0x80),
    STYLE_NAME_BUILTIN: (0x40, 0x70, 0x90),
    STYLE_NAME_FUNCTION: (0x00, 0x60, 0x60),
    STYLE_NAME_CLASS: (0x00, 0x60, 0x60),
    STYLE_STRING: (0x00, 0x80, 0x00),
    STYLE_NUMBER: (0x80, 0x00, 0x80),
    STYLE_COMMENT: (0x80, 0x80, 0x80),
    STYLE_OPERATOR: (0x40, 0x40, 0x40),
}


def rgb(red: int, green: int, blue: int) -> int:
    """Pack an 8-bit RGB triple into Scintilla's 0xBBGGRR colour format."""
    return red | (green << 8) | (blue << 16)


def style_for_token(token: _TokenType) -> int:
    """Map a Pygments token type to one of the style numbers above."""
    for candidate, style in TOKEN_STYLES:
        if token in candidate:
            return style
    return STYLE_DEFAULT


class PygmentsHighlighter(QObject):
    """Keeps a ScintillaEdit's styling in sync with a Pygments lexer.

    Pass parent (e.g. the window that owns editor) to tie its lifetime to
    that QObject -- then there's no need for the caller to keep an explicit
    reference around just to stop it from being garbage-collected.

    Re-tokenizes the whole buffer on every edit, which is fine at example/
    small-file scale but wouldn't scale to large files - a production
    version would restyle only the changed region (e.g. from the modified
    signal's position/length) and reuse the lexer's stateful tokenizing
    where the lexer supports it.
    """

    def __init__(
        self, editor: ScintillaEdit, lexer: Lexer, font: QFont | None = None, parent: QObject | None = None
    ) -> None:
        super().__init__(parent)
        self.__editor: Final = editor
        self.__lexer: Final = lexer
        self.__connected = False

        for style, (red, green, blue) in STYLE_COLORS.items():
            if font is not None:
                editor.styleSetFont(style, font.family())
            editor.styleSetFore(style, rgb(red, green, blue))
        editor.styleSetBold(STYLE_KEYWORD, True)
        editor.styleSetItalic(STYLE_COMMENT, True)

        self.rehighlight()
        self.__set_connected(True)

    def rehighlight(self) -> None:
        """Re-tokenize and restyle the editor's full current text."""
        editor = self.__editor
        self.__set_connected(False)
        try:
            text = editor.getText(editor.textLength()).data().decode("utf-8")

            editor.startStyling(0, 0)
            for token, value in self.__lexer.get_tokens(text):
                length = len(value.encode("utf-8"))
                if length:
                    editor.setStyling(length, style_for_token(token))
        finally:
            self.__set_connected(True)

    def __set_connected(self, connected: bool) -> None:
        if connected == self.__connected:
            return
        if connected:
            self.__editor.modified.connect(self.__on_modified)
        else:
            self.__editor.modified.disconnect(self.__on_modified)
        self.__connected = connected

    def __on_modified(self, *_args: object) -> None:
        self.rehighlight()
