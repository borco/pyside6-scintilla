# pyside6-scintilla

[![CI](https://github.com/borco/pyside6-scintilla/actions/workflows/ci.yml/badge.svg)](https://github.com/borco/pyside6-scintilla/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/pyside6-scintilla)](https://pypi.org/project/pyside6-scintilla/)
[![Downloads](https://static.pepy.tech/badge/pyside6-scintilla)](https://pepy.tech/project/pyside6-scintilla)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/borco/pyside6-scintilla/blob/master/LICENSE)
[![Python versions](https://img.shields.io/pypi/pyversions/pyside6-scintilla)](https://pypi.org/project/pyside6-scintilla/)

*Permissively-licensed PySide6 bindings for the [Scintilla](https://www.scintilla.org/) code editor component.*

## Status

The `ScintillaEditBase` binding is implemented and working — see
[examples/simple_scintilla_base_edit/](https://github.com/borco/pyside6-scintilla/tree/master/examples/simple_scintilla_base_edit/)
for a runnable demo. Pre-built wheels are published on PyPI for Linux
(x86_64), Windows (x86_64), and macOS (arm64, x86_64), Python 3.11-3.14 —
see [Installation](#installation). `ScintillaEdit` (Scintilla's full
~700-method API) and Linux aarch64 wheels are planned —
see [docs/mission.md](https://github.com/borco/pyside6-scintilla/blob/master/docs/mission.md) for the roadmap.

## Why this exists

The standard way to use Scintilla from Python + Qt is
[QScintilla](https://riverbankcomputing.com/software/qscintilla/) (Riverbank Computing) —
but it's a PyQt6 binding, with no PySide6 equivalent. Like PyQt6, it's also
**GPLv3 or commercially licensed**.

Scintilla itself is licensed under the
[Historical Permission Notice and Disclaimer](https://www.scintilla.org/License.txt) —
a permissive license with no copyleft. This project aims to expose that permissive
core directly to PySide6 users.

## Goals

`pyside6-scintilla` aims to be:

- **MIT licensed** — usable in open-source or closed-source projects freely
- **PySide6 native** — built with shiboken6, integrating naturally with PySide6 widgets
- A **faithful, low-level binding** of Scintilla's `ScintillaEditBase` widget — not a
  reimplementation of QScintilla's higher-level API
- Available as **pre-built wheels** for Linux (x86_64, aarch64), Windows (x86_64),
  and macOS (arm64, x86_64)
- **Not affiliated** with Riverbank Computing or the QScintilla project

## Installation

```bash
pip install pyside6-scintilla
```

PySide6 6.10+ is installed automatically as a dependency; the wheels bundle
everything else `ScintillaEditBase` needs at runtime.

To build from source instead (e.g. for development), see
[docs/build.md](https://github.com/borco/pyside6-scintilla/blob/master/docs/build.md)
for prerequisites (Qt 6.10+ with `Qt6Core5Compat`, a C++17 compiler) and
platform-specific setup.

## Usage

```python
from PySide6.QtWidgets import QApplication
from pyside6_scintilla import Scintilla, ScintillaEditBase

app = QApplication([])
editor = ScintillaEditBase()
editor.sends(int(Scintilla.Message.SetText), 0, "hello, world")
editor.show()
app.exec()
```

`ScintillaEditBase` exposes Scintilla's low-level message API via `.send()`/
`.sends()` — the same `SCI_*` messages as the C interface, not a
QScintilla-style high-level API. See
[examples/simple_scintilla_base_edit/](https://github.com/borco/pyside6-scintilla/tree/master/examples/simple_scintilla_base_edit/)
for a complete example (line-number margin, block selection/editing).

## Versioning

Version numbers follow `<Scintilla version>.<binding revision>` — e.g. `5.6.3.0`
is binding revision `0` for Scintilla `5.6.3`. The binding revision increments
for releases of this package that don't correspond to a new Scintilla version
(bug fixes, new API surface, CI changes, etc.), and resets to `0` when Scintilla
itself releases a new version.

## Documentation

| Doc | Contents |
| --- | --- |
| [docs/auditing.md](https://github.com/borco/pyside6-scintilla/blob/master/docs/auditing.md) | How to verify the vendored Scintilla source matches upstream |
| [docs/bindings.md](https://github.com/borco/pyside6-scintilla/blob/master/docs/bindings.md) | How the shiboken6 bindings are built, generated files, and the Scintilla-update procedure |
| [docs/build.md](https://github.com/borco/pyside6-scintilla/blob/master/docs/build.md) | Build prerequisites, local build/rebuild, wheels, and publishing |
| [docs/mission.md](https://github.com/borco/pyside6-scintilla/blob/master/docs/mission.md) | Project background, goals, and design decisions |

## License

- `src/scintilla/` — [HPND License](https://www.scintilla.org/License.txt)
  (Scintilla, copyright Neil Hodgson)
- Everything else — [MIT License](https://github.com/borco/pyside6-scintilla/blob/master/LICENSE)
