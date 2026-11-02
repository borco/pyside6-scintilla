# Lexilla build notes

lexilla is built, tested and published with the rest of the workspace -- see
[Building and publishing](../build.md) for the dev environment, CI, wheels
and the release process. This page covers what's specific to lexilla. Paths
are relative to `packages/lexilla/`.

## No Qt SDK

lexilla itself has no Qt dependency: its extension is
[nanobind](https://nanobind.readthedocs.io/) + CMake around the vendored
Lexilla sources (`src/lexilla_vendor/`), so building it alone needs only a
C++17 compiler and uv:

```bash
uv build --package lexilla
```

The workspace dev environment still needs the Qt SDK, because `uv sync`
also builds pyside6-scintilla (which lexilla's glue module and tests use).

## Scintilla headers

lexilla compiles against three Scintilla headers (`ILexer.h`,
`Sci_Position.h`, `Scintilla.h`), kept in `src/scintilla_interface/`. It
keeps its own copy rather than including pyside6-scintilla's vendored tree
because its sdist must build on its own (an sdist contains only its package
directory). `tools/sync_scintilla_headers.py` (repo root) keeps the copy
byte-identical to the vendored Scintilla: `make sync-headers` after vendoring
a new Scintilla release, `--check` in `make lint` and CI.

## Wheels

One `cp312-abi3` wheel per platform (`wheel.py-api = "cp312"`;
`STABLE_ABI` in `src/lexilla/bindings/CMakeLists.txt`), forward-compatible
with later Python versions without a rebuild. nanobind's stable ABI needs
CPython 3.12, hence `requires-python >= 3.12` -- Python 3.11 support (a
separate `cp311` wheel per platform) ended with the move into the monorepo;
lexilla 5.5.0.1 remains available for 3.11.

There's no Qt/PySide6 ABI to keep consistent and no external library to
bundle -- the default delocate/auditwheel/delvewheel repair behavior in
cibuildwheel needs no overrides. The wheel tests need pyside6-scintilla, which
`.github/workflows/wheels.yml` provides from the same run
(`tools/install_pyside6_scintilla.py`).

## Generated files

- `src/lexilla/_lexilla.pyi`: `make lexilla-stubs` (nanobind's stubgen),
  after rebuilding, whenever `_binding.cpp` changes the public API.
- `src/lexilla/_languages.py` and the matching enum in `_binding.cpp`:
  `make lexilla-enums` (`tools/generate_language_enums.py`), after
  re-vendoring Lexilla -- see [Verifying vendored Lexilla](auditing.md).

## Versioning

`X.Y.Z.N`, where `X.Y.Z` is the vendored Lexilla release and `N` increments
for binding-only changes against it. Releases are tagged `lexilla-X.Y.Z.N`.
