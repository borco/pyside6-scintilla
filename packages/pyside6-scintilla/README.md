<!-- sync:header -->
# pyside6-scintilla

[![CI](https://github.com/borco/scintilla-py/actions/workflows/ci.yml/badge.svg)](https://github.com/borco/scintilla-py/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/pyside6-scintilla)](https://pypi.org/project/pyside6-scintilla/)
[![Downloads](https://static.pepy.tech/badge/pyside6-scintilla)](https://pepy.tech/project/pyside6-scintilla)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/borco/scintilla-py/blob/master/LICENSE)
[![Python versions](https://img.shields.io/pypi/pyversions/pyside6-scintilla)](https://pypi.org/project/pyside6-scintilla/)

*Permissively-licensed PySide6 bindings for the [Scintilla](https://www.scintilla.org/) code editor component.*

[View on PyPI](https://pypi.org/project/pyside6-scintilla/) · [View on GitHub](https://github.com/borco/scintilla-py)
<!-- /sync:header -->

## Status

See [GitHub Issues](https://github.com/borco/scintilla-py/issues) for
what's done and what's next.

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

<!-- sync:installation -->
Install from [PyPI](https://pypi.org/project/pyside6-scintilla/):

```bash
pip install pyside6-scintilla
```

`PySide6-Essentials` 6.11.x is installed automatically as a dependency; the
wheels bundle everything else `ScintillaEditBase` needs at runtime. Each
release is built for, and pinned to, one PySide6 minor (its binding libraries
aren't ABI-compatible across minors), so on another PySide6 minor pip picks
the release built for it, or refuses the install, rather than installing a
wheel that fails to import. Essentials
provides the whole `PySide6` import namespace — only `QtCore`, `QtGui` and
`QtWidgets` are used here, so the ~175 MB of `PySide6-Addons` (Qt WebEngine,
Qt3D, QtCharts …) is left out. Install `PySide6` yourself if you want them.
<!-- /sync:installation -->

To build from source instead (e.g. for development), see
[docs/build.md](https://github.com/borco/scintilla-py/blob/master/docs/build.md)
for prerequisites (Qt 6.11 with `Qt6Core5Compat`, a C++17 compiler) and
platform-specific setup.

`examples/highlighting/lexilla_highlighting/` uses
[lexilla](https://pypi.org/project/lexilla/) as a dev dependency, installed
from PyPI like any other package.

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
interface, not a QScintilla-style high-level API. See
[examples/simple_scintilla_edit/](https://github.com/borco/scintilla-py/tree/master/examples/simple_scintilla_edit/)
for a complete example (line-number margin, "Go to Line", block
selection/editing), or
[examples/simple_scintilla_base_edit/](https://github.com/borco/scintilla-py/tree/master/examples/simple_scintilla_base_edit/)
for the lower-level `send`/`sends` API.

## Versioning

Version numbers follow `<Scintilla version>.<binding revision>` — e.g. `5.6.3.0`
is binding revision `0` for Scintilla `5.6.3`. The binding revision increments
for releases of this package that don't correspond to a new Scintilla version
(bug fixes, new API surface, CI changes, etc.), and resets to `0` when Scintilla
itself releases a new version.

## Documentation

Full docs: <https://borco.github.io/scintilla-py/>. pyside6-scintilla lives in
the [scintilla-py](https://github.com/borco/scintilla-py) repo, next to
[lexilla](https://github.com/borco/scintilla-py/tree/master/packages/lexilla), under
[`packages/pyside6-scintilla/`](https://github.com/borco/scintilla-py/tree/master/packages/pyside6-scintilla).

| Doc | Contents |
| --- | --- |
| [docs/alternatives.md](https://github.com/borco/scintilla-py/blob/master/docs/alternatives.md) | How this compares to Monaco-based Qt bindings and other line-numbers + block-edit widgets |
| [docs/auditing.md](https://github.com/borco/scintilla-py/blob/master/docs/auditing.md) | How to verify the vendored Scintilla source matches upstream |
| [docs/bindings.md](https://github.com/borco/scintilla-py/blob/master/docs/bindings.md) | How the shiboken6 bindings are built, generated files, and the Scintilla-update procedure |
| [docs/build.md](https://github.com/borco/scintilla-py/blob/master/docs/build.md) | Build prerequisites, local build/rebuild, wheels, and publishing |
| [docs/documenting.md](https://github.com/borco/scintilla-py/blob/master/docs/documenting.md) | How the docs site is built, and how to add or update a page |
| [docs/specs/](https://github.com/borco/scintilla-py/tree/master/docs/specs/) | Design specifications and action plans for in-progress and planned work |
| [docs/specs/mission.md](https://github.com/borco/scintilla-py/blob/master/docs/specs/mission.md) | Project background, goals, and design decisions |
| [docs/testpypi.md](https://github.com/borco/scintilla-py/blob/master/docs/testpypi.md) | Setting up TestPyPI trusted publishing |
| [examples/](https://github.com/borco/scintilla-py/tree/master/examples) | Standalone example apps, including ones showing [lexilla](https://github.com/borco/scintilla-py/tree/master/packages/lexilla) in use |
| [GitHub Issues](https://github.com/borco/scintilla-py/issues) | Planned and in-progress work |
| [Project board](https://github.com/users/borco/projects/3) | Roadmap |

## Development tools

Development scripts, run with `uv run python <path>` from the repo root (or
via the top-level `Makefile`):

| Script | Purpose |
| --- | --- |
| [generate_scintilla_edit.py](https://github.com/borco/scintilla-py/blob/master/packages/pyside6-scintilla/tools/generate_scintilla_edit.py) | Generates the typed `ScintillaEdit` class from `Scintilla.iface` (`make scintilla-generate`) |
| [generate_pyi.py](https://github.com/borco/scintilla-py/blob/master/packages/pyside6-scintilla/tools/generate_pyi.py) | Regenerates the `.pyi` type stub for `_pyside6_scintilla` (`make scintilla-stubs`) |
| [check_docs_sync.py](https://github.com/borco/scintilla-py/blob/master/tools/check_docs_sync.py) | Verifies shared content blocks stay in sync between each package's README and its docs page |
| [clean_window_corners.py](https://github.com/borco/scintilla-py/blob/master/tools/clean_window_corners.py) | One-off cleanup for Windows window screenshots used in docs |

## License

- `src/scintilla/` — [HPND License](https://www.scintilla.org/License.txt)
  (Scintilla, copyright Neil Hodgson)
- Everything else — [MIT License](https://github.com/borco/scintilla-py/blob/master/LICENSE)
