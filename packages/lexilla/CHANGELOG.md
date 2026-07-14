# Changelog

All notable changes to this project will be documented in this file, one
entry per release. Format loosely follows [Keep a
Changelog](https://keepachangelog.com/en/1.0.0/); entries are kept
high-level (what shipped, breaking changes) rather than a full
commit-by-commit log — see git history for that.

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
