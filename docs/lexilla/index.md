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
done and what's next, the
[project board](https://github.com/users/borco/projects/3) for the roadmap,
and the [changelog](../changelog/lexilla.md) for releases. lexilla lives in
the [scintilla-py](../index.md) repo, next to
[pyside6-scintilla](../pyside6-scintilla/index.md).

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
attaches via `SCI_SETILEXER` -- since Scintilla 5.0 a separate, Qt-free C++
library. This package exposes it directly to Python; in practice its consumer
is [pyside6-scintilla](../pyside6-scintilla/index.md), wired up via
`set_lexer()` (see Usage above). It's a separate package so it can follow
upstream Lexilla releases independently and stay free of Qt -- see the
[mission](../development/mission.md) and the
[design decisions](design-decisions.md).

## More

- [Bindings architecture](bindings.md) -- how the nanobind bindings are built
  and what they expose
- [Build notes](build.md) -- what's specific to building lexilla (the
  workspace build is in [Building and publishing](../development/build.md))
- [Verifying vendored Lexilla](auditing.md) -- checking the vendored source
  against upstream, and the Scintilla interface headers
- [API](../api/lexilla/index.md) and [Reference](../reference/lexilla.md)
- The [lexilla highlighting example](../highlighting/lexilla_highlighting.md)
