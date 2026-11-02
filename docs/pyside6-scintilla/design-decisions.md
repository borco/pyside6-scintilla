# pyside6-scintilla design decisions

The decisions behind pyside6-scintilla's technical approach. The project's
overall purpose is in the [mission](../development/mission.md); how its
build differs from lexilla's is in
[How the packages are built](../development/architecture.md).

## Technical approach

- **Scintilla** is vendored from a release tarball (not the Mercurial tip),
  pinned to a stable release; updates happen deliberately, when a new
  Scintilla release has been tested -- see
  [Verifying vendored Scintilla](auditing.md).
- **shiboken6** generates the Python ↔ C++ bridge from a typesystem XML file;
  the typed per-message `ScintillaEdit` class is generated from
  `Scintilla.iface` by `tools/generate_scintilla_edit.py` (issue #16).
- **scikit-build-core** drives the CMake build and produces PEP 517 wheels;
  **cibuildwheel** on GitHub Actions builds them for every platform, and
  PyPI trusted publishing (TestPyPI first) uploads them.
- **Versioning** follows the vendored Scintilla: `X.Y.Z.N`, where `X.Y.Z` is
  the Scintilla release and `N` counts binding-only releases against it.
- **PyPI name**: `pyside6-scintilla` (import `pyside6_scintilla`), claimed in
  June 2026.

## Decision log

| Decision | Rationale |
| --- | --- |
| PySide6, not PyQt6 | PySide6 is LGPL; PyQt6 is GPL -- consistent with the permissive goals. |
| shiboken6, not ctypes/cffi | Native Qt integration, proper signal/slot support -- see [How the packages are built](../development/architecture.md#why-shiboken6-for-pyside6-scintilla). |
| GitHub, not GitLab | Unlimited free CI minutes for public repos; GitLab's free tier is 400 min/month. |
| Standalone project, not Scintilla upstream | Scintilla upstream is C++ only, hg-based, unlikely to accept a Python binding. |
| Vendor Scintilla releases, not a git-cinnabar bridge | Simpler, more reproducible, no hg toolchain dependency for contributors. |
| uv for local dev | Fast, modern, handles venvs and tool installs cleanly; the repo is a uv workspace. |
| cibuildwheel | The standard for multi-platform Python native extension wheels. |
| Depend on `PySide6-Essentials`, not the `PySide6` meta-package (issue #14) | The meta-package requires Addons too, so every install pulled ~175 MB (compressed) of modules these bindings never import -- 205 MB unpacked of it a full Chromium in `Qt6WebEngineCore`. Only Core/Gui/Widgets are used, and Core5Compat is vendored into the repaired wheel rather than taken from a PySide6 wheel. Essentials ships the whole `PySide6` import namespace (`__init__.py`, `py.typed`, all `.pyi` stubs) plus the CMake config, typesystems and glue the build needs, so nothing is lost; a consumer wanting an add-on depends on `PySide6` explicitly. |
| Single `cp311-abi3` wheel per platform, not one per Python version (issue #13) | shiboken6's `FORCE_LIMITED_API` compiles the extension against Python's stable ABI, so the same build works on 3.11+ without a rebuild -- the pattern PySide6's own wheels use. Verified by building once against 3.11 and running the full test suite unmodified under 3.11-3.14. |
| One PySide6 minor per release (issue #15) | The extension links shiboken6's/PySide6's C++ libraries, whose ABI changes between minors: an unbounded `>=6.10` let 5.6.3.7 install beside PySide6 6.12 and then fail to import. Each release pins `>=6.X,<6.(X+1)`; patch releases stay compatible. |
| Text is `str`, raw data is bytes, no implicit conversion (issue #16) | Text methods take and return `str`, encoded per the document's encoding; style bytes, images and the raw `sends`/`sendr` are bytes; lengths that only measure the string argument are computed. See [Bindings architecture](bindings.md), issue 5. |
| Colours are `QColor` (issue #17) | Scintilla's packed `0xBBGGRR` ints are the opposite byte order from Qt's; the typed methods take and return `QColor`, the raw `send()` keeps the ints, and `colour_to_scintilla()`/`colour_from_scintilla()` convert. Implicit int → `QColor` conversion (Qt's byte order) is kept, consistent with PySide6. |
| Part of the `scintilla-py` monorepo (issue #19) | Maintained together with lexilla: one CI, one docs site, lexilla always tested against this package's source. |
