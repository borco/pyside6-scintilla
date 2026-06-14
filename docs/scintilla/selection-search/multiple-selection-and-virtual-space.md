# Multiple Selection and Virtual Space [:material-link-variant:](../../scintilla-original/ScintillaDoc.html#MultipleSelectionAndVirtualSpace "Upstream documentation"){ .heading-link }

!!! note
    This page is adapted from the upstream Scintilla **5.6.3** documentation
    (`ScintillaDoc.html`), converted to Markdown for this site. It documents
    the underlying `ScintillaEditBase.send`/`sends` message API -- see the
    [API reference](../../reference.md) for the Python bindings themselves.

- [`SCI_SETMULTIPLESELECTION(bool multipleSelection)`](#SCI_SETMULTIPLESELECTION)
- [`SCI_GETMULTIPLESELECTION → bool`](#SCI_GETMULTIPLESELECTION)
- [`SCI_SETADDITIONALSELECTIONTYPING(bool additionalSelectionTyping)`](#SCI_SETADDITIONALSELECTIONTYPING)
- [`SCI_GETADDITIONALSELECTIONTYPING → bool`](#SCI_GETADDITIONALSELECTIONTYPING)
- [`SCI_SETMULTIPASTE(int multiPaste)`](#SCI_SETMULTIPASTE)
- [`SCI_GETMULTIPASTE → int`](#SCI_GETMULTIPASTE)
- [`SCI_SETVIRTUALSPACEOPTIONS(int virtualSpaceOptions)`](#SCI_SETVIRTUALSPACEOPTIONS)
- [`SCI_GETVIRTUALSPACEOPTIONS → int`](#SCI_GETVIRTUALSPACEOPTIONS)
- [`SCI_SETRECTANGULARSELECTIONMODIFIER(int modifier)`](#SCI_SETRECTANGULARSELECTIONMODIFIER)
- [`SCI_GETRECTANGULARSELECTIONMODIFIER → int`](#SCI_GETRECTANGULARSELECTIONMODIFIER)
- [`SCI_GETSELECTIONS → int`](#SCI_GETSELECTIONS)
- [`SCI_GETSELECTIONEMPTY → bool`](#SCI_GETSELECTIONEMPTY)
- [`SCI_CLEARSELECTIONS`](#SCI_CLEARSELECTIONS)
- [`SCI_SETSELECTION(position caret, position anchor)`](#SCI_SETSELECTION)
- [`SCI_ADDSELECTION(position caret, position anchor)`](#SCI_ADDSELECTION)
- [`SCI_SELECTIONFROMPOINT(int x, int y) → int`](#SCI_SELECTIONFROMPOINT)
- [`SCI_DROPSELECTIONN(int selection)`](#SCI_DROPSELECTIONN)
- [`SCI_SETMAINSELECTION(int selection)`](#SCI_SETMAINSELECTION)
- [`SCI_GETMAINSELECTION → int`](#SCI_GETMAINSELECTION)
- [`SCI_SETSELECTIONNCARET(int selection, position caret)`](#SCI_SETSELECTIONNCARET)
- [`SCI_GETSELECTIONNCARET(int selection) → position`](#SCI_GETSELECTIONNCARET)
- [`SCI_SETSELECTIONNCARETVIRTUALSPACE(int selection, position space)`](#SCI_SETSELECTIONNCARETVIRTUALSPACE)
- [`SCI_GETSELECTIONNCARETVIRTUALSPACE(int selection) → position`](#SCI_GETSELECTIONNCARETVIRTUALSPACE)
- [`SCI_SETSELECTIONNANCHOR(int selection, position anchor)`](#SCI_SETSELECTIONNANCHOR)
- [`SCI_GETSELECTIONNANCHOR(int selection) → position`](#SCI_GETSELECTIONNANCHOR)
- [`SCI_SETSELECTIONNANCHORVIRTUALSPACE(int selection, position space)`](#SCI_SETSELECTIONNANCHORVIRTUALSPACE)
- [`SCI_GETSELECTIONNANCHORVIRTUALSPACE(int selection) → position`](#SCI_GETSELECTIONNANCHORVIRTUALSPACE)
- [`SCI_SETSELECTIONNSTART(int selection, position anchor)`](#SCI_SETSELECTIONNSTART)
- [`SCI_GETSELECTIONNSTART(int selection) → position`](#SCI_GETSELECTIONNSTART)
- [`SCI_GETSELECTIONNSTARTVIRTUALSPACE(int selection) → position`](#SCI_GETSELECTIONNSTARTVIRTUALSPACE)
- [`SCI_SETSELECTIONNEND(int selection, position caret)`](#SCI_SETSELECTIONNEND)
- [`SCI_GETSELECTIONNEND(int selection) → position`](#SCI_GETSELECTIONNEND)
- [`SCI_GETSELECTIONNENDVIRTUALSPACE(int selection) → position`](#SCI_GETSELECTIONNENDVIRTUALSPACE)
- [`SCI_SETRECTANGULARSELECTIONCARET(position caret)`](#SCI_SETRECTANGULARSELECTIONCARET)
- [`SCI_GETRECTANGULARSELECTIONCARET → position`](#SCI_GETRECTANGULARSELECTIONCARET)
- [`SCI_SETRECTANGULARSELECTIONCARETVIRTUALSPACE(position space)`](#SCI_SETRECTANGULARSELECTIONCARETVIRTUALSPACE)
- [`SCI_GETRECTANGULARSELECTIONCARETVIRTUALSPACE → position`](#SCI_GETRECTANGULARSELECTIONCARETVIRTUALSPACE)
- [`SCI_SETRECTANGULARSELECTIONANCHOR(position anchor)`](#SCI_SETRECTANGULARSELECTIONANCHOR)
- [`SCI_GETRECTANGULARSELECTIONANCHOR → position`](#SCI_GETRECTANGULARSELECTIONANCHOR)
- [`SCI_SETRECTANGULARSELECTIONANCHORVIRTUALSPACE(position space)`](#SCI_SETRECTANGULARSELECTIONANCHORVIRTUALSPACE)
- [`SCI_GETRECTANGULARSELECTIONANCHORVIRTUALSPACE → position`](#SCI_GETRECTANGULARSELECTIONANCHORVIRTUALSPACE)
- [`SCI_SETSELECTIONSERIALIZED(<unused>, const char *selectionString)`](#SCI_SETSELECTIONSERIALIZED)
- [`SCI_GETSELECTIONSERIALIZED(<unused>, char *selectionString) → position`](#SCI_GETSELECTIONSERIALIZED)
- [`SC_ELEMENT_SELECTION_ADDITIONAL_TEXT : colouralpha`](#SC_ELEMENT_SELECTION_ADDITIONAL_TEXT)
- [`SC_ELEMENT_SELECTION_ADDITIONAL_BACK : colouralpha`](#SC_ELEMENT_SELECTION_ADDITIONAL_BACK)
- [`SCI_SETADDITIONALSELALPHA(alpha alpha)`](#SCI_SETADDITIONALSELALPHA)
- [`SCI_GETADDITIONALSELALPHA → int`](#SCI_GETADDITIONALSELALPHA)
- [`SCI_SETADDITIONALSELFORE(colour fore)`](#SCI_SETADDITIONALSELFORE)
- [`SCI_SETADDITIONALSELBACK(colour back)`](#SCI_SETADDITIONALSELBACK)
- [`SC_ELEMENT_CARET_ADDITIONAL : colouralpha`](#SC_ELEMENT_CARET_ADDITIONAL)
- [`SCI_SETADDITIONALCARETFORE(colour fore)`](#SCI_SETADDITIONALCARETFORE)
- [`SCI_GETADDITIONALCARETFORE → colour`](#SCI_GETADDITIONALCARETFORE)
- [`SCI_SETADDITIONALCARETSBLINK(bool additionalCaretsBlink)`](#SCI_SETADDITIONALCARETSBLINK)
- [`SCI_GETADDITIONALCARETSBLINK → bool`](#SCI_GETADDITIONALCARETSBLINK)
- [`SCI_SETADDITIONALCARETSVISIBLE(bool additionalCaretsVisible)`](#SCI_SETADDITIONALCARETSVISIBLE)
- [`SCI_GETADDITIONALCARETSVISIBLE → bool`](#SCI_GETADDITIONALCARETSVISIBLE)
- [`SCI_SWAPMAINANCHORCARET`](#SCI_SWAPMAINANCHORCARET)
- [`SCI_ROTATESELECTION`](#SCI_ROTATESELECTION)
- [`SCI_MULTIPLESELECTADDNEXT`](#SCI_MULTIPLESELECTADDNEXT)
- [`SCI_MULTIPLESELECTADDEACH`](#SCI_MULTIPLESELECTADDEACH)

There may be multiple selections active at one time. More selections are made by holding down the Ctrl key while dragging with the mouse. The most recent selection is the main selection and determines which part of the document is shown automatically. Any selection apart from the main selection is called an additional selection. The calls in the previous section operate on the main selection. There is always at least one selection. The selection can be simplified down to just the main selection by `SCI_CANCEL` which is normally mapped to the Esc key.

Rectangular selections are handled as multiple selections although the original rectangular range is remembered so that subsequent operations may be handled differently for rectangular selections. For example, pasting a rectangular selection places each piece in a vertical column.

Virtual space is space beyond the end of each line. The caret may be moved into virtual space but no real space will be added to the document until there is some text typed or some other text insertion command is used.

When discontiguous selections are copied to the clipboard, each selection is added to the clipboard text in order with no delimiting characters. For rectangular selections the document's line end is added after each line's text. Rectangular selections are always copied from top line to bottom, not in the in order of selection. Virtual space is not copied.

### `SCI_SETMULTIPLESELECTION(bool multipleSelection)` {: #SCI_SETMULTIPLESELECTION }

### `SCI_GETMULTIPLESELECTION → bool` {: #SCI_GETMULTIPLESELECTION }

Enable or disable multiple selection. When multiple selection is disabled, it is not possible to select multiple ranges by holding down the Ctrl key while dragging with the mouse.

### `SCI_SETADDITIONALSELECTIONTYPING(bool additionalSelectionTyping)` {: #SCI_SETADDITIONALSELECTIONTYPING }

### `SCI_GETADDITIONALSELECTIONTYPING → bool` {: #SCI_GETADDITIONALSELECTIONTYPING }

Whether typing, new line, cursor left/right/up/down, backspace, delete, home, and end work with multiple selections simultaneously. Also allows selection and word and line deletion commands.

### `SCI_SETMULTIPASTE(int multiPaste)` {: #SCI_SETMULTIPASTE }

### `SCI_GETMULTIPASTE → int` {: #SCI_GETMULTIPASTE }

When pasting into multiple selections, the pasted text can go into just the main selection with `SC_MULTIPASTE_ONCE`=0 or into each selection with `SC_MULTIPASTE_EACH`=1. `SC_MULTIPASTE_ONCE` is the default.

### `SCI_SETVIRTUALSPACEOPTIONS(int virtualSpaceOptions)` {: #SCI_SETVIRTUALSPACEOPTIONS }

### `SCI_GETVIRTUALSPACEOPTIONS → int` {: #SCI_GETVIRTUALSPACEOPTIONS }

Virtual space can be enabled or disabled for rectangular selections or in other circumstances or in both. There are three bit flags `SCVS_RECTANGULARSELECTION`=1, `SCVS_USERACCESSIBLE`=2, and `SCVS_NOWRAPLINESTART`=4 which can be set independently. `SCVS_NONE`=0, the default, disables all use of virtual space.

`SCVS_NOWRAPLINESTART` prevents left arrow movement and selection from wrapping to the previous line. This is most commonly desired in conjunction with virtual space but is an independent setting so works without virtual space.

| | | |
| --- | --- | --- |
| `SCVS_NONE` | 0 | The default: no virtual space. |
| `SCVS_RECTANGULARSELECTION` | 1 | Virtual space is enabled for rectangular selections. |
| `SCVS_USERACCESSIBLE` | 2 | Virtual space is enabled for user actions such as right arrow key or clicking beyond line end. |
| `SCVS_NOWRAPLINESTART` | 4 | Left arrow does not wrap to the previous line. |

### `SCI_SETRECTANGULARSELECTIONMODIFIER(int modifier)` {: #SCI_SETRECTANGULARSELECTIONMODIFIER }

### `SCI_GETRECTANGULARSELECTIONMODIFIER → int` {: #SCI_GETRECTANGULARSELECTIONMODIFIER }

On GTK and Qt, the key used to indicate that a rectangular selection should be created when combined with a mouse drag can be set. The three possible values are `SCMOD_CTRL`=2, `SCMOD_ALT`=4 (default) or `SCMOD_SUPER`=8. Since `SCMOD_ALT` may already be used by a window manager, the window manager may need configuring to allow this choice. `SCMOD_SUPER` is often a system dependent modifier key such as the Left Windows key on a Windows keyboard or the Command key on a Mac.

### `SCI_GETSELECTIONS → int` {: #SCI_GETSELECTIONS }

Return the number of selections currently active. There is always at least one selection.

### `SCI_GETSELECTIONEMPTY → bool` {: #SCI_GETSELECTIONEMPTY }

Return 1 if every selected range is empty else 0.

### `SCI_CLEARSELECTIONS` {: #SCI_CLEARSELECTIONS }

Set a single empty selection at 0 as the only selection.

### `SCI_SETSELECTION(position caret, position anchor)` {: #SCI_SETSELECTION }

Set a single selection from `anchor` to `caret` as the only selection.

### `SCI_ADDSELECTION(position caret, position anchor)` {: #SCI_ADDSELECTION }

Add a new selection from `anchor` to `caret` as the main selection retaining all other selections as additional selections. Since there is always at least one selection, to set a list of selections, the first selection should be added with `SCI_SETSELECTION` and later selections added with `SCI_ADDSELECTION`

### `SCI_SELECTIONFROMPOINT(int x, int y) → int` {: #SCI_SELECTIONFROMPOINT }

Return the index of the selection at the point. If there is no selection at the point, return -1. This can be used to drop a selection or make it the main selection.

### `SCI_DROPSELECTIONN(int selection)` {: #SCI_DROPSELECTIONN }

If there are multiple selections, remove the indicated selection. If this was the main selection then make the previous selection the main and if it was the first then the last selection becomes main. If there is only one selection, or there is no selection `selection`, then there is no effect.

### `SCI_SETMAINSELECTION(int selection)` {: #SCI_SETMAINSELECTION }

### `SCI_GETMAINSELECTION → int` {: #SCI_GETMAINSELECTION }

One of the selections is the main selection which is used to determine what range of text is automatically visible. The main selection may be displayed in different colours or with a differently styled caret. Only an already existing selection can be made main.

### `SCI_SETSELECTIONNCARET(int selection, position caret)` {: #SCI_SETSELECTIONNCARET }

### `SCI_GETSELECTIONNCARET(int selection) → position` {: #SCI_GETSELECTIONNCARET }

### `SCI_SETSELECTIONNCARETVIRTUALSPACE(int selection, position space)` {: #SCI_SETSELECTIONNCARETVIRTUALSPACE }

### `SCI_GETSELECTIONNCARETVIRTUALSPACE(int selection) → position` {: #SCI_GETSELECTIONNCARETVIRTUALSPACE }

### `SCI_SETSELECTIONNANCHOR(int selection, position anchor)` {: #SCI_SETSELECTIONNANCHOR }

### `SCI_GETSELECTIONNANCHOR(int selection) → position` {: #SCI_GETSELECTIONNANCHOR }

### `SCI_SETSELECTIONNANCHORVIRTUALSPACE(int selection, position space)` {: #SCI_SETSELECTIONNANCHORVIRTUALSPACE }

### `SCI_GETSELECTIONNANCHORVIRTUALSPACE(int selection) → position` {: #SCI_GETSELECTIONNANCHORVIRTUALSPACE }

Set or query the position and amount of virtual space for the caret and anchor of each already existing selection.

### `SCI_SETSELECTIONNSTART(int selection, position anchor)` {: #SCI_SETSELECTIONNSTART }

### `SCI_GETSELECTIONNSTART(int selection) → position` {: #SCI_GETSELECTIONNSTART }

### `SCI_GETSELECTIONNSTARTVIRTUALSPACE(int selection) → position` {: #SCI_GETSELECTIONNSTARTVIRTUALSPACE }

### `SCI_SETSELECTIONNEND(int selection, position caret)` {: #SCI_SETSELECTIONNEND }

### `SCI_GETSELECTIONNEND(int selection) → position` {: #SCI_GETSELECTIONNEND }

### `SCI_GETSELECTIONNENDVIRTUALSPACE(int selection) → position` {: #SCI_GETSELECTIONNENDVIRTUALSPACE }

Set or query the start and end position of each already existing selection. Query the virtual space at start and end of each selection. Mostly of use to query each range for its text. The `selection` parameter is zero-based.

### `SCI_SETRECTANGULARSELECTIONCARET(position caret)` {: #SCI_SETRECTANGULARSELECTIONCARET }

### `SCI_GETRECTANGULARSELECTIONCARET → position` {: #SCI_GETRECTANGULARSELECTIONCARET }

### `SCI_SETRECTANGULARSELECTIONCARETVIRTUALSPACE(position space)` {: #SCI_SETRECTANGULARSELECTIONCARETVIRTUALSPACE }

### `SCI_GETRECTANGULARSELECTIONCARETVIRTUALSPACE → position` {: #SCI_GETRECTANGULARSELECTIONCARETVIRTUALSPACE }

### `SCI_SETRECTANGULARSELECTIONANCHOR(position anchor)` {: #SCI_SETRECTANGULARSELECTIONANCHOR }

### `SCI_GETRECTANGULARSELECTIONANCHOR → position` {: #SCI_GETRECTANGULARSELECTIONANCHOR }

### `SCI_SETRECTANGULARSELECTIONANCHORVIRTUALSPACE(position space)` {: #SCI_SETRECTANGULARSELECTIONANCHORVIRTUALSPACE }

### `SCI_GETRECTANGULARSELECTIONANCHORVIRTUALSPACE → position` {: #SCI_GETRECTANGULARSELECTIONANCHORVIRTUALSPACE }

Set or query the position and amount of virtual space for the caret and anchor of the rectangular selection. After setting the rectangular selection, this is broken down into multiple selections, one for each line.

### `SCI_SETSELECTIONSERIALIZED(<unused>, const char *selectionString)` {: #SCI_SETSELECTIONSERIALIZED }

### `SCI_GETSELECTIONSERIALIZED(<unused>, char *selectionString) → position` {: #SCI_GETSELECTIONSERIALIZED }

Set or query the selection type and positions as a serialized string. The format of this string may change in future versions so should not be persisted beyond the current session.

The format is currently
`[selType:R|L|T] [# mainRange ,] [anchor [v virtualSpace] [- caret [v virtualSpace]]] [, ...]`
Example of a multiple selection with virtual space: `#1,5v3-2,1`

### `SC_ELEMENT_SELECTION_ADDITIONAL_TEXT : colouralpha` {: #SC_ELEMENT_SELECTION_ADDITIONAL_TEXT }

### `SC_ELEMENT_SELECTION_ADDITIONAL_BACK : colouralpha` {: #SC_ELEMENT_SELECTION_ADDITIONAL_BACK }

### `SCI_SETADDITIONALSELALPHA(alpha alpha)` {: #SCI_SETADDITIONALSELALPHA }

### `SCI_GETADDITIONALSELALPHA → int` {: #SCI_GETADDITIONALSELALPHA }

### `SCI_SETADDITIONALSELFORE(colour fore)` {: #SCI_SETADDITIONALSELFORE }

### `SCI_SETADDITIONALSELBACK(colour back)` {: #SCI_SETADDITIONALSELBACK }

Modify the appearance of additional selections so that they can be differentiated from the main selection which has its appearance set with `SC_ELEMENT_SELECTION_TEXT`, `SC_ELEMENT_SELECTION_BACK`, `SCI_SETSELALPHA`, `SCI_GETSELALPHA`, `SCI_SETSELFORE`, and `SCI_SETSELBACK`. The element APIs are preferred and the following messages discouraged. The additional selection background is drawn on the layer defined for all selection backgrounds by `SCI_SETSELECTIONLAYER`. `SCI_SETADDITIONALSELFORE` and `SCI_SETADDITIONALSELBACK` calls have no effect until `SCI_SETSELFORE` and `SCI_SETSELBACK` are called with `useSetting` value set to true. Subsequent calls to `SCI_SETSELFORE`, and `SCI_SETSELBACK` will overwrite the values set by `SCI_SETADDITIONALSEL*` functions.

### `SC_ELEMENT_CARET_ADDITIONAL : colouralpha` {: #SC_ELEMENT_CARET_ADDITIONAL }

### `SCI_SETADDITIONALCARETFORE(colour fore)` {: #SCI_SETADDITIONALCARETFORE }

### `SCI_GETADDITIONALCARETFORE → colour` {: #SCI_GETADDITIONALCARETFORE }

### `SCI_SETADDITIONALCARETSBLINK(bool additionalCaretsBlink)` {: #SCI_SETADDITIONALCARETSBLINK }

### `SCI_GETADDITIONALCARETSBLINK → bool` {: #SCI_GETADDITIONALCARETSBLINK }

Modify the appearance of additional carets so that they can be differentiated from the main caret which has its appearance set with `SC_ELEMENT_CARET`, `SCI_SETCARETFORE`, `SCI_GETCARETFORE`, `SCI_SETCARETPERIOD`, and `SCI_GETCARETPERIOD`.

### `SCI_SETADDITIONALCARETSVISIBLE(bool additionalCaretsVisible)` {: #SCI_SETADDITIONALCARETSVISIBLE }

### `SCI_GETADDITIONALCARETSVISIBLE → bool` {: #SCI_GETADDITIONALCARETSVISIBLE }

Determine whether to show additional carets (defaults to `true`).

### `SCI_SWAPMAINANCHORCARET` {: #SCI_SWAPMAINANCHORCARET }

### `SCI_ROTATESELECTION` {: #SCI_ROTATESELECTION }

### `SCI_MULTIPLESELECTADDNEXT` {: #SCI_MULTIPLESELECTADDNEXT }

### `SCI_MULTIPLESELECTADDEACH` {: #SCI_MULTIPLESELECTADDEACH }

These commands may be assigned to keys to make it possible to manipulate multiple selections. `SCI_SWAPMAINANCHORCARET` moves the caret to the opposite end of the main selection. `SCI_ROTATESELECTION` makes the next selection be the main selection.
`SCI_MULTIPLESELECTADDNEXT` adds the next occurrence of the main selection within the target to the set of selections as main. If the current selection is empty then select word around caret. The current `searchFlags` are used so the application may choose case sensitivity and word search options.
`SCI_MULTIPLESELECTADDEACH` is similar to `SCI_MULTIPLESELECTADDNEXT` but adds multiple occurrences instead of just one.
