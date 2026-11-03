# PyPI

Both packages are published to PyPI separately, each with its own version
(following its vendored upstream release) and its own
[changelog](changelog/index.md):

| Package | Install | PyPI |
| --- | --- | --- |
| pyside6-scintilla | `pip install pyside6-scintilla` | [pypi.org/project/pyside6-scintilla](https://pypi.org/project/pyside6-scintilla/) ![PyPI](https://img.shields.io/pypi/v/pyside6-scintilla) |
| lexilla | `pip install lexilla` | [pypi.org/project/lexilla](https://pypi.org/project/lexilla/) ![PyPI](https://img.shields.io/pypi/v/lexilla) |

pyside6-scintilla pins one PySide6 minor per release, and pip picks the
release matching your PySide6. lexilla has no runtime dependencies (its
`lexilla.pyside6_scintilla` glue uses pyside6-scintilla when it's installed).
