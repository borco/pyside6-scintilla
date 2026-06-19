# tree_sitter_highlighting

A minimal `QMainWindow` with a `ScintillaEdit` central widget, showing Python
syntax highlighting *and* code folding driven by
[tree-sitter](https://tree-sitter.github.io/tree-sitter/) — `pyside6-
scintilla` doesn't wrap a lexer binding, so there's no `SCI_SETLEXER` to
flip on. Instead, [`tree_sitter_highlighter.py`](tree_sitter_highlighter.py)
parses the editor's text with a tree-sitter `Language` (here,
`tree-sitter-python`) on every edit and:

- runs a highlight `Query` over the resulting tree and applies the captured
  node ranges manually via `ScintillaEdit`'s raw `SCI_STYLE*` messages
  (`styleSetFore()`, `startStyling()`, `setStyling()`, ...);
- walks the tree's `block` nodes (the indented body of any compound
  statement) to compute each line's fold level and applies it via
  `setFoldLevel()` — the same message a real lexer would drive folding
  with, wired to a standard "boxes" fold margin.

Both re-run on every edit via the editor's document's `modified` signal
(see Limitations below for why the document's, not the editor's, signal).

`tree_sitter_highlighter.py` has no dependencies beyond `pyside6-scintilla`,
`tree-sitter` and a tree-sitter language package — copy it straight into
your own project, same as [`bscintillaedit.py`](../../bscintillaedit/).
`main.py` itself stays a thin PySide6 app shell, and owns the
hand-written highlight query (`HIGHLIGHTS_QUERY`) for Python, since the
query is grammar-specific and not part of the reusable highlighter.

## Limitations

`TreeSitterHighlighter.rehighlight()` re-parses and re-queries the *whole*
buffer on every edit. That's fine at example/small-file scale, but won't
scale to large files — a production version would use tree-sitter's
incremental parsing (`Parser.parse(..., old_tree=...)`) and restyle/refold
only the changed range.

`HIGHLIGHTS_QUERY` is a small, hand-written query covering keywords,
strings, numbers, comments, function/class names, and calls — not the full
capture set you'd get from a real grammar's `highlights.scm` (e.g. from
[nvim-treesitter](https://github.com/nvim-treesitter/nvim-treesitter)).
Anything not captured falls back to the default style.

Folding is keyed off the Python grammar's `block` node alone (any indented
compound-statement body) — good enough for `if`/`for`/`while`/`def`/`class`/
etc., but a grammar with other foldable constructs (e.g. multi-line
collections, import groups) would need more node types in `fold_levels()`.

`ScintillaEdit.modified`'s `Scintilla::Position`/`Scintilla::FoldLevel`-typed
parameters can't be marshalled to a Python slot — `TreeSitterHighlighter`
connects to `editor.get_doc().modified` instead, which carries the same
notification with plain-int parameters (same workaround as
[`bscintillaedit.py`](../../bscintillaedit/)).

## Running

From the repo root, after `uv sync`:

```bash
uv run python examples/highlighting/tree_sitter_highlighting/main.py
```

`tree-sitter` and `tree-sitter-python` are dev-only dependencies of this
repo (in the `dev` dependency group in `pyproject.toml`) used solely for
this example — they are not dependencies of the `pyside6-scintilla` package
itself.

## Screenshots

![tree-sitter syntax highlighting](../../../docs/assets/images/examples/tree_sitter_highlighting.png)
