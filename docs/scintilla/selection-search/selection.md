# Selection [:material-link-variant:](../../scintilla-original/ScintillaDoc.html#Selection "Upstream documentation"){ .heading-link }

> [!NOTE]
> This page is adapted from the upstream Scintilla **5.6.3** documentation
> (`ScintillaDoc.html`), converted to Markdown for this site. It documents
> the underlying `ScintillaEditBase.send`/`sends` message API -- see the
> [API reference](../../reference/index.md) for the Python bindings themselves.

Scintilla maintains a selection that stretches between two points, the anchor and the current position. If the anchor and the current position are the same, there is no selected text. Positions in the document range from 0 (before the first character), to the document size (after the last character). If you use messages, there is nothing to stop you setting a position that is in the middle of a CRLF pair, or in the middle of a 2 byte character. However, keyboard commands will not move the caret into such positions.

- [`SCI_SETSEL(position anchor, position caret)`](#SCI_SETSEL)
- [`SCI_GOTOPOS(position caret)`](#SCI_GOTOPOS)
- [`SCI_GOTOLINE(line line)`](#SCI_GOTOLINE)
- [`SCI_SETCURRENTPOS(position caret)`](#SCI_SETCURRENTPOS)
- [`SCI_GETCURRENTPOS → position`](#SCI_GETCURRENTPOS)
- [`SCI_SETANCHOR(position anchor)`](#SCI_SETANCHOR)
- [`SCI_GETANCHOR → position`](#SCI_GETANCHOR)
- [`SCI_SETSELECTIONSTART(position anchor)`](#SCI_SETSELECTIONSTART)
- [`SCI_GETSELECTIONSTART → position`](#SCI_GETSELECTIONSTART)
- [`SCI_SETSELECTIONEND(position caret)`](#SCI_SETSELECTIONEND)
- [`SCI_GETSELECTIONEND → position`](#SCI_GETSELECTIONEND)
- [`SCI_SETEMPTYSELECTION(position caret)`](#SCI_SETEMPTYSELECTION)
- [`SCI_SELECTALL`](#SCI_SELECTALL)
- [`SCI_HIDESELECTION(bool hide)`](#SCI_HIDESELECTION)
- [`SCI_GETSELECTIONHIDDEN → bool`](#SCI_GETSELECTIONHIDDEN)
- [`SCI_GETSELTEXT(<unused>, char *text) → position`](#SCI_GETSELTEXT)
- [`SCI_GETCURLINE(position length, char *text) → position`](#SCI_GETCURLINE)
- [`SCI_SELECTIONISRECTANGLE → bool`](#SCI_SELECTIONISRECTANGLE)
- [`SCI_SETSELECTIONMODE(int selectionMode)`](#SCI_SETSELECTIONMODE)
- [`SCI_CHANGESELECTIONMODE(int selectionMode)`](#SCI_CHANGESELECTIONMODE)
- [`SCI_GETSELECTIONMODE → int`](#SCI_GETSELECTIONMODE)
- [`SCI_SETMOVEEXTENDSSELECTION(bool moveExtendsSelection)`](#SCI_SETMOVEEXTENDSSELECTION)
- [`SCI_GETMOVEEXTENDSSELECTION → bool`](#SCI_GETMOVEEXTENDSSELECTION)
- [`SCI_GETLINESELSTARTPOSITION(line line) → position`](#SCI_GETLINESELSTARTPOSITION)
- [`SCI_GETLINESELENDPOSITION(line line) → position`](#SCI_GETLINESELENDPOSITION)
- [`SCI_MOVECARETINSIDEVIEW`](#SCI_MOVECARETINSIDEVIEW)
- [`SCI_CHOOSECARETX`](#SCI_CHOOSECARETX)
- [`SCI_MOVESELECTEDLINESUP`](#SCI_MOVESELECTEDLINESUP)
- [`SCI_MOVESELECTEDLINESDOWN`](#SCI_MOVESELECTEDLINESDOWN)
- [`SCI_SETMOUSESELECTIONRECTANGULARSWITCH(bool mouseSelectionRectangularSwitch)`](#SCI_SETMOUSESELECTIONRECTANGULARSWITCH)
- [`SCI_GETMOUSESELECTIONRECTANGULARSWITCH → bool`](#SCI_GETMOUSESELECTIONRECTANGULARSWITCH)

### `SCI_SETSEL(position anchor, position caret)` {: #SCI_SETSEL }

This message sets both the anchor and the current position. If `caret` is negative, it means the end of the document. If `anchor` is negative, it means remove any selection (i.e. set the anchor to the same position as `caret`). The caret is scrolled into view after this operation.

### `SCI_GOTOPOS(position caret)` {: #SCI_GOTOPOS }

This removes any selection, sets the caret at `caret` and scrolls the view to make the caret visible, if necessary. It is equivalent to `SCI_SETSEL(caret, caret)`. The anchor position is set the same as the current position.

### `SCI_GOTOLINE(line line)` {: #SCI_GOTOLINE }

This removes any selection and sets the caret at the start of line number `line` and scrolls the view (if needed) to make it visible. The anchor position is set the same as the current position. If `line` is outside the lines in the document (first line is 0), the line set is the first or last.

### `SCI_SETCURRENTPOS(position caret)` {: #SCI_SETCURRENTPOS }

This sets the current position and creates a selection between the anchor and the current position. The caret is not scrolled into view.

See also: `SCI_SCROLLCARET`

### `SCI_GETCURRENTPOS → position` {: #SCI_GETCURRENTPOS }

This returns the current position.

### `SCI_SETANCHOR(position anchor)` {: #SCI_SETANCHOR }

This sets the anchor position and creates a selection between the anchor position and the current position. The caret is not scrolled into view.

See also: `SCI_SCROLLCARET`

### `SCI_GETANCHOR → position` {: #SCI_GETANCHOR }

This returns the current anchor position.

### `SCI_SETSELECTIONSTART(position anchor)` {: #SCI_SETSELECTIONSTART }

### `SCI_SETSELECTIONEND(position caret)` {: #SCI_SETSELECTIONEND }

These set the selection based on the assumption that the anchor position is less than the current position. They do not make the caret visible. The table shows the positions of the anchor and the current position after using these messages.

| New value for | anchor | caret |
| --- | --- | --- |
| `SCI_SETSELECTIONSTART` | `anchor` | `Max(anchor, current)` |
| `SCI_SETSELECTIONEND` | `Min(anchor, caret)` | `caret` |

See also: `SCI_SCROLLCARET`

### `SCI_GETSELECTIONSTART → position` {: #SCI_GETSELECTIONSTART }

### `SCI_GETSELECTIONEND → position` {: #SCI_GETSELECTIONEND }

These return the start and end of the selection without regard to which end is the current position and which is the anchor. `SCI_GETSELECTIONSTART` returns the smaller of the current position or the anchor position. `SCI_GETSELECTIONEND` returns the larger of the two values.

### `SCI_SETEMPTYSELECTION(position caret)` {: #SCI_SETEMPTYSELECTION }

This removes any selection and sets the caret at `caret`. The caret is not scrolled into view.

### `SCI_SELECTALL` {: #SCI_SELECTALL }

This selects all the text in the document. The current position is not scrolled into view.

### `SCI_HIDESELECTION(bool hide)` {: #SCI_HIDESELECTION }

### `SCI_GETSELECTIONHIDDEN → bool` {: #SCI_GETSELECTIONHIDDEN }

The normal state is to make the selection visible by drawing it as set by `SCI_SETSELFORE`, `SCI_SETSELBACK`, and related calls. However, if you hide the selection, it is drawn as normal text.

### `SCI_GETSELTEXT(<unused>, char *text NUL-terminated) → position` {: #SCI_GETSELTEXT }

This copies the currently selected text and a terminating NUL(0) byte to the `text` buffer. The buffer size should be determined by calling with a NULL pointer for the `text` argument: `1 + SCI_GETSELTEXT(0, NULL)`. This allows for rectangular and discontiguous selections as well as simple selections. See Multiple Selection for information on how multiple and rectangular selections and virtual space are copied.

See also: [`SCI_GETCURLINE`](#SCI_GETCURLINE), `SCI_GETLINE`, `SCI_GETTEXT`, `SCI_GETSTYLEDTEXT`, `SCI_GETTEXTRANGE`

### `SCI_GETCURLINE(position length, char *text NUL-terminated) → position` {: #SCI_GETCURLINE }

This retrieves the text of the line containing the caret and returns the position within the line of the caret. Pass in `char* text` pointing at a buffer large enough to hold the text you wish to retrieve and a terminating NUL(0) character. Set `length` to the length of the buffer not including the terminating NUL character. If the text argument is NULL(0) then the length that should be allocated to store the entire current line is returned.

See also: [`SCI_GETSELTEXT`](#SCI_GETSELTEXT), `SCI_GETLINE`, `SCI_GETTEXT`, `SCI_GETSTYLEDTEXT`, `SCI_GETTEXTRANGE`

### `SCI_SELECTIONISRECTANGLE → bool` {: #SCI_SELECTIONISRECTANGLE }

This returns 1 if the current selection is in rectangle mode, 0 if not.

### `SCI_SETSELECTIONMODE(int selectionMode)` {: #SCI_SETSELECTIONMODE }

### `SCI_CHANGESELECTIONMODE(int selectionMode)` {: #SCI_CHANGESELECTIONMODE }

### `SCI_GETSELECTIONMODE → int` {: #SCI_GETSELECTIONMODE }

The functions set, change, and get the selection mode, which can be stream (`SC_SEL_STREAM`=0) or rectangular (`SC_SEL_RECTANGLE`=1) or by lines (`SC_SEL_LINES`=2) or thin rectangular (`SC_SEL_THIN`=3). When `SCI_SETSELECTIONMODE` sets these modes, regular caret moves will extend or reduce the selection, until the mode is cancelled by a call with same value, or with `SCI_CANCEL`, or with `SCI_SETMOVEEXTENDSSELECTION`. `SCI_CHANGESELECTIONMODE` sets the mode but does not make regular caret moves extend or reduce the selection.

The get function returns the current mode even if the selection was made by mouse or with regular extended moves. `SC_SEL_THIN` is the mode after a rectangular selection has been typed into and ensures that no characters are selected.

### `SCI_SETMOVEEXTENDSSELECTION(bool moveExtendsSelection)` {: #SCI_SETMOVEEXTENDSSELECTION }

### `SCI_GETMOVEEXTENDSSELECTION → bool` {: #SCI_GETMOVEEXTENDSSELECTION }

This controls whether regular caret moves extends the selection leaving the anchor unchanged. It is 1 if regular caret moves will extend or reduce the selection, 0 if not. `SCI_SETSELECTIONMODE` toggles this setting between on and off.

### `SCI_GETLINESELSTARTPOSITION(line line) → position` {: #SCI_GETLINESELSTARTPOSITION }

### `SCI_GETLINESELENDPOSITION(line line) → position` {: #SCI_GETLINESELENDPOSITION }

Retrieve the position of the start and end of the selection at the given line with `INVALID_POSITION` returned if no selection on this line.

### `SCI_MOVECARETINSIDEVIEW` {: #SCI_MOVECARETINSIDEVIEW }

If the caret is off the top or bottom of the view, it is moved to the nearest line that is visible to its current position. Any selection is lost.

### `SCI_CHOOSECARETX` {: #SCI_CHOOSECARETX }

Scintilla remembers the x value of the last position horizontally moved to explicitly by the user and this value is then used when moving vertically such as by using the up and down keys. This message sets the current x position of the caret as the remembered value.

### `SCI_MOVESELECTEDLINESUP` {: #SCI_MOVESELECTEDLINESUP }

Move the selected lines up one line, shifting the line above after the selection. The selection will be automatically extended to the beginning of the selection's first line and the end of the selection's last line. If nothing was selected, the line the cursor is currently at will be selected.

### `SCI_MOVESELECTEDLINESDOWN` {: #SCI_MOVESELECTEDLINESDOWN }

Move the selected lines down one line, shifting the line below before the selection. The selection will be automatically extended to the beginning of the selection's first line and the end of the selection's last line. If nothing was selected, the line the cursor is currently at will be selected.

### `SCI_SETMOUSESELECTIONRECTANGULARSWITCH(bool mouseSelectionRectangularSwitch)` {: #SCI_SETMOUSESELECTIONRECTANGULARSWITCH }

### `SCI_GETMOUSESELECTIONRECTANGULARSWITCH → bool` {: #SCI_GETMOUSESELECTIONRECTANGULARSWITCH }

Enable or disable the ability to switch to rectangular selection mode while making a selection with the mouse. When this option is turned on, mouse selections in stream mode can be switched to rectangular mode by pressing the corresponding modifier key. They then stick to rectangular mode even when the modifier key is released again. When this option is turned off, mouse selections will always stick to the mode the selection was started in. It is off by default.
