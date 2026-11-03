# Top-level orchestration for the workspace (see CLAUDE.md, "Monorepo layout").
# Workspace-wide targets act on both packages; per-package targets are
# prefixed `scintilla-` (packages/pyside6-scintilla) or `lexilla-`
# (packages/lexilla). Everything runs in the one workspace venv at the root.

.PHONY: setup sync test lint format pyright qa docs-serve docs-build clean clean-setup sync-headers \
	scintilla-configure scintilla-build scintilla-install scintilla-generate scintilla-stubs \
	lexilla-stubs lexilla-enums

SCINTILLA := packages/pyside6-scintilla
LEXILLA := packages/lexilla

# UTF-8 mode (PEP 540) for every recipe, so a tool printing non-ASCII can't
# die on a Windows console's default cp1252 encoding.
export PYTHONUTF8 := 1

# --- workspace ---------------------------------------------------------------

# Build both packages from source into .venv (editable), plus the dev tools.
setup sync:
	uv sync

test:
	uv run pytest

lint:
	uv run ruff check .
	uv run ruff format --check .
	uv run python tools/check_docs_sync.py
	uv run python tools/sync_scintilla_headers.py --check
	uv run python $(SCINTILLA)/tools/generate_scintilla_edit.py --check
	uv run pyright

format:
	uv run ruff format .

pyright:
	uv run pyright

qa: format test lint

# Serve the docs site locally with live-reload.
docs-serve:
	uv run --group docs mkdocs serve

docs-build:
	uv run --group docs mkdocs build --strict

clean:
	rm -rf build dist site $(SCINTILLA)/build $(SCINTILLA)/dist $(LEXILLA)/build $(LEXILLA)/dist

clean-setup:
	rm -rf .venv

# Refresh lexilla's copy of the Scintilla interface headers from the vendored
# Scintilla (see tools/sync_scintilla_headers.py). Run after vendoring a new
# Scintilla release.
sync-headers:
	uv run python tools/sync_scintilla_headers.py

# --- pyside6-scintilla ------------------------------------------------------

# Fast local iteration on the C++/binding side: reconfigure/rebuild the
# extension in-place against the existing .venv, without a full `uv sync`.
# The `venv` preset installs the built module into the package's src/, so
# `import pyside6_scintilla` picks up the change. The preset already targets
# `install`, so `scintilla-build` and `scintilla-install` run the same
# command -- the split is for clarity/ordering only.
scintilla-configure:
	cd $(SCINTILLA) && cmake --preset venv

scintilla-build: scintilla-configure
	cd $(SCINTILLA) && cmake --build --preset venv

scintilla-install: scintilla-build
	cd $(SCINTILLA) && cmake --build --preset venv --target install

# Regenerate the typed ScintillaEdit class (scintilla_edit_fixed.{h,cpp}) from
# Scintilla.iface. Run after vendoring a new Scintilla release, then rebuild
# and `make scintilla-stubs`.
scintilla-generate:
	uv run python $(SCINTILLA)/tools/generate_scintilla_edit.py

# Regenerate _pyside6_scintilla.pyi. Run after rebuilding (`make sync` or
# `uv sync --reinstall-package pyside6-scintilla`) whenever bindings.xml/
# bindings.h or the generated class change the public API.
scintilla-stubs:
	uv run python $(SCINTILLA)/tools/generate_pyi.py

# --- lexilla ---------------------------------------------------------------

# Regenerate _lexilla.pyi from the compiled extension. Run after rebuilding
# whenever _binding.cpp changes the public API.
lexilla-stubs:
	uv run python -m nanobind.stubgen -m lexilla._lexilla -O $(LEXILLA)/src/lexilla

# Regenerate the LanguageIdentifier/Language enums from the vendored Lexilla.
# One-off, not part of qa/build -- re-run after re-vendoring Lexilla.
lexilla-enums:
	uv run python $(LEXILLA)/tools/generate_language_enums.py
