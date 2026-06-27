# Changelog

All notable changes to this project are documented in this file, one entry
per release. Format loosely follows [Keep a
Changelog](https://keepachangelog.com/en/1.0.0/); entries are kept high-level
(what shipped, breaking changes) rather than a full commit-by-commit log —
see git history for that.

## [5.6.3.4] - 2026-06-27

### Added

- All 74 Scintilla enum classes now bound (previously 11), each with
  class- and member-level docstrings sourced from `ScintillaDoc.html`, for
  IDE hover docs.
- New example: `lexilla_highlighting`, using lexilla-py's `set_lexer()`
  glue and runtime style-name resolution (`Lexer.named_styles()`/
  `name_of_style()`).

No breaking changes.

## [5.6.3.3] - 2026-06-19

### Fixed

- `modified`-style signals carrying `Scintilla::Position`/enum-typed
  parameters (e.g. `modified`) never reached connected Python slots on
  `ScintillaEditBase`/`ScintillaEdit`.
- `Unknown` types in the generated `.pyi` stub for `ScintillaEdit.get_doc()`,
  `setText()`, `getText()`, etc., caused by an unresolvable self-import in
  the stub generator.

### Added

- pyright added to CI to catch typing regressions.
- Typed `Scintilla.<Name>` namespace constants (`InvalidPosition`, `CpUtf8`,
  `MarkerMax`, etc.) with docstrings.
- New examples: `bscintillaedit`, `pygments_highlighting`,
  `tree_sitter_highlighting`.

No breaking changes.

## [5.6.3.2] - 2026-06-14

### Added

- `ScintillaEdit`, a typed per-message wrapper over `ScintillaEditBase`
  (~780 methods generated from `Scintilla.iface`).
- `ScintillaDocument`, wrapping Scintilla's shared/refcounted document
  buffer for multi-view editing.
- New example: `examples/simple_scintilla_edit/`.
- Full `.pyi` stub docstrings for `ScintillaEdit`, `ScintillaDocument`, and
  `ScintillaEditBase`.

No breaking changes to `ScintillaEditBase`'s existing API.

## [5.6.3.1] - 2026-06-13

Docs-only release: corrects the PyPI README to reflect that pre-built
wheels are published.

## [5.6.3.0] - 2026-06-13

First published release: `ScintillaEditBase` binding with pre-built wheels
for Linux (x86_64), Windows (x86_64), and macOS (arm64, x86_64), Python
3.11-3.14.
