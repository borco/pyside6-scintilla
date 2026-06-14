# Examples

Standalone example apps for `pyside6-scintilla`. These are development aids,
not part of the published package (see `[tool.scikit-build]` in
`pyproject.toml`).

Run from the repo root after `uv sync`:

```
uv run python examples/<example>/main.py
```

## [`simple_scintilla_base_edit`](simple_scintilla_base_edit/)

`QMainWindow` with a `ScintillaEditBase` central widget, a toolbar button to
show/hide the line-number margin, and block (rectangular) selection / block
editing enabled.

## [`simple_scintilla_edit`](simple_scintilla_edit/)

`QMainWindow` with a `ScintillaEdit` central widget, using its typed,
per-message API (e.g. `setText()`, `lineCount()`, `gotoLine()`) instead of
`ScintillaEditBase`'s raw `send`/`sends` messages. Has a toolbar button to
show/hide the line-number margin and a "Go to Line" action.
