# Changelog

All notable changes to this project are documented in this file, one entry
per release. Format loosely follows [Keep a
Changelog](https://keepachangelog.com/en/1.0.0/); entries are kept high-level
(what shipped, breaking changes) rather than a full commit-by-commit log —
see git history for that.

## [Unreleased]

### Changed (breaking)

- A strict, consistent text/bytes API (#16). Text -- document text, names,
  display strings -- is `str` in and out, encoded with the document's
  encoding (UTF-8 by default; the matching codec for other code pages).
  Raw data -- style bytes, images, the raw `sends` -- is bytes in, and
  `QByteArray` out. Nothing is converted implicitly: passing bytes to a text
  method, or `str` to a bytes one, raises `TypeError`.

  | Before | Now |
  | --- | --- |
  | `editor.getText(n).data().decode()` | `editor.getText()` |
  | `editor.getText(n).data()` (for the raw bytes) | `editor.getBytes()` / `getBytes(start, end)` -- the document's stored bytes, undecoded |
  | `doc.get_char_range(...)` (for the raw bytes) | `doc.get_byte_range(...)` |
  | `editor.getLine(i)`, `getSelText()`, `textRange(a, b)`, `styleFont(s)`, ... returned `QByteArray` | return `str` |
  | `editor.addText(len(b), s)`, `appendText`, `replaceTarget`, `searchInTarget`, `copyText`, ... | `editor.addText(s)` -- the byte length is computed from the encoded text |
  | `editor.setStylingEx(n, styles)`, `addStyledText(n, cells)` | `editor.setStylingEx(styles)` -- bytes, length computed |
  | `editor.getCurLine(n)` returned the line | `editor.getCurLine()` returns `(line, caret)` |
  | `base.sends(msg, w, "text")` | `base.sends(msg, w, b"text")` -- bytes only |
  | `editor.TextReturner(msg, w)` | `base.sendr(msg, w)` (also on `ScintillaEditBase`) |
  | `doc.insert_string(pos, b"...")`, `doc.get_char_range(...)` returned bytes | `str` in and out; `doc.style_at()` returns an `int` |
  | `modified` signals' `text` was `QByteArray` | `str` |
  | `targetAsUTF8()`/`encodedFromUTF8()` (always empty on Qt) | removed |

  Positions and lengths elsewhere are still Scintilla's byte offsets. Each
  method's docstring names the `SCI_*` message it sends and how its signature
  differs from it.

### Fixed

- A wrong argument type raised `NameError: name '_pyside6_scintilla' is not
  defined` from shiboken's error reporting instead of a `TypeError`.
- `getText(n)`/`getCurLine(n)` padded their result with NULs.
- `setText`/`insertText`/`replaceSel` silently cut text off at an embedded
  NUL character; they now keep it.
- The type stub claimed text methods accepted `bytes | bytearray |
  memoryview`; it now matches the runtime exactly.
- `ScintillaEdit` is generated from the vendored `Scintilla.iface` again
  (upstream's generated copy was about 40 messages behind), adding e.g.
  `undoActionText`, `selectionSerialized`, `replaceTargetMinimal` and
  `copySeparator`.
- `macroRecord`/`command` signal parameters were truncated to 32 bits on
  Windows.

## [5.6.3.7] - 2026-07-28

### Changed

- Depends on `PySide6-Essentials` instead of the `PySide6` meta-package,
  which required `PySide6-Addons` as well -- ~175 MB (compressed) of
  modules these bindings never import, 205 MB unpacked of it a full
  Chromium in `Qt6WebEngineCore`. Essentials provides the whole `PySide6`
  import namespace, including `py.typed` and the `.pyi` stubs, so nothing
  changes for code importing `PySide6.QtCore`/`QtGui`/`QtWidgets`.

Not breaking for this library's own API, but a fresh install no longer
brings Qt WebEngine, Qt3D, QtCharts and the other add-ons along with it:
if your code imports one of those, depend on `PySide6` or
`PySide6-Addons` explicitly.

## [5.6.3.6] - 2026-07-14

### Changed

- A single `cp311-abi3` wheel per platform instead of one per Python
  version (`cp311`/`cp312`/`cp313`/`cp314`) -- the extension now compiles
  against Python's limited API (shiboken6's `FORCE_LIMITED_API`), the same
  approach PySide6's own wheels use. 5 wheels per release instead of 20.

No breaking changes.

## [5.6.3.5] - 2026-07-14

### Added

- Linux aarch64 wheels, built via cibuildwheel's `manylinux_aarch64` target
  (Qt installed through aqtinstall's `linux_arm64` host).

No breaking changes.

## [5.6.3.4] - 2026-06-27

### Added

- All 74 Scintilla enum classes now bound (previously 11), each with
  class- and member-level docstrings sourced from `ScintillaDoc.html`, for
  IDE hover docs.
- New example: `lexilla_highlighting`, using lexilla-py's `set_lexer()`
  glue and runtime style-name resolution (`Lexer.named_styles()`/
  `name_of_style()`).

No breaking changes.

## [5.6.3.3] - 2026-06-19

### Fixed

- `modified`-style signals carrying `Scintilla::Position`/enum-typed
  parameters (e.g. `modified`) never reached connected Python slots on
  `ScintillaEditBase`/`ScintillaEdit`.
- `Unknown` types in the generated `.pyi` stub for `ScintillaEdit.get_doc()`,
  `setText()`, `getText()`, etc., caused by an unresolvable self-import in
  the stub generator.

### Added

- pyright added to CI to catch typing regressions.
- Typed `Scintilla.<Name>` namespace constants (`InvalidPosition`, `CpUtf8`,
  `MarkerMax`, etc.) with docstrings.
- New examples: `bscintillaedit`, `pygments_highlighting`,
  `tree_sitter_highlighting`.

No breaking changes.

## [5.6.3.2] - 2026-06-14

### Added

- `ScintillaEdit`, a typed per-message wrapper over `ScintillaEditBase`
  (~780 methods generated from `Scintilla.iface`).
- `ScintillaDocument`, wrapping Scintilla's shared/refcounted document
  buffer for multi-view editing.
- New example: `examples/simple_scintilla_edit/`.
- Full `.pyi` stub docstrings for `ScintillaEdit`, `ScintillaDocument`, and
  `ScintillaEditBase`.

No breaking changes to `ScintillaEditBase`'s existing API.

## [5.6.3.1] - 2026-06-13

Docs-only release: corrects the PyPI README to reflect that pre-built
wheels are published.

## [5.6.3.0] - 2026-06-13

First published release: `ScintillaEditBase` binding with pre-built wheels
for Linux (x86_64), Windows (x86_64), and macOS (arm64, x86_64), Python
3.11-3.14.
