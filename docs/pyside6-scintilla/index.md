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

See [GitHub Issues](https://github.com/borco/scintilla-py/issues) for what's
done and what's next, the
[project board](https://github.com/users/borco/projects/3) for the roadmap,
and the [changelog](../changelog/pyside6-scintilla.md) for releases.
pyside6-scintilla lives in the [scintilla-py](../index.md) repo, next to
[lexilla](../lexilla/index.md).

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
[examples gallery](../examples/index.md) for complete examples of both.

## Why this exists

The standard way to use Scintilla from Python + Qt is
[QScintilla](https://riverbankcomputing.com/software/qscintilla/) -- but it's
a PyQt6 binding with no PySide6 equivalent, and it's GPLv3 or commercially
licensed. Scintilla itself is licensed under the permissive
[HPND license](https://www.scintilla.org/License.txt). This package exposes
that permissive core directly to PySide6 users -- see the
[mission](../development/mission.md) for the full background, and the
[design decisions](design-decisions.md) for the technical choices.

## More

- [Bindings architecture](bindings.md) -- how the shiboken6 bindings are
  built, the problems solved along the way, and the Scintilla update process
- [Build notes](build.md) -- what's specific to building pyside6-scintilla
  (the workspace build is in [Building and publishing](../development/build.md))
- [Verifying vendored Scintilla](auditing.md) -- checking the vendored source
  against upstream
- [Alternatives](alternatives.md) -- how this compares to other editor widgets
- [API](../api/scintilla/index.md) and [Reference](../reference/scintilla/index.md)
