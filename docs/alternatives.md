# Alternatives & Landscape

A look at how `pyside6-scintilla` compares to Monaco-based Qt bindings (e.g.
`qtmonaco`), and at other widgets/recipes that cover the two features most
often asked about: **line numbers** and **block (rectangular/column) edit**.

This is a snapshot (June 2026) for orientation, not a commitment to match
feature-for-feature with anything listed here — see
[Project mission](mission.md) for this project's actual scope.

## TL;DR

| | `pyside6-scintilla` (Scintilla) | `qtmonaco` / `monaco-qt` (Monaco) |
| --- | --- | --- |
| Editor core | Native C++ (Scintilla), HPND | Monaco/VS Code editor (TypeScript), MIT, run inside Chromium |
| Qt integration | `QWidget` via shiboken6, direct `SCI_*` messages | `QWebEngineView` + JS bridge (`QWebChannel`) |
| Runtime weight | A few MB; no extra process | Chromium renderer process(es) via Qt WebEngine — typically +100-200MB RSS |
| Wheel/install size | Small (Scintilla + glue) | Large (bundles Qt WebEngine + Monaco's web assets) |
| API style | Typed per-message Python API (`ScintillaEdit`) or raw `send`/`sends` (`ScintillaEditBase`) | Python wrapper around a JS API, calls marshalled over `QWebChannel` |
| Line numbers | Built in (`SCI_SETMARGINWIDTHN`, etc.) | Built in (Monaco default) |
| Block/column edit | Built in (`SCI_SETMOUSESELECTIONRECTANGULARSWITCH`, multiple selection + virtual space) | Alt+Shift+drag column selection + multi-cursor (Monaco default) |
| LSP / IntelliSense | Not provided — bring your own | Built-in LSP client (e.g. `pylsp`) |
| Platforms | Linux, Windows, macOS (per `docs/mission.md`) | macOS and Linux only (per `qtmonaco` README, no Windows) |
| License | MIT (binding) + HPND (Scintilla) | BSD-3-Clause (binding) + MIT (Monaco), but pulls in Qt WebEngine (Chromium, BSD-ish but huge) |

## Monaco-based bindings (`qtmonaco`, `monaco-qt`)

[`bec-project/qtmonaco`](https://github.com/bec-project/qtmonaco) embeds the
[Monaco Editor](https://microsoft.github.io/monaco-editor/) — the editor that
powers VS Code — into PySide6/PyQt6 apps via `QWebEngineView`. It's a
successor to [`DaelonSuzuka/monaco-qt`](https://github.com/DaelonSuzuka/monaco-qt).

### Architecture & stack

- Editor itself is **TypeScript** (Monaco, built with Vite), running inside a
  Chromium instance provided by **Qt WebEngine**.
- Python side is a thin `QWebEngineView` subclass; calls into the editor go
  over `QWebChannel`/JS evaluation, not direct C++ calls.
- Depends on `PySide6-Addons`/`PySide6-Essentials` with `QtWebEngineWidgets`,
  which is a much larger dependency than plain `PySide6`.

### Features

- Syntax highlighting for 80+ languages, code folding, find/replace,
  minimap, command palette, theming (`vs`, `vs-dark`, `hc-black`).
- Built-in LSP client (e.g. Python via `pylsp`), multiple cursors, column
  (box) selection via Alt+Shift+drag — this covers "block edit" out of the
  box.
- Line numbers, by default.

### Memory footprint & install size

Embedding `QtWebEngineWidgets` pulls in a full Chromium renderer. Reports
from the Qt forums put the *added* cost at roughly +100-200MB RSS just for
linking/using `QtWebEngine`, before Monaco itself loads any content, plus
multiple helper `QtWebEngineProcess` processes per view. Wheel size is
correspondingly large (Qt WebEngine wheels are commonly 100MB+), versus this
project's wheels which only need to bundle Scintilla + the shiboken6 glue.

### Ease of use

- **Pro**: if your users already expect a VS Code-like editing experience
  (multi-cursor, command palette, LSP-backed completion), Monaco gives you
  that essentially for free.
- **Con**: the Python API is a wrapper around a web API — features map to JS
  calls marshalled across a process boundary, rather than a typed
  per-message Python API. Debugging spans Python, the `QWebChannel` bridge,
  and the embedded JS/TS bundle.
- **Con**: no Windows support per the `qtmonaco` README (Linux/macOS only),
  vs. this project's Linux + Windows + macOS wheel matrix.

### License

`qtmonaco`/`monaco-qt` are BSD-3-Clause, and Monaco itself is MIT — both
permissive, same spirit as this project. The practical cost isn't the
license, it's the Chromium dependency pulled in via Qt WebEngine.

## `pyside6-scintilla` (recap)

See [Project mission](mission.md) for the full background. In short: a
native `QWidget` binding of Scintilla (HPND), MIT-licensed, no extra runtime
beyond Qt + Scintilla itself, with both a raw message API
(`ScintillaEditBase`) and a typed per-message API (`ScintillaEdit`). Line
numbers and block/column edit are both native Scintilla features, already
demonstrated in the [examples gallery](examples/index.md).

## Other widgets offering line numbers + block edit

A non-exhaustive list of other options that provide **both** line numbers and
some form of block/rectangular/column edit, for context:

| Widget | Stack | License | Block edit? | Notes |
| --- | --- | --- | --- | --- |
| [QScintilla](https://riverbankcomputing.com/software/qscintilla/) | C++/Qt, Scintilla-based | GPLv3 or commercial | Yes (same Scintilla feature) | The PyQt-only predecessor this project avoids depending on |
| [Monaco](https://microsoft.github.io/monaco-editor/) (via `qtmonaco`/`monaco-qt`, or any `QWebEngineView`) | TypeScript + Chromium | MIT (+ Chromium) | Yes — Alt+Shift+drag column selection, multi-cursor | See above |
| [Ace Editor](https://ace.c9.io/) (via `QWebEngineView`) | JavaScript + Chromium | BSD | Yes — rectangular/block selection built in | Same Chromium-weight tradeoff as Monaco |
| [CodeMirror 6](https://codemirror.net/) (via `QWebEngineView`) | JavaScript + Chromium | MIT | Via `@codemirror/rectangular-selection` extension | Same Chromium-weight tradeoff |
| [KTextEditor](https://api.kde.org/frameworks/ktexteditor/html/index.html) (Kate's editor component) | C++/KDE Frameworks | LGPL | Yes — Kate has had block selection for years | Pulls in KDE Frameworks; LGPL is more permissive than QScintilla's GPL but still copyleft, and the dependency footprint is heavy for a non-KDE app |
| [qutepart](https://github.com/andreikop/qutepart) / [qutepart-cpp](https://github.com/diegoiast/qutepart-cpp) | `QPlainTextEdit`-based, Python/C++ | MIT-ish | Block/rectangular selection is part of its feature set | Reuses Kate syntax/indent definitions without the KDE dependency; closest "permissive, native Qt" alternative to Scintilla, but far less mature/battle-tested |

Of these, **KTextEditor** and **qutepart(-cpp)** are the only other
native-Qt (non-Chromium) options. Both are viable, but neither matches
Scintilla's combination of permissive license, maturity, and lack of a
heavyweight framework dependency (KDE Frameworks for KTextEditor).

## Doing it with plain Qt alone (no third-party widget)

### Line numbers: yes, well-trodden

Qt's own [Code Editor
Example](https://doc.qt.io/qt-6/qtwidgets-widgets-codeeditor-example.html)
is the standard recipe: subclass `QPlainTextEdit`, keep a small sibling
`LineNumberArea` widget, reserve space for it via
`setViewportMargins()`/`QPlainTextEdit::extraSelections`, and repaint the
numbers in response to `blockCountChanged`/`updateRequest`/`resizeEvent`.
This is a few dozen lines of boilerplate and is reproduced in countless
tutorials — there's no reason to reach for a third-party widget for line
numbers alone.

### Block/column edit: no, not built in

`QPlainTextEdit`/`QTextEdit` have **no built-in concept of rectangular or
column selection/editing**. `QTextCursor` is fundamentally a pair of linear
character offsets into the document — there's no API for "select column 4-8
on lines 10-20" as a first-class selection.

To approximate it with plain Qt you'd need to build it yourself:

- Track a rectangular region (start/end line + column) separately from
  `QTextCursor`'s linear selection.
- Render it via multiple `QTextEdit::ExtraSelection`s (one per line) so it
  *looks* like a block selection.
- Intercept key events (typed characters, Delete/Backspace, paste) and apply
  the edit to every line in the tracked region via a sequence of
  `QTextCursor` operations wrapped in a single `QTextCursor::beginEditBlock`/
  `endEditBlock` (for one-shot undo).
- Handle the ragged-right-edge case (lines shorter than the rectangle) —
  Scintilla's answer to this is "virtual space"
  (`SC_MARGIN_*`/`SCI_SETVIRTUALSPACEOPTIONS`,  see
  [Multiple Selection and Virtual Space](scintilla/selection-search/multiple-selection-and-virtual-space.md)),
  which has no Qt equivalent and would need to be reimplemented.

This is exactly the kind of feature where reaching for an editor component
that already has it (Scintilla, KTextEditor, qutepart, or a Chromium-based
editor) is cheaper than reimplementing it on `QPlainTextEdit` — block edit is
a small feature to *describe* but a fiddly one to get right (caret rendering,
undo grouping, virtual space, interaction with word-wrap), which is part of
why this project exists rather than wrapping `QPlainTextEdit`.
