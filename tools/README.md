# tools

Repo-level development scripts. Run with `uv run python tools/<script>.py`.

The package-specific code generators live in each package's own `tools/`
(e.g. [`packages/pyside6-scintilla/tools/`](../packages/pyside6-scintilla/tools/)).

## [`check_docs_sync.py`](check_docs_sync.py)

Verifies that each package's README (its PyPI page) and its docs-site page
share identical `<!-- sync:NAME -->` blocks (badges, install snippet, usage
example): `packages/pyside6-scintilla/README.md` with `docs/pyside6-scintilla/index.md`, and
`packages/lexilla/README.md` with `docs/lexilla/index.md`. Run via
`make lint` and in CI.

## [`sync_scintilla_headers.py`](sync_scintilla_headers.py)

Keeps lexilla's copy of the Scintilla interface headers
(`packages/lexilla/src/scintilla_interface/`) byte-identical to the vendored
Scintilla in `packages/pyside6-scintilla/src/scintilla/`. lexilla keeps its
own copy so its sdist builds on its own. Run via `make sync-headers` after
vendoring a new Scintilla release; `--check` runs in `make lint` and CI.

## [`changelog_section.py`](changelog_section.py)

Prints one version's section of a package's `CHANGELOG.md`, failing if it's
missing. `.github/workflows/publish.yml` uses it for the GitHub Release notes.

## [`clean_window_corners.py`](clean_window_corners.py)

One-off image cleanup for Windows window screenshots (e.g. Snipping Tool)
used in docs: removes the dark rounded-corner/border artifacts that a
rectangular capture picks up from the desktop behind the window. Used for
`docs/assets/images/examples/*.png`; not part of the build.
