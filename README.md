# scintilla-py

[![CI](https://github.com/borco/scintilla-py/actions/workflows/ci.yml/badge.svg)](https://github.com/borco/scintilla-py/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Permissively-licensed (MIT) Python bindings for
[Scintilla](https://www.scintilla.org/), the code editor component, and
[Lexilla](https://www.scintilla.org/Lexilla.html), its lexer library. Two
packages, each released to PyPI on its own:

| Package | PyPI | What it is |
| --- | --- | --- |
| [`pyside6-scintilla`](packages/pyside6-scintilla/) | [![PyPI](https://img.shields.io/pypi/v/pyside6-scintilla)](https://pypi.org/project/pyside6-scintilla/) | PySide6 bindings for the Scintilla editor widget -- a GPL-free alternative to PyQt6-QScintilla |
| [`lexilla`](packages/lexilla/) | [![PyPI](https://img.shields.io/pypi/v/lexilla)](https://pypi.org/project/lexilla/) | Bindings for Lexilla (syntax highlighting for ~125 languages), usable with `pyside6-scintilla` |

```bash
pip install pyside6-scintilla lexilla
```

Documentation: <https://borco.github.io/scintilla-py/>. Each package's README
(also its PyPI page) has the details and a usage example.

## Repository layout

```text
packages/pyside6-scintilla/   the pyside6-scintilla package (vendored Scintilla, shiboken6 bindings)
packages/lexilla/             the lexilla package (vendored Lexilla, nanobind bindings)
examples/                     example apps for both packages
docs/                         the documentation site (mkdocs)
tools/                        repo-level development scripts
```

## Development

The repo is a [uv workspace](https://docs.astral.sh/uv/concepts/projects/workspaces/):
`uv sync` at the root builds both packages from source into one `.venv`
(this needs a Qt 6.11 SDK, for pyside6-scintilla), and the top-level
`Makefile` runs the usual tasks for both:

```bash
make sync   # uv sync
make test   # both packages' tests
make lint   # ruff, docs/header/generator sync checks, pyright
```

See [docs/build.md](docs/build.md) for prerequisites, CI, wheels and the
release process, and the [project board](https://github.com/users/borco/projects/3)
and [issues](https://github.com/borco/scintilla-py/issues) for the roadmap.

## License

MIT for this repo's own code (see [LICENSE](LICENSE)); the vendored Scintilla
and Lexilla sources keep their [HPND license](https://www.scintilla.org/License.txt).
