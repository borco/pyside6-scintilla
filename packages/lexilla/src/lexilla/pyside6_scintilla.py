"""Convenience glue for handing a Lexilla lexer to pyside6-scintilla.

Requires pyside6-scintilla to be installed -- importing this module pulls it
in directly. The core ``lexilla`` package has no such dependency; this is the
only place the two packages are allowed to depend on each other (see
``docs/specs/mission.md``'s "Cross-binding integration" decision).
"""

from pyside6_scintilla import ScintillaEdit

from ._lexilla import Lexer

__all__ = ["set_lexer"]


def set_lexer(editor: ScintillaEdit, lexer: Lexer) -> None:
    """Set `lexer` on `editor`, transferring ownership to it.

    :param editor: The widget to lex.
    :param lexer: The lexer to set; detached, so it must not be used afterwards.

    Example
    -------

    .. code:: python

        from lexilla import Language, create_lexer
        from lexilla.pyside6_scintilla import set_lexer
        from pyside6_scintilla import ScintillaEdit

        editor = ScintillaEdit()
        lexer = create_lexer(Language.CPP)
        assert lexer is not None
        set_lexer(editor, lexer)
    """
    editor.setILexer(lexer.detach())
