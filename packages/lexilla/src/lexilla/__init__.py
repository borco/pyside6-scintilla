"""Python bindings for Lexilla, the lexer library used by Scintilla.

Re-exports the public API of the compiled ``_lexilla`` extension module,
built with nanobind: ``create_lexer``, ``get_lexer_count``,
``get_lexer_name``, and the ``Lexer`` class wrapping ``ILexer5``. Hand a
created lexer's ``.pointer`` (or the value from ``.detach()``) to any
Scintilla binding's ``SCI_SETILEXER`` -- see ``docs/specs/mission.md``.
"""

from ._languages import Language
from ._lexilla import (
    Lexer,
    LanguageIdentifier,
    LineEndType,
    PropertyType,
    create_lexer,
    get_lexer_count,
    get_lexer_name,
)

__version__ = "5.5.0.0"

__all__ = [
    "Language",
    "LanguageIdentifier",
    "Lexer",
    "LineEndType",
    "PropertyType",
    "__version__",
    "create_lexer",
    "get_lexer_count",
    "get_lexer_name",
]
