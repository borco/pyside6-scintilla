# Building and publishing

## Prerequisites

- Python 3.11+ and [uv](https://docs.astral.sh/uv/)
- Qt 6.10+ matching the PySide6/shiboken6 version resolved by `uv sync`
  (currently 6.11.x), **including the Qt 5 Compatibility module
  (`Qt6Core5Compat`)** -- not installed by default, add it via the Qt
  Maintenance Tool/online installer for your kit.
- A C++17 compiler:
  - **Windows**: MSVC (Visual Studio 2022). Use the same MSVC toolchain
    PySide6's wheels are built with, to avoid ABI mismatches against the
    Qt/shiboken libraries bundled in the PySide6 wheel.
  - **macOS**: Xcode command line tools.
  - **Linux**: GCC or Clang.
- CMake 3.25+ and Ninja -- available as dev dependencies via `uv`, or from
  `<Qt>/Tools/CMake_64` / `<Qt>/Tools/Ninja` if you installed them through the
  Qt installer.

## Local development build

The build is driven by `uv sync` (scikit-build-core + CMake +
`shiboken_generator_create_binding()`). CMake needs `CMAKE_PREFIX_PATH`
pointing at your Qt 6 installation:

```powershell
# Windows (PowerShell)
$env:CMAKE_PREFIX_PATH = "C:\Qt\6.11.1\msvc2022_64"
uv sync
```

```bash
# Linux / macOS
export CMAKE_PREFIX_PATH=/path/to/Qt/6.11.1/gcc_64   # or macos/clang_64, etc.
uv sync
```

To avoid setting this every time, copy it into a gitignored
`CMakeUserPresets.json` that inherits from the `venv` preset in
`CMakePresets.json`, e.g.:

```json
{
    "version": 8,
    "configurePresets": [
        {
            "name": "venv-local",
            "inherits": "venv",
            "cacheVariables": {
                "CMAKE_PREFIX_PATH": "C:/Qt/6.11.1/msvc2022_64"
            }
        }
    ]
}
```

### Forcing a rebuild

`uv sync` doesn't always notice changes to `CMakeLists.txt` or the typesystem
files -- it may print "Checked N packages" without rebuilding. Force a
rebuild + reinstall with:

```bash
uv sync --reinstall-package pyside6-scintilla
```

### Faster C++/binding-only iteration

For changes to `CMakeLists.txt`, `bindings.xml`, or the binding glue, `uv
sync --reinstall-package` does a clean, isolated rebuild every time. The
`configure`/`build`/`install` Make targets are faster for repeated
iteration: they reuse an incremental CMake build tree (`build/venv/`) and,
via the `venv` preset's `CMAKE_INSTALL_PREFIX`, drop the rebuilt extension
and shared libs directly into `src/pyside6_scintilla/`, where `import
pyside6_scintilla` picks them up immediately.

```bash
make configure   # once, to set up build/venv/
make install      # rebuild + drop the extension into src/pyside6_scintilla/
```

**Windows**: the `venv` preset uses the Ninja generator, which needs
`cl.exe` on `PATH` -- run these from an **x64 Native Tools Command Prompt
for VS 2022** (or call `vcvarsall.bat x64` first). `uv sync` doesn't need
this, since scikit-build-core uses the Visual Studio generator, which
locates MSVC itself.

### Verifying the build

```bash
uv run python -c "from pyside6_scintilla import Scintilla, ScintillaEditBase; print(Scintilla.Message.SetText)"
uv run pytest
uv run ruff check .
```

or, via the `Makefile`:

```bash
make setup
make test
make lint
```

## Continuous integration

`.github/workflows/ci.yml` runs on every push and on pull requests targeting
`master`, across `ubuntu-latest`, `windows-latest`, and `ubuntu-24.04-arm`
(Linux x86_64/aarch64 + Windows x86_64). Each job:

1. Installs Qt **6.11.1** plus the `Qt6Core5Compat` module via
   [`jurplel/install-qt-action`](https://github.com/jurplel/install-qt-action)
   -- matching the PySide6 6.11.1 pinned in `uv.lock`, since CI and local
   builds must use the same Qt minor version to avoid ABI mismatches (see
   [Prerequisites](#prerequisites) above).
2. Points `CMAKE_PREFIX_PATH` at that Qt install, and on Linux also sets
   `LD_LIBRARY_PATH` so `scintilla_qt.so` can find `libQt6Core5Compat.so.6` at
   runtime (see [bindings.md](bindings.md) issue 3).
3. Runs `uv sync`, `uv run pytest` (with `QT_QPA_PLATFORM=offscreen` for a
   headless `pytest-qt`), and `uv run ruff check .` / `ruff format --check .`
   -- the same commands as [Verifying the build](#verifying-the-build) above.

CI doesn't run the example app, and only builds the dev install (not wheels)
-- see [Building wheels](#building-wheels) below for the wheel-building
workflow.

## Building wheels

```bash
uv build
```

produces a wheel + sdist in `dist/`, for the **current platform only**.
Multi-platform wheels are built in CI by
`.github/workflows/wheels.yml` via [cibuildwheel](https://cibuildwheel.pypa.io/),
covering `cp31{1,2,3,4}` for Linux x86_64 (`manylinux_2_34`), Windows x86_64,
and macOS arm64/x86_64 (the latter cross-built via Rosetta 2 on the
`macos-latest` runner). It's `workflow_dispatch`-only for manual/ad-hoc builds,
and also exposed as a reusable `workflow_call` job consumed by
`publish.yml` (see [Publishing to PyPI](#publishing-to-pypi)).

### Platform-specific bundling caveats

`Qt6Core5Compat` is required by `scintilla_qt` but isn't bundled in the
PySide6 wheel on any platform. `bindings/CMakeLists.txt` installs it
alongside the extension for all three platforms (a flat `.dll`/`.so` on
Windows/Linux, a framework bundle on macOS), and each platform's
`repair-wheel-command` in `pyproject.toml`
(`delvewheel`/`auditwheel`/`delocate`) excludes the Qt/PySide6/shiboken6
libraries provided at runtime by the installed PySide6 package. See
[bindings.md](bindings.md) issue 3 for the details and history.

## Publishing to PyPI

1. Bump `__version__` in `src/pyside6_scintilla/__init__.py` -- this is the
   single source of truth for the package version
   (`[tool.scikit-build.metadata.version]` in `pyproject.toml` reads it via
   regex). Follow Scintilla's version: `X.Y.Z.N`, where `X.Y.Z` is the
   vendored Scintilla release and `N` increments for binding-only changes
   against that release. See [bindings.md](bindings.md) for the Scintilla
   update process.
2. Push the version bump to `master`.
3. Create a GitHub Release with a tag matching the version (e.g. `v5.6.3.0`).
   This triggers `.github/workflows/publish.yml`, which builds the sdist and
   all wheels (via `wheels.yml`), publishes them to TestPyPI, and then -- for
   real releases only -- to PyPI.

No PyPI API tokens are involved: both the TestPyPI and PyPI publish steps use
[PyPI trusted publishing](https://docs.pypi.org/trusted-publishers/) (GitHub
OIDC), configured per-project on test.pypi.org/pypi.org against this repo's
`publish.yml` workflow and the `testpypi`/`pypi` GitHub environments.

The `pyside6-scintilla` PyPI name was claimed early with a placeholder `0.0.0`
release (pure-Python, hatchling backend, published manually via `uv publish`)
to prevent squatting -- the first real release is the first one published via
`publish.yml`.
