# Building and publishing

## Prerequisites

- Python 3.11+ and [uv](https://docs.astral.sh/uv/)
- A C++17 compiler:
  - **Windows**: MSVC (Visual Studio 2022) or any toolchain Ninja can drive.
  - **macOS**: Xcode command line tools.
  - **Linux**: GCC or Clang.
- CMake 3.25+ and Ninja -- available as dev dependencies via `uv`.

No Qt SDK or other external SDK is needed -- Lexilla has no Qt dependency,
unlike pyside6-scintilla.

## Local development build

```bash
uv sync
```

drives the build (scikit-build-core + CMake + nanobind). No environment
variables to set (no `CMAKE_PREFIX_PATH` needed, unlike pyside6-scintilla).

### Forcing a rebuild

`uv sync` doesn't always notice changes to `CMakeLists.txt` or
`_binding.cpp` -- it may print "Checked N packages" without rebuilding.
Force a rebuild + reinstall with:

```bash
uv sync --reinstall-package lexilla
```

### Faster C++/binding-only iteration

```bash
make configure   # once, to set up build/venv/
make install      # rebuild + drop the extension into src/lexilla/
```

**Windows**: the `venv` preset uses the Ninja generator, which needs
`cl.exe` on `PATH` -- run these from an **x64 Native Tools Command Prompt
for VS 2022** (or call `vcvarsall.bat x64` first). `uv sync` doesn't need
this, since scikit-build-core handles compiler discovery itself.

### Verifying the build

```bash
uv run python -c "import lexilla; print(lexilla.__version__)"
uv run pytest
uv run ruff check .
uv run pyright
```

or, via the `Makefile`:

```bash
make setup
make test
make lint
```

## Continuous integration

`.github/workflows/ci.yml` runs on every push and on pull requests targeting
`master`, across `ubuntu-latest`, `windows-latest`, `macos-latest`, and
`ubuntu-24.04-arm`. Each job runs `uv sync`, `uv run pytest`, and
`uv run ruff check .` / `ruff format --check .` / `uv run pyright`.

CI doesn't run example apps, and only builds the dev install (not wheels) --
see [Building wheels](#building-wheels) below.

## Building wheels

```bash
uv build
```

produces a wheel + sdist in `dist/`, for the current platform only.
Multi-platform wheels are built in CI by `.github/workflows/wheels.yml` via
[cibuildwheel](https://cibuildwheel.pypa.io/), covering `cp31{1,2,3,4}` for
Linux x86_64/aarch64, Windows x86_64, and macOS arm64/x86_64. It's
`workflow_dispatch`-only for manual/ad-hoc builds, and also exposed as a
reusable `workflow_call` job consumed by `publish.yml`.

Unlike pyside6-scintilla, there's no Qt/PySide6 ABI to keep consistent and
no external library to bundle -- the default delocate/auditwheel/delvewheel
repair behavior in `cibuildwheel` needs no overrides here.

## Publishing to PyPI

1. Bump `__version__` in `src/lexilla/__init__.py` -- this is the single
   source of truth for the package version
   (`[tool.scikit-build.metadata.version]` in `pyproject.toml` reads it via
   regex). Follow Lexilla's version: `X.Y.Z.N`, where `X.Y.Z` is the
   vendored Lexilla release and `N` increments for binding-only changes
   against that release.
2. Push the version bump to `master`.
3. Create a GitHub Release with a tag matching the version (e.g.
   `v0.0.0.1`). This triggers `.github/workflows/publish.yml`, which builds
   the sdist and all wheels (via `wheels.yml`), publishes them to TestPyPI,
   and then -- for real releases only -- to PyPI.

No PyPI API tokens are involved -- see [docs/testpypi.md](testpypi.md) for
the trusted-publishing setup.

The `lexilla` PyPI name was claimed early to prevent squatting -- the first
real release is the first one published via `publish.yml`.
