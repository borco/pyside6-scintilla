.PHONY: setup lint format test clean clean-setup configure build install publish stubs docs-serve

setup:
	uv sync

lint:
	uv run ruff check .
	uv run python tools/check_docs_sync.py

# Serve the docs site locally with live-reload (http://127.0.0.1:8000/pyside6-scintilla/).
docs-serve:
	uv run --group docs mkdocs serve

format:
	uv run ruff format .

test:
	uv run pytest

clean:
	rm -rf build dist

clean-setup:
	rm -rf .venv

# Fast local iteration on the C++/binding side: reconfigure/rebuild the
# extension in-place against the existing .venv, without a full `uv sync`.
# `install` also copies the built module into src/pyside6_scintilla/ so
# `import pyside6_scintilla` picks up the change.
# These need build/venv/ to exist (run `configure` once first) -- `build`
# and `install` chain to it so `make install` works standalone. Note: the
# `venv` build preset in CMakePresets.json already sets `targets: install`,
# and `--target` replaces (not adds to) a preset's targets, so `build` and
# `install` currently run the exact same cmake command -- the split exists
# for clarity/ordering, not because they differ.
configure:
	cmake --preset venv

build: configure
	cmake --build --preset venv

install: build
	cmake --build --preset venv --target install

# `uv build` does a clean, isolated scikit-build-core build (its own cmake
# configure+build+install) to produce a wheel + sdist in dist/ for
# distribution -- use this for releases, not day-to-day development.
publish: format test lint
	uv build
	uv publish

# Regenerate src/pyside6_scintilla/_pyside6_scintilla.pyi (see tools/generate_pyi.py
# and docs/bindings.md). Run after `make install` / `uv sync --reinstall-package
# pyside6-scintilla` whenever bindings.xml/bindings.h change the public API.
stubs:
	uv run python tools/generate_pyi.py
