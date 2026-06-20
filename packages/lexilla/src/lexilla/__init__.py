"""Python bindings for Lexilla, the lexer library used by Scintilla.

Re-exports the public API of the compiled ``_lexilla`` extension module,
built with nanobind. See ``docs/specs/roadmap.md`` for the plan to replace
the current placeholder extension with real ``CreateLexer``/``ILexer5``
bindings.
"""

__version__ = "0.0.0.0"

__all__ = [
    "__version__",
]
