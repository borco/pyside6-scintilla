# Text retrieval and modification

[:material-open-in-new: Upstream documentation](https://www.scintilla.org/ScintillaDoc.html#TextRetrievalAndModification)

!!! note
    This page is adapted from the upstream Scintilla **5.6.3** documentation
    (`ScintillaDoc.html`), converted to Markdown for this site. It documents
    the underlying `ScintillaEditBase.send`/`sends` message API -- see the
    [API reference](../../reference.md) for the Python bindings themselves.

Each byte in a Scintilla document is associated with a byte of styling information. The combination of a character byte and a style byte is called a cell. Style bytes are interpreted an index into an array of styles.

In this document, 'character' normally refers to a byte even when multi-byte characters are used. Lengths measure the numbers of bytes, not the amount of characters in those bytes.

Positions within the Scintilla document refer to a character or the gap before that character. The first character in a document is 0, the second 1 and so on. If a document contains `nLen` characters, the last character is numbered `nLen`-1. The caret exists between character positions and can be located from before the first character (0) to after the last character (`nLen`).

There are places where the caret can not go where two character bytes make up one character. This occurs when a DBCS character from a language like Japanese is included in the document or when line ends are marked with the CP/M standard of a carriage return followed by a line feed. The `INVALID_POSITION` constant (-1) represents an invalid position within the document.

All lines of text in Scintilla are the same height, and this height is calculated from the largest font in any current style. This restriction is for performance; if lines differed in height then calculations involving positioning of text would require the text to be styled first.

- [`SCI_GETTEXT(position length, char *text) → position`](#SCI_GETTEXT)
- [`SCI_SETTEXT(<unused>, const char *text)`](#SCI_SETTEXT)
- [`SCI_SETSAVEPOINT`](#SCI_SETSAVEPOINT)
- [`SCI_GETLINE(line line, char *text) → position`](#SCI_GETLINE)
- [`SCI_REPLACESEL(<unused>, const char *text)`](#SCI_REPLACESEL)
- [`SCI_SETREADONLY(bool readOnly)`](#SCI_SETREADONLY)
- [`SCI_GETREADONLY → bool`](#SCI_GETREADONLY)
- [`SCI_GETDRAGDROPENABLED → bool`](#SCI_GETDRAGDROPENABLED)
- [`SCI_SETDRAGDROPENABLED(bool dragDropEnabled)`](#SCI_SETDRAGDROPENABLED)
- [`SCI_GETTEXTRANGE(<unused>, Sci_TextRange *tr) → position`](#SCI_GETTEXTRANGE)
- [`SCI_GETTEXTRANGEFULL(<unused>, Sci_TextRangeFull *tr) → position`](#SCI_GETTEXTRANGEFULL)
- [`SCI_ALLOCATE(position bytes)`](#SCI_ALLOCATE)
- [`SCI_ALLOCATELINES(line lines)`](#SCI_ALLOCATELINES)
- [`SCI_ADDTEXT(position length, const char *text)`](#SCI_ADDTEXT)
- [`SCI_ADDSTYLEDTEXT(position length, cell *c)`](#SCI_ADDSTYLEDTEXT)
- [`SCI_APPENDTEXT(position length, const char *text)`](#SCI_APPENDTEXT)
- [`SCI_INSERTTEXT(position pos, const char *text)`](#SCI_INSERTTEXT)
- [`SCI_CHANGEINSERTION(position length, const char *text)`](#SCI_CHANGEINSERTION)
- [`SCI_CLEARALL`](#SCI_CLEARALL)
- [`SCI_DELETERANGE(position start, position lengthDelete)`](#SCI_DELETERANGE)
- [`SCI_CLEARDOCUMENTSTYLE`](#SCI_CLEARDOCUMENTSTYLE)
- [`SCI_GETCHARAT(position pos) → int`](#SCI_GETCHARAT)
- [`SCI_GETSTYLEAT(position pos) → int`](#SCI_GETSTYLEAT)
- [`SCI_GETSTYLEINDEXAT(position pos) → int`](#SCI_GETSTYLEINDEXAT)
- [`SCI_GETSTYLEDTEXT(<unused>, Sci_TextRange *tr) → position`](#SCI_GETSTYLEDTEXT)
- [`SCI_GETSTYLEDTEXTFULL(<unused>, Sci_TextRangeFull *tr) → position`](#SCI_GETSTYLEDTEXTFULL)
- [`SCI_RELEASEALLEXTENDEDSTYLES`](#SCI_RELEASEALLEXTENDEDSTYLES)
- [`SCI_ALLOCATEEXTENDEDSTYLES(int numberStyles) → int`](#SCI_ALLOCATEEXTENDEDSTYLES)
- [`SCI_TARGETASUTF8(<unused>, char *s) → position`](#SCI_TARGETASUTF8)
- [`SCI_ENCODEDFROMUTF8(const char *utf8, char *encoded) → position`](#SCI_ENCODEDFROMUTF8)
- [`SCI_SETLENGTHFORENCODE(position bytes)`](#SCI_SETLENGTHFORENCODE)

### `SCI_GETTEXT(position length, char *text NUL-terminated) → position` {: #SCI_GETTEXT }

This returns at most `length` characters of text from the start of the document plus one terminating 0 character. When `length` is beyond document length, it returns document length. To collect all the text in a document, use `SCI_GETLENGTH` to get the number of characters in the document (`nLen`), allocate a character buffer of length `nLen+1` bytes, then call `SCI_GETTEXT(nLen, char *text)`. If the text argument is NULL(0) then the length that should be allocated to store the entire document is returned. If you then save the text, you should use `SCI_SETSAVEPOINT` to mark the text as unmodified.

See also: `SCI_GETSELTEXT`, `SCI_GETCURLINE`, [`SCI_GETLINE`](#SCI_GETLINE), [`SCI_GETSTYLEDTEXT`](#SCI_GETSTYLEDTEXT), [`SCI_GETTEXTRANGE`](#SCI_GETTEXTRANGE)

### `SCI_SETTEXT(<unused>, const char *text)` {: #SCI_SETTEXT }

This replaces all the text in the document with the zero terminated text string you pass in.

### `SCI_SETSAVEPOINT` {: #SCI_SETSAVEPOINT }

This message tells Scintilla that the current state of the document is unmodified. This is usually done when the file is saved or loaded, hence the name "save point". As Scintilla performs undo and redo operations, it notifies the container that it has entered or left the save point with `SCN_SAVEPOINTREACHED` and `SCN_SAVEPOINTLEFT` notification messages, allowing the container to know if the file should be considered dirty or not.

See also: `SCI_EMPTYUNDOBUFFER`, `SCI_GETMODIFY`

### `SCI_GETLINE(line line, char *text) → position` {: #SCI_GETLINE }

This fills the buffer defined by text with the contents of the nominated line (lines start at 0). The buffer is not terminated by a NUL(0) character. It is up to you to make sure that the buffer is long enough for the text, use `SCI_LINELENGTH(line line)`. The returned value is the number of characters copied to the buffer. The returned text includes any end of line characters. If you ask for a line number outside the range of lines in the document, 0 characters are copied. If the text argument is 0 then the length that should be allocated to store the entire line is returned.

See also: `SCI_GETCURLINE`, `SCI_GETSELTEXT`, [`SCI_GETTEXTRANGE`](#SCI_GETTEXTRANGE), [`SCI_GETSTYLEDTEXT`](#SCI_GETSTYLEDTEXT), [`SCI_GETTEXT`](#SCI_GETTEXT)

### `SCI_REPLACESEL(<unused>, const char *text)` {: #SCI_REPLACESEL }

The currently selected text between the anchor and the current position is replaced by the 0 terminated text string. If the anchor and current position are the same, the text is inserted at the caret position. The caret is positioned after the inserted text and the caret is scrolled into view.

### `SCI_SETREADONLY(bool readOnly)` {: #SCI_SETREADONLY }

### `SCI_GETREADONLY → bool` {: #SCI_GETREADONLY }

These messages set and get the read-only flag for the document. If you mark a document as read only, attempts to modify the text cause the `SCN_MODIFYATTEMPTRO` notification.

### `SCI_GETDRAGDROPENABLED → bool` {: #SCI_GETDRAGDROPENABLED }

### `SCI_SETDRAGDROPENABLED(bool dragDropEnabled)` {: #SCI_SETDRAGDROPENABLED }

These messages get and set the flag controlling whether drag-and-drop is enabled or not.

### `SCI_GETTEXTRANGE(<unused>, Sci_TextRange *tr) → position` {: #SCI_GETTEXTRANGE }

### `SCI_GETTEXTRANGEFULL(<unused>, Sci_TextRangeFull *tr) → position` {: #SCI_GETTEXTRANGEFULL }

This collects the text between the positions `cpMin` and `cpMax` and copies it to `lpstrText` (see `struct Sci_TextRange` in `Scintilla.h`). If `cpMax` is -1, text is returned to the end of the document. The text is 0 terminated, so you must supply a buffer that is at least 1 character longer than the number of characters you wish to read. The return value is the length of the returned text not including the terminating 0.

`SCI_GETTEXTRANGEFULL` uses 64-bit positions on all platforms so is safe for documents larger than 2GB. It should always be used in preference to `SCI_GETTEXTRANGE` which will be deprecated in a future release.

See also: `SCI_GETSELTEXT`, [`SCI_GETLINE`](#SCI_GETLINE), `SCI_GETCURLINE`, [`SCI_GETSTYLEDTEXT`](#SCI_GETSTYLEDTEXT), [`SCI_GETTEXT`](#SCI_GETTEXT)

### `SCI_GETSTYLEDTEXT(<unused>, Sci_TextRange *tr) → position` {: #SCI_GETSTYLEDTEXT }

### `SCI_GETSTYLEDTEXTFULL(<unused>, Sci_TextRangeFull *tr) → position` {: #SCI_GETSTYLEDTEXTFULL }

This collects styled text into a buffer using two bytes for each cell, with the character at the lower address of each pair and the style byte at the upper address. Characters between the positions `cpMin` and `cpMax` are copied to `lpstrText` (see `struct Sci_TextRange` and `struct Sci_TextRangeFull` in `Scintilla.h`). Two 0 bytes are added to the end of the text, so the buffer that `lpstrText` points at must be at least `2*(cpMax-cpMin)+2` bytes long. No check is made for sensible values of `cpMin` or `cpMax`. Positions outside the document return character codes and style bytes of 0.

`SCI_GETSTYLEDTEXTFULL` uses 64-bit positions on all platforms so is safe for documents larger than 2GB. It should always be used in preference to `SCI_GETSTYLEDTEXT` which will be deprecated in a future release.

See also: `SCI_GETSELTEXT`, [`SCI_GETLINE`](#SCI_GETLINE), `SCI_GETCURLINE`, [`SCI_GETTEXTRANGE`](#SCI_GETTEXTRANGE), [`SCI_GETTEXT`](#SCI_GETTEXT)

### `SCI_ALLOCATE(position bytes)` {: #SCI_ALLOCATE }

Allocate a document buffer large enough to store a given number of bytes. The document will not be made smaller than its current contents.

### `SCI_ALLOCATELINES(line lines)` {: #SCI_ALLOCATELINES }

Allocate line indices to match the `lines` argument. This is an optimization that can prevent multiple reallocations of the indices as text is inserted if the application can estimate the number of lines in the document. The number of lines will not be reduced by this call.

### `SCI_ADDTEXT(position length, const char *text)` {: #SCI_ADDTEXT }

This inserts the first `length` characters from the string `text` at the current position. This will include any 0's in the string that you might have expected to stop the insert operation. The current position is set at the end of the inserted text, but it is not scrolled into view.

### `SCI_ADDSTYLEDTEXT(position length, cell *c)` {: #SCI_ADDSTYLEDTEXT }

This behaves just like `SCI_ADDTEXT`, but inserts styled text.

### `SCI_APPENDTEXT(position length, const char *text)` {: #SCI_APPENDTEXT }

This adds the first `length` characters from the string `text` to the end of the document. This will include any 0's in the string that you might have expected to stop the operation. The current selection is not changed and the new text is not scrolled into view.

### `SCI_INSERTTEXT(position pos, const char *text)` {: #SCI_INSERTTEXT }

This inserts the zero terminated `text` string at position `pos` or at the current position if `pos` is -1. If the current position is after the insertion point then it is moved along with its surrounding text but no scrolling is performed.

### `SCI_CHANGEINSERTION(position length, const char *text)` {: #SCI_CHANGEINSERTION }

This may only be called from a `SC_MOD_INSERTCHECK` notification handler and will change the text being inserted to that provided.

### `SCI_CLEARALL` {: #SCI_CLEARALL }

Unless the document is read-only, this deletes all the text.

### `SCI_DELETERANGE(position start, position lengthDelete)` {: #SCI_DELETERANGE }

Deletes a range of text in the document.

### `SCI_CLEARDOCUMENTSTYLE` {: #SCI_CLEARDOCUMENTSTYLE }

When wanting to completely restyle the document, for example after choosing a lexer, the `SCI_CLEARDOCUMENTSTYLE` can be used to clear all styling information and reset the folding state.

### `SCI_GETCHARAT(position pos) → int` {: #SCI_GETCHARAT }

This returns the character at `pos` in the document or 0 if `pos` is negative or past the end of the document.

### `SCI_GETSTYLEAT(position pos) → int` {: #SCI_GETSTYLEAT }

### `SCI_GETSTYLEINDEXAT(position pos) → int` {: #SCI_GETSTYLEINDEXAT }

This returns the style at `pos` in the document, or 0 if `pos` is negative or past the end of the document. `SCI_GETSTYLEAT` may return a negative number for styles over 127 whereas `SCI_GETSTYLEINDEXAT` will only return positive numbers. `SCI_GETSTYLEINDEXAT` should be preferred as it handles styles more consistently and may avoid problems with lexers that define more than 128 styles.

### `SCI_RELEASEALLEXTENDEDSTYLES` {: #SCI_RELEASEALLEXTENDEDSTYLES }

### `SCI_ALLOCATEEXTENDEDSTYLES(int numberStyles) → int` {: #SCI_ALLOCATEEXTENDEDSTYLES }

Extended styles are used for features like textual margins and annotations and autocompletion lists as well as internally by Scintilla. They are outside the range 0..255 used for the styles bytes associated with document bytes. These functions manage the use of extended styles to ensures that components cooperate in defining styles. `SCI_RELEASEALLEXTENDEDSTYLES` releases any extended styles allocated by the container. `SCI_ALLOCATEEXTENDEDSTYLES` allocates a range of style numbers after the byte style values and returns the number of the first allocated style. Ranges for margin, annotation, and autocompletion list styles should be allocated before calling `SCI_MARGINSETSTYLEOFFSET` or `SCI_ANNOTATIONSETSTYLEOFFSET` or `SCI_AUTOCSETSTYLE`.

### `Sci_TextRange` {: #Sci_TextRange }

### `Sci_CharacterRange` {: #Sci_CharacterRange }

These structures are defined to be exactly the same shape as the Win32 `TEXTRANGE` and `CHARRANGE`, so that older code that treats Scintilla as a RichEdit will work.

In a future release, these types will be deprecated. [`SCI_GETTEXTRANGEFULL`](#SCI_GETTEXTRANGEFULL), `Sci_TextRangeFull` and `Sci_CharacterRangeFull` should be used instead.

```c
typedef long Sci_PositionCR;

struct Sci_CharacterRange {
    Sci_PositionCR cpMin;
    Sci_PositionCR cpMax;
};

struct Sci_TextRange {
    struct Sci_CharacterRange chrg;
    char *lpstrText;
};
```

### `Sci_TextRangeFull` {: #Sci_TextRangeFull }

### `Sci_CharacterRangeFull` {: #Sci_CharacterRangeFull }

These structures are the same as `Sci_TextRange` and `Sci_CharacterRange` except that positions are always 64-bit in 64-bit builds so will work on documents larger than 2GB.

```c
typedef ptrdiff_t Sci_Position;

struct Sci_CharacterRangeFull {
    Sci_Position cpMin;
    Sci_Position cpMax;
};

struct Sci_TextRangeFull {
    struct Sci_CharacterRangeFull chrg;
    char *lpstrText;
};
```

## Specific to GTK, Cocoa and Windows only: Access to encoded text

[:material-open-in-new: Upstream documentation](https://www.scintilla.org/ScintillaDoc.html#EncodedAccess)

### `SCI_TARGETASUTF8(<unused>, char *s) → position` {: #SCI_TARGETASUTF8 }

This method retrieves the value of the target encoded as UTF-8 which is the default encoding of GTK so is useful for retrieving text for use in other parts of the user interface, such as find and replace dialogs. The length of the encoded text in bytes is returned. Cocoa uses UTF-16 which is easily converted from UTF-8 so this method can be used to perform the more complex work of transcoding from the various encodings supported.

### `SCI_ENCODEDFROMUTF8(const char *utf8, char *encoded) → position` {: #SCI_ENCODEDFROMUTF8 }

### `SCI_SETLENGTHFORENCODE(position bytes)` {: #SCI_SETLENGTHFORENCODE }

`SCI_ENCODEDFROMUTF8` converts a UTF-8 string into the document's encoding which is useful for taking the results of a find dialog, for example, and receiving a string of bytes that can be searched for in the document. Since the text can contain nul bytes, the `SCI_SETLENGTHFORENCODE` method can be used to set the length that will be converted. If set to -1, the length is determined by finding a nul byte. The length of the converted string is returned.