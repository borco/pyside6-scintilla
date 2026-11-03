# pyside6-scintilla build notes

pyside6-scintilla is built, tested and published with the rest of the
workspace -- see [Building and publishing](../development/build.md) for the
dev environment, CI, wheels and the release process, and
[How the packages are built](../development/architecture.md) for how it
differs from lexilla. This page covers what's specific to pyside6-scintilla.
Paths are relative to `packages/pyside6-scintilla/` unless they start at the
repo root.

## Faster C++/binding-only iteration

For changes to `CMakeLists.txt`, `bindings.xml`, or the binding glue, `uv
sync --reinstall-package` does a clean rebuild every time. The
`scintilla-configure`/`-build`/`-install` Make targets are faster for repeated
iteration: they reuse an incremental CMake build tree
(`packages/pyside6-scintilla/build/venv/`) and, via the `venv` preset's
`CMAKE_INSTALL_PREFIX`, drop the rebuilt extension and shared libs directly
into `packages/pyside6-scintilla/src/pyside6_scintilla/`, where `import
pyside6_scintilla` picks them up immediately.

```bash
make scintilla-configure   # once, to set up the build tree
make scintilla-install     # rebuild + drop the extension into src/
```

**Windows**: the `venv` preset uses the Ninja generator, which needs
`cl.exe` on `PATH` -- run these from an **x64 Native Tools Command Prompt
for VS 2022** (or call `vcvarsall.bat x64` first). `uv sync` doesn't need
this, since scikit-build-core uses the Visual Studio generator, which
locates MSVC itself.

## Platform-specific bundling caveats

`Qt6Core5Compat` is required by `scintilla_qt` but isn't bundled in the
PySide6 wheel on any platform. `bindings/CMakeLists.txt` installs it
alongside the extension for all three platforms (a flat `.dll`/`.so` on
Windows/Linux, a framework bundle on macOS), and each platform's
`repair-wheel-command` (`delvewheel`/`auditwheel`/`delocate`) excludes the
Qt/PySide6/shiboken6 libraries provided at runtime by the installed PySide6
package. See [Bindings architecture](bindings.md) issue 3 for the details and history.

## Bumping the PySide6 minor

Each pyside6-scintilla release is built for one PySide6 minor (issue #15):
shiboken6/PySide6's C++ ABI changes between minors, so a wheel built against
6.11 fails to import with 6.12. Moving to a new minor (`6.X`) means a new
release with all of these updated together:

1. `packages/pyside6-scintilla/pyproject.toml`
   - `[build-system].requires`: `shiboken6-generator`, `shiboken6`,
     `PySide6-Essentials` -> `>=6.X,<6.(X+1)`.
   - `[project].dependencies`: `PySide6-Essentials`, `shiboken6` -> same.
   - `[tool.cibuildwheel]`: the Qt version in every `before-all` (aqtinstall)
     and `CMAKE_PREFIX_PATH` (Linux x86_64, Linux aarch64, macOS); the
     manylinux image if PySide6's own wheel tag moved; the macOS
     `MACOSX_DEPLOYMENT_TARGET` if PySide6's macOS wheel tag moved; and the
     Linux auditwheel excludes `libpyside6.abi3.so.6.X` /
     `libshiboken6.abi3.so.6.X` (the soname carries the minor -- a stale
     exclude silently bundles a second copy of PySide6's libraries) and the
     `libicu*` version the Qt SDK ships.
2. The root `pyproject.toml`'s dev group: `shiboken6-generator` -> same.
3. `.github/actions/setup/action.yml`: the Qt `version:` (the one place CI
   names it).
4. `uv lock` (then `uv sync --reinstall-package pyside6-scintilla`, run the
   tests, and `make scintilla-stubs` in case genpyi's output changed).
5. The Qt SDK version mentioned in this file's examples, and the
   installation note in `packages/pyside6-scintilla/README.md`/`docs/index.md`.
6. `packages/pyside6-scintilla/CHANGELOG.md`: a breaking "requires PySide6
   6.X" entry, and a new `__version__`.

Then check the built wheel in a fresh venv: it must import beside the new
minor's newest patch release, and pip must refuse to install it beside the
previous minor.
