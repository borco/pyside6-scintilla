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

## Building wheels

```bash
uv build
```

produces a wheel + sdist in `dist/`, for the **current platform only**. There
is no multi-platform CI build (cibuildwheel) yet -- see `MISSION.md` for the
intended Linux x86_64/aarch64, Windows x86_64, and macOS arm64/x86_64 targets.
Until that's set up, release wheels must be built manually on each platform.

### Platform-specific bundling caveats

`Qt6Core5Compat` is required by `scintilla_qt` but isn't bundled in the
PySide6 wheel on any platform. On Windows, `bindings/CMakeLists.txt` installs
`Qt6Core5Compat.dll` alongside the extension. **Linux/macOS still need an
equivalent step** (`delvewheel`/`auditwheel`/`delocate`, or an
`install(FILES ...)` analogous to the Windows one) -- see
[BINDINGS.md](BINDINGS.md) issue 3.

## Publishing to PyPI

1. Bump `__version__` in `src/pyside6_scintilla/__init__.py` -- this is the
   single source of truth for the package version
   (`[tool.scikit-build.metadata.version]` in `pyproject.toml` reads it via
   regex). Follow Scintilla's version: `X.Y.Z.N`, where `X.Y.Z` is the
   vendored Scintilla release and `N` increments for binding-only changes
   against that release. See [BINDINGS.md](BINDINGS.md) for the Scintilla
   update process.
2. Build wheels for all target platforms (manually, until CI is wired up).
3. `uv build`
4. `uv publish` (requires a PyPI API token, e.g. via
   `uv publish --token <token>` or the `UV_PUBLISH_TOKEN` environment
   variable).

The `pyside6-scintilla` PyPI name was claimed early with a placeholder `0.0.0`
release (pure-Python, hatchling backend) to prevent squatting -- the first
real release will be the first one built from this binding.
