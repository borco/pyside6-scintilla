# simple_scintilla_edit

A minimal `QMainWindow` with a `ScintillaEdit` central widget, demonstrating
the typed, per-message API (e.g. `setText()`, `lineCount()`, `gotoLine()`)
instead of `ScintillaEditBase`'s raw `send`/`sends` messages (contrast with
`simple_scintilla_base_edit`):

- a toolbar button that shows/hides the line-number margin
- a "Go to Line" toolbar action

## Running

From the repo root, after `uv sync`:

```bash
uv run python examples/simple_scintilla_edit/main.py
```
