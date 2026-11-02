# tools

Development scripts for this repo. Run with `uv run python tools/<script>.py`.

## [`generate_scintilla_edit.py`](generate_scintilla_edit.py)

Generates `src/pyside6_scintilla/bindings/scintilla_edit_fixed.{h,cpp}`, the
typed method-per-message class exposed as `ScintillaEdit`, from
`src/scintilla/include/Scintilla.iface` -- text as `str`, raw data as bytes
(see "Text vs bytes" in [`docs/bindings.md`](../docs/bindings.md)). Run via
`make generate` after vendoring a new Scintilla release; `--check` (run by
`make lint` and CI) fails if the checked-in output is stale.

## [`generate_pyi.py`](generate_pyi.py)

Regenerates `src/pyside6_scintilla/_pyside6_scintilla.pyi`, the type stub
that gives Pylance/mypy/ruff full signatures and autocomplete for
`Scintilla.*` and `ScintillaEditBase`. Run after `make install` /
`uv sync --reinstall-package pyside6-scintilla` whenever `bindings.xml`/
`bindings.h` change the public API (see `make stubs` and
[`docs/bindings.md`](../docs/bindings.md)).

## [`check_docs_sync.py`](check_docs_sync.py)

Verifies that the `<!-- sync:NAME -->` blocks shared between `README.md`
and `docs/index.md` (badges, install snippet, usage example) stay
identical in both files. Run via `make lint` and in CI.

## [`clean_window_corners.py`](clean_window_corners.py)

One-off image cleanup for Windows window screenshots (e.g. Snipping Tool)
used in docs: removes the dark rounded-corner/border artifacts that a
rectangular capture picks up from the desktop behind the window. Used for
`docs/assets/images/examples/*.png`; not part of the build.
