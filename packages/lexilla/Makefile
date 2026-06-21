.PHONY: setup lint format test clean clean-setup configure build install publish stubs docs-serve qa generate-language-enums

setup:
	uv sync

lint:
	uv run ruff check .
	uv run pyright

# Serve the docs site locally with live-reload (http://127.0.0.1:8000/lexilla-py/).
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
# `install` also copies the built module into src/lexilla/ so `import
# lexilla` picks up the change. These need build/venv/ to exist (run
# `configure` once first) -- `build` and `install` chain to it so `make
# install` works standalone.
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

# Regenerate src/lexilla/_lexilla.pyi from the compiled extension. Run after
# `make install` whenever _binding.cpp changes the public API.
stubs:
	uv run python -m nanobind.stubgen -m lexilla._lexilla -O src/lexilla

qa: format test lint

# Regenerate the LanguageIdentifier/Language enums from src/lexilla_vendor/.
# One-off, NOT part of qa/build/setup -- re-run manually after re-vendoring
# (see docs/auditing.md's re-vendoring checklist).
generate-language-enums:
	uv run python tools/generate_language_enums.py
