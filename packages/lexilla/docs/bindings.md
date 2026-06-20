# The nanobind bindings

How `_lexilla` is built today, and how it's expected to grow once real
Lexilla bindings replace the current placeholder.

## How it fits together (current, placeholder state)

- `src/lexilla_vendor/` -- vendored Lexilla release source (see
  [docs/auditing.md](auditing.md) for how it's verified against upstream).
- `src/lexilla/bindings/_binding.cpp` -- nanobind module source. Currently a
  single placeholder function (`smoke_test`), proving the toolchain (CMake +
  scikit-build-core + nanobind) builds, installs, and loads end to end.
- `src/lexilla/bindings/CMakeLists.txt` -- compiles `_binding.cpp` into
  `_lexilla.{pyd,so,dylib}` via `nanobind_add_module`, `add_subdirectory`'d
  from the top-level `CMakeLists.txt`.
- `src/lexilla/__init__.py` -- re-exports the compiled extension's public
  API as the `lexilla` package.

## Planned, once real bindings are built

See [docs/specs/mission.md](specs/mission.md) for the reasoning behind
these:

- A CMake target (e.g. `lexilla_core`) building the vendored Lexilla C++
  sources (`Lexilla.cxx`, the individual lexer `.cxx` files) as a static or
  shared library, analogous to pyside6-scintilla's `src/scintilla_qt/`.
  `src/lexilla/bindings/CMakeLists.txt` would link `_lexilla` against it.
- `_lexilla` bindings for `CreateLexer`, `GetLexerCount`, `GetLexerName`,
  and the core `ILexer5` methods (`Lex`, `Fold`, property get/set,
  `WordListSet`) -- the minimal scope decided for the first usable version.
- The created lexer's raw pointer exposed as a plain Python `int`, so it can
  be handed to any Scintilla binding's `SCI_SETILEXER` -- and an optional
  `lexilla[pyside6-scintilla]` extra with convenience glue on top of that.

## Type stubs (`_lexilla.pyi`)

Generated with `make stubs` (`python -m nanobind.stubgen`), checked into
git for IDE/type-checker support -- same rationale as pyside6-scintilla's
[`_pyside6_scintilla.pyi`](https://github.com/borco/pyside6-scintilla/blob/master/docs/bindings.md#type-stubs-_pyside6_scintillapyi).
Excluded from `ruff` formatting (`extend-exclude` in `pyproject.toml`) since
it's machine-generated, not hand-edited.

Regenerate it after rebuilding the extension (`make install` or
`uv sync --reinstall-package lexilla`), and whenever `_binding.cpp` changes
the public API surface.
