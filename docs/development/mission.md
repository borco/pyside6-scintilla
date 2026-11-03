# Mission

## What this is

`scintilla-py` provides permissively-licensed (MIT) Python bindings for the
[Scintilla](https://www.scintilla.org/) source code editing component and its
lexer library, [Lexilla](https://www.scintilla.org/Lexilla.html), as two
packages:

- **pyside6-scintilla** -- the Scintilla editor widget for
  [PySide6](https://pypi.org/project/PySide6/) (the official Qt for Python
  project), as a `QWidget` that drops into any PySide6 application.
- **lexilla** -- Lexilla's lexers: the `ILexer5` objects that give a Scintilla
  editor syntax highlighting and folding for ~125 languages.

## Why it exists

The established option for using Scintilla from Python with Qt is
[QScintilla](https://riverbankcomputing.com/software/qscintilla/) by Riverbank
Computing, with Python bindings via `PyQt6-QScintilla`. However:

- QScintilla is licensed under **GPLv3 or a paid commercial license**, which
  prevents use in closed-source or permissively-licensed projects without
  buying a commercial license.
- QScintilla targets **PyQt6**, not PySide6; there are no official PySide6
  bindings.

Scintilla and Lexilla themselves are licensed under the
[Historical Permission Notice and Disclaimer (HPND)](https://www.scintilla.org/License.txt)
-- permissive, no copyleft, compatible with MIT, BSD, commercial and
closed-source use. This project exposes that permissive core directly to
PySide6 users, without the GPL encumbrance.

## Why two packages

Since Scintilla 5.0, lexers live in a separate library, Lexilla: a Qt-free C++
library that creates `ILexer5` objects by name (`CreateLexer`), which a
Scintilla editor then uses via `SCI_SETILEXER`. The packages follow that
split:

- **Separate release cadences.** Each package's version follows its vendored
  upstream (Scintilla 5.6.3 → pyside6-scintilla 5.6.3.N, Lexilla 5.5.0 →
  lexilla 5.5.0.N), and Scintilla and Lexilla release independently.
- **No Qt in lexilla.** Lexilla has no Qt dependency, so its binding needs
  none either -- a much smaller, simpler package (see
  [How the packages are built](architecture.md)).
- **Optional.** An editor that doesn't need Lexilla's lexers (e.g. one styled
  with Pygments or tree-sitter instead, as in the examples) doesn't install
  them.

In practice pyside6-scintilla is lexilla's only consumer -- nothing else
implements `ILexer5`, and Python code wanting syntax highlighting without a
Scintilla editor has better-fitting tools. The two packages connect through
the lexer's raw `ILexer5*` pointer (zero coupling), plus an optional
`lexilla.pyside6_scintilla.set_lexer()` convenience.

## Why one repo

The packages were developed as two repos (`pyside6-scintilla` and
`lexilla-py`) and merged into this monorepo (issue #19): they're maintained
together, occasionally, and lexilla doesn't make sense on its own. One repo
means one CI, one docs site, one dev environment in which lexilla is always
tested against the pyside6-scintilla it ships with, and Scintilla interface
headers that can't drift apart -- while each package still releases on its
own.

## Scope

The goal is **faithful, low-level bindings**:

- pyside6-scintilla exposes the Scintilla API -- one typed method per Scintilla
  message, text as `str`, colours as `QColor` -- not a re-implementation of
  QScintilla's high-level API (auto-completion helpers, lexer configuration
  wrappers, etc.). That higher-level layer can be built on top by consumers.
- lexilla exposes `CreateLexer`/`ILexer5` as-is, not a redesign of Lexilla's
  API.

## What this is NOT

- Not a port of QScintilla's high-level API.
- Not affiliated with Riverbank Computing, the QScintilla project, or the
  Scintilla/Lexilla project.
- Not trying to upstream into Scintilla or Lexilla: upstream uses Mercurial
  on SourceForge with an informal, maintainer-driven patch process not suited
  to Python/Qt bindings, and staying separate lets these packages evolve on
  their own schedule.

## Licensing

| Component | License |
| --- | --- |
| Scintilla / Lexilla C++ source (vendored) | HPND (permissive, no copyleft) |
| This repo's own code (binding glue, Python packages) | MIT |

The packages must **not** depend on or bundle any GPL or LGPL code at runtime
in a way that would require users to open-source their applications.
(PySide6 itself is LGPL, used as a separately installed dependency.)

## Upstream sources

Both upstreams are vendored from **release tarballs**, not the Mercurial tip
(no hg toolchain needed). Updating either is a deliberate, tested action --
not automatic. See [Verifying vendored Scintilla](../pyside6-scintilla/auditing.md)
and [Verifying vendored Lexilla](../lexilla/auditing.md).

## Target platforms

| Platform | Architecture | Notes |
| --- | --- | --- |
| Linux | x86_64, aarch64 | manylinux wheels via cibuildwheel |
| Windows | x86_64 | MSVC build |
| macOS | arm64 (Apple Silicon) | Primary test machine: M1 Mac Mini |
| macOS | x86_64 (Intel) | Cross-built on Apple Silicon CI runners |

## Development environment

- **Primary dev machine**: Windows 11 PC with WSL (Debian/Ubuntu)
- **Secondary machine**: macOS M1 Mac Mini
- **Package manager**: `uv` (a workspace with both packages)
- **CI**: GitHub Actions; wheels via `cibuildwheel`; PyPI trusted publishing
  (TestPyPI first)

## Prior work by the same author

- [`bscintillaedit`](https://pypi.org/project/bscintillaedit/) -- on PyPI,
  Windows-only wheel, wraps `ScintillaEditBase` inside a `QScrollArea`-derived
  widget.
- [`pyside6-scintilla`](https://gitlab.com/iborco-pyside/pyside6-scintilla) --
  on GitLab, archived, a simpler binding experiment.

This project is the clean, properly packaged successor to both.

## Design decisions

Each package keeps its own decision log:
[pyside6-scintilla](../pyside6-scintilla/design-decisions.md) and
[lexilla](../lexilla/design-decisions.md).
