# Building and publishing

This repo is a [uv workspace](https://docs.astral.sh/uv/concepts/projects/workspaces/)
with two packages, each released to PyPI on its own:

| Package | Directory | Binding | Needs a Qt SDK to build |
| --- | --- | --- | --- |
| `pyside6-scintilla` | `packages/pyside6-scintilla/` | shiboken6 | yes |
| `lexilla` | `packages/lexilla/` | nanobind | no |

The dev environment (`.venv` at the repo root) builds **both** from source,
so the prerequisites below are pyside6-scintilla's. lexilla-specific notes:
[lexilla build notes](../lexilla/build.md), and [How the packages are built](architecture.md) for why the two differ.

## Prerequisites

- Python 3.12+ (the workspace's floor -- lexilla needs 3.12; pyside6-scintilla
  itself supports 3.11) and [uv](https://docs.astral.sh/uv/)
- Qt 6.12.x, the PySide6/shiboken6 minor pinned in
  `packages/pyside6-scintilla/pyproject.toml` (the SDK must match the minor
  the extension links against; patch releases are interchangeable),
  **including the Qt 5 Compatibility module (`Qt6Core5Compat`)** -- not
  installed by default, add it via the Qt Maintenance Tool/online installer
  for your kit.
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
    Reported upstream as
    [PYSIDE-3504](https://qt-project.atlassian.net/browse/PYSIDE-3504).
    Only building is affected: the extension doesn't use libxml2, and the
    published wheels run fine on 26.04 (CI's `runtime` job checks this).
- CMake 3.25+ and Ninja -- available as dev dependencies via `uv`, or from
  `<Qt>/Tools/CMake_64` / `<Qt>/Tools/Ninja` if you installed them through the
  Qt installer.

## Local development build

From the repo root, `uv sync` builds both packages (editable) plus the dev
tools into `.venv`. pyside6-scintilla's CMake needs `CMAKE_PREFIX_PATH`
pointing at your Qt 6 installation:

```powershell
# Windows (PowerShell)
$env:CMAKE_PREFIX_PATH = "C:\Qt\6.12.0\msvc2022_64"
uv sync
```

```bash
# Linux / macOS
export CMAKE_PREFIX_PATH=/path/to/Qt/6.12.0/gcc_64   # or macos/clang_64, etc.
uv sync
```

> [!TIP]
> **Windows**: to avoid setting `CMAKE_PREFIX_PATH` every session, persist it
> to the user environment instead:
>
> ```powershell
> $existing = [System.Environment]::GetEnvironmentVariable("CMAKE_PREFIX_PATH", "User")
> $new = if ($existing) { "$existing;C:\Qt\6.12.0\msvc2022_64" } else { "C:\Qt\6.12.0\msvc2022_64" }
> [System.Environment]::SetEnvironmentVariable("CMAKE_PREFIX_PATH", $new, "User")
> ```
>
> Restart your terminal (or VS Code) afterward -- the new value only applies
> to terminals opened after it's set.

The packages depend on each other only for development -- lexilla's glue
module and tests use pyside6-scintilla, pyside6-scintilla's lexilla example
uses lexilla -- and always as workspace sources (`[tool.uv.sources]` in the
root `pyproject.toml`), never the PyPI copies.

### Forcing a rebuild

`uv sync` doesn't always notice changes to `CMakeLists.txt`, the typesystem
files or the binding sources -- it may print "Checked N packages" without
rebuilding. Force a rebuild + reinstall of one package with:

```bash
uv sync --reinstall-package pyside6-scintilla   # or lexilla
```

For faster C++/binding-only iteration on pyside6-scintilla, see its
[build notes](../pyside6-scintilla/build.md#faster-cbinding-only-iteration).

### Verifying the build

```bash
make test   # both packages' tests (uv run pytest)
make lint   # ruff, docs/header/generator sync checks, pyright
```

`make` lists the per-package targets (`scintilla-*`, `lexilla-*`); see the
top-level `Makefile`.

## Continuous integration

`.github/workflows/ci.yml` runs on every push and on pull requests targeting
`master`, across Ubuntu 24.04 x86_64/aarch64, Windows and macOS. Each job:

1. Sets up the toolchain with `.github/actions/setup`: Qt **6.12.0** plus
   `Qt6Core5Compat` via
   [`jurplel/install-qt-action`](https://github.com/jurplel/install-qt-action)
   (the one place CI names the Qt version), `CMAKE_PREFIX_PATH` (and, on
   Linux, `LD_LIBRARY_PATH` so `scintilla_qt.so` can find
   `libQt6Core5Compat.so.6` at runtime -- see [Bindings architecture](../pyside6-scintilla/bindings.md)
   issue 3), clang on Linux, then `uv sync` (both packages).
2. Runs both packages' tests (with `QT_QPA_PLATFORM=offscreen` for a
   headless `pytest-qt`) and the same checks as `make lint`.

The Ubuntu 24.04 job also builds both wheels; the `runtime` job installs them
on Ubuntu 26.04 with Python 3.14 and runs both test suites against them.

## Building wheels

```bash
uv build --package pyside6-scintilla   # or lexilla
```

produces a wheel + sdist in `dist/`, for the **current platform only**.
Multi-platform wheels are built in CI by `.github/workflows/wheels.yml` via
[cibuildwheel](https://cibuildwheel.pypa.io/), one package at a time
(`package-dir: packages/<name>`), each with its own `[tool.cibuildwheel]`
config in its `pyproject.toml`:

- **pyside6-scintilla**: a single `cp311-abi3` wheel per platform -- Linux
  x86_64 (`manylinux_2_34`), Linux aarch64, Windows x86_64, and macOS
  arm64/x86_64 (the latter cross-built via Rosetta 2 on the `macos-latest`
  runner). One wheel per platform, not one per Python version, because the
  extension is compiled against Python's limited API (`FORCE_LIMITED_API` in
  `bindings/CMakeLists.txt`, `wheel.py-api = "cp311"`), same as PySide6's own
  wheels.
- **lexilla**: a single `cp312-abi3` wheel per platform, for the same reason
  (nanobind's stable ABI needs CPython 3.12). Its wheel tests need
  pyside6-scintilla, so `wheels.yml` always builds pyside6-scintilla's wheels
  first and lexilla's tests install those
  (`packages/lexilla/tools/install_pyside6_scintilla.py`), not PyPI's.

`wheels.yml` is `workflow_dispatch`-able for ad-hoc builds and is the
reusable job `publish.yml` calls.

Bundling caveats for pyside6-scintilla's wheels, and the checklist for moving
it to a new PySide6 minor, are in its [build notes](../pyside6-scintilla/build.md).

## Publishing to PyPI

One tag, one package: pushing a tag named `<package>-<version>` publishes
that package at that version.

1. Bump `__version__` in the package's `src/<module>/__init__.py` -- the
   single source of truth for its version
   (`[tool.scikit-build.metadata.version]` reads it via regex). Versions
   follow the vendored upstream release: `X.Y.Z.N`, where `X.Y.Z` is the
   vendored Scintilla (pyside6-scintilla) or Lexilla (lexilla) release and
   `N` increments for binding-only changes against it. Date the package's
   `CHANGELOG.md` section for that version (`## [X.Y.Z.N] - YYYY-MM-DD`).
2. Push the version bump to `master`, and let CI pass.
3. Tag and push: `git tag pyside6-scintilla-5.6.3.10 && git push origin
   pyside6-scintilla-5.6.3.10` (or `lexilla-...`). This triggers
   `.github/workflows/publish.yml`, which checks the tag against
   `__version__`, builds the sdist and all wheels (via `wheels.yml`),
   publishes them to TestPyPI, then to PyPI, and creates the GitHub Release
   with the changelog section as its notes.

Running `publish.yml` by hand (`workflow_dispatch`, choosing the package) is
a dry run: it stops at TestPyPI.

No PyPI API tokens are involved: both publish steps use
[PyPI trusted publishing](https://docs.pypi.org/trusted-publishers/) (GitHub
OIDC), configured per package on test.pypi.org/pypi.org against this repo,
the `publish.yml` workflow and the `testpypi`/`pypi` GitHub environments
(see [TestPyPI](testpypi.md)).

Releases before the monorepo were tagged `v5.6.3.N` (pyside6-scintilla, in
this repo) and `lexilla-5.5.0.N` (lexilla, imported from lexilla-py, where
they were `v5.5.0.N`).
