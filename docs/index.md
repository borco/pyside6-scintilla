# scintilla-py

[![CI](https://github.com/borco/scintilla-py/actions/workflows/ci.yml/badge.svg)](https://github.com/borco/scintilla-py/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/borco/scintilla-py/blob/master/LICENSE)

*Permissively-licensed Python bindings for the [Scintilla](https://www.scintilla.org/)
code editor component and its lexer library, [Lexilla](https://www.scintilla.org/Lexilla.html).*

[View on GitHub](https://github.com/borco/scintilla-py)

## The packages

Two packages, built in one repo and released to PyPI separately:

| Package | PyPI | What it is |
| --- | --- | --- |
| [**pyside6-scintilla**](pyside6-scintilla/index.md) | [![PyPI](https://img.shields.io/pypi/v/pyside6-scintilla)](https://pypi.org/project/pyside6-scintilla/) | The Scintilla editor widget for PySide6 -- a GPL-free alternative to PyQt6-QScintilla. |
| [**lexilla**](lexilla/index.md) | [![PyPI](https://img.shields.io/pypi/v/lexilla)](https://pypi.org/project/lexilla/) | Lexilla's lexers (syntax highlighting and folding for ~125 languages), handed to a pyside6-scintilla editor. |

```bash
pip install pyside6-scintilla lexilla
```

```python
from PySide6.QtWidgets import QApplication
from lexilla import Language, create_lexer
from lexilla.pyside6_scintilla import set_lexer
from pyside6_scintilla import ScintillaEdit

app = QApplication([])
editor = ScintillaEdit()
lexer = create_lexer(Language.CPP)
assert lexer is not None
set_lexer(editor, lexer)
editor.setText("int main() { return 0; }")
editor.show()
app.exec()
```

Each package's page has the details; the [examples gallery](examples/index.md)
has complete apps, and [Reference](reference/index.md) the Python API.

## Why this exists

The usual way to use Scintilla from Python with Qt is QScintilla -- a PyQt6
binding, GPLv3 or commercially licensed. Scintilla and Lexilla themselves are
permissively licensed (HPND). These packages expose them directly to PySide6
users under MIT -- see the [mission](development/mission.md) for the full
background, and [How the packages are built](development/architecture.md) for
why they're two packages with two different binding stacks.

## Status

See [GitHub Issues](https://github.com/borco/scintilla-py/issues) for what's
done and what's next, the
[project board](https://github.com/users/borco/projects/3) for the roadmap,
and the [Changelog](changelog/index.md) for each package's releases.
