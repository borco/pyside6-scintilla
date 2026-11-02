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
done and what's next, and the
[project board](https://github.com/users/borco/projects/3) for the roadmap.
lexilla lives in the same repo as [pyside6-scintilla](../index.md), under
`packages/lexilla/`.

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
via `SCI_SETILEXER`, transferring ownership to it — see the
[lexilla_highlighting example](https://github.com/borco/scintilla-py/tree/master/examples/highlighting/lexilla_highlighting/)
for a complete example.

## Why this exists

Lexilla creates the lexer objects (`ILexer5`) that a Scintilla editor widget
attaches via `SCI_SETILEXER` — it's a separate, Qt-free C++ library from
Scintilla itself since Scintilla 5.0. This project exposes that library
directly to Python. In practice,
[pyside6-scintilla](https://github.com/borco/scintilla-py) is its only
consumer, wired up via the `set_lexer()` convenience function (see Usage
above) rather than raw `SCI_SETILEXER` pointer plumbing; it's kept as a
separate package so this binding's release cadence and vendored Lexilla
version can track upstream Lexilla releases independently of
pyside6-scintilla's own release cycle — see
[Project mission](../specs/lexilla-mission.md) for the full background.

## Development

See the pages in this section for the bindings architecture, lexilla-specific
build notes and how the vendored Lexilla source is verified against upstream,
and [Building and publishing](../build.md) for the workspace as a whole. See
[GitHub Issues](https://github.com/borco/scintilla-py/issues) for the ordered
list of upcoming work. For lexilla in use, see the
[lexilla highlighting example](../highlighting/lexilla_highlighting.md).
