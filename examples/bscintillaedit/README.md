# bscintillaedit

A small, portable, single-file `BScintillaEdit(QScrollArea)` widget that's a
**drop-in replacement** for the old, now-archived `bscintillaedit` PyPI
package's widget of the same name (see
[Project mission](../../docs/mission.md)). Copy
[`bscintillaedit.py`](bscintillaedit.py) straight into your own project — it
has no dependencies beyond `pyside6-scintilla` itself.

## Porting from the old `bscintillaedit` package

1. Copy `bscintillaedit.py` into your project.
2. Change `from bscintillaedit import BScintillaEdit` to
   `from .bscintillaedit import BScintillaEdit` (or wherever you placed it).
3. That's it. Same base class, properties, signals, slots, and spelling —
   and the same out-of-the-box defaults (LF line endings, hidden symbol
   margin, styled line-number margin, "↩" end-of-line glyph) as the old
   widget — so existing code keeps working unchanged.

`BScintillaEdit` wraps a `ScintillaEdit` (exposed as `.editor`), so every
typed `ScintillaEdit`/`ScintillaEditBase` method (~780 `SCI_*` messages) is
available via `.editor` — useful for anything not covered by the properties
below.

## API reference

The first five properties (and `clear()`) are the old widget's API,
unchanged — all four boolean toggles there default to `False`, matching the
old widget exactly. `blockEditEnabled` is new, additive functionality not
present in the old widget.

| Property | Type | Default | Signal | Setter slot |
| --- | --- | --- | --- | --- |
| `lineEndVisible` | `bool` | `False` | `lineEndVisibleChanged(bool)` | `setLineEndVisible(bool)` |
| `lineNumbersVisible` | `bool` | `False` | `lineNumbersVisibleChanged(bool)` | `setLineNumbersVisible(bool)` |
| `lineWrapped` | `bool` | `False` | `lineWrappedChanged(bool)` | `setLineWrapped(bool)` |
| `readOnly` | `bool` | `False` | `readOnlyChanged(bool)` | `setReadOnly(bool)` |
| `text` | `str` | `""` | `textChanged(str)` | `setText(str)` |
| `blockEditEnabled` | `bool` | `False` | `blockEditEnabledChanged(bool)` | `setBlockEditEnabled(bool)` |

- `lineEndVisible` — show end-of-line characters as a visible glyph (the
  default glyph is "↩"; pick a different one with
  `.editor.setRepresentation("\n", glyph)`).
- `lineNumbersVisible` — show or hide the line-number margin. The margin
  width is recalculated to fit the current line count each time it's shown.
- `lineWrapped` — wrap long lines at whitespace instead of scrolling
  horizontally.
- `readOnly` — reject further edits.
- `text` — the editor's full contents, kept in sync with `textChanged` on
  every edit.
- `clear()` — slot, equivalent to `setText("")`.
- `blockEditEnabled` — enable block (rectangular) selection and block
  editing: Alt+drag or Alt+Shift+Arrow makes a rectangular selection, and
  typing then edits every selected line at once.

`main.py` additionally turns `lineNumbersVisible` on for a nicer
out-of-the-box look — `BScintillaEdit` itself defaults to it being off, like
the old widget.

## Efficiently syncing multiple editors / a preview pane

The old widget's `text`/`textChanged` round-trip (decode the whole buffer to
a `str` on every keystroke, re-`setText()` it into another widget) doesn't
scale well for keeping editors in sync. Two patterns — using only methods
already available on `.editor`, no `BScintillaEdit` API additions:

- **`BScintillaEdit` ↔ `BScintillaEdit` live mirroring**: share the
  underlying document instead of copying text —
  `editor_b.editor.setDocPointer(editor_a.editor.docPointer())`. Both views
  then share one document and undo history; edits in either appear in both
  instantly with zero string marshalling, and each view keeps its own
  cursor/scroll position.
- **`BScintillaEdit` → non-Scintilla widget** (e.g. a `QTextBrowser` HTML
  preview that can't share a Scintilla document): connect to `textChanged`,
  but debounce the expensive re-render/re-parse on the receiving end with a
  short single-shot `QTimer` rather than running it on every keystroke.

`BScintillaEdit.text`/`textChanged` itself is also cheaper than the old
widget's: the full-buffer read only happens when `textChanged` has at least
one connected receiver, so it costs nothing when nothing is listening.

## Running

From the repo root, after `uv sync`:

```bash
uv run python examples/bscintillaedit/main.py
```

The demo's toolbar toggles each boolean property, plus menus for picking the
end-of-line representation glyph and colour (visible once "Show EOL" is on).
`setRepresentation()` resets a representation's colour to Scintilla's plain
default, so the demo re-applies the last-picked colour whenever the glyph
changes; pick "Default" from the "EOL Colour" menu to restore
`BScintillaEdit`'s own default colour.

## Screenshots

![BScintillaEdit example](../../docs/assets/images/examples/bscintillaedit.png)
