<!-- sync:header -->
# pyside6-scintilla

[![CI](https://github.com/borco/pyside6-scintilla/actions/workflows/ci.yml/badge.svg)](https://github.com/borco/pyside6-scintilla/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/pyside6-scintilla)](https://pypi.org/project/pyside6-scintilla/)
[![Downloads](https://static.pepy.tech/badge/pyside6-scintilla)](https://pepy.tech/project/pyside6-scintilla)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/borco/pyside6-scintilla/blob/master/LICENSE)
[![Python versions](https://img.shields.io/pypi/pyversions/pyside6-scintilla)](https://pypi.org/project/pyside6-scintilla/)

*Permissively-licensed PySide6 bindings for the [Scintilla](https://www.scintilla.org/) code editor component.*

[View on PyPI](https://pypi.org/project/pyside6-scintilla/) · [View on GitHub](https://github.com/borco/pyside6-scintilla)
<!-- /sync:header -->

## Status

The `ScintillaEditBase` and `ScintillaEdit` bindings are implemented and
working — see the [examples gallery](examples/index.md) for runnable demos.
Pre-built wheels are published on
[PyPI](https://pypi.org/project/pyside6-scintilla/) for Linux (x86_64),
Windows (x86_64), and macOS (arm64, x86_64), Python 3.11-3.14.

## Installation

<!-- sync:installation -->
Install from [PyPI](https://pypi.org/project/pyside6-scintilla/):

```bash
pip install pyside6-scintilla
```

PySide6 6.10+ is installed automatically as a dependency; the wheels bundle
everything else `ScintillaEditBase` needs at runtime.
<!-- /sync:installation -->

## Usage

<!-- sync:usage-example -->
```python
from PySide6.QtWidgets import QApplication
from pyside6_scintilla import ScintillaEdit

app = QApplication([])
editor = ScintillaEdit()
editor.setText("hello, world")
editor.show()
app.exec()
```
<!-- /sync:usage-example -->

`ScintillaEdit` exposes a typed method per Scintilla message (e.g.
`setText()`, `textLength()`, `gotoLine()`) on top of `ScintillaEditBase`'s
raw `.send()`/`.sends()` message API — the same `SCI_*` messages as the C
interface, not a QScintilla-style high-level API. See the
[examples gallery](examples/index.md) for complete examples of both.

## Why this exists

The standard way to use Scintilla from Python + Qt is
[QScintilla](https://riverbankcomputing.com/software/qscintilla/) — but it's
a PyQt6 binding with no PySide6 equivalent, and it's GPLv3 or commercially
licensed. Scintilla itself is licensed under the permissive
[HPND license](https://www.scintilla.org/License.txt). This project exposes
that permissive core directly to PySide6 users — see
[Project mission](specs/mission.md) for the full background.

## Development

See the **Development** section for how the bindings are built, how to set
up a local build, and how the vendored Scintilla source is verified against
upstream.
