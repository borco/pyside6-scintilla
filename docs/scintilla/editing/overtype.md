# Overtype [:material-link-variant:](../../scintilla-original/ScintillaDoc.html#Overtype "Upstream documentation"){ .heading-link }

!!! note
    This page is adapted from the upstream Scintilla **5.6.3** documentation
    (`ScintillaDoc.html`), converted to Markdown for this site. It documents
    the underlying `ScintillaEditBase.send`/`sends` message API -- see the
    [API reference](../../reference.md) for the Python bindings themselves.

- [`SCI_SETOVERTYPE(bool overType)`](#SCI_SETOVERTYPE)
- [`SCI_GETOVERTYPE → bool`](#SCI_GETOVERTYPE)

### `SCI_SETOVERTYPE(bool overType)` {: #SCI_SETOVERTYPE }

### `SCI_GETOVERTYPE → bool` {: #SCI_GETOVERTYPE }

When overtype is enabled, each typed character replaces the character to the right of the text caret. When overtype is disabled, characters are inserted at the caret. `SCI_GETOVERTYPE` returns `true` (1) if overtyping is active, otherwise `false` (0) will be returned. Use `SCI_SETOVERTYPE` to set the overtype mode.
