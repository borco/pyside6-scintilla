# CLAUDE.md

This file grounds Claude sessions working on this repository.
Read `MISSION.md` for full background. Key facts:

## What this is

A permissively-licensed (MIT) PySide6 binding for the Scintilla code editor
component. Built with shiboken6 + CMake + scikit-build-core. The main motivation
is providing a GPL-free alternative to PyQt6-QScintilla.

## What this is NOT

- Not a port of QScintilla's high-level API
- Not affiliated with Riverbank Computing or the QScintilla project
- Not trying to upstream into Scintilla itself

## Stack

- **Language**: C++ (binding glue) + Python (package/API)
- **Binding generator**: shiboken6
- **Build system**: CMake + scikit-build-core
- **Package manager**: uv
- **CI**: GitHub Actions + cibuildwheel
- **Scintilla**: vendored release tarball (not a live hg clone)

## Dev machines

- Windows 11 + WSL (Debian/Ubuntu) — primary
- macOS M1 Mac Mini — secondary

## Platforms targeted

Linux x86_64/aarch64, Windows x86_64, macOS arm64 + x86_64

## Conventions

- Python package name on PyPI: `pyside6-scintilla`
- Import name: `pyside6_scintilla` (underscore, as per PEP 8)
- Versioning: follow Scintilla's version (e.g. Scintilla 5.5.x → this package 5.5.x.N)
- All new code under MIT license; Scintilla vendored code retains HPND license

## Where to find things

- `src/scintilla/` — vendored Scintilla source
- `src/pyside6_scintilla/` — shiboken6 typesystem XML and binding glue
- `src/pyside6_scintilla/__init__.py` — public Python API surface
- `.github/workflows/` — CI (build + publish)
- `MISSION.md` — full project background and decision log
