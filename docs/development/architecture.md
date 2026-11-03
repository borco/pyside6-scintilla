# How the packages are built

Both packages are C++ extensions built with CMake and
[scikit-build-core](https://scikit-build-core.readthedocs.io/), from vendored
upstream release sources, into one wheel per platform. Beyond that they use
different binding stacks, on purpose. This page explains the difference and
the reasons; [Building and publishing](build.md) covers the day-to-day
workflow.

## At a glance

| | pyside6-scintilla | lexilla |
| --- | --- | --- |
| Wraps | Scintilla's Qt widget (`ScintillaEditBase`, a `QAbstractScrollArea`) | Lexilla's C++ API (`CreateLexer`, `ILexer5`) |
| Binding generator | [shiboken6](https://doc.qt.io/qtforpython-6/shiboken6/) (PySide6's own) | [nanobind](https://nanobind.readthedocs.io/) |
| Build needs | a Qt 6.12 SDK (incl. `Qt6Core5Compat`), PySide6 + shiboken6 6.12, libclang | a C++17 compiler |
| Runtime needs | PySide6-Essentials 6.12.x (pinned to the minor) | nothing (pyside6-scintilla only for the glue) |
| Python ABI | limited API, `cp311-abi3` (shiboken6's `FORCE_LIMITED_API`) | limited API, `cp312-abi3` (nanobind's `STABLE_ABI` needs 3.12) |
| Built as | `scintilla_qt` shared library + the `_pyside6_scintilla` extension | `lexilla_core` static library linked into `_lexilla` |
| Workspace build | without build isolation (must see `.venv`'s PySide6) | isolated, as usual |
| Generated code | the typed `ScintillaEdit` class (`tools/generate_scintilla_edit.py`, from `Scintilla.iface`), the `.pyi` stub (genpyi + `tools/generate_pyi.py`) | the `LanguageIdentifier`/`Language` enums (`tools/generate_language_enums.py`), the `.pyi` stub (nanobind's stubgen) |
| Wheel repair | excludes the Qt/PySide6/shiboken6 libraries PySide6 provides, bundles `Qt6Core5Compat` | default (nothing to exclude or bundle) |
| Details | [Bindings architecture](../pyside6-scintilla/bindings.md), [build notes](../pyside6-scintilla/build.md) | [Bindings architecture](../lexilla/bindings.md), [build notes](../lexilla/build.md) |

## Why shiboken6 for pyside6-scintilla

The thing being bound is a Qt widget. Python code has to be able to put it in
a layout, parent it, connect its signals to slots, subclass it and pass
`QColor`s and `QString`s in and out -- i.e. it has to *be* a PySide6
`QWidget`, not merely look like one. Only shiboken6 generates wrappers that
plug into PySide6's own type system (the converters, the `QObject` ownership
model, the signal/slot machinery, PySide6's typesystems for QtCore/QtGui/
QtWidgets). A binding made with any other generator would be a separate type
universe that PySide6 doesn't recognize as a widget.

The cost is PySide6's toolchain:

- **The Qt SDK**, at the same minor version as the PySide6 the extension runs
  against, because `scintilla_qt` compiles against Qt's headers.
- **One PySide6 minor per release.** The extension calls into shiboken6's and
  PySide6's C++ libraries, whose ABI changes between minors, so each release
  pins `PySide6-Essentials>=6.X,<6.(X+1)` (issue #15).
- **No build isolation in the workspace:** CMake must find the PySide6/shiboken6
  CMake packages of the environment the extension is imported from.

## Why nanobind for lexilla

Lexilla's public surface is plain C++ -- a few free functions and one
abstract interface -- with no Qt types anywhere. shiboken6 would drag in the
whole Qt toolchain and the PySide6 version pin just to bind those, for no
benefit. nanobind is small, has no Qt/PySide6 dependency, and fits a handful
of functions plus one interface class. As a result lexilla builds with just a
C++ compiler, has no runtime dependencies, and doesn't care which PySide6
version is installed.

## Where they meet

- **The lexer pointer.** `create_lexer()` returns a `Lexer` whose
  `ILexer5*` pointer is handed to the editor with `SCI_SETILEXER`, as a plain
  integer -- the two extensions never see each other's types.
  `lexilla.pyside6_scintilla.set_lexer()` wraps that for convenience; it's
  the only place lexilla imports pyside6-scintilla.
- **The Scintilla interface headers.** For that pointer to be usable, both
  sides must agree on `ILexer5`'s layout, declared in Scintilla's `ILexer.h`.
  pyside6-scintilla compiles against its vendored Scintilla; lexilla against
  a byte-identical copy of the same headers (lexilla's sdist must build on its
  own, so it can't reach into the other package), kept in sync by
  `tools/sync_scintilla_headers.py` and checked in CI. See
  [Verifying vendored Lexilla](../lexilla/auditing.md) for what that does and
  doesn't guarantee across releases.
- **Tests.** In the workspace and in CI, lexilla's tests (including its glue)
  run against the pyside6-scintilla built from the same commit, and its wheel
  tests install the pyside6-scintilla wheels built in the same run.
