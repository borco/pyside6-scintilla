# Information [:material-link-variant:](../../scintilla-original/ScintillaDoc.html#Information "Upstream documentation"){ .heading-link }

> [!NOTE]
> This page is adapted from the upstream Scintilla **5.6.3** documentation
> (`ScintillaDoc.html`), converted to Markdown for this site. It documents
> the underlying `ScintillaEditBase.send`/`sends` message API -- see the
> [API reference](../../reference/index.md) for the Python bindings themselves.

- [`SCI_GETTEXTLENGTH → position`](#SCI_GETTEXTLENGTH)
- [`SCI_GETLENGTH → position`](#SCI_GETLENGTH)
- [`SCI_GETLINECOUNT → line`](#SCI_GETLINECOUNT)
- [`SCI_LINESONSCREEN → line`](#SCI_LINESONSCREEN)
- [`SCI_GETMODIFY → bool`](#SCI_GETMODIFY)
- [`SCI_LINEFROMPOSITION(position pos) → line`](#SCI_LINEFROMPOSITION)
- [`SCI_POSITIONFROMLINE(line line) → position`](#SCI_POSITIONFROMLINE)
- [`SCI_GETLINEENDPOSITION(line line) → position`](#SCI_GETLINEENDPOSITION)
- [`SCI_LINELENGTH(line line) → position`](#SCI_LINELENGTH)
- [`SCI_GETCOLUMN(position pos) → position`](#SCI_GETCOLUMN)
- [`SCI_FINDCOLUMN(line line, position column) → position`](#SCI_FINDCOLUMN)
- [`SCI_POSITIONBEFORE(position pos) → position`](#SCI_POSITIONBEFORE)
- [`SCI_POSITIONAFTER(position pos) → position`](#SCI_POSITIONAFTER)
- [`SCI_TEXTWIDTH(int style, const char *text) → int`](#SCI_TEXTWIDTH)
- [`SCI_TEXTHEIGHT(line line) → int`](#SCI_TEXTHEIGHT)
- [`SCI_POSITIONFROMPOINT(int x, int y) → position`](#SCI_POSITIONFROMPOINT)
- [`SCI_POSITIONFROMPOINTCLOSE(int x, int y) → position`](#SCI_POSITIONFROMPOINTCLOSE)
- [`SCI_CHARPOSITIONFROMPOINT(int x, int y) → position`](#SCI_CHARPOSITIONFROMPOINT)
- [`SCI_CHARPOSITIONFROMPOINTCLOSE(int x, int y) → position`](#SCI_CHARPOSITIONFROMPOINTCLOSE)
- [`SCI_POINTXFROMPOSITION(<unused>, position pos) → int`](#SCI_POINTXFROMPOSITION)
- [`SCI_POINTYFROMPOSITION(<unused>, position pos) → int`](#SCI_POINTYFROMPOSITION)

### `SCI_GETTEXTLENGTH → position` {: #SCI_GETTEXTLENGTH }

### `SCI_GETLENGTH → position` {: #SCI_GETLENGTH }

Both these messages return the length of the document in bytes.

### `SCI_GETLINECOUNT → line` {: #SCI_GETLINECOUNT }

This returns the number of lines in the document. An empty document contains 1 line. A document holding only an end of line sequence has 2 lines.

### `SCI_LINESONSCREEN → line` {: #SCI_LINESONSCREEN }

This returns the number of complete lines visible on the screen. With a constant line height, this is the vertical space available divided by the line separation. Unless you arrange to size your window to an integral number of lines, there may be a partial line visible at the bottom of the view.

### `SCI_GETMODIFY → bool` {: #SCI_GETMODIFY }

This returns non-zero if the document is modified and 0 if it is unmodified. The modified status of a document is determined by the undo position relative to the save point. The save point is set by `SCI_SETSAVEPOINT`, usually when you have saved data to a file.

If you need to be notified when the document becomes modified, Scintilla notifies the container that it has entered or left the save point with the `SCN_SAVEPOINTREACHED` and `SCN_SAVEPOINTLEFT` notification messages.

### `SCI_LINEFROMPOSITION(position pos) → line` {: #SCI_LINEFROMPOSITION }

This message returns the line that contains the position `pos` in the document. The return value is 0 if `pos` <= 0. The return value is the last line if `pos` is beyond the end of the document.

### `SCI_POSITIONFROMLINE(line line) → position` {: #SCI_POSITIONFROMLINE }

This returns the document position that corresponds with the start of the line. If `line` is negative, the position of the line holding the start of the selection is returned. If `line` is greater than the lines in the document, the return value is -1. If `line` is equal to the number of lines in the document (i.e. 1 line past the last line), the return value is the end of the document.

### `SCI_GETLINEENDPOSITION(line line) → position` {: #SCI_GETLINEENDPOSITION }

This returns the position at the end of the line, before any line end characters. If `line` is the last line in the document (which does not have any end of line characters) or greater, the result is the size of the document. If `line` is negative the result is undefined.

### `SCI_LINELENGTH(line line) → position` {: #SCI_LINELENGTH }

This returns the length of the line, including any line end characters. If `line` is negative or beyond the last line in the document, the result is 0. If you want the length of the line not including any end of line characters, use [`SCI_GETLINEENDPOSITION(line)`](#SCI_GETLINEENDPOSITION) - [`SCI_POSITIONFROMLINE(line)`](#SCI_POSITIONFROMLINE).

### `SCI_GETCOLUMN(position pos) → position` {: #SCI_GETCOLUMN }

This message returns the column number of a position `pos` within the document taking the width of tabs into account. This returns the column number of the last tab on the line before `pos`, plus the number of characters between the last tab and `pos`. If there are no tab characters on the line, the return value is the number of characters up to the position on the line. In both cases, double byte characters count as a single character. This is probably only useful with monospaced fonts.

### `SCI_FINDCOLUMN(line line, position column) → position` {: #SCI_FINDCOLUMN }

This message returns the position of a `column` on a `line` taking the width of tabs into account. It treats a multi-byte character as a single column. Column numbers, like lines start at 0.

### `SCI_POSITIONBEFORE(position pos) → position` {: #SCI_POSITIONBEFORE }

### `SCI_POSITIONAFTER(position pos) → position` {: #SCI_POSITIONAFTER }

These messages return the position before and after another position in the document taking into account the current code page. The minimum position returned is 0 and the maximum is the last position in the document. If called with a position within a multi byte character will return the position of the start/end of that character.

### `SCI_TEXTWIDTH(int style, const char *text) → int` {: #SCI_TEXTWIDTH }

This returns the pixel width of a string drawn in the given `style` which can be used, for example, to decide how wide to make the line number margin in order to display a given number of numerals.

### `SCI_TEXTHEIGHT(line line) → int` {: #SCI_TEXTHEIGHT }

This returns the height in pixels of a particular line. Currently all lines are the same height.

### `SCI_POSITIONFROMPOINT(int x, int y) → position` {: #SCI_POSITIONFROMPOINT }

### `SCI_POSITIONFROMPOINTCLOSE(int x, int y) → position` {: #SCI_POSITIONFROMPOINTCLOSE }

`SCI_POSITIONFROMPOINT` finds the closest character position to a point and `SCI_POSITIONFROMPOINTCLOSE` is similar but returns -1 if the point is outside the window or not close to any characters.

### `SCI_CHARPOSITIONFROMPOINT(int x, int y) → position` {: #SCI_CHARPOSITIONFROMPOINT }

### `SCI_CHARPOSITIONFROMPOINTCLOSE(int x, int y) → position` {: #SCI_CHARPOSITIONFROMPOINTCLOSE }

`SCI_CHARPOSITIONFROMPOINT` finds the closest character to a point and `SCI_CHARPOSITIONFROMPOINTCLOSE` is similar but returns -1 if the point is outside the window or not close to any characters. This is similar to the previous methods but finds characters rather than inter-character positions.

### `SCI_POINTXFROMPOSITION(<unused>, position pos) → int` {: #SCI_POINTXFROMPOSITION }

### `SCI_POINTYFROMPOSITION(<unused>, position pos) → int` {: #SCI_POINTYFROMPOSITION }

These messages return the x and y display pixel location of text at position `pos` in the document.

## By character or UTF-16 code unit [:material-link-variant:](../../scintilla-original/ScintillaDoc.html#ByCharacterOrCodeUnit "Upstream documentation"){ .heading-link }

Most Scintilla APIs use byte positions but some applications want to use positions based on counting (UTF-32) characters or (UTF-16) code units or need to communicate with other code written in terms of characters or code units. With only byte positions, this may require examining many bytes to count characters or code units in the document but this may be sped up in some cases by indexing the line starts by character or code unit.

- [`SCI_POSITIONRELATIVE(position pos, position relative) → position`](#SCI_POSITIONRELATIVE)
- [`SCI_POSITIONRELATIVECODEUNITS(position pos, position relative) → position`](#SCI_POSITIONRELATIVECODEUNITS)
- [`SCI_COUNTCHARACTERS(position start, position end) → position`](#SCI_COUNTCHARACTERS)
- [`SCI_COUNTCODEUNITS(position start, position end) → position`](#SCI_COUNTCODEUNITS)
- [`SCI_GETLINECHARACTERINDEX → int`](#SCI_GETLINECHARACTERINDEX)
- [`SCI_ALLOCATELINECHARACTERINDEX(int lineCharacterIndex)`](#SCI_ALLOCATELINECHARACTERINDEX)
- [`SCI_RELEASELINECHARACTERINDEX(int lineCharacterIndex)`](#SCI_RELEASELINECHARACTERINDEX)
- [`SCI_LINEFROMINDEXPOSITION(position pos, int lineCharacterIndex) → line`](#SCI_LINEFROMINDEXPOSITION)
- [`SCI_INDEXPOSITIONFROMLINE(line line, int lineCharacterIndex) → position`](#SCI_INDEXPOSITIONFROMLINE)

### `SCI_POSITIONRELATIVE(position pos, position relative) → position` {: #SCI_POSITIONRELATIVE }

Count a number of whole characters before or after the argument position and return that position. The minimum position returned is 0 and the maximum is the last position in the document. If the position goes past the document end then 0 is returned.

### `SCI_COUNTCHARACTERS(position start, position end) → position` {: #SCI_COUNTCHARACTERS }

Returns the number of whole characters between two positions.

### `SCI_POSITIONRELATIVECODEUNITS(position pos, position relative) → position` {: #SCI_POSITIONRELATIVECODEUNITS }

### `SCI_COUNTCODEUNITS(position start, position end) → position` {: #SCI_COUNTCODEUNITS }

These are the UTF-16 versions of [`SCI_POSITIONRELATIVE`](#SCI_POSITIONRELATIVE) and [`SCI_COUNTCHARACTERS`](#SCI_COUNTCHARACTERS) working in terms of UTF-16 code units.

### `SCI_GETLINECHARACTERINDEX → int` {: #SCI_GETLINECHARACTERINDEX }

Returns which if any indexes are active. It may be `SC_LINECHARACTERINDEX_NONE` (0) or one or more of `SC_LINECHARACTERINDEX_UTF32` (1) if whole characters are indexed or `SC_LINECHARACTERINDEX_UTF16` (2) if UTF-16 code units are indexed. Character indexes are currently only supported for UTF-8 documents.

### `SCI_ALLOCATELINECHARACTERINDEX(int lineCharacterIndex)` {: #SCI_ALLOCATELINECHARACTERINDEX }

### `SCI_RELEASELINECHARACTERINDEX(int lineCharacterIndex)` {: #SCI_RELEASELINECHARACTERINDEX }

Allocate or release one or more indexes using same enumeration as [`SCI_GETLINECHARACTERINDEX`](#SCI_GETLINECHARACTERINDEX). Different aspects of an application may need indexes for different periods and should allocate for those periods. Indexes use additional memory so releasing them can help minimize memory but they also take time to recalculate. Scintilla may also allocate indexes to support features like accessibility or input method editors. Only one index of each type is created for a document at a time.

### `SCI_LINEFROMINDEXPOSITION(position pos, int lineCharacterIndex) → line` {: #SCI_LINEFROMINDEXPOSITION }

### `SCI_INDEXPOSITIONFROMLINE(line line, int lineCharacterIndex) → position` {: #SCI_INDEXPOSITIONFROMLINE }

The document line of a particular character or code unit may be found by calling [`SCI_LINEFROMINDEXPOSITION`](#SCI_LINEFROMINDEXPOSITION) with one of `SC_LINECHARACTERINDEX_UTF32` (1) or `SC_LINECHARACTERINDEX_UTF16` (2). The inverse action, finds the starting position of a document line either in characters or code units from the document start by calling [`SCI_INDEXPOSITIONFROMLINE`](#SCI_INDEXPOSITIONFROMLINE) with the same `lineCharacterIndex` argument.

## Error handling [:material-link-variant:](../../scintilla-original/ScintillaDoc.html#ErrorHandling "Upstream documentation"){ .heading-link }

- [`SCI_SETSTATUS(int status)`](#SCI_SETSTATUS)
- [`SCI_GETSTATUS → int`](#SCI_GETSTATUS)

### `SCI_SETSTATUS(int status)` {: #SCI_SETSTATUS }

### `SCI_GETSTATUS → int` {: #SCI_GETSTATUS }

If an error occurs, Scintilla may set an internal error number that can be retrieved with `SCI_GETSTATUS`. To clear the error status call `SCI_SETSTATUS(0)`. Status values from 1 to 999 are errors and status `SC_STATUS_WARN_START` (1000) and above are warnings. The currently defined statuses are:

|     |      |     |
| :-- | ---- | --- |
| `SC_STATUS_OK` | 0 | No failures |
| `SC_STATUS_FAILURE` | 1 | Generic failure |
| `SC_STATUS_BADALLOC` | 2 | Memory is exhausted |
| `SC_STATUS_OUTSIDE_DOCUMENT` | 3 | An operation was attempted on a position that is outside the document |
| `SC_STATUS_WARN_REGEX` | 1001 | Regular expression is invalid |

To more easily check the status of APIs, applications should call the direct status function using `SCI_GETDIRECTSTATUSFUNCTION`.
