<!-- sync:header -->
# lexilla: Python bindings for Lexilla

[![CI](https://github.com/borco/scintilla-py/actions/workflows/ci.yml/badge.svg)](https://github.com/borco/scintilla-py/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/lexilla)](https://pypi.org/project/lexilla/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/borco/scintilla-py/blob/master/packages/lexilla/LICENSE)
[![Python versions](https://img.shields.io/pypi/pyversions/lexilla)](https://pypi.org/project/lexilla/)

*Permissively-licensed Python bindings for [Lexilla](https://www.scintilla.org/Lexilla.html), the lexer library for Scintilla.*

[View on PyPI](https://pypi.org/project/lexilla/) · [View on GitHub](https://github.com/borco/scintilla-py/tree/master/packages/lexilla)
<!-- /sync:header -->

## Status

See [GitHub Issues](https://github.com/borco/scintilla-py/issues) for what's
done and what's next.

## Why this exists

Lexilla creates the lexer objects (`ILexer5`) that a Scintilla editor widget
attaches via `SCI_SETILEXER` — it's a separate, Qt-free C++ library from
Scintilla itself since Scintilla 5.0. This project exposes that library
directly to Python. In practice,
[pyside6-scintilla](https://github.com/borco/scintilla-py) is its only
consumer, wired up via the `set_lexer()` convenience function (see Usage
below) rather than raw `SCI_SETILEXER` pointer plumbing; it's kept as a
separate package so this binding's release cadence and vendored Lexilla
version can track upstream Lexilla releases independently of
pyside6-scintilla's own release cycle — see
[docs/lexilla/design-decisions.md](docs/lexilla/design-decisions.md) for the full background.

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
[lexilla_highlighting](https://github.com/borco/scintilla-py/tree/master/examples/highlighting/lexilla_highlighting/)
for a complete example.

## Versioning

Version numbers follow `<Lexilla version>.<binding revision>` — e.g. `5.5.0.0`
is binding revision `0` for Lexilla `5.5.0`. The binding revision increments
for releases of this package that don't correspond to a new Lexilla version,
and resets to `0` when Lexilla itself releases a new version.

## Documentation

Full docs: <https://borco.github.io/scintilla-py/lexilla/>. lexilla lives in
the [scintilla-py](https://github.com/borco/scintilla-py) repo, next to pyside6-scintilla, under
[`packages/lexilla/`](https://github.com/borco/scintilla-py/tree/master/packages/lexilla).

| Doc | Contents |
| --- | --- |
| [docs/lexilla/auditing.md](https://github.com/borco/scintilla-py/blob/master/docs/lexilla/auditing.md) | How to verify the vendored Lexilla source matches upstream |
| [docs/lexilla/bindings.md](https://github.com/borco/scintilla-py/blob/master/docs/lexilla/bindings.md) | How the nanobind bindings are built, and how they're expected to grow |
| [docs/lexilla/build.md](https://github.com/borco/scintilla-py/blob/master/docs/lexilla/build.md) | lexilla-specific build notes (no Qt SDK, wheels, generated files) |
| [docs/development/build.md](https://github.com/borco/scintilla-py/blob/master/docs/development/build.md) | Building the workspace, CI, wheels, and publishing |
| [docs/lexilla/design-decisions.md](https://github.com/borco/scintilla-py/blob/master/docs/lexilla/design-decisions.md) | Project background, goals, and design decisions |
| [examples/](https://github.com/borco/scintilla-py/tree/master/examples) | Example apps, including [lexilla_highlighting](https://github.com/borco/scintilla-py/tree/master/examples/highlighting/lexilla_highlighting) |
| [GitHub Issues](https://github.com/borco/scintilla-py/issues) | Planned and in-progress work |
| [Project board](https://github.com/users/borco/projects/3) | Roadmap |

## License

- `src/lexilla_vendor/` — [HPND License](https://www.scintilla.org/License.txt)
  (Lexilla, copyright Neil Hodgson)
- Everything else — [MIT License](https://github.com/borco/scintilla-py/blob/master/packages/lexilla/LICENSE)
