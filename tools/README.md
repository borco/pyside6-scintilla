# tools

Repo-level development scripts. Run with `uv run python tools/<script>.py`.

The package-specific code generators live in each package's own `tools/`
(e.g. [`packages/pyside6-scintilla/tools/`](../packages/pyside6-scintilla/tools/)).

## [`check_docs_sync.py`](check_docs_sync.py)

Verifies that the `<!-- sync:NAME -->` blocks shared between
`packages/pyside6-scintilla/README.md` and `docs/index.md` (badges, install snippet, usage example) stay
identical in both files. Run via `make lint` and in CI.

## [`clean_window_corners.py`](clean_window_corners.py)

One-off image cleanup for Windows window screenshots (e.g. Snipping Tool)
used in docs: removes the dark rounded-corner/border artifacts that a
rectangular capture picks up from the desktop behind the window. Used for
`docs/assets/images/examples/*.png`; not part of the build.
