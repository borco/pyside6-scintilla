<!-- sync:header -->
# lexilla

[![CI](https://github.com/borco/lexilla-py/actions/workflows/ci.yml/badge.svg)](https://github.com/borco/lexilla-py/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/lexilla)](https://pypi.org/project/lexilla/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/borco/lexilla-py/blob/master/LICENSE)
[![Python versions](https://img.shields.io/pypi/pyversions/lexilla)](https://pypi.org/project/lexilla/)

*Permissively-licensed Python bindings for [Lexilla](https://www.scintilla.org/Lexilla.html), the lexer library for Scintilla.*

[View on PyPI](https://pypi.org/project/lexilla/) · [View on GitHub](https://github.com/borco/lexilla-py)
<!-- /sync:header -->

## Status

Early scaffolding — the build toolchain (nanobind + CMake + scikit-build-core)
is wired up end to end, but the real `CreateLexer`/`ILexer5` bindings don't
exist yet. See [Roadmap](specs/roadmap.md) for what's next.

## Why this exists

Lexilla creates the lexer objects (`ILexer5`) that a Scintilla editor widget
attaches via `SCI_SETILEXER` — it's a separate, Qt-free C++ library from
Scintilla itself since Scintilla 5.0. This project exposes that library
directly to Python, so any Scintilla binding (e.g.
[pyside6-scintilla](https://github.com/borco/pyside6-scintilla)) can use it
without re-implementing lexer creation itself — see
[Project mission](specs/mission.md) for the full background.

## Development

See the **Development** section for the project's mission, roadmap, and (as
they fill in) the bindings architecture, build instructions, and how the
vendored Lexilla source will be verified against upstream. See the
**Examples** section for what's planned there.
