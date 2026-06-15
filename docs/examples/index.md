# Examples

Standalone example apps demonstrating `pyside6_scintilla`. Each one lives
under [`examples/`](https://github.com/borco/pyside6-scintilla/tree/master/examples)
in the repository and can be run directly after `uv sync`:

```bash
uv run python examples/<example>/main.py
```

<div class="grid cards" markdown>

-   :material-form-textbox:{ .lg .middle } __Simple ScintillaEditBase edit__

    ---

    A minimal `QMainWindow` built around `ScintillaEditBase`, with a
    line-number margin toggle and block (rectangular) selection/editing.

    [:octicons-arrow-right-24: More](simple_scintilla_base_edit.md)

-   :material-form-textbox:{ .lg .middle } __Simple ScintillaEdit edit__

    ---

    A minimal `QMainWindow` built around `ScintillaEdit`'s typed methods,
    with a line-number margin toggle, "Go to Line", and block (rectangular)
    selection/editing.

    [:octicons-arrow-right-24: More](simple_scintilla_edit.md)

-   :material-form-textbox:{ .lg .middle } __BScintillaEdit drop-in replacement__

    ---

    A small, portable, single-file `BScintillaEdit(QScrollArea)` widget that's
    a drop-in replacement for the old, now-archived `bscintillaedit` PyPI
    package's widget of the same name, meant to be copied into your own
    project.

    [:octicons-arrow-right-24: More](bscintillaedit.md)

</div>
