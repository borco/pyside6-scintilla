# Changelog

All notable changes to this project will be documented in this file, one
entry per release. Format loosely follows [Keep a
Changelog](https://keepachangelog.com/en/1.0.0/); entries are kept
high-level (what shipped, breaking changes) rather than a full
commit-by-commit log — see git history for that.

## [Unreleased]

### Changed (breaking)

- Requires Python 3.12 or later, with a single `cp312-abi3` wheel per
  platform (forward-compatible with later Pythons). The separate `cp311`
  wheels are gone: nanobind's stable ABI needs 3.12, and a version-specific
  3.11 build doubled the wheel count for one Python version. lexilla 5.5.0.1
  remains available for Python 3.11.

### Changed

- The project moved from `lexilla-py` into the
  [scintilla-py](https://github.com/borco/scintilla-py) monorepo, next to
  pyside6-scintilla (as `packages/lexilla/`). Docs:
  <https://borco.github.io/scintilla-py/lexilla/>.
- Built against the Scintilla 5.6.3 interface headers (the Scintilla release
  pyside6-scintilla vendors), up from 5.5.0. `ILexer5` and the fold-level
  constants are unchanged.
- The wheel tests run against the pyside6-scintilla built from the same
  commit, not the PyPI release.

## [5.5.0.1] - 2026-07-14

### Changed

- CI: re-enabled `aarch64` testing now that pyside6-scintilla ships an
  aarch64 wheel (#10).
- Wheel builds: a version-specific `cp311` wheel plus a `cp312-abi3` wheel
  (forward-compatible with 3.13, 3.14, and beyond without a rebuild) per
  platform, instead of one wheel per Python version -- 10 wheels per
  release instead of 20.

No breaking changes.

## [5.5.0.0] - 2026-06-27

First published release: `CreateLexer`/`ILexer5` binding (the `Lexer` class,
plus named/sub-style and `ILexer4` introspection) with pre-built wheels for
Linux (x86_64, aarch64), Windows (x86_64), and macOS (arm64, x86_64), Python
3.11-3.14.
