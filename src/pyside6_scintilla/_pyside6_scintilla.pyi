# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
"""
This file contains the exact signatures for all functions in module
_pyside6_scintilla, except for defaults which are replaced by "...".
"""

# mypy: disable-error-code="override, overload-overlap"
# Module `_pyside6_scintilla`

import _pyside6_scintilla
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

import enum
import typing
from PySide6.QtCore import Signal
from shiboken6 import Shiboken


class QIntList: ...


class Scintilla(Shiboken.Object):

    # Position/sptr_t/uptr_t are primitive typedefs (plain `int` at runtime),
    # not nested types -- but genpyi emits forward references like
    # 'Scintilla.Position' for them. Alias to int so those resolve.
    Position = int
    sptr_t = int
    uptr_t = int

    class CharacterSource(enum.IntEnum):

        DirectInput               = 0x0
        r"""Direct input characters."""
        TentativeInput            = 0x1
        r"""IME (inline mode) or dead key tentative input characters."""
        ImeResult                 = 0x2
        r"""IME (either inline or windowed mode) full composited string."""

    class CompletionMethods(enum.IntEnum):

        FillUp                    = 0x1
        DoubleClick               = 0x2
        Tab                       = 0x3
        Newline                   = 0x4
        Command                   = 0x5
        SingleChoice              = 0x6

    class FoldLevel(enum.IntEnum):

        None_                     = 0x0
        Base                      = 0x400
        NumberMask                = 0xfff
        WhiteFlag                 = 0x1000
        HeaderFlag                = 0x2000

    class KeyMod(enum.IntEnum):

        Norm                      = 0x0
        Shift                     = 0x1
        Ctrl                      = 0x2
        Alt                       = 0x4
        Super                     = 0x8
        Meta                      = 0x10

    class MarginType(enum.IntEnum):

        Symbol                    = 0x0
        Number                    = 0x1
        Back                      = 0x2
        Fore                      = 0x3
        Text                      = 0x4
        RText                     = 0x5
        Colour                    = 0x6

    class Message(enum.IntEnum):

        AddText                   = 0x7d1
        r"""Add text to the document at current position."""
        AddStyledText             = 0x7d2
        r"""Add array of cells to document."""
        InsertText                = 0x7d3
        r"""Insert string at a position."""
        ClearAll                  = 0x7d4
        r"""Delete all text in the document."""
        ClearDocumentStyle        = 0x7d5
        r"""Set all style bytes to 0, remove all folding information."""
        GetLength                 = 0x7d6
        r"""Returns the number of bytes in the document."""
        GetCharAt                 = 0x7d7
        r"""Returns the character byte at the position."""
        GetCurrentPos             = 0x7d8
        r"""Returns the position of the caret."""
        GetAnchor                 = 0x7d9
        r"""Returns the position of the opposite end of the selection to the caret."""
        GetStyleAt                = 0x7da
        r"""Returns the style byte at the position."""
        Redo                      = 0x7db
        r"""Redoes the next action on the undo history."""
        SetUndoCollection         = 0x7dc
        r"""Choose between collecting actions into the undo history and discarding them."""
        SelectAll                 = 0x7dd
        r"""Select all the text in the document."""
        SetSavePoint              = 0x7de
        r"""Remember the current position in the undo history as the position at which the document was saved."""
        GetStyledText             = 0x7df
        r"""Retrieve a buffer of cells. Returns the number of bytes in the buffer not including terminating NULs."""
        CanRedo                   = 0x7e0
        r"""Are there any redoable actions in the undo history?"""
        MarkerLineFromHandle      = 0x7e1
        r"""Retrieve the line number at which a particular marker is located."""
        MarkerDeleteHandle        = 0x7e2
        r"""Delete a marker."""
        GetUndoCollection         = 0x7e3
        r"""Is undo history being collected?"""
        GetViewWS                 = 0x7e4
        r"""Are white space characters currently visible? Returns one of SCWS_* constants."""
        SetViewWS                 = 0x7e5
        r"""Make white space characters invisible, always visible or visible outside indentation."""
        PositionFromPoint         = 0x7e6
        r"""Find the position from a point within the window."""
        PositionFromPointClose    = 0x7e7
        r"""Find the position from a point within the window but return INVALID_POSITION if not close to text."""
        GotoLine                  = 0x7e8
        r"""Set caret to start of a line and ensure it is visible."""
        GotoPos                   = 0x7e9
        r"""Set caret to a position and ensure it is visible."""
        SetAnchor                 = 0x7ea
        r"""Set the selection anchor to a position. The anchor is the opposite end of the selection from the caret."""
        GetCurLine                = 0x7eb
        r"""Retrieve the text of the line containing the caret. Returns the index of the caret on the line. Result is NUL-terminated."""
        GetEndStyled              = 0x7ec
        r"""Retrieve the position of the last correctly styled character."""
        ConvertEOLs               = 0x7ed
        r"""Convert all line endings in the document to one mode."""
        GetEOLMode                = 0x7ee
        r"""Retrieve the current end of line mode - one of CRLF, CR, or LF."""
        SetEOLMode                = 0x7ef
        r"""Set the current end of line mode."""
        StartStyling              = 0x7f0
        r"""Set the current styling position to start. The unused parameter is no longer used and should be set to 0."""
        SetStyling                = 0x7f1
        r"""Change style from current styling position for length characters to a style and move the current styling position to after this newly styled segment."""
        GetBufferedDraw           = 0x7f2
        r"""Is drawing done first into a buffer or direct to the screen?"""
        SetBufferedDraw           = 0x7f3
        r"""If drawing is buffered then each line of text is drawn into a bitmap buffer before drawing it to the screen to avoid flicker."""
        SetTabWidth               = 0x7f4
        r"""Change the visible size of a tab to be a multiple of the width of a space character."""
        SetCodePage               = 0x7f5
        r"""Set the code page used to interpret the bytes of the document as characters. The SC_CP_UTF8 value can be used to enter Unicode mode."""
        GetStyleIndexAt           = 0x7f6
        r"""Returns the unsigned style byte at the position."""
        GetTextRangeFull          = 0x7f7
        r"""Retrieve a range of text that can be past 2GB. Return the length of the text."""
        MarkerDefine              = 0x7f8
        r"""Set the symbol used for a particular marker number."""
        MarkerSetFore             = 0x7f9
        r"""Set the foreground colour used for a particular marker number."""
        MarkerSetBack             = 0x7fa
        r"""Set the background colour used for a particular marker number."""
        MarkerAdd                 = 0x7fb
        r"""Add a marker to a line, returning an ID which can be used to find or delete the marker."""
        MarkerDelete              = 0x7fc
        r"""Delete a marker from a line."""
        MarkerDeleteAll           = 0x7fd
        r"""Delete all markers with a particular number from all lines."""
        MarkerGet                 = 0x7fe
        r"""Get a bit mask of all the markers set on a line."""
        MarkerNext                = 0x7ff
        r"""Find the next line at or after lineStart that includes a marker in mask. Return -1 when no more lines."""
        MarkerPrevious            = 0x800
        r"""Find the previous line before lineStart that includes a marker in mask."""
        MarkerDefinePixmap        = 0x801
        r"""Define a marker from a pixmap."""
        StyleClearAll             = 0x802
        r"""Clear all the styles and make equivalent to the global default style."""
        StyleSetFore              = 0x803
        r"""Set the foreground colour of a style."""
        StyleSetBack              = 0x804
        r"""Set the background colour of a style."""
        StyleSetBold              = 0x805
        r"""Set a style to be bold or not."""
        StyleSetItalic            = 0x806
        r"""Set a style to be italic or not."""
        StyleSetSize              = 0x807
        r"""Set the size of characters of a style."""
        StyleSetFont              = 0x808
        r"""Set the font of a style."""
        StyleSetEOLFilled         = 0x809
        r"""Set a style to have its end of line filled or not."""
        StyleResetDefault         = 0x80a
        r"""Reset the default style to its state at startup"""
        StyleSetUnderline         = 0x80b
        r"""Set a style to be underlined or not."""
        StyleSetCase              = 0x80c
        r"""Set a style to be mixed case, or to force upper or lower case."""
        StyleSetSizeFractional    = 0x80d
        r"""Set the size of characters of a style. Size is in points multiplied by 100."""
        StyleGetSizeFractional    = 0x80e
        r"""Get the size of characters of a style in points multiplied by 100"""
        StyleSetWeight            = 0x80f
        r"""Set the weight of characters of a style."""
        StyleGetWeight            = 0x810
        r"""Get the weight of characters of a style."""
        StyleSetCharacterSet      = 0x812
        r"""Set the character set of the font in a style."""
        SetSelFore                = 0x813
        r"""Set the foreground colour of the main and additional selections and whether to use this setting."""
        SetSelBack                = 0x814
        r"""Set the background colour of the main and additional selections and whether to use this setting."""
        SetCaretFore              = 0x815
        r"""Set the foreground colour of the caret."""
        AssignCmdKey              = 0x816
        r"""When key+modifier combination keyDefinition is pressed perform sciCommand."""
        ClearCmdKey               = 0x817
        r"""When key+modifier combination keyDefinition is pressed do nothing."""
        ClearAllCmdKeys           = 0x818
        r"""Drop all key mappings."""
        SetStylingEx              = 0x819
        r"""Set the styles for a segment of the document."""
        StyleSetVisible           = 0x81a
        r"""Set a style to be visible or not."""
        GetCaretPeriod            = 0x81b
        r"""Get the time in milliseconds that the caret is on and off."""
        SetCaretPeriod            = 0x81c
        r"""Get the time in milliseconds that the caret is on and off. 0 = steady on."""
        SetWordChars              = 0x81d
        r"""Set the set of characters making up words for when moving or selecting by word. First sets defaults like SetCharsDefault."""
        BeginUndoAction           = 0x81e
        r"""Start a sequence of actions that is undone and redone as a unit. May be nested."""
        EndUndoAction             = 0x81f
        r"""End a sequence of actions that is undone and redone as a unit."""
        IndicSetStyle             = 0x820
        r"""Set an indicator to plain, squiggle or TT."""
        IndicGetStyle             = 0x821
        r"""Retrieve the style of an indicator."""
        IndicSetFore              = 0x822
        r"""Set the foreground colour of an indicator."""
        IndicGetFore              = 0x823
        r"""Retrieve the foreground colour of an indicator."""
        SetWhitespaceFore         = 0x824
        r"""Set the foreground colour of all whitespace and whether to use this setting."""
        SetWhitespaceBack         = 0x825
        r"""Set the background colour of all whitespace and whether to use this setting."""
        SetWhitespaceSize         = 0x826
        r"""Set the size of the dots used to mark space characters."""
        GetWhitespaceSize         = 0x827
        r"""Get the size of the dots used to mark space characters."""
        GetSelectionHidden        = 0x828
        AllocateLines             = 0x829
        r"""Enlarge the number of lines allocated."""
        SetLineState              = 0x82c
        r"""Used to hold extra styling information for each line."""
        GetLineState              = 0x82d
        r"""Retrieve the extra styling information for a line."""
        GetMaxLineState           = 0x82e
        r"""Retrieve the last line number that has line state."""
        GetCaretLineVisible       = 0x82f
        r"""Is the background of the line containing the caret in a different colour?"""
        SetCaretLineVisible       = 0x830
        r"""Display the background of the line containing the caret in a different colour."""
        GetCaretLineBack          = 0x831
        r"""Get the colour of the background of the line containing the caret."""
        SetCaretLineBack          = 0x832
        r"""Set the colour of the background of the line containing the caret."""
        StyleSetChangeable        = 0x833
        r"""Set a style to be changeable or not (read only). Experimental feature, currently buggy."""
        AutoCShow                 = 0x834
        r"""Display a auto-completion list. The lengthEntered parameter indicates how many characters before the caret should be used to provide context."""
        AutoCCancel               = 0x835
        r"""Remove the auto-completion list from the screen."""
        AutoCActive               = 0x836
        r"""Is there an auto-completion list visible?"""
        AutoCPosStart             = 0x837
        r"""Retrieve the position of the caret when the auto-completion list was displayed."""
        AutoCComplete             = 0x838
        r"""User has selected an item so remove the list and insert the selection."""
        AutoCStops                = 0x839
        r"""Define a set of character that when typed cancel the auto-completion list."""
        AutoCSetSeparator         = 0x83a
        r"""Change the separator character in the string setting up an auto-completion list. Default is space but can be changed if items contain space."""
        AutoCGetSeparator         = 0x83b
        r"""Retrieve the auto-completion list separator character."""
        AutoCSelect               = 0x83c
        r"""Select the item in the auto-completion list that starts with a string."""
        AutoCSetStyle             = 0x83d
        r"""Set the style number used for auto-completion and user lists fonts."""
        AutoCSetCancelAtStart     = 0x83e
        r"""Should the auto-completion list be cancelled if the user backspaces to a position before where the box was created."""
        AutoCGetCancelAtStart     = 0x83f
        r"""Retrieve whether auto-completion cancelled by backspacing before start."""
        AutoCSetFillUps           = 0x840
        r"""Define a set of characters that when typed will cause the autocompletion to choose the selected item."""
        AutoCSetChooseSingle      = 0x841
        r"""Should a single item auto-completion list automatically choose the item."""
        AutoCGetChooseSingle      = 0x842
        r"""Retrieve whether a single item auto-completion list automatically choose the item."""
        AutoCSetIgnoreCase        = 0x843
        r"""Set whether case is significant when performing auto-completion searches."""
        AutoCGetIgnoreCase        = 0x844
        r"""Retrieve state of ignore case flag."""
        UserListShow              = 0x845
        r"""Display a list of strings and send notification when user chooses one."""
        AutoCSetAutoHide          = 0x846
        r"""Set whether or not autocompletion is hidden automatically when nothing matches."""
        AutoCGetAutoHide          = 0x847
        r"""Retrieve whether or not autocompletion is hidden automatically when nothing matches."""
        AutoCGetStyle             = 0x848
        r"""Get the style number used for auto-completion and user lists fonts."""
        GetTabWidth               = 0x849
        r"""Retrieve the visible size of a tab."""
        SetIndent                 = 0x84a
        r"""Set the number of spaces used for one level of indentation."""
        GetIndent                 = 0x84b
        r"""Retrieve indentation size."""
        SetUseTabs                = 0x84c
        r"""Indentation will only use space characters if useTabs is false, otherwise it will use a combination of tabs and spaces."""
        GetUseTabs                = 0x84d
        r"""Retrieve whether tabs will be used in indentation."""
        SetLineIndentation        = 0x84e
        r"""Change the indentation of a line to a number of columns."""
        GetLineIndentation        = 0x84f
        r"""Retrieve the number of columns that a line is indented."""
        GetLineIndentPosition     = 0x850
        r"""Retrieve the position before the first non indentation character on a line."""
        GetColumn                 = 0x851
        r"""Retrieve the column number of a position, taking tab width into account."""
        SetHScrollBar             = 0x852
        r"""Show or hide the horizontal scroll bar."""
        GetHScrollBar             = 0x853
        r"""Is the horizontal scroll bar visible?"""
        SetIndentationGuides      = 0x854
        r"""Show or hide indentation guides."""
        GetIndentationGuides      = 0x855
        r"""Are the indentation guides visible?"""
        SetHighlightGuide         = 0x856
        r"""Set the highlighted indentation guide column. 0 = no highlighted guide."""
        GetHighlightGuide         = 0x857
        r"""Get the highlighted indentation guide column."""
        GetLineEndPosition        = 0x858
        r"""Get the position after the last visible characters on a line."""
        GetCodePage               = 0x859
        r"""Get the code page used to interpret the bytes of the document as characters."""
        GetCaretFore              = 0x85a
        r"""Get the foreground colour of the caret."""
        GetReadOnly               = 0x85c
        r"""In read-only mode?"""
        SetCurrentPos             = 0x85d
        r"""Sets the position of the caret."""
        SetSelectionStart         = 0x85e
        r"""Sets the position that starts the selection - this becomes the anchor."""
        GetSelectionStart         = 0x85f
        r"""Returns the position at the start of the selection."""
        SetSelectionEnd           = 0x860
        r"""Sets the position that ends the selection - this becomes the caret."""
        GetSelectionEnd           = 0x861
        r"""Returns the position at the end of the selection."""
        SetPrintMagnification     = 0x862
        r"""Sets the print magnification added to the point size of each style for printing."""
        GetPrintMagnification     = 0x863
        r"""Returns the print magnification."""
        SetPrintColourMode        = 0x864
        r"""Modify colours when printing for clearer printed text."""
        GetPrintColourMode        = 0x865
        r"""Returns the print colour mode."""
        FindText                  = 0x866
        r"""Find some text in the document."""
        FormatRange               = 0x867
        r"""Draw the document into a display context such as a printer."""
        GetFirstVisibleLine       = 0x868
        r"""Retrieve the display line at the top of the display."""
        GetLine                   = 0x869
        r"""Retrieve the contents of a line. Returns the length of the line."""
        GetLineCount              = 0x86a
        r"""Returns the number of lines in the document. There is always at least one."""
        SetMarginLeft             = 0x86b
        r"""Sets the size in pixels of the left margin."""
        GetMarginLeft             = 0x86c
        r"""Returns the size in pixels of the left margin."""
        SetMarginRight            = 0x86d
        r"""Sets the size in pixels of the right margin."""
        GetMarginRight            = 0x86e
        r"""Returns the size in pixels of the right margin."""
        GetModify                 = 0x86f
        r"""Is the document different from when it was last saved?"""
        SetSel                    = 0x870
        r"""Select a range of text."""
        GetSelText                = 0x871
        r"""Retrieve the selected text. Return the length of the text. Result is NUL-terminated."""
        GetTextRange              = 0x872
        r"""Retrieve a range of text. Return the length of the text."""
        HideSelection             = 0x873
        r"""Draw the selection either highlighted or in normal (non-highlighted) style."""
        PointXFromPosition        = 0x874
        r"""Retrieve the x value of the point in the window where a position is displayed."""
        PointYFromPosition        = 0x875
        r"""Retrieve the y value of the point in the window where a position is displayed."""
        LineFromPosition          = 0x876
        r"""Retrieve the line containing a position."""
        PositionFromLine          = 0x877
        r"""Retrieve the position at the start of a line."""
        LineScroll                = 0x878
        r"""Scroll horizontally and vertically."""
        ScrollCaret               = 0x879
        r"""Ensure the caret is visible."""
        ReplaceSel                = 0x87a
        r"""Replace the selected text with the argument text."""
        SetReadOnly               = 0x87b
        r"""Set to read only or read write."""
        Null                      = 0x87c
        r"""Null operation."""
        CanPaste                  = 0x87d
        r"""Will a paste succeed?"""
        CanUndo                   = 0x87e
        r"""Are there any undoable actions in the undo history?"""
        EmptyUndoBuffer           = 0x87f
        r"""Delete the undo history."""
        Undo                      = 0x880
        r"""Undo one action in the undo history."""
        Cut                       = 0x881
        r"""Cut the selection to the clipboard."""
        Copy                      = 0x882
        r"""Copy the selection to the clipboard."""
        Paste                     = 0x883
        r"""Paste the contents of the clipboard into the document replacing the selection."""
        Clear                     = 0x884
        r"""Clear the selection."""
        SetText                   = 0x885
        r"""Replace the contents of the document with the argument text."""
        GetText                   = 0x886
        r"""Retrieve all the text in the document. Returns number of characters retrieved. Result is NUL-terminated."""
        GetTextLength             = 0x887
        r"""Retrieve the number of characters in the document."""
        GetDirectFunction         = 0x888
        r"""Retrieve a pointer to a function that processes messages for this Scintilla."""
        GetDirectPointer          = 0x889
        r"""Retrieve a pointer value to use as the first argument when calling the function returned by GetDirectFunction."""
        SetOvertype               = 0x88a
        r"""Set to overtype (true) or insert mode."""
        GetOvertype               = 0x88b
        r"""Returns true if overtype mode is active otherwise false is returned."""
        SetCaretWidth             = 0x88c
        r"""Set the width of the insert mode caret."""
        GetCaretWidth             = 0x88d
        r"""Returns the width of the insert mode caret."""
        SetTargetStart            = 0x88e
        r"""Sets the position that starts the target which is used for updating the document without affecting the scroll position."""
        GetTargetStart            = 0x88f
        r"""Get the position that starts the target."""
        SetTargetEnd              = 0x890
        r"""Sets the position that ends the target which is used for updating the document without affecting the scroll position."""
        GetTargetEnd              = 0x891
        r"""Get the position that ends the target."""
        ReplaceTarget             = 0x892
        r"""Replace the target text with the argument text. Text is counted so it can contain NULs. Returns the length of the replacement text."""
        ReplaceTargetRE           = 0x893
        r"""Replace the target text with the argument text after \d processing. Text is counted so it can contain NULs. Looks for \d where d is between 1 and 9 and replaces these with the strings matched in the last search operation which were surrounded by \( and \). Returns the length of the replacement text including any change caused by processing the \d patterns."""
        FindTextFull              = 0x894
        r"""Find some text in the document."""
        SearchInTarget            = 0x895
        r"""Search for a counted string in the target and set the target to the found range. Text is counted so it can contain NULs. Returns start of found range or -1 for failure in which case target is not moved."""
        SetSearchFlags            = 0x896
        r"""Set the search flags used by SearchInTarget."""
        GetSearchFlags            = 0x897
        r"""Get the search flags used by SearchInTarget."""
        CallTipShow               = 0x898
        r"""Show a call tip containing a definition near position pos."""
        CallTipCancel             = 0x899
        r"""Remove the call tip from the screen."""
        CallTipActive             = 0x89a
        r"""Is there an active call tip?"""
        CallTipPosStart           = 0x89b
        r"""Retrieve the position where the caret was before displaying the call tip."""
        CallTipSetHlt             = 0x89c
        r"""Highlight a segment of the definition."""
        CallTipSetBack            = 0x89d
        r"""Set the background colour for the call tip."""
        CallTipSetFore            = 0x89e
        r"""Set the foreground colour for the call tip."""
        CallTipSetForeHlt         = 0x89f
        r"""Set the foreground colour for the highlighted part of the call tip."""
        AutoCSetMaxWidth          = 0x8a0
        r"""Set the maximum width, in characters, of auto-completion and user lists. Set to 0 to autosize to fit longest item, which is the default."""
        AutoCGetMaxWidth          = 0x8a1
        r"""Get the maximum width, in characters, of auto-completion and user lists."""
        AutoCSetMaxHeight         = 0x8a2
        r"""Set the maximum height, in rows, of auto-completion and user lists. The default is 5 rows."""
        AutoCGetMaxHeight         = 0x8a3
        r"""Set the maximum height, in rows, of auto-completion and user lists."""
        CallTipUseStyle           = 0x8a4
        r"""Enable use of STYLE_CALLTIP and set call tip tab size in pixels."""
        CallTipSetPosition        = 0x8a5
        r"""Set position of calltip, above or below text."""
        CallTipSetPosStart        = 0x8a6
        r"""Set the start position in order to change when backspacing removes the calltip."""
        VisibleFromDocLine        = 0x8ac
        r"""Find the display line of a document line taking hidden lines into account."""
        DocLineFromVisible        = 0x8ad
        r"""Find the document line of a display line taking hidden lines into account."""
        SetFoldLevel              = 0x8ae
        r"""Set the fold level of a line. This encodes an integer level along with flags indicating whether the line is a header and whether it is effectively white space."""
        GetFoldLevel              = 0x8af
        r"""Retrieve the fold level of a line."""
        GetLastChild              = 0x8b0
        r"""Find the last child line of a header line."""
        GetFoldParent             = 0x8b1
        r"""Find the parent line of a child line."""
        ShowLines                 = 0x8b2
        r"""Make a range of lines visible."""
        HideLines                 = 0x8b3
        r"""Make a range of lines invisible."""
        GetLineVisible            = 0x8b4
        r"""Is a line visible?"""
        SetFoldExpanded           = 0x8b5
        r"""Show the children of a header line."""
        GetFoldExpanded           = 0x8b6
        r"""Is a header line expanded?"""
        ToggleFold                = 0x8b7
        r"""Switch a header line between expanded and contracted."""
        EnsureVisible             = 0x8b8
        r"""Ensure a particular line is visible by expanding any header line hiding it."""
        SetFoldFlags              = 0x8b9
        r"""Set some style options for folding."""
        EnsureVisibleEnforcePolicy = 0x8ba
        r"""Ensure a particular line is visible by expanding any header line hiding it. Use the currently set visibility policy to determine which range to display."""
        WrapCount                 = 0x8bb
        r"""The number of display lines needed to wrap a document line"""
        GetAllLinesVisible        = 0x8bc
        r"""Are all lines visible?"""
        FoldLine                  = 0x8bd
        r"""Expand or contract a fold header."""
        FoldChildren              = 0x8be
        r"""Expand or contract a fold header and its children."""
        ExpandChildren            = 0x8bf
        r"""Expand a fold header and all children. Use the level argument instead of the line's current level."""
        SetMarginTypeN            = 0x8c0
        r"""Set a margin to be either numeric or symbolic."""
        GetMarginTypeN            = 0x8c1
        r"""Retrieve the type of a margin."""
        SetMarginWidthN           = 0x8c2
        r"""Set the width of a margin to a width expressed in pixels."""
        GetMarginWidthN           = 0x8c3
        r"""Retrieve the width of a margin in pixels."""
        SetMarginMaskN            = 0x8c4
        r"""Set a mask that determines which markers are displayed in a margin."""
        GetMarginMaskN            = 0x8c5
        r"""Retrieve the marker mask of a margin."""
        SetMarginSensitiveN       = 0x8c6
        r"""Make a margin sensitive or insensitive to mouse clicks."""
        GetMarginSensitiveN       = 0x8c7
        r"""Retrieve the mouse click sensitivity of a margin."""
        SetMarginCursorN          = 0x8c8
        r"""Set the cursor shown when the mouse is inside a margin."""
        GetMarginCursorN          = 0x8c9
        r"""Retrieve the cursor shown in a margin."""
        SetMarginBackN            = 0x8ca
        r"""Set the background colour of a margin. Only visible for SC_MARGIN_COLOUR."""
        GetMarginBackN            = 0x8cb
        r"""Retrieve the background colour of a margin"""
        SetMargins                = 0x8cc
        r"""Allocate a non-standard number of margins."""
        GetMargins                = 0x8cd
        r"""How many margins are there?."""
        StyleSetCheckMonospaced   = 0x8ce
        r"""Indicate that a style may be monospaced over ASCII graphics characters which enables optimizations."""
        StyleGetCheckMonospaced   = 0x8cf
        r"""Get whether a style may be monospaced."""
        StyleSetInvisibleRepresentation = 0x8d0
        r"""Set the invisible representation for a style."""
        StyleGetInvisibleRepresentation = 0x8d1
        r"""Get the invisible representation for a style."""
        StyleSetStretch           = 0x8d2
        r"""Set the stretch of characters of a style."""
        StyleGetStretch           = 0x8d3
        r"""Get the stretch of characters of a style."""
        SetTabIndents             = 0x8d4
        r"""Sets whether a tab pressed when caret is within indentation indents."""
        GetTabIndents             = 0x8d5
        r"""Does a tab pressed when caret is within indentation indent?"""
        SetBackSpaceUnIndents     = 0x8d6
        r"""Sets whether a backspace pressed when caret is within indentation unindents."""
        GetBackSpaceUnIndents     = 0x8d7
        r"""Does a backspace pressed when caret is within indentation unindent?"""
        SetMouseDwellTime         = 0x8d8
        r"""Sets the time the mouse must sit still to generate a mouse dwell event."""
        GetMouseDwellTime         = 0x8d9
        r"""Retrieve the time the mouse must sit still to generate a mouse dwell event."""
        WordStartPosition         = 0x8da
        r"""Get position of start of word."""
        WordEndPosition           = 0x8db
        r"""Get position of end of word."""
        SetWrapMode               = 0x8dc
        r"""Sets whether text is word wrapped."""
        GetWrapMode               = 0x8dd
        r"""Retrieve whether text is word wrapped."""
        AutoCSetDropRestOfWord    = 0x8de
        r"""Set whether or not autocompletion deletes any word characters after the inserted text upon completion."""
        AutoCGetDropRestOfWord    = 0x8df
        r"""Retrieve whether or not autocompletion deletes any word characters after the inserted text upon completion."""
        SetLayoutCache            = 0x8e0
        r"""Sets the degree of caching of layout information."""
        GetLayoutCache            = 0x8e1
        r"""Retrieve the degree of caching of layout information."""
        SetScrollWidth            = 0x8e2
        r"""Sets the document width assumed for scrolling."""
        GetScrollWidth            = 0x8e3
        r"""Retrieve the document width assumed for scrolling."""
        TextWidth                 = 0x8e4
        r"""Measure the pixel width of some text in a particular style. NUL terminated text argument. Does not handle tab or control characters."""
        SetEndAtLastLine          = 0x8e5
        r"""Sets the scroll range so that maximum scroll position has the last line at the bottom of the view (default). Setting this to false allows scrolling one page below the last line."""
        GetEndAtLastLine          = 0x8e6
        r"""Retrieve whether the maximum scroll position has the last line at the bottom of the view."""
        TextHeight                = 0x8e7
        r"""Retrieve the height of a particular line of text in pixels."""
        SetVScrollBar             = 0x8e8
        r"""Show or hide the vertical scroll bar."""
        GetVScrollBar             = 0x8e9
        r"""Is the vertical scroll bar visible?"""
        AppendText                = 0x8ea
        r"""Append a string to the end of the document without changing the selection."""
        AutoCGetTypeSeparator     = 0x8ed
        r"""Retrieve the auto-completion list type-separator character."""
        AutoCSetTypeSeparator     = 0x8ee
        r"""Change the type-separator character in the string setting up an auto-completion list. Default is '?' but can be changed if items contain '?'."""
        TargetFromSelection       = 0x8ef
        r"""Make the target range start and end be the same as the selection range start and end."""
        LinesJoin                 = 0x8f0
        r"""Join the lines in the target."""
        LinesSplit                = 0x8f1
        r"""Split the lines in the target into lines that are less wide than pixelWidth where possible."""
        SetFoldMarginColour       = 0x8f2
        r"""Set one of the colours used as a chequerboard pattern in the fold margin"""
        SetFoldMarginHiColour     = 0x8f3
        r"""Set the other colour used as a chequerboard pattern in the fold margin"""
        MarkerSetBackSelected     = 0x8f4
        r"""Set the background colour used for a particular marker number when its folding block is selected."""
        MarkerEnableHighlight     = 0x8f5
        r"""Enable/disable highlight for current folding block (smallest one that contains the caret)"""
        MarkerSetForeTranslucent  = 0x8f6
        r"""Set the foreground colour used for a particular marker number."""
        MarkerSetBackTranslucent  = 0x8f7
        r"""Set the background colour used for a particular marker number."""
        MarkerSetBackSelectedTranslucent = 0x8f8
        r"""Set the background colour used for a particular marker number when its folding block is selected."""
        MarkerSetStrokeWidth      = 0x8f9
        r"""Set the width of strokes used in .01 pixels so 50  = 1/2 pixel width."""
        LineDown                  = 0x8fc
        r"""Move caret down one line."""
        LineDownExtend            = 0x8fd
        r"""Move caret down one line extending selection to new caret position."""
        LineUp                    = 0x8fe
        r"""Move caret up one line."""
        LineUpExtend              = 0x8ff
        r"""Move caret up one line extending selection to new caret position."""
        CharLeft                  = 0x900
        r"""Move caret left one character."""
        CharLeftExtend            = 0x901
        r"""Move caret left one character extending selection to new caret position."""
        CharRight                 = 0x902
        r"""Move caret right one character."""
        CharRightExtend           = 0x903
        r"""Move caret right one character extending selection to new caret position."""
        WordLeft                  = 0x904
        r"""Move caret left one word."""
        WordLeftExtend            = 0x905
        r"""Move caret left one word extending selection to new caret position."""
        WordRight                 = 0x906
        r"""Move caret right one word."""
        WordRightExtend           = 0x907
        r"""Move caret right one word extending selection to new caret position."""
        Home                      = 0x908
        r"""Move caret to first position on line."""
        HomeExtend                = 0x909
        r"""Move caret to first position on line extending selection to new caret position."""
        LineEnd                   = 0x90a
        r"""Move caret to last position on line."""
        LineEndExtend             = 0x90b
        r"""Move caret to last position on line extending selection to new caret position."""
        DocumentStart             = 0x90c
        r"""Move caret to first position in document."""
        DocumentStartExtend       = 0x90d
        r"""Move caret to first position in document extending selection to new caret position."""
        DocumentEnd               = 0x90e
        r"""Move caret to last position in document."""
        DocumentEndExtend         = 0x90f
        r"""Move caret to last position in document extending selection to new caret position."""
        PageUp                    = 0x910
        r"""Move caret one page up."""
        PageUpExtend              = 0x911
        r"""Move caret one page up extending selection to new caret position."""
        PageDown                  = 0x912
        r"""Move caret one page down."""
        PageDownExtend            = 0x913
        r"""Move caret one page down extending selection to new caret position."""
        EditToggleOvertype        = 0x914
        r"""Switch from insert to overtype mode or the reverse."""
        Cancel                    = 0x915
        r"""Cancel any modes such as call tip or auto-completion list display."""
        DeleteBack                = 0x916
        r"""Delete the selection or if no selection, the character before the caret."""
        Tab                       = 0x917
        r"""If selection is empty or all on one line replace the selection with a tab character. If more than one line selected, indent the lines."""
        BackTab                   = 0x918
        r"""If selection is empty or all on one line dedent the line if caret is at start, else move caret. If more than one line selected, dedent the lines."""
        NewLine                   = 0x919
        r"""Insert a new line, may use a CRLF, CR or LF depending on EOL mode."""
        FormFeed                  = 0x91a
        r"""Insert a Form Feed character."""
        VCHome                    = 0x91b
        r"""Move caret to before first visible character on line. If already there move to first character on line."""
        VCHomeExtend              = 0x91c
        r"""Like VCHome but extending selection to new caret position."""
        ZoomIn                    = 0x91d
        r"""Magnify the displayed text by increasing the sizes by 1 point."""
        ZoomOut                   = 0x91e
        r"""Make the displayed text smaller by decreasing the sizes by 1 point."""
        DelWordLeft               = 0x91f
        r"""Delete the word to the left of the caret."""
        DelWordRight              = 0x920
        r"""Delete the word to the right of the caret."""
        LineCut                   = 0x921
        r"""Cut the line containing the caret."""
        LineDelete                = 0x922
        r"""Delete the line containing the caret."""
        LineTranspose             = 0x923
        r"""Switch the current line with the previous."""
        LowerCase                 = 0x924
        r"""Transform the selection to lower case."""
        UpperCase                 = 0x925
        r"""Transform the selection to upper case."""
        LineScrollDown            = 0x926
        r"""Scroll the document down, keeping the caret visible."""
        LineScrollUp              = 0x927
        r"""Scroll the document up, keeping the caret visible."""
        DeleteBackNotLine         = 0x928
        r"""Delete the selection or if no selection, the character before the caret. Will not delete the character before at the start of a line."""
        HomeDisplay               = 0x929
        r"""Move caret to first position on display line."""
        HomeDisplayExtend         = 0x92a
        r"""Move caret to first position on display line extending selection to new caret position."""
        LineEndDisplay            = 0x92b
        r"""Move caret to last position on display line."""
        LineEndDisplayExtend      = 0x92c
        r"""Move caret to last position on display line extending selection to new caret position."""
        HomeWrap                  = 0x92d
        r"""Like Home but when word-wrap is enabled goes first to start of display line HomeDisplay, then to start of document line Home."""
        LineLength                = 0x92e
        r"""How many characters are on a line, including end of line characters?"""
        BraceHighlight            = 0x92f
        r"""Highlight the characters at two positions."""
        BraceBadLight             = 0x930
        r"""Highlight the character at a position indicating there is no matching brace."""
        BraceMatch                = 0x931
        r"""Find the position of a matching brace or INVALID_POSITION if no match. The maxReStyle must be 0 for now. It may be defined in a future release."""
        LineReverse               = 0x932
        r"""Reverse order of selected lines."""
        GetViewEOL                = 0x933
        r"""Are the end of line characters visible?"""
        SetViewEOL                = 0x934
        r"""Make the end of line characters visible or invisible."""
        GetDocPointer             = 0x935
        r"""Retrieve a pointer to the document object."""
        SetDocPointer             = 0x936
        r"""Change the document object used."""
        SetModEventMask           = 0x937
        r"""Set which document modification events are sent to the container."""
        GetEdgeColumn             = 0x938
        r"""Retrieve the column number which text should be kept within."""
        SetEdgeColumn             = 0x939
        r"""Set the column number of the edge. If text goes past the edge then it is highlighted."""
        GetEdgeMode               = 0x93a
        r"""Retrieve the edge highlight mode."""
        SetEdgeMode               = 0x93b
        r"""The edge may be displayed by a line (EDGE_LINE/EDGE_MULTILINE) or by highlighting text that goes beyond it (EDGE_BACKGROUND) or not displayed at all (EDGE_NONE)."""
        GetEdgeColour             = 0x93c
        r"""Retrieve the colour used in edge indication."""
        SetEdgeColour             = 0x93d
        r"""Change the colour used in edge indication."""
        SearchAnchor              = 0x93e
        r"""Sets the current caret position to be the search anchor."""
        SearchNext                = 0x93f
        r"""Find some text starting at the search anchor. Does not ensure the selection is visible."""
        SearchPrev                = 0x940
        r"""Find some text starting at the search anchor and moving backwards. Does not ensure the selection is visible."""
        BraceMatchNext            = 0x941
        r"""Similar to BraceMatch, but matching starts at the explicit start position."""
        LinesOnScreen             = 0x942
        r"""Retrieves the number of lines completely visible."""
        UsePopUp                  = 0x943
        r"""Set whether a pop up menu is displayed automatically when the user presses the wrong mouse button on certain areas."""
        SelectionIsRectangle      = 0x944
        r"""Is the selection rectangular? The alternative is the more common stream selection."""
        SetZoom                   = 0x945
        r"""Set the zoom level. This number of points is added to the size of all fonts. It may be positive to magnify or negative to reduce."""
        GetZoom                   = 0x946
        r"""Retrieve the zoom level."""
        CreateDocument            = 0x947
        r"""Create a new document object. Starts with reference count of 1 and not selected into editor."""
        AddRefDocument            = 0x948
        r"""Extend life of document."""
        ReleaseDocument           = 0x949
        r"""Release a reference to the document, deleting document if it fades to black."""
        GetModEventMask           = 0x94a
        r"""Get which document modification events are sent to the container."""
        GetDocumentOptions        = 0x94b
        r"""Get which document options are set."""
        SetFocus                  = 0x94c
        r"""Change internal focus flag."""
        GetFocus                  = 0x94d
        r"""Get internal focus flag."""
        SetStatus                 = 0x94e
        r"""Change error status - 0 = OK."""
        GetStatus                 = 0x94f
        r"""Get error status."""
        SetMouseDownCaptures      = 0x950
        r"""Set whether the mouse is captured when its button is pressed."""
        GetMouseDownCaptures      = 0x951
        r"""Get whether mouse gets captured."""
        SetCursor                 = 0x952
        r"""Sets the cursor to one of the SC_CURSOR* values."""
        GetCursor                 = 0x953
        r"""Get cursor type."""
        SetControlCharSymbol      = 0x954
        r"""Change the way control characters are displayed: If symbol is < 32, keep the drawn way, else, use the given character."""
        GetControlCharSymbol      = 0x955
        r"""Get the way control characters are displayed."""
        WordPartLeft              = 0x956
        r"""Move to the previous change in capitalisation."""
        WordPartLeftExtend        = 0x957
        r"""Move to the previous change in capitalisation extending selection to new caret position."""
        WordPartRight             = 0x958
        r"""Move to the change next in capitalisation."""
        WordPartRightExtend       = 0x959
        r"""Move to the next change in capitalisation extending selection to new caret position."""
        SetVisiblePolicy          = 0x95a
        r"""Set the way the display area is determined when a particular line is to be moved to by Find, FindNext, GotoLine, etc."""
        DelLineLeft               = 0x95b
        r"""Delete back from the current position to the start of the line."""
        DelLineRight              = 0x95c
        r"""Delete forwards from the current position to the end of the line."""
        SetXOffset                = 0x95d
        r"""Set the xOffset (ie, horizontal scroll position)."""
        GetXOffset                = 0x95e
        r"""Get the xOffset (ie, horizontal scroll position)."""
        ChooseCaretX              = 0x95f
        r"""Set the last x chosen value to be the caret x position."""
        GrabFocus                 = 0x960
        r"""Set the focus to this Scintilla widget."""
        MoveCaretInsideView       = 0x961
        r"""Move the caret inside current view if it's not there already."""
        SetXCaretPolicy           = 0x962
        r"""Set the way the caret is kept visible when going sideways. The exclusion zone is given in pixels."""
        SetYCaretPolicy           = 0x963
        r"""Set the way the line the caret is on is kept visible. The exclusion zone is given in lines."""
        LineDuplicate             = 0x964
        r"""Duplicate the current line."""
        RegisterImage             = 0x965
        r"""Register an XPM image for use in autocompletion lists."""
        SetPrintWrapMode          = 0x966
        r"""Set printing to line wrapped (SC_WRAP_WORD) or not line wrapped (SC_WRAP_NONE)."""
        GetPrintWrapMode          = 0x967
        r"""Is printing line wrapped?"""
        ClearRegisteredImages     = 0x968
        r"""Clear all the registered XPM images."""
        StyleSetHotSpot           = 0x969
        r"""Set a style to be a hotspot or not."""
        SetHotspotActiveFore      = 0x96a
        r"""Set a fore colour for active hotspots."""
        SetHotspotActiveBack      = 0x96b
        r"""Set a back colour for active hotspots."""
        SetHotspotActiveUnderline = 0x96c
        r"""Enable / Disable underlining active hotspots."""
        ParaDown                  = 0x96d
        r"""Move caret down one paragraph (delimited by empty lines)."""
        ParaDownExtend            = 0x96e
        r"""Extend selection down one paragraph (delimited by empty lines)."""
        ParaUp                    = 0x96f
        r"""Move caret up one paragraph (delimited by empty lines)."""
        ParaUpExtend              = 0x970
        r"""Extend selection up one paragraph (delimited by empty lines)."""
        PositionBefore            = 0x971
        r"""Given a valid document position, return the previous position taking code page into account. Returns 0 if passed 0."""
        PositionAfter             = 0x972
        r"""Given a valid document position, return the next position taking code page into account. Maximum value returned is the last position in the document."""
        CopyRange                 = 0x973
        r"""Copy a range of text to the clipboard. Positions are clipped into the document."""
        CopyText                  = 0x974
        r"""Copy argument text to the clipboard."""
        SetHotspotSingleLine      = 0x975
        r"""Limit hotspots to single line so hotspots on two lines don't merge."""
        SetSelectionMode          = 0x976
        r"""Set the selection mode to stream (SC_SEL_STREAM) or rectangular (SC_SEL_RECTANGLE/SC_SEL_THIN) or by lines (SC_SEL_LINES)."""
        GetSelectionMode          = 0x977
        r"""Get the mode of the current selection."""
        GetLineSelStartPosition   = 0x978
        r"""Retrieve the position of the start of the selection at the given line (INVALID_POSITION if no selection on this line)."""
        GetLineSelEndPosition     = 0x979
        r"""Retrieve the position of the end of the selection at the given line (INVALID_POSITION if no selection on this line)."""
        LineDownRectExtend        = 0x97a
        r"""Move caret down one line, extending rectangular selection to new caret position."""
        LineUpRectExtend          = 0x97b
        r"""Move caret up one line, extending rectangular selection to new caret position."""
        CharLeftRectExtend        = 0x97c
        r"""Move caret left one character, extending rectangular selection to new caret position."""
        CharRightRectExtend       = 0x97d
        r"""Move caret right one character, extending rectangular selection to new caret position."""
        HomeRectExtend            = 0x97e
        r"""Move caret to first position on line, extending rectangular selection to new caret position."""
        VCHomeRectExtend          = 0x97f
        r"""Move caret to before first visible character on line. If already there move to first character on line. In either case, extend rectangular selection to new caret position."""
        LineEndRectExtend         = 0x980
        r"""Move caret to last position on line, extending rectangular selection to new caret position."""
        PageUpRectExtend          = 0x981
        r"""Move caret one page up, extending rectangular selection to new caret position."""
        PageDownRectExtend        = 0x982
        r"""Move caret one page down, extending rectangular selection to new caret position."""
        StutteredPageUp           = 0x983
        r"""Move caret to top of page, or one page up if already at top of page."""
        StutteredPageUpExtend     = 0x984
        r"""Move caret to top of page, or one page up if already at top of page, extending selection to new caret position."""
        StutteredPageDown         = 0x985
        r"""Move caret to bottom of page, or one page down if already at bottom of page."""
        StutteredPageDownExtend   = 0x986
        r"""Move caret to bottom of page, or one page down if already at bottom of page, extending selection to new caret position."""
        WordLeftEnd               = 0x987
        r"""Move caret left one word, position cursor at end of word."""
        WordLeftEndExtend         = 0x988
        r"""Move caret left one word, position cursor at end of word, extending selection to new caret position."""
        WordRightEnd              = 0x989
        r"""Move caret right one word, position cursor at end of word."""
        WordRightEndExtend        = 0x98a
        r"""Move caret right one word, position cursor at end of word, extending selection to new caret position."""
        SetWhitespaceChars        = 0x98b
        r"""Set the set of characters making up whitespace for when moving or selecting by word. Should be called after SetWordChars."""
        SetCharsDefault           = 0x98c
        r"""Reset the set of characters for whitespace and word characters to the defaults."""
        AutoCGetCurrent           = 0x98d
        r"""Get currently selected item position in the auto-completion list"""
        Allocate                  = 0x98e
        r"""Enlarge the document to a particular size of text bytes."""
        TargetAsUTF8              = 0x98f
        r"""Returns the target converted to UTF8. Return the length in bytes."""
        SetLengthForEncode        = 0x990
        r"""Set the length of the utf8 argument for calling EncodedFromUTF8. Set to -1 and the string will be measured to the first nul."""
        EncodedFromUTF8           = 0x991
        r"""Translates a UTF8 string into the document encoding. Return the length of the result in bytes. On error return 0."""
        HomeWrapExtend            = 0x992
        r"""Like HomeExtend but when word-wrap is enabled extends first to start of display line HomeDisplayExtend, then to start of document line HomeExtend."""
        LineEndWrap               = 0x993
        r"""Like LineEnd but when word-wrap is enabled goes first to end of display line LineEndDisplay, then to start of document line LineEnd."""
        LineEndWrapExtend         = 0x994
        r"""Like LineEndExtend but when word-wrap is enabled extends first to end of display line LineEndDisplayExtend, then to start of document line LineEndExtend."""
        VCHomeWrap                = 0x995
        r"""Like VCHome but when word-wrap is enabled goes first to start of display line VCHomeDisplay, then behaves like VCHome."""
        VCHomeWrapExtend          = 0x996
        r"""Like VCHomeExtend but when word-wrap is enabled extends first to start of display line VCHomeDisplayExtend, then behaves like VCHomeExtend."""
        LineCopy                  = 0x997
        r"""Copy the line containing the caret."""
        FindColumn                = 0x998
        r"""Find the position of a column on a line taking into account tabs and multi-byte characters. If beyond end of line, return line end position."""
        GetCaretSticky            = 0x999
        r"""Can the caret preferred x position only be changed by explicit movement commands?"""
        SetCaretSticky            = 0x99a
        r"""Stop the caret preferred x position changing when the user types."""
        ToggleCaretSticky         = 0x99b
        r"""Switch between sticky and non-sticky: meant to be bound to a key."""
        SetWrapVisualFlags        = 0x99c
        r"""Set the display mode of visual flags for wrapped lines."""
        GetWrapVisualFlags        = 0x99d
        r"""Retrive the display mode of visual flags for wrapped lines."""
        SetWrapVisualFlagsLocation = 0x99e
        r"""Set the location of visual flags for wrapped lines."""
        GetWrapVisualFlagsLocation = 0x99f
        r"""Retrive the location of visual flags for wrapped lines."""
        SetWrapStartIndent        = 0x9a0
        r"""Set the start indent for wrapped lines."""
        GetWrapStartIndent        = 0x9a1
        r"""Retrive the start indent for wrapped lines."""
        MarkerAddSet              = 0x9a2
        r"""Add a set of markers to a line."""
        SetPasteConvertEndings    = 0x9a3
        r"""Enable/Disable convert-on-paste for line endings"""
        GetPasteConvertEndings    = 0x9a4
        r"""Get convert-on-paste setting"""
        SelectionDuplicate        = 0x9a5
        r"""Duplicate the selection. If selection empty duplicate the line containing the caret."""
        SetCaretLineBackAlpha     = 0x9a6
        r"""Set background alpha of the caret line."""
        GetCaretLineBackAlpha     = 0x9a7
        r"""Get the background alpha of the caret line."""
        SetWrapIndentMode         = 0x9a8
        r"""Sets how wrapped sublines are placed. Default is fixed."""
        GetWrapIndentMode         = 0x9a9
        r"""Retrieve how wrapped sublines are placed. Default is fixed."""
        SelectionFromPoint        = 0x9aa
        r"""Find the selection index for a point. -1 when not at a selection."""
        MarkerSetAlpha            = 0x9ac
        r"""Set the alpha used for a marker that is drawn in the text area, not the margin."""
        GetSelAlpha               = 0x9ad
        r"""Get the alpha of the selection."""
        SetSelAlpha               = 0x9ae
        r"""Set the alpha of the selection."""
        GetSelEOLFilled           = 0x9af
        r"""Is the selection end of line filled?"""
        SetSelEOLFilled           = 0x9b0
        r"""Set the selection to have its end of line filled or not."""
        StyleGetFore              = 0x9b1
        r"""Get the foreground colour of a style."""
        StyleGetBack              = 0x9b2
        r"""Get the background colour of a style."""
        StyleGetBold              = 0x9b3
        r"""Get is a style bold or not."""
        StyleGetItalic            = 0x9b4
        r"""Get is a style italic or not."""
        StyleGetSize              = 0x9b5
        r"""Get the size of characters of a style."""
        StyleGetFont              = 0x9b6
        r"""Get the font of a style. Returns the length of the fontName Result is NUL-terminated."""
        StyleGetEOLFilled         = 0x9b7
        r"""Get is a style to have its end of line filled or not."""
        StyleGetUnderline         = 0x9b8
        r"""Get is a style underlined or not."""
        StyleGetCase              = 0x9b9
        r"""Get is a style mixed case, or to force upper or lower case."""
        StyleGetCharacterSet      = 0x9ba
        r"""Get the character get of the font in a style."""
        StyleGetVisible           = 0x9bb
        r"""Get is a style visible or not."""
        StyleGetChangeable        = 0x9bc
        r"""Get is a style changeable or not (read only). Experimental feature, currently buggy."""
        StyleGetHotSpot           = 0x9bd
        r"""Get is a style a hotspot or not."""
        GetHotspotActiveFore      = 0x9be
        r"""Get the fore colour for active hotspots."""
        GetHotspotActiveBack      = 0x9bf
        r"""Get the back colour for active hotspots."""
        GetHotspotActiveUnderline = 0x9c0
        r"""Get whether underlining for active hotspots."""
        GetHotspotSingleLine      = 0x9c1
        r"""Get the HotspotSingleLine property"""
        BraceHighlightIndicator   = 0x9c2
        r"""Use specified indicator to highlight matching braces instead of changing their style."""
        BraceBadLightIndicator    = 0x9c3
        r"""Use specified indicator to highlight non matching brace instead of changing its style."""
        SetIndicatorCurrent       = 0x9c4
        r"""Set the indicator used for IndicatorFillRange and IndicatorClearRange"""
        GetIndicatorCurrent       = 0x9c5
        r"""Get the current indicator"""
        SetIndicatorValue         = 0x9c6
        r"""Set the value used for IndicatorFillRange"""
        GetIndicatorValue         = 0x9c7
        r"""Get the current indicator value"""
        IndicatorFillRange        = 0x9c8
        r"""Turn a indicator on over a range."""
        IndicatorClearRange       = 0x9c9
        r"""Turn a indicator off over a range."""
        IndicatorAllOnFor         = 0x9ca
        r"""Are any indicators present at pos?"""
        IndicatorValueAt          = 0x9cb
        r"""What value does a particular indicator have at a position?"""
        IndicatorStart            = 0x9cc
        r"""Where does a particular indicator start?"""
        IndicatorEnd              = 0x9cd
        r"""Where does a particular indicator end?"""
        IndicSetUnder             = 0x9ce
        r"""Set an indicator to draw under text or over(default)."""
        IndicGetUnder             = 0x9cf
        r"""Retrieve whether indicator drawn under or over text."""
        SetCaretStyle             = 0x9d0
        r"""Set the style of the caret to be drawn."""
        GetCaretStyle             = 0x9d1
        r"""Returns the current style of the caret."""
        SetPositionCache          = 0x9d2
        r"""Set number of entries in position cache"""
        GetPositionCache          = 0x9d3
        r"""How many entries are allocated to the position cache?"""
        SetScrollWidthTracking    = 0x9d4
        r"""Sets whether the maximum width line displayed is used to set scroll width."""
        GetScrollWidthTracking    = 0x9d5
        r"""Retrieve whether the scroll width tracks wide lines."""
        DelWordRightEnd           = 0x9d6
        r"""Delete the word to the right of the caret, but not the trailing non-word characters."""
        CopyAllowLine             = 0x9d7
        r"""Copy the selection, if selection empty copy the line with the caret"""
        GetCharacterPointer       = 0x9d8
        r"""Compact the document buffer and return a read-only pointer to the characters in the document."""
        IndicSetAlpha             = 0x9db
        r"""Set the alpha fill colour of the given indicator."""
        IndicGetAlpha             = 0x9dc
        r"""Get the alpha fill colour of the given indicator."""
        SetExtraAscent            = 0x9dd
        r"""Set extra ascent for each line"""
        GetExtraAscent            = 0x9de
        r"""Get extra ascent for each line"""
        SetExtraDescent           = 0x9df
        r"""Set extra descent for each line"""
        GetExtraDescent           = 0x9e0
        r"""Get extra descent for each line"""
        MarkerSymbolDefined       = 0x9e1
        r"""Which symbol was defined for markerNumber with MarkerDefine"""
        MarginSetText             = 0x9e2
        r"""Set the text in the text margin for a line"""
        MarginGetText             = 0x9e3
        r"""Get the text in the text margin for a line"""
        MarginSetStyle            = 0x9e4
        r"""Set the style number for the text margin for a line"""
        MarginGetStyle            = 0x9e5
        r"""Get the style number for the text margin for a line"""
        MarginSetStyles           = 0x9e6
        r"""Set the style in the text margin for a line"""
        MarginGetStyles           = 0x9e7
        r"""Get the styles in the text margin for a line"""
        MarginTextClearAll        = 0x9e8
        r"""Clear the margin text on all lines"""
        MarginSetStyleOffset      = 0x9e9
        r"""Get the start of the range of style numbers used for margin text"""
        MarginGetStyleOffset      = 0x9ea
        r"""Get the start of the range of style numbers used for margin text"""
        SetMarginOptions          = 0x9eb
        r"""Set the margin options."""
        AnnotationSetText         = 0x9ec
        r"""Set the annotation text for a line"""
        AnnotationGetText         = 0x9ed
        r"""Get the annotation text for a line"""
        AnnotationSetStyle        = 0x9ee
        r"""Set the style number for the annotations for a line"""
        AnnotationGetStyle        = 0x9ef
        r"""Get the style number for the annotations for a line"""
        AnnotationSetStyles       = 0x9f0
        r"""Set the annotation styles for a line"""
        AnnotationGetStyles       = 0x9f1
        r"""Get the annotation styles for a line"""
        AnnotationGetLines        = 0x9f2
        r"""Get the number of annotation lines for a line"""
        AnnotationClearAll        = 0x9f3
        r"""Clear the annotations from all lines"""
        AnnotationSetVisible      = 0x9f4
        r"""Set the visibility for the annotations for a view"""
        AnnotationGetVisible      = 0x9f5
        r"""Get the visibility for the annotations for a view"""
        AnnotationSetStyleOffset  = 0x9f6
        r"""Get the start of the range of style numbers used for annotations"""
        AnnotationGetStyleOffset  = 0x9f7
        r"""Get the start of the range of style numbers used for annotations"""
        ReleaseAllExtendedStyles  = 0x9f8
        r"""Release all extended (>255) style numbers"""
        AllocateExtendedStyles    = 0x9f9
        r"""Allocate some extended (>255) style numbers and return the start of the range"""
        SetEmptySelection         = 0x9fc
        r"""Set caret to a position, while removing any existing selection."""
        GetMarginOptions          = 0x9fd
        r"""Get the margin options."""
        IndicSetOutlineAlpha      = 0x9fe
        r"""Set the alpha outline colour of the given indicator."""
        IndicGetOutlineAlpha      = 0x9ff
        r"""Get the alpha outline colour of the given indicator."""
        AddUndoAction             = 0xa00
        r"""Add a container action to the undo stack"""
        CharPositionFromPoint     = 0xa01
        r"""Find the position of a character from a point within the window."""
        CharPositionFromPointClose = 0xa02
        r"""Find the position of a character from a point within the window. Return INVALID_POSITION if not close to text."""
        SetMultipleSelection      = 0xa03
        r"""Set whether multiple selections can be made"""
        GetMultipleSelection      = 0xa04
        r"""Whether multiple selections can be made"""
        SetAdditionalSelectionTyping = 0xa05
        r"""Set whether typing can be performed into multiple selections"""
        GetAdditionalSelectionTyping = 0xa06
        r"""Whether typing can be performed into multiple selections"""
        SetAdditionalCaretsBlink  = 0xa07
        r"""Set whether additional carets will blink"""
        GetAdditionalCaretsBlink  = 0xa08
        r"""Whether additional carets will blink"""
        ScrollRange               = 0xa09
        r"""Scroll the argument positions and the range between them into view giving priority to the primary position then the secondary position. This may be used to make a search match visible."""
        GetSelections             = 0xa0a
        r"""How many selections are there?"""
        ClearSelections           = 0xa0b
        r"""Clear selections to a single empty stream selection"""
        SetSelection              = 0xa0c
        r"""Set a simple selection"""
        AddSelection              = 0xa0d
        r"""Add a selection"""
        SetMainSelection          = 0xa0e
        r"""Set the main selection"""
        GetMainSelection          = 0xa0f
        r"""Which selection is the main selection"""
        SetSelectionNCaret        = 0xa10
        r"""Set the caret position of the nth selection."""
        GetSelectionNCaret        = 0xa11
        r"""Return the caret position of the nth selection."""
        SetSelectionNAnchor       = 0xa12
        r"""Set the anchor position of the nth selection."""
        GetSelectionNAnchor       = 0xa13
        r"""Return the anchor position of the nth selection."""
        SetSelectionNCaretVirtualSpace = 0xa14
        r"""Set the virtual space of the caret of the nth selection."""
        GetSelectionNCaretVirtualSpace = 0xa15
        r"""Return the virtual space of the caret of the nth selection."""
        SetSelectionNAnchorVirtualSpace = 0xa16
        r"""Set the virtual space of the anchor of the nth selection."""
        GetSelectionNAnchorVirtualSpace = 0xa17
        r"""Return the virtual space of the anchor of the nth selection."""
        SetSelectionNStart        = 0xa18
        r"""Sets the position that starts the selection - this becomes the anchor."""
        GetSelectionNStart        = 0xa19
        r"""Returns the position at the start of the selection."""
        SetSelectionNEnd          = 0xa1a
        r"""Sets the position that ends the selection - this becomes the currentPosition."""
        GetSelectionNEnd          = 0xa1b
        r"""Returns the position at the end of the selection."""
        SetRectangularSelectionCaret = 0xa1c
        r"""Set the caret position of the rectangular selection."""
        GetRectangularSelectionCaret = 0xa1d
        r"""Return the caret position of the rectangular selection."""
        SetRectangularSelectionAnchor = 0xa1e
        r"""Set the anchor position of the rectangular selection."""
        GetRectangularSelectionAnchor = 0xa1f
        r"""Return the anchor position of the rectangular selection."""
        SetRectangularSelectionCaretVirtualSpace = 0xa20
        r"""Set the virtual space of the caret of the rectangular selection."""
        GetRectangularSelectionCaretVirtualSpace = 0xa21
        r"""Return the virtual space of the caret of the rectangular selection."""
        SetRectangularSelectionAnchorVirtualSpace = 0xa22
        r"""Set the virtual space of the anchor of the rectangular selection."""
        GetRectangularSelectionAnchorVirtualSpace = 0xa23
        r"""Return the virtual space of the anchor of the rectangular selection."""
        SetVirtualSpaceOptions    = 0xa24
        r"""Set options for virtual space behaviour."""
        GetVirtualSpaceOptions    = 0xa25
        r"""Return options for virtual space behaviour."""
        SetRectangularSelectionModifier = 0xa26
        GetRectangularSelectionModifier = 0xa27
        r"""Get the modifier key used for rectangular selection."""
        SetAdditionalSelFore      = 0xa28
        r"""Set the foreground colour of additional selections. Must have previously called SetSelFore with non-zero first argument for this to have an effect."""
        SetAdditionalSelBack      = 0xa29
        r"""Set the background colour of additional selections. Must have previously called SetSelBack with non-zero first argument for this to have an effect."""
        SetAdditionalSelAlpha     = 0xa2a
        r"""Set the alpha of the selection."""
        GetAdditionalSelAlpha     = 0xa2b
        r"""Get the alpha of the selection."""
        SetAdditionalCaretFore    = 0xa2c
        r"""Set the foreground colour of additional carets."""
        GetAdditionalCaretFore    = 0xa2d
        r"""Get the foreground colour of additional carets."""
        RotateSelection           = 0xa2e
        r"""Set the main selection to the next selection."""
        SwapMainAnchorCaret       = 0xa2f
        r"""Swap that caret and anchor of the main selection."""
        SetAdditionalCaretsVisible = 0xa30
        r"""Set whether additional carets are visible"""
        GetAdditionalCaretsVisible = 0xa31
        r"""Whether additional carets are visible"""
        AutoCGetCurrentText       = 0xa32
        r"""Get currently selected item text in the auto-completion list Returns the length of the item text Result is NUL-terminated."""
        SetFontQuality            = 0xa33
        r"""Choose the quality level for text from the FontQuality enumeration."""
        GetFontQuality            = 0xa34
        r"""Retrieve the quality level for text."""
        SetFirstVisibleLine       = 0xa35
        r"""Scroll so that a display line is at the top of the display."""
        SetMultiPaste             = 0xa36
        r"""Change the effect of pasting when there are multiple selections."""
        GetMultiPaste             = 0xa37
        r"""Retrieve the effect of pasting when there are multiple selections."""
        GetTag                    = 0xa38
        r"""Retrieve the value of a tag from a regular expression search. Result is NUL-terminated."""
        ChangeLexerState          = 0xa39
        r"""Indicate that the internal state of a lexer has changed over a range and therefore there may be a need to redraw."""
        ContractedFoldNext        = 0xa3a
        r"""Find the next line at or after lineStart that is a contracted fold header line. Return -1 when no more lines."""
        VerticalCentreCaret       = 0xa3b
        r"""Centre current line in window."""
        MoveSelectedLinesUp       = 0xa3c
        r"""Move the selected lines up one line, shifting the line above after the selection"""
        MoveSelectedLinesDown     = 0xa3d
        r"""Move the selected lines down one line, shifting the line below before the selection"""
        SetIdentifier             = 0xa3e
        r"""Set the identifier reported as idFrom in notification messages."""
        GetIdentifier             = 0xa3f
        r"""Get the identifier."""
        RGBAImageSetWidth         = 0xa40
        r"""Set the width for future RGBA image data."""
        RGBAImageSetHeight        = 0xa41
        r"""Set the height for future RGBA image data."""
        MarkerDefineRGBAImage     = 0xa42
        r"""Define a marker from RGBA data. It has the width and height from RGBAImageSetWidth/Height"""
        RegisterRGBAImage         = 0xa43
        r"""Register an RGBA image for use in autocompletion lists. It has the width and height from RGBAImageSetWidth/Height"""
        ScrollToStart             = 0xa44
        r"""Scroll to start of document."""
        ScrollToEnd               = 0xa45
        r"""Scroll to end of document."""
        SetTechnology             = 0xa46
        r"""Set the technology used."""
        GetTechnology             = 0xa47
        r"""Get the tech."""
        CreateLoader              = 0xa48
        r"""Create an ILoader*."""
        CountCharacters           = 0xa49
        r"""Count characters between two positions."""
        AutoCSetCaseInsensitiveBehaviour = 0xa4a
        r"""Set auto-completion case insensitive behaviour to either prefer case-sensitive matches or have no preference."""
        AutoCGetCaseInsensitiveBehaviour = 0xa4b
        r"""Get auto-completion case insensitive behaviour."""
        AutoCSetMulti             = 0xa4c
        r"""Change the effect of autocompleting when there are multiple selections."""
        AutoCGetMulti             = 0xa4d
        r"""Retrieve the effect of autocompleting when there are multiple selections."""
        AutoCSetOptions           = 0xa4e
        r"""Set autocompletion options."""
        AutoCGetOptions           = 0xa4f
        r"""Retrieve autocompletion options."""
        FindIndicatorShow         = 0xa50
        r"""On macOS, show a find indicator."""
        FindIndicatorFlash        = 0xa51
        r"""On macOS, flash a find indicator, then fade out."""
        FindIndicatorHide         = 0xa52
        r"""On macOS, hide the find indicator."""
        GetRangePointer           = 0xa53
        r"""Return a read-only pointer to a range of characters in the document. May move the gap so that the range is contiguous, but will only move up to lengthRange bytes."""
        GetGapPosition            = 0xa54
        r"""Return a position which, to avoid performance costs, should not be within the range of a call to GetRangePointer."""
        DeleteRange               = 0xa55
        r"""Delete a range of text in the document."""
        GetWordChars              = 0xa56
        r"""Get the set of characters making up words for when moving or selecting by word. Returns the number of characters"""
        GetWhitespaceChars        = 0xa57
        r"""Get the set of characters making up whitespace for when moving or selecting by word."""
        SetPunctuationChars       = 0xa58
        r"""Set the set of characters making up punctuation characters Should be called after SetWordChars."""
        GetPunctuationChars       = 0xa59
        r"""Get the set of characters making up punctuation characters"""
        GetSelectionEmpty         = 0xa5a
        r"""Is every selected range empty?"""
        RGBAImageSetScale         = 0xa5b
        r"""Set the scale factor in percent for future RGBA image data."""
        VCHomeDisplay             = 0xa5c
        r"""Move caret to before first visible character on display line. If already there move to first character on display line."""
        VCHomeDisplayExtend       = 0xa5d
        r"""Like VCHomeDisplay but extending selection to new caret position."""
        GetCaretLineVisibleAlways = 0xa5e
        r"""Is the caret line always visible?"""
        SetCaretLineVisibleAlways = 0xa5f
        r"""Sets the caret line to always visible."""
        SetLineEndTypesAllowed    = 0xa60
        r"""Set the line end types that the application wants to use. May not be used if incompatible with lexer or encoding."""
        GetLineEndTypesAllowed    = 0xa61
        r"""Get the line end types currently allowed."""
        GetLineEndTypesActive     = 0xa62
        r"""Get the line end types currently recognised. May be a subset of the allowed types due to lexer limitation."""
        ChangeSelectionMode       = 0xa63
        r"""Set the selection mode to stream (SC_SEL_STREAM) or rectangular (SC_SEL_RECTANGLE/SC_SEL_THIN) or by lines (SC_SEL_LINES) without changing MoveExtendsSelection."""
        AutoCSetOrder             = 0xa64
        r"""Set the way autocompletion lists are ordered."""
        AutoCGetOrder             = 0xa65
        r"""Get the way autocompletion lists are ordered."""
        FoldAll                   = 0xa66
        r"""Expand or contract all fold headers."""
        SetAutomaticFold          = 0xa67
        r"""Set automatic folding behaviours."""
        GetAutomaticFold          = 0xa68
        r"""Get automatic folding behaviours."""
        SetRepresentation         = 0xa69
        r"""Set the way a character is drawn."""
        GetRepresentation         = 0xa6a
        r"""Get the way a character is drawn. Result is NUL-terminated."""
        ClearRepresentation       = 0xa6b
        r"""Remove a character representation."""
        SetMouseSelectionRectangularSwitch = 0xa6c
        r"""Set whether switching to rectangular mode while selecting with the mouse is allowed."""
        GetMouseSelectionRectangularSwitch = 0xa6d
        r"""Whether switching to rectangular mode while selecting with the mouse is allowed."""
        PositionRelative          = 0xa6e
        r"""Given a valid document position, return a position that differs in a number of characters. Returned value is always between 0 and last position in document."""
        DropSelectionN            = 0xa6f
        r"""Drop one selection"""
        ChangeInsertion           = 0xa70
        r"""Change the text that is being inserted in response to SC_MOD_INSERTCHECK"""
        GetPhasesDraw             = 0xa71
        r"""How many phases is drawing done in?"""
        SetPhasesDraw             = 0xa72
        r"""In one phase draw, text is drawn in a series of rectangular blocks with no overlap. In two phase draw, text is drawn in a series of lines allowing runs to overlap horizontally. In multiple phase draw, each element is drawn over the whole drawing area, allowing text to overlap from one line to the next."""
        ClearTabStops             = 0xa73
        r"""Clear explicit tabstops on a line."""
        AddTabStop                = 0xa74
        r"""Add an explicit tab stop for a line."""
        GetNextTabStop            = 0xa75
        r"""Find the next explicit tab stop position on a line after a position."""
        GetIMEInteraction         = 0xa76
        r"""Is the IME displayed in a window or inline?"""
        SetIMEInteraction         = 0xa77
        r"""Choose to display the IME in a window or inline."""
        IndicSetHoverStyle        = 0xa78
        r"""Set a hover indicator to plain, squiggle or TT."""
        IndicGetHoverStyle        = 0xa79
        r"""Retrieve the hover style of an indicator."""
        IndicSetHoverFore         = 0xa7a
        r"""Set the foreground hover colour of an indicator."""
        IndicGetHoverFore         = 0xa7b
        r"""Retrieve the foreground hover colour of an indicator."""
        IndicSetFlags             = 0xa7c
        r"""Set the attributes of an indicator."""
        IndicGetFlags             = 0xa7d
        r"""Retrieve the attributes of an indicator."""
        SetTargetRange            = 0xa7e
        r"""Sets both the start and end of the target in one call."""
        GetTargetText             = 0xa7f
        r"""Retrieve the text in the target."""
        MultipleSelectAddNext     = 0xa80
        r"""Add the next occurrence of the main selection to the set of selections as main. If the current selection is empty then select word around caret."""
        MultipleSelectAddEach     = 0xa81
        r"""Add each occurrence of the main selection in the target to the set of selections. If the current selection is empty then select word around caret."""
        TargetWholeDocument       = 0xa82
        r"""Sets the target to the whole document."""
        IsRangeWord               = 0xa83
        r"""Is the range start..end considered a word?"""
        SetIdleStyling            = 0xa84
        r"""Sets limits to idle styling."""
        GetIdleStyling            = 0xa85
        r"""Retrieve the limits to idle styling."""
        MultiEdgeAddLine          = 0xa86
        r"""Add a new vertical edge to the view."""
        MultiEdgeClearAll         = 0xa87
        r"""Clear all vertical edges."""
        SetMouseWheelCaptures     = 0xa88
        r"""Set whether the mouse wheel can be active outside the window."""
        GetMouseWheelCaptures     = 0xa89
        r"""Get whether mouse wheel can be active outside the window."""
        GetTabDrawMode            = 0xa8a
        r"""Retrieve the current tab draw mode. Returns one of SCTD_* constants."""
        SetTabDrawMode            = 0xa8b
        r"""Set how tabs are drawn when visible."""
        ToggleFoldShowText        = 0xa8c
        r"""Switch a header line between expanded and contracted and show some text after the line."""
        FoldDisplayTextSetStyle   = 0xa8d
        r"""Set the style of fold display text."""
        SetAccessibility          = 0xa8e
        r"""Enable or disable accessibility."""
        GetAccessibility          = 0xa8f
        r"""Report accessibility status."""
        GetCaretLineFrame         = 0xa90
        r"""Retrieve the caret line frame width. Width = 0 means this option is disabled."""
        SetCaretLineFrame         = 0xa91
        r"""Display the caret line framed. Set width != 0 to enable this option and width = 0 to disable it."""
        GetMoveExtendsSelection   = 0xa92
        r"""Get whether or not regular caret moves will extend or reduce the selection."""
        FoldDisplayTextGetStyle   = 0xa93
        r"""Get the style of fold display text."""
        GetBidirectional          = 0xa94
        r"""Retrieve bidirectional text display state."""
        SetBidirectional          = 0xa95
        r"""Set bidirectional text display state."""
        GetLineCharacterIndex     = 0xa96
        r"""Retrieve line character index state."""
        AllocateLineCharacterIndex = 0xa97
        r"""Request line character index be created or its use count increased."""
        ReleaseLineCharacterIndex = 0xa98
        r"""Decrease use count of line character index and remove if 0."""
        LineFromIndexPosition     = 0xa99
        r"""Retrieve the document line containing a position measured in index units."""
        IndexPositionFromLine     = 0xa9a
        r"""Retrieve the position measured in index units at the start of a document line."""
        CountCodeUnits            = 0xa9b
        r"""Count code units between two positions."""
        PositionRelativeCodeUnits = 0xa9c
        r"""Given a valid document position, return a position that differs in a number of UTF-16 code units. Returned value is always between 0 and last position in document. The result may point half way (2 bytes) inside a non-BMP character."""
        SetCommandEvents          = 0xa9d
        r"""Set whether command events are sent to the container."""
        GetCommandEvents          = 0xa9e
        r"""Get whether command events are sent to the container."""
        SetMoveExtendsSelection   = 0xa9f
        r"""Set whether or not regular caret moves will extend or reduce the selection."""
        SetCharacterCategoryOptimization = 0xaa0
        r"""Set the number of characters to have directly indexed categories"""
        GetCharacterCategoryOptimization = 0xaa1
        r"""Get the number of characters to have directly indexed categories"""
        SetDefaultFoldDisplayText = 0xaa2
        r"""Set the default fold display text."""
        GetDefaultFoldDisplayText = 0xaa3
        r"""Get the default fold display text."""
        SetTabMinimumWidth        = 0xaa4
        r"""Set the minimum visual width of a tab."""
        GetTabMinimumWidth        = 0xaa5
        r"""Get the minimum visual width of a tab."""
        GetSelectionNStartVirtualSpace = 0xaa6
        r"""Returns the virtual space at the start of the selection."""
        GetSelectionNEndVirtualSpace = 0xaa7
        r"""Returns the virtual space at the end of the selection."""
        SetTargetStartVirtualSpace = 0xaa8
        r"""Sets the virtual space of the target start"""
        GetTargetStartVirtualSpace = 0xaa9
        r"""Get the virtual space of the target start"""
        SetTargetEndVirtualSpace  = 0xaaa
        r"""Sets the virtual space of the target end"""
        GetTargetEndVirtualSpace  = 0xaab
        r"""Get the virtual space of the target end"""
        MarkerHandleFromLine      = 0xaac
        r"""Retrieve marker handles of a line"""
        MarkerNumberFromLine      = 0xaad
        r"""Retrieve marker number of a marker handle"""
        MarkerGetLayer            = 0xaae
        r"""Get the layer used for a marker that is drawn in the text area, not the margin."""
        MarkerSetLayer            = 0xaaf
        r"""Set the layer used for a marker that is drawn in the text area, not the margin."""
        EOLAnnotationSetText      = 0xab4
        r"""Set the end of line annotation text for a line"""
        EOLAnnotationGetText      = 0xab5
        r"""Get the end of line annotation text for a line"""
        EOLAnnotationSetStyle     = 0xab6
        r"""Set the style number for the end of line annotations for a line"""
        EOLAnnotationGetStyle     = 0xab7
        r"""Get the style number for the end of line annotations for a line"""
        EOLAnnotationClearAll     = 0xab8
        r"""Clear the end of annotations from all lines"""
        EOLAnnotationSetVisible   = 0xab9
        r"""Set the visibility for the end of line annotations for a view"""
        EOLAnnotationGetVisible   = 0xaba
        r"""Get the visibility for the end of line annotations for a view"""
        EOLAnnotationSetStyleOffset = 0xabb
        r"""Get the start of the range of style numbers used for end of line annotations"""
        EOLAnnotationGetStyleOffset = 0xabc
        r"""Get the start of the range of style numbers used for end of line annotations"""
        GetMultiEdgeColumn        = 0xabd
        r"""Get multi edge positions."""
        SupportsFeature           = 0xabe
        r"""Get whether a feature is supported"""
        IndicSetStrokeWidth       = 0xabf
        r"""Set the stroke width of an indicator in hundredths of a pixel."""
        IndicGetStrokeWidth       = 0xac0
        r"""Retrieve the stroke width of an indicator."""
        SetElementColour          = 0xac1
        r"""Set the colour of an element. Translucency (alpha) may or may not be significant and this may depend on the platform. The alpha byte should commonly be 0xff for opaque."""
        GetElementColour          = 0xac2
        r"""Get the colour of an element."""
        ResetElementColour        = 0xac3
        r"""Use the default or platform-defined colour for an element."""
        GetElementIsSet           = 0xac4
        r"""Get whether an element has been set by SetElementColour. When false, a platform-defined or default colour is used."""
        GetElementAllowsTranslucent = 0xac5
        r"""Get whether an element supports translucency."""
        GetElementBaseColour      = 0xac6
        r"""Get the colour of an element."""
        SetFontLocale             = 0xac8
        r"""Set the locale for displaying text."""
        GetFontLocale             = 0xac9
        r"""Get the locale for displaying text."""
        GetSelectionLayer         = 0xaca
        r"""Get the layer for drawing selections"""
        SetSelectionLayer         = 0xacb
        r"""Set the layer for drawing selections: either opaquely on base layer or translucently over text"""
        GetCaretLineLayer         = 0xacc
        r"""Get the layer of the background of the line containing the caret."""
        SetCaretLineLayer         = 0xacd
        r"""Set the layer of the background of the line containing the caret."""
        SetRepresentationAppearance = 0xace
        r"""Set the appearance of a representation."""
        GetRepresentationAppearance = 0xacf
        r"""Get the appearance of a representation."""
        SetRepresentationColour   = 0xad0
        r"""Set the colour of a representation."""
        GetRepresentationColour   = 0xad1
        r"""Get the colour of a representation."""
        ClearAllRepresentations   = 0xad2
        r"""Clear representations to default."""
        ReplaceRectangular        = 0xad3
        r"""Replace the selection with text like a rectangular paste."""
        GetDirectStatusFunction   = 0xad4
        r"""Retrieve a pointer to a function that processes messages for this Scintilla and returns status."""
        GetCaretLineHighlightSubLine = 0xad5
        r"""Get only highlighting subline instead of whole line."""
        SetCaretLineHighlightSubLine = 0xad6
        r"""Set only highlighting subline instead of whole line."""
        SetLayoutThreads          = 0xad7
        r"""Set maximum number of threads used for layout"""
        GetLayoutThreads          = 0xad8
        r"""Get maximum number of threads used for layout"""
        FormatRangeFull           = 0xad9
        r"""Draw the document into a display context such as a printer."""
        GetStyledTextFull         = 0xada
        r"""Retrieve a buffer of cells that can be past 2GB. Returns the number of bytes in the buffer not including terminating NULs."""
        ReplaceTargetMinimal      = 0xadb
        r"""Replace the target text with the argument text but ignore prefix and suffix that are the same as current."""
        SetChangeHistory          = 0xadc
        r"""Enable or disable change history."""
        GetChangeHistory          = 0xadd
        r"""Report change history status."""
        SetUndoSelectionHistory   = 0xade
        r"""Enable or disable undo selection history."""
        GetUndoSelectionHistory   = 0xadf
        r"""Report undo selection history status."""
        SetSelectionSerialized    = 0xae0
        r"""Set selection from serialized form."""
        GetSelectionSerialized    = 0xae1
        r"""Retrieve serialized form of selection."""
        GetUndoActions            = 0xae6
        r"""How many undo actions are in the history?"""
        SetUndoSavePoint          = 0xae7
        r"""Set action as the save point"""
        GetUndoSavePoint          = 0xae8
        r"""Which action is the save point?"""
        SetUndoDetach             = 0xae9
        r"""Set action as the detach point"""
        GetUndoDetach             = 0xaea
        r"""Which action is the detach point?"""
        SetUndoTentative          = 0xaeb
        r"""Set action as the tentative point"""
        GetUndoTentative          = 0xaec
        r"""Which action is the tentative point?"""
        SetUndoCurrent            = 0xaed
        r"""Set action as the current point"""
        GetUndoCurrent            = 0xaee
        r"""Which action is the current point?"""
        GetUndoSequence           = 0xaef
        r"""Is an undo sequence active?"""
        PushUndoActionType        = 0xaf0
        r"""Push one action onto undo history with no text"""
        ChangeLastUndoActionText  = 0xaf1
        r"""Set the text and length of the most recently pushed action"""
        GetUndoActionType         = 0xaf2
        r"""What is the type of an action?"""
        GetUndoActionPosition     = 0xaf3
        r"""What is the position of an action?"""
        GetUndoActionText         = 0xaf4
        r"""What is the text of an action?"""
        CutAllowLine              = 0xafa
        r"""Cut the selection, if selection empty cut the line with the caret"""
        SetCopySeparator          = 0xafb
        r"""Set the string to separate parts when copying a multiple selection."""
        GetCopySeparator          = 0xafc
        r"""Get the string to separate parts when copying a multiple selection."""
        LineIndent                = 0xafd
        r"""Indent the current and selected lines."""
        LineDedent                = 0xafe
        r"""Dedent the current and selected lines."""
        AutoCSetImageScale        = 0xaff
        r"""Set the scale factor in percent for auto-completion list images."""
        AutoCGetImageScale        = 0xb00
        r"""Get the scale factor in percent for auto-completion list images."""
        ScrollVertical            = 0xb01
        r"""Scroll vertically with allowance for wrapping."""
        GetDragDropEnabled        = 0xb02
        r"""Get whether drag-and-drop is enabled or disabled"""
        SetDragDropEnabled        = 0xb03
        r"""Enable or disable drag-and-drop"""
        StartRecord               = 0xbb9
        r"""Start notifying the container of all key presses and commands."""
        StopRecord                = 0xbba
        r"""Stop notifying the container of all key presses and commands."""
        GetLexer                  = 0xfa2
        r"""Retrieve the lexing language of the document."""
        Colourise                 = 0xfa3
        r"""Colourise a segment of the document using the current lexing language."""
        SetProperty               = 0xfa4
        r"""Set up a value that may be used by a lexer for some optional feature."""
        SetKeyWords               = 0xfa5
        r"""Set up the key words used by the lexer."""
        GetProperty               = 0xfa8
        r"""Retrieve a "property" value previously set with SetProperty. Result is NUL-terminated."""
        GetPropertyExpanded       = 0xfa9
        r"""Retrieve a "property" value previously set with SetProperty, with "$()" variable replacement on returned buffer. Result is NUL-terminated."""
        GetPropertyInt            = 0xfaa
        r"""Retrieve a "property" value previously set with SetProperty, interpreted as an int AFTER any "$()" variable replacement."""
        GetLexerLanguage          = 0xfac
        r"""Retrieve the name of the lexer. Return the length of the text. Result is NUL-terminated."""
        PrivateLexerCall          = 0xfad
        r"""For private communication between an application and a known lexer."""
        PropertyNames             = 0xfae
        r"""Retrieve a '\n' separated list of properties understood by the current lexer. Result is NUL-terminated."""
        PropertyType              = 0xfaf
        r"""Retrieve the type of a property."""
        DescribeProperty          = 0xfb0
        r"""Describe a property. Result is NUL-terminated."""
        DescribeKeyWordSets       = 0xfb1
        r"""Retrieve a '\n' separated list of descriptions of the keyword sets understood by the current lexer. Result is NUL-terminated."""
        GetLineEndTypesSupported  = 0xfb2
        r"""Bit set of LineEndType enumertion for which line ends beyond the standard LF, CR, and CRLF are supported by the lexer."""
        AllocateSubStyles         = 0xfb4
        r"""Allocate a set of sub styles for a particular base style, returning start of range"""
        GetSubStylesStart         = 0xfb5
        r"""The starting style number for the sub styles associated with a base style"""
        GetSubStylesLength        = 0xfb6
        r"""The number of sub styles associated with a base style"""
        FreeSubStyles             = 0xfb7
        r"""Free allocated sub styles"""
        SetIdentifiers            = 0xfb8
        r"""Set the identifiers that are shown in a particular style"""
        DistanceToSecondaryStyles = 0xfb9
        r"""Where styles are duplicated by a feature such as active/inactive code return the distance between the two types."""
        GetSubStyleBases          = 0xfba
        r"""Get the set of base styles that can be extended with sub styles Result is NUL-terminated."""
        GetStyleFromSubStyle      = 0xfbb
        r"""For a sub style, return the base style, else return the argument."""
        GetPrimaryStyleFromStyle  = 0xfbc
        r"""For a secondary style, return the primary style, else return the argument."""
        GetNamedStyles            = 0xfbd
        r"""Retrieve the number of named styles for the lexer."""
        NameOfStyle               = 0xfbe
        r"""Retrieve the name of a style. Result is NUL-terminated."""
        TagsOfStyle               = 0xfbf
        r"""Retrieve a ' ' separated list of style tags like "literal quoted string". Result is NUL-terminated."""
        DescriptionOfStyle        = 0xfc0
        r"""Retrieve a description of a style. Result is NUL-terminated."""
        SetILexer                 = 0xfc1
        r"""Set the lexer from an ILexer*."""

    class ModificationFlags(enum.IntEnum):

        None_                     = 0x0
        r"""Base value with no fields valid. Will not occur but is useful in tests."""
        InsertText                = 0x1
        r"""Text has been inserted into the document."""
        DeleteText                = 0x2
        r"""Text has been removed from the document."""
        ChangeStyle               = 0x4
        r"""A style change has occurred."""
        ChangeFold                = 0x8
        r"""A folding change has occurred."""
        User                      = 0x10
        r"""Information: the operation was done by the user."""
        Undo                      = 0x20
        r"""Information: this was the result of an Undo."""
        Redo                      = 0x40
        r"""Information: this was the result of a Redo."""
        MultiStepUndoRedo         = 0x80
        r"""This is part of a multi-step Undo or Redo transaction."""
        LastStepInUndoRedo        = 0x100
        r"""This is the final step in an Undo or Redo transaction."""
        ChangeMarker              = 0x200
        r"""One or more markers has changed in a line."""
        BeforeInsert              = 0x400
        r"""Text is about to be inserted into the document."""
        BeforeDelete              = 0x800
        r"""Text is about to be deleted from the document."""
        MultilineUndoRedo         = 0x1000
        r"""This is part of an Undo or Redo with multi-line changes."""
        StartAction               = 0x2000
        r"""Set on a SC_PERFORMED_USER action that is the first or only step in an undo transaction."""
        ChangeIndicator           = 0x4000
        r"""An indicator has been added or removed from a range of text."""
        ChangeLineState           = 0x8000
        r"""A line state has changed because SCI_SETLINESTATE was called."""
        ChangeMargin              = 0x10000
        r"""A text margin has changed."""
        ChangeAnnotation          = 0x20000
        r"""An annotation has changed."""
        Container                 = 0x40000
        r"""Set on actions that the container stored into the undo stack with SCI_ADDUNDOACTION."""
        LexerState                = 0x80000
        r"""The internal state of a lexer has changed over a range."""
        InsertCheck               = 0x100000
        r"""Text is about to be inserted; the handler may change it via SCI_CHANGEINSERTION."""
        ChangeTabStops            = 0x200000
        r"""The explicit tab stops on a line have changed because SCI_CLEARTABSTOPS or SCI_ADDTABSTOP was called."""
        ChangeEOLAnnotation       = 0x400000
        r"""An EOL annotation has changed."""
        EventMaskAll              = 0x7fffff
        r"""Mask for all valid flags; the default mask state set by SCI_SETMODEVENTMASK."""

    class Notification(enum.IntEnum):

        StyleNeeded               = 0x7d0
        CharAdded                 = 0x7d1
        SavePointReached          = 0x7d2
        SavePointLeft             = 0x7d3
        ModifyAttemptRO           = 0x7d4
        Key                       = 0x7d5
        DoubleClick               = 0x7d6
        UpdateUI                  = 0x7d7
        Modified                  = 0x7d8
        MacroRecord               = 0x7d9
        MarginClick               = 0x7da
        NeedShown                 = 0x7db
        Painted                   = 0x7dd
        UserListSelection         = 0x7de
        URIDropped                = 0x7df
        DwellStart                = 0x7e0
        DwellEnd                  = 0x7e1
        Zoom                      = 0x7e2
        HotSpotClick              = 0x7e3
        HotSpotDoubleClick        = 0x7e4
        CallTipClick              = 0x7e5
        AutoCSelection            = 0x7e6
        IndicatorClick            = 0x7e7
        IndicatorRelease          = 0x7e8
        AutoCCancelled            = 0x7e9
        AutoCCharDeleted          = 0x7ea
        HotSpotReleaseClick       = 0x7eb
        FocusIn                   = 0x7ec
        FocusOut                  = 0x7ed
        AutoCCompleted            = 0x7ee
        MarginRightClick          = 0x7ef
        AutoCSelectionChange      = 0x7f0

    class NotificationData(Shiboken.Object):

        annotationLinesAdded      = ...  # type: Scintilla.Position
        ch                        = ...  # type: int
        characterSource           = ...  # type: _pyside6_scintilla.Scintilla.CharacterSource
        foldLevelNow              = ...  # type: _pyside6_scintilla.Scintilla.FoldLevel
        foldLevelPrev             = ...  # type: _pyside6_scintilla.Scintilla.FoldLevel
        lParam                    = ...  # type: Scintilla.sptr_t
        length                    = ...  # type: Scintilla.Position
        line                      = ...  # type: Scintilla.Position
        linesAdded                = ...  # type: Scintilla.Position
        listCompletionMethod      = ...  # type: _pyside6_scintilla.Scintilla.CompletionMethods
        listType                  = ...  # type: int
        margin                    = ...  # type: int
        modificationType          = ...  # type: _pyside6_scintilla.Scintilla.ModificationFlags
        modifiers                 = ...  # type: _pyside6_scintilla.Scintilla.KeyMod
        position                  = ...  # type: Scintilla.Position
        text                      = ...  # type: str
        token                     = ...  # type: int
        updated                   = ...  # type: _pyside6_scintilla.Scintilla.Update
        wParam                    = ...  # type: Scintilla.uptr_t
        x                         = ...  # type: int
        y                         = ...  # type: int

        @typing.overload
        def __init__(self, /) -> None: ...
        @typing.overload
        def __init__(self, NotificationData: _pyside6_scintilla.Scintilla.NotificationData, /) -> None: ...

        def __copy__(self, /) -> typing.Self: ...

    class StylesCommon(enum.IntEnum):

        Default                   = 0x20
        LineNumber                = 0x21
        BraceLight                = 0x22
        BraceBad                  = 0x23
        ControlChar               = 0x24
        IndentGuide               = 0x25
        CallTip                   = 0x26
        FoldDisplayText           = 0x27
        LastPredefined            = 0x27
        Max                       = 0xff

    class Update(enum.IntEnum):

        None_                     = 0x0
        r"""Value without any changes."""
        Content                   = 0x1
        r"""Contents, styling or markers may have been changed."""
        Selection                 = 0x2
        r"""Selection may have been changed."""
        VScroll                   = 0x4
        r"""May have scrolled vertically."""
        HScroll                   = 0x8
        r"""May have scrolled horizontally."""

    class VirtualSpace(enum.IntEnum):

        None_                     = 0x0
        r"""The default: no virtual space."""
        RectangularSelection      = 0x1
        r"""Virtual space is enabled for rectangular selections."""
        UserAccessible            = 0x2
        r"""Virtual space is enabled for user actions such as right arrow key or clicking beyond line end."""
        NoWrapLineStart           = 0x4
        r"""Left arrow does not wrap to the previous line."""


    @staticmethod
    def LevelIsHeader(level: _pyside6_scintilla.Scintilla.FoldLevel, /) -> bool: ...
    @staticmethod
    def LevelIsWhitespace(level: _pyside6_scintilla.Scintilla.FoldLevel, /) -> bool: ...
    @staticmethod
    def LevelNumber(level: _pyside6_scintilla.Scintilla.FoldLevel, /) -> int: ...
    @staticmethod
    def LevelNumberPart(level: _pyside6_scintilla.Scintilla.FoldLevel, /) -> _pyside6_scintilla.Scintilla.FoldLevel: ...
    @staticmethod
    def ModifierFlags(shift: bool, ctrl: bool, alt: bool, /, meta: bool = ..., super: bool = ...) -> _pyside6_scintilla.Scintilla.KeyMod: ...


class ScintillaDocument(PySide6.QtCore.QObject):

    error_occurred           : typing.ClassVar[Signal] = ... # error_occurred(int)
    modified                 : typing.ClassVar[Signal] = ... # modified(int,int,QByteArray,int,int,int,int,int)
    modify_attempt           : typing.ClassVar[Signal] = ... # modify_attempt()
    save_point               : typing.ClassVar[Signal] = ... # save_point(bool)
    style_needed             : typing.ClassVar[Signal] = ... # style_needed(int)

    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., pdoc_: int | None = ...) -> None:
        r"""Wrap a Scintilla document buffer, creating a new empty one unless `pdoc_` is given.

        `pdoc_` is a native document pointer, as returned by `pointer()` -- pass it to share an existing document, e.g. one obtained via `ScintillaEdit.get_doc()`."""

    def begin_undo_action(self, /, coalesceWithPrior: bool = ...) -> None:
        r"""Start a sequence of actions that is undone/redone as a single unit.

        If `coalesceWithPrior`, merge it with the previous undo action when possible."""
    def can_redo(self, /) -> bool:
        r"""Return whether there is an action to redo."""
    def can_undo(self, /) -> bool:
        r"""Return whether there is an action to undo."""
    def decoration_fill_range(self, position: int, value: int, fillLength: int, /) -> None:
        r"""Set `fillLength` bytes starting at `position` to `value` for the current indicator (see `set_current_indicator`)."""
    def decorations_end(self, indic: int, position: int, /) -> int:
        r"""Return the end of the run of indicator `indic` that includes `position`."""
    def decorations_start(self, indic: int, position: int, /) -> int:
        r"""Return the start of the run of indicator `indic` that includes `position`."""
    def decorations_value_at(self, indic: int, position: int, /) -> int:
        r"""Return the value of indicator `indic` at `position`."""
    def delete_chars(self, pos: int, len: int, /) -> bool:
        r"""Delete `len` characters starting at `pos`. Returns whether anything was deleted."""
    def delete_undo_history(self, /) -> None:
        r"""Discard the undo history."""
    def end_undo_action(self, /) -> None:
        r"""End a sequence of actions started by `begin_undo_action`."""
    def ensure_styled_to(self, position: int, /) -> None:
        r"""Ensure the document is styled up to at least `position`, emitting `style_needed` as needed."""
    def get_char_range(self, position: int, length: int, /) -> PySide6.QtCore.QByteArray:
        r"""Return `length` bytes of the document's text starting at `position`."""
    def get_character(self, pos: int, /) -> int:
        r"""Return the character at `pos`."""
    def get_code_page(self, /) -> int:
        r"""Return the code page used to interpret the document's bytes as characters."""
    def get_end_styled(self, /) -> int:
        r"""Return the position up to which the document has been styled."""
    def get_eol_mode(self, /) -> int:
        r"""Return the line ending type (`Scintilla.EndOfLine` value) used for new lines."""
    def insert_string(self, position: int, str: PySide6.QtCore.QByteArray | bytes | bytearray | memoryview | str, /) -> None:
        r"""Insert `str` at `position`."""
    def is_collecting_undo(self, /) -> bool:
        r"""Return whether undo actions are being collected."""
    def is_cr_lf(self, pos: int, /) -> bool:
        r"""Return whether the line ending at `pos` is CR+LF, as opposed to a lone CR or LF."""
    def is_read_only(self, /) -> bool:
        r"""Return whether the document refuses modification."""
    def is_save_point(self, /) -> bool:
        r"""Return whether the document is at its save point (unmodified since `set_save_point`)."""
    def length(self, /) -> int:
        r"""Return the number of bytes in the document."""
    def line_end(self, lineno: int, /) -> int:
        r"""Return the position of the end of line `lineno`, before any line ending characters."""
    def line_end_position(self, pos: int, /) -> int:
        r"""Return the position of the end of the line containing `pos`, before any line ending characters."""
    def line_from_position(self, pos: int, /) -> int:
        r"""Return the line containing position `pos`."""
    def line_start(self, lineno: int, /) -> int:
        r"""Return the position of the start of line `lineno`."""
    def lines_total(self, /) -> int:
        r"""Return the number of lines in the document."""
    def move_position_outside_char(self, pos: int, move_dir: int, check_line_end: bool, /) -> int:
        r"""Move `pos` outside of a multi-byte character towards `move_dir`.

        If `check_line_end`, also move it outside of a line ending."""
    def pointer(self, /) -> int:
        r"""Return the underlying native document pointer, for sharing with another `ScintillaDocument`."""
    def redo(self, /) -> int:
        r"""Redo one action from the undo history. Returns the position of the start of the change."""
    def set_code_page(self, code_page: int, /) -> None:
        r"""Set the code page used to interpret the document's bytes as characters."""
    def set_current_indicator(self, indic: int, /) -> None:
        r"""Set the indicator used by subsequent `decoration_fill_range` calls."""
    def set_eol_mode(self, eol_mode: int, /) -> None:
        r"""Set the line ending type (`Scintilla.EndOfLine` value) used for new lines."""
    def set_read_only(self, read_only: bool, /) -> None:
        r"""Set whether the document refuses modification."""
    def set_save_point(self, /) -> None:
        r"""Mark the document's current state as unmodified (the save point)."""
    def set_style_for(self, length: int, style: int, /) -> bool:
        r"""Set the next `length` bytes from the current styling position (see `start_styling`) to `style`.

        Returns whether successful."""
    def set_undo_collection(self, collect_undo: bool, /) -> bool:
        r"""Enable or disable collection of undo actions. Returns the previous setting."""
    def start_styling(self, position: int, /) -> None:
        r"""Set the styling position to `position`; subsequent `set_style_for` calls style from there."""
    def style_at(self, position: int, /) -> int:
        r"""Return the style byte at `position`."""
    def undo(self, /) -> int:
        r"""Undo one action from the undo history. Returns the position of the start of the change."""


