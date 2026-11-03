# tools

Code generators for the `pyside6-scintilla` package. Run from this package's
directory with `uv run python tools/<script>.py` (or via the top-level `Makefile`).

## [`generate_scintilla_edit.py`](generate_scintilla_edit.py)

Generates `src/pyside6_scintilla/bindings/scintilla_edit_fixed.{h,cpp}`, the
typed method-per-message class exposed as `ScintillaEdit`, from
`src/scintilla/include/Scintilla.iface` -- text as `str`, raw data as bytes
(see "Text vs bytes" in [`docs/pyside6-scintilla/bindings.md`](../../../docs/pyside6-scintilla/bindings.md)). Run via
`make scintilla-generate` after vendoring a new Scintilla release; `--check` (run by
`make lint` and CI) fails if the checked-in output is stale.

## [`generate_pyi.py`](generate_pyi.py)

Regenerates `src/pyside6_scintilla/_pyside6_scintilla.pyi`, the type stub
that gives Pylance/mypy/ruff full signatures and autocomplete for
`Scintilla.*` and `ScintillaEditBase`. Run after `make scintilla-install` /
`uv sync --reinstall-package pyside6-scintilla` whenever `bindings.xml`/
`bindings.h` change the public API (see `make scintilla-stubs` and
[`docs/pyside6-scintilla/bindings.md`](../../../docs/pyside6-scintilla/bindings.md)).

