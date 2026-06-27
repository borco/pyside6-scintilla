# Examples

Standalone example apps for `pyside6-scintilla`. These are development aids,
not part of the published package (see `[tool.scikit-build]` in
`pyproject.toml`).

Run from the repo root after `uv sync`:

```
uv run python examples/<example>/main.py
```

## Basic

### [`simple_scintilla_base_edit`](simple_scintilla_base_edit/)

`QMainWindow` with a `ScintillaEditBase` central widget, a toolbar button to
show/hide the line-number margin, and block (rectangular) selection / block
editing enabled.

### [`simple_scintilla_edit`](simple_scintilla_edit/)

`QMainWindow` with a `ScintillaEdit` central widget, using its typed,
per-message API (e.g. `setText()`, `lineCount()`, `gotoLine()`) instead of
`ScintillaEditBase`'s raw `send`/`sends` messages. Has a toolbar button to
show/hide the line-number margin and a "Go to Line" action.

### [`bscintillaedit`](bscintillaedit/)

A small, portable, single-file `BScintillaEdit(QScrollArea)` widget that's a
drop-in replacement for the old, now-archived `bscintillaedit` PyPI
package's widget of the same name, meant to be copied into your own
project.

## Highlighting

### [`pygments_highlighting`](highlighting/pygments_highlighting/)

`QMainWindow` with a `ScintillaEdit` central widget showing Python syntax
highlighting driven by a [Pygments](https://pygments.org/) lexer, with
styling applied manually via raw `SCI_STYLE*` messages (no lexer binding
required). The reusable highlighter lives in `pygments_highlighter.py`,
copyable into your own project.

### [`tree_sitter_highlighting`](highlighting/tree_sitter_highlighting/)

`QMainWindow` with a `ScintillaEdit` central widget showing Python syntax
highlighting *and* code folding, both driven by a
[tree-sitter](https://tree-sitter.github.io/tree-sitter/) grammar — styling
applied manually via raw `SCI_STYLE*` messages and a highlight query,
folding via `setFoldLevel()` and the tree's `block` nodes (no lexer binding
required for either). The reusable highlighter lives in
`tree_sitter_highlighter.py`, copyable into your own project.

### [`lexilla_highlighting`](highlighting/lexilla_highlighting/)

`QMainWindow` with a `ScintillaEdit` central widget showing real C++ syntax
highlighting and folding driven by a
[lexilla](https://github.com/borco/lexilla-py)-created `"cpp"` lexer, wired
in via `setILexer()` (`SCI_SETILEXER`) — unlike the `pygments_highlighting`/
`tree_sitter_highlighting` examples above, no per-edit re-tokenizing glue
code is needed once the lexer is attached, since Scintilla calls its
`Lex()`/`Fold()` itself.