class ScintillaEdit(_pyside6_scintilla.ScintillaEditBase):

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def TextReturner(self, message: int, wParam: int, /) -> PySide6.QtCore.QByteArray:
        r"""Send `message` with `wParam`, passing a buffer as its `lParam`, and return the buffer.

        Used internally for messages whose result is a string, e.g. `getText`/`getLine`."""
    def accessibility(self, /) -> int:
        r"""Report accessibility status."""
    def addRefDocument(self, doc: int, /) -> None:
        r"""Extend life of document."""
    def addSelection(self, caret: int, anchor: int, /) -> None:
        r"""Add a selection"""
    def addStyledText(self, length: int, c: bytes | bytearray | memoryview | str, /) -> None:
        r"""Add array of cells to document."""
    def addTabStop(self, line: int, x: int, /) -> None:
        r"""Add an explicit tab stop for a line."""
    def addText(self, length: int, text: bytes | bytearray | memoryview | str, /) -> None:
        r"""Add text to the document at current position."""
    def addUndoAction(self, token: int, flags: int, /) -> None:
        r"""Add a container action to the undo stack"""
    def additionalCaretFore(self, /) -> int:
        r"""Get the foreground colour of additional carets."""
    def additionalCaretsBlink(self, /) -> bool:
        r"""Whether additional carets will blink"""
    def additionalCaretsVisible(self, /) -> bool:
        r"""Whether additional carets are visible"""
    def additionalSelAlpha(self, /) -> int:
        r"""Get the alpha of the selection."""
    def additionalSelectionTyping(self, /) -> bool:
        r"""Whether typing can be performed into multiple selections"""
    def allLinesVisible(self, /) -> bool:
        r"""Are all lines visible?"""
    def allocate(self, bytes: int, /) -> None:
        r"""Enlarge the document to a particular size of text bytes."""
    def allocateExtendedStyles(self, numberStyles: int, /) -> int:
        r"""Allocate some extended (>255) style numbers and return the start of the range"""
    def allocateLineCharacterIndex(self, lineCharacterIndex: int, /) -> None:
        r"""Request line character index be created or its use count increased."""
    def allocateLines(self, lines: int, /) -> None:
        r"""Enlarge the number of lines allocated."""
    def allocateSubStyles(self, styleBase: int, numberStyles: int, /) -> int:
        r"""Allocate a set of sub styles for a particular base style, returning start of range"""
    def anchor(self, /) -> int:
        r"""Returns the position of the opposite end of the selection to the caret."""
    def annotationClearAll(self, /) -> None:
        r"""Clear the annotations from all lines"""
    def annotationLines(self, line: int, /) -> int:
        r"""Get the number of annotation lines for a line"""
    def annotationSetStyle(self, line: int, style: int, /) -> None:
        r"""Set the style number for the annotations for a line"""
    def annotationSetStyleOffset(self, style: int, /) -> None:
        r"""Get the start of the range of style numbers used for annotations"""
    def annotationSetStyles(self, line: int, styles: bytes | bytearray | memoryview | str, /) -> None:
        r"""Set the annotation styles for a line"""
    def annotationSetText(self, line: int, text: bytes | bytearray | memoryview | str, /) -> None:
        r"""Set the annotation text for a line"""
    def annotationSetVisible(self, visible: int, /) -> None:
        r"""Set the visibility for the annotations for a view"""
    def annotationStyle(self, line: int, /) -> int:
        r"""Get the style number for the annotations for a line"""
    def annotationStyleOffset(self, /) -> int:
        r"""Get the start of the range of style numbers used for annotations"""
    def annotationStyles(self, line: int, /) -> PySide6.QtCore.QByteArray:
        r"""Get the annotation styles for a line"""
    def annotationText(self, line: int, /) -> PySide6.QtCore.QByteArray:
        r"""Get the annotation text for a line"""
    def annotationVisible(self, /) -> int:
        r"""Get the visibility for the annotations for a view"""
    def appendText(self, length: int, text: bytes | bytearray | memoryview | str, /) -> None:
        r"""Append a string to the end of the document without changing the selection."""
    def assignCmdKey(self, keyDefinition: int, sciCommand: int, /) -> None:
        r"""When key+modifier combination keyDefinition is pressed perform sciCommand."""
    def autoCActive(self, /) -> bool:
        r"""Is there an auto-completion list visible?"""
    def autoCAutoHide(self, /) -> bool:
        r"""Retrieve whether or not autocompletion is hidden automatically when nothing matches."""
    def autoCCancel(self, /) -> None:
        r"""Remove the auto-completion list from the screen."""
    def autoCCancelAtStart(self, /) -> bool:
        r"""Retrieve whether auto-completion cancelled by backspacing before start."""
    def autoCCaseInsensitiveBehaviour(self, /) -> int:
        r"""Get auto-completion case insensitive behaviour."""
    def autoCChooseSingle(self, /) -> bool:
        r"""Retrieve whether a single item auto-completion list automatically choose the item."""
    def autoCComplete(self, /) -> None:
        r"""User has selected an item so remove the list and insert the selection."""
    def autoCCurrent(self, /) -> int:
        r"""Get currently selected item position in the auto-completion list"""
    def autoCCurrentText(self, /) -> PySide6.QtCore.QByteArray:
        r"""Get currently selected item text in the auto-completion list Returns the length of the item text Result is NUL-terminated."""
    def autoCDropRestOfWord(self, /) -> bool:
        r"""Retrieve whether or not autocompletion deletes any word characters after the inserted text upon completion."""
    def autoCIgnoreCase(self, /) -> bool:
        r"""Retrieve state of ignore case flag."""
    def autoCMaxHeight(self, /) -> int:
        r"""Set the maximum height, in rows, of auto-completion and user lists."""
    def autoCMaxWidth(self, /) -> int:
        r"""Get the maximum width, in characters, of auto-completion and user lists."""
    def autoCMulti(self, /) -> int:
        r"""Retrieve the effect of autocompleting when there are multiple selections."""
    def autoCOptions(self, /) -> int:
        r"""Retrieve autocompletion options."""
    def autoCOrder(self, /) -> int:
        r"""Get the way autocompletion lists are ordered."""
    def autoCPosStart(self, /) -> int:
        r"""Retrieve the position of the caret when the auto-completion list was displayed."""
    def autoCSelect(self, select: bytes | bytearray | memoryview | str, /) -> None:
        r"""Select the item in the auto-completion list that starts with a string."""
    def autoCSeparator(self, /) -> int:
        r"""Retrieve the auto-completion list separator character."""
    def autoCSetAutoHide(self, autoHide: bool, /) -> None:
        r"""Set whether or not autocompletion is hidden automatically when nothing matches."""
    def autoCSetCancelAtStart(self, cancel: bool, /) -> None:
        r"""Should the auto-completion list be cancelled if the user backspaces to a position before where the box was created."""
    def autoCSetCaseInsensitiveBehaviour(self, behaviour: int, /) -> None:
        r"""Set auto-completion case insensitive behaviour to either prefer case-sensitive matches or have no preference."""
    def autoCSetChooseSingle(self, chooseSingle: bool, /) -> None:
        r"""Should a single item auto-completion list automatically choose the item."""
    def autoCSetDropRestOfWord(self, dropRestOfWord: bool, /) -> None:
        r"""Set whether or not autocompletion deletes any word characters after the inserted text upon completion."""
    def autoCSetFillUps(self, characterSet: bytes | bytearray | memoryview | str, /) -> None:
        r"""Define a set of characters that when typed will cause the autocompletion to choose the selected item."""
    def autoCSetIgnoreCase(self, ignoreCase: bool, /) -> None:
        r"""Set whether case is significant when performing auto-completion searches."""
    def autoCSetMaxHeight(self, rowCount: int, /) -> None:
        r"""Set the maximum height, in rows, of auto-completion and user lists. The default is 5 rows."""
    def autoCSetMaxWidth(self, characterCount: int, /) -> None:
        r"""Set the maximum width, in characters, of auto-completion and user lists. Set to 0 to autosize to fit longest item, which is the default."""
    def autoCSetMulti(self, multi: int, /) -> None:
        r"""Change the effect of autocompleting when there are multiple selections."""
    def autoCSetOptions(self, options: int, /) -> None:
        r"""Set autocompletion options."""
    def autoCSetOrder(self, order: int, /) -> None:
        r"""Set the way autocompletion lists are ordered."""
    def autoCSetSeparator(self, separatorCharacter: int, /) -> None:
        r"""Change the separator character in the string setting up an auto-completion list. Default is space but can be changed if items contain space."""
    def autoCSetTypeSeparator(self, separatorCharacter: int, /) -> None:
        r"""Change the type-separator character in the string setting up an auto-completion list. Default is '?' but can be changed if items contain '?'."""
    def autoCShow(self, lengthEntered: int, itemList: bytes | bytearray | memoryview | str, /) -> None:
        r"""Display a auto-completion list. The lengthEntered parameter indicates how many characters before the caret should be used to provide context."""
    def autoCStops(self, characterSet: bytes | bytearray | memoryview | str, /) -> None:
        r"""Define a set of character that when typed cancel the auto-completion list."""
    def autoCTypeSeparator(self, /) -> int:
        r"""Retrieve the auto-completion list type-separator character."""
    def automaticFold(self, /) -> int:
        r"""Get automatic folding behaviours."""
    def backSpaceUnIndents(self, /) -> bool:
        r"""Does a backspace pressed when caret is within indentation unindent?"""
    def backTab(self, /) -> None:
        r"""If selection is empty or all on one line dedent the line if caret is at start, else move caret. If more than one line selected, dedent the lines."""
    def beginUndoAction(self, /) -> None:
        r"""Start a sequence of actions that is undone and redone as a unit. May be nested."""
    def bidirectional(self, /) -> int:
        r"""Retrieve bidirectional text display state."""
    def braceBadLight(self, pos: int, /) -> None:
        r"""Highlight the character at a position indicating there is no matching brace."""
    def braceBadLightIndicator(self, useSetting: bool, indicator: int, /) -> None:
        r"""Use specified indicator to highlight non matching brace instead of changing its style."""
    def braceHighlight(self, posA: int, posB: int, /) -> None:
        r"""Highlight the characters at two positions."""
    def braceHighlightIndicator(self, useSetting: bool, indicator: int, /) -> None:
        r"""Use specified indicator to highlight matching braces instead of changing their style."""
    def braceMatch(self, pos: int, maxReStyle: int, /) -> int:
        r"""Find the position of a matching brace or INVALID_POSITION if no match. The maxReStyle must be 0 for now. It may be defined in a future release."""
    def braceMatchNext(self, pos: int, startPos: int, /) -> int:
        r"""Similar to BraceMatch, but matching starts at the explicit start position."""
    def bufferedDraw(self, /) -> bool:
        r"""Is drawing done first into a buffer or direct to the screen?"""
    def callTipActive(self, /) -> bool:
        r"""Is there an active call tip?"""
    def callTipCancel(self, /) -> None:
        r"""Remove the call tip from the screen."""
    def callTipPosStart(self, /) -> int:
        r"""Retrieve the position where the caret was before displaying the call tip."""
    def callTipSetBack(self, back: int, /) -> None:
        r"""Set the background colour for the call tip."""
    def callTipSetFore(self, fore: int, /) -> None:
        r"""Set the foreground colour for the call tip."""
    def callTipSetForeHlt(self, fore: int, /) -> None:
        r"""Set the foreground colour for the highlighted part of the call tip."""
    def callTipSetHlt(self, highlightStart: int, highlightEnd: int, /) -> None:
        r"""Highlight a segment of the definition."""
    def callTipSetPosStart(self, posStart: int, /) -> None:
        r"""Set the start position in order to change when backspacing removes the calltip."""
    def callTipSetPosition(self, above: bool, /) -> None:
        r"""Set position of calltip, above or below text."""
    def callTipShow(self, pos: int, definition: bytes | bytearray | memoryview | str, /) -> None:
        r"""Show a call tip containing a definition near position pos."""
    def callTipUseStyle(self, tabSize: int, /) -> None:
        r"""Enable use of STYLE_CALLTIP and set call tip tab size in pixels."""
    def canPaste(self, /) -> bool:
        r"""Will a paste succeed?"""
    def canRedo(self, /) -> bool:
        r"""Are there any redoable actions in the undo history?"""
    def canUndo(self, /) -> bool:
        r"""Are there any undoable actions in the undo history?"""
    def cancel(self, /) -> None:
        r"""Cancel any modes such as call tip or auto-completion list display."""
    def caretFore(self, /) -> int:
        r"""Get the foreground colour of the caret."""
    def caretLineBack(self, /) -> int:
        r"""Get the colour of the background of the line containing the caret."""
    def caretLineBackAlpha(self, /) -> int:
        r"""Get the background alpha of the caret line."""
    def caretLineFrame(self, /) -> int:
        r"""Retrieve the caret line frame width. Width = 0 means this option is disabled."""
    def caretLineHighlightSubLine(self, /) -> bool:
        r"""Get only highlighting subline instead of whole line."""
    def caretLineLayer(self, /) -> int:
        r"""Get the layer of the background of the line containing the caret."""
    def caretLineVisible(self, /) -> bool:
        r"""Is the background of the line containing the caret in a different colour?"""
    def caretLineVisibleAlways(self, /) -> bool:
        r"""Is the caret line always visible?"""
    def caretPeriod(self, /) -> int:
        r"""Get the time in milliseconds that the caret is on and off."""
    def caretSticky(self, /) -> int:
        r"""Can the caret preferred x position only be changed by explicit movement commands?"""
    def caretStyle(self, /) -> int:
        r"""Returns the current style of the caret."""
    def caretWidth(self, /) -> int:
        r"""Returns the width of the insert mode caret."""
    def changeHistory(self, /) -> int:
        r"""Report change history status."""
    def changeInsertion(self, length: int, text: bytes | bytearray | memoryview | str, /) -> None:
        r"""Change the text that is being inserted in response to SC_MOD_INSERTCHECK"""
    def changeLexerState(self, start: int, end: int, /) -> int:
        r"""Indicate that the internal state of a lexer has changed over a range and therefore there may be a need to redraw."""
    def charAt(self, pos: int, /) -> int:
        r"""Returns the character byte at the position."""
    def charLeft(self, /) -> None:
        r"""Move caret left one character."""
    def charLeftExtend(self, /) -> None:
        r"""Move caret left one character extending selection to new caret position."""
    def charLeftRectExtend(self, /) -> None:
        r"""Move caret left one character, extending rectangular selection to new caret position."""
    def charPositionFromPoint(self, x: int, y: int, /) -> int:
        r"""Find the position of a character from a point within the window."""
    def charPositionFromPointClose(self, x: int, y: int, /) -> int:
        r"""Find the position of a character from a point within the window. Return INVALID_POSITION if not close to text."""
    def charRight(self, /) -> None:
        r"""Move caret right one character."""
    def charRightExtend(self, /) -> None:
        r"""Move caret right one character extending selection to new caret position."""
    def charRightRectExtend(self, /) -> None:
        r"""Move caret right one character, extending rectangular selection to new caret position."""
    def characterCategoryOptimization(self, /) -> int:
        r"""Get the number of characters to have directly indexed categories"""
    def characterPointer(self, /) -> int:
        r"""Compact the document buffer and return a read-only pointer to the characters in the document."""
    def chooseCaretX(self, /) -> None:
        r"""Set the last x chosen value to be the caret x position."""
    def clear(self, /) -> None:
        r"""Clear the selection."""
    def clearAll(self, /) -> None:
        r"""Delete all text in the document."""
    def clearAllCmdKeys(self, /) -> None:
        r"""Drop all key mappings."""
    def clearAllRepresentations(self, /) -> None:
        r"""Clear representations to default."""
    def clearCmdKey(self, keyDefinition: int, /) -> None:
        r"""When key+modifier combination keyDefinition is pressed do nothing."""
    def clearDocumentStyle(self, /) -> None:
        r"""Set all style bytes to 0, remove all folding information."""
    def clearRegisteredImages(self, /) -> None:
        r"""Clear all the registered XPM images."""
    def clearRepresentation(self, encodedCharacter: bytes | bytearray | memoryview | str, /) -> None:
        r"""Remove a character representation."""
    def clearSelections(self, /) -> None:
        r"""Clear selections to a single empty stream selection"""
    def clearTabStops(self, line: int, /) -> None:
        r"""Clear explicit tabstops on a line."""
    def codePage(self, /) -> int:
        r"""Get the code page used to interpret the bytes of the document as characters."""
    def colourise(self, start: int, end: int, /) -> None:
        r"""Colourise a segment of the document using the current lexing language."""
    def column(self, pos: int, /) -> int:
        r"""Retrieve the column number of a position, taking tab width into account."""
    def commandEvents(self, /) -> bool:
        r"""Get whether command events are sent to the container."""
    def contractedFoldNext(self, lineStart: int, /) -> int:
        r"""Find the next line at or after lineStart that is a contracted fold header line. Return -1 when no more lines."""
    def controlCharSymbol(self, /) -> int:
        r"""Get the way control characters are displayed."""
    def convertEOLs(self, eolMode: int, /) -> None:
        r"""Convert all line endings in the document to one mode."""
    def copy(self, /) -> None:
        r"""Copy the selection to the clipboard."""
    def copyAllowLine(self, /) -> None:
        r"""Copy the selection, if selection empty copy the line with the caret"""
    def copyRange(self, start: int, end: int, /) -> None:
        r"""Copy a range of text to the clipboard. Positions are clipped into the document."""
    def copyText(self, length: int, text: bytes | bytearray | memoryview | str, /) -> None:
        r"""Copy argument text to the clipboard."""
    def countCharacters(self, start: int, end: int, /) -> int:
        r"""Count characters between two positions."""
    def countCodeUnits(self, start: int, end: int, /) -> int:
        r"""Count code units between two positions."""
    def createDocument(self, bytes: int, documentOptions: int, /) -> int:
        r"""Create a new document object. Starts with reference count of 1 and not selected into editor."""
    def createLoader(self, bytes: int, documentOptions: int, /) -> int:
        r"""Create an ILoader*."""
    def currentPos(self, /) -> int:
        r"""Returns the position of the caret."""
    def cursor(self, /) -> int:
        r"""Get cursor type."""
    def cut(self, /) -> None:
        r"""Cut the selection to the clipboard."""
    def delLineLeft(self, /) -> None:
        r"""Delete back from the current position to the start of the line."""
    def delLineRight(self, /) -> None:
        r"""Delete forwards from the current position to the end of the line."""
    def delWordLeft(self, /) -> None:
        r"""Delete the word to the left of the caret."""
    def delWordRight(self, /) -> None:
        r"""Delete the word to the right of the caret."""
    def delWordRightEnd(self, /) -> None:
        r"""Delete the word to the right of the caret, but not the trailing non-word characters."""
    def deleteBack(self, /) -> None:
        r"""Delete the selection or if no selection, the character before the caret."""
    def deleteBackNotLine(self, /) -> None:
        r"""Delete the selection or if no selection, the character before the caret. Will not delete the character before at the start of a line."""
    def deleteRange(self, start: int, lengthDelete: int, /) -> None:
        r"""Delete a range of text in the document."""
    def describeKeyWordSets(self, /) -> PySide6.QtCore.QByteArray:
        r"""Retrieve a '\n' separated list of descriptions of the keyword sets understood by the current lexer. Result is NUL-terminated."""
    def describeProperty(self, name: bytes | bytearray | memoryview | str, /) -> PySide6.QtCore.QByteArray:
        r"""Describe a property. Result is NUL-terminated."""
    def descriptionOfStyle(self, style: int, /) -> PySide6.QtCore.QByteArray:
        r"""Retrieve a description of a style. Result is NUL-terminated."""
    def directFunction(self, /) -> int:
        r"""Retrieve a pointer to a function that processes messages for this Scintilla."""
    def directPointer(self, /) -> int:
        r"""Retrieve a pointer value to use as the first argument when calling the function returned by GetDirectFunction."""
    def directStatusFunction(self, /) -> int:
        r"""Retrieve a pointer to a function that processes messages for this Scintilla and returns status."""
    def distanceToSecondaryStyles(self, /) -> int:
        r"""Where styles are duplicated by a feature such as active/inactive code return the distance between the two types."""
    def docLineFromVisible(self, displayLine: int, /) -> int:
        r"""Find the document line of a display line taking hidden lines into account."""
    def docPointer(self, /) -> int:
        r"""Retrieve a pointer to the document object."""
    def documentEnd(self, /) -> None:
        r"""Move caret to last position in document."""
    def documentEndExtend(self, /) -> None:
        r"""Move caret to last position in document extending selection to new caret position."""
    def documentOptions(self, /) -> int:
        r"""Get which document options are set."""
    def documentStart(self, /) -> None:
        r"""Move caret to first position in document."""
    def documentStartExtend(self, /) -> None:
        r"""Move caret to first position in document extending selection to new caret position."""
    def dropSelectionN(self, selection: int, /) -> None:
        r"""Drop one selection"""
    def eOLAnnotationClearAll(self, /) -> None:
        r"""Clear the end of annotations from all lines"""
    def eOLAnnotationSetStyle(self, line: int, style: int, /) -> None:
        r"""Set the style number for the end of line annotations for a line"""
    def eOLAnnotationSetStyleOffset(self, style: int, /) -> None:
        r"""Get the start of the range of style numbers used for end of line annotations"""
    def eOLAnnotationSetText(self, line: int, text: bytes | bytearray | memoryview | str, /) -> None:
        r"""Set the end of line annotation text for a line"""
    def eOLAnnotationSetVisible(self, visible: int, /) -> None:
        r"""Set the visibility for the end of line annotations for a view"""
    def eOLAnnotationStyle(self, line: int, /) -> int:
        r"""Get the style number for the end of line annotations for a line"""
    def eOLAnnotationStyleOffset(self, /) -> int:
        r"""Get the start of the range of style numbers used for end of line annotations"""
    def eOLAnnotationText(self, line: int, /) -> PySide6.QtCore.QByteArray:
        r"""Get the end of line annotation text for a line"""
    def eOLAnnotationVisible(self, /) -> int:
        r"""Get the visibility for the end of line annotations for a view"""
    def eOLMode(self, /) -> int:
        r"""Retrieve the current end of line mode - one of CRLF, CR, or LF."""
    def edgeColour(self, /) -> int:
        r"""Retrieve the colour used in edge indication."""
    def edgeColumn(self, /) -> int:
        r"""Retrieve the column number which text should be kept within."""
    def edgeMode(self, /) -> int:
        r"""Retrieve the edge highlight mode."""
    def editToggleOvertype(self, /) -> None:
        r"""Switch from insert to overtype mode or the reverse."""
    def elementAllowsTranslucent(self, element: int, /) -> bool:
        r"""Get whether an element supports translucency."""
    def elementBaseColour(self, element: int, /) -> int:
        r"""Get the colour of an element."""
    def elementColour(self, element: int, /) -> int:
        r"""Get the colour of an element."""
    def elementIsSet(self, element: int, /) -> bool:
        r"""Get whether an element has been set by SetElementColour. When false, a platform-defined or default colour is used."""
    def emptyUndoBuffer(self, /) -> None:
        r"""Delete the undo history."""
    def encodedFromUTF8(self, utf8: bytes | bytearray | memoryview | str, /) -> PySide6.QtCore.QByteArray:
        r"""Translates a UTF8 string into the document encoding. Return the length of the result in bytes. On error return 0."""
    def endAtLastLine(self, /) -> bool:
        r"""Retrieve whether the maximum scroll position has the last line at the bottom of the view."""
    def endStyled(self, /) -> int:
        r"""Retrieve the position of the last correctly styled character."""
    def endUndoAction(self, /) -> None:
        r"""End a sequence of actions that is undone and redone as a unit."""
    def ensureVisible(self, line: int, /) -> None:
        r"""Ensure a particular line is visible by expanding any header line hiding it."""
    def ensureVisibleEnforcePolicy(self, line: int, /) -> None:
        r"""Ensure a particular line is visible by expanding any header line hiding it. Use the currently set visibility policy to determine which range to display."""
    def expandChildren(self, line: int, level: int, /) -> None:
        r"""Expand a fold header and all children. Use the level argument instead of the line's current level."""
    def extraAscent(self, /) -> int:
        r"""Get extra ascent for each line"""
    def extraDescent(self, /) -> int:
        r"""Get extra descent for each line"""
    def findColumn(self, line: int, column: int, /) -> int:
        r"""Find the position of a column on a line taking into account tabs and multi-byte characters. If beyond end of line, return line end position."""
    def findIndicatorFlash(self, start: int, end: int, /) -> None:
        r"""On macOS, flash a find indicator, then fade out."""
    def findIndicatorHide(self, /) -> None:
        r"""On macOS, hide the find indicator."""
    def findIndicatorShow(self, start: int, end: int, /) -> None:
        r"""On macOS, show a find indicator."""
    def findText(self, flags: int, text: bytes | bytearray | memoryview | str, cpMin: int, cpMax: int, /) -> typing.Tuple[int, int]:
        r"""Alias for `find_text`."""
    def find_text(self, flags: int, text: bytes | bytearray | memoryview | str, cpMin: int, cpMax: int, /) -> typing.Tuple[int, int]:
        r"""Search for `text` between `cpMin` and `cpMax` using `flags` (`Scintilla.FindOption` values).

        Returns the `(start, end)` position of the match, or `(-1, cpMax)` if not found."""
    def firstVisibleLine(self, /) -> int:
        r"""Retrieve the display line at the top of the display."""
    def focus(self, /) -> bool:
        r"""Get internal focus flag."""
    def foldAll(self, action: int, /) -> None:
        r"""Expand or contract all fold headers."""
    def foldChildren(self, line: int, action: int, /) -> None:
        r"""Expand or contract a fold header and its children."""
    def foldDisplayTextSetStyle(self, style: int, /) -> None:
        r"""Set the style of fold display text."""
    def foldDisplayTextStyle(self, /) -> int:
        r"""Get the style of fold display text."""
    def foldExpanded(self, line: int, /) -> bool:
        r"""Is a header line expanded?"""
    def foldLevel(self, line: int, /) -> int:
        r"""Retrieve the fold level of a line."""
    def foldLine(self, line: int, action: int, /) -> None:
        r"""Expand or contract a fold header."""
    def foldParent(self, line: int, /) -> int:
        r"""Find the parent line of a child line."""
    def fontLocale(self, /) -> PySide6.QtCore.QByteArray:
        r"""Get the locale for displaying text."""
    def fontQuality(self, /) -> int:
        r"""Retrieve the quality level for text."""
    def formFeed(self, /) -> None:
        r"""Insert a Form Feed character."""
    def formatRange(self, draw: bool, target: PySide6.QtGui.QPaintDevice, measure: PySide6.QtGui.QPaintDevice, print_rect: PySide6.QtCore.QRect, page_rect: PySide6.QtCore.QRect, range_start: int, range_end: int, /) -> int:
        r"""Alias for `format_range`."""
    def format_range(self, draw: bool, target: PySide6.QtGui.QPaintDevice, measure: PySide6.QtGui.QPaintDevice, print_rect: PySide6.QtCore.QRect, page_rect: PySide6.QtCore.QRect, range_start: int, range_end: int, /) -> int:
        r"""Render the document between `range_start` and `range_end` for printing.

        Draws onto `target` (and lays out using `measure`) within `print_rect`/`page_rect`. If `draw` is false, only measures. Returns the position after the last formatted character."""
    def freeSubStyles(self, /) -> None:
        r"""Free allocated sub styles"""
    def gapPosition(self, /) -> int:
        r"""Return a position which, to avoid performance costs, should not be within the range of a call to GetRangePointer."""
    def getCurLine(self, length: int, /) -> PySide6.QtCore.QByteArray:
        r"""Retrieve the text of the line containing the caret. Returns the index of the caret on the line. Result is NUL-terminated."""
    def getDefaultFoldDisplayText(self, /) -> PySide6.QtCore.QByteArray:
        r"""Get the default fold display text."""
    def getLine(self, line: int, /) -> PySide6.QtCore.QByteArray:
        r"""Retrieve the contents of a line. Returns the length of the line."""
    def getLineSelEndPosition(self, line: int, /) -> int:
        r"""Retrieve the position of the end of the selection at the given line (INVALID_POSITION if no selection on this line)."""
    def getLineSelStartPosition(self, line: int, /) -> int:
        r"""Retrieve the position of the start of the selection at the given line (INVALID_POSITION if no selection on this line)."""
    def getNextTabStop(self, line: int, x: int, /) -> int:
        r"""Find the next explicit tab stop position on a line after a position."""
    def getSelText(self, /) -> PySide6.QtCore.QByteArray:
        r"""Retrieve the selected text. Return the length of the text. Result is NUL-terminated."""
    def getText(self, length: int, /) -> PySide6.QtCore.QByteArray:
        r"""Retrieve all the text in the document. Returns number of characters retrieved. Result is NUL-terminated."""
    def get_doc(self, /) -> _pyside6_scintilla.ScintillaDocument:
        r"""Return a new `ScintillaDocument` wrapping this editor's current document.

        Pass it to another `ScintillaEdit`'s `set_doc` to share the document between views.

        The returned object has no Qt parent, so it's kept alive only by your Python reference to it -- if you let it go, its `modified`/`save_point`/etc. signals stop firing (the underlying document itself stays alive as long as an editor is using it)."""
    def get_text_range(self, start: int, end: int, /) -> PySide6.QtCore.QByteArray:
        r"""Return the document's text between `start` and `end`."""
    def gotoLine(self, line: int, /) -> None:
        r"""Set caret to start of a line and ensure it is visible."""
    def gotoPos(self, caret: int, /) -> None:
        r"""Set caret to a position and ensure it is visible."""
    def grabFocus(self, /) -> None:
        r"""Set the focus to this Scintilla widget."""
    def hScrollBar(self, /) -> bool:
        r"""Is the horizontal scroll bar visible?"""
    def hideLines(self, lineStart: int, lineEnd: int, /) -> None:
        r"""Make a range of lines invisible."""
    def hideSelection(self, hide: bool, /) -> None:
        r"""Draw the selection either highlighted or in normal (non-highlighted) style."""
    def highlightGuide(self, /) -> int:
        r"""Get the highlighted indentation guide column."""
    def home(self, /) -> None:
        r"""Move caret to first position on line."""
    def homeDisplay(self, /) -> None:
        r"""Move caret to first position on display line."""
    def homeDisplayExtend(self, /) -> None:
        r"""Move caret to first position on display line extending selection to new caret position."""
    def homeExtend(self, /) -> None:
        r"""Move caret to first position on line extending selection to new caret position."""
    def homeRectExtend(self, /) -> None:
        r"""Move caret to first position on line, extending rectangular selection to new caret position."""
    def homeWrap(self, /) -> None:
        r"""Like Home but when word-wrap is enabled goes first to start of display line HomeDisplay, then to start of document line Home."""
    def homeWrapExtend(self, /) -> None:
        r"""Like HomeExtend but when word-wrap is enabled extends first to start of display line HomeDisplayExtend, then to start of document line HomeExtend."""
    def hotspotActiveBack(self, /) -> int:
        r"""Get the back colour for active hotspots."""
    def hotspotActiveFore(self, /) -> int:
        r"""Get the fore colour for active hotspots."""
    def hotspotActiveUnderline(self, /) -> bool:
        r"""Get whether underlining for active hotspots."""
    def hotspotSingleLine(self, /) -> bool:
        r"""Get the HotspotSingleLine property"""
    def iMEInteraction(self, /) -> int:
        r"""Is the IME displayed in a window or inline?"""
    def identifier(self, /) -> int:
        r"""Get the identifier."""
    def idleStyling(self, /) -> int:
        r"""Retrieve the limits to idle styling."""
    def indent(self, /) -> int:
        r"""Retrieve indentation size."""
    def indentationGuides(self, /) -> int:
        r"""Are the indentation guides visible?"""
    def indexPositionFromLine(self, line: int, lineCharacterIndex: int, /) -> int:
        r"""Retrieve the position measured in index units at the start of a document line."""
    def indicAlpha(self, indicator: int, /) -> int:
        r"""Get the alpha fill colour of the given indicator."""
    def indicFlags(self, indicator: int, /) -> int:
        r"""Retrieve the attributes of an indicator."""
    def indicFore(self, indicator: int, /) -> int:
        r"""Retrieve the foreground colour of an indicator."""
    def indicHoverFore(self, indicator: int, /) -> int:
        r"""Retrieve the foreground hover colour of an indicator."""
    def indicHoverStyle(self, indicator: int, /) -> int:
        r"""Retrieve the hover style of an indicator."""
    def indicOutlineAlpha(self, indicator: int, /) -> int:
        r"""Get the alpha outline colour of the given indicator."""
    def indicSetAlpha(self, indicator: int, alpha: int, /) -> None:
        r"""Set the alpha fill colour of the given indicator."""
    def indicSetFlags(self, indicator: int, flags: int, /) -> None:
        r"""Set the attributes of an indicator."""
    def indicSetFore(self, indicator: int, fore: int, /) -> None:
        r"""Set the foreground colour of an indicator."""
    def indicSetHoverFore(self, indicator: int, fore: int, /) -> None:
        r"""Set the foreground hover colour of an indicator."""
    def indicSetHoverStyle(self, indicator: int, indicatorStyle: int, /) -> None:
        r"""Set a hover indicator to plain, squiggle or TT."""
    def indicSetOutlineAlpha(self, indicator: int, alpha: int, /) -> None:
        r"""Set the alpha outline colour of the given indicator."""
    def indicSetStrokeWidth(self, indicator: int, hundredths: int, /) -> None:
        r"""Set the stroke width of an indicator in hundredths of a pixel."""
    def indicSetStyle(self, indicator: int, indicatorStyle: int, /) -> None:
        r"""Set an indicator to plain, squiggle or TT."""
    def indicSetUnder(self, indicator: int, under: bool, /) -> None:
        r"""Set an indicator to draw under text or over(default)."""
    def indicStrokeWidth(self, indicator: int, /) -> int:
        r"""Retrieve the stroke width of an indicator."""
    def indicStyle(self, indicator: int, /) -> int:
        r"""Retrieve the style of an indicator."""
    def indicUnder(self, indicator: int, /) -> bool:
        r"""Retrieve whether indicator drawn under or over text."""
    def indicatorAllOnFor(self, pos: int, /) -> int:
        r"""Are any indicators present at pos?"""
    def indicatorClearRange(self, start: int, lengthClear: int, /) -> None:
        r"""Turn a indicator off over a range."""
    def indicatorCurrent(self, /) -> int:
        r"""Get the current indicator"""
    def indicatorEnd(self, indicator: int, pos: int, /) -> int:
        r"""Where does a particular indicator end?"""
    def indicatorFillRange(self, start: int, lengthFill: int, /) -> None:
        r"""Turn a indicator on over a range."""
    def indicatorStart(self, indicator: int, pos: int, /) -> int:
        r"""Where does a particular indicator start?"""
    def indicatorValue(self, /) -> int:
        r"""Get the current indicator value"""
    def indicatorValueAt(self, indicator: int, pos: int, /) -> int:
        r"""What value does a particular indicator have at a position?"""
    def insertText(self, pos: int, text: bytes | bytearray | memoryview | str, /) -> None:
        r"""Insert string at a position."""
    def isRangeWord(self, start: int, end: int, /) -> bool:
        r"""Is the range start..end considered a word?"""
    def lastChild(self, line: int, level: int, /) -> int:
        r"""Find the last child line of a header line."""
    def layoutCache(self, /) -> int:
        r"""Retrieve the degree of caching of layout information."""
    def layoutThreads(self, /) -> int:
        r"""Get maximum number of threads used for layout"""
    def length(self, /) -> int:
        r"""Returns the number of bytes in the document."""
    def lexer(self, /) -> int:
        r"""Retrieve the lexing language of the document."""
    def lexerLanguage(self, /) -> PySide6.QtCore.QByteArray:
        r"""Retrieve the name of the lexer. Return the length of the text. Result is NUL-terminated."""
    def lineCharacterIndex(self, /) -> int:
        r"""Retrieve line character index state."""
    def lineCopy(self, /) -> None:
        r"""Copy the line containing the caret."""
    def lineCount(self, /) -> int:
        r"""Returns the number of lines in the document. There is always at least one."""
    def lineCut(self, /) -> None:
        r"""Cut the line containing the caret."""
    def lineDelete(self, /) -> None:
        r"""Delete the line containing the caret."""
    def lineDown(self, /) -> None:
        r"""Move caret down one line."""
    def lineDownExtend(self, /) -> None:
        r"""Move caret down one line extending selection to new caret position."""
    def lineDownRectExtend(self, /) -> None:
        r"""Move caret down one line, extending rectangular selection to new caret position."""
    def lineDuplicate(self, /) -> None:
        r"""Duplicate the current line."""
    def lineEnd(self, /) -> None:
        r"""Move caret to last position on line."""
    def lineEndDisplay(self, /) -> None:
        r"""Move caret to last position on display line."""
    def lineEndDisplayExtend(self, /) -> None:
        r"""Move caret to last position on display line extending selection to new caret position."""
    def lineEndExtend(self, /) -> None:
        r"""Move caret to last position on line extending selection to new caret position."""
    def lineEndPosition(self, line: int, /) -> int:
        r"""Get the position after the last visible characters on a line."""
    def lineEndRectExtend(self, /) -> None:
        r"""Move caret to last position on line, extending rectangular selection to new caret position."""
    def lineEndTypesActive(self, /) -> int:
        r"""Get the line end types currently recognised. May be a subset of the allowed types due to lexer limitation."""
    def lineEndTypesAllowed(self, /) -> int:
        r"""Get the line end types currently allowed."""
    def lineEndTypesSupported(self, /) -> int:
        r"""Bit set of LineEndType enumertion for which line ends beyond the standard LF, CR, and CRLF are supported by the lexer."""
    def lineEndWrap(self, /) -> None:
        r"""Like LineEnd but when word-wrap is enabled goes first to end of display line LineEndDisplay, then to start of document line LineEnd."""
    def lineEndWrapExtend(self, /) -> None:
        r"""Like LineEndExtend but when word-wrap is enabled extends first to end of display line LineEndDisplayExtend, then to start of document line LineEndExtend."""
    def lineFromIndexPosition(self, pos: int, lineCharacterIndex: int, /) -> int:
        r"""Retrieve the document line containing a position measured in index units."""
    def lineFromPosition(self, pos: int, /) -> int:
        r"""Retrieve the line containing a position."""
    def lineIndentPosition(self, line: int, /) -> int:
        r"""Retrieve the position before the first non indentation character on a line."""
    def lineIndentation(self, line: int, /) -> int:
        r"""Retrieve the number of columns that a line is indented."""
    def lineLength(self, line: int, /) -> int:
        r"""How many characters are on a line, including end of line characters?"""
    def lineReverse(self, /) -> None:
        r"""Reverse order of selected lines."""
    def lineScroll(self, columns: int, lines: int, /) -> None:
        r"""Scroll horizontally and vertically."""
    def lineScrollDown(self, /) -> None:
        r"""Scroll the document down, keeping the caret visible."""
    def lineScrollUp(self, /) -> None:
        r"""Scroll the document up, keeping the caret visible."""
    def lineState(self, line: int, /) -> int:
        r"""Retrieve the extra styling information for a line."""
    def lineTranspose(self, /) -> None:
        r"""Switch the current line with the previous."""
    def lineUp(self, /) -> None:
        r"""Move caret up one line."""
    def lineUpExtend(self, /) -> None:
        r"""Move caret up one line extending selection to new caret position."""
    def lineUpRectExtend(self, /) -> None:
        r"""Move caret up one line, extending rectangular selection to new caret position."""
    def lineVisible(self, line: int, /) -> bool:
        r"""Is a line visible?"""
    def linesJoin(self, /) -> None:
        r"""Join the lines in the target."""
    def linesOnScreen(self, /) -> int:
        r"""Retrieves the number of lines completely visible."""
    def linesSplit(self, pixelWidth: int, /) -> None:
        r"""Split the lines in the target into lines that are less wide than pixelWidth where possible."""
    def lowerCase(self, /) -> None:
        r"""Transform the selection to lower case."""
    def mainSelection(self, /) -> int:
        r"""Which selection is the main selection"""
    def marginBackN(self, margin: int, /) -> int:
        r"""Retrieve the background colour of a margin"""
    def marginCursorN(self, margin: int, /) -> int:
        r"""Retrieve the cursor shown in a margin."""
    def marginLeft(self, /) -> int:
        r"""Returns the size in pixels of the left margin."""
    def marginMaskN(self, margin: int, /) -> int:
        r"""Retrieve the marker mask of a margin."""
    def marginOptions(self, /) -> int:
        r"""Get the margin options."""
    def marginRight(self, /) -> int:
        r"""Returns the size in pixels of the right margin."""
    def marginSensitiveN(self, margin: int, /) -> bool:
        r"""Retrieve the mouse click sensitivity of a margin."""
    def marginSetStyle(self, line: int, style: int, /) -> None:
        r"""Set the style number for the text margin for a line"""
    def marginSetStyleOffset(self, style: int, /) -> None:
        r"""Get the start of the range of style numbers used for margin text"""
    def marginSetStyles(self, line: int, styles: bytes | bytearray | memoryview | str, /) -> None:
        r"""Set the style in the text margin for a line"""
    def marginSetText(self, line: int, text: bytes | bytearray | memoryview | str, /) -> None:
        r"""Set the text in the text margin for a line"""
    def marginStyle(self, line: int, /) -> int:
        r"""Get the style number for the text margin for a line"""
    def marginStyleOffset(self, /) -> int:
        r"""Get the start of the range of style numbers used for margin text"""
    def marginStyles(self, line: int, /) -> PySide6.QtCore.QByteArray:
        r"""Get the styles in the text margin for a line"""
    def marginText(self, line: int, /) -> PySide6.QtCore.QByteArray:
        r"""Get the text in the text margin for a line"""
    def marginTextClearAll(self, /) -> None:
        r"""Clear the margin text on all lines"""
    def marginTypeN(self, margin: int, /) -> int:
        r"""Retrieve the type of a margin."""
    def marginWidthN(self, margin: int, /) -> int:
        r"""Retrieve the width of a margin in pixels."""
    def margins(self, /) -> int:
        r"""How many margins are there?."""
    def markerAdd(self, line: int, markerNumber: int, /) -> int:
        r"""Add a marker to a line, returning an ID which can be used to find or delete the marker."""
    def markerAddSet(self, line: int, markerSet: int, /) -> None:
        r"""Add a set of markers to a line."""
    def markerDefine(self, markerNumber: int, markerSymbol: int, /) -> None:
        r"""Set the symbol used for a particular marker number."""
    def markerDefinePixmap(self, markerNumber: int, pixmap: bytes | bytearray | memoryview | str, /) -> None:
        r"""Define a marker from a pixmap."""
    def markerDefineRGBAImage(self, markerNumber: int, pixels: bytes | bytearray | memoryview | str, /) -> None:
        r"""Define a marker from RGBA data. It has the width and height from RGBAImageSetWidth/Height"""
    def markerDelete(self, line: int, markerNumber: int, /) -> None:
        r"""Delete a marker from a line."""
    def markerDeleteAll(self, markerNumber: int, /) -> None:
        r"""Delete all markers with a particular number from all lines."""
    def markerDeleteHandle(self, markerHandle: int, /) -> None:
        r"""Delete a marker."""
    def markerEnableHighlight(self, enabled: bool, /) -> None:
        r"""Enable/disable highlight for current folding block (smallest one that contains the caret)"""
    def markerGet(self, line: int, /) -> int:
        r"""Get a bit mask of all the markers set on a line."""
    def markerHandleFromLine(self, line: int, which: int, /) -> int:
        r"""Retrieve marker handles of a line"""
    def markerLayer(self, markerNumber: int, /) -> int:
        r"""Get the layer used for a marker that is drawn in the text area, not the margin."""
    def markerLineFromHandle(self, markerHandle: int, /) -> int:
        r"""Retrieve the line number at which a particular marker is located."""
    def markerNext(self, lineStart: int, markerMask: int, /) -> int:
        r"""Find the next line at or after lineStart that includes a marker in mask. Return -1 when no more lines."""
    def markerNumberFromLine(self, line: int, which: int, /) -> int:
        r"""Retrieve marker number of a marker handle"""
    def markerPrevious(self, lineStart: int, markerMask: int, /) -> int:
        r"""Find the previous line before lineStart that includes a marker in mask."""
    def markerSetAlpha(self, markerNumber: int, alpha: int, /) -> None:
        r"""Set the alpha used for a marker that is drawn in the text area, not the margin."""
    def markerSetBack(self, markerNumber: int, back: int, /) -> None:
        r"""Set the background colour used for a particular marker number."""
    def markerSetBackSelected(self, markerNumber: int, back: int, /) -> None:
        r"""Set the background colour used for a particular marker number when its folding block is selected."""
    def markerSetBackSelectedTranslucent(self, markerNumber: int, back: int, /) -> None:
        r"""Set the background colour used for a particular marker number when its folding block is selected."""
    def markerSetBackTranslucent(self, markerNumber: int, back: int, /) -> None:
        r"""Set the background colour used for a particular marker number."""
    def markerSetFore(self, markerNumber: int, fore: int, /) -> None:
        r"""Set the foreground colour used for a particular marker number."""
    def markerSetForeTranslucent(self, markerNumber: int, fore: int, /) -> None:
        r"""Set the foreground colour used for a particular marker number."""
    def markerSetLayer(self, markerNumber: int, layer: int, /) -> None:
        r"""Set the layer used for a marker that is drawn in the text area, not the margin."""
    def markerSetStrokeWidth(self, markerNumber: int, hundredths: int, /) -> None:
        r"""Set the width of strokes used in .01 pixels so 50  = 1/2 pixel width."""
    def markerSymbolDefined(self, markerNumber: int, /) -> int:
        r"""Which symbol was defined for markerNumber with MarkerDefine"""
    def maxLineState(self, /) -> int:
        r"""Retrieve the last line number that has line state."""
    def modEventMask(self, /) -> int:
        r"""Get which document modification events are sent to the container."""
    def modify(self, /) -> bool:
        r"""Is the document different from when it was last saved?"""
    def mouseDownCaptures(self, /) -> bool:
        r"""Get whether mouse gets captured."""
    def mouseDwellTime(self, /) -> int:
        r"""Retrieve the time the mouse must sit still to generate a mouse dwell event."""
    def mouseSelectionRectangularSwitch(self, /) -> bool:
        r"""Whether switching to rectangular mode while selecting with the mouse is allowed."""
    def mouseWheelCaptures(self, /) -> bool:
        r"""Get whether mouse wheel can be active outside the window."""
    def moveCaretInsideView(self, /) -> None:
        r"""Move the caret inside current view if it's not there already."""
    def moveExtendsSelection(self, /) -> bool:
        r"""Get whether or not regular caret moves will extend or reduce the selection."""
    def moveSelectedLinesDown(self, /) -> None:
        r"""Move the selected lines down one line, shifting the line below before the selection"""
    def moveSelectedLinesUp(self, /) -> None:
        r"""Move the selected lines up one line, shifting the line above after the selection"""
    def multiEdgeAddLine(self, column: int, edgeColour: int, /) -> None:
        r"""Add a new vertical edge to the view."""
    def multiEdgeClearAll(self, /) -> None:
        r"""Clear all vertical edges."""
    def multiEdgeColumn(self, which: int, /) -> int:
        r"""Get multi edge positions."""
    def multiPaste(self, /) -> int:
        r"""Retrieve the effect of pasting when there are multiple selections."""
    def multipleSelectAddEach(self, /) -> None:
        r"""Add each occurrence of the main selection in the target to the set of selections. If the current selection is empty then select word around caret."""
    def multipleSelectAddNext(self, /) -> None:
        r"""Add the next occurrence of the main selection to the set of selections as main. If the current selection is empty then select word around caret."""
    def multipleSelection(self, /) -> bool:
        r"""Whether multiple selections can be made"""
    def nameOfStyle(self, style: int, /) -> PySide6.QtCore.QByteArray:
        r"""Retrieve the name of a style. Result is NUL-terminated."""
    def namedStyles(self, /) -> int:
        r"""Retrieve the number of named styles for the lexer."""
    def newLine(self, /) -> None:
        r"""Insert a new line, may use a CRLF, CR or LF depending on EOL mode."""
    def null(self, /) -> None:
        r"""Null operation."""
    def overtype(self, /) -> bool:
        r"""Returns true if overtype mode is active otherwise false is returned."""
    def pageDown(self, /) -> None:
        r"""Move caret one page down."""
    def pageDownExtend(self, /) -> None:
        r"""Move caret one page down extending selection to new caret position."""
    def pageDownRectExtend(self, /) -> None:
        r"""Move caret one page down, extending rectangular selection to new caret position."""
    def pageUp(self, /) -> None:
        r"""Move caret one page up."""
    def pageUpExtend(self, /) -> None:
        r"""Move caret one page up extending selection to new caret position."""
    def pageUpRectExtend(self, /) -> None:
        r"""Move caret one page up, extending rectangular selection to new caret position."""
    def paraDown(self, /) -> None:
        r"""Move caret down one paragraph (delimited by empty lines)."""
    def paraDownExtend(self, /) -> None:
        r"""Extend selection down one paragraph (delimited by empty lines)."""
    def paraUp(self, /) -> None:
        r"""Move caret up one paragraph (delimited by empty lines)."""
    def paraUpExtend(self, /) -> None:
        r"""Extend selection up one paragraph (delimited by empty lines)."""
    def paste(self, /) -> None:
        r"""Paste the contents of the clipboard into the document replacing the selection."""
    def pasteConvertEndings(self, /) -> bool:
        r"""Get convert-on-paste setting"""
    def phasesDraw(self, /) -> int:
        r"""How many phases is drawing done in?"""
    def pointXFromPosition(self, pos: int, /) -> int:
        r"""Retrieve the x value of the point in the window where a position is displayed."""
    def pointYFromPosition(self, pos: int, /) -> int:
        r"""Retrieve the y value of the point in the window where a position is displayed."""
    def positionAfter(self, pos: int, /) -> int:
        r"""Given a valid document position, return the next position taking code page into account. Maximum value returned is the last position in the document."""
    def positionBefore(self, pos: int, /) -> int:
        r"""Given a valid document position, return the previous position taking code page into account. Returns 0 if passed 0."""
    def positionCache(self, /) -> int:
        r"""How many entries are allocated to the position cache?"""
    def positionFromLine(self, line: int, /) -> int:
        r"""Retrieve the position at the start of a line."""
    def positionFromPoint(self, x: int, y: int, /) -> int:
        r"""Find the position from a point within the window."""
    def positionFromPointClose(self, x: int, y: int, /) -> int:
        r"""Find the position from a point within the window but return INVALID_POSITION if not close to text."""
    def positionRelative(self, pos: int, relative: int, /) -> int:
        r"""Given a valid document position, return a position that differs in a number of characters. Returned value is always between 0 and last position in document."""
    def positionRelativeCodeUnits(self, pos: int, relative: int, /) -> int:
        r"""Given a valid document position, return a position that differs in a number of UTF-16 code units. Returned value is always between 0 and last position in document. The result may point half way (2 bytes) inside a non-BMP character."""
    def primaryStyleFromStyle(self, style: int, /) -> int:
        r"""For a secondary style, return the primary style, else return the argument."""
    def printColourMode(self, /) -> int:
        r"""Returns the print colour mode."""
    def printMagnification(self, /) -> int:
        r"""Returns the print magnification."""
    def printWrapMode(self, /) -> int:
        r"""Is printing line wrapped?"""
    def privateLexerCall(self, operation: int, pointer: int, /) -> int:
        r"""For private communication between an application and a known lexer."""
    def property(self, key: bytes | bytearray | memoryview | str, /) -> PySide6.QtCore.QByteArray:
        r"""Retrieve a "property" value previously set with SetProperty. Result is NUL-terminated."""
    def propertyExpanded(self, key: bytes | bytearray | memoryview | str, /) -> PySide6.QtCore.QByteArray:
        r"""Retrieve a "property" value previously set with SetProperty, with "$()" variable replacement on returned buffer. Result is NUL-terminated."""
    def propertyInt(self, key: bytes | bytearray | memoryview | str, defaultValue: int, /) -> int:
        r"""Retrieve a "property" value previously set with SetProperty, interpreted as an int AFTER any "$()" variable replacement."""
    def propertyNames(self, /) -> PySide6.QtCore.QByteArray:
        r"""Retrieve a '\n' separated list of properties understood by the current lexer. Result is NUL-terminated."""
    def propertyType(self, name: bytes | bytearray | memoryview | str, /) -> int:
        r"""Retrieve the type of a property."""
    def punctuationChars(self, /) -> PySide6.QtCore.QByteArray:
        r"""Get the set of characters making up punctuation characters"""
    def rGBAImageSetHeight(self, height: int, /) -> None:
        r"""Set the height for future RGBA image data."""
    def rGBAImageSetScale(self, scalePercent: int, /) -> None:
        r"""Set the scale factor in percent for future RGBA image data."""
    def rGBAImageSetWidth(self, width: int, /) -> None:
        r"""Set the width for future RGBA image data."""
    def rangePointer(self, start: int, lengthRange: int, /) -> int:
        r"""Return a read-only pointer to a range of characters in the document. May move the gap so that the range is contiguous, but will only move up to lengthRange bytes."""
    def readOnly(self, /) -> bool:
        r"""In read-only mode?"""
    def rectangularSelectionAnchor(self, /) -> int:
        r"""Return the anchor position of the rectangular selection."""
    def rectangularSelectionAnchorVirtualSpace(self, /) -> int:
        r"""Return the virtual space of the anchor of the rectangular selection."""
    def rectangularSelectionCaret(self, /) -> int:
        r"""Return the caret position of the rectangular selection."""
    def rectangularSelectionCaretVirtualSpace(self, /) -> int:
        r"""Return the virtual space of the caret of the rectangular selection."""
    def rectangularSelectionModifier(self, /) -> int:
        r"""Get the modifier key used for rectangular selection."""
    def redo(self, /) -> None:
        r"""Redoes the next action on the undo history."""
    def registerImage(self, type: int, xpmData: bytes | bytearray | memoryview | str, /) -> None:
        r"""Register an XPM image for use in autocompletion lists."""
    def registerRGBAImage(self, type: int, pixels: bytes | bytearray | memoryview | str, /) -> None:
        r"""Register an RGBA image for use in autocompletion lists. It has the width and height from RGBAImageSetWidth/Height"""
    def releaseAllExtendedStyles(self, /) -> None:
        r"""Release all extended (>255) style numbers"""
    def releaseDocument(self, doc: int, /) -> None:
        r"""Release a reference to the document, deleting document if it fades to black."""
    def releaseLineCharacterIndex(self, lineCharacterIndex: int, /) -> None:
        r"""Decrease use count of line character index and remove if 0."""
    def replaceRectangular(self, length: int, text: bytes | bytearray | memoryview | str, /) -> None:
        r"""Replace the selection with text like a rectangular paste."""
    def replaceSel(self, text: bytes | bytearray | memoryview | str, /) -> None:
        r"""Replace the selected text with the argument text."""
    def replaceTarget(self, length: int, text: bytes | bytearray | memoryview | str, /) -> int:
        r"""Replace the target text with the argument text. Text is counted so it can contain NULs. Returns the length of the replacement text."""
    def replaceTargetRE(self, length: int, text: bytes | bytearray | memoryview | str, /) -> int:
        r"""Replace the target text with the argument text after \d processing. Text is counted so it can contain NULs. Looks for \d where d is between 1 and 9 and replaces these with the strings matched in the last search operation which were surrounded by \( and \). Returns the length of the replacement text including any change caused by processing the \d patterns."""
    def representation(self, encodedCharacter: bytes | bytearray | memoryview | str, /) -> PySide6.QtCore.QByteArray:
        r"""Get the way a character is drawn. Result is NUL-terminated."""
    def representationAppearance(self, encodedCharacter: bytes | bytearray | memoryview | str, /) -> int:
        r"""Get the appearance of a representation."""
    def representationColour(self, encodedCharacter: bytes | bytearray | memoryview | str, /) -> int:
        r"""Get the colour of a representation."""
    def resetElementColour(self, element: int, /) -> None:
        r"""Use the default or platform-defined colour for an element."""
    def rotateSelection(self, /) -> None:
        r"""Set the main selection to the next selection."""
    def scrollCaret(self, /) -> None:
        r"""Ensure the caret is visible."""
    def scrollRange(self, secondary: int, primary: int, /) -> None:
        r"""Scroll the argument positions and the range between them into view giving priority to the primary position then the secondary position. This may be used to make a search match visible."""
    def scrollToEnd(self, /) -> None:
        r"""Scroll to end of document."""
    def scrollToStart(self, /) -> None:
        r"""Scroll to start of document."""
    def scrollWidth(self, /) -> int:
        r"""Retrieve the document width assumed for scrolling."""
    def scrollWidthTracking(self, /) -> bool:
        r"""Retrieve whether the scroll width tracks wide lines."""
    def searchAnchor(self, /) -> None:
        r"""Sets the current caret position to be the search anchor."""
    def searchFlags(self, /) -> int:
        r"""Get the search flags used by SearchInTarget."""
    def searchInTarget(self, length: int, text: bytes | bytearray | memoryview | str, /) -> int:
        r"""Search for a counted string in the target and set the target to the found range. Text is counted so it can contain NULs. Returns start of found range or -1 for failure in which case target is not moved."""
    def searchNext(self, searchFlags: int, text: bytes | bytearray | memoryview | str, /) -> int:
        r"""Find some text starting at the search anchor. Does not ensure the selection is visible."""
    def searchPrev(self, searchFlags: int, text: bytes | bytearray | memoryview | str, /) -> int:
        r"""Find some text starting at the search anchor and moving backwards. Does not ensure the selection is visible."""
    def selAlpha(self, /) -> int:
        r"""Get the alpha of the selection."""
    def selEOLFilled(self, /) -> bool:
        r"""Is the selection end of line filled?"""
    def selectAll(self, /) -> None:
        r"""Select all the text in the document."""
    def selectionDuplicate(self, /) -> None:
        r"""Duplicate the selection. If selection empty duplicate the line containing the caret."""
    def selectionEmpty(self, /) -> bool:
        r"""Is every selected range empty?"""
    def selectionEnd(self, /) -> int:
        r"""Returns the position at the end of the selection."""
    def selectionHidden(self, /) -> bool: ...
    def selectionIsRectangle(self, /) -> bool:
        r"""Is the selection rectangular? The alternative is the more common stream selection."""
    def selectionLayer(self, /) -> int:
        r"""Get the layer for drawing selections"""
    def selectionMode(self, /) -> int:
        r"""Get the mode of the current selection."""
    def selectionNAnchor(self, selection: int, /) -> int:
        r"""Return the anchor position of the nth selection."""
    def selectionNAnchorVirtualSpace(self, selection: int, /) -> int:
        r"""Return the virtual space of the anchor of the nth selection."""
    def selectionNCaret(self, selection: int, /) -> int:
        r"""Return the caret position of the nth selection."""
    def selectionNCaretVirtualSpace(self, selection: int, /) -> int:
        r"""Return the virtual space of the caret of the nth selection."""
    def selectionNEnd(self, selection: int, /) -> int:
        r"""Returns the position at the end of the selection."""
    def selectionNEndVirtualSpace(self, selection: int, /) -> int:
        r"""Returns the virtual space at the end of the selection."""
    def selectionNStart(self, selection: int, /) -> int:
        r"""Returns the position at the start of the selection."""
    def selectionNStartVirtualSpace(self, selection: int, /) -> int:
        r"""Returns the virtual space at the start of the selection."""
    def selectionStart(self, /) -> int:
        r"""Returns the position at the start of the selection."""
    def selections(self, /) -> int:
        r"""How many selections are there?"""
    def setAccessibility(self, accessibility: int, /) -> None:
        r"""Enable or disable accessibility."""
    def setAdditionalCaretFore(self, fore: int, /) -> None:
        r"""Set the foreground colour of additional carets."""
    def setAdditionalCaretsBlink(self, additionalCaretsBlink: bool, /) -> None:
        r"""Set whether additional carets will blink"""
    def setAdditionalCaretsVisible(self, additionalCaretsVisible: bool, /) -> None:
        r"""Set whether additional carets are visible"""
    def setAdditionalSelAlpha(self, alpha: int, /) -> None:
        r"""Set the alpha of the selection."""
    def setAdditionalSelBack(self, back: int, /) -> None:
        r"""Set the background colour of additional selections. Must have previously called SetSelBack with non-zero first argument for this to have an effect."""
    def setAdditionalSelFore(self, fore: int, /) -> None:
        r"""Set the foreground colour of additional selections. Must have previously called SetSelFore with non-zero first argument for this to have an effect."""
    def setAdditionalSelectionTyping(self, additionalSelectionTyping: bool, /) -> None:
        r"""Set whether typing can be performed into multiple selections"""
    def setAnchor(self, anchor: int, /) -> None:
        r"""Set the selection anchor to a position. The anchor is the opposite end of the selection from the caret."""
    def setAutomaticFold(self, automaticFold: int, /) -> None:
        r"""Set automatic folding behaviours."""
    def setBackSpaceUnIndents(self, bsUnIndents: bool, /) -> None:
        r"""Sets whether a backspace pressed when caret is within indentation unindents."""
    def setBidirectional(self, bidirectional: int, /) -> None:
        r"""Set bidirectional text display state."""
    def setBufferedDraw(self, buffered: bool, /) -> None:
        r"""If drawing is buffered then each line of text is drawn into a bitmap buffer before drawing it to the screen to avoid flicker."""
    def setCaretFore(self, fore: int, /) -> None:
        r"""Set the foreground colour of the caret."""
    def setCaretLineBack(self, back: int, /) -> None:
        r"""Set the colour of the background of the line containing the caret."""
    def setCaretLineBackAlpha(self, alpha: int, /) -> None:
        r"""Set background alpha of the caret line."""
    def setCaretLineFrame(self, width: int, /) -> None:
        r"""Display the caret line framed. Set width != 0 to enable this option and width = 0 to disable it."""
    def setCaretLineHighlightSubLine(self, subLine: bool, /) -> None:
        r"""Set only highlighting subline instead of whole line."""
    def setCaretLineLayer(self, layer: int, /) -> None:
        r"""Set the layer of the background of the line containing the caret."""
    def setCaretLineVisible(self, show: bool, /) -> None:
        r"""Display the background of the line containing the caret in a different colour."""
    def setCaretLineVisibleAlways(self, alwaysVisible: bool, /) -> None:
        r"""Sets the caret line to always visible."""
    def setCaretPeriod(self, periodMilliseconds: int, /) -> None:
        r"""Get the time in milliseconds that the caret is on and off. 0 = steady on."""
    def setCaretSticky(self, useCaretStickyBehaviour: int, /) -> None:
        r"""Stop the caret preferred x position changing when the user types."""
    def setCaretStyle(self, caretStyle: int, /) -> None:
        r"""Set the style of the caret to be drawn."""
    def setCaretWidth(self, pixelWidth: int, /) -> None:
        r"""Set the width of the insert mode caret."""
    def setChangeHistory(self, changeHistory: int, /) -> None:
        r"""Enable or disable change history."""
    def setCharacterCategoryOptimization(self, countCharacters: int, /) -> None:
        r"""Set the number of characters to have directly indexed categories"""
    def setCharsDefault(self, /) -> None:
        r"""Reset the set of characters for whitespace and word characters to the defaults."""
    def setCodePage(self, codePage: int, /) -> None:
        r"""Set the code page used to interpret the bytes of the document as characters. The SC_CP_UTF8 value can be used to enter Unicode mode."""
    def setCommandEvents(self, commandEvents: bool, /) -> None:
        r"""Set whether command events are sent to the container."""
    def setControlCharSymbol(self, symbol: int, /) -> None:
        r"""Change the way control characters are displayed: If symbol is < 32, keep the drawn way, else, use the given character."""
    def setCurrentPos(self, caret: int, /) -> None:
        r"""Sets the position of the caret."""
    def setCursor(self, cursorType: int, /) -> None:
        r"""Sets the cursor to one of the SC_CURSOR* values."""
    def setDefaultFoldDisplayText(self, text: bytes | bytearray | memoryview | str, /) -> None:
        r"""Set the default fold display text."""
    def setDocPointer(self, doc: int, /) -> None:
        r"""Change the document object used."""
    def setEOLMode(self, eolMode: int, /) -> None:
        r"""Set the current end of line mode."""
    def setEdgeColour(self, edgeColour: int, /) -> None:
        r"""Change the colour used in edge indication."""
    def setEdgeColumn(self, column: int, /) -> None:
        r"""Set the column number of the edge. If text goes past the edge then it is highlighted."""
    def setEdgeMode(self, edgeMode: int, /) -> None:
        r"""The edge may be displayed by a line (EDGE_LINE/EDGE_MULTILINE) or by highlighting text that goes beyond it (EDGE_BACKGROUND) or not displayed at all (EDGE_NONE)."""
    def setElementColour(self, element: int, colourElement: int, /) -> None:
        r"""Set the colour of an element. Translucency (alpha) may or may not be significant and this may depend on the platform. The alpha byte should commonly be 0xff for opaque."""
    def setEmptySelection(self, caret: int, /) -> None:
        r"""Set caret to a position, while removing any existing selection."""
    def setEndAtLastLine(self, endAtLastLine: bool, /) -> None:
        r"""Sets the scroll range so that maximum scroll position has the last line at the bottom of the view (default). Setting this to false allows scrolling one page below the last line."""
    def setExtraAscent(self, extraAscent: int, /) -> None:
        r"""Set extra ascent for each line"""
    def setExtraDescent(self, extraDescent: int, /) -> None:
        r"""Set extra descent for each line"""
    def setFirstVisibleLine(self, displayLine: int, /) -> None:
        r"""Scroll so that a display line is at the top of the display."""
    def setFocus(self, focus: bool, /) -> None:
        r"""Change internal focus flag."""
    def setFoldExpanded(self, line: int, expanded: bool, /) -> None:
        r"""Show the children of a header line."""
    def setFoldFlags(self, flags: int, /) -> None:
        r"""Set some style options for folding."""
    def setFoldLevel(self, line: int, level: int, /) -> None:
        r"""Set the fold level of a line. This encodes an integer level along with flags indicating whether the line is a header and whether it is effectively white space."""
    def setFoldMarginColour(self, useSetting: bool, back: int, /) -> None:
        r"""Set one of the colours used as a chequerboard pattern in the fold margin"""
    def setFoldMarginHiColour(self, useSetting: bool, fore: int, /) -> None:
        r"""Set the other colour used as a chequerboard pattern in the fold margin"""
    def setFontLocale(self, localeName: bytes | bytearray | memoryview | str, /) -> None:
        r"""Set the locale for displaying text."""
    def setFontQuality(self, fontQuality: int, /) -> None:
        r"""Choose the quality level for text from the FontQuality enumeration."""
    def setHScrollBar(self, visible: bool, /) -> None:
        r"""Show or hide the horizontal scroll bar."""
    def setHighlightGuide(self, column: int, /) -> None:
        r"""Set the highlighted indentation guide column. 0 = no highlighted guide."""
    def setHotspotActiveBack(self, useSetting: bool, back: int, /) -> None:
        r"""Set a back colour for active hotspots."""
    def setHotspotActiveFore(self, useSetting: bool, fore: int, /) -> None:
        r"""Set a fore colour for active hotspots."""
    def setHotspotActiveUnderline(self, underline: bool, /) -> None:
        r"""Enable / Disable underlining active hotspots."""
    def setHotspotSingleLine(self, singleLine: bool, /) -> None:
        r"""Limit hotspots to single line so hotspots on two lines don't merge."""
    def setILexer(self, ilexer: int, /) -> None:
        r"""Set the lexer from an ILexer*."""
    def setIMEInteraction(self, imeInteraction: int, /) -> None:
        r"""Choose to display the IME in a window or inline."""
    def setIdentifier(self, identifier: int, /) -> None:
        r"""Set the identifier reported as idFrom in notification messages."""
    def setIdentifiers(self, style: int, identifiers: bytes | bytearray | memoryview | str, /) -> None:
        r"""Set the identifiers that are shown in a particular style"""
    def setIdleStyling(self, idleStyling: int, /) -> None:
        r"""Sets limits to idle styling."""
    def setIndent(self, indentSize: int, /) -> None:
        r"""Set the number of spaces used for one level of indentation."""
    def setIndentationGuides(self, indentView: int, /) -> None:
        r"""Show or hide indentation guides."""
    def setIndicatorCurrent(self, indicator: int, /) -> None:
        r"""Set the indicator used for IndicatorFillRange and IndicatorClearRange"""
    def setIndicatorValue(self, value: int, /) -> None:
        r"""Set the value used for IndicatorFillRange"""
    def setKeyWords(self, keyWordSet: int, keyWords: bytes | bytearray | memoryview | str, /) -> None:
        r"""Set up the key words used by the lexer."""
    def setLayoutCache(self, cacheMode: int, /) -> None:
        r"""Sets the degree of caching of layout information."""
    def setLayoutThreads(self, threads: int, /) -> None:
        r"""Set maximum number of threads used for layout"""
    def setLengthForEncode(self, bytes: int, /) -> None:
        r"""Set the length of the utf8 argument for calling EncodedFromUTF8. Set to -1 and the string will be measured to the first nul."""
    def setLineEndTypesAllowed(self, lineEndBitSet: int, /) -> None:
        r"""Set the line end types that the application wants to use. May not be used if incompatible with lexer or encoding."""
    def setLineIndentation(self, line: int, indentation: int, /) -> None:
        r"""Change the indentation of a line to a number of columns."""
    def setLineState(self, line: int, state: int, /) -> None:
        r"""Used to hold extra styling information for each line."""
    def setMainSelection(self, selection: int, /) -> None:
        r"""Set the main selection"""
    def setMarginBackN(self, margin: int, back: int, /) -> None:
        r"""Set the background colour of a margin. Only visible for SC_MARGIN_COLOUR."""
    def setMarginCursorN(self, margin: int, cursor: int, /) -> None:
        r"""Set the cursor shown when the mouse is inside a margin."""
    def setMarginLeft(self, pixelWidth: int, /) -> None:
        r"""Sets the size in pixels of the left margin."""
    def setMarginMaskN(self, margin: int, mask: int, /) -> None:
        r"""Set a mask that determines which markers are displayed in a margin."""
    def setMarginOptions(self, marginOptions: int, /) -> None:
        r"""Set the margin options."""
    def setMarginRight(self, pixelWidth: int, /) -> None:
        r"""Sets the size in pixels of the right margin."""
    def setMarginSensitiveN(self, margin: int, sensitive: bool, /) -> None:
        r"""Make a margin sensitive or insensitive to mouse clicks."""
    def setMarginTypeN(self, margin: int, marginType: int, /) -> None:
        r"""Set a margin to be either numeric or symbolic."""
    def setMarginWidthN(self, margin: int, pixelWidth: int, /) -> None:
        r"""Set the width of a margin to a width expressed in pixels."""
    def setMargins(self, margins: int, /) -> None:
        r"""Allocate a non-standard number of margins."""
    def setModEventMask(self, eventMask: int, /) -> None:
        r"""Set which document modification events are sent to the container."""
    def setMouseDownCaptures(self, captures: bool, /) -> None:
        r"""Set whether the mouse is captured when its button is pressed."""
    def setMouseDwellTime(self, periodMilliseconds: int, /) -> None:
        r"""Sets the time the mouse must sit still to generate a mouse dwell event."""
    def setMouseSelectionRectangularSwitch(self, mouseSelectionRectangularSwitch: bool, /) -> None:
        r"""Set whether switching to rectangular mode while selecting with the mouse is allowed."""
    def setMouseWheelCaptures(self, captures: bool, /) -> None:
        r"""Set whether the mouse wheel can be active outside the window."""
    def setMultiPaste(self, multiPaste: int, /) -> None:
        r"""Change the effect of pasting when there are multiple selections."""
    def setMultipleSelection(self, multipleSelection: bool, /) -> None:
        r"""Set whether multiple selections can be made"""
    def setOvertype(self, overType: bool, /) -> None:
        r"""Set to overtype (true) or insert mode."""
    def setPasteConvertEndings(self, convert: bool, /) -> None:
        r"""Enable/Disable convert-on-paste for line endings"""
    def setPhasesDraw(self, phases: int, /) -> None:
        r"""In one phase draw, text is drawn in a series of rectangular blocks with no overlap. In two phase draw, text is drawn in a series of lines allowing runs to overlap horizontally. In multiple phase draw, each element is drawn over the whole drawing area, allowing text to overlap from one line to the next."""
    def setPositionCache(self, size: int, /) -> None:
        r"""Set number of entries in position cache"""
    def setPrintColourMode(self, mode: int, /) -> None:
        r"""Modify colours when printing for clearer printed text."""
    def setPrintMagnification(self, magnification: int, /) -> None:
        r"""Sets the print magnification added to the point size of each style for printing."""
    def setPrintWrapMode(self, wrapMode: int, /) -> None:
        r"""Set printing to line wrapped (SC_WRAP_WORD) or not line wrapped (SC_WRAP_NONE)."""
    def setProperty(self, key: bytes | bytearray | memoryview | str, value: bytes | bytearray | memoryview | str, /) -> None:
        r"""Set up a value that may be used by a lexer for some optional feature."""
    def setPunctuationChars(self, characters: bytes | bytearray | memoryview | str, /) -> None:
        r"""Set the set of characters making up punctuation characters Should be called after SetWordChars."""
    def setReadOnly(self, readOnly: bool, /) -> None:
        r"""Set to read only or read write."""
    def setRectangularSelectionAnchor(self, anchor: int, /) -> None:
        r"""Set the anchor position of the rectangular selection."""
    def setRectangularSelectionAnchorVirtualSpace(self, space: int, /) -> None:
        r"""Set the virtual space of the anchor of the rectangular selection."""
    def setRectangularSelectionCaret(self, caret: int, /) -> None:
        r"""Set the caret position of the rectangular selection."""
    def setRectangularSelectionCaretVirtualSpace(self, space: int, /) -> None:
        r"""Set the virtual space of the caret of the rectangular selection."""
    def setRectangularSelectionModifier(self, modifier: int, /) -> None: ...
    def setRepresentation(self, encodedCharacter: bytes | bytearray | memoryview | str, representation: bytes | bytearray | memoryview | str, /) -> None:
        r"""Set the way a character is drawn."""
    def setRepresentationAppearance(self, encodedCharacter: bytes | bytearray | memoryview | str, appearance: int, /) -> None:
        r"""Set the appearance of a representation."""
    def setRepresentationColour(self, encodedCharacter: bytes | bytearray | memoryview | str, colour: int, /) -> None:
        r"""Set the colour of a representation."""
    def setSavePoint(self, /) -> None:
        r"""Remember the current position in the undo history as the position at which the document was saved."""
    def setScrollWidth(self, pixelWidth: int, /) -> None:
        r"""Sets the document width assumed for scrolling."""
    def setScrollWidthTracking(self, tracking: bool, /) -> None:
        r"""Sets whether the maximum width line displayed is used to set scroll width."""
    def setSearchFlags(self, searchFlags: int, /) -> None:
        r"""Set the search flags used by SearchInTarget."""
    def setSel(self, anchor: int, caret: int, /) -> None:
        r"""Select a range of text."""
    def setSelAlpha(self, alpha: int, /) -> None:
        r"""Set the alpha of the selection."""
    def setSelBack(self, useSetting: bool, back: int, /) -> None:
        r"""Set the background colour of the main and additional selections and whether to use this setting."""
    def setSelEOLFilled(self, filled: bool, /) -> None:
        r"""Set the selection to have its end of line filled or not."""
    def setSelFore(self, useSetting: bool, fore: int, /) -> None:
        r"""Set the foreground colour of the main and additional selections and whether to use this setting."""
    def setSelection(self, caret: int, anchor: int, /) -> None:
        r"""Set a simple selection"""
    def setSelectionEnd(self, caret: int, /) -> None:
        r"""Sets the position that ends the selection - this becomes the caret."""
    def setSelectionLayer(self, layer: int, /) -> None:
        r"""Set the layer for drawing selections: either opaquely on base layer or translucently over text"""
    def setSelectionMode(self, selectionMode: int, /) -> None:
        r"""Set the selection mode to stream (SC_SEL_STREAM) or rectangular (SC_SEL_RECTANGLE/SC_SEL_THIN) or by lines (SC_SEL_LINES)."""
    def setSelectionNAnchor(self, selection: int, anchor: int, /) -> None:
        r"""Set the anchor position of the nth selection."""
    def setSelectionNAnchorVirtualSpace(self, selection: int, space: int, /) -> None:
        r"""Set the virtual space of the anchor of the nth selection."""
    def setSelectionNCaret(self, selection: int, caret: int, /) -> None:
        r"""Set the caret position of the nth selection."""
    def setSelectionNCaretVirtualSpace(self, selection: int, space: int, /) -> None:
        r"""Set the virtual space of the caret of the nth selection."""
    def setSelectionNEnd(self, selection: int, caret: int, /) -> None:
        r"""Sets the position that ends the selection - this becomes the currentPosition."""
    def setSelectionNStart(self, selection: int, anchor: int, /) -> None:
        r"""Sets the position that starts the selection - this becomes the anchor."""
    def setSelectionStart(self, anchor: int, /) -> None:
        r"""Sets the position that starts the selection - this becomes the anchor."""
    def setStatus(self, status: int, /) -> None:
        r"""Change error status - 0 = OK."""
    def setStyling(self, length: int, style: int, /) -> None:
        r"""Change style from current styling position for length characters to a style and move the current styling position to after this newly styled segment."""
    def setStylingEx(self, length: int, styles: bytes | bytearray | memoryview | str, /) -> None:
        r"""Set the styles for a segment of the document."""
    def setTabDrawMode(self, tabDrawMode: int, /) -> None:
        r"""Set how tabs are drawn when visible."""
    def setTabIndents(self, tabIndents: bool, /) -> None:
        r"""Sets whether a tab pressed when caret is within indentation indents."""
    def setTabMinimumWidth(self, pixels: int, /) -> None:
        r"""Set the minimum visual width of a tab."""
    def setTabWidth(self, tabWidth: int, /) -> None:
        r"""Change the visible size of a tab to be a multiple of the width of a space character."""
    def setTargetEnd(self, end: int, /) -> None:
        r"""Sets the position that ends the target which is used for updating the document without affecting the scroll position."""
    def setTargetEndVirtualSpace(self, space: int, /) -> None:
        r"""Sets the virtual space of the target end"""
    def setTargetRange(self, start: int, end: int, /) -> None:
        r"""Sets both the start and end of the target in one call."""
    def setTargetStart(self, start: int, /) -> None:
        r"""Sets the position that starts the target which is used for updating the document without affecting the scroll position."""
    def setTargetStartVirtualSpace(self, space: int, /) -> None:
        r"""Sets the virtual space of the target start"""
    def setTechnology(self, technology: int, /) -> None:
        r"""Set the technology used."""
    def setText(self, text: bytes | bytearray | memoryview | str, /) -> None:
        r"""Replace the contents of the document with the argument text."""
    def setUndoCollection(self, collectUndo: bool, /) -> None:
        r"""Choose between collecting actions into the undo history and discarding them."""
    def setUseTabs(self, useTabs: bool, /) -> None:
        r"""Indentation will only use space characters if useTabs is false, otherwise it will use a combination of tabs and spaces."""
    def setVScrollBar(self, visible: bool, /) -> None:
        r"""Show or hide the vertical scroll bar."""
    def setViewEOL(self, visible: bool, /) -> None:
        r"""Make the end of line characters visible or invisible."""
    def setViewWS(self, viewWS: int, /) -> None:
        r"""Make white space characters invisible, always visible or visible outside indentation."""
    def setVirtualSpaceOptions(self, virtualSpaceOptions: int, /) -> None:
        r"""Set options for virtual space behaviour."""
    def setVisiblePolicy(self, visiblePolicy: int, visibleSlop: int, /) -> None:
        r"""Set the way the display area is determined when a particular line is to be moved to by Find, FindNext, GotoLine, etc."""
    def setWhitespaceBack(self, useSetting: bool, back: int, /) -> None:
        r"""Set the background colour of all whitespace and whether to use this setting."""
    def setWhitespaceChars(self, characters: bytes | bytearray | memoryview | str, /) -> None:
        r"""Set the set of characters making up whitespace for when moving or selecting by word. Should be called after SetWordChars."""
    def setWhitespaceFore(self, useSetting: bool, fore: int, /) -> None:
        r"""Set the foreground colour of all whitespace and whether to use this setting."""
    def setWhitespaceSize(self, size: int, /) -> None:
        r"""Set the size of the dots used to mark space characters."""
    def setWordChars(self, characters: bytes | bytearray | memoryview | str, /) -> None:
        r"""Set the set of characters making up words for when moving or selecting by word. First sets defaults like SetCharsDefault."""
    def setWrapIndentMode(self, wrapIndentMode: int, /) -> None:
        r"""Sets how wrapped sublines are placed. Default is fixed."""
    def setWrapMode(self, wrapMode: int, /) -> None:
        r"""Sets whether text is word wrapped."""
    def setWrapStartIndent(self, indent: int, /) -> None:
        r"""Set the start indent for wrapped lines."""
    def setWrapVisualFlags(self, wrapVisualFlags: int, /) -> None:
        r"""Set the display mode of visual flags for wrapped lines."""
    def setWrapVisualFlagsLocation(self, wrapVisualFlagsLocation: int, /) -> None:
        r"""Set the location of visual flags for wrapped lines."""
    def setXCaretPolicy(self, caretPolicy: int, caretSlop: int, /) -> None:
        r"""Set the way the caret is kept visible when going sideways. The exclusion zone is given in pixels."""
    def setXOffset(self, xOffset: int, /) -> None:
        r"""Set the xOffset (ie, horizontal scroll position)."""
    def setYCaretPolicy(self, caretPolicy: int, caretSlop: int, /) -> None:
        r"""Set the way the line the caret is on is kept visible. The exclusion zone is given in lines."""
    def setZoom(self, zoomInPoints: int, /) -> None:
        r"""Set the zoom level. This number of points is added to the size of all fonts. It may be positive to magnify or negative to reduce."""
    def set_doc(self, pdoc_: _pyside6_scintilla.ScintillaDocument, /) -> None:
        r"""Make this editor display `doc`.

        The document isn't copied -- multiple `ScintillaEdit` widgets can share it this way."""
    def showLines(self, lineStart: int, lineEnd: int, /) -> None:
        r"""Make a range of lines visible."""
    def startRecord(self, /) -> None:
        r"""Start notifying the container of all key presses and commands."""
    def startStyling(self, start: int, unused: int, /) -> None:
        r"""Set the current styling position to start. The unused parameter is no longer used and should be set to 0."""
    def status(self, /) -> int:
        r"""Get error status."""
    def stopRecord(self, /) -> None:
        r"""Stop notifying the container of all key presses and commands."""
    def stutteredPageDown(self, /) -> None:
        r"""Move caret to bottom of page, or one page down if already at bottom of page."""
    def stutteredPageDownExtend(self, /) -> None:
        r"""Move caret to bottom of page, or one page down if already at bottom of page, extending selection to new caret position."""
    def stutteredPageUp(self, /) -> None:
        r"""Move caret to top of page, or one page up if already at top of page."""
    def stutteredPageUpExtend(self, /) -> None:
        r"""Move caret to top of page, or one page up if already at top of page, extending selection to new caret position."""
    def styleAt(self, pos: int, /) -> int:
        r"""Returns the style byte at the position."""
    def styleBack(self, style: int, /) -> int:
        r"""Get the background colour of a style."""
    def styleBold(self, style: int, /) -> bool:
        r"""Get is a style bold or not."""
    def styleCase(self, style: int, /) -> int:
        r"""Get is a style mixed case, or to force upper or lower case."""
    def styleChangeable(self, style: int, /) -> bool:
        r"""Get is a style changeable or not (read only). Experimental feature, currently buggy."""
    def styleCharacterSet(self, style: int, /) -> int:
        r"""Get the character get of the font in a style."""
    def styleCheckMonospaced(self, style: int, /) -> bool:
        r"""Get whether a style may be monospaced."""
    def styleClearAll(self, /) -> None:
        r"""Clear all the styles and make equivalent to the global default style."""
    def styleEOLFilled(self, style: int, /) -> bool:
        r"""Get is a style to have its end of line filled or not."""
    def styleFont(self, style: int, /) -> PySide6.QtCore.QByteArray:
        r"""Get the font of a style. Returns the length of the fontName Result is NUL-terminated."""
    def styleFore(self, style: int, /) -> int:
        r"""Get the foreground colour of a style."""
    def styleFromSubStyle(self, subStyle: int, /) -> int:
        r"""For a sub style, return the base style, else return the argument."""
    def styleHotSpot(self, style: int, /) -> bool:
        r"""Get is a style a hotspot or not."""
    def styleIndexAt(self, pos: int, /) -> int:
        r"""Returns the unsigned style byte at the position."""
    def styleInvisibleRepresentation(self, style: int, /) -> PySide6.QtCore.QByteArray:
        r"""Get the invisible representation for a style."""
    def styleItalic(self, style: int, /) -> bool:
        r"""Get is a style italic or not."""
    def styleResetDefault(self, /) -> None:
        r"""Reset the default style to its state at startup"""
    def styleSetBack(self, style: int, back: int, /) -> None:
        r"""Set the background colour of a style."""
    def styleSetBold(self, style: int, bold: bool, /) -> None:
        r"""Set a style to be bold or not."""
    def styleSetCase(self, style: int, caseVisible: int, /) -> None:
        r"""Set a style to be mixed case, or to force upper or lower case."""
    def styleSetChangeable(self, style: int, changeable: bool, /) -> None:
        r"""Set a style to be changeable or not (read only). Experimental feature, currently buggy."""
    def styleSetCharacterSet(self, style: int, characterSet: int, /) -> None:
        r"""Set the character set of the font in a style."""
    def styleSetCheckMonospaced(self, style: int, checkMonospaced: bool, /) -> None:
        r"""Indicate that a style may be monospaced over ASCII graphics characters which enables optimizations."""
    def styleSetEOLFilled(self, style: int, eolFilled: bool, /) -> None:
        r"""Set a style to have its end of line filled or not."""
    def styleSetFont(self, style: int, fontName: bytes | bytearray | memoryview | str, /) -> None:
        r"""Set the font of a style."""
    def styleSetFore(self, style: int, fore: int, /) -> None:
        r"""Set the foreground colour of a style."""
    def styleSetHotSpot(self, style: int, hotspot: bool, /) -> None:
        r"""Set a style to be a hotspot or not."""
    def styleSetInvisibleRepresentation(self, style: int, representation: bytes | bytearray | memoryview | str, /) -> None:
        r"""Set the invisible representation for a style."""
    def styleSetItalic(self, style: int, italic: bool, /) -> None:
        r"""Set a style to be italic or not."""
    def styleSetSize(self, style: int, sizePoints: int, /) -> None:
        r"""Set the size of characters of a style."""
    def styleSetSizeFractional(self, style: int, sizeHundredthPoints: int, /) -> None:
        r"""Set the size of characters of a style. Size is in points multiplied by 100."""
    def styleSetUnderline(self, style: int, underline: bool, /) -> None:
        r"""Set a style to be underlined or not."""
    def styleSetVisible(self, style: int, visible: bool, /) -> None:
        r"""Set a style to be visible or not."""
    def styleSetWeight(self, style: int, weight: int, /) -> None:
        r"""Set the weight of characters of a style."""
    def styleSize(self, style: int, /) -> int:
        r"""Get the size of characters of a style."""
    def styleSizeFractional(self, style: int, /) -> int:
        r"""Get the size of characters of a style in points multiplied by 100"""
    def styleUnderline(self, style: int, /) -> bool:
        r"""Get is a style underlined or not."""
    def styleVisible(self, style: int, /) -> bool:
        r"""Get is a style visible or not."""
    def styleWeight(self, style: int, /) -> int:
        r"""Get the weight of characters of a style."""
    def subStyleBases(self, /) -> PySide6.QtCore.QByteArray:
        r"""Get the set of base styles that can be extended with sub styles Result is NUL-terminated."""
    def subStylesLength(self, styleBase: int, /) -> int:
        r"""The number of sub styles associated with a base style"""
    def subStylesStart(self, styleBase: int, /) -> int:
        r"""The starting style number for the sub styles associated with a base style"""
    def supportsFeature(self, feature: int, /) -> bool:
        r"""Get whether a feature is supported"""
    def swapMainAnchorCaret(self, /) -> None:
        r"""Swap that caret and anchor of the main selection."""
    def tab(self, /) -> None:
        r"""If selection is empty or all on one line replace the selection with a tab character. If more than one line selected, indent the lines."""
    def tabDrawMode(self, /) -> int:
        r"""Retrieve the current tab draw mode. Returns one of SCTD_* constants."""
    def tabIndents(self, /) -> bool:
        r"""Does a tab pressed when caret is within indentation indent?"""
    def tabMinimumWidth(self, /) -> int:
        r"""Get the minimum visual width of a tab."""
    def tabWidth(self, /) -> int:
        r"""Retrieve the visible size of a tab."""
    def tag(self, tagNumber: int, /) -> PySide6.QtCore.QByteArray:
        r"""Retrieve the value of a tag from a regular expression search. Result is NUL-terminated."""
    def tagsOfStyle(self, style: int, /) -> PySide6.QtCore.QByteArray:
        r"""Retrieve a ' ' separated list of style tags like "literal quoted string". Result is NUL-terminated."""
    def targetAsUTF8(self, /) -> PySide6.QtCore.QByteArray:
        r"""Returns the target converted to UTF8. Return the length in bytes."""
    def targetEnd(self, /) -> int:
        r"""Get the position that ends the target."""
    def targetEndVirtualSpace(self, /) -> int:
        r"""Get the virtual space of the target end"""
    def targetFromSelection(self, /) -> None:
        r"""Make the target range start and end be the same as the selection range start and end."""
    def targetStart(self, /) -> int:
        r"""Get the position that starts the target."""
    def targetStartVirtualSpace(self, /) -> int:
        r"""Get the virtual space of the target start"""
    def targetText(self, /) -> PySide6.QtCore.QByteArray:
        r"""Retrieve the text in the target."""
    def targetWholeDocument(self, /) -> None:
        r"""Sets the target to the whole document."""
    def technology(self, /) -> int:
        r"""Get the tech."""
    def textHeight(self, line: int, /) -> int:
        r"""Retrieve the height of a particular line of text in pixels."""
    def textLength(self, /) -> int:
        r"""Retrieve the number of characters in the document."""
    def textRange(self, start: int, end: int, /) -> PySide6.QtCore.QByteArray:
        r"""Alias for `get_text_range`."""
    def textWidth(self, style: int, text: bytes | bytearray | memoryview | str, /) -> int:
        r"""Measure the pixel width of some text in a particular style. NUL terminated text argument. Does not handle tab or control characters."""
    def toggleCaretSticky(self, /) -> None:
        r"""Switch between sticky and non-sticky: meant to be bound to a key."""
    def toggleFold(self, line: int, /) -> None:
        r"""Switch a header line between expanded and contracted."""
    def toggleFoldShowText(self, line: int, text: bytes | bytearray | memoryview | str, /) -> None:
        r"""Switch a header line between expanded and contracted and show some text after the line."""
    def undo(self, /) -> None:
        r"""Undo one action in the undo history."""
    def undoCollection(self, /) -> bool:
        r"""Is undo history being collected?"""
    def upperCase(self, /) -> None:
        r"""Transform the selection to upper case."""
    def usePopUp(self, popUpMode: int, /) -> None:
        r"""Set whether a pop up menu is displayed automatically when the user presses the wrong mouse button on certain areas."""
    def useTabs(self, /) -> bool:
        r"""Retrieve whether tabs will be used in indentation."""
    def userListShow(self, listType: int, itemList: bytes | bytearray | memoryview | str, /) -> None:
        r"""Display a list of strings and send notification when user chooses one."""
    def vCHome(self, /) -> None:
        r"""Move caret to before first visible character on line. If already there move to first character on line."""
    def vCHomeDisplay(self, /) -> None:
        r"""Move caret to before first visible character on display line. If already there move to first character on display line."""
    def vCHomeDisplayExtend(self, /) -> None:
        r"""Like VCHomeDisplay but extending selection to new caret position."""
    def vCHomeExtend(self, /) -> None:
        r"""Like VCHome but extending selection to new caret position."""
    def vCHomeRectExtend(self, /) -> None:
        r"""Move caret to before first visible character on line. If already there move to first character on line. In either case, extend rectangular selection to new caret position."""
    def vCHomeWrap(self, /) -> None:
        r"""Like VCHome but when word-wrap is enabled goes first to start of display line VCHomeDisplay, then behaves like VCHome."""
    def vCHomeWrapExtend(self, /) -> None:
        r"""Like VCHomeExtend but when word-wrap is enabled extends first to start of display line VCHomeDisplayExtend, then behaves like VCHomeExtend."""
    def vScrollBar(self, /) -> bool:
        r"""Is the vertical scroll bar visible?"""
    def verticalCentreCaret(self, /) -> None:
        r"""Centre current line in window."""
    def viewEOL(self, /) -> bool:
        r"""Are the end of line characters visible?"""
    def viewWS(self, /) -> int:
        r"""Are white space characters currently visible? Returns one of SCWS_* constants."""
    def virtualSpaceOptions(self, /) -> int:
        r"""Return options for virtual space behaviour."""
    def visibleFromDocLine(self, docLine: int, /) -> int:
        r"""Find the display line of a document line taking hidden lines into account."""
    def whitespaceChars(self, /) -> PySide6.QtCore.QByteArray:
        r"""Get the set of characters making up whitespace for when moving or selecting by word."""
    def whitespaceSize(self, /) -> int:
        r"""Get the size of the dots used to mark space characters."""
    def wordChars(self, /) -> PySide6.QtCore.QByteArray:
        r"""Get the set of characters making up words for when moving or selecting by word. Returns the number of characters"""
    def wordEndPosition(self, pos: int, onlyWordCharacters: bool, /) -> int:
        r"""Get position of end of word."""
    def wordLeft(self, /) -> None:
        r"""Move caret left one word."""
    def wordLeftEnd(self, /) -> None:
        r"""Move caret left one word, position cursor at end of word."""
    def wordLeftEndExtend(self, /) -> None:
        r"""Move caret left one word, position cursor at end of word, extending selection to new caret position."""
    def wordLeftExtend(self, /) -> None:
        r"""Move caret left one word extending selection to new caret position."""
    def wordPartLeft(self, /) -> None:
        r"""Move to the previous change in capitalisation."""
    def wordPartLeftExtend(self, /) -> None:
        r"""Move to the previous change in capitalisation extending selection to new caret position."""
    def wordPartRight(self, /) -> None:
        r"""Move to the change next in capitalisation."""
    def wordPartRightExtend(self, /) -> None:
        r"""Move to the next change in capitalisation extending selection to new caret position."""
    def wordRight(self, /) -> None:
        r"""Move caret right one word."""
    def wordRightEnd(self, /) -> None:
        r"""Move caret right one word, position cursor at end of word."""
    def wordRightEndExtend(self, /) -> None:
        r"""Move caret right one word, position cursor at end of word, extending selection to new caret position."""
    def wordRightExtend(self, /) -> None:
        r"""Move caret right one word extending selection to new caret position."""
    def wordStartPosition(self, pos: int, onlyWordCharacters: bool, /) -> int:
        r"""Get position of start of word."""
    def wrapCount(self, docLine: int, /) -> int:
        r"""The number of display lines needed to wrap a document line"""
    def wrapIndentMode(self, /) -> int:
        r"""Retrieve how wrapped sublines are placed. Default is fixed."""
    def wrapMode(self, /) -> int:
        r"""Retrieve whether text is word wrapped."""
    def wrapStartIndent(self, /) -> int:
        r"""Retrive the start indent for wrapped lines."""
    def wrapVisualFlags(self, /) -> int:
        r"""Retrive the display mode of visual flags for wrapped lines."""
    def wrapVisualFlagsLocation(self, /) -> int:
        r"""Retrive the location of visual flags for wrapped lines."""
    def xOffset(self, /) -> int:
        r"""Get the xOffset (ie, horizontal scroll position)."""
    def zoom(self, /) -> int:
        r"""Retrieve the zoom level."""
    def zoomIn(self, /) -> None:
        r"""Magnify the displayed text by increasing the sizes by 1 point."""
    def zoomOut(self, /) -> None:
        r"""Make the displayed text smaller by decreasing the sizes by 1 point."""


