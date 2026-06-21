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

The first usable version covers `CreateLexer(name)`, lexer discovery
(`GetLexerCount`, `GetLexerName`), and the core `ILexer4`/`ILexer5` property
and word-list methods (`PropertyGet`/`PropertySet`, `WordListSet`, and the
introspection methods used to back them). `Lex` and `Fold` are deferred:
both take an `IDocument*`, which only a Scintilla editor instance provides in
normal use (Scintilla calls them itself once a lexer is wired up via
`SCI_SETILEXER`) — binding them as Python-callable would mean also binding
`IDocument` as a trampoline class Python code can implement, a much bigger
surface for unclear benefit. A follow-up should investigate whether
something like Pygments or tree-sitter could back an `IDocument`
implementation usefully, or whether exposing `IDocument` at all is worth it
— see [borco/lexilla-py#6](https://github.com/borco/lexilla-py/issues/6).
The deprecated `CreateLexerLibrary` path and
the full property/word-list introspection API are also deferred.

### No bare ints/strings for "magic" values: typed enums for property types, language identifiers, and lexer names

`Lexer.property_type()`, `Lexer.identifier`, and `create_lexer(name)` all
deal in values that are really enumerations dressed up as a bare `int` or
`str`: Scintilla's `SC_TYPE_*` (boolean/integer/string), Scintilla's
`SCLEX_*` language identifiers (declared in Lexilla's own vendored
`include/SciLexer.h`), and Lexilla's ~139-entry lexer-name catalogue
respectively. Left as bare values there's no IDE autocomplete or hover
documentation, and a typo silently does the wrong thing instead of failing
loudly. The fix, applied consistently to all three:

- Both `PropertyType` and `LanguageIdentifier` are registered with
  `nb::is_arithmetic()`, so e.g. `lexer.identifier == 3` works directly
  against the raw Scintilla constant, without requiring `.value` or an
  explicit `int()` cast — they still wrap Scintilla's own `SC_TYPE_*`/
  `SCLEX_*` integers, so comparing against the documented numeric constant
  should just work.
- `PropertyType` (`SC_TYPE_*`) is a small, hand-written `nb::enum_` in
  `_binding.cpp` — only 3 values, no codegen needed.
- `LanguageIdentifier` (`SCLEX_*`, ~142 values) is **generated**, not
  hand-typed, by `tools/generate_language_enums.py` (a top-level `tools/`,
  matching the sibling pyside6-scintilla project's convention for its own
  generator scripts), mirroring Lexilla's *own* convention for its large
  generated lists (`src/lexilla_vendor/src/Lexilla.cxx`'s
  `//++Autogenerated -- run scripts/LexillaGen.py to regenerate` markers):
  a one-off script, run manually, output spliced into `_binding.cpp` and
  checked into git — not wired into the CMake/`uv sync` build, so Python
  stays out of the C++ compile step beyond what scikit-build-core already
  needs. The generator reuses the vendored, unmodified
  `src/lexilla_vendor/scripts/LexillaData.py` (Lexilla's own lexer-catalogue
  parser) rather than re-deriving its parsing logic. Four `SCLEX_*` macros
  have no associated lexer (`CONTAINER`, `NULL`, `AUTOMATIC`, and
  `XCODE` — confirmed via grep that none has a `LexerModule`); all four are
  kept in the enum rather than excluded, since dropping any would make the
  enum lossy and risk a runtime nanobind error if `GetIdentifier()` ever
  legitimately returns one. `SCLEX_NULL`'s enum member is named `NullValue`
  in C++ (it would otherwise collide with the `<cstddef>` `NULL` macro,
  which the preprocessor rewrites before the compiler ever sees an
  identifier); its Python-facing name is still `NULL`, via the
  `nb::enum_<>::value()` registration string. Every generated value gets its
  own short docstring, derived from the same name data already being
  parsed, so the per-value documentation bar is the same for 3 values or
  142.
- `Language` (the lexer-name strings) is a Python `enum.StrEnum` in a
  generated `src/lexilla/_languages.py` — no C++ change needed, since
  nanobind's `const char*` parameter for `create_lexer` accepts any `str`
  subclass, and `StrEnum` members *are* `str` instances
  (`create_lexer(Language.CPP)` works with zero binding changes). There's
  no natural C++ representation for opaque name strings (unlike `SCLEX_*`,
  a real Scintilla enum), so this stays pure Python. The one catalogue name
  unsafe as a Python identifier as-is, `"PL/M"`, becomes member name `PLM`
  (not `PL_M`) — matching every other C identifier for that lexer across
  the vendored source (`SCLEX_PLM`, `SCE_PLM_*`, `lmPLM`), none of which use
  an underscore for the dropped slash.

Checked `https://www.scintilla.org/LexillaDoc.html` for official wording to
reuse in these docstrings: it documents only the library-level functions
(`CreateLexer`, `GetLexerCount`, `GetLexerName`, etc.), nothing at the
`SC_TYPE_*`/`SCLEX_*`/`ILexer4`/`ILexer5` granularity — so all docstrings
here are original, not adapted from upstream text.

Because the generated enums are derived from whatever Lexilla version is
currently vendored, they go stale silently at compile time (a `static_cast`
always succeeds) but loudly at the Python boundary (nanobind raises if
`GetIdentifier()` ever returns a value with no matching enum member) — see
[auditing.md](../auditing.md)'s re-vendoring checklist for the regeneration
step this requires.

### `ILexer5`'s declaration: vendor Scintilla's interface headers, not all of Scintilla

`ILexer5` (along with `ILexer4`, `IDocument`, and the `Sci_Position`/
`Sci_PositionU` types) is declared in Scintilla's `ILexer.h`/`Sci_Position.h`,
not in Lexilla's own tarball — `Lexilla.h` assumes the caller has already
included `ILexer.h`. The individual lexer implementations also need a
handful of fold-level flag constants from Scintilla's `Scintilla.h` to
compile (the per-language `SCE_*` style constants already live in Lexilla's
own vendored `include/SciLexer.h`, no extra vendoring needed for those).
Vendoring all of Scintilla just for these interface/constant headers would reintroduce
the dependency this project deliberately avoids (see "What this is NOT").
Instead, only those headers are vendored, unmodified, under
`src/scintilla_interface/include/` — see [auditing.md](../auditing.md) for
the version/checksum table and the process
for keeping them in sync with the vendored Lexilla version when it updates.

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
