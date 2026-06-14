# Cut, copy and paste [:material-link-variant:](../../scintilla-original/ScintillaDoc.html#CutCopyAndPaste "Upstream documentation"){ .heading-link }

!!! note
    This page is adapted from the upstream Scintilla **5.6.3** documentation
    (`ScintillaDoc.html`), converted to Markdown for this site. It documents
    the underlying `ScintillaEditBase.send`/`sends` message API -- see the
    [API reference](../../reference/index.md) for the Python bindings themselves.

- [`SCI_CUT`](#SCI_CUT)
- [`SCI_COPY`](#SCI_COPY)
- [`SCI_PASTE`](#SCI_PASTE)
- [`SCI_CLEAR`](#SCI_CLEAR)
- [`SCI_CANPASTE → bool`](#SCI_CANPASTE)
- [`SCI_COPYRANGE(position start, position end)`](#SCI_COPYRANGE)
- [`SCI_COPYTEXT(position length, const char *text)`](#SCI_COPYTEXT)
- [`SCI_COPYALLOWLINE`](#SCI_COPYALLOWLINE)
- [`SCI_CUTALLOWLINE`](#SCI_CUTALLOWLINE)
- [`SCI_SETPASTECONVERTENDINGS(bool convert)`](#SCI_SETPASTECONVERTENDINGS)
- [`SCI_GETPASTECONVERTENDINGS → bool`](#SCI_GETPASTECONVERTENDINGS)
- [`SCI_SETCOPYSEPARATOR(<unused>, const char *separator)`](#SCI_SETCOPYSEPARATOR)
- [`SCI_GETCOPYSEPARATOR(<unused>, char *separator) → int`](#SCI_GETCOPYSEPARATOR)
- [`SCI_REPLACERECTANGULAR(position length, const char *text)`](#SCI_REPLACERECTANGULAR)

### `SCI_CUT` {: #SCI_CUT }

### `SCI_COPY` {: #SCI_COPY }

### `SCI_PASTE` {: #SCI_PASTE }

### `SCI_CLEAR` {: #SCI_CLEAR }

### `SCI_CANPASTE → bool` {: #SCI_CANPASTE }

### `SCI_COPYALLOWLINE` {: #SCI_COPYALLOWLINE }

### `SCI_CUTALLOWLINE` {: #SCI_CUTALLOWLINE }

These commands perform the standard tasks of cutting and copying data to the clipboard, pasting from the clipboard into the document, and clearing the document. `SCI_CANPASTE` returns non-zero if the document isn't read-only and if the selection doesn't contain protected text. If you need a "can copy" or "can cut", use `SCI_GETSELECTIONEMPTY()`, which will be zero if there are any non-empty selection ranges implying that a copy or cut to the clipboard should work.

GTK does not really support `SCI_CANPASTE` and always returns `true` unless the document is read-only.

On X, the clipboard is asynchronous and may require several messages between the destination and source applications. Data from `SCI_PASTE` will not arrive in the document immediately.

`SCI_COPYALLOWLINE` works the same as `SCI_COPY` except that if the selection is empty then the current line is copied. On Windows, an extra "MSDEVLineSelect" marker is added to the clipboard which is then used in `SCI_PASTE` to paste the whole line before the current line.

`SCI_CUTALLOWLINE` works the same as `SCI_CUT` except that if the selection is empty then the current line is cut. On Windows, an extra "MSDEVLineSelect" marker is added to the clipboard which is then used in `SCI_PASTE` to paste the whole line before the current line.

### `SCI_COPYRANGE(position start, position end)` {: #SCI_COPYRANGE }

### `SCI_COPYTEXT(position length, const char *text)` {: #SCI_COPYTEXT }

`SCI_COPYRANGE` copies a range of text from the document to the system clipboard and `SCI_COPYTEXT` copies a supplied piece of text to the system clipboard.

### `SCI_SETPASTECONVERTENDINGS(bool convert)` {: #SCI_SETPASTECONVERTENDINGS }

### `SCI_GETPASTECONVERTENDINGS → bool` {: #SCI_GETPASTECONVERTENDINGS }

If this property is set then when text is pasted any line ends are converted to match the document's end of line mode as set with `SCI_SETEOLMODE`. Defaults to true.

### `SCI_SETCOPYSEPARATOR(<unused>, const char *separator)` {: #SCI_SETCOPYSEPARATOR }

### `SCI_GETCOPYSEPARATOR(<unused>, char *separator) → int` {: #SCI_GETCOPYSEPARATOR }

When a multiple selection is copied, this string property is added between each part. Defaults to empty.

### `SCI_REPLACERECTANGULAR(position length, const char *text)` {: #SCI_REPLACERECTANGULAR }

Replaces the selected text or empty selection with the given text. The insertion is performed similarly to rectangular pastes: new lines in the given text are interpreted as moving to the next line without inserting new lines unless at the end of the document.
