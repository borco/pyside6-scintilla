# Scintilla API

Scintilla's message API, adapted from upstream's
[ScintillaDoc.html](../scintilla-original/ScintillaDoc.html) and grouped by
topic. Every `SCI_*` message here is available two ways:

- raw, through `ScintillaEditBase.send()`/`sends()`/`sendr()`, exactly as
  Scintilla documents it;
- typed, as a `ScintillaEdit` method named after the message (`SCI_SETTEXT` →
  `setText()`), with text as `str`, colours as `QColor`, and length/buffer
  arguments handled for you. Each method's docstring names its message and
  any difference -- see the [Reference](../../reference/scintilla/index.md).

| Topic | Covers |
| --- | --- |
| Editing | text retrieval and modification, undo/redo, cut/copy/paste, overtype |
| Selection & Search | selection, multiple selection and virtual space, searching |
| Display | margins, markers, indicators, folding, annotations, wrapping, ... |
| Styling & Lexing | styles, lexers (see [Lexilla](../lexilla/index.md)) |
| Interaction & Commands | keyboard commands, key bindings, popups, macros |
| Documents | multiple views, document pointers |
| Notifications | the signals/`notify` events Scintilla emits |
| Appendix / Reference | deprecated, provisional and removed features |
