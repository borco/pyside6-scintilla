# Building and publishing

## Prerequisites

- Python 3.11+ and [uv](https://docs.astral.sh/uv/)
- Qt 6.11.x, the PySide6/shiboken6 minor pinned in `pyproject.toml` (the
  SDK must match the minor the extension links against; patch releases are
  interchangeable), **including the Qt 5 Compatibility module
  (`Qt6Core5Compat`)** -- not installed by default, add it via the Qt
  Maintenance Tool/online installer for your kit.
- A C++17 compiler:
  - **Windows**: MSVC (Visual Studio 2022). Use the same MSVC toolchain
    PySide6's wheels are built with, to avoid ABI mismatches against the
    Qt/shiboken libraries bundled in the PySide6 wheel.
  - **macOS**: Xcode command line tools.
  - **Linux**: GCC or Clang. **Not Ubuntu 26.04 or newer (or another
    distro with libxml2 2.14+)**: `shiboken6-generator`'s prebuilt
    `shiboken6` binary (6.11 and 6.12 alike) links the system
    `libxml2.so.2`, which libxml2 2.14 replaced with `libxml2.so.16`, so the
    build fails with "error while loading shared libraries: libxml2.so.2".
    Build on Ubuntu 24.04 (as CI does) or in a container/manylinux image.
    Only building is affected: the extension doesn't use libxml2, and the
    published wheels run fine on 26.04 (CI's `runtime` job checks this).
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

> [!TIP]
> **Windows**: to avoid setting `CMAKE_PREFIX_PATH` every session, persist it
> to the user environment instead:
>
> ```powershell
> $existing = [System.Environment]::GetEnvironmentVariable("CMAKE_PREFIX_PATH", "User")
> $new = if ($existing) { "$existing;C:\Qt\6.11.1\msvc2022_64" } else { "C:\Qt\6.11.1\msvc2022_64" }
> [System.Environment]::SetEnvironmentVariable("CMAKE_PREFIX_PATH", $new, "User")
> ```
>
> Restart your terminal (or VS Code) afterward -- the new value only applies
> to terminals opened after it's set.

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
   / `uv run pyright` -- the same commands as
   [Verifying the build](#verifying-the-build) above.

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
covering a single `cp311-abi3` wheel per platform -- Linux x86_64
(`manylinux_2_34`), Linux aarch64, Windows x86_64, and macOS arm64/x86_64
(the latter cross-built via Rosetta 2 on the `macos-latest` runner). One
wheel per platform, not one per Python version, because the extension is
compiled against Python's limited API (`FORCE_LIMITED_API` in
`bindings/CMakeLists.txt`, `wheel.py-api = "cp311"` in `pyproject.toml`) --
the same build works on 3.11+ (forward-compatible with 3.12, 3.13, 3.14,
and beyond) without a rebuild, same as PySide6's own wheels. It's `workflow_dispatch`-only for manual/ad-hoc builds, and also
exposed as a reusable `workflow_call` job consumed by `publish.yml` (see
[Publishing to PyPI](#publishing-to-pypi)).

### Platform-specific bundling caveats

`Qt6Core5Compat` is required by `scintilla_qt` but isn't bundled in the
PySide6 wheel on any platform. `bindings/CMakeLists.txt` installs it
alongside the extension for all three platforms (a flat `.dll`/`.so` on
Windows/Linux, a framework bundle on macOS), and each platform's
`repair-wheel-command` in `pyproject.toml`
(`delvewheel`/`auditwheel`/`delocate`) excludes the Qt/PySide6/shiboken6
libraries provided at runtime by the installed PySide6 package. See
[bindings.md](bindings.md) issue 3 for the details and history.

## Bumping the PySide6 minor

Each release is built for one PySide6 minor (issue #15): shiboken6/PySide6's
C++ ABI changes between minors, so a wheel built against 6.11 fails to import
with 6.12. Moving to a new minor (`6.X`) means a new release with all of
these updated together -- there is no single source of truth yet (the
monorepo's shared CI setup action will hold the Qt version), so check each:

1. `pyproject.toml`
   - `[build-system].requires`: `shiboken6-generator`, `shiboken6`,
     `PySide6-Essentials` -> `>=6.X,<6.(X+1)`.
   - `[project].dependencies`: `PySide6-Essentials`, `shiboken6` -> same.
   - `[dependency-groups].dev`: `shiboken6-generator` -> same.
   - `[tool.cibuildwheel]`: the Qt version in every `before-all` (aqtinstall)
     and `CMAKE_PREFIX_PATH` (Linux x86_64, Linux aarch64, macOS); the
     manylinux image if PySide6's own wheel tag moved; the macOS
     `MACOSX_DEPLOYMENT_TARGET` if PySide6's macOS wheel tag moved; and the
     Linux auditwheel excludes `libpyside6.abi3.so.6.X` /
     `libshiboken6.abi3.so.6.X` (the soname carries the minor -- a stale
     exclude silently bundles a second copy of PySide6's libraries) and the
     `libicu*` version the Qt SDK ships.
2. `.github/workflows/ci.yml` and `wheels.yml`: the Qt `version:` installed
   by `install-qt-action`.
3. `uv lock` (then `uv sync --reinstall-package pyside6-scintilla`, run the
   tests, and `make stubs` in case genpyi's output changed).
4. The Qt SDK version mentioned in this file's examples, and the
   installation note in `README.md`/`docs/index.md`.
5. `CHANGELOG.md`: a breaking "requires PySide6 6.X" entry, and a new
   `__version__`.

Then check the built wheel in a fresh venv: it must import beside the new
minor's newest patch release, and pip must refuse to install it beside the
previous minor.

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
