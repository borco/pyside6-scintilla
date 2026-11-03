# Changelog

All notable changes to this project are documented in this file, one entry
per release. Format loosely follows [Keep a
Changelog](https://keepachangelog.com/en/1.0.0/); entries are kept high-level
(what shipped, breaking changes) rather than a full commit-by-commit log —
see git history for that.

## [5.6.9.0] - 2026-11-03

### Changed

- Vendors Scintilla 5.6.9, up from 5.6.3 (#23). See
  [ScintillaHistory](https://www.scintilla.org/ScintillaHistory.html) for
  the full list: faster layout and lower memory use, Unicode 17 case
  conversion and character categories, and crash fixes.
- `updateUi` (`SCN_UPDATEUI`) and the styling after an edit now run from a
  posted Qt event rather than inside painting (Scintilla 5.6.5): they arrive
  once the event loop runs, before the next repaint, and also for a widget
  that isn't being painted (e.g. hidden).
- Building from source finds the Qt SDK matching the installed PySide6 by
  itself (#25): it looks for that Qt release in the standard install
  locations (`C:/Qt`, `~/Qt`, `/opt/Qt`) unless `CMAKE_PREFIX_PATH` already
  provides a matching one, and stops with a clear message naming the
  needed Qt version instead of failing inside PySide6's headers.

### Added

- `setScaleTechnique()`/`scaleTechnique()` (`SCI_SETSCALETECHNIQUE`) and the
  `Scintilla.ScaleTechnique` enum. `ScaleTechnique.PixelAligned` aligns
  lines to physical pixels, removing the 'seams' between background
  rectangles under fractional display scaling (e.g. 150%).
- The pixel methods (`setMarginWidthN`, `textWidth`, `pointXFromPosition`,
  ... -- the messages Scintilla now types as `pixels`) take and return
  logical pixels, like upstream's `ScintillaEdit`: under `PixelAligned`,
  where the engine works in device pixels, they convert (rounding), while
  raw `send()` sees device pixels. Each has a `...F` twin (`textWidthF`,
  `setMarginWidthNF`, ...) with unrounded `float` pixels. With the default
  technique nothing changes.
- `Scintilla.Update.Text` and `Update.LineCount` (`SC_UPDATE_TEXT`/
  `SC_UPDATE_LINE_COUNT`) for `updateUi`. With `Update.Text`, the
  notification's `position` (`NotificationData.position`, from the `notify`
  signal) holds the start of the changes.

## [5.6.3.11] - 2026-11-03

### Changed (breaking)

- Built for PySide6 6.12 (#15): requires `PySide6-Essentials>=6.12,<6.13`
  and `shiboken6>=6.12,<6.13`. Keep using 5.6.3.10 with PySide6 6.11 -- pip
  picks the release matching the installed PySide6 minor.
- macOS wheels need macOS 14.4 (tagged `macosx_14_0`, like PySide6 6.12's
  own wheels), up from 13.0: Qt 6.12's `QtCore5Compat.framework`, bundled in
  the wheel, requires it.

### Added

- Python 3.15 classifier (PySide6 6.12 supports it; the `cp311-abi3` wheel
  already ran on it).

## [5.6.3.10] - 2026-11-03

### Changed

- The project moved into the [scintilla-py](https://github.com/borco/scintilla-py)
  monorepo (as `packages/pyside6-scintilla/`), next to lexilla. Docs:
  <https://borco.github.io/scintilla-py/>. Releases are now tagged
  `pyside6-scintilla-<version>`.
- The PyPI project links (homepage, repository, issues) and the README's
  links point to the new locations; 5.6.3.9's docs link 404s since the move.
  No code changes: still built for PySide6 6.11.

## [5.6.3.9] - 2026-11-02

### Changed (breaking)

- Colours are `QColor` (#17). The 45 colour methods -- `styleSetFore`/
  `styleFore`, `styleSetBack`, `markerSetBack`, `setElementColour`,
  `indicSetFore`, `setCaretLineBack`, `setSelBack`, `setRepresentationColour`,
  ... -- used to take and return Scintilla's packed `0xBBGGRR` ints
  (`0xAABBGGRR` for the alpha ones). They now take and return `QColor`
  (anything PySide6 converts to one: `QColor`, `Qt.GlobalColor`, a colour
  name). Plain `colour` messages ignore alpha and read back opaque.

  **Check every colour call:** an `int` is still accepted, because PySide6
  converts it to `QColor` -- but as Qt's `0xRRGGBB` with the alpha byte
  ignored, so old code passing Scintilla's packed ints keeps running with red
  and blue swapped, and the `...Translucent`/element/representation colours
  become opaque. Replace `0xBBGGRR` values with `QColor(r, g, b)` (or `QColor(r, g, b,
  a)`). The raw `send()` still takes Scintilla's packed ints.

### Added

- `colour_to_scintilla()` / `colour_from_scintilla()` (#17): convert between
  a `QColor` (or colour name such as `"#00ff00"`, or `Qt.GlobalColor`) and
  Scintilla's packed `0xBBGGRR` / `0xAABBGGRR` ints, for code using the raw
  `send()`. They reject an `int` argument rather than guess its byte order.

### Fixed

- Linux wheels no longer bundle private copies of `libOpenGL`, `libGLX` and
  `libGLdispatch`. Qt's CMake target linked OpenGL into the extension
  although it never uses it, so auditwheel grafted those libraries into the
  wheel, next to the system ones PySide6 loads, and a locally built wheel
  needed `libopengl0` installed. OpenGL is now kept off the link line.

## [5.6.3.8] - 2026-11-02

### Changed (breaking)

- Requires PySide6 6.11 exactly (`PySide6-Essentials>=6.11,<6.12`, and the
  same for `shiboken6`) (#15). The extension links against shiboken6/PySide6's
  C++ libraries, whose ABI changes between minor releases: 5.6.3.7 and
  earlier declared `>=6.10` with no upper bound, so they installed beside
  PySide6 6.12 and then failed to import ("The specified procedure could not
  be found"). Each PySide6 minor now gets its own release, so pip picks the
  one matching your PySide6 -- once the unpinned 5.6.3.0-5.6.3.7 are yanked
  on PyPI (otherwise pip still falls back to them). 6.12 support follows in
  the next release.

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
  | `NotificationData.text` (raw `notify` signal) was a UTF-8-decoded `str` | `QByteArray`: the raw `length` bytes, in the document's encoding |
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
- `NotificationData.text` raised `UnicodeDecodeError` in non-UTF-8 code pages
  and ignored `length`.

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
