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
exist yet. Nothing is published to PyPI yet. See
[docs/specs/roadmap.md](docs/specs/roadmap.md) for what's next.

## Why this exists

Lexilla creates the lexer objects (`ILexer5`) that a Scintilla editor widget
attaches via `SCI_SETILEXER` — it's a separate, Qt-free C++ library from
Scintilla itself since Scintilla 5.0. This project exposes that library
directly to Python, so any Scintilla binding can create and configure lexers,
not just one tied to a specific Qt/GTK/wx binding — see
[docs/specs/mission.md](docs/specs/mission.md) for the full background.

## Goals

`lexilla` aims to be:

- **MIT licensed** — usable in open-source or closed-source projects freely
- A **faithful, low-level binding** of Lexilla's `CreateLexer`/`ILexer5` C++
  API — not a redesign of it
- **Binding-agnostic** — no dependency on any particular Scintilla binding;
  the lexer pointer it creates works with any of them via `SCI_SETILEXER`
- Available as **pre-built wheels** for Linux (x86_64, aarch64), Windows
  (x86_64), and macOS (arm64, x86_64)
- **Not affiliated** with the Scintilla/Lexilla project

## Installation

Not yet published. Once it is:

```bash
pip install lexilla
```

For convenience glue with [pyside6-scintilla](https://github.com/borco/pyside6-scintilla):

```bash
pip install lexilla[pyside6-scintilla]
```

## Versioning

Version numbers follow `<Lexilla version>.<binding revision>` — e.g. `5.5.0.0`
is binding revision `0` for Lexilla `5.5.0`. The binding revision increments
for releases of this package that don't correspond to a new Lexilla version,
and resets to `0` when Lexilla itself releases a new version.

## Documentation

| Doc | Contents |
| --- | --- |
| [docs/specs/](docs/specs/) | Design specifications and action plans for in-progress and planned work |
| [docs/specs/mission.md](docs/specs/mission.md) | Project background, goals, and design decisions |
| [docs/specs/roadmap.md](docs/specs/roadmap.md) | Ordered list of upcoming work |
| [docs/bindings.md](docs/bindings.md) | How the nanobind bindings are built, and how they're expected to grow |
| [docs/build.md](docs/build.md) | Build prerequisites, local build/rebuild, wheels, and publishing |
| [docs/auditing.md](docs/auditing.md) | How to verify the vendored Lexilla source matches upstream |
| [docs/documenting.md](docs/documenting.md) | How the docs site is built (stub) |
| [docs/testpypi.md](docs/testpypi.md) | Setting up TestPyPI trusted publishing |
| [examples/](examples/) | Standalone example apps (planned) |

## License

- `src/lexilla_vendor/` — [HPND License](https://www.scintilla.org/License.txt)
  (Lexilla, copyright Neil Hodgson)
- Everything else — [MIT License](https://github.com/borco/lexilla-py/blob/master/LICENSE)
