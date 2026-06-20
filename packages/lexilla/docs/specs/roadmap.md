# Roadmap

Ordered list of upcoming work. Update this file as items complete or
priorities change. See [mission.md](mission.md) for the decisions behind
these.

1. **Cross-binding example**: add an example wiring a lexer's `.pointer`
   (or `.detach()`'d pointer) into pyside6-scintilla via `SCI_SETILEXER`.
2. **`lexilla[pyside6-scintilla]` extra**: convenience glue (e.g.
   `lexer.set_on(editor)`) once the raw-pointer path above works.
3. **CI**: real build verification (`uv sync` actually compiling against
   vendored Lexilla source) and a fuller test suite beyond the current
   property-get/set/detach smoke tests.
4. **Wheels**: cibuildwheel matrix across all target platforms, publish
   workflow with TestPyPI trusted publishing (mirroring
   pyside6-scintilla's `docs/testpypi.md`).
5. **Docs site**: flesh out `docs/build.md` once there's more to document;
   convert `docs/documenting.md` from a stub once the docs structure is
   decided.
6. **Examples gallery**: a standalone example, plus one using
   pyside6-scintilla once the cross-binding path (item 1) works.
7. **`Lex`/`Fold` investigation**: `ILexer5::Lex`/`Fold` are not yet bound
   (they need an `IDocument*`, which only a real Scintilla editor instance
   provides today -- see [docs/bindings.md](../bindings.md)). Investigate
   whether something like Pygments or tree-sitter could back an `IDocument`
   implementation to give a better standalone lexing/folding experience
   than what the pyside6-scintilla examples currently offer, or whether
   exposing `IDocument` to Python is worth doing at all.
