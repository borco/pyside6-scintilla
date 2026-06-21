# Examples

Standalone example apps for `lexilla`. These are development aids, not part
of the published package (see `[tool.scikit-build]` in `pyproject.toml`).

- [pyside6_scintilla_cpp_lexer](pyside6_scintilla_cpp_lexer/): a created
  `"cpp"` lexer wired into a
  [pyside6-scintilla](https://github.com/borco/pyside6-scintilla)
  `ScintillaEdit` via `SCI_SETILEXER`, showing real C++ syntax highlighting.

> [!NOTE]
> Still planned: a standalone example creating a lexer and inspecting it
> directly, with no Scintilla editor involved (see
> [borco/lexilla-py#5](https://github.com/borco/lexilla-py/issues/5)).

Run examples from the repo root after `uv sync`:

```bash
uv run python examples/<example>/main.py
```
