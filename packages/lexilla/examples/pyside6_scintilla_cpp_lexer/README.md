# pyside6_scintilla_cpp_lexer

A minimal `QMainWindow` with a
[pyside6-scintilla](https://github.com/borco/pyside6-scintilla) `ScintillaEdit`
central widget, showing real C++ syntax highlighting driven by a
`lexilla`-created `"cpp"` lexer — the cross-binding pointer path described in
[docs/specs/mission.md](../../docs/specs/mission.md)'s "Cross-binding
integration" decision:

```python
lexer = create_lexer(Language.CPP)
editor.setILexer(lexer.detach())
```

`detach()` hands the lexer's `ILexer5*` to Scintilla via `SCI_SETILEXER`
(`setILexer()`), which takes ownership from there — the `Lexer` wrapper must
not be used again afterwards. Once wired up, Scintilla calls the lexer's
`Lex()`/`Fold()` itself whenever it needs to (re)style text, so — unlike
pyside6-scintilla's own `pygments_highlighting`/`tree_sitter_highlighting`
examples, which re-tokenize on every edit because pyside6-scintilla has no
lexer of its own — no per-edit glue code is needed here.

This example still sets the *colors* per style number itself
(`styleSetFore()`), and the keyword word list (`setKeyWords()`) — the lexer
only assigns style numbers (`SCE_C_*`, from Lexilla's own `SciLexer.h`) to
ranges of text, the same way SciTE's properties files do for any other
Scintilla-based editor.

## Folding

Setting the lexer's `"fold"` property to `"1"` before `detach()` makes
`Fold()` compute fold levels alongside `Lex()`'s styling — click the arrow
markers in the left margin (`class`/function bodies in `SAMPLE_TEXT`) to
collapse/expand them. `setAutomaticFold(SC_AUTOMATICFOLD_CLICK)` handles the
margin click itself; no signal/slot code needed.

The marker symbols (`SC_MARK_ARROW`/`SC_MARK_ARROWDOWN`) and the
margin-click flag (`SC_AUTOMATICFOLD_CLICK`) are hardcoded the same way the
`SCE_C_*` style numbers are — pyside6-scintilla's `Scintilla.iface` declares
these as enums (`MarkerSymbol`, `AutomaticFold`, etc.), but they aren't
exposed in the generated bindings yet
([borco/pyside6-scintilla#1](https://github.com/borco/pyside6-scintilla/issues/1)).

## Running

From the repo root, after `uv sync`:

```bash
uv run python examples/pyside6_scintilla_cpp_lexer/main.py
```

`pyside6-scintilla` is a dev dependency of this repo (used solely for this
example) — it is not a dependency of the `lexilla` package itself. Projects
wanting the cross-binding glue at runtime should depend on the
`lexilla[pyside6-scintilla]` extra (see roadmap item 1 for the convenience
helper that extra will add, e.g. `lexer.set_on(editor)`).
