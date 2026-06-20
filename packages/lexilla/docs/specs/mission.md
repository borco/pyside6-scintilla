# Project mission

## Background

[Lexilla](https://www.scintilla.org/Lexilla.html) is the lexer library used
by the [Scintilla](https://www.scintilla.org/) code editor component. Since
Scintilla 5.0, lexers were split out of Scintilla itself into Lexilla — a
separate, Qt-free C++ library that creates `ILexer5` lexer objects by name
(`CreateLexer`) and hands them to a Scintilla editor via `SCI_SETILEXER`.

This project ([lexilla-py](https://github.com/borco/lexilla-py), PyPI package
`lexilla`) is a permissively-licensed Python binding for that library. It is
a sibling to [pyside6-scintilla](https://github.com/borco/pyside6-scintilla)
(same author) — a PySide6 binding for `ScintillaEditBase` — but is
intentionally independent of it: Lexilla has no Qt dependency, and the lexer
objects it creates work with any Scintilla binding, not only a PySide6 one.

## What this is NOT

- Not a Scintilla binding itself — it pairs with one
- Not affiliated with the Scintilla/Lexilla project
- Not a redesign of Lexilla's API — exposes `CreateLexer`/`ILexer5` as-is,
  not a higher-level reimagining of it

## Key decisions

### Binding technology: nanobind

Lexilla's public surface is plain C++ (`CreateLexer`, a handful of free
functions, and the `ILexer5` abstract interface) with no Qt types involved.
[shiboken6](https://doc.qt.io/qtforpython/shiboken6/) — used by
pyside6-scintilla — is built around Qt's object model (parent/child
ownership, signals/slots, `QObject` metatype) and would be substantial
overkill here. [nanobind](https://nanobind.readthedocs.io/) is header-only,
has no Qt/PySide6 toolchain dependency, and is a good fit for binding a small
set of free functions and one abstract interface class.

### Cross-binding integration: raw pointer, with an optional convenience extra

`CreateLexer` returns an `ILexer5*`. The Scintilla side expects that same
pointer value via `SCI_SETILEXER` (an `sptr_t` message parameter). The
default, zero-coupling approach is to expose the lexer's pointer as a plain
Python `int` (`uintptr_t`) — callers pass it to whatever binding's
`send`/message API they're using themselves:

```python
editor.send(SCI_SETILEXER, 0, lexer.pointer)
```

For ergonomics, the optional `lexilla[pyside6-scintilla]` extra adds
convenience glue that knows about pyside6-scintilla's API directly (e.g. a
`lexer.set_on(editor)` helper) — this is the only place the two packages are
allowed to depend on each other.

### Scope: minimal first, full API later

The first usable version covers `CreateLexer(name)`, the core `ILexer5`
methods needed to actually lex and fold (`Lex`, `Fold`, property
get/set, `WordListSet`), and lexer discovery (`GetLexerCount`,
`GetLexerName`). The deprecated `CreateLexerLibrary` path and the full
property/word-list introspection API are deferred — see
[roadmap.md](roadmap.md).

### Naming: `lexilla-py` repo, `lexilla` package, `src/lexilla_vendor/` for vendored source

The GitHub repo is `lexilla-py` rather than `lexilla` so that vendoring
Lexilla's own upstream source never collides with the repo's own checkout
directory name on case-insensitive filesystems (Windows, default macOS).
Within the repo, the same concern applies one level down: pyside6-scintilla
vendors Scintilla under `src/scintilla/`, sitting next to the binding
package `src/pyside6_scintilla/` — distinct names, no collision. Lexilla's
own package would naturally be `src/lexilla/`, identical to a same-named
vendor directory, so the vendored source instead lives at
`src/lexilla_vendor/`. The PyPI package and Python import name are both
plain `lexilla` — that namespace doesn't have the same collision risk.

### Versioning

Same scheme as pyside6-scintilla: `<Lexilla version>.<binding revision>`
(e.g. Lexilla `5.5.0` → package `5.5.0.0`). The binding revision increments
for releases of this package that don't correspond to a new Lexilla version,
and resets to `0` when Lexilla itself releases a new version.
