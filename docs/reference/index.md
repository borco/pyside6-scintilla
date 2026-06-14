# API reference

`pyside6_scintilla`'s public API: the `ScintillaEditBase`/`ScintillaEdit`
widgets, `ScintillaDocument`, and the `Scintilla.Message` enum used by
`send`/`sends`.

- [**ScintillaEditBase**](scintilla-edit-base.md) -- the raw widget, exposing
  only `send`/`sends` (and Scintilla's notification signals) for the full
  `SCI_*` message API.
- [**ScintillaEdit**](scintilla-edit.md) -- `ScintillaEditBase` plus a typed
  Python method for every `SCI_*` message (e.g. `setText()`, `textLength()`).
- [**ScintillaDocument**](scintilla-document.md) -- a Scintilla document
  buffer, for sharing one document between multiple `ScintillaEdit` widgets.
- [**Scintilla.Message**](message.md) -- the `SCI_*` message IDs sent via
  `send`/`sends`.
