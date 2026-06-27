# pyside6-scintilla — Project Mission & Background

## What is this project?

`pyside6-scintilla` is a permissively-licensed Python binding for the
[Scintilla](https://www.scintilla.org/) source code editing component, targeting
[PySide6](https://pypi.org/project/PySide6/) (the official Qt for Python project).

The bindings are built with **shiboken6** (the same binding generator used by PySide6
itself) and packaged with **scikit-build-core** + **CMake**.

## Why does this exist?

The established option for using Scintilla from Python with Qt is
[QScintilla](https://riverbankcomputing.com/software/qscintilla/) by Riverbank
Computing, with Python bindings via `PyQt6-QScintilla`. However:

- QScintilla is licensed under **GPLv3 or a paid commercial license** — which
  prevents use in closed-source or permissively-licensed projects without purchasing
  a commercial license.
- QScintilla targets **PyQt6**, not PySide6. There are no official PySide6 bindings.

Scintilla itself is licensed under the
[Historical Permission Notice and Disclaimer (HPND)](https://www.scintilla.org/License.txt)
— a permissive license with no copyleft, compatible with MIT, BSD, commercial, and
closed-source use. This project exposes that permissive core directly to PySide6
users, without the GPL encumbrance.

## Prior work by the same author

Two earlier prototype projects explored this space:

- [`bscintillaedit`](https://pypi.org/project/bscintillaedit/) — on PyPI, Windows-only
  wheel, wraps `ScintillaEditBase` inside a `QScrollArea`-derived widget.
- [`pyside6-scintilla`](https://gitlab.com/iborco-pyside/pyside6-scintilla) — on
  GitLab, archived, simpler binding experiment.

`pyside6-scintilla` on PyPI/GitHub is the clean, properly packaged successor to both.

## Licensing

| Component | License |
| --- | --- |
| Scintilla / Lexilla C++ source | HPND (permissive, no copyleft) |
| shiboken6 binding glue code | MIT |
| This project overall | MIT |

The project must **not** depend on or bundle any GPL or LGPL code at runtime in a
way that would require users to open-source their applications.

## Technical approach

- **Scintilla** is vendored as a subtree/submodule pinned to a stable release tag
  (not hg tip). Updates happen deliberately when a new Scintilla release is tested.
- **shiboken6** generates the Python ↔ C++ bridge from a typesystem XML file.
- **scikit-build-core** drives the CMake build and produces PEP 517-compliant wheels.
- **cibuildwheel** on **GitHub Actions** builds wheels for all three platforms
  when a GitHub Release is published, then publishes to PyPI via trusted
  publishing (OIDC) — first to TestPyPI as a tracer, then to the real index.
- **uv** is used for local development environment management.

## Scope

The goal is a **faithful, low-level binding** — exposing the Scintilla API to
PySide6 as a `QWidget`-compatible widget that can be dropped into any PySide6
application. It is **not** a goal to re-implement QScintilla's high-level API
(auto-completion helpers, lexer configuration wrappers, etc.) in this package.
That higher-level layer can be built on top by consumers.

## Target platforms

| Platform | Architecture | Notes |
| --- | --- | --- |
| Linux | x86_64, aarch64 | manylinux wheels via cibuildwheel |
| Windows | x86_64 | MSVC build |
| macOS | arm64 (Apple Silicon) | Primary test machine: M1 Mac Mini |
| macOS | x86_64 (Intel) | Cross-compiled or CI runner |

## Development environment

- **Primary dev machine**: Windows 11 PC with WSL (Debian/Ubuntu)
- **Secondary machine**: macOS M1 Mac Mini
- **Package manager**: `uv`
- **CI**: GitHub Actions (free, unlimited for public repos)
- **Wheel builder**: `cibuildwheel`
- **Source control**: Git on GitHub (Scintilla itself is on SourceForge/Mercurial
  — vendored as a release tarball, see "Scintilla version strategy" below, to
  avoid a hg toolchain dependency)

## Scintilla version strategy

Pin to **release tarballs**, not the hg tip. Check
[scintilla.org](https://www.scintilla.org/ScintillaDownload.html) for the latest
stable release. Updating Scintilla is a deliberate, tested action — not automatic.

## Relationship to Scintilla upstream

This project is a **standalone binding** — there is no intent to upstream it into
Scintilla. Scintilla upstream uses Mercurial on SourceForge and has an informal,
maintainer-driven patch process that is not well-suited to accepting a Python/Qt
binding. Keeping it separate also means it can evolve independently of Scintilla's
release cycle.

## PyPI name

`pyside6-scintilla` — confirmed available at time of project creation (June 2026).

## Key decisions log

| Decision | Rationale |
| --- | --- |
| PySide6, not PyQt6 | PySide6 is LGPL; PyQt6 is GPL — consistent with permissive goals |
| shiboken6, not ctypes/cffi | Native Qt integration, proper signal/slot support |
| GitHub, not GitLab | Unlimited free CI minutes for public repos; GitLab free tier is 400 min/month |
| Standalone project, not Scintilla upstream | Scintilla upstream is C++ only, hg-based, unlikely to accept a Python binding |
| Vendor Scintilla releases, not git-cinnabar bridge | Simpler, more reproducible, no hg toolchain dependency for contributors |
| uv for local dev | Fast, modern, handles venvs and tool installs cleanly |
| cibuildwheel | Industry standard for multi-platform Python native extension wheels |
