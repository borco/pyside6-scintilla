# lexilla_highlighting

A minimal `QMainWindow` with a `ScintillaEdit` central widget, showing real
C++ syntax highlighting driven by a
[lexilla](https://github.com/borco/lexilla-py)-created `"cpp"` lexer — the
cross-binding pointer path described in lexilla-py's
[docs/specs/mission.md](https://github.com/borco/lexilla-py/blob/master/docs/specs/mission.md#cross-binding-integration-raw-pointer-with-an-optional-convenience-extra)
"Cross-binding integration" decision:

```python
lexer = create_lexer(Language.CPP)
editor.setILexer(lexer.detach())
```

`detach()` hands the lexer's `ILexer5*` to Scintilla via `SCI_SETILEXER`
(`setILexer()`), which takes ownership from there — the `Lexer` wrapper must
not be used again afterwards. Once wired up, Scintilla calls the lexer's
`Lex()`/`Fold()` itself whenever it needs to (re)style text, so — unlike
this repo's own `pygments_highlighting`/`tree_sitter_highlighting` examples,
which re-tokenize on every edit because pyside6-scintilla has no lexer of
its own — no per-edit glue code is needed here.

This example still sets the *colors* per style number itself
(`styleSetFore()`), and the keyword word list (`setKeyWords()`) — the lexer
only assigns style numbers (`SCE_C_*`, from Lexilla's own `SciLexer.h`) to
ranges of text, the same way SciTE's properties files do for any other
Scintilla-based editor.

## Folding

Setting the lexer's `"fold"` property to `"1"` before `detach()` makes
`Fold()` compute fold levels alongside `Lex()`'s styling — click the boxed
+/- markers in the left margin (`class`/function bodies in `SAMPLE_TEXT`) to
collapse/expand them. `setAutomaticFold(Scintilla.AutomaticFold.Click)`
handles the margin click itself; no signal/slot code needed.

The marker symbols (`Scintilla.MarkerSymbol.BoxPlus`/`BoxMinus`/...) and the
margin-click flag (`Scintilla.AutomaticFold.Click`) use this repo's real
typed enums. The `SCE_C_*` style numbers above don't have an equivalent yet
— they're Lexilla's own, and lexilla-py doesn't bind them
([borco/lexilla-py#8](https://github.com/borco/lexilla-py/issues/8)).

## Running

From the repo root, after `uv sync`:

```bash
uv run python examples/highlighting/lexilla_highlighting/main.py
```

`lexilla` is a dev dependency of this repo (used solely for this example) —
it is not a dependency of the `pyside6-scintilla` package itself. It's
installed straight from GitHub since it isn't published on PyPI yet (see
[../../README.md](../../README.md) for the resync note this implies).
