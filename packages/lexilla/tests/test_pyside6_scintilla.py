from pytestqt.qtbot import QtBot

import lexilla
from lexilla.pyside6_scintilla import set_lexer
from pyside6_scintilla import ScintillaEdit

SCE_C_COMMENTLINE = 2


def test_set_lexer_wires_lexer_into_editor(qtbot: QtBot) -> None:
    """set_lexer() sets the lexer on the editor via SCI_SETILEXER, and it actually lexes."""
    editor = ScintillaEdit()
    qtbot.addWidget(editor)

    lexer = lexilla.create_lexer(lexilla.Language.CPP)
    assert lexer is not None

    set_lexer(editor, lexer)

    editor.setText("// comment\n")
    editor.colourise(0, -1)

    assert editor.styleAt(2) == SCE_C_COMMENTLINE
