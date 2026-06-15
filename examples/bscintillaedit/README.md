# bscintillaedit

A small, portable, single-file `BScintillaEdit` convenience subclass of
`ScintillaEdit` — a spiritual successor to the old Windows-only
`bscintillaedit` PyPI package (see `docs/mission.md`), meant to be copied
straight into your own project:

- sets a fixed-width font, as is conventional for a code editor
- shows a line-number margin by default, with `setLineNumbersVisible()` /
  `lineNumbersVisible()` to toggle it

The demo `main.py` shows `BScintillaEdit` used as a `QMainWindow`'s central
widget, with a toolbar button to toggle the line-number margin.

## Running

From the repo root, after `uv sync`:

```bash
uv run python examples/bscintillaedit/main.py
```

## Screenshots

![BScintillaEdit example](../../docs/assets/images/examples/bscintillaedit.png)
