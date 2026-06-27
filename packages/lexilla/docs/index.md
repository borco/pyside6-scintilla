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
done and what's next, and the
[project board](https://github.com/users/borco/projects/3) for the joint
roadmap with [pyside6-scintilla](https://github.com/borco/pyside6-scintilla)
(issues and PRs from both repos are added to it automatically).

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
[lexilla_highlighting example](https://github.com/borco/pyside6-scintilla/tree/master/examples/highlighting/lexilla_highlighting/)
for a complete example.

## Why this exists

Lexilla creates the lexer objects (`ILexer5`) that a Scintilla editor widget
attaches via `SCI_SETILEXER` — it's a separate, Qt-free C++ library from
Scintilla itself since Scintilla 5.0. This project exposes that library
directly to Python. In practice,
[pyside6-scintilla](https://github.com/borco/pyside6-scintilla) is its only
consumer, wired up via the `set_lexer()` convenience function (see Usage
above) rather than raw `SCI_SETILEXER` pointer plumbing; it's kept as a
separate package so this binding's release cadence and vendored Lexilla
version can track upstream Lexilla releases independently of
pyside6-scintilla's own release cycle — see
[Project mission](specs/mission.md) for the full background.

## Development

See the **Development** section for the project's mission, how the vendored
Lexilla source is verified against upstream, and (as they fill in) the
bindings architecture and build instructions. See
[GitHub Issues](https://github.com/borco/lexilla-py/issues) for the ordered
list of upcoming work. This repo has no examples of its own — see
[pyside6-scintilla's examples](https://github.com/borco/pyside6-scintilla/tree/master/examples)
instead.
