<!-- sync:header -->
# lexilla-py: Python bindings for Lexilla

[![CI](https://github.com/borco/lexilla-py/actions/workflows/ci.yml/badge.svg)](https://github.com/borco/lexilla-py/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/lexilla)](https://pypi.org/project/lexilla/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/borco/lexilla-py/blob/master/LICENSE)
[![Python versions](https://img.shields.io/pypi/pyversions/lexilla)](https://pypi.org/project/lexilla/)

*Permissively-licensed Python bindings for [Lexilla](https://www.scintilla.org/Lexilla.html), the lexer library for Scintilla.*

[View on PyPI](https://pypi.org/project/lexilla/) · [View on GitHub](https://github.com/borco/lexilla-py)
<!-- /sync:header -->

## Status

See [GitHub Issues](https://github.com/borco/lexilla-py/issues) for what's
done and what's next.

## Why this exists

Lexilla creates the lexer objects (`ILexer5`) that a Scintilla editor widget
attaches via `SCI_SETILEXER` — it's a separate, Qt-free C++ library from
Scintilla itself since Scintilla 5.0. This project exposes that library
directly to Python. In practice,
[pyside6-scintilla](https://github.com/borco/pyside6-scintilla) is its only
consumer, wired up via the `set_lexer()` convenience function (see Usage
below) rather than raw `SCI_SETILEXER` pointer plumbing; it's kept as a
separate package so this binding's release cadence and vendored Lexilla
version can track upstream Lexilla releases independently of
pyside6-scintilla's own release cycle — see
[docs/specs/mission.md](docs/specs/mission.md) for the full background.

## Goals

`lexilla` aims to be:

- **MIT licensed** — usable in open-source or closed-source projects freely
- A **faithful, low-level binding** of Lexilla's `CreateLexer`/`ILexer5` C++
  API — not a redesign of it
- **Vendored and versioned independently of pyside6-scintilla** — exposes
  the lexer as a raw pointer (`SCI_SETILEXER`-compatible), so this package
  can track upstream Lexilla releases on its own schedule
- Available as **pre-built wheels** for Linux (x86_64, aarch64), Windows
  (x86_64), and macOS (arm64, x86_64)
- **Not affiliated** with the Scintilla/Lexilla project

## Installation

<!-- sync:installation -->
Install from [PyPI](https://pypi.org/project/lexilla/):

```bash
pip install lexilla
```
<!-- /sync:installation -->

## Usage

<!-- sync:usage-example -->
```python
from lexilla import Language, create_lexer
from lexilla.pyside6_scintilla import set_lexer
from pyside6_scintilla import ScintillaEdit

editor = ScintillaEdit()
lexer = create_lexer(Language.CPP)
assert lexer is not None
set_lexer(editor, lexer)
```
<!-- /sync:usage-example -->

`set_lexer()` hands a created lexer to a `pyside6-scintilla` `ScintillaEdit`
via `SCI_SETILEXER`, transferring ownership to it — see
[lexilla_highlighting](https://github.com/borco/pyside6-scintilla/tree/master/examples/highlighting/lexilla_highlighting/)
for a complete example.

## Versioning

Version numbers follow `<Lexilla version>.<binding revision>` — e.g. `5.5.0.0`
is binding revision `0` for Lexilla `5.5.0`. The binding revision increments
for releases of this package that don't correspond to a new Lexilla version,
and resets to `0` when Lexilla itself releases a new version.

## Documentation

| Doc | Contents |
| --- | --- |
| [docs/auditing.md](docs/auditing.md) | How to verify the vendored Lexilla source matches upstream |
| [docs/bindings.md](docs/bindings.md) | How the nanobind bindings are built, and how they're expected to grow |
| [docs/build.md](docs/build.md) | Build prerequisites, local build/rebuild, wheels, and publishing |
| [docs/documenting.md](docs/documenting.md) | How the docs site is built (stub) |
| [docs/specs/](docs/specs/) | Design specifications and action plans for in-progress and planned work |
| [docs/specs/mission.md](docs/specs/mission.md) | Project background, goals, and design decisions |
| [docs/testpypi.md](docs/testpypi.md) | Setting up TestPyPI trusted publishing |
| [examples/](examples/) | No examples of its own — see [pyside6-scintilla/examples/](https://github.com/borco/pyside6-scintilla/tree/master/examples) |
| [GitHub Issues](https://github.com/borco/lexilla-py/issues) | Ordered list of upcoming work |
| [Project board](https://github.com/users/borco/projects/3) | Joint roadmap for `lexilla-py` and [pyside6-scintilla](https://github.com/borco/pyside6-scintilla); issues/PRs from both repos are auto-added |

## License

- `src/lexilla_vendor/` — [HPND License](https://www.scintilla.org/License.txt)
  (Lexilla, copyright Neil Hodgson)
- Everything else — [MIT License](https://github.com/borco/lexilla-py/blob/master/LICENSE)
