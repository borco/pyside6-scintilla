.PHONY: setup lint format test clean clean-setup

setup:
	uv sync

lint:
	uv run ruff check .

format:
	uv run ruff format .

test:
	uv run pytest

clean:
	rm -rf build dist

clean-setup:
	rm -rf .venv

# Added once CMakeLists.txt / CMakePresets.json exist:
# .PHONY: configure build install
# configure:
# 	cmake --preset venv
# build:
# 	cmake --build --preset venv
# install:
# 	cmake --build --preset venv --target install
