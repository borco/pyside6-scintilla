# Roadmap

Ordered list of upcoming work. See [mission.md](mission.md) for the
decisions behind these.

1. **Vendor Lexilla source** under `src/lexilla_vendor/` (release tarball,
   kept byte-identical to upstream — see [docs/auditing.md](../auditing.md)).
2. **Real bindings**: replace the placeholder `_lexilla` extension
   (`src/lexilla/_binding.cpp`) with nanobind bindings for `CreateLexer`,
   `ILexer5` (`Lex`, `Fold`, property get/set, `WordListSet`),
   `GetLexerCount`, `GetLexerName`.
3. **Cross-binding example**: expose the created lexer's pointer as an
   `int`; add an example wiring a lexer into pyside6-scintilla via
   `SCI_SETILEXER`.
4. **`lexilla[pyside6-scintilla]` extra**: convenience glue (e.g.
   `lexer.set_on(editor)`) once the raw-pointer path above works.
5. **CI**: real build verification (`uv sync` actually compiling against
   vendored Lexilla source) and a real test suite beyond the import smoke
   test.
6. **Wheels**: cibuildwheel matrix across all target platforms, publish
   workflow with TestPyPI trusted publishing (mirroring
   pyside6-scintilla's `docs/testpypi.md`).
7. **Docs site**: flesh out `docs/bindings.md`, `docs/build.md`,
   `docs/auditing.md` once there's something real to document; convert
   `docs/documenting.md` from a stub once the docs structure is decided.
8. **Examples gallery**: a standalone example, plus one using
   pyside6-scintilla once the cross-binding path (item 3) works.