class ScintillaEditBase(PySide6.QtWidgets.QAbstractScrollArea):
    r"""Qt widget exposing Scintilla's editor core via the raw `Scintilla.Message` API.

    `send`/`sends` send any message; `notify` and the typed signals below (`modified`, `charAdded`, `updateUi`, ...) deliver Scintilla's notifications. For a typed method per message, use the `ScintillaEdit` subclass instead."""

    aboutToCopy              : typing.ClassVar[Signal] = ... # aboutToCopy(QMimeData*)
    r"""Emitted just before selected text is copied to the clipboard, with the `QMimeData` about to be placed there.

        Connect to add extra formats (e.g. rich text) to `data` before it's copied."""
    autoCompleteCancelled    : typing.ClassVar[Signal] = ... # autoCompleteCancelled()
    r"""The user cancelled an active autocompletion list (SCN_AUTOCCANCELLED)."""
    autoCompleteSelection    : typing.ClassVar[Signal] = ... # autoCompleteSelection(Scintilla::Position,QString)
    r"""The user selected `text` from an autocompletion list, before it's inserted (SCN_AUTOCSELECTION). `position` is the start of the word being completed.

        Call `Scintilla.Message.AutoCCancel` during this signal to stop the automatic insertion."""
    buttonPressed            : typing.ClassVar[Signal] = ... # buttonPressed(QMouseEvent*)
    r"""A mouse button was pressed over the editor."""
    buttonReleased           : typing.ClassVar[Signal] = ... # buttonReleased(QMouseEvent*)
    r"""A mouse button was released over the editor."""
    callTipClick             : typing.ClassVar[Signal] = ... # callTipClick()
    r"""The user clicked the visible call tip (SCN_CALLTIPCLICK)."""
    charAdded                : typing.ClassVar[Signal] = ... # charAdded(int)
    r"""The user typed an ordinary character that was inserted into the text (SCN_CHARADDED). `ch` is its character code -- a Unicode code point in UTF-8 mode."""
    command                  : typing.ClassVar[Signal] = ... # command(Scintilla::uptr_t,Scintilla::sptr_t)
    r"""Emitted for compatibility with other Scintilla front-ends' command notifications, e.g. alongside `notifyChange` with `wParam`/`lParam` encoding `SCEN_CHANGE` and the control id."""
    doubleClick              : typing.ClassVar[Signal] = ... # doubleClick(Scintilla::Position,Scintilla::Position)
    r"""The mouse was double-clicked at `position` on `line` (SCN_DOUBLECLICK)."""
    dwellEnd                 : typing.ClassVar[Signal] = ... # dwellEnd(int,int)
    r"""The mouse pointer, which had been dwelling, moved or other activity ended the dwell (SCN_DWELLEND). `x`/`y` are where the dwell occurred."""
    dwellStart               : typing.ClassVar[Signal] = ... # dwellStart(int,int)
    r"""The mouse pointer has rested at `(x, y)` for the dwell period set with `Scintilla.Message.SetMouseDwellTime` (SCN_DWELLSTART)."""
    focusChanged             : typing.ClassVar[Signal] = ... # focusChanged(bool)
    r"""The editor gained (`True`) or lost (`False`) keyboard focus (SCN_FOCUSIN/SCN_FOCUSOUT)."""
    horizontalRangeChanged   : typing.ClassVar[Signal] = ... # horizontalRangeChanged(int,int)
    r"""The horizontal scrollbar's range changed to `max` with page size `page`."""
    horizontalScrolled       : typing.ClassVar[Signal] = ... # horizontalScrolled(int)
    r"""The view scrolled horizontally; `value` is the new horizontal scroll position."""
    hotSpotClick             : typing.ClassVar[Signal] = ... # hotSpotClick(Scintilla::Position,Scintilla::KeyMod)
    r"""The user clicked text styled with the hotspot attribute, at `position`, with `modifiers` held down (SCN_HOTSPOTCLICK)."""
    hotSpotDoubleClick       : typing.ClassVar[Signal] = ... # hotSpotDoubleClick(Scintilla::Position,Scintilla::KeyMod)
    r"""Like `hotSpotClick`, but for a double-click (SCN_HOTSPOTDOUBLECLICK)."""
    key                      : typing.ClassVar[Signal] = ... # key(int)
    r"""Reports a key press not consumed by Scintilla (SCN_KEY). Only emitted on GTK, and only for Alt/Ctrl-modified keys below 256 -- prefer `keyPressed` for a portable signal."""
    keyPressed               : typing.ClassVar[Signal] = ... # keyPressed(QKeyEvent*)
    r"""A key was pressed over the editor, after Scintilla has had a chance to handle it."""
    linesAdded               : typing.ClassVar[Signal] = ... # linesAdded(Scintilla::Position)
    r"""The number of lines in the document changed by `linesAdded` (negative if lines were removed)."""
    macroRecord              : typing.ClassVar[Signal] = ... # macroRecord(Scintilla::Message,Scintilla::uptr_t,Scintilla::sptr_t)
    r"""A recordable action occurred while macro recording is enabled (`Scintilla.Message.StartRecord`, SCN_MACRORECORD). `message`/`wParam`/`lParam` are the message to replay."""
    marginClicked            : typing.ClassVar[Signal] = ... # marginClicked(Scintilla::Position,Scintilla::KeyMod,int)
    r"""The mouse was clicked in a margin marked sensitive with `Scintilla.Message.SetMarginSensitiveN` (SCN_MARGINCLICK). `position` is the start of the clicked line and `margin` its index."""
    modified                 : typing.ClassVar[Signal] = ... # modified(Scintilla::ModificationFlags,Scintilla::Position,Scintilla::Position,Scintilla::Position,QByteArray,Scintilla::Position,Scintilla::FoldLevel,Scintilla::FoldLevel)
    r"""The document's text or styling changed, or is about to (SCN_MODIFIED). `type` is a `Scintilla.ModificationFlags` bitmask describing what; `text` holds the inserted/deleted bytes for `Scintilla.ModificationFlags.InsertText`/`DeleteText`."""
    modifyAttemptReadOnly    : typing.ClassVar[Signal] = ... # modifyAttemptReadOnly()
    r"""The user tried to edit the document while it is read-only (SCN_MODIFYATTEMPTRO)."""
    needShown                : typing.ClassVar[Signal] = ... # needShown(Scintilla::Position,Scintilla::Position)
    r"""A range of currently-hidden lines should be made visible, e.g. with `Scintilla.Message.EnsureVisible` (SCN_NEEDSHOWN)."""
    notify                   : typing.ClassVar[Signal] = ... # notify(Scintilla::NotificationData*)
    r"""Delivers every Scintilla notification, before the typed signals above are emitted for it.

        See the `NotificationData` lifetime caveat in docs/bindings.md -- prefer a typed signal where one exists."""
    notifyChange             : typing.ClassVar[Signal] = ... # notifyChange()
    r"""The document was modified; emitted alongside `command` for compatibility."""
    painted                  : typing.ClassVar[Signal] = ... # painted()
    r"""Painting has just completed (SCN_PAINTED)."""
    resized                  : typing.ClassVar[Signal] = ... # resized()
    r"""The widget was resized."""
    savePointChanged         : typing.ClassVar[Signal] = ... # savePointChanged(bool)
    r"""The document entered (`True`) or left (`False`) its save point (SCN_SAVEPOINTREACHED/SCN_SAVEPOINTLEFT)."""
    styleNeeded              : typing.ClassVar[Signal] = ... # styleNeeded(Scintilla::Position)
    r"""Container-lexer styling is needed up to `position` (SCN_STYLENEEDED). Only sent if `Scintilla.Message.SetILexer` was passed `None`."""
    textAreaClicked          : typing.ClassVar[Signal] = ... # textAreaClicked(Scintilla::Position,int)
    r"""The text area was clicked on `line`, with `modifiers` held down."""
    updateUi                 : typing.ClassVar[Signal] = ... # updateUi(Scintilla::Update)
    r"""The text, styling, selection, or scroll position may have changed (SCN_UPDATEUI). `updated` is a `Scintilla.Update` bitmask of what changed since the previous notification."""
    uriDropped               : typing.ClassVar[Signal] = ... # uriDropped(QString)
    r"""The user dragged a URI such as a file path onto the editor (SCN_URIDROPPED, GTK only)."""
    userListSelection        : typing.ClassVar[Signal] = ... # userListSelection()
    r"""The user selected an item from a user list shown with `Scintilla.Message.UserListShow` (SCN_USERLISTSELECTION)."""
    verticalRangeChanged     : typing.ClassVar[Signal] = ... # verticalRangeChanged(int,int)
    r"""The vertical scrollbar's range changed to `max` with page size `page`."""
    verticalScrolled         : typing.ClassVar[Signal] = ... # verticalScrolled(int)
    r"""The view scrolled vertically; `value` is the new top visible line."""
    zoom                     : typing.ClassVar[Signal] = ... # zoom(int)
    r"""The zoom level changed to `zoom`, e.g. via `Scintilla.Message.SetZoom` (SCN_ZOOM)."""

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def contextMenuEvent(self, event: PySide6.QtGui.QContextMenuEvent, /) -> None:
        r"""Reimplemented from `QWidget`: shows Scintilla's built-in right-click context menu."""
    def dragEnterEvent(self, event: PySide6.QtGui.QDragEnterEvent, /) -> None:
        r"""Reimplemented from `QWidget`: accepts drags carrying text or URLs, for drag-and-drop editing."""
    def dragLeaveEvent(self, event: PySide6.QtGui.QDragLeaveEvent, /) -> None:
        r"""Reimplemented from `QWidget`: cancels the drop-position indicator drawn by `dragMoveEvent`."""
    def dragMoveEvent(self, event: PySide6.QtGui.QDragMoveEvent, /) -> None:
        r"""Reimplemented from `QWidget`: moves the drop-position indicator as a drag tracks over the editor."""
    def dropEvent(self, event: PySide6.QtGui.QDropEvent, /) -> None:
        r"""Reimplemented from `QWidget`: inserts the dropped text (or file URIs), completing a drag-and-drop edit."""
    def event(self, event: PySide6.QtCore.QEvent, /) -> bool:
        r"""Reimplemented from `QObject`: routes `QEvent.Type.KeyPress` to `keyPressEvent` directly, bypassing Qt's tab-focus handling so Scintilla sees Tab/Backtab as editing keys."""
    def event_command(self, wParam: int, lParam: int, /) -> None:
        r"""Internal slot: emits `command(wParam, lParam)` for compatibility with other Scintilla front-ends."""
    def focusInEvent(self, event: PySide6.QtGui.QFocusEvent, /) -> None:
        r"""Reimplemented from `QWidget`: tells Scintilla it gained keyboard focus (SCN_FOCUSIN, `focusChanged(True)`)."""
    def focusOutEvent(self, event: PySide6.QtGui.QFocusEvent, /) -> None:
        r"""Reimplemented from `QWidget`: tells Scintilla it lost keyboard focus (SCN_FOCUSOUT, `focusChanged(False)`)."""
    def inputMethodEvent(self, event: PySide6.QtGui.QInputMethodEvent, /) -> None:
        r"""Reimplemented from `QWidget`: forwards input-method composition/commit events to Scintilla for IME text entry."""
    def inputMethodQuery(self, query: PySide6.QtCore.Qt.InputMethodQuery, /) -> typing.Any:
        r"""Reimplemented from `QWidget`: reports caret geometry, font, and surrounding text to the input method."""
    def keyPressEvent(self, event: PySide6.QtGui.QKeyEvent, /) -> None:
        r"""Reimplemented from `QWidget`: translates the key event into a Scintilla command (caret movement, deletion, character insertion, ...) and emits `keyPressed`."""
    def leaveEvent(self, event: PySide6.QtCore.QEvent, /) -> None:
        r"""Reimplemented from `QWidget`: tells Scintilla the mouse left the editor, clearing any hover state."""
    def mouseDoubleClickEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None:
        r"""Reimplemented from `QWidget`: Scintilla does its own double-click detection from `mousePressEvent`."""
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None:
        r"""Reimplemented from `QWidget`: updates the selection while dragging, and hover/dwell state."""
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None:
        r"""Reimplemented from `QWidget`: positions the caret or starts a selection, and emits `buttonPressed`."""
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent, /) -> None:
        r"""Reimplemented from `QWidget`: ends a selection drag and emits `textAreaClicked` and `buttonReleased`."""
    def notifyParent(self, scn: _pyside6_scintilla.Scintilla.NotificationData, /) -> None:
        r"""Internal slot: receives a raw Scintilla notification and emits `notify`, plus the corresponding typed signal above (e.g. `modified`, `charAdded`, `updateUi`)."""
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent, /) -> None:
        r"""Reimplemented from `QWidget`: repaints the visible document."""
    def resizeEvent(self, event: PySide6.QtGui.QResizeEvent, /) -> None:
        r"""Reimplemented from `QWidget`: updates Scintilla's view size and scrollbars, and emits `resized`."""
    def scrollContentsBy(self, arg__1: int, arg__2: int, /) -> None:
        r"""Reimplemented from `QAbstractScrollArea`: a no-op -- Scintilla repaints the viewport itself rather than blitting it."""
    def scrollHorizontal(self, value: int, /) -> None:
        r"""Scroll the view horizontally to `value`, e.g. from a connected `QScrollBar`."""
    def scrollVertical(self, value: int, /) -> None:
        r"""Scroll the view vertically to `value` (the top visible line), e.g. from a connected `QScrollBar`."""
    def send(self, iMessage: int, /, wParam: int | None = ..., lParam: int | None = ...) -> int:
        r"""Send a message to the underlying Scintilla editor and return its result.

        `iMessage` is usually a `Scintilla.Message` value, e.g. `Scintilla.Message.GetTextLength`. `wParam` and `lParam` are that message's two generic parameters, interpreted as documented for the message in the upstream Scintilla documentation."""
    def sends(self, iMessage: int, /, wParam: int | None = ..., s: bytes | bytearray | memoryview | str | None = ...) -> int:
        r"""Like `send`, but pass `s` as the message's string `lParam`.

        Use this for messages whose `lParam` is a string, e.g. `Scintilla.Message.AddText` or `Scintilla.Message.SetText`. `s` accepts `bytes`, `bytearray`, `memoryview`, or `str` (encoded as UTF-8)."""
    def wheelEvent(self, event: PySide6.QtGui.QWheelEvent, /) -> None:
        r"""Reimplemented from `QWidget`: scrolls the view, or changes zoom when Ctrl is held."""


# eof
