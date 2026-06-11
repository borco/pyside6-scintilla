# pyside6-scintilla

> Permissively-licensed PySide6 bindings for the [Scintilla](https://www.scintilla.org/) code editor component.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Status: pre-alpha / early development.** There is no installable package or
build yet — this README describes the project's goals.

## Why this exists

The standard way to use Scintilla from Python + Qt is
[QScintilla](https://riverbankcomputing.com/software/qscintilla/) (Riverbank Computing),
but it is **GPLv3 or commercially licensed** and targets PyQt6 — not PySide6.

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

See [MISSION.md](MISSION.md) for the full background and design decisions.

## License

- `src/scintilla/` — [HPND License](https://www.scintilla.org/License.txt)
  (Scintilla, copyright Neil Hodgson)
- Everything else — [MIT License](LICENSE)
