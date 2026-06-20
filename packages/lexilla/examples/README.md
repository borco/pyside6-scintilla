# Examples

Standalone example apps for `lexilla`. These are development aids, not part
of the published package (see `[tool.scikit-build]` in `pyproject.toml`).

> [!NOTE]
> No examples yet -- the real `CreateLexer`/`ILexer5` bindings don't exist
> yet (see [docs/specs/roadmap.md](../docs/specs/roadmap.md)). Planned:
>
> - A standalone example creating a lexer and inspecting it directly.
> - An example wiring a created lexer into a
>   [pyside6-scintilla](https://github.com/borco/pyside6-scintilla)
>   `ScintillaEdit` via `SCI_SETILEXER`, once the cross-binding pointer path
>   works.

Once examples exist, run them from the repo root after `uv sync`:

```bash
uv run python examples/<example>/main.py
```
