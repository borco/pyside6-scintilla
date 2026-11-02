# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
"""
This file contains the exact signatures for all functions in module
_pyside6_scintilla, except for defaults which are replaced by "...".
"""

# mypy: disable-error-code="override, overload-overlap"
# Module `_pyside6_scintilla`

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

    # ScintillaTypes.h's free-standing constexpr constants -- not enum
    # members, but real Scintilla.<Name> attributes at runtime.
    InvalidPosition: typing.Final = -1
    r"""Sentinel returned by position-returning `Scintilla.Message` values when there is no match or no valid position."""
    CpUtf8: typing.Final = 65001
    r"""Code page value enabling UTF-8 mode, e.g. via `Scintilla.Message.SetCodePage`. Same value as Windows' `CP_UTF8`."""
    MarkerMax: typing.Final = 31
    r"""Highest valid marker number -- up to 32 markers (0-31) can be set per line."""
    MaskHistory: typing.Final = 31457280
    r"""Bitmask (0x01E00000) isolating the change-history bits of a line's marker/margin mask."""
    MaskFolders: typing.Final = -33554432
    r"""Bitmask (0xFE000000) isolating the fold-level bits of a line's marker/margin mask. Too large for a 32-bit signed int, so its runtime value wraps to negative."""
    MaxMargin: typing.Final = 4
    r"""Highest valid margin index -- up to 5 margins (0-4) can be shown."""
    FontSizeMultiplier: typing.Final = 100
    r"""Scintilla stores font sizes as hundredths of a point internally; divide a fractional size (e.g. from `Scintilla.Message.StyleGetSizeFractional`) by this to get points."""
    TimeForever: typing.Final = 10000000
    r"""Sentinel meaning "no timeout", e.g. for `Scintilla.Message.SetMouseDwellTime`."""
    KeywordsetMax: typing.Final = 8
    r"""Highest valid `keywordSet` index accepted by `Scintilla.Message.SetKeyWords`."""
    IndicatorMax: typing.Final = 43
    r"""Highest valid indicator number."""

    class Accessibility(enum.IntEnum):
        r"""Controls whether accessibility (screen reader) support is enabled, set with `SCI_SETACCESSIBILITY`/`SCI_GETACCESSIBILITY`."""

        Disabled                  = 0x0
        Enabled                   = 0x1

    class Alpha(enum.IntEnum):
        r"""Translucency level used by alpha-blended drawing such as marker and selection layers."""

        Transparent               = 0x0
        r"""Value 0; completely transparent."""
        Opaque                    = 0xff
        r"""Value 255; fully opaque."""
        NoAlpha                   = 0x100
        r"""Legacy value (256) meaning drawing is performed opaquely directly on the base layer; prefer choosing a layer via the `Layer`-based APIs instead."""

    class AnnotationVisible(enum.IntEnum):
        r"""Display mode for line annotations, set with `SCI_ANNOTATIONSETVISIBLE`/`SCI_ANNOTATIONGETVISIBLE`."""

        Hidden                    = 0x0
        r"""Annotations are not displayed."""
        Standard                  = 0x1
        r"""Annotations are drawn left justified with no adornment."""
        Boxed                     = 0x2
        r"""Annotations are indented to match the text and are surrounded by a box."""
        Indented                  = 0x3
        r"""Annotations are indented to match the text."""

    class AutoCompleteOption(enum.IntEnum):
        r"""Options controlling autocompletion list display and selection behaviour, set with `SCI_AUTOCSETOPTIONS`."""

        Normal                    = 0x0
        FixedSize                 = 0x1
        r"""On Win32 only, uses a fixed-size list instead of one resizable by the user; also avoids a header rectangle above the list."""
        SelectFirstItem           = 0x2
        r"""Always selects the first item in the list regardless of the entered text; useful when the application's autocompletion logic already sorts so the best match is on top. Without this option, Scintilla selects the item matching the entered text."""

    class AutomaticFold(enum.IntEnum):
        r"""Bit flags choosing which parts of fold-handling behaviour Scintilla performs automatically instead of relying on the container, set with `SCI_SETAUTOMATICFOLD`."""

        None_                     = 0x0
        Show                      = 0x1
        r"""Automatically shows lines as needed, avoiding the `SCN_NEEDSHOWN` notification."""
        Click                     = 0x2
        r"""Handles clicks in the fold margin automatically, avoiding the `SCN_MARGINCLICK` notification for folding margins."""
        Change                    = 0x4
        r"""Shows lines as needed when the fold structure changes; `SCN_MODIFIED` is still sent unless disabled by the container."""

    class Bidirectional(enum.IntEnum):
        r"""Selects the default text direction for bidirectional (e.g. Arabic/Hebrew) text support, set with `SCI_SETBIDIRECTIONAL`."""

        Disabled                  = 0x0
        r"""Bidirectional support is off; also the value returned by `SCI_GETBIDIRECTIONAL` if a previous `SCI_SETBIDIRECTIONAL` call failed."""
        L2R                       = 0x1
        r"""Left-to-right is the default direction. Currently the only mode with actual bidirectional display support (experimental, Win32 DirectWrite and macOS Cocoa only); only UTF-8 documents show bidirectional behaviour."""
        R2L                       = 0x2
        r"""Right-to-left is the default direction. Reserved for future implementation; not yet functional."""

    class CaretPolicy(enum.IntEnum):
        r"""Bit flags controlling how the caret is kept in view, passed as the `caretPolicy` argument to `SCI_SETXCARETPOLICY`/`SCI_SETYCARETPOLICY` together with a `caretSlop` value."""

        Slop                      = 0x1
        r"""Enables a slop value (`caretSlop`) defining an unwanted zone near the margins (pixels for vertical margins, lines for horizontal margins) that the caret is kept out of, so surrounding context stays visible."""
        Strict                    = 0x4
        r"""Strictly enforces the slop policy: the caret is centred on the display if no slop is set, and cannot enter the unwanted zone if slop is set."""
        Even                      = 0x8
        r"""If NOT set, the left/bottom unwanted zones are extended to match the right/top ones (asymmetrical), favouring visibility of line starts and the lines following the caret."""
        Jumps                     = 0x10
        r"""Moves the display more energetically so the caret can travel further in one direction before the policy reapplies."""

    class CaretSticky(enum.IntEnum):
        r"""Controls when the caret's horizontal position on a line is remembered when moving between lines, set with `SCI_SETCARETSTICKY`."""

        Off                       = 0x0
        r"""Default: all text changes and caret position changes remember the caret's new horizontal position when moving to a different line."""
        On                        = 0x1
        r"""Only moving the caret directly via mouse or keyboard updates the remembered horizontal position; text changes do not."""
        WhiteSpace                = 0x2
        r"""Behaves like `Off` except when only space/tab characters are inserted -- in that one case the horizontal position is not updated."""

    class CaretStyle(enum.IntEnum):
        r"""Caret drawing style, set with `SCI_SETCARETSTYLE`; separate bit ranges select insert-mode, overtype-mode, and curses-mode appearance."""

        Invisible                 = 0x0
        r"""Carets are not drawn at all."""
        OverstrikeBar             = 0x0
        r"""Draws an overstrike caret as a bar; the default for overtype mode (shares value 0 with `Invisible`, but applies to the separate overtype-mode bit, not the insert-mode bits)."""
        Line                      = 0x1
        r"""Draws insertion carets as lines; the default."""
        Block                     = 0x2
        r"""Draws insertion carets as blocks."""
        InsMask                   = 0xf
        r"""Mask (lower 4 bits) isolating the insert-mode caret style bits."""
        OverstrikeBlock           = 0x10
        r"""Draws an overstrike caret as a block; OR with one of the insert-mode styles (`Line`/`Block`/`Invisible`)."""
        Curses                    = 0x20
        r"""Draws additional (non-main) carets as blocks for environments, such as a terminal, that cannot draw them otherwise; the main caret is left to the terminal."""
        BlockAfter                = 0x100
        r"""When the caret end of a range is at the end of the selection and a block caret style is chosen, draws the block outside the selection instead of inside; OR with `Block` or `Curses`."""

    class CaseInsensitiveBehaviour(enum.IntEnum):
        r"""Controls how case-insensitive autocompletion selects among matching entries, set with `SCI_AUTOCSETCASEINSENSITIVEBEHAVIOUR`."""

        RespectCase               = 0x0
        r"""Default: even with case-insensitive autocompletion, still selects the first list entry that matches the entered text in a case-sensitive way."""
        IgnoreCase                = 0x1
        r"""Ignores case entirely when selecting the matching autocompletion entry."""

    class CaseVisible(enum.IntEnum):
        r"""Forces how a style's text is displayed (upper/lower/camel case) without altering the stored text, set with `SCI_STYLESETCASE`."""

        Mixed                     = 0x0
        r"""Displays text normally, unmodified."""
        Upper                     = 0x1
        Lower                     = 0x2
        Camel                     = 0x3

    class ChangeHistoryOption(enum.IntEnum):
        r"""Bit flags enabling change-history tracking and how it is displayed, set with `SCI_SETCHANGEHISTORY`."""

        Disabled                  = 0x0
        r"""Default: change history is turned off."""
        Enabled                   = 0x1
        r"""Tracks changes to the document."""
        Markers                   = 0x2
        r"""Displays changes in the margin using the `MarkerOutline` history markers."""
        Indicators                = 0x4
        r"""Displays changes in the text using the `IndicatorNumbers` history indicators."""

    class CharacterSet(enum.IntEnum):
        r"""Character set used to display a style's text (independent of document encoding), set with `SCI_STYLESETCHARACTERSET`; useful for comments/string literals in a different language than the rest of the document. This binding's Qt platform layer (`PlatQt.cpp`) maps each value to a Qt `QTextCodec` name, so support depends only on which codecs Qt ships, not on the OS -- unlike Scintilla's native GTK/Cocoa/Win32 ports, where support and code-page mapping vary by platform."""

        Ansi                      = 0x0
        r"""Not mapped to a codec by this binding's Qt platform layer -- falls back to the same "ISO 8859-1" codec as `Default` regardless of platform."""
        Default                   = 0x1
        r"""Maps to the "ISO 8859-1" (Latin-1) codec; the default character set used by styles unless changed."""
        Symbol                    = 0x2
        r"""Not mapped to a codec by this binding's Qt platform layer -- falls back to the same "ISO 8859-1" codec as `Default` regardless of platform."""
        Mac                       = 0x4d
        r"""Maps to the "Apple Roman" codec."""
        ShiftJis                  = 0x80
        r"""Maps to the "Shift-JIS" codec."""
        Hangul                    = 0x81
        r"""Maps to the "CP949" codec."""
        Johab                     = 0x82
        r"""Not mapped to a codec by this binding's Qt platform layer -- falls back to the same "ISO 8859-1" codec as `Default` regardless of platform."""
        GB2312                    = 0x86
        r"""Maps to the "GB18030-0" codec."""
        ChineseBig5               = 0x88
        r"""Maps to the "Big5" codec."""
        Greek                     = 0xa1
        r"""Maps to the "ISO 8859-7" codec."""
        Turkish                   = 0xa2
        r"""Maps to the "ISO 8859-9" codec."""
        Vietnamese                = 0xa3
        r"""Maps to the "Windows-1258" codec."""
        Hebrew                    = 0xb1
        r"""Maps to the "ISO 8859-8" codec."""
        Arabic                    = 0xb2
        r"""Maps to the "ISO 8859-6" codec."""
        Baltic                    = 0xba
        r"""Maps to the "ISO 8859-13" codec."""
        Russian                   = 0xcc
        r"""Maps to the "KOI8-R" codec."""
        Thai                      = 0xde
        r"""Maps to the "TIS-620" codec."""
        EastEurope                = 0xee
        r"""Maps to the "ISO 8859-2" codec."""
        Oem                       = 0xff
        r"""Not mapped to a codec by this binding's Qt platform layer -- falls back to the same "ISO 8859-1" codec as `Default` regardless of platform."""
        Oem866                    = 0x362
        r"""Not mapped to a codec by this binding's Qt platform layer -- falls back to the same "ISO 8859-1" codec as `Default` regardless of platform."""
        Iso8859_15                = 0x3e8
        r"""Maps to the "ISO 8859-15" (Latin-9) codec."""
        Cyrillic                  = 0x4e3
        r"""Maps to the "Windows-1251" codec."""

    class CharacterSource(enum.IntEnum):
        r"""Identifies how a character was entered, reported as `NotificationData.characterSource` on the `SCN_CHARADDED` notification -- only available via the raw `notify` signal, since the typed `charAdded` signal only carries the character code."""

        DirectInput               = 0x0
        r"""Direct input characters."""
        TentativeInput            = 0x1
        r"""IME (inline mode) or dead key tentative input characters."""
        ImeResult                 = 0x2
        r"""IME (either inline or windowed mode) full composited string."""

    class CompletionMethods(enum.IntEnum):
        r"""Identifies how an autocompletion list selection was triggered, reported as the `listCompletionMethod` field of `SCN_AUTOCSELECTION`/`SCN_AUTOCCOMPLETED` notifications."""

        FillUp                    = 0x1
        r"""A fillup character (see `SCI_AUTOCSETFILLUPS`) triggered the completion; the character used is reported separately."""
        DoubleClick               = 0x2
        r"""A double-click on a list item triggered the completion."""
        Tab                       = 0x3
        r"""The Tab key, or `SCI_TAB`, triggered the completion."""
        Newline                   = 0x4
        r"""A newline, or `SCI_NEWLINE`, triggered the completion."""
        Command                   = 0x5
        r"""The `SCI_AUTOCSELECT` message triggered the completion."""
        SingleChoice              = 0x6
        r"""There was only a single choice in the list and 'choose single' mode was active, as set by `SCI_AUTOCSETCHOOSESINGLE`."""

    class CursorShape(enum.IntEnum):
        r"""Mouse cursor shape shown over the editor or a margin, set with `SCI_SETCURSOR`/`SCI_SETMARGINCURSORN`."""

        Normal                    = -1
        Arrow                     = 0x2
        Wait                      = 0x4
        r"""The wait cursor, shown when the mouse is over (or captured by) Scintilla and Scintilla is busy."""
        ReverseArrow              = 0x7
        r"""A reversed arrow, normally shown over margins by default."""

    class DocumentOption(enum.IntEnum):
        r"""Bit flags chosen when creating a document with `SCI_CREATEDOCUMENT`, affecting memory allocation and performance."""

        Default                   = 0x0
        StylesNone                = 0x1
        r"""Stops allocation of memory for per-character styles, treating the whole document as style 0; saves significant memory. Lexers may still style visually via indicators. Often combined with the null lexer for documents too large to lex efficiently."""
        TextLarge                 = 0x100
        r"""Allows the document to be larger than 2 GB, for 64-bit executables."""

    class EOLAnnotationVisible(enum.IntEnum):
        r"""Display mode and decoration style for end-of-line annotations, set with `SCI_EOLANNOTATIONSETVISIBLE`/`SCI_EOLANNOTATIONGETVISIBLE`."""

        Hidden                    = 0x0
        r"""End-of-line annotations are not displayed."""
        Standard                  = 0x1
        r"""Drawn left justified with no adornment."""
        Boxed                     = 0x2
        r"""Drawn surrounded by a box."""
        Stadium                   = 0x100
        r"""Surrounded with a ◖stadium◗ -- a rectangle with rounded ends."""
        FlatCircle                = 0x101
        r"""Surrounded with a |shape◗ -- flat left end, curved right end."""
        AngleCircle               = 0x102
        r"""Surrounded with a ◄shape◗ -- angled left end, curved right end."""
        CircleFlat                = 0x110
        r"""Surrounded with a ◖shape| -- curved left end, flat right end."""
        Flats                     = 0x111
        r"""Surrounded with a |shape| -- flat on both ends."""
        AngleFlat                 = 0x112
        r"""Surrounded with a ◄shape| -- angled left end, flat right end."""
        CircleAngle               = 0x120
        r"""Surrounded with a ◖shape▶ -- curved left end, angled right end."""
        FlatAngle                 = 0x121
        r"""Surrounded with a |shape▶ -- flat left end, angled right end."""
        Angles                    = 0x122
        r"""Surrounded with a ◄shape▶ -- angled on both ends."""

    class EdgeVisualStyle(enum.IntEnum):
        r"""Used with `SCI_SETEDGEMODE`/`SCI_GETEDGEMODE` to control how the long-line edge marker is displayed."""

        None_                     = 0x0
        r"""Long lines are not marked. This is the default state."""
        Line                      = 0x1
        r"""Draws a vertical line at the column set by `SCI_SETEDGECOLUMN`; works well for monospaced fonts but may not align well with proportional fonts."""
        Background                = 0x2
        r"""Changes the background colour of characters after the column limit; recommended for proportional fonts."""
        MultiLine                 = 0x3
        r"""Like `Line` but draws a configurable set of vertical lines simultaneously, using an independent dataset configured via the `SCI_MULTIEDGE*` messages."""

    class Element(enum.IntEnum):
        r"""Identifies a visual element (selection, caret, whitespace, fold/hidden line, etc.) whose colour can be get/set with `SCI_SETELEMENTCOLOUR`/`SCI_GETELEMENTCOLOUR`."""

        List                      = 0x0
        r"""Text colour in autocompletion lists; on Win32 this is currently provided by the platform layer."""
        ListBack                  = 0x1
        r"""Background colour of autocompletion lists; on Win32 this is currently provided by the platform layer."""
        ListSelected              = 0x2
        r"""Text colour of the selected item in autocompletion lists; on Win32 this is currently provided by the platform layer."""
        ListSelectedBack          = 0x3
        r"""Background colour of the selected item in autocompletion lists; on Win32 this is currently provided by the platform layer."""
        SelectionText             = 0xa
        r"""Overrides the default selection text colour."""
        SelectionBack             = 0xb
        r"""Overrides the default selection background colour; can be drawn translucently (see `SCI_SETSELECTIONLAYER`) or opaquely."""
        SelectionAdditionalText   = 0xc
        r"""Text colour used for additional selections (multiple/rectangular selection) alongside the main selection."""
        SelectionAdditionalBack   = 0xd
        r"""Background colour used for additional selections (multiple/rectangular selection) alongside the main selection."""
        SelectionSecondaryText    = 0xe
        r"""On X11/Wayland, used instead of the main selection colours when another application has taken over the 'primary selection'; commonly grey."""
        SelectionSecondaryBack    = 0xf
        r"""On X11/Wayland, used instead of the main selection colours when another application has taken over the 'primary selection'; commonly grey."""
        SelectionInactiveText     = 0x10
        r"""Colour used for the selection when the window has lost keyboard focus, customarily greyed out."""
        SelectionInactiveBack     = 0x11
        r"""Colour used for the selection when the window has lost keyboard focus, customarily greyed out."""
        SelectionInactiveAdditionalText = 0x12
        r"""Colour for additional (multiple) selections when unfocused; if not explicitly set, falls back to `SelectionInactiveText`."""
        SelectionInactiveAdditionalBack = 0x13
        r"""Colour for additional (multiple) selections when unfocused; if not explicitly set, falls back to `SelectionInactiveBack`."""
        Caret                     = 0x28
        r"""Colour of the text caret for the main selection; allows setting caret translucency, unlike the discouraged `SCI_SETCARETFORE`."""
        CaretAdditional           = 0x29
        r"""Colour of the caret for additional (multiple) selections."""
        CaretLineBack             = 0x32
        r"""Background colour of the line containing the caret; can be drawn translucently (`SCI_SETCARETLINELAYER`) or opaquely, with the highest priority over other background colours such as markers when drawn opaquely."""
        WhiteSpace                = 0x3c
        r"""Overrides the lexer-determined foreground colour of visible whitespace globally."""
        WhiteSpaceBack            = 0x3d
        r"""Overrides the lexer-determined background colour of visible whitespace globally."""
        HotSpotActive             = 0x46
        r"""Text colour of an active hot spot."""
        HotSpotActiveBack         = 0x47
        r"""Background colour of an active hot spot."""
        FoldLine                  = 0x50
        r"""Colour of the lines drawn in the text area to indicate folds (set via `SCI_SETFOLDFLAGS`); if not set, the `StylesCommon.Default` foreground colour is used."""
        HiddenLine                = 0x51
        r"""If set, draws a horizontal line in this colour to indicate hidden lines (from `SCI_HIDELINES`); a fold line drawn at the same position takes precedence."""

    class EndOfLine(enum.IntEnum):
        r"""Selects the line-ending character sequence used by `SCI_SETEOLMODE`/`SCI_CONVERTEOLS`."""

        CrLf                      = 0x0
        Cr                        = 0x1
        Lf                        = 0x2

    class FindOption(enum.IntEnum):
        r"""Flags (combinable by OR-ing) controlling how `SCI_SEARCHINTARGET` and related search messages match text, set via `SCI_SETSEARCHFLAGS`."""

        None_                     = 0x0
        r"""Default setting is a case-insensitive literal match."""
        WholeWord                 = 0x2
        r"""A match only occurs if the characters before and after are not word characters, as defined by `SCI_SETWORDCHARS`."""
        MatchCase                 = 0x4
        r"""A match only occurs with text that matches the case of the search string."""
        WordStart                 = 0x100000
        r"""A match only occurs if the character immediately before the match is not a word character (unlike `WholeWord`, the character after is not checked)."""
        RegExp                    = 0x200000
        r"""Interpret the search string as a regular expression, using Scintilla's base implementation unless combined with `Cxx11RegEx`; matches never span multiple lines."""
        Posix                     = 0x400000
        r"""Treat the regular expression in a more POSIX-compatible manner by interpreting bare '(' and ')' as tagged sections rather than requiring '\(' and '\)'; has no effect when `Cxx11RegEx` is set."""
        Cxx11RegEx                = 0x800000
        r"""Use the C++11 <regex> library instead of Scintilla's basic regular expressions, with ECMAScript semantics and Unicode-aware behaviour on UTF-8 documents; requires `RegExp` to also be set, and returns -1 with status `Status.RegEx` if the expression is invalid."""

    class FocusChange(enum.IntEnum):
        r"""Notification codes sent to the container for `SCEN_CHANGE`/`SCEN_SETFOCUS`/`SCEN_KILLFOCUS` events."""

        Killfocus                 = 0x100
        r"""Fired when Scintilla loses focus."""
        Setfocus                  = 0x200
        r"""Fired when Scintilla receives focus."""
        Change                    = 0x300
        r"""Fired when the text (not the styling) of the document changes; carries no further detail -- use the `modified` signal/`SCN_MODIFIED` for more detailed change information."""

    class FoldAction(enum.IntEnum):
        r"""Action to perform on a fold point, used with `SCI_FOLDLINE`, `SCI_FOLDCHILDREN`, and `SCI_FOLDALL`."""

        Contract                  = 0x0
        Expand                    = 0x1
        Toggle                    = 0x2
        r"""Toggles between contracted and expanded; for `SCI_FOLDALL`, the first fold header in the document is examined to decide whether to expand or contract the whole document."""
        ContractEveryLevel        = 0x4
        r"""Used only with `SCI_FOLDALL`; can be combined (OR-ed) with `Contract` or `Toggle` to contract all fold levels instead of only the top level."""

    class FoldDisplayTextStyle(enum.IntEnum):
        r"""Controls how fold-tag text (set via `SCI_TOGGLEFOLDSHOWTEXT`/`SCI_SETDEFAULTFOLDDISPLAYTEXT`) is rendered, via `SCI_FOLDDISPLAYTEXTSETSTYLE`."""

        Hidden                    = 0x0
        r"""Do not display the fold text tags. This is the default."""
        Standard                  = 0x1
        Boxed                     = 0x2
        r"""Display the fold text tags with a box drawn around them."""

    class FoldFlag(enum.IntEnum):
        r"""Bit flags controlling where fold-indicator lines are drawn in the text area, set with `SCI_SETFOLDFLAGS`."""

        None_                     = 0x0
        LineBeforeExpanded        = 0x2
        r"""Draws a line above the fold header when it is expanded."""
        LineBeforeContracted      = 0x4
        r"""Draws a line above the fold header when it is not expanded."""
        LineAfterExpanded         = 0x8
        r"""Draws a line below the fold header when it is expanded."""
        LineAfterContracted       = 0x10
        r"""Draws a line below the fold header when it is not expanded."""
        LevelNumbers              = 0x40
        r"""Displays hexadecimal fold levels in the line margin to aid debugging of folding; cannot be combined with `LineState`."""
        LineState                 = 0x80
        r"""Displays hexadecimal line state in the line margin to aid debugging of lexing and folding; cannot be used together with `LevelNumbers`."""

    class FoldLevel(enum.IntEnum):
        r"""A line's fold level and associated flags, set/got with `SCI_SETFOLDLEVEL`/`SCI_GETFOLDLEVEL` as a single 32-bit value combining a level number with flag bits."""

        None_                     = 0x0
        r"""A default level that may occur before folding is applied."""
        Base                      = 0x400
        r"""The initial fold level assigned to a line, allowing unsigned arithmetic on levels below it."""
        NumberMask                = 0xfff
        r"""Mask (0xFFF) isolating the level-number portion from the flag bits; the level number itself ranges from 0 to this mask."""
        WhiteFlag                 = 0x1000
        r"""Indicates the line is blank, so it should be treated as part of the preceding section (e.g. not a fold point) even if its level number suggests otherwise."""
        HeaderFlag                = 0x2000
        r"""Indicates the line is a header, i.e. a fold point; OR this into the level when calling `SCI_SETFOLDLEVEL`."""

    class FontQuality(enum.IntEnum):
        r"""Controls the antialiasing method used to render fonts, set/got via `SCI_SETFONTQUALITY`/`SCI_GETFONTQUALITY` (Windows only at present)."""

        QualityDefault            = 0x0
        r"""The backward-compatible default antialiasing behaviour."""
        QualityNonAntialiased     = 0x1
        QualityAntialiased        = 0x2
        QualityLcdOptimized       = 0x3
        QualityMask               = 0xf
        r"""Mask (0xF) isolating the bits used for the quality value."""

    class FontStretch(enum.IntEnum):
        r"""Horizontal stretch/condensation of a font's glyphs, set with `SCI_STYLESETSTRETCH`; corresponds to a horizontal magnification between 50% and 200%, though most fonts/platforms only support 2-3 of these values well."""

        UltraCondensed            = 0x1
        r"""Corresponds to 50% horizontal width."""
        ExtraCondensed            = 0x2
        r"""Corresponds to 62.5% horizontal width."""
        Condensed                 = 0x3
        r"""Corresponds to 75% horizontal width; one of the best-supported stretch values along with `Normal` and `Expanded`."""
        SemiCondensed             = 0x4
        r"""Corresponds to 87.5% horizontal width."""
        Normal                    = 0x5
        r"""Corresponds to 100% horizontal width (no stretch); one of the best-supported stretch values along with `Condensed` and `Expanded`."""
        SemiExpanded              = 0x6
        r"""Corresponds to 112.5% horizontal width."""
        Expanded                  = 0x7
        r"""Corresponds to 125% horizontal width; one of the best-supported stretch values along with `Condensed` and `Normal`."""
        ExtraExpanded             = 0x8
        r"""Corresponds to 150% horizontal width."""
        UltraExpanded             = 0x9
        r"""Corresponds to 200% horizontal width."""

    class FontWeight(enum.IntEnum):
        r"""Font boldness/weight, set with `SCI_STYLESETWEIGHT`; any value from 1 (very light) to 999 (very heavy) is accepted, though fonts typically only support 2-4 distinct weights."""

        Normal                    = 0x190
        r"""Standard weight (400); selected by `SCI_STYLESETBOLD` when its boolean argument is false."""
        SemiBold                  = 0x258
        r"""Semi-bold weight (600), between `Normal` and `Bold`."""
        Bold                      = 0x2bc
        r"""Bold weight (700); selected by `SCI_STYLESETBOLD` when its boolean argument is true."""

    class IMEInteraction(enum.IntEnum):
        r"""Selects how the platform's Input Method Editor (for Chinese, Japanese, or Korean text entry) is displayed, set with `SCI_SETIMEINTERACTION`."""

        Windowed                  = 0x0
        r"""The IME is shown as a separate window above Scintilla, like in other applications."""
        Inline                    = 0x1
        r"""The IME is displayed by Scintilla itself as text; works better with rectangular/multiple selection. Scintilla may ignore this setting in some cases, e.g. it may only be supported for certain languages."""

    class IdleStyling(enum.IntEnum):
        r"""Controls whether syntax styling of text outside the immediately visible area is deferred to an idle-time background task, set with `SCI_SETIDLESTYLING`."""

        None_                     = 0x0
        r"""Default: styling is performed for all currently visible text before displaying it, which may make scrolling slow on very large files."""
        ToVisible                 = 0x1
        r"""A small amount of styling is done before display, then the rest of the visible text is styled incrementally in the background; text may briefly appear uncoloured."""
        AfterVisible              = 0x2
        r"""Text after the currently visible portion is also styled in the background during idle time."""
        All                       = 0x3
        r"""Styles text both before and after the visible portion in the background during idle time."""

    class IndentView(enum.IntEnum):
        r"""Controls how far indentation guides extend on blank/empty lines, set with `SCI_SETINDENTATIONGUIDES`."""

        None_                     = 0x0
        r"""No indentation guides are shown (turns the feature off)."""
        Real                      = 0x1
        r"""Indentation guides are shown only inside real (actual) indentation white space on a line."""
        LookForward               = 0x2
        r"""Indentation guides extend beyond the actual indentation up to the level of the next non-empty line."""
        LookBoth                  = 0x3
        r"""Indentation guides extend up to whichever of the next or previous non-empty line has the greater indentation level; recommended for most languages."""

    class IndicFlag(enum.IntEnum):
        r"""Flags controlling indicator colouring behaviour, set/got with `SCI_INDICSETFLAGS`/`SCI_INDICGETFLAGS`."""

        None_                     = 0x0
        r"""Default: the indicator uses its configured fore colour."""
        ValueFore                 = 0x1
        r"""The indicator's colour is taken from the per-character indicator value (see `IndicValue`) rather than its fore setting, allowing many colours for a single indicator."""

    class IndicValue(enum.IntEnum):
        r"""Masks for packing an RGB colour into the indicator value used with `SCI_SETINDICATORVALUE` when `IndicFlag.ValueFore` is set."""

        Mask                      = 0xffffff
        r"""Mask (0xFFFFFF) used to extract the RGB colour portion from an indicator value."""
        Bit                       = 0x1000000
        r"""Bit (0x1000000) OR-ed into the RGB colour to mark it as a per-character indicator colour value."""

    class IndicatorNumbers(enum.IntEnum):
        r"""Identifies the indicator number ranges reserved for containers, IME, and change-history use, as passed to the `SCI_INDIC*` messages."""

        Container                 = 0x8
        r"""First indicator number in the range reserved for use by containers; indicators 0-7 are reserved for lexers."""
        Ime                       = 0x20
        r"""First indicator number reserved for IME (Input Method Editor) indicators."""
        ImeMax                    = 0x23
        r"""Last indicator number reserved for IME indicators."""
        HistoryRevertedToOriginInsertion = 0x24
        r"""Indicator for text that was deleted and saved but then reverted to its original state; the text has not been saved to disk."""
        HistoryRevertedToOriginDeletion = 0x25
        r"""Indicator for text that was inserted and saved but then reverted to its original state; there is text on disk that is missing."""
        HistorySavedInsertion     = 0x26
        r"""Indicator for text that was inserted and saved; this text is the same as on disk."""
        HistorySavedDeletion      = 0x27
        r"""Indicator for text that was deleted and saved; this range is the same as on disk."""
        HistoryModifiedInsertion  = 0x28
        r"""Indicator for text that was inserted but not yet saved."""
        HistoryModifiedDeletion   = 0x29
        r"""Indicator for text that was deleted but not yet saved."""
        HistoryRevertedToModifiedInsertion = 0x2a
        r"""Indicator for text that was deleted and saved but then reverted, though not to its original state; the text has not been saved to disk."""
        HistoryRevertedToModifiedDeletion = 0x2b
        r"""Indicator for text that was inserted and saved but then reverted, though not to its original state; there is text on disk that is missing."""
        Max                       = 0x2b
        r"""The last valid indicator number."""

    class IndicatorStyle(enum.IntEnum):
        r"""Visual appearance of an indicator, set with `SCI_INDICSETSTYLE` and used to highlight text such as syntax errors, deprecated names, or URLs."""

        Plain                     = 0x0
        r"""Underlined with a single, straight line."""
        Squiggle                  = 0x1
        r"""A squiggly underline; requires 3 pixels of descender space."""
        TT                        = 0x2
        r"""A line of small T shapes."""
        Diagonal                  = 0x3
        r"""Diagonal hatching."""
        Strike                    = 0x4
        Hidden                    = 0x5
        r"""An indicator with no visual effect, useful for tracking content invisibly."""
        Box                       = 0x6
        r"""A rectangle drawn around the text."""
        RoundBox                  = 0x7
        r"""A translucent rectangle with rounded corners around the text; fill and outline alpha are controlled with `SCI_INDICSETALPHA`/`SCI_INDICSETOUTLINEALPHA`."""
        StraightBox               = 0x8
        r"""Like `RoundBox` but with square corners; does not colour the top pixel of the line so indicators on contiguous lines stay visually distinct."""
        Dash                      = 0x9
        r"""A dashed underline."""
        Dots                      = 0xa
        r"""A dotted underline."""
        SquiggleLow               = 0xb
        r"""Like `Squiggle` but only 2 vertical pixels tall, so it fits under small fonts."""
        DotBox                    = 0xc
        r"""A dotted rectangle drawn with alternating alpha/outline-alpha translucency."""
        SquigglePixmap            = 0xd
        r"""A pixmap-based version of `Squiggle` for performance; appearance is worse than `Squiggle` on macOS HiDPI."""
        CompositionThick          = 0xe
        r"""A 2-pixel-thick underline near the bottom of the line, resembling the target style used in Asian language input composition."""
        CompositionThin           = 0xf
        r"""A 1-pixel-thick underline just above the bottom of the line, resembling non-target ranges in Asian language input composition."""
        FullBox                   = 0x10
        r"""Like `StraightBox` but covers the entire character area, including the top pixel."""
        TextFore                  = 0x11
        r"""Changes the text colour to the indicator's foreground colour instead of drawing a decoration."""
        Point                     = 0x12
        r"""Draws a small triangle below the start of the indicator range."""
        PointCharacter            = 0x13
        r"""Draws a small triangle below the centre of the first character of the indicator range."""
        Gradient                  = 0x14
        r"""A vertical gradient from the indicator colour/alpha at top fading to fully transparent at bottom."""
        GradientCentre            = 0x15
        r"""A vertical gradient with the colour/alpha centred in the middle, fading to fully transparent at both top and bottom."""
        PointTop                  = 0x16
        r"""Draws a small triangle above the start of the indicator range."""

    class KeyMod(enum.IntEnum):
        r"""Modifier-key flags (combinable by OR-ing) used alongside a `Keys` code in a `keyDefinition` passed to `SCI_ASSIGNCMDKEY`/`SCI_CLEARCMDKEY` for custom key bindings."""

        Norm                      = 0x0
        r"""No modifiers; useful as the zero value when building a key-binding table."""
        Shift                     = 0x1
        Ctrl                      = 0x2
        Alt                       = 0x4
        Super                     = 0x8
        r"""A system-dependent modifier key, such as the Windows key on Windows or the GTK 'Super'/Meta key on Linux."""
        Meta                      = 0x10
        r"""On macOS, the Mac Control key is mapped to this modifier (while the Mac Command key is mapped to `Ctrl`)."""

    class Keys(enum.IntEnum):
        r"""Virtual key codes used in a `keyDefinition` (with `KeyMod` modifiers) passed to `SCI_ASSIGNCMDKEY`/`SCI_CLEARCMDKEY` for custom key bindings."""

        Escape                    = 0x7
        Back                      = 0x8
        Tab                       = 0x9
        Return                    = 0xd
        Down                      = 0x12c
        Up                        = 0x12d
        Left                      = 0x12e
        Right                     = 0x12f
        Home                      = 0x130
        End                       = 0x131
        Prior                     = 0x132
        r"""Page Up key."""
        Next                      = 0x133
        r"""Page Down key."""
        Delete                    = 0x134
        Insert                    = 0x135
        Add                       = 0x136
        Subtract                  = 0x137
        Divide                    = 0x138
        Win                       = 0x139
        RWin                      = 0x13a
        Menu                      = 0x13b

    class Layer(enum.IntEnum):
        r"""Controls whether a background effect (selection or caret-line background) is drawn opaquely on the base layer or translucently under/over the text, used by `SCI_SETSELECTIONLAYER`/`SCI_SETCARETLINELAYER`."""

        Base                      = 0x0
        r"""Draw the background opaquely on the base layer."""
        UnderText                 = 0x1
        r"""Draw the background translucently under the text; does not work in single-phase drawing mode (`PhasesDraw.One`) since there is no under-text phase."""
        OverText                  = 0x2
        r"""Draw the background translucently over the text."""

    class LineCache(enum.IntEnum):
        r"""Controls which lines have their layout (wrapping/positions) cached, set with `SCI_SETLAYOUTCACHE`."""

        None_                     = 0x0
        r"""No lines are cached."""
        Caret                     = 0x1
        r"""Only the line containing the caret is cached; this is the default."""
        Page                      = 0x2
        r"""The visible lines plus the line containing the caret are cached."""
        Document                  = 0x3
        r"""All lines in the document are cached."""

    class LineCharacterIndexType(enum.IntEnum):
        r"""Identifies which line/character position index is active, used with `SCI_GETLINECHARACTERINDEX`/`SCI_ALLOCATELINECHARACTERINDEX`; only supported for UTF-8 documents."""

        None_                     = 0x0
        r"""No line-character index is active."""
        Utf32                     = 0x1
        r"""Index by whole (UTF-32) characters."""
        Utf16                     = 0x2
        r"""Index by UTF-16 code units."""

    class LineEndType(enum.IntEnum):
        r"""Selects whether only ASCII line endings or also Unicode line endings are recognized, used with `SCI_SETLINEENDTYPESALLOWED`/`SCI_GETLINEENDTYPESSUPPORTED`; Unicode mode is ineffective unless the active lexer also supports it."""

        Default                   = 0x0
        r"""Only ASCII line ends (CR, LF, CRLF) are interpreted."""
        Unicode                   = 0x1
        r"""Unicode line-ending characters are also interpreted, if the lexer supports it."""

    class MarginOption(enum.IntEnum):
        r"""Bit flags for `SCI_SETMARGINOPTIONS` that control margin click behaviour."""

        None_                     = 0x0
        SubLineSelect             = 0x1
        r"""Clicking the margin in front of a wrapped line selects only that sub-line instead of the whole wrapped line."""

    class MarginType(enum.IntEnum):
        r"""The kind of content a margin shows, set with `SCI_SETMARGINTYPEN`; by convention margin 0 is used for line numbers and the next two for symbols."""

        Symbol                    = 0x0
        r"""A symbol margin, e.g. for markers (breakpoints, bookmarks)."""
        Number                    = 0x1
        r"""A line-number margin."""
        Back                      = 0x2
        r"""A symbol margin whose background colour matches `StylesCommon.Default`'s background."""
        Fore                      = 0x3
        r"""A symbol margin whose background colour matches `StylesCommon.Default`'s foreground."""
        Text                      = 0x4
        r"""A margin showing application-defined text, set with `SCI_MARGINSETTEXT`."""
        RText                     = 0x5
        r"""Like `Text`, but right-justified."""
        Colour                    = 0x6
        r"""A symbol margin whose background colour is set explicitly with `SCI_SETMARGINBACKN`."""

    class MarkerOutline(enum.IntEnum):
        r"""Marker numbers reserved by Scintilla for change-history tracking and folding margin symbols, used with `SCI_MARKERDEFINE`."""

        HistoryRevertedToOrigin   = 0x15
        r"""Marks a line that was changed and saved but then reverted to its original state; the line differs from its on-disk state."""
        HistorySaved              = 0x16
        r"""Marks a line that was modified and saved; the line matches its on-disk state."""
        HistoryModified           = 0x17
        r"""Marks a line that was modified but not yet saved; the line differs from its on-disk state."""
        HistoryRevertedToModified = 0x18
        r"""Marks a line that was changed and saved but then reverted, though not to its original state; the line differs from its on-disk state."""
        FolderEnd                 = 0x19
        r"""In the flattened-tree folding style: a closed fold header nested inside another fold, so it needs a tree connector below it (e.g. `MarkerSymbol.CirclePlusConnected`)."""
        FolderOpenMid             = 0x1a
        r"""In the flattened-tree folding style: an open fold header nested inside another fold, so it needs a tree connector below it (e.g. `MarkerSymbol.CircleMinusConnected`)."""
        FolderMidTail             = 0x1b
        r"""In the flattened-tree folding style: the last child line of a fold that is itself nested inside another fold, combining a corner with a continuing connector for the parent (e.g. `MarkerSymbol.TCornerCurve`)."""
        FolderTail                = 0x1c
        r"""In the flattened-tree folding style: the last child line of a top-level fold (e.g. `MarkerSymbol.LCornerCurve`)."""
        FolderSub                 = 0x1d
        r"""In the flattened-tree folding style: a child line of a fold that is neither the first nor last, drawn as a plain vertical connector (e.g. `MarkerSymbol.VLine`)."""
        Folder                    = 0x1e
        r"""Marks a line where a closed fold is present; pair with `FolderOpen` using a symbol like Plus/Minus or Arrow/ArrowDown."""
        FolderOpen                = 0x1f
        r"""Marks a line where an open fold is present; pair with `Folder`."""

    class MarkerSymbol(enum.IntEnum):
        r"""Symbol drawn for a given marker number in the selection margin, assigned with `SCI_MARKERDEFINE`; by default all 32 markers use `Circle`."""

        Circle                    = 0x0
        RoundRect                 = 0x1
        Arrow                     = 0x2
        SmallRect                 = 0x3
        ShortArrow                = 0x4
        Empty                     = 0x5
        r"""An invisible symbol, useful for tracking line movement programmatically."""
        ArrowDown                 = 0x6
        Minus                     = 0x7
        Plus                      = 0x8
        VLine                     = 0x9
        LCorner                   = 0xa
        TCorner                   = 0xb
        BoxPlus                   = 0xc
        BoxPlusConnected          = 0xd
        BoxMinus                  = 0xe
        BoxMinusConnected         = 0xf
        LCornerCurve              = 0x10
        TCornerCurve              = 0x11
        CirclePlus                = 0x12
        CirclePlusConnected       = 0x13
        CircleMinus               = 0x14
        CircleMinusConnected      = 0x15
        Background                = 0x16
        r"""Changes only the background colour of the line, drawing no symbol."""
        DotDotDot                 = 0x17
        Arrows                    = 0x18
        Pixmap                    = 0x19
        r"""Used automatically when a marker is defined via `SCI_MARKERDEFINEPIXMAP`."""
        FullRect                  = 0x1a
        r"""Mirrors `Background` but changes only the margin background colour instead of the line."""
        LeftRect                  = 0x1b
        Available                 = 0x1c
        r"""A convention applications can use to indicate that a marker number is free for plugins to allocate."""
        Underline                 = 0x1d
        r"""Draws an underline across the text rather than a margin symbol."""
        RgbaImage                 = 0x1e
        r"""Used automatically when a marker is defined via `SCI_MARKERDEFINERGBAIMAGE`."""
        Bookmark                  = 0x1f
        VerticalBookmark          = 0x20
        Bar                       = 0x21
        r"""Drawn first/underneath all other markers regardless of marker number, since bars often span multiple lines (e.g. change history) while other markers mark individual lines."""
        Character                 = 0x2710
        r"""Add a Unicode code point to this base value (10000) to use that character as the marker, e.g. `Character + 9637`."""

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
        r"""Bitmask describing what kind of document change occurred, delivered as the `type`/`modification_type` parameter of `ScintillaEditBase.modified`/`ScintillaDocument.modified` (SCN_MODIFIED), and used to filter which kinds of modification get reported at all via `SCI_SETMODEVENTMASK`/`SCI_GETMODEVENTMASK`."""

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

    class MultiAutoComplete(enum.IntEnum):
        r"""Controls whether autocompleted text is inserted into just the main selection or into every selection, set with `SCI_AUTOCSETMULTI`."""

        Once                      = 0x0
        r"""Autocompleted text goes into only the main selection; this is the default."""
        Each                      = 0x1
        r"""Autocompleted text is inserted into each selection."""

    class MultiPaste(enum.IntEnum):
        r"""Controls whether pasted text goes into just the main selection or into every selection, set with `SCI_SETMULTIPASTE`."""

        Once                      = 0x0
        r"""Pasted text goes into only the main selection; this is the default."""
        Each                      = 0x1
        r"""Pasted text is inserted into each selection."""

    class Notification(enum.IntEnum):
        r"""Identifies which Scintilla notification (`SCN_*`) a `NotificationData` carries, as `NotificationData.nmhdr.code` -- delivered via the raw `notify` signal, or (for most values) a corresponding typed signal on `ScintillaEditBase` that carries the same notification already unpacked into typed parameters."""

        StyleNeeded               = 0x7d0
        r"""Corresponds to the `styleNeeded` signal."""
        CharAdded                 = 0x7d1
        r"""Corresponds to the `charAdded` signal."""
        SavePointReached          = 0x7d2
        r"""Corresponds to the `savePointChanged` signal with `dirty=False`."""
        SavePointLeft             = 0x7d3
        r"""Corresponds to the `savePointChanged` signal with `dirty=True`."""
        ModifyAttemptRO           = 0x7d4
        r"""Corresponds to the `modifyAttemptReadOnly` signal."""
        Key                       = 0x7d5
        r"""Corresponds to the `key` signal."""
        DoubleClick               = 0x7d6
        r"""Corresponds to the `doubleClick` signal."""
        UpdateUI                  = 0x7d7
        r"""Corresponds to the `updateUi` signal."""
        Modified                  = 0x7d8
        r"""Corresponds to the `modified` signal."""
        MacroRecord               = 0x7d9
        r"""Corresponds to the `macroRecord` signal."""
        MarginClick               = 0x7da
        r"""Corresponds to the `marginClicked` signal."""
        NeedShown                 = 0x7db
        r"""Corresponds to the `needShown` signal."""
        Painted                   = 0x7dd
        r"""Corresponds to the `painted` signal."""
        UserListSelection         = 0x7de
        r"""Corresponds to the `userListSelection` signal."""
        URIDropped                = 0x7df
        r"""Corresponds to the `uriDropped` signal."""
        DwellStart                = 0x7e0
        r"""Corresponds to the `dwellStart` signal."""
        DwellEnd                  = 0x7e1
        r"""Corresponds to the `dwellEnd` signal."""
        Zoom                      = 0x7e2
        r"""Corresponds to the `zoom` signal."""
        HotSpotClick              = 0x7e3
        r"""Corresponds to the `hotSpotClick` signal."""
        HotSpotDoubleClick        = 0x7e4
        r"""Corresponds to the `hotSpotDoubleClick` signal."""
        CallTipClick              = 0x7e5
        r"""Corresponds to the `callTipClick` signal."""
        AutoCSelection            = 0x7e6
        r"""Corresponds to the `autoCompleteSelection` signal."""
        IndicatorClick            = 0x7e7
        r"""The mouse was clicked over an indicator; no typed signal exists for this -- only reachable via the raw `notify` signal."""
        IndicatorRelease          = 0x7e8
        r"""The mouse button was released after a click over an indicator; no typed signal exists for this -- only reachable via the raw `notify` signal."""
        AutoCCancelled            = 0x7e9
        r"""Corresponds to the `autoCompleteCancelled` signal."""
        AutoCCharDeleted          = 0x7ea
        r"""A character was deleted from an active autocompletion word; no typed signal exists for this -- only reachable via the raw `notify` signal."""
        HotSpotReleaseClick       = 0x7eb
        r"""The mouse button was released after a click on hotspot-styled text; no typed signal exists for this -- only reachable via the raw `notify` signal."""
        FocusIn                   = 0x7ec
        r"""Corresponds to the `focusChanged` signal with `focused=True`."""
        FocusOut                  = 0x7ed
        r"""Corresponds to the `focusChanged` signal with `focused=False`."""
        AutoCCompleted            = 0x7ee
        r"""Autocompleted text has just been inserted; no typed signal exists for this -- only reachable via the raw `notify` signal."""
        MarginRightClick          = 0x7ef
        r"""The mouse was right-clicked in a sensitive margin; no typed signal exists for this -- only reachable via the raw `notify` signal."""
        AutoCSelectionChange      = 0x7f0
        r"""The current selection in an autocompletion list changed without being chosen; no typed signal exists for this -- only reachable via the raw `notify` signal."""

    class NotificationData(Shiboken.Object):

        annotationLinesAdded      = ...  # type: Scintilla.Position
        ch                        = ...  # type: int
        characterSource           = ...  # type: Scintilla.CharacterSource
        foldLevelNow              = ...  # type: Scintilla.FoldLevel
        foldLevelPrev             = ...  # type: Scintilla.FoldLevel
        lParam                    = ...  # type: Scintilla.sptr_t
        length                    = ...  # type: Scintilla.Position
        line                      = ...  # type: Scintilla.Position
        linesAdded                = ...  # type: Scintilla.Position
        listCompletionMethod      = ...  # type: Scintilla.CompletionMethods
        listType                  = ...  # type: int
        margin                    = ...  # type: int
        modificationType          = ...  # type: Scintilla.ModificationFlags
        modifiers                 = ...  # type: Scintilla.KeyMod
        position                  = ...  # type: Scintilla.Position
        token                     = ...  # type: int
        updated                   = ...  # type: Scintilla.Update
        wParam                    = ...  # type: Scintilla.uptr_t
        x                         = ...  # type: int
        y                         = ...  # type: int

        @typing.overload
        def __init__(self, /) -> None: ...
        @typing.overload
        def __init__(self, NotificationData: Scintilla.NotificationData, /) -> None: ...

        def __copy__(self, /) -> typing.Self: ...
        @property
        def text(self, /) -> PySide6.QtCore.QByteArray: ...
        def textBytes(self, /) -> PySide6.QtCore.QByteArray: ...
        @property
        def text(self) -> PySide6.QtCore.QByteArray:
            r"""The notification's text as raw document bytes: `length` bytes for SCN_MODIFIED, else NUL-terminated. Decode per the document's encoding, or use the typed signals, which deliver `str`. (`textBytes()` is the same value.)"""

    class Ordering(enum.IntEnum):
        r"""Controls how the autocompletion list passed to `SCI_AUTOCSHOW` is ordered, set with `SCI_AUTOCSETORDER` before showing the list."""

        PreSorted                 = 0x0
        r"""The default; requires the application to supply the list already in alphabetical sorted order."""
        PerformSort               = 0x1
        r"""Scintilla sorts the list itself; takes additional time compared to `PreSorted`."""
        Custom                    = 0x2
        r"""The application provides the list in a priority order other than alphabetical; requires extra processing to build a sorted index."""

    class PhasesDraw(enum.IntEnum):
        r"""Selects the drawing order/strategy for the text area, trading speed against correctly rendering overlapping pixels, set with `SCI_SETPHASESDRAW`."""

        One                       = 0x0
        r"""Deprecated single-phase drawing: each run of characters is drawn with its background in one pass, which can let a following run's background cut off an overhanging character. Should not be used by applications."""
        Two                       = 0x1
        r"""The default: draws all line backgrounds first, then all text in transparent mode; lines never overlap, so extreme ascenders/descenders are clipped."""
        Multiple                  = 0x2
        r"""Draws the whole area multiple times, layering backgrounds then text without clipping to line boundaries, allowing extreme ascenders/descenders to overflow into adjacent lines; slower than `Two`, and incompatible with buffered drawing."""

    class PopUp(enum.IntEnum):
        r"""Controls when the built-in default context/edit menu is shown, set with `SCI_USEPOPUP`."""

        Never                     = 0x0
        r"""Never show the default editing menu; context-menu messages are passed to the parent window instead."""
        All                       = 0x1
        r"""Show the default editing menu when clicking anywhere on the Scintilla window."""
        Text                      = 0x2
        r"""Show the default editing menu only when clicking on the text area."""

    class PrintOption(enum.IntEnum):
        r"""Colour mode used when printing the document, set with `SCI_SETPRINTCOLOURMODE`; useful for saving ink/toner when the editor uses a dark screen theme."""

        Normal                    = 0x0
        r"""Default: prints using the current screen colours, except line-number margins print on a white background."""
        InvertLight               = 0x1
        r"""Inverts the lightness of all colours and prints on a white background, saving ink for dark screen themes."""
        BlackOnWhite              = 0x2
        r"""Prints all text as black on a white background."""
        ColourOnWhite             = 0x3
        r"""Prints everything in its own colour on a white background."""
        ColourOnWhiteDefaultBG    = 0x4
        r"""Prints everything in its own foreground colour, but all styles up to and including the line-number style print on a white background."""
        ScreenColours             = 0x5
        r"""Prints using the current screen colours for both foreground and background; the only mode that does not force the line-number margin background to white."""

    class RepresentationAppearance(enum.IntEnum):
        r"""Flags controlling how a character representation set with `SCI_SETREPRESENTATION` is drawn, used with `SCI_SETREPRESENTATIONAPPEARANCE`."""

        Plain                     = 0x0
        r"""Draws the representation text with no decoration."""
        Blob                      = 0x1
        r"""Draws the representation text inverted inside a rounded rectangle (a small badge); this is the default appearance."""
        Colour                    = 0x10
        r"""If set, the representation is drawn in the colour set for it; if a colour is set but this flag is not, the representation shows in the colour of the underlying text instead."""

    class SelectionMode(enum.IntEnum):
        r"""The selection mode used by `SCI_SETSELECTIONMODE`/`SCI_CHANGESELECTIONMODE`/`SCI_GETSELECTIONMODE`, controlling how caret moves extend the selection."""

        Stream                    = 0x0
        r"""Regular, contiguous text selection."""
        Rectangle                 = 0x1
        r"""Rectangular (column) selection."""
        Lines                     = 0x2
        r"""Selection extended by whole lines."""
        Thin                      = 0x3
        r"""The mode entered automatically after typing into a rectangular selection, ensuring no characters remain selected."""

    class Status(enum.IntEnum):
        r"""Error/warning status codes returned by `SCI_GETSTATUS` and set by `SCI_SETSTATUS`; values 1-999 are errors and `WarnStart` (1000) and above are warnings."""

        Ok                        = 0x0
        r"""No failures."""
        Failure                   = 0x1
        r"""Generic failure."""
        BadAlloc                  = 0x2
        r"""Memory is exhausted."""
        OutsideDocument           = 0x3
        r"""An operation was attempted on a position that is outside the document."""
        WarnStart                 = 0x3e8
        r"""The threshold at and above which status codes are warnings rather than errors."""
        RegEx                     = 0x3e9
        r"""The regular expression is invalid; returned when the C++11 <regex> engine is selected and given a malformed pattern."""

    class StylesCommon(enum.IntEnum):
        r"""Predefined style numbers with special meaning, used with `SCI_STYLESETFORE` and friends; lexer styles occupy 0 to `Max`, and `SCI_STYLECLEARALL` resets every style to `Default`'s attributes."""

        Default                   = 0x20
        r"""The attributes every style is reset to by `SCI_STYLECLEARALL`."""
        LineNumber                = 0x21
        r"""Attributes of the line-number margin's text; its background colour also sets the background of any margin not used for folding (see `SCI_SETMARGINMASKN`)."""
        BraceLight                = 0x22
        r"""Attributes used to highlight a matched brace, via `SCI_BRACEHIGHLIGHT`, and its corresponding indentation guide via `SCI_SETHIGHLIGHTGUIDE`."""
        BraceBad                  = 0x23
        r"""Attributes used to mark an unmatched brace, via `SCI_BRACEBADLIGHT`."""
        ControlChar               = 0x24
        r"""Font used when drawing control characters; only font/size/bold/italic/character-set attributes apply, not colour -- see also `SCI_SETCONTROLCHARSYMBOL`."""
        IndentGuide               = 0x25
        r"""Foreground/background colours used when drawing indentation guides."""
        CallTip                   = 0x26
        r"""Attributes for call tips when `SCI_CALLTIPUSESTYLE` is used; otherwise call tips use `Default`. Only font face/size, foreground/background colour, and character set apply."""
        FoldDisplayText           = 0x27
        r"""Attributes for text tags attached to folded text."""
        LastPredefined            = 0x27
        r"""The last predefined style number (39), so client code can discover the range of predefined styles without hardcoding it."""
        Max                       = 0xff
        r"""The highest style number that can be set (255); styles between `LastPredefined` and this value are free for lexers/applications to use."""

    class Supports(enum.IntEnum):
        r"""Feature flags queried with `SCI_SUPPORTSFEATURE` to check which drawing/measurement capabilities the current platform supports."""

        LineDrawsFinal            = 0x0
        r"""Whether drawing a line draws its final position; only false on Win32 GDI."""
        PixelDivisions            = 0x1
        r"""Whether logical pixels are larger than physical pixels (sub-pixel positioning is possible); currently only true for macOS Cocoa with 'retina' displays."""
        FractionalStrokeWidth     = 0x2
        r"""Whether lines can be drawn with fractional widths like 1.5 or 0.5 pixels."""
        TranslucentStroke         = 0x3
        r"""Whether translucent lines, polygons, ellipses, and text can be drawn (e.g. true for Direct2D, false for GDI)."""
        PixelModification         = 0x4
        r"""Whether individual pixels can be modified; false for character-cell platforms like curses."""
        ThreadSafeMeasureWidths   = 0x5
        r"""Whether text measurement can be safely performed concurrently on multiple threads."""

    class TabDrawMode(enum.IntEnum):
        r"""How tab characters are drawn when white space is made visible, set with `SCI_SETTABDRAWMODE`."""

        LongArrow                 = 0x0
        r"""The default mode: an arrow stretching until the tabstop."""
        StrikeOut                 = 0x1
        r"""A horizontal line stretching until the tabstop."""
        ControlChar               = 0x2
        r"""Drawn as a control code according to the configured character representation, without any indentation."""

    class Technology(enum.IntEnum):
        r"""The drawing API/technology used for rendering, set with `SCI_SETTECHNOLOGY`; choices beyond `Default` are Windows-specific DirectWrite variants."""

        Default                   = 0x0
        r"""Use the older GDI API, compatible with all versions of Windows including Vista and XP."""
        DirectWrite               = 0x1
        r"""Use the Direct2D and DirectWrite APIs for higher quality antialiased drawing (Windows 7+)."""
        DirectWriteRetain         = 0x2
        r"""Request that the frame is retained after being presented, which may prevent drawing failures on some cards and drivers."""
        DirectWriteDC             = 0x3
        r"""Use DirectWrite to draw into a GDI DC; may work for remote access/RDP sessions."""
        DirectWrite1              = 0x4
        r"""Use DirectWrite in a lower-level way that manages graphics state more explicitly."""

    class TypeProperty(enum.IntEnum):
        r"""How to interpret the string value of a named lexer property (set via `SCI_SETPROPERTY`), as reported by `SCI_PROPERTYTYPE` -- all property values are passed as plain strings regardless of type. Only available for newer lexers; a companion to `SCI_PROPERTYNAMES` (lists property names) and `SCI_DESCRIBEPROPERTY` (a human-readable description), e.g. for building a generic lexer property editor."""

        Boolean                   = 0x0
        r"""The property's string value is "0" or "1"."""
        Integer                   = 0x1
        r"""The property's string value is a number."""
        String                    = 0x2
        r"""The property's string value is arbitrary text."""

    class UndoFlags(enum.IntEnum):
        r"""Flags passed to `SCI_ADDUNDOACTION` controlling how a container-supplied undo action interacts with coalescing of other undo actions."""

        None_                     = 0x0
        MayCoalesce               = 0x1
        r"""The container action may be coalesced together with surrounding insertion/deletion actions into a single compound action."""

    class UndoSelectionHistoryOption(enum.IntEnum):
        r"""Controls whether selection (and scroll position) state is restored when performing undo/redo, set with `SCI_SETUNDOSELECTIONHISTORY`."""

        Disabled                  = 0x0
        r"""The default: undo selection history turned off."""
        Enabled                   = 0x1
        r"""Restore the selection for each undo and redo."""
        Scroll                    = 0x2
        r"""Also restore the vertical scroll position; has no effect unless combined with `Enabled`."""

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

    class VisiblePolicy(enum.IntEnum):
        r"""Flags for `SCI_SETVISIBLEPOLICY` controlling vertical positioning when `SCI_ENSUREVISIBLEENFORCEPOLICY` is called; operates like the caret's vertical policy (`SCI_SETYCARETPOLICY`)."""

        Slop                      = 0x1
        r"""Defines an unwanted zone, a number of lines near the vertical margins where the target line should not end up, keeping it within visible context."""
        Strict                    = 0x4
        r"""Enforces the slop policy strictly: the line is centred on the display if no slop value is set, and cannot land in the unwanted zone if one is set."""

    class WhiteSpace(enum.IntEnum):
        r"""The white-space display mode set with `SCI_SETVIEWWS`/`SCI_GETVIEWWS`, controlling whether spaces and tabs are drawn as visible dots and arrows."""

        Invisible                 = 0x0
        r"""The normal display mode: white space is displayed as an empty background colour."""
        VisibleAlways             = 0x1
        r"""White space characters are always drawn as dots and arrows."""
        VisibleAfterIndent        = 0x2
        r"""Indentation white space is displayed normally, but after the first visible character on the line, white space is shown as dots and arrows."""
        VisibleOnlyInIndent       = 0x3
        r"""Only the white space used for indentation is displayed as dots and arrows; white space elsewhere on the line is shown normally."""

    class Wrap(enum.IntEnum):
        r"""The line-wrap mode set with `SCI_SETWRAPMODE` (and, partially, `SCI_SETPRINTWRAPMODE`)."""

        None_                     = 0x0
        r"""Disables line wrapping."""
        Word                      = 0x1
        r"""Wraps on word or style boundaries; if a word is longer than a line it is still wrapped before the line end."""
        Char                      = 0x2
        r"""Wraps between any characters; preferred for Asian languages where there is no white space between words. Not supported for printing."""
        WhiteSpace                = 0x3
        r"""Wraps on whitespace boundaries."""

    class WrapIndentMode(enum.IntEnum):
        r"""Controls how wrapped sublines of a line are indented relative to the first subline, set with `SCI_SETWRAPINDENTMODE`."""

        Fixed                     = 0x0
        r"""Wrapped sublines are aligned to the left of the window plus the amount set by `SCI_SETWRAPSTARTINDENT` (the default mode)."""
        Same                      = 0x1
        r"""Wrapped sublines are aligned to the first subline's indent."""
        Indent                    = 0x2
        r"""Wrapped sublines are aligned to the first subline's indent plus one more level of indentation."""
        DeepIndent                = 0x3
        r"""Wrapped sublines are aligned to the first subline's indent plus two more levels of indentation."""

    class WrapVisualFlag(enum.IntEnum):
        r"""Bit flags for `SCI_SETWRAPVISUALFLAGS` controlling which visual indicators are drawn to show a line has wrapped."""

        None_                     = 0x0
        End                       = 0x1
        r"""Draws a visual flag at the end of each wrapped subline."""
        Start                     = 0x2
        r"""Draws a visual flag at the start of each wrapped subline; the subline is indented by at least 1 to make room for the flag."""
        Margin                    = 0x4
        r"""Draws a visual flag in the line-number margin."""

    class WrapVisualLocation(enum.IntEnum):
        r"""Set with `SCI_SETWRAPVISUALFLAGSLOCATION`, controls where wrap visual flags are drawn relative to the text versus the window border."""

        Default                   = 0x0
        r"""Visual flags are drawn near the border."""
        EndByText                 = 0x1
        r"""The end-of-subline visual flag is drawn near the text instead of the border."""
        StartByText               = 0x2
        r"""The start-of-subline visual flag is drawn near the text instead of the border."""


    @staticmethod
    def LevelIsHeader(level: Scintilla.FoldLevel, /) -> bool: ...
    @staticmethod
    def LevelIsWhitespace(level: Scintilla.FoldLevel, /) -> bool: ...
    @staticmethod
    def LevelNumber(level: Scintilla.FoldLevel, /) -> int: ...
    @staticmethod
    def LevelNumberPart(level: Scintilla.FoldLevel, /) -> Scintilla.FoldLevel: ...
    @staticmethod
    def ModifierFlags(shift: bool, ctrl: bool, alt: bool, /, meta: bool = ..., super: bool = ...) -> Scintilla.KeyMod: ...


class ScintillaDocument(PySide6.QtCore.QObject):
    r"""Wraps a Scintilla document buffer independently of any `ScintillaEdit` view.

    Obtain one from an existing editor via `ScintillaEdit.get_doc()` (and share it with another editor via `set_doc()`), or construct one standalone to hold text off-screen. Exposes a subset of `ScintillaEdit`'s editing/undo API directly on the buffer, plus `modified`/`save_point`/etc. signals."""

    error_occurred           : typing.ClassVar[Signal] = ... # error_occurred(int)
    r"""An internal error occurred while editing the document. `status` is one of Scintilla's internal `Scintilla.Status` codes (e.g. out-of-memory or a malformed regular expression)."""
    modified                 : typing.ClassVar[Signal] = ... # modified(int,int,QByteArray,int,int,int,int,int)
    r"""The document's text or styling changed, or is about to (SCN_MODIFIED). `modification_type` is a `Scintilla.ModificationFlags` bitmask describing what; `text` holds the inserted/deleted text (decoded per the document's code page) for `Scintilla.ModificationFlags.InsertText`/`DeleteText`."""
    modify_attempt           : typing.ClassVar[Signal] = ... # modify_attempt()
    r"""An edit was attempted while the document is read-only (SCN_MODIFYATTEMPTRO)."""
    save_point               : typing.ClassVar[Signal] = ... # save_point(bool)
    r"""The document entered (`True`) or left (`False`) its save point (SCN_SAVEPOINTREACHED/SCN_SAVEPOINTLEFT)."""
    style_needed             : typing.ClassVar[Signal] = ... # style_needed(int)
    r"""Container-lexer styling is needed up to `pos` (SCN_STYLENEEDED). Only sent if `Scintilla.Message.SetILexer` was passed `None`."""

    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., pdoc_: Shiboken.VoidPtr | None = ...) -> None:
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
        r"""Return the document's text in the `length` bytes starting at byte `position`, decoded per the document's code page (see `insert_string`)."""
    def get_character(self, pos: int, /) -> int:
        r"""Return the character at `pos`."""
    def get_code_page(self, /) -> int:
        r"""Return the code page used to interpret the document's bytes as characters."""
    def get_end_styled(self, /) -> int:
        r"""Return the position up to which the document has been styled."""
    def get_eol_mode(self, /) -> int:
        r"""Return the line ending type (`Scintilla.EndOfLine` value) used for new lines."""
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
    def set_undo_collection(self, collect_undo: bool, /) -> bool:
        r"""Enable or disable collection of undo actions. Returns the previous setting."""
    def start_styling(self, position: int, /) -> None:
        r"""Set the styling position to `position`; subsequent `set_style_for` calls style from there."""
    def style_at(self, position: int, /) -> int:
        r"""Return the style number (0-255) at byte `position`."""
    def undo(self, /) -> int:
        r"""Undo one action from the undo history. Returns the position of the start of the change."""


class ScintillaDocumentFixed(ScintillaDocument):

    modified                 : typing.ClassVar[Signal] = ... # modified(int,int,QString,int,int,int,int,int)
    r"""The document's text or styling changed, or is about to (SCN_MODIFIED). `modification_type` is a `Scintilla.ModificationFlags` bitmask describing what; `text` holds the inserted/deleted text (decoded per the document's code page) for `Scintilla.ModificationFlags.InsertText`/`DeleteText`."""

    def __init__(self, /, parent: PySide6.QtCore.QObject | None = ..., pdoc_: Shiboken.VoidPtr | None = ...) -> None:
        r"""Wrap a Scintilla document buffer, creating a new empty one unless `pdoc_` is given.

        `pdoc_` is a native document pointer, as returned by `pointer()` -- pass it to share an existing document, e.g. one obtained via `ScintillaEdit.get_doc()`."""

    def get_byte_range(self, position: int, length: int, /) -> PySide6.QtCore.QByteArray:
        r"""Return the `length` bytes starting at byte `position` as stored, not decoded -- the bytes counterpart of `get_char_range`."""
    def get_char_range(self, position: int, length: int, /) -> str:
        r"""Return the document's text in the `length` bytes starting at byte `position`, decoded per the document's code page (see `insert_string`)."""
    def insert_string(self, position: int, text: str, /) -> None:
        r"""Insert `text` at byte `position`, encoded per the document's code page (UTF-8 for `Scintilla.CpUtf8`, the matching DBCS codec for 932/936/949/950, Latin-1 for 0)."""
    def set_style_for(self, length: int, style: int, /) -> bool:
        r"""Set the next `length` bytes from the current styling position (see `start_styling`) to `style`.

        Returns whether successful."""
    def style_at(self, position: int, /) -> int:
        r"""Return the style number (0-255) at byte `position`."""


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
    r"""The document's text or styling changed, or is about to (SCN_MODIFIED). `type` is a `Scintilla.ModificationFlags` bitmask describing what; `text` holds the inserted/deleted text (decoded per the document's encoding) for `Scintilla.ModificationFlags.InsertText`/`DeleteText`. `position`/`length` are byte positions/counts, not character ones."""
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
    def notifyParent(self, scn: Scintilla.NotificationData, /) -> None:
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
    def wheelEvent(self, event: PySide6.QtGui.QWheelEvent, /) -> None:
        r"""Reimplemented from `QWidget`: scrolls the view, or changes zoom when Ctrl is held."""


class ScintillaEditBaseFixed(ScintillaEditBase):

    autoCompleteSelection    : typing.ClassVar[Signal] = ... # autoCompleteSelection(int,QString)
    r"""The user selected `text` from an autocompletion list, before it's inserted (SCN_AUTOCSELECTION). `position` is the start of the word being completed.

        Call `Scintilla.Message.AutoCCancel` during this signal to stop the automatic insertion."""
    command                  : typing.ClassVar[Signal] = ... # command(qulonglong,qlonglong)
    r"""Emitted for compatibility with other Scintilla front-ends' command notifications, e.g. alongside `notifyChange` with `wParam`/`lParam` encoding `SCEN_CHANGE` and the control id."""
    doubleClick              : typing.ClassVar[Signal] = ... # doubleClick(int,int)
    r"""The mouse was double-clicked at `position` on `line` (SCN_DOUBLECLICK)."""
    hotSpotClick             : typing.ClassVar[Signal] = ... # hotSpotClick(int,int)
    r"""The user clicked text styled with the hotspot attribute, at `position`, with `modifiers` held down (SCN_HOTSPOTCLICK)."""
    hotSpotDoubleClick       : typing.ClassVar[Signal] = ... # hotSpotDoubleClick(int,int)
    r"""Like `hotSpotClick`, but for a double-click (SCN_HOTSPOTDOUBLECLICK)."""
    linesAdded               : typing.ClassVar[Signal] = ... # linesAdded(int)
    r"""The number of lines in the document changed by `linesAdded` (negative if lines were removed)."""
    macroRecord              : typing.ClassVar[Signal] = ... # macroRecord(int,qulonglong,qlonglong)
    r"""A recordable action occurred while macro recording is enabled (`Scintilla.Message.StartRecord`, SCN_MACRORECORD). `message`/`wParam`/`lParam` are the message to replay."""
    marginClicked            : typing.ClassVar[Signal] = ... # marginClicked(int,int,int)
    r"""The mouse was clicked in a margin marked sensitive with `Scintilla.Message.SetMarginSensitiveN` (SCN_MARGINCLICK). `position` is the start of the clicked line and `margin` its index."""
    modified                 : typing.ClassVar[Signal] = ... # modified(int,int,int,int,QString,int,int,int)
    r"""The document's text or styling changed, or is about to (SCN_MODIFIED). `type` is a `Scintilla.ModificationFlags` bitmask describing what; `text` holds the inserted/deleted text (decoded per the document's encoding) for `Scintilla.ModificationFlags.InsertText`/`DeleteText`. `position`/`length` are byte positions/counts, not character ones."""
    needShown                : typing.ClassVar[Signal] = ... # needShown(int,int)
    r"""A range of currently-hidden lines should be made visible, e.g. with `Scintilla.Message.EnsureVisible` (SCN_NEEDSHOWN)."""
    styleNeeded              : typing.ClassVar[Signal] = ... # styleNeeded(int)
    r"""Container-lexer styling is needed up to `position` (SCN_STYLENEEDED). Only sent if `Scintilla.Message.SetILexer` was passed `None`."""
    textAreaClicked          : typing.ClassVar[Signal] = ... # textAreaClicked(int,int)
    r"""The text area was clicked on `line`, with `modifiers` held down."""
    updateUi                 : typing.ClassVar[Signal] = ... # updateUi(int)
    r"""The text, styling, selection, or scroll position may have changed (SCN_UPDATEUI). `updated` is a `Scintilla.Update` bitmask of what changed since the previous notification."""

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def send(self, iMessage: int, /, wParam: int | None = ..., lParam: int | None = ...) -> int:
        r"""Send a message to the underlying Scintilla editor and return its result.

        `iMessage` is usually a `Scintilla.Message` value, e.g. `Scintilla.Message.GetTextLength`. `wParam` and `lParam` are that message's two generic parameters, interpreted as documented for the message in the upstream Scintilla documentation."""
    def sendr(self, iMessage: int, /, wParam: int | None = ...) -> PySide6.QtCore.QByteArray:
        r"""Send a message whose `lParam` is a result buffer, and return that result as bytes.

        For messages Scintilla.iface types as `stringresult`, e.g. `Scintilla.Message.GetSelText` or `Scintilla.Message.GetLexerLanguage`. The buffer is sized by first sending the message with a NULL `lParam`, as Scintilla documents, and `wParam` is passed to both sends -- so for the messages whose `wParam` is the buffer length (`GetText`, `GetCurLine`), pass that length (e.g. `textLength()`); with 0 they copy nothing and the result is all NULs. The typed `getText()`/`getCurLine()` handle this for you."""
    def sends(self, iMessage: int, wParam: int, data: PySide6.QtCore.QByteArray | bytes | bytearray, /) -> int:
        r"""Like `send`, but pass `data` as the message's string `lParam`.

        Use this for messages whose `lParam` is a string, e.g. `Scintilla.Message.SetText`. `data` is the exact bytes Scintilla receives (NUL-terminated; embedded NULs are passed through too), so it must already be in the document's encoding -- `str` isn't accepted. For text, prefer `ScintillaEdit`'s typed methods, which take and return `str`."""


class ScintillaEditFixed(ScintillaEditBaseFixed):

    def __init__(self, /, parent: PySide6.QtWidgets.QWidget | None = ...) -> None: ...

    def accessibility(self, /) -> int:
        r"""Report accessibility status.

        Sends `SCI_GETACCESSIBILITY`."""
    def addRefDocument(self, doc: int, /) -> None:
        r"""Extend life of document.

        Sends `SCI_ADDREFDOCUMENT`."""
    def addSelection(self, caret: int, anchor: int, /) -> None:
        r"""Add a selection

        Sends `SCI_ADDSELECTION`."""
    def addStyledText(self, c: PySide6.QtCore.QByteArray | bytes | bytearray, /) -> None:
        r"""Add array of cells to document.

        Sends `SCI_ADDSTYLEDTEXT`. No `length` argument: it's the byte length of the `c`."""
    def addTabStop(self, line: int, x: int, /) -> None:
        r"""Add an explicit tab stop for a line.

        Sends `SCI_ADDTABSTOP`."""
    def addText(self, text: str, /) -> None:
        r"""Add text to the document at current position.

        Sends `SCI_ADDTEXT`. No `length` argument: it's the byte length of the encoded `text`."""
    def addUndoAction(self, token: int, flags: int, /) -> None:
        r"""Add a container action to the undo stack

        Sends `SCI_ADDUNDOACTION`."""
    def additionalCaretFore(self, /) -> PySide6.QtGui.QColor:
        r"""Get the foreground colour of additional carets.

        Sends `SCI_GETADDITIONALCARETFORE`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def additionalCaretsBlink(self, /) -> bool:
        r"""Whether additional carets will blink

        Sends `SCI_GETADDITIONALCARETSBLINK`."""
    def additionalCaretsVisible(self, /) -> bool:
        r"""Whether additional carets are visible

        Sends `SCI_GETADDITIONALCARETSVISIBLE`."""
    def additionalSelAlpha(self, /) -> int:
        r"""Get the alpha of the selection.

        Sends `SCI_GETADDITIONALSELALPHA`."""
    def additionalSelectionTyping(self, /) -> bool:
        r"""Whether typing can be performed into multiple selections

        Sends `SCI_GETADDITIONALSELECTIONTYPING`."""
    def allLinesVisible(self, /) -> bool:
        r"""Are all lines visible?

        Sends `SCI_GETALLLINESVISIBLE`."""
    def allocate(self, bytes: int, /) -> None:
        r"""Enlarge the document to a particular size of text bytes.

        Sends `SCI_ALLOCATE`."""
    def allocateExtendedStyles(self, numberStyles: int, /) -> int:
        r"""Allocate some extended (>255) style numbers and return the start of the range

        Sends `SCI_ALLOCATEEXTENDEDSTYLES`."""
    def allocateLineCharacterIndex(self, lineCharacterIndex: int, /) -> None:
        r"""Request line character index be created or its use count increased.

        Sends `SCI_ALLOCATELINECHARACTERINDEX`."""
    def allocateLines(self, lines: int, /) -> None:
        r"""Enlarge the number of lines allocated.

        Sends `SCI_ALLOCATELINES`."""
    def allocateSubStyles(self, styleBase: int, numberStyles: int, /) -> int:
        r"""Allocate a set of sub styles for a particular base style, returning start of range

        Sends `SCI_ALLOCATESUBSTYLES`."""
    def anchor(self, /) -> int:
        r"""Returns the position of the opposite end of the selection to the caret.

        Sends `SCI_GETANCHOR`."""
    def annotationClearAll(self, /) -> None:
        r"""Clear the annotations from all lines

        Sends `SCI_ANNOTATIONCLEARALL`."""
    def annotationLines(self, line: int, /) -> int:
        r"""Get the number of annotation lines for a line

        Sends `SCI_ANNOTATIONGETLINES`."""
    def annotationSetStyle(self, line: int, style: int, /) -> None:
        r"""Set the style number for the annotations for a line

        Sends `SCI_ANNOTATIONSETSTYLE`."""
    def annotationSetStyleOffset(self, style: int, /) -> None:
        r"""Get the start of the range of style numbers used for annotations

        Sends `SCI_ANNOTATIONSETSTYLEOFFSET`."""
    def annotationSetStyles(self, line: int, styles: PySide6.QtCore.QByteArray | bytes | bytearray, /) -> None:
        r"""Set the annotation styles for a line

        Sends `SCI_ANNOTATIONSETSTYLES`."""
    def annotationSetText(self, line: int, text: str, /) -> None:
        r"""Set the annotation text for a line

        Sends `SCI_ANNOTATIONSETTEXT`."""
    def annotationSetVisible(self, visible: int, /) -> None:
        r"""Set the visibility for the annotations for a view

        Sends `SCI_ANNOTATIONSETVISIBLE`."""
    def annotationStyle(self, line: int, /) -> int:
        r"""Get the style number for the annotations for a line

        Sends `SCI_ANNOTATIONGETSTYLE`."""
    def annotationStyleOffset(self, /) -> int:
        r"""Get the start of the range of style numbers used for annotations

        Sends `SCI_ANNOTATIONGETSTYLEOFFSET`."""
    def annotationStyles(self, line: int, /) -> PySide6.QtCore.QByteArray:
        r"""Get the annotation styles for a line

        Sends `SCI_ANNOTATIONGETSTYLES`. Returns the result instead of filling a `styles` buffer; the message's own result (the length) is dropped."""
    def annotationText(self, line: int, /) -> str:
        r"""Get the annotation text for a line

        Sends `SCI_ANNOTATIONGETTEXT`. Returns the result instead of filling a `text` buffer; the message's own result (the length) is dropped."""
    def annotationVisible(self, /) -> int:
        r"""Get the visibility for the annotations for a view

        Sends `SCI_ANNOTATIONGETVISIBLE`."""
    def appendText(self, text: str, /) -> None:
        r"""Append a string to the end of the document without changing the selection.

        Sends `SCI_APPENDTEXT`. No `length` argument: it's the byte length of the encoded `text`."""
    def assignCmdKey(self, keyDefinition: int, sciCommand: int, /) -> None:
        r"""When key+modifier combination keyDefinition is pressed perform sciCommand.

        Sends `SCI_ASSIGNCMDKEY`."""
    def autoCActive(self, /) -> bool:
        r"""Is there an auto-completion list visible?

        Sends `SCI_AUTOCACTIVE`."""
    def autoCAutoHide(self, /) -> bool:
        r"""Retrieve whether or not autocompletion is hidden automatically when nothing matches.

        Sends `SCI_AUTOCGETAUTOHIDE`."""
    def autoCCancel(self, /) -> None:
        r"""Remove the auto-completion list from the screen.

        Sends `SCI_AUTOCCANCEL`."""
    def autoCCancelAtStart(self, /) -> bool:
        r"""Retrieve whether auto-completion cancelled by backspacing before start.

        Sends `SCI_AUTOCGETCANCELATSTART`."""
    def autoCCaseInsensitiveBehaviour(self, /) -> int:
        r"""Get auto-completion case insensitive behaviour.

        Sends `SCI_AUTOCGETCASEINSENSITIVEBEHAVIOUR`."""
    def autoCChooseSingle(self, /) -> bool:
        r"""Retrieve whether a single item auto-completion list automatically choose the item.

        Sends `SCI_AUTOCGETCHOOSESINGLE`."""
    def autoCComplete(self, /) -> None:
        r"""User has selected an item so remove the list and insert the selection.

        Sends `SCI_AUTOCCOMPLETE`."""
    def autoCCurrent(self, /) -> int:
        r"""Get currently selected item position in the auto-completion list

        Sends `SCI_AUTOCGETCURRENT`."""
    def autoCCurrentText(self, /) -> str:
        r"""Get currently selected item text in the auto-completion list Returns the length of the item text Result is NUL-terminated.

        Sends `SCI_AUTOCGETCURRENTTEXT`. Returns the result instead of filling a `text` buffer; the message's own result (the length) is dropped."""
    def autoCDropRestOfWord(self, /) -> bool:
        r"""Retrieve whether or not autocompletion deletes any word characters after the inserted text upon completion.

        Sends `SCI_AUTOCGETDROPRESTOFWORD`."""
    def autoCIgnoreCase(self, /) -> bool:
        r"""Retrieve state of ignore case flag.

        Sends `SCI_AUTOCGETIGNORECASE`."""
    def autoCImageScale(self, /) -> int:
        r"""Get the scale factor in percent for auto-completion list images.

        Sends `SCI_AUTOCGETIMAGESCALE`."""
    def autoCMaxHeight(self, /) -> int:
        r"""Set the maximum height, in rows, of auto-completion and user lists.

        Sends `SCI_AUTOCGETMAXHEIGHT`."""
    def autoCMaxWidth(self, /) -> int:
        r"""Get the maximum width, in characters, of auto-completion and user lists.

        Sends `SCI_AUTOCGETMAXWIDTH`."""
    def autoCMulti(self, /) -> int:
        r"""Retrieve the effect of autocompleting when there are multiple selections.

        Sends `SCI_AUTOCGETMULTI`."""
    def autoCOptions(self, /) -> int:
        r"""Retrieve autocompletion options.

        Sends `SCI_AUTOCGETOPTIONS`."""
    def autoCOrder(self, /) -> int:
        r"""Get the way autocompletion lists are ordered.

        Sends `SCI_AUTOCGETORDER`."""
    def autoCPosStart(self, /) -> int:
        r"""Retrieve the position of the caret when the auto-completion list was displayed.

        Sends `SCI_AUTOCPOSSTART`."""
    def autoCSelect(self, select: str, /) -> None:
        r"""Select the item in the auto-completion list that starts with a string.

        Sends `SCI_AUTOCSELECT`."""
    def autoCSeparator(self, /) -> int:
        r"""Retrieve the auto-completion list separator character.

        Sends `SCI_AUTOCGETSEPARATOR`."""
    def autoCSetAutoHide(self, autoHide: bool, /) -> None:
        r"""Set whether or not autocompletion is hidden automatically when nothing matches.

        Sends `SCI_AUTOCSETAUTOHIDE`."""
    def autoCSetCancelAtStart(self, cancel: bool, /) -> None:
        r"""Should the auto-completion list be cancelled if the user backspaces to a position before where the box was created.

        Sends `SCI_AUTOCSETCANCELATSTART`."""
    def autoCSetCaseInsensitiveBehaviour(self, behaviour: int, /) -> None:
        r"""Set auto-completion case insensitive behaviour to either prefer case-sensitive matches or have no preference.

        Sends `SCI_AUTOCSETCASEINSENSITIVEBEHAVIOUR`."""
    def autoCSetChooseSingle(self, chooseSingle: bool, /) -> None:
        r"""Should a single item auto-completion list automatically choose the item.

        Sends `SCI_AUTOCSETCHOOSESINGLE`."""
    def autoCSetDropRestOfWord(self, dropRestOfWord: bool, /) -> None:
        r"""Set whether or not autocompletion deletes any word characters after the inserted text upon completion.

        Sends `SCI_AUTOCSETDROPRESTOFWORD`."""
    def autoCSetFillUps(self, characterSet: str, /) -> None:
        r"""Define a set of characters that when typed will cause the autocompletion to choose the selected item.

        Sends `SCI_AUTOCSETFILLUPS`."""
    def autoCSetIgnoreCase(self, ignoreCase: bool, /) -> None:
        r"""Set whether case is significant when performing auto-completion searches.

        Sends `SCI_AUTOCSETIGNORECASE`."""
    def autoCSetImageScale(self, scalePercent: int, /) -> None:
        r"""Set the scale factor in percent for auto-completion list images.

        Sends `SCI_AUTOCSETIMAGESCALE`."""
    def autoCSetMaxHeight(self, rowCount: int, /) -> None:
        r"""Set the maximum height, in rows, of auto-completion and user lists. The default is 5 rows.

        Sends `SCI_AUTOCSETMAXHEIGHT`."""
    def autoCSetMaxWidth(self, characterCount: int, /) -> None:
        r"""Set the maximum width, in characters, of auto-completion and user lists. Set to 0 to autosize to fit longest item, which is the default.

        Sends `SCI_AUTOCSETMAXWIDTH`."""
    def autoCSetMulti(self, multi: int, /) -> None:
        r"""Change the effect of autocompleting when there are multiple selections.

        Sends `SCI_AUTOCSETMULTI`."""
    def autoCSetOptions(self, options: int, /) -> None:
        r"""Set autocompletion options.

        Sends `SCI_AUTOCSETOPTIONS`."""
    def autoCSetOrder(self, order: int, /) -> None:
        r"""Set the way autocompletion lists are ordered.

        Sends `SCI_AUTOCSETORDER`."""
    def autoCSetSeparator(self, separatorCharacter: int, /) -> None:
        r"""Change the separator character in the string setting up an auto-completion list. Default is space but can be changed if items contain space.

        Sends `SCI_AUTOCSETSEPARATOR`."""
    def autoCSetStyle(self, style: int, /) -> None:
        r"""Set the style number used for auto-completion and user lists fonts.

        Sends `SCI_AUTOCSETSTYLE`."""
    def autoCSetTypeSeparator(self, separatorCharacter: int, /) -> None:
        r"""Change the type-separator character in the string setting up an auto-completion list. Default is '?' but can be changed if items contain '?'.

        Sends `SCI_AUTOCSETTYPESEPARATOR`."""
    def autoCShow(self, lengthEntered: int, itemList: str, /) -> None:
        r"""Display a auto-completion list. The lengthEntered parameter indicates how many characters before the caret should be used to provide context.

        Sends `SCI_AUTOCSHOW`."""
    def autoCStops(self, characterSet: str, /) -> None:
        r"""Define a set of character that when typed cancel the auto-completion list.

        Sends `SCI_AUTOCSTOPS`."""
    def autoCStyle(self, /) -> int:
        r"""Get the style number used for auto-completion and user lists fonts.

        Sends `SCI_AUTOCGETSTYLE`."""
    def autoCTypeSeparator(self, /) -> int:
        r"""Retrieve the auto-completion list type-separator character.

        Sends `SCI_AUTOCGETTYPESEPARATOR`."""
    def automaticFold(self, /) -> int:
        r"""Get automatic folding behaviours.

        Sends `SCI_GETAUTOMATICFOLD`."""
    def backSpaceUnIndents(self, /) -> bool:
        r"""Does a backspace pressed when caret is within indentation unindent?

        Sends `SCI_GETBACKSPACEUNINDENTS`."""
    def backTab(self, /) -> None:
        r"""If selection is empty or all on one line dedent the line if caret is at start, else move caret. If more than one line selected, dedent the lines.

        Sends `SCI_BACKTAB`."""
    def beginUndoAction(self, /) -> None:
        r"""Start a sequence of actions that is undone and redone as a unit. May be nested.

        Sends `SCI_BEGINUNDOACTION`."""
    def bidirectional(self, /) -> int:
        r"""Retrieve bidirectional text display state.

        Sends `SCI_GETBIDIRECTIONAL`."""
    def braceBadLight(self, pos: int, /) -> None:
        r"""Highlight the character at a position indicating there is no matching brace.

        Sends `SCI_BRACEBADLIGHT`."""
    def braceBadLightIndicator(self, useSetting: bool, indicator: int, /) -> None:
        r"""Use specified indicator to highlight non matching brace instead of changing its style.

        Sends `SCI_BRACEBADLIGHTINDICATOR`."""
    def braceHighlight(self, posA: int, posB: int, /) -> None:
        r"""Highlight the characters at two positions.

        Sends `SCI_BRACEHIGHLIGHT`."""
    def braceHighlightIndicator(self, useSetting: bool, indicator: int, /) -> None:
        r"""Use specified indicator to highlight matching braces instead of changing their style.

        Sends `SCI_BRACEHIGHLIGHTINDICATOR`."""
    def braceMatch(self, pos: int, maxReStyle: int, /) -> int:
        r"""Find the position of a matching brace or INVALID_POSITION if no match. The maxReStyle must be 0 for now. It may be defined in a future release.

        Sends `SCI_BRACEMATCH`."""
    def braceMatchNext(self, pos: int, startPos: int, /) -> int:
        r"""Similar to BraceMatch, but matching starts at the explicit start position.

        Sends `SCI_BRACEMATCHNEXT`."""
    def bufferedDraw(self, /) -> bool:
        r"""Is drawing done first into a buffer or direct to the screen?

        Sends `SCI_GETBUFFEREDDRAW`."""
    def callTipActive(self, /) -> bool:
        r"""Is there an active call tip?

        Sends `SCI_CALLTIPACTIVE`."""
    def callTipCancel(self, /) -> None:
        r"""Remove the call tip from the screen.

        Sends `SCI_CALLTIPCANCEL`."""
    def callTipPosStart(self, /) -> int:
        r"""Retrieve the position where the caret was before displaying the call tip.

        Sends `SCI_CALLTIPPOSSTART`."""
    def callTipSetBack(self, back: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set the background colour for the call tip.

        Sends `SCI_CALLTIPSETBACK`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def callTipSetFore(self, fore: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set the foreground colour for the call tip.

        Sends `SCI_CALLTIPSETFORE`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def callTipSetForeHlt(self, fore: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set the foreground colour for the highlighted part of the call tip.

        Sends `SCI_CALLTIPSETFOREHLT`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def callTipSetHlt(self, highlightStart: int, highlightEnd: int, /) -> None:
        r"""Highlight a segment of the definition.

        Sends `SCI_CALLTIPSETHLT`."""
    def callTipSetPosStart(self, posStart: int, /) -> None:
        r"""Set the start position in order to change when backspacing removes the calltip.

        Sends `SCI_CALLTIPSETPOSSTART`."""
    def callTipSetPosition(self, above: bool, /) -> None:
        r"""Set position of calltip, above or below text.

        Sends `SCI_CALLTIPSETPOSITION`."""
    def callTipShow(self, pos: int, definition: str, /) -> None:
        r"""Show a call tip containing a definition near position pos.

        Sends `SCI_CALLTIPSHOW`."""
    def callTipUseStyle(self, tabSize: int, /) -> None:
        r"""Enable use of STYLE_CALLTIP and set call tip tab size in pixels.

        Sends `SCI_CALLTIPUSESTYLE`."""
    def canPaste(self, /) -> bool:
        r"""Will a paste succeed?

        Sends `SCI_CANPASTE`."""
    def canRedo(self, /) -> bool:
        r"""Are there any redoable actions in the undo history?

        Sends `SCI_CANREDO`."""
    def canUndo(self, /) -> bool:
        r"""Are there any undoable actions in the undo history?

        Sends `SCI_CANUNDO`."""
    def cancel(self, /) -> None:
        r"""Cancel any modes such as call tip or auto-completion list display.

        Sends `SCI_CANCEL`."""
    def caretFore(self, /) -> PySide6.QtGui.QColor:
        r"""Get the foreground colour of the caret.

        Sends `SCI_GETCARETFORE`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def caretLineBack(self, /) -> PySide6.QtGui.QColor:
        r"""Get the colour of the background of the line containing the caret.

        Sends `SCI_GETCARETLINEBACK`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def caretLineBackAlpha(self, /) -> int:
        r"""Get the background alpha of the caret line.

        Sends `SCI_GETCARETLINEBACKALPHA`."""
    def caretLineFrame(self, /) -> int:
        r"""Retrieve the caret line frame width. Width = 0 means this option is disabled.

        Sends `SCI_GETCARETLINEFRAME`."""
    def caretLineHighlightSubLine(self, /) -> bool:
        r"""Get only highlighting subline instead of whole line.

        Sends `SCI_GETCARETLINEHIGHLIGHTSUBLINE`."""
    def caretLineLayer(self, /) -> int:
        r"""Get the layer of the background of the line containing the caret.

        Sends `SCI_GETCARETLINELAYER`."""
    def caretLineVisible(self, /) -> bool:
        r"""Is the background of the line containing the caret in a different colour?

        Sends `SCI_GETCARETLINEVISIBLE`."""
    def caretLineVisibleAlways(self, /) -> bool:
        r"""Is the caret line always visible?

        Sends `SCI_GETCARETLINEVISIBLEALWAYS`."""
    def caretPeriod(self, /) -> int:
        r"""Get the time in milliseconds that the caret is on and off.

        Sends `SCI_GETCARETPERIOD`."""
    def caretSticky(self, /) -> int:
        r"""Can the caret preferred x position only be changed by explicit movement commands?

        Sends `SCI_GETCARETSTICKY`."""
    def caretStyle(self, /) -> int:
        r"""Returns the current style of the caret.

        Sends `SCI_GETCARETSTYLE`."""
    def caretWidth(self, /) -> int:
        r"""Returns the width of the insert mode caret.

        Sends `SCI_GETCARETWIDTH`."""
    def changeHistory(self, /) -> int:
        r"""Report change history status.

        Sends `SCI_GETCHANGEHISTORY`."""
    def changeInsertion(self, text: str, /) -> None:
        r"""Change the text that is being inserted in response to SC_MOD_INSERTCHECK

        Sends `SCI_CHANGEINSERTION`. No `length` argument: it's the byte length of the encoded `text`."""
    def changeLastUndoActionText(self, text: str, /) -> None:
        r"""Set the text and length of the most recently pushed action

        Sends `SCI_CHANGELASTUNDOACTIONTEXT`. No `length` argument: it's the byte length of the encoded `text`."""
    def changeLexerState(self, start: int, end: int, /) -> int:
        r"""Indicate that the internal state of a lexer has changed over a range and therefore there may be a need to redraw.

        Sends `SCI_CHANGELEXERSTATE`."""
    def changeSelectionMode(self, selectionMode: int, /) -> None:
        r"""Set the selection mode to stream (SC_SEL_STREAM) or rectangular (SC_SEL_RECTANGLE/SC_SEL_THIN) or by lines (SC_SEL_LINES) without changing MoveExtendsSelection.

        Sends `SCI_CHANGESELECTIONMODE`."""
    def charAt(self, pos: int, /) -> int:
        r"""Returns the character byte at the position.

        Sends `SCI_GETCHARAT`."""
    def charLeft(self, /) -> None:
        r"""Move caret left one character.

        Sends `SCI_CHARLEFT`."""
    def charLeftExtend(self, /) -> None:
        r"""Move caret left one character extending selection to new caret position.

        Sends `SCI_CHARLEFTEXTEND`."""
    def charLeftRectExtend(self, /) -> None:
        r"""Move caret left one character, extending rectangular selection to new caret position.

        Sends `SCI_CHARLEFTRECTEXTEND`."""
    def charPositionFromPoint(self, x: int, y: int, /) -> int:
        r"""Find the position of a character from a point within the window.

        Sends `SCI_CHARPOSITIONFROMPOINT`."""
    def charPositionFromPointClose(self, x: int, y: int, /) -> int:
        r"""Find the position of a character from a point within the window. Return INVALID_POSITION if not close to text.

        Sends `SCI_CHARPOSITIONFROMPOINTCLOSE`."""
    def charRight(self, /) -> None:
        r"""Move caret right one character.

        Sends `SCI_CHARRIGHT`."""
    def charRightExtend(self, /) -> None:
        r"""Move caret right one character extending selection to new caret position.

        Sends `SCI_CHARRIGHTEXTEND`."""
    def charRightRectExtend(self, /) -> None:
        r"""Move caret right one character, extending rectangular selection to new caret position.

        Sends `SCI_CHARRIGHTRECTEXTEND`."""
    def characterCategoryOptimization(self, /) -> int:
        r"""Get the number of characters to have directly indexed categories

        Sends `SCI_GETCHARACTERCATEGORYOPTIMIZATION`."""
    def characterPointer(self, /) -> int:
        r"""Compact the document buffer and return a read-only pointer to the characters in the document.

        Sends `SCI_GETCHARACTERPOINTER`."""
    def chooseCaretX(self, /) -> None:
        r"""Set the last x chosen value to be the caret x position.

        Sends `SCI_CHOOSECARETX`."""
    def clear(self, /) -> None:
        r"""Clear the selection.

        Sends `SCI_CLEAR`."""
    def clearAll(self, /) -> None:
        r"""Delete all text in the document.

        Sends `SCI_CLEARALL`."""
    def clearAllCmdKeys(self, /) -> None:
        r"""Drop all key mappings.

        Sends `SCI_CLEARALLCMDKEYS`."""
    def clearAllRepresentations(self, /) -> None:
        r"""Clear representations to default.

        Sends `SCI_CLEARALLREPRESENTATIONS`."""
    def clearCmdKey(self, keyDefinition: int, /) -> None:
        r"""When key+modifier combination keyDefinition is pressed do nothing.

        Sends `SCI_CLEARCMDKEY`."""
    def clearDocumentStyle(self, /) -> None:
        r"""Set all style bytes to 0, remove all folding information.

        Sends `SCI_CLEARDOCUMENTSTYLE`."""
    def clearRegisteredImages(self, /) -> None:
        r"""Clear all the registered XPM images.

        Sends `SCI_CLEARREGISTEREDIMAGES`."""
    def clearRepresentation(self, encodedCharacter: str, /) -> None:
        r"""Remove a character representation.

        Sends `SCI_CLEARREPRESENTATION`."""
    def clearSelections(self, /) -> None:
        r"""Clear selections to a single empty stream selection

        Sends `SCI_CLEARSELECTIONS`."""
    def clearTabStops(self, line: int, /) -> None:
        r"""Clear explicit tabstops on a line.

        Sends `SCI_CLEARTABSTOPS`."""
    def codePage(self, /) -> int:
        r"""Get the code page used to interpret the bytes of the document as characters.

        Sends `SCI_GETCODEPAGE`."""
    def colourise(self, start: int, end: int, /) -> None:
        r"""Colourise a segment of the document using the current lexing language.

        Sends `SCI_COLOURISE`."""
    def column(self, pos: int, /) -> int:
        r"""Retrieve the column number of a position, taking tab width into account.

        Sends `SCI_GETCOLUMN`."""
    def commandEvents(self, /) -> bool:
        r"""Get whether command events are sent to the container.

        Sends `SCI_GETCOMMANDEVENTS`."""
    def contractedFoldNext(self, lineStart: int, /) -> int:
        r"""Find the next line at or after lineStart that is a contracted fold header line. Return -1 when no more lines.

        Sends `SCI_CONTRACTEDFOLDNEXT`."""
    def controlCharSymbol(self, /) -> int:
        r"""Get the way control characters are displayed.

        Sends `SCI_GETCONTROLCHARSYMBOL`."""
    def convertEOLs(self, eolMode: int, /) -> None:
        r"""Convert all line endings in the document to one mode.

        Sends `SCI_CONVERTEOLS`."""
    def copy(self, /) -> None:
        r"""Copy the selection to the clipboard.

        Sends `SCI_COPY`."""
    def copyAllowLine(self, /) -> None:
        r"""Copy the selection, if selection empty copy the line with the caret

        Sends `SCI_COPYALLOWLINE`."""
    def copyRange(self, start: int, end: int, /) -> None:
        r"""Copy a range of text to the clipboard. Positions are clipped into the document.

        Sends `SCI_COPYRANGE`."""
    def copySeparator(self, /) -> str:
        r"""Get the string to separate parts when copying a multiple selection.

        Sends `SCI_GETCOPYSEPARATOR`. Returns the result instead of filling a `separator` buffer; the message's own result (the length) is dropped."""
    def copyText(self, text: str, /) -> None:
        r"""Copy argument text to the clipboard.

        Sends `SCI_COPYTEXT`. No `length` argument: it's the byte length of the encoded `text`."""
    def countCharacters(self, start: int, end: int, /) -> int:
        r"""Count characters between two positions.

        Sends `SCI_COUNTCHARACTERS`."""
    def countCodeUnits(self, start: int, end: int, /) -> int:
        r"""Count code units between two positions.

        Sends `SCI_COUNTCODEUNITS`."""
    def createDocument(self, bytes: int, documentOptions: int, /) -> int:
        r"""Create a new document object. Starts with reference count of 1 and not selected into editor.

        Sends `SCI_CREATEDOCUMENT`."""
    def createLoader(self, bytes: int, documentOptions: int, /) -> int:
        r"""Create an ILoader*.

        Sends `SCI_CREATELOADER`."""
    def currentPos(self, /) -> int:
        r"""Returns the position of the caret.

        Sends `SCI_GETCURRENTPOS`."""
    def cursor(self, /) -> int:
        r"""Get cursor type.

        Sends `SCI_GETCURSOR`."""
    def cut(self, /) -> None:
        r"""Cut the selection to the clipboard.

        Sends `SCI_CUT`."""
    def cutAllowLine(self, /) -> None:
        r"""Cut the selection, if selection empty cut the line with the caret

        Sends `SCI_CUTALLOWLINE`."""
    def delLineLeft(self, /) -> None:
        r"""Delete back from the current position to the start of the line.

        Sends `SCI_DELLINELEFT`."""
    def delLineRight(self, /) -> None:
        r"""Delete forwards from the current position to the end of the line.

        Sends `SCI_DELLINERIGHT`."""
    def delWordLeft(self, /) -> None:
        r"""Delete the word to the left of the caret.

        Sends `SCI_DELWORDLEFT`."""
    def delWordRight(self, /) -> None:
        r"""Delete the word to the right of the caret.

        Sends `SCI_DELWORDRIGHT`."""
    def delWordRightEnd(self, /) -> None:
        r"""Delete the word to the right of the caret, but not the trailing non-word characters.

        Sends `SCI_DELWORDRIGHTEND`."""
    def deleteBack(self, /) -> None:
        r"""Delete the selection or if no selection, the character before the caret.

        Sends `SCI_DELETEBACK`."""
    def deleteBackNotLine(self, /) -> None:
        r"""Delete the selection or if no selection, the character before the caret. Will not delete the character before at the start of a line.

        Sends `SCI_DELETEBACKNOTLINE`."""
    def deleteRange(self, start: int, lengthDelete: int, /) -> None:
        r"""Delete a range of text in the document.

        Sends `SCI_DELETERANGE`."""
    def describeKeyWordSets(self, /) -> str:
        r"""Retrieve a '\n' separated list of descriptions of the keyword sets understood by the current lexer. Result is NUL-terminated.

        Sends `SCI_DESCRIBEKEYWORDSETS`. Returns the result instead of filling a `descriptions` buffer; the message's own result (the length) is dropped."""
    def describeProperty(self, name: str, /) -> str:
        r"""Describe a property. Result is NUL-terminated.

        Sends `SCI_DESCRIBEPROPERTY`. Returns the result instead of filling a `description` buffer; the message's own result (the length) is dropped."""
    def descriptionOfStyle(self, style: int, /) -> str:
        r"""Retrieve a description of a style. Result is NUL-terminated.

        Sends `SCI_DESCRIPTIONOFSTYLE`. Returns the result instead of filling a `description` buffer; the message's own result (the length) is dropped."""
    def directFunction(self, /) -> int:
        r"""Retrieve a pointer to a function that processes messages for this Scintilla.

        Sends `SCI_GETDIRECTFUNCTION`."""
    def directPointer(self, /) -> int:
        r"""Retrieve a pointer value to use as the first argument when calling the function returned by GetDirectFunction.

        Sends `SCI_GETDIRECTPOINTER`."""
    def directStatusFunction(self, /) -> int:
        r"""Retrieve a pointer to a function that processes messages for this Scintilla and returns status.

        Sends `SCI_GETDIRECTSTATUSFUNCTION`."""
    def distanceToSecondaryStyles(self, /) -> int:
        r"""Where styles are duplicated by a feature such as active/inactive code return the distance between the two types.

        Sends `SCI_DISTANCETOSECONDARYSTYLES`."""
    def docLineFromVisible(self, displayLine: int, /) -> int:
        r"""Find the document line of a display line taking hidden lines into account.

        Sends `SCI_DOCLINEFROMVISIBLE`."""
    def docPointer(self, /) -> int:
        r"""Retrieve a pointer to the document object.

        Sends `SCI_GETDOCPOINTER`."""
    def documentEnd(self, /) -> None:
        r"""Move caret to last position in document.

        Sends `SCI_DOCUMENTEND`."""
    def documentEndExtend(self, /) -> None:
        r"""Move caret to last position in document extending selection to new caret position.

        Sends `SCI_DOCUMENTENDEXTEND`."""
    def documentOptions(self, /) -> int:
        r"""Get which document options are set.

        Sends `SCI_GETDOCUMENTOPTIONS`."""
    def documentStart(self, /) -> None:
        r"""Move caret to first position in document.

        Sends `SCI_DOCUMENTSTART`."""
    def documentStartExtend(self, /) -> None:
        r"""Move caret to first position in document extending selection to new caret position.

        Sends `SCI_DOCUMENTSTARTEXTEND`."""
    def dragDropEnabled(self, /) -> bool:
        r"""Get whether drag-and-drop is enabled or disabled

        Sends `SCI_GETDRAGDROPENABLED`."""
    def dropSelectionN(self, selection: int, /) -> None:
        r"""Drop one selection

        Sends `SCI_DROPSELECTIONN`."""
    def eOLAnnotationClearAll(self, /) -> None:
        r"""Clear the end of annotations from all lines

        Sends `SCI_EOLANNOTATIONCLEARALL`."""
    def eOLAnnotationSetStyle(self, line: int, style: int, /) -> None:
        r"""Set the style number for the end of line annotations for a line

        Sends `SCI_EOLANNOTATIONSETSTYLE`."""
    def eOLAnnotationSetStyleOffset(self, style: int, /) -> None:
        r"""Get the start of the range of style numbers used for end of line annotations

        Sends `SCI_EOLANNOTATIONSETSTYLEOFFSET`."""
    def eOLAnnotationSetText(self, line: int, text: str, /) -> None:
        r"""Set the end of line annotation text for a line

        Sends `SCI_EOLANNOTATIONSETTEXT`."""
    def eOLAnnotationSetVisible(self, visible: int, /) -> None:
        r"""Set the visibility for the end of line annotations for a view

        Sends `SCI_EOLANNOTATIONSETVISIBLE`."""
    def eOLAnnotationStyle(self, line: int, /) -> int:
        r"""Get the style number for the end of line annotations for a line

        Sends `SCI_EOLANNOTATIONGETSTYLE`."""
    def eOLAnnotationStyleOffset(self, /) -> int:
        r"""Get the start of the range of style numbers used for end of line annotations

        Sends `SCI_EOLANNOTATIONGETSTYLEOFFSET`."""
    def eOLAnnotationText(self, line: int, /) -> str:
        r"""Get the end of line annotation text for a line

        Sends `SCI_EOLANNOTATIONGETTEXT`. Returns the result instead of filling a `text` buffer; the message's own result (the length) is dropped."""
    def eOLAnnotationVisible(self, /) -> int:
        r"""Get the visibility for the end of line annotations for a view

        Sends `SCI_EOLANNOTATIONGETVISIBLE`."""
    def eOLMode(self, /) -> int:
        r"""Retrieve the current end of line mode - one of CRLF, CR, or LF.

        Sends `SCI_GETEOLMODE`."""
    def edgeColour(self, /) -> PySide6.QtGui.QColor:
        r"""Retrieve the colour used in edge indication.

        Sends `SCI_GETEDGECOLOUR`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def edgeColumn(self, /) -> int:
        r"""Retrieve the column number which text should be kept within.

        Sends `SCI_GETEDGECOLUMN`."""
    def edgeMode(self, /) -> int:
        r"""Retrieve the edge highlight mode.

        Sends `SCI_GETEDGEMODE`."""
    def editToggleOvertype(self, /) -> None:
        r"""Switch from insert to overtype mode or the reverse.

        Sends `SCI_EDITTOGGLEOVERTYPE`."""
    def elementAllowsTranslucent(self, element: int, /) -> bool:
        r"""Get whether an element supports translucency.

        Sends `SCI_GETELEMENTALLOWSTRANSLUCENT`."""
    def elementBaseColour(self, element: int, /) -> PySide6.QtGui.QColor:
        r"""Get the colour of an element.

        Sends `SCI_GETELEMENTBASECOLOUR`. Uses a `QColor` (with alpha) where the message uses a packed `0xAABBGGRR` int. The message's 0 result for an unset value is `QColor(0, 0, 0, 0)`, transparent black."""
    def elementColour(self, element: int, /) -> PySide6.QtGui.QColor:
        r"""Get the colour of an element.

        Sends `SCI_GETELEMENTCOLOUR`. Uses a `QColor` (with alpha) where the message uses a packed `0xAABBGGRR` int. The message's 0 result for an unset value is `QColor(0, 0, 0, 0)`, transparent black."""
    def elementIsSet(self, element: int, /) -> bool:
        r"""Get whether an element has been set by SetElementColour. When false, a platform-defined or default colour is used.

        Sends `SCI_GETELEMENTISSET`."""
    def emptyUndoBuffer(self, /) -> None:
        r"""Delete the undo history.

        Sends `SCI_EMPTYUNDOBUFFER`."""
    def endAtLastLine(self, /) -> bool:
        r"""Retrieve whether the maximum scroll position has the last line at the bottom of the view.

        Sends `SCI_GETENDATLASTLINE`."""
    def endStyled(self, /) -> int:
        r"""Retrieve the position of the last correctly styled character.

        Sends `SCI_GETENDSTYLED`."""
    def endUndoAction(self, /) -> None:
        r"""End a sequence of actions that is undone and redone as a unit.

        Sends `SCI_ENDUNDOACTION`."""
    def ensureVisible(self, line: int, /) -> None:
        r"""Ensure a particular line is visible by expanding any header line hiding it.

        Sends `SCI_ENSUREVISIBLE`."""
    def ensureVisibleEnforcePolicy(self, line: int, /) -> None:
        r"""Ensure a particular line is visible by expanding any header line hiding it. Use the currently set visibility policy to determine which range to display.

        Sends `SCI_ENSUREVISIBLEENFORCEPOLICY`."""
    def expandChildren(self, line: int, level: int, /) -> None:
        r"""Expand a fold header and all children. Use the level argument instead of the line's current level.

        Sends `SCI_EXPANDCHILDREN`."""
    def extraAscent(self, /) -> int:
        r"""Get extra ascent for each line

        Sends `SCI_GETEXTRAASCENT`."""
    def extraDescent(self, /) -> int:
        r"""Get extra descent for each line

        Sends `SCI_GETEXTRADESCENT`."""
    def findColumn(self, line: int, column: int, /) -> int:
        r"""Find the position of a column on a line taking into account tabs and multi-byte characters. If beyond end of line, return line end position.

        Sends `SCI_FINDCOLUMN`."""
    def findIndicatorFlash(self, start: int, end: int, /) -> None:
        r"""On macOS, flash a find indicator, then fade out.

        Sends `SCI_FINDINDICATORFLASH`."""
    def findIndicatorHide(self, /) -> None:
        r"""On macOS, hide the find indicator.

        Sends `SCI_FINDINDICATORHIDE`."""
    def findIndicatorShow(self, start: int, end: int, /) -> None:
        r"""On macOS, show a find indicator.

        Sends `SCI_FINDINDICATORSHOW`."""
    def findText(self, flags: int, text: str, cpMin: int, cpMax: int, /) -> typing.Tuple[int, int]:
        r"""Alias for `find_text`."""
    def find_text(self, flags: int, text: str, cpMin: int, cpMax: int, /) -> typing.Tuple[int, int]:
        r"""Search for `text` between byte positions `cpMin` and `cpMax` using `flags` (`Scintilla.FindOption` values).

        Returns the `(start, end)` byte positions of the match, or `(-1, cpMax)` if not found."""
    def firstVisibleLine(self, /) -> int:
        r"""Retrieve the display line at the top of the display.

        Sends `SCI_GETFIRSTVISIBLELINE`."""
    def focus(self, /) -> bool:
        r"""Get internal focus flag.

        Sends `SCI_GETFOCUS`."""
    def foldAll(self, action: int, /) -> None:
        r"""Expand or contract all fold headers.

        Sends `SCI_FOLDALL`."""
    def foldChildren(self, line: int, action: int, /) -> None:
        r"""Expand or contract a fold header and its children.

        Sends `SCI_FOLDCHILDREN`."""
    def foldDisplayTextSetStyle(self, style: int, /) -> None:
        r"""Set the style of fold display text.

        Sends `SCI_FOLDDISPLAYTEXTSETSTYLE`."""
    def foldDisplayTextStyle(self, /) -> int:
        r"""Get the style of fold display text.

        Sends `SCI_FOLDDISPLAYTEXTGETSTYLE`."""
    def foldExpanded(self, line: int, /) -> bool:
        r"""Is a header line expanded?

        Sends `SCI_GETFOLDEXPANDED`."""
    def foldLevel(self, line: int, /) -> int:
        r"""Retrieve the fold level of a line.

        Sends `SCI_GETFOLDLEVEL`."""
    def foldLine(self, line: int, action: int, /) -> None:
        r"""Expand or contract a fold header.

        Sends `SCI_FOLDLINE`."""
    def foldParent(self, line: int, /) -> int:
        r"""Find the parent line of a child line.

        Sends `SCI_GETFOLDPARENT`."""
    def fontLocale(self, /) -> str:
        r"""Get the locale for displaying text.

        Sends `SCI_GETFONTLOCALE`. Returns the result instead of filling a `localeName` buffer; the message's own result (the length) is dropped."""
    def fontQuality(self, /) -> int:
        r"""Retrieve the quality level for text.

        Sends `SCI_GETFONTQUALITY`."""
    def formFeed(self, /) -> None:
        r"""Insert a Form Feed character.

        Sends `SCI_FORMFEED`."""
    def formatRange(self, draw: bool, target: PySide6.QtGui.QPaintDevice, measure: PySide6.QtGui.QPaintDevice, print_rect: PySide6.QtCore.QRect, page_rect: PySide6.QtCore.QRect, range_start: int, range_end: int, /) -> int:
        r"""Alias for `format_range`."""
    def format_range(self, draw: bool, target: PySide6.QtGui.QPaintDevice, measure: PySide6.QtGui.QPaintDevice, print_rect: PySide6.QtCore.QRect, page_rect: PySide6.QtCore.QRect, range_start: int, range_end: int, /) -> int:
        r"""Render the document between `range_start` and `range_end` for printing.

        Draws onto `target` (and lays out using `measure`) within `print_rect`/`page_rect`. If `draw` is false, only measures. Returns the position after the last formatted character."""
    def freeSubStyles(self, /) -> None:
        r"""Free allocated sub styles

        Sends `SCI_FREESUBSTYLES`."""
    def gapPosition(self, /) -> int:
        r"""Return a position which, to avoid performance costs, should not be within the range of a call to GetRangePointer.

        Sends `SCI_GETGAPPOSITION`."""
    @typing.overload
    def getBytes(self, /) -> PySide6.QtCore.QByteArray:
        r"""Return the document (or the byte range `start`..`end`) as stored: its bytes in the document's encoding, not decoded.

        The bytes counterpart of `getText()`/`textRange()`: use it where byte offsets matter (e.g. feeding a parser whose positions must match Scintilla's), instead of decoding to `str` and encoding back. `.data()` gives a Python `bytes`."""
    @typing.overload
    def getBytes(self, start: int, end: int, /) -> PySide6.QtCore.QByteArray:
        r"""Return the document (or the byte range `start`..`end`) as stored: its bytes in the document's encoding, not decoded.

        The bytes counterpart of `getText()`/`textRange()`: use it where byte offsets matter (e.g. feeding a parser whose positions must match Scintilla's), instead of decoding to `str` and encoding back. `.data()` gives a Python `bytes`."""
    def getCurLine(self, /) -> typing.Tuple[str, int]:
        r"""Retrieve the text of the line containing the caret. Returns the index of the caret on the line. Result is NUL-terminated.

        Sends `SCI_GETCURLINE`. Returns the result instead of filling a `text` buffer, so there's no `length` buffer-size argument; returns `(text, caret)`, the caret's byte offset in the line being the message's result."""
    def getDefaultFoldDisplayText(self, /) -> str:
        r"""Get the default fold display text.

        Sends `SCI_GETDEFAULTFOLDDISPLAYTEXT`. Returns the result instead of filling a `text` buffer; the message's own result (the length) is dropped."""
    def getLine(self, line: int, /) -> str:
        r"""Retrieve the contents of a line. Returns the length of the line.

        Sends `SCI_GETLINE`. Returns the result instead of filling a `text` buffer; the message's own result (the length) is dropped."""
    def getLineSelEndPosition(self, line: int, /) -> int:
        r"""Retrieve the position of the end of the selection at the given line (INVALID_POSITION if no selection on this line).

        Sends `SCI_GETLINESELENDPOSITION`."""
    def getLineSelStartPosition(self, line: int, /) -> int:
        r"""Retrieve the position of the start of the selection at the given line (INVALID_POSITION if no selection on this line).

        Sends `SCI_GETLINESELSTARTPOSITION`."""
    def getNextTabStop(self, line: int, x: int, /) -> int:
        r"""Find the next explicit tab stop position on a line after a position.

        Sends `SCI_GETNEXTTABSTOP`."""
    def getSelText(self, /) -> str:
        r"""Retrieve the selected text. Return the length of the text. Result is NUL-terminated.

        Sends `SCI_GETSELTEXT`. Returns the result instead of filling a `text` buffer; the message's own result (the length) is dropped."""
    def getText(self, /) -> str:
        r"""Retrieve all the text in the document. Returns number of characters retrieved. Result is NUL-terminated.

        Sends `SCI_GETTEXT`. Returns the result instead of filling a `text` buffer, so there's no `length` buffer-size argument; the message's own result (the length) is dropped."""
    def get_text_range(self, start: int, end: int, /) -> str:
        r"""Return the document's text between byte positions `start` and `end`."""
    def gotoLine(self, line: int, /) -> None:
        r"""Set caret to start of a line and ensure it is visible.

        Sends `SCI_GOTOLINE`."""
    def gotoPos(self, caret: int, /) -> None:
        r"""Set caret to a position and ensure it is visible.

        Sends `SCI_GOTOPOS`."""
    def grabFocus(self, /) -> None:
        r"""Set the focus to this Scintilla widget.

        Sends `SCI_GRABFOCUS`."""
    def hScrollBar(self, /) -> bool:
        r"""Is the horizontal scroll bar visible?

        Sends `SCI_GETHSCROLLBAR`."""
    def hideLines(self, lineStart: int, lineEnd: int, /) -> None:
        r"""Make a range of lines invisible.

        Sends `SCI_HIDELINES`."""
    def hideSelection(self, hide: bool, /) -> None:
        r"""Draw the selection either highlighted or in normal (non-highlighted) style.

        Sends `SCI_HIDESELECTION`."""
    def highlightGuide(self, /) -> int:
        r"""Get the highlighted indentation guide column.

        Sends `SCI_GETHIGHLIGHTGUIDE`."""
    def home(self, /) -> None:
        r"""Move caret to first position on line.

        Sends `SCI_HOME`."""
    def homeDisplay(self, /) -> None:
        r"""Move caret to first position on display line.

        Sends `SCI_HOMEDISPLAY`."""
    def homeDisplayExtend(self, /) -> None:
        r"""Move caret to first position on display line extending selection to new caret position.

        Sends `SCI_HOMEDISPLAYEXTEND`."""
    def homeExtend(self, /) -> None:
        r"""Move caret to first position on line extending selection to new caret position.

        Sends `SCI_HOMEEXTEND`."""
    def homeRectExtend(self, /) -> None:
        r"""Move caret to first position on line, extending rectangular selection to new caret position.

        Sends `SCI_HOMERECTEXTEND`."""
    def homeWrap(self, /) -> None:
        r"""Like Home but when word-wrap is enabled goes first to start of display line HomeDisplay, then to start of document line Home.

        Sends `SCI_HOMEWRAP`."""
    def homeWrapExtend(self, /) -> None:
        r"""Like HomeExtend but when word-wrap is enabled extends first to start of display line HomeDisplayExtend, then to start of document line HomeExtend.

        Sends `SCI_HOMEWRAPEXTEND`."""
    def hotspotActiveBack(self, /) -> PySide6.QtGui.QColor:
        r"""Get the back colour for active hotspots.

        Sends `SCI_GETHOTSPOTACTIVEBACK`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def hotspotActiveFore(self, /) -> PySide6.QtGui.QColor:
        r"""Get the fore colour for active hotspots.

        Sends `SCI_GETHOTSPOTACTIVEFORE`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def hotspotActiveUnderline(self, /) -> bool:
        r"""Get whether underlining for active hotspots.

        Sends `SCI_GETHOTSPOTACTIVEUNDERLINE`."""
    def hotspotSingleLine(self, /) -> bool:
        r"""Get the HotspotSingleLine property

        Sends `SCI_GETHOTSPOTSINGLELINE`."""
    def iMEInteraction(self, /) -> int:
        r"""Is the IME displayed in a window or inline?

        Sends `SCI_GETIMEINTERACTION`."""
    def identifier(self, /) -> int:
        r"""Get the identifier.

        Sends `SCI_GETIDENTIFIER`."""
    def idleStyling(self, /) -> int:
        r"""Retrieve the limits to idle styling.

        Sends `SCI_GETIDLESTYLING`."""
    def indent(self, /) -> int:
        r"""Retrieve indentation size.

        Sends `SCI_GETINDENT`."""
    def indentationGuides(self, /) -> int:
        r"""Are the indentation guides visible?

        Sends `SCI_GETINDENTATIONGUIDES`."""
    def indexPositionFromLine(self, line: int, lineCharacterIndex: int, /) -> int:
        r"""Retrieve the position measured in index units at the start of a document line.

        Sends `SCI_INDEXPOSITIONFROMLINE`."""
    def indicAlpha(self, indicator: int, /) -> int:
        r"""Get the alpha fill colour of the given indicator.

        Sends `SCI_INDICGETALPHA`."""
    def indicFlags(self, indicator: int, /) -> int:
        r"""Retrieve the attributes of an indicator.

        Sends `SCI_INDICGETFLAGS`."""
    def indicFore(self, indicator: int, /) -> PySide6.QtGui.QColor:
        r"""Retrieve the foreground colour of an indicator.

        Sends `SCI_INDICGETFORE`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def indicHoverFore(self, indicator: int, /) -> PySide6.QtGui.QColor:
        r"""Retrieve the foreground hover colour of an indicator.

        Sends `SCI_INDICGETHOVERFORE`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def indicHoverStyle(self, indicator: int, /) -> int:
        r"""Retrieve the hover style of an indicator.

        Sends `SCI_INDICGETHOVERSTYLE`."""
    def indicOutlineAlpha(self, indicator: int, /) -> int:
        r"""Get the alpha outline colour of the given indicator.

        Sends `SCI_INDICGETOUTLINEALPHA`."""
    def indicSetAlpha(self, indicator: int, alpha: int, /) -> None:
        r"""Set the alpha fill colour of the given indicator.

        Sends `SCI_INDICSETALPHA`."""
    def indicSetFlags(self, indicator: int, flags: int, /) -> None:
        r"""Set the attributes of an indicator.

        Sends `SCI_INDICSETFLAGS`."""
    def indicSetFore(self, indicator: int, fore: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set the foreground colour of an indicator.

        Sends `SCI_INDICSETFORE`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def indicSetHoverFore(self, indicator: int, fore: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set the foreground hover colour of an indicator.

        Sends `SCI_INDICSETHOVERFORE`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def indicSetHoverStyle(self, indicator: int, indicatorStyle: int, /) -> None:
        r"""Set a hover indicator to plain, squiggle or TT.

        Sends `SCI_INDICSETHOVERSTYLE`."""
    def indicSetOutlineAlpha(self, indicator: int, alpha: int, /) -> None:
        r"""Set the alpha outline colour of the given indicator.

        Sends `SCI_INDICSETOUTLINEALPHA`."""
    def indicSetStrokeWidth(self, indicator: int, hundredths: int, /) -> None:
        r"""Set the stroke width of an indicator in hundredths of a pixel.

        Sends `SCI_INDICSETSTROKEWIDTH`."""
    def indicSetStyle(self, indicator: int, indicatorStyle: int, /) -> None:
        r"""Set an indicator to plain, squiggle or TT.

        Sends `SCI_INDICSETSTYLE`."""
    def indicSetUnder(self, indicator: int, under: bool, /) -> None:
        r"""Set an indicator to draw under text or over(default).

        Sends `SCI_INDICSETUNDER`."""
    def indicStrokeWidth(self, indicator: int, /) -> int:
        r"""Retrieve the stroke width of an indicator.

        Sends `SCI_INDICGETSTROKEWIDTH`."""
    def indicStyle(self, indicator: int, /) -> int:
        r"""Retrieve the style of an indicator.

        Sends `SCI_INDICGETSTYLE`."""
    def indicUnder(self, indicator: int, /) -> bool:
        r"""Retrieve whether indicator drawn under or over text.

        Sends `SCI_INDICGETUNDER`."""
    def indicatorAllOnFor(self, pos: int, /) -> int:
        r"""Are any indicators present at pos?

        Sends `SCI_INDICATORALLONFOR`."""
    def indicatorClearRange(self, start: int, lengthClear: int, /) -> None:
        r"""Turn a indicator off over a range.

        Sends `SCI_INDICATORCLEARRANGE`."""
    def indicatorCurrent(self, /) -> int:
        r"""Get the current indicator

        Sends `SCI_GETINDICATORCURRENT`."""
    def indicatorEnd(self, indicator: int, pos: int, /) -> int:
        r"""Where does a particular indicator end?

        Sends `SCI_INDICATOREND`."""
    def indicatorFillRange(self, start: int, lengthFill: int, /) -> None:
        r"""Turn a indicator on over a range.

        Sends `SCI_INDICATORFILLRANGE`."""
    def indicatorStart(self, indicator: int, pos: int, /) -> int:
        r"""Where does a particular indicator start?

        Sends `SCI_INDICATORSTART`."""
    def indicatorValue(self, /) -> int:
        r"""Get the current indicator value

        Sends `SCI_GETINDICATORVALUE`."""
    def indicatorValueAt(self, indicator: int, pos: int, /) -> int:
        r"""What value does a particular indicator have at a position?

        Sends `SCI_INDICATORVALUEAT`."""
    def insertText(self, pos: int, text: str, /) -> None:
        r"""Insert string at a position.

        Sends `SCI_INSERTTEXT`. Unlike the message (a NUL-terminated string), keeps embedded NUL characters: text containing one is inserted with `SCI_ADDTEXT` and an explicit length instead."""
    def isRangeWord(self, start: int, end: int, /) -> bool:
        r"""Is the range start..end considered a word?

        Sends `SCI_ISRANGEWORD`."""
    def lastChild(self, line: int, level: int, /) -> int:
        r"""Find the last child line of a header line.

        Sends `SCI_GETLASTCHILD`."""
    def layoutCache(self, /) -> int:
        r"""Retrieve the degree of caching of layout information.

        Sends `SCI_GETLAYOUTCACHE`."""
    def layoutThreads(self, /) -> int:
        r"""Get maximum number of threads used for layout

        Sends `SCI_GETLAYOUTTHREADS`."""
    def length(self, /) -> int:
        r"""Returns the number of bytes in the document.

        Sends `SCI_GETLENGTH`."""
    def lexer(self, /) -> int:
        r"""Retrieve the lexing language of the document.

        Sends `SCI_GETLEXER`."""
    def lexerLanguage(self, /) -> str:
        r"""Retrieve the name of the lexer. Return the length of the text. Result is NUL-terminated.

        Sends `SCI_GETLEXERLANGUAGE`. Returns the result instead of filling a `language` buffer; the message's own result (the length) is dropped."""
    def lineCharacterIndex(self, /) -> int:
        r"""Retrieve line character index state.

        Sends `SCI_GETLINECHARACTERINDEX`."""
    def lineCopy(self, /) -> None:
        r"""Copy the line containing the caret.

        Sends `SCI_LINECOPY`."""
    def lineCount(self, /) -> int:
        r"""Returns the number of lines in the document. There is always at least one.

        Sends `SCI_GETLINECOUNT`."""
    def lineCut(self, /) -> None:
        r"""Cut the line containing the caret.

        Sends `SCI_LINECUT`."""
    def lineDedent(self, /) -> None:
        r"""Dedent the current and selected lines.

        Sends `SCI_LINEDEDENT`."""
    def lineDelete(self, /) -> None:
        r"""Delete the line containing the caret.

        Sends `SCI_LINEDELETE`."""
    def lineDown(self, /) -> None:
        r"""Move caret down one line.

        Sends `SCI_LINEDOWN`."""
    def lineDownExtend(self, /) -> None:
        r"""Move caret down one line extending selection to new caret position.

        Sends `SCI_LINEDOWNEXTEND`."""
    def lineDownRectExtend(self, /) -> None:
        r"""Move caret down one line, extending rectangular selection to new caret position.

        Sends `SCI_LINEDOWNRECTEXTEND`."""
    def lineDuplicate(self, /) -> None:
        r"""Duplicate the current line.

        Sends `SCI_LINEDUPLICATE`."""
    def lineEnd(self, /) -> None:
        r"""Move caret to last position on line.

        Sends `SCI_LINEEND`."""
    def lineEndDisplay(self, /) -> None:
        r"""Move caret to last position on display line.

        Sends `SCI_LINEENDDISPLAY`."""
    def lineEndDisplayExtend(self, /) -> None:
        r"""Move caret to last position on display line extending selection to new caret position.

        Sends `SCI_LINEENDDISPLAYEXTEND`."""
    def lineEndExtend(self, /) -> None:
        r"""Move caret to last position on line extending selection to new caret position.

        Sends `SCI_LINEENDEXTEND`."""
    def lineEndPosition(self, line: int, /) -> int:
        r"""Get the position after the last visible characters on a line.

        Sends `SCI_GETLINEENDPOSITION`."""
    def lineEndRectExtend(self, /) -> None:
        r"""Move caret to last position on line, extending rectangular selection to new caret position.

        Sends `SCI_LINEENDRECTEXTEND`."""
    def lineEndTypesActive(self, /) -> int:
        r"""Get the line end types currently recognised. May be a subset of the allowed types due to lexer limitation.

        Sends `SCI_GETLINEENDTYPESACTIVE`."""
    def lineEndTypesAllowed(self, /) -> int:
        r"""Get the line end types currently allowed.

        Sends `SCI_GETLINEENDTYPESALLOWED`."""
    def lineEndTypesSupported(self, /) -> int:
        r"""Bit set of LineEndType enumertion for which line ends beyond the standard LF, CR, and CRLF are supported by the lexer.

        Sends `SCI_GETLINEENDTYPESSUPPORTED`."""
    def lineEndWrap(self, /) -> None:
        r"""Like LineEnd but when word-wrap is enabled goes first to end of display line LineEndDisplay, then to start of document line LineEnd.

        Sends `SCI_LINEENDWRAP`."""
    def lineEndWrapExtend(self, /) -> None:
        r"""Like LineEndExtend but when word-wrap is enabled extends first to end of display line LineEndDisplayExtend, then to start of document line LineEndExtend.

        Sends `SCI_LINEENDWRAPEXTEND`."""
    def lineFromIndexPosition(self, pos: int, lineCharacterIndex: int, /) -> int:
        r"""Retrieve the document line containing a position measured in index units.

        Sends `SCI_LINEFROMINDEXPOSITION`."""
    def lineFromPosition(self, pos: int, /) -> int:
        r"""Retrieve the line containing a position.

        Sends `SCI_LINEFROMPOSITION`."""
    def lineIndent(self, /) -> None:
        r"""Indent the current and selected lines.

        Sends `SCI_LINEINDENT`."""
    def lineIndentPosition(self, line: int, /) -> int:
        r"""Retrieve the position before the first non indentation character on a line.

        Sends `SCI_GETLINEINDENTPOSITION`."""
    def lineIndentation(self, line: int, /) -> int:
        r"""Retrieve the number of columns that a line is indented.

        Sends `SCI_GETLINEINDENTATION`."""
    def lineLength(self, line: int, /) -> int:
        r"""How many characters are on a line, including end of line characters?

        Sends `SCI_LINELENGTH`."""
    def lineReverse(self, /) -> None:
        r"""Reverse order of selected lines.

        Sends `SCI_LINEREVERSE`."""
    def lineScroll(self, columns: int, lines: int, /) -> None:
        r"""Scroll horizontally and vertically.

        Sends `SCI_LINESCROLL`."""
    def lineScrollDown(self, /) -> None:
        r"""Scroll the document down, keeping the caret visible.

        Sends `SCI_LINESCROLLDOWN`."""
    def lineScrollUp(self, /) -> None:
        r"""Scroll the document up, keeping the caret visible.

        Sends `SCI_LINESCROLLUP`."""
    def lineState(self, line: int, /) -> int:
        r"""Retrieve the extra styling information for a line.

        Sends `SCI_GETLINESTATE`."""
    def lineTranspose(self, /) -> None:
        r"""Switch the current line with the previous.

        Sends `SCI_LINETRANSPOSE`."""
    def lineUp(self, /) -> None:
        r"""Move caret up one line.

        Sends `SCI_LINEUP`."""
    def lineUpExtend(self, /) -> None:
        r"""Move caret up one line extending selection to new caret position.

        Sends `SCI_LINEUPEXTEND`."""
    def lineUpRectExtend(self, /) -> None:
        r"""Move caret up one line, extending rectangular selection to new caret position.

        Sends `SCI_LINEUPRECTEXTEND`."""
    def lineVisible(self, line: int, /) -> bool:
        r"""Is a line visible?

        Sends `SCI_GETLINEVISIBLE`."""
    def linesJoin(self, /) -> None:
        r"""Join the lines in the target.

        Sends `SCI_LINESJOIN`."""
    def linesOnScreen(self, /) -> int:
        r"""Retrieves the number of lines completely visible.

        Sends `SCI_LINESONSCREEN`."""
    def linesSplit(self, pixelWidth: int, /) -> None:
        r"""Split the lines in the target into lines that are less wide than pixelWidth where possible.

        Sends `SCI_LINESSPLIT`."""
    def lowerCase(self, /) -> None:
        r"""Transform the selection to lower case.

        Sends `SCI_LOWERCASE`."""
    def mainSelection(self, /) -> int:
        r"""Which selection is the main selection

        Sends `SCI_GETMAINSELECTION`."""
    def marginBackN(self, margin: int, /) -> PySide6.QtGui.QColor:
        r"""Retrieve the background colour of a margin

        Sends `SCI_GETMARGINBACKN`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def marginCursorN(self, margin: int, /) -> int:
        r"""Retrieve the cursor shown in a margin.

        Sends `SCI_GETMARGINCURSORN`."""
    def marginLeft(self, /) -> int:
        r"""Returns the size in pixels of the left margin.

        Sends `SCI_GETMARGINLEFT`."""
    def marginMaskN(self, margin: int, /) -> int:
        r"""Retrieve the marker mask of a margin.

        Sends `SCI_GETMARGINMASKN`."""
    def marginOptions(self, /) -> int:
        r"""Get the margin options.

        Sends `SCI_GETMARGINOPTIONS`."""
    def marginRight(self, /) -> int:
        r"""Returns the size in pixels of the right margin.

        Sends `SCI_GETMARGINRIGHT`."""
    def marginSensitiveN(self, margin: int, /) -> bool:
        r"""Retrieve the mouse click sensitivity of a margin.

        Sends `SCI_GETMARGINSENSITIVEN`."""
    def marginSetStyle(self, line: int, style: int, /) -> None:
        r"""Set the style number for the text margin for a line

        Sends `SCI_MARGINSETSTYLE`."""
    def marginSetStyleOffset(self, style: int, /) -> None:
        r"""Get the start of the range of style numbers used for margin text

        Sends `SCI_MARGINSETSTYLEOFFSET`."""
    def marginSetStyles(self, line: int, styles: PySide6.QtCore.QByteArray | bytes | bytearray, /) -> None:
        r"""Set the style in the text margin for a line

        Sends `SCI_MARGINSETSTYLES`."""
    def marginSetText(self, line: int, text: str, /) -> None:
        r"""Set the text in the text margin for a line

        Sends `SCI_MARGINSETTEXT`."""
    def marginStyle(self, line: int, /) -> int:
        r"""Get the style number for the text margin for a line

        Sends `SCI_MARGINGETSTYLE`."""
    def marginStyleOffset(self, /) -> int:
        r"""Get the start of the range of style numbers used for margin text

        Sends `SCI_MARGINGETSTYLEOFFSET`."""
    def marginStyles(self, line: int, /) -> PySide6.QtCore.QByteArray:
        r"""Get the styles in the text margin for a line

        Sends `SCI_MARGINGETSTYLES`. Returns the result instead of filling a `styles` buffer; the message's own result (the length) is dropped."""
    def marginText(self, line: int, /) -> str:
        r"""Get the text in the text margin for a line

        Sends `SCI_MARGINGETTEXT`. Returns the result instead of filling a `text` buffer; the message's own result (the length) is dropped."""
    def marginTextClearAll(self, /) -> None:
        r"""Clear the margin text on all lines

        Sends `SCI_MARGINTEXTCLEARALL`."""
    def marginTypeN(self, margin: int, /) -> int:
        r"""Retrieve the type of a margin.

        Sends `SCI_GETMARGINTYPEN`."""
    def marginWidthN(self, margin: int, /) -> int:
        r"""Retrieve the width of a margin in pixels.

        Sends `SCI_GETMARGINWIDTHN`."""
    def margins(self, /) -> int:
        r"""How many margins are there?.

        Sends `SCI_GETMARGINS`."""
    def markerAdd(self, line: int, markerNumber: int, /) -> int:
        r"""Add a marker to a line, returning an ID which can be used to find or delete the marker.

        Sends `SCI_MARKERADD`."""
    def markerAddSet(self, line: int, markerSet: int, /) -> None:
        r"""Add a set of markers to a line.

        Sends `SCI_MARKERADDSET`."""
    def markerDefine(self, markerNumber: int, markerSymbol: int, /) -> None:
        r"""Set the symbol used for a particular marker number.

        Sends `SCI_MARKERDEFINE`."""
    def markerDefinePixmap(self, markerNumber: int, pixmap: PySide6.QtCore.QByteArray | bytes | bytearray, /) -> None:
        r"""Define a marker from a pixmap.

        Sends `SCI_MARKERDEFINEPIXMAP`."""
    def markerDefineRGBAImage(self, markerNumber: int, pixels: PySide6.QtCore.QByteArray | bytes | bytearray, /) -> None:
        r"""Define a marker from RGBA data. It has the width and height from RGBAImageSetWidth/Height

        Sends `SCI_MARKERDEFINERGBAIMAGE`."""
    def markerDelete(self, line: int, markerNumber: int, /) -> None:
        r"""Delete a marker from a line.

        Sends `SCI_MARKERDELETE`."""
    def markerDeleteAll(self, markerNumber: int, /) -> None:
        r"""Delete all markers with a particular number from all lines.

        Sends `SCI_MARKERDELETEALL`."""
    def markerDeleteHandle(self, markerHandle: int, /) -> None:
        r"""Delete a marker.

        Sends `SCI_MARKERDELETEHANDLE`."""
    def markerEnableHighlight(self, enabled: bool, /) -> None:
        r"""Enable/disable highlight for current folding block (smallest one that contains the caret)

        Sends `SCI_MARKERENABLEHIGHLIGHT`."""
    def markerGet(self, line: int, /) -> int:
        r"""Get a bit mask of all the markers set on a line.

        Sends `SCI_MARKERGET`."""
    def markerHandleFromLine(self, line: int, which: int, /) -> int:
        r"""Retrieve marker handles of a line

        Sends `SCI_MARKERHANDLEFROMLINE`."""
    def markerLayer(self, markerNumber: int, /) -> int:
        r"""Get the layer used for a marker that is drawn in the text area, not the margin.

        Sends `SCI_MARKERGETLAYER`."""
    def markerLineFromHandle(self, markerHandle: int, /) -> int:
        r"""Retrieve the line number at which a particular marker is located.

        Sends `SCI_MARKERLINEFROMHANDLE`."""
    def markerNext(self, lineStart: int, markerMask: int, /) -> int:
        r"""Find the next line at or after lineStart that includes a marker in mask. Return -1 when no more lines.

        Sends `SCI_MARKERNEXT`."""
    def markerNumberFromLine(self, line: int, which: int, /) -> int:
        r"""Retrieve marker number of a marker handle

        Sends `SCI_MARKERNUMBERFROMLINE`."""
    def markerPrevious(self, lineStart: int, markerMask: int, /) -> int:
        r"""Find the previous line before lineStart that includes a marker in mask.

        Sends `SCI_MARKERPREVIOUS`."""
    def markerSetAlpha(self, markerNumber: int, alpha: int, /) -> None:
        r"""Set the alpha used for a marker that is drawn in the text area, not the margin.

        Sends `SCI_MARKERSETALPHA`."""
    def markerSetBack(self, markerNumber: int, back: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set the background colour used for a particular marker number.

        Sends `SCI_MARKERSETBACK`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def markerSetBackSelected(self, markerNumber: int, back: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set the background colour used for a particular marker number when its folding block is selected.

        Sends `SCI_MARKERSETBACKSELECTED`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def markerSetBackSelectedTranslucent(self, markerNumber: int, back: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set the background colour used for a particular marker number when its folding block is selected.

        Sends `SCI_MARKERSETBACKSELECTEDTRANSLUCENT`. Uses a `QColor` (with alpha) where the message uses a packed `0xAABBGGRR` int."""
    def markerSetBackTranslucent(self, markerNumber: int, back: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set the background colour used for a particular marker number.

        Sends `SCI_MARKERSETBACKTRANSLUCENT`. Uses a `QColor` (with alpha) where the message uses a packed `0xAABBGGRR` int."""
    def markerSetFore(self, markerNumber: int, fore: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set the foreground colour used for a particular marker number.

        Sends `SCI_MARKERSETFORE`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def markerSetForeTranslucent(self, markerNumber: int, fore: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set the foreground colour used for a particular marker number.

        Sends `SCI_MARKERSETFORETRANSLUCENT`. Uses a `QColor` (with alpha) where the message uses a packed `0xAABBGGRR` int."""
    def markerSetLayer(self, markerNumber: int, layer: int, /) -> None:
        r"""Set the layer used for a marker that is drawn in the text area, not the margin.

        Sends `SCI_MARKERSETLAYER`."""
    def markerSetStrokeWidth(self, markerNumber: int, hundredths: int, /) -> None:
        r"""Set the width of strokes used in .01 pixels so 50  = 1/2 pixel width.

        Sends `SCI_MARKERSETSTROKEWIDTH`."""
    def markerSymbolDefined(self, markerNumber: int, /) -> int:
        r"""Which symbol was defined for markerNumber with MarkerDefine

        Sends `SCI_MARKERSYMBOLDEFINED`."""
    def maxLineState(self, /) -> int:
        r"""Retrieve the last line number that has line state.

        Sends `SCI_GETMAXLINESTATE`."""
    def modEventMask(self, /) -> int:
        r"""Get which document modification events are sent to the container.

        Sends `SCI_GETMODEVENTMASK`."""
    def modify(self, /) -> bool:
        r"""Is the document different from when it was last saved?

        Sends `SCI_GETMODIFY`."""
    def mouseDownCaptures(self, /) -> bool:
        r"""Get whether mouse gets captured.

        Sends `SCI_GETMOUSEDOWNCAPTURES`."""
    def mouseDwellTime(self, /) -> int:
        r"""Retrieve the time the mouse must sit still to generate a mouse dwell event.

        Sends `SCI_GETMOUSEDWELLTIME`."""
    def mouseSelectionRectangularSwitch(self, /) -> bool:
        r"""Whether switching to rectangular mode while selecting with the mouse is allowed.

        Sends `SCI_GETMOUSESELECTIONRECTANGULARSWITCH`."""
    def mouseWheelCaptures(self, /) -> bool:
        r"""Get whether mouse wheel can be active outside the window.

        Sends `SCI_GETMOUSEWHEELCAPTURES`."""
    def moveCaretInsideView(self, /) -> None:
        r"""Move the caret inside current view if it's not there already.

        Sends `SCI_MOVECARETINSIDEVIEW`."""
    def moveExtendsSelection(self, /) -> bool:
        r"""Get whether or not regular caret moves will extend or reduce the selection.

        Sends `SCI_GETMOVEEXTENDSSELECTION`."""
    def moveSelectedLinesDown(self, /) -> None:
        r"""Move the selected lines down one line, shifting the line below before the selection

        Sends `SCI_MOVESELECTEDLINESDOWN`."""
    def moveSelectedLinesUp(self, /) -> None:
        r"""Move the selected lines up one line, shifting the line above after the selection

        Sends `SCI_MOVESELECTEDLINESUP`."""
    def multiEdgeAddLine(self, column: int, edgeColour: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Add a new vertical edge to the view.

        Sends `SCI_MULTIEDGEADDLINE`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def multiEdgeClearAll(self, /) -> None:
        r"""Clear all vertical edges.

        Sends `SCI_MULTIEDGECLEARALL`."""
    def multiEdgeColumn(self, which: int, /) -> int:
        r"""Get multi edge positions.

        Sends `SCI_GETMULTIEDGECOLUMN`."""
    def multiPaste(self, /) -> int:
        r"""Retrieve the effect of pasting when there are multiple selections.

        Sends `SCI_GETMULTIPASTE`."""
    def multipleSelectAddEach(self, /) -> None:
        r"""Add each occurrence of the main selection in the target to the set of selections. If the current selection is empty then select word around caret.

        Sends `SCI_MULTIPLESELECTADDEACH`."""
    def multipleSelectAddNext(self, /) -> None:
        r"""Add the next occurrence of the main selection to the set of selections as main. If the current selection is empty then select word around caret.

        Sends `SCI_MULTIPLESELECTADDNEXT`."""
    def multipleSelection(self, /) -> bool:
        r"""Whether multiple selections can be made

        Sends `SCI_GETMULTIPLESELECTION`."""
    def nameOfStyle(self, style: int, /) -> str:
        r"""Retrieve the name of a style. Result is NUL-terminated.

        Sends `SCI_NAMEOFSTYLE`. Returns the result instead of filling a `name` buffer; the message's own result (the length) is dropped."""
    def namedStyles(self, /) -> int:
        r"""Retrieve the number of named styles for the lexer.

        Sends `SCI_GETNAMEDSTYLES`."""
    def newLine(self, /) -> None:
        r"""Insert a new line, may use a CRLF, CR or LF depending on EOL mode.

        Sends `SCI_NEWLINE`."""
    def null(self, /) -> None:
        r"""Null operation.

        Sends `SCI_NULL`."""
    def overtype(self, /) -> bool:
        r"""Returns true if overtype mode is active otherwise false is returned.

        Sends `SCI_GETOVERTYPE`."""
    def pageDown(self, /) -> None:
        r"""Move caret one page down.

        Sends `SCI_PAGEDOWN`."""
    def pageDownExtend(self, /) -> None:
        r"""Move caret one page down extending selection to new caret position.

        Sends `SCI_PAGEDOWNEXTEND`."""
    def pageDownRectExtend(self, /) -> None:
        r"""Move caret one page down, extending rectangular selection to new caret position.

        Sends `SCI_PAGEDOWNRECTEXTEND`."""
    def pageUp(self, /) -> None:
        r"""Move caret one page up.

        Sends `SCI_PAGEUP`."""
    def pageUpExtend(self, /) -> None:
        r"""Move caret one page up extending selection to new caret position.

        Sends `SCI_PAGEUPEXTEND`."""
    def pageUpRectExtend(self, /) -> None:
        r"""Move caret one page up, extending rectangular selection to new caret position.

        Sends `SCI_PAGEUPRECTEXTEND`."""
    def paraDown(self, /) -> None:
        r"""Move caret down one paragraph (delimited by empty lines).

        Sends `SCI_PARADOWN`."""
    def paraDownExtend(self, /) -> None:
        r"""Extend selection down one paragraph (delimited by empty lines).

        Sends `SCI_PARADOWNEXTEND`."""
    def paraUp(self, /) -> None:
        r"""Move caret up one paragraph (delimited by empty lines).

        Sends `SCI_PARAUP`."""
    def paraUpExtend(self, /) -> None:
        r"""Extend selection up one paragraph (delimited by empty lines).

        Sends `SCI_PARAUPEXTEND`."""
    def paste(self, /) -> None:
        r"""Paste the contents of the clipboard into the document replacing the selection.

        Sends `SCI_PASTE`."""
    def pasteConvertEndings(self, /) -> bool:
        r"""Get convert-on-paste setting

        Sends `SCI_GETPASTECONVERTENDINGS`."""
    def phasesDraw(self, /) -> int:
        r"""How many phases is drawing done in?

        Sends `SCI_GETPHASESDRAW`."""
    def pointXFromPosition(self, pos: int, /) -> int:
        r"""Retrieve the x value of the point in the window where a position is displayed.

        Sends `SCI_POINTXFROMPOSITION`."""
    def pointYFromPosition(self, pos: int, /) -> int:
        r"""Retrieve the y value of the point in the window where a position is displayed.

        Sends `SCI_POINTYFROMPOSITION`."""
    def positionAfter(self, pos: int, /) -> int:
        r"""Given a valid document position, return the next position taking code page into account. Maximum value returned is the last position in the document.

        Sends `SCI_POSITIONAFTER`."""
    def positionBefore(self, pos: int, /) -> int:
        r"""Given a valid document position, return the previous position taking code page into account. Returns 0 if passed 0.

        Sends `SCI_POSITIONBEFORE`."""
    def positionCache(self, /) -> int:
        r"""How many entries are allocated to the position cache?

        Sends `SCI_GETPOSITIONCACHE`."""
    def positionFromLine(self, line: int, /) -> int:
        r"""Retrieve the position at the start of a line.

        Sends `SCI_POSITIONFROMLINE`."""
    def positionFromPoint(self, x: int, y: int, /) -> int:
        r"""Find the position from a point within the window.

        Sends `SCI_POSITIONFROMPOINT`."""
    def positionFromPointClose(self, x: int, y: int, /) -> int:
        r"""Find the position from a point within the window but return INVALID_POSITION if not close to text.

        Sends `SCI_POSITIONFROMPOINTCLOSE`."""
    def positionRelative(self, pos: int, relative: int, /) -> int:
        r"""Given a valid document position, return a position that differs in a number of characters. Returned value is always between 0 and last position in document.

        Sends `SCI_POSITIONRELATIVE`."""
    def positionRelativeCodeUnits(self, pos: int, relative: int, /) -> int:
        r"""Given a valid document position, return a position that differs in a number of UTF-16 code units. Returned value is always between 0 and last position in document. The result may point half way (2 bytes) inside a non-BMP character.

        Sends `SCI_POSITIONRELATIVECODEUNITS`."""
    def primaryStyleFromStyle(self, style: int, /) -> int:
        r"""For a secondary style, return the primary style, else return the argument.

        Sends `SCI_GETPRIMARYSTYLEFROMSTYLE`."""
    def printColourMode(self, /) -> int:
        r"""Returns the print colour mode.

        Sends `SCI_GETPRINTCOLOURMODE`."""
    def printMagnification(self, /) -> int:
        r"""Returns the print magnification.

        Sends `SCI_GETPRINTMAGNIFICATION`."""
    def printWrapMode(self, /) -> int:
        r"""Is printing line wrapped?

        Sends `SCI_GETPRINTWRAPMODE`."""
    def privateLexerCall(self, operation: int, pointer: int, /) -> int:
        r"""For private communication between an application and a known lexer.

        Sends `SCI_PRIVATELEXERCALL`."""
    def property(self, key: str, /) -> str:
        r"""Retrieve a "property" value previously set with SetProperty. Result is NUL-terminated.

        Sends `SCI_GETPROPERTY`. Returns the result instead of filling a `value` buffer; the message's own result (the length) is dropped."""
    def propertyExpanded(self, key: str, /) -> str:
        r"""Retrieve a "property" value previously set with SetProperty, with "$()" variable replacement on returned buffer. Result is NUL-terminated.

        Sends `SCI_GETPROPERTYEXPANDED`. Returns the result instead of filling a `value` buffer; the message's own result (the length) is dropped."""
    def propertyInt(self, key: str, defaultValue: int, /) -> int:
        r"""Retrieve a "property" value previously set with SetProperty, interpreted as an int AFTER any "$()" variable replacement.

        Sends `SCI_GETPROPERTYINT`."""
    def propertyNames(self, /) -> str:
        r"""Retrieve a '\n' separated list of properties understood by the current lexer. Result is NUL-terminated.

        Sends `SCI_PROPERTYNAMES`. Returns the result instead of filling a `names` buffer; the message's own result (the length) is dropped."""
    def propertyType(self, name: str, /) -> int:
        r"""Retrieve the type of a property.

        Sends `SCI_PROPERTYTYPE`."""
    def punctuationChars(self, /) -> str:
        r"""Get the set of characters making up punctuation characters

        Sends `SCI_GETPUNCTUATIONCHARS`. Returns the result instead of filling a `characters` buffer; the message's own result (the length) is dropped."""
    def pushUndoActionType(self, type: int, pos: int, /) -> None:
        r"""Push one action onto undo history with no text

        Sends `SCI_PUSHUNDOACTIONTYPE`."""
    def rGBAImageSetHeight(self, height: int, /) -> None:
        r"""Set the height for future RGBA image data.

        Sends `SCI_RGBAIMAGESETHEIGHT`."""
    def rGBAImageSetScale(self, scalePercent: int, /) -> None:
        r"""Set the scale factor in percent for future RGBA image data.

        Sends `SCI_RGBAIMAGESETSCALE`."""
    def rGBAImageSetWidth(self, width: int, /) -> None:
        r"""Set the width for future RGBA image data.

        Sends `SCI_RGBAIMAGESETWIDTH`."""
    def rangePointer(self, start: int, lengthRange: int, /) -> int:
        r"""Return a read-only pointer to a range of characters in the document. May move the gap so that the range is contiguous, but will only move up to lengthRange bytes.

        Sends `SCI_GETRANGEPOINTER`."""
    def readOnly(self, /) -> bool:
        r"""In read-only mode?

        Sends `SCI_GETREADONLY`."""
    def rectangularSelectionAnchor(self, /) -> int:
        r"""Return the anchor position of the rectangular selection.

        Sends `SCI_GETRECTANGULARSELECTIONANCHOR`."""
    def rectangularSelectionAnchorVirtualSpace(self, /) -> int:
        r"""Return the virtual space of the anchor of the rectangular selection.

        Sends `SCI_GETRECTANGULARSELECTIONANCHORVIRTUALSPACE`."""
    def rectangularSelectionCaret(self, /) -> int:
        r"""Return the caret position of the rectangular selection.

        Sends `SCI_GETRECTANGULARSELECTIONCARET`."""
    def rectangularSelectionCaretVirtualSpace(self, /) -> int:
        r"""Return the virtual space of the caret of the rectangular selection.

        Sends `SCI_GETRECTANGULARSELECTIONCARETVIRTUALSPACE`."""
    def rectangularSelectionModifier(self, /) -> int:
        r"""Get the modifier key used for rectangular selection.

        Sends `SCI_GETRECTANGULARSELECTIONMODIFIER`."""
    def redo(self, /) -> None:
        r"""Redoes the next action on the undo history.

        Sends `SCI_REDO`."""
    def registerImage(self, type: int, xpmData: PySide6.QtCore.QByteArray | bytes | bytearray, /) -> None:
        r"""Register an XPM image for use in autocompletion lists.

        Sends `SCI_REGISTERIMAGE`."""
    def registerRGBAImage(self, type: int, pixels: PySide6.QtCore.QByteArray | bytes | bytearray, /) -> None:
        r"""Register an RGBA image for use in autocompletion lists. It has the width and height from RGBAImageSetWidth/Height

        Sends `SCI_REGISTERRGBAIMAGE`."""
    def releaseAllExtendedStyles(self, /) -> None:
        r"""Release all extended (>255) style numbers

        Sends `SCI_RELEASEALLEXTENDEDSTYLES`."""
    def releaseDocument(self, doc: int, /) -> None:
        r"""Release a reference to the document, deleting document if it fades to black.

        Sends `SCI_RELEASEDOCUMENT`."""
    def releaseLineCharacterIndex(self, lineCharacterIndex: int, /) -> None:
        r"""Decrease use count of line character index and remove if 0.

        Sends `SCI_RELEASELINECHARACTERINDEX`."""
    def replaceRectangular(self, text: str, /) -> None:
        r"""Replace the selection with text like a rectangular paste.

        Sends `SCI_REPLACERECTANGULAR`. No `length` argument: it's the byte length of the encoded `text`."""
    def replaceSel(self, text: str, /) -> None:
        r"""Replace the selected text with the argument text.

        Sends `SCI_REPLACESEL`. Unlike the message (a NUL-terminated string), keeps embedded NUL characters: text containing one is inserted with `SCI_ADDTEXT` and an explicit length instead."""
    def replaceTarget(self, text: str, /) -> int:
        r"""Replace the target text with the argument text. Text is counted so it can contain NULs. Returns the length of the replacement text.

        Sends `SCI_REPLACETARGET`. No `length` argument: it's the byte length of the encoded `text`."""
    def replaceTargetMinimal(self, text: str, /) -> int:
        r"""Replace the target text with the argument text but ignore prefix and suffix that are the same as current.

        Sends `SCI_REPLACETARGETMINIMAL`. No `length` argument: it's the byte length of the encoded `text`."""
    def replaceTargetRE(self, text: str, /) -> int:
        r"""Replace the target text with the argument text after \d processing. Text is counted so it can contain NULs. Looks for \d where d is between 1 and 9 and replaces these with the strings matched in the last search operation which were surrounded by \( and \). Returns the length of the replacement text including any change caused by processing the \d patterns.

        Sends `SCI_REPLACETARGETRE`. No `length` argument: it's the byte length of the encoded `text`."""
    def representation(self, encodedCharacter: str, /) -> str:
        r"""Get the way a character is drawn. Result is NUL-terminated.

        Sends `SCI_GETREPRESENTATION`. Returns the result instead of filling a `representation` buffer; the message's own result (the length) is dropped."""
    def representationAppearance(self, encodedCharacter: str, /) -> int:
        r"""Get the appearance of a representation.

        Sends `SCI_GETREPRESENTATIONAPPEARANCE`."""
    def representationColour(self, encodedCharacter: str, /) -> PySide6.QtGui.QColor:
        r"""Get the colour of a representation.

        Sends `SCI_GETREPRESENTATIONCOLOUR`. Uses a `QColor` (with alpha) where the message uses a packed `0xAABBGGRR` int. The message's 0 result for an unset value is `QColor(0, 0, 0, 0)`, transparent black."""
    def resetElementColour(self, element: int, /) -> None:
        r"""Use the default or platform-defined colour for an element.

        Sends `SCI_RESETELEMENTCOLOUR`."""
    def rotateSelection(self, /) -> None:
        r"""Set the main selection to the next selection.

        Sends `SCI_ROTATESELECTION`."""
    def scrollCaret(self, /) -> None:
        r"""Ensure the caret is visible.

        Sends `SCI_SCROLLCARET`."""
    def scrollRange(self, secondary: int, primary: int, /) -> None:
        r"""Scroll the argument positions and the range between them into view giving priority to the primary position then the secondary position. This may be used to make a search match visible.

        Sends `SCI_SCROLLRANGE`."""
    def scrollToEnd(self, /) -> None:
        r"""Scroll to end of document.

        Sends `SCI_SCROLLTOEND`."""
    def scrollToStart(self, /) -> None:
        r"""Scroll to start of document.

        Sends `SCI_SCROLLTOSTART`."""
    def scrollVertical(self, docLine: int, subLine: int, /) -> None:
        r"""Scroll vertically with allowance for wrapping.

        Sends `SCI_SCROLLVERTICAL`."""
    def scrollWidth(self, /) -> int:
        r"""Retrieve the document width assumed for scrolling.

        Sends `SCI_GETSCROLLWIDTH`."""
    def scrollWidthTracking(self, /) -> bool:
        r"""Retrieve whether the scroll width tracks wide lines.

        Sends `SCI_GETSCROLLWIDTHTRACKING`."""
    def searchAnchor(self, /) -> None:
        r"""Sets the current caret position to be the search anchor.

        Sends `SCI_SEARCHANCHOR`."""
    def searchFlags(self, /) -> int:
        r"""Get the search flags used by SearchInTarget.

        Sends `SCI_GETSEARCHFLAGS`."""
    def searchInTarget(self, text: str, /) -> int:
        r"""Search for a counted string in the target and set the target to the found range. Text is counted so it can contain NULs. Returns start of found range or -1 for failure in which case target is not moved.

        Sends `SCI_SEARCHINTARGET`. No `length` argument: it's the byte length of the encoded `text`."""
    def searchNext(self, searchFlags: int, text: str, /) -> int:
        r"""Find some text starting at the search anchor. Does not ensure the selection is visible.

        Sends `SCI_SEARCHNEXT`."""
    def searchPrev(self, searchFlags: int, text: str, /) -> int:
        r"""Find some text starting at the search anchor and moving backwards. Does not ensure the selection is visible.

        Sends `SCI_SEARCHPREV`."""
    def selAlpha(self, /) -> int:
        r"""Get the alpha of the selection.

        Sends `SCI_GETSELALPHA`."""
    def selEOLFilled(self, /) -> bool:
        r"""Is the selection end of line filled?

        Sends `SCI_GETSELEOLFILLED`."""
    def selectAll(self, /) -> None:
        r"""Select all the text in the document.

        Sends `SCI_SELECTALL`."""
    def selectionDuplicate(self, /) -> None:
        r"""Duplicate the selection. If selection empty duplicate the line containing the caret.

        Sends `SCI_SELECTIONDUPLICATE`."""
    def selectionEmpty(self, /) -> bool:
        r"""Is every selected range empty?

        Sends `SCI_GETSELECTIONEMPTY`."""
    def selectionEnd(self, /) -> int:
        r"""Returns the position at the end of the selection.

        Sends `SCI_GETSELECTIONEND`."""
    def selectionFromPoint(self, x: int, y: int, /) -> int:
        r"""Find the selection index for a point. -1 when not at a selection.

        Sends `SCI_SELECTIONFROMPOINT`."""
    def selectionHidden(self, /) -> bool:
        r"""Sends `SCI_GETSELECTIONHIDDEN`."""
    def selectionIsRectangle(self, /) -> bool:
        r"""Is the selection rectangular? The alternative is the more common stream selection.

        Sends `SCI_SELECTIONISRECTANGLE`."""
    def selectionLayer(self, /) -> int:
        r"""Get the layer for drawing selections

        Sends `SCI_GETSELECTIONLAYER`."""
    def selectionMode(self, /) -> int:
        r"""Get the mode of the current selection.

        Sends `SCI_GETSELECTIONMODE`."""
    def selectionNAnchor(self, selection: int, /) -> int:
        r"""Return the anchor position of the nth selection.

        Sends `SCI_GETSELECTIONNANCHOR`."""
    def selectionNAnchorVirtualSpace(self, selection: int, /) -> int:
        r"""Return the virtual space of the anchor of the nth selection.

        Sends `SCI_GETSELECTIONNANCHORVIRTUALSPACE`."""
    def selectionNCaret(self, selection: int, /) -> int:
        r"""Return the caret position of the nth selection.

        Sends `SCI_GETSELECTIONNCARET`."""
    def selectionNCaretVirtualSpace(self, selection: int, /) -> int:
        r"""Return the virtual space of the caret of the nth selection.

        Sends `SCI_GETSELECTIONNCARETVIRTUALSPACE`."""
    def selectionNEnd(self, selection: int, /) -> int:
        r"""Returns the position at the end of the selection.

        Sends `SCI_GETSELECTIONNEND`."""
    def selectionNEndVirtualSpace(self, selection: int, /) -> int:
        r"""Returns the virtual space at the end of the selection.

        Sends `SCI_GETSELECTIONNENDVIRTUALSPACE`."""
    def selectionNStart(self, selection: int, /) -> int:
        r"""Returns the position at the start of the selection.

        Sends `SCI_GETSELECTIONNSTART`."""
    def selectionNStartVirtualSpace(self, selection: int, /) -> int:
        r"""Returns the virtual space at the start of the selection.

        Sends `SCI_GETSELECTIONNSTARTVIRTUALSPACE`."""
    def selectionSerialized(self, /) -> str:
        r"""Retrieve serialized form of selection.

        Sends `SCI_GETSELECTIONSERIALIZED`. Returns the result instead of filling a `selectionString` buffer; the message's own result (the length) is dropped."""
    def selectionStart(self, /) -> int:
        r"""Returns the position at the start of the selection.

        Sends `SCI_GETSELECTIONSTART`."""
    def selections(self, /) -> int:
        r"""How many selections are there?

        Sends `SCI_GETSELECTIONS`."""
    def setAccessibility(self, accessibility: int, /) -> None:
        r"""Enable or disable accessibility.

        Sends `SCI_SETACCESSIBILITY`."""
    def setAdditionalCaretFore(self, fore: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set the foreground colour of additional carets.

        Sends `SCI_SETADDITIONALCARETFORE`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def setAdditionalCaretsBlink(self, additionalCaretsBlink: bool, /) -> None:
        r"""Set whether additional carets will blink

        Sends `SCI_SETADDITIONALCARETSBLINK`."""
    def setAdditionalCaretsVisible(self, additionalCaretsVisible: bool, /) -> None:
        r"""Set whether additional carets are visible

        Sends `SCI_SETADDITIONALCARETSVISIBLE`."""
    def setAdditionalSelAlpha(self, alpha: int, /) -> None:
        r"""Set the alpha of the selection.

        Sends `SCI_SETADDITIONALSELALPHA`."""
    def setAdditionalSelBack(self, back: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set the background colour of additional selections. Must have previously called SetSelBack with non-zero first argument for this to have an effect.

        Sends `SCI_SETADDITIONALSELBACK`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def setAdditionalSelFore(self, fore: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set the foreground colour of additional selections. Must have previously called SetSelFore with non-zero first argument for this to have an effect.

        Sends `SCI_SETADDITIONALSELFORE`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def setAdditionalSelectionTyping(self, additionalSelectionTyping: bool, /) -> None:
        r"""Set whether typing can be performed into multiple selections

        Sends `SCI_SETADDITIONALSELECTIONTYPING`."""
    def setAnchor(self, anchor: int, /) -> None:
        r"""Set the selection anchor to a position. The anchor is the opposite end of the selection from the caret.

        Sends `SCI_SETANCHOR`."""
    def setAutomaticFold(self, automaticFold: int, /) -> None:
        r"""Set automatic folding behaviours.

        Sends `SCI_SETAUTOMATICFOLD`."""
    def setBackSpaceUnIndents(self, bsUnIndents: bool, /) -> None:
        r"""Sets whether a backspace pressed when caret is within indentation unindents.

        Sends `SCI_SETBACKSPACEUNINDENTS`."""
    def setBidirectional(self, bidirectional: int, /) -> None:
        r"""Set bidirectional text display state.

        Sends `SCI_SETBIDIRECTIONAL`."""
    def setBufferedDraw(self, buffered: bool, /) -> None:
        r"""If drawing is buffered then each line of text is drawn into a bitmap buffer before drawing it to the screen to avoid flicker.

        Sends `SCI_SETBUFFEREDDRAW`."""
    def setCaretFore(self, fore: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set the foreground colour of the caret.

        Sends `SCI_SETCARETFORE`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def setCaretLineBack(self, back: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set the colour of the background of the line containing the caret.

        Sends `SCI_SETCARETLINEBACK`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def setCaretLineBackAlpha(self, alpha: int, /) -> None:
        r"""Set background alpha of the caret line.

        Sends `SCI_SETCARETLINEBACKALPHA`."""
    def setCaretLineFrame(self, width: int, /) -> None:
        r"""Display the caret line framed. Set width != 0 to enable this option and width = 0 to disable it.

        Sends `SCI_SETCARETLINEFRAME`."""
    def setCaretLineHighlightSubLine(self, subLine: bool, /) -> None:
        r"""Set only highlighting subline instead of whole line.

        Sends `SCI_SETCARETLINEHIGHLIGHTSUBLINE`."""
    def setCaretLineLayer(self, layer: int, /) -> None:
        r"""Set the layer of the background of the line containing the caret.

        Sends `SCI_SETCARETLINELAYER`."""
    def setCaretLineVisible(self, show: bool, /) -> None:
        r"""Display the background of the line containing the caret in a different colour.

        Sends `SCI_SETCARETLINEVISIBLE`."""
    def setCaretLineVisibleAlways(self, alwaysVisible: bool, /) -> None:
        r"""Sets the caret line to always visible.

        Sends `SCI_SETCARETLINEVISIBLEALWAYS`."""
    def setCaretPeriod(self, periodMilliseconds: int, /) -> None:
        r"""Get the time in milliseconds that the caret is on and off. 0 = steady on.

        Sends `SCI_SETCARETPERIOD`."""
    def setCaretSticky(self, useCaretStickyBehaviour: int, /) -> None:
        r"""Stop the caret preferred x position changing when the user types.

        Sends `SCI_SETCARETSTICKY`."""
    def setCaretStyle(self, caretStyle: int, /) -> None:
        r"""Set the style of the caret to be drawn.

        Sends `SCI_SETCARETSTYLE`."""
    def setCaretWidth(self, pixelWidth: int, /) -> None:
        r"""Set the width of the insert mode caret.

        Sends `SCI_SETCARETWIDTH`."""
    def setChangeHistory(self, changeHistory: int, /) -> None:
        r"""Enable or disable change history.

        Sends `SCI_SETCHANGEHISTORY`."""
    def setCharacterCategoryOptimization(self, countCharacters: int, /) -> None:
        r"""Set the number of characters to have directly indexed categories

        Sends `SCI_SETCHARACTERCATEGORYOPTIMIZATION`."""
    def setCharsDefault(self, /) -> None:
        r"""Reset the set of characters for whitespace and word characters to the defaults.

        Sends `SCI_SETCHARSDEFAULT`."""
    def setCodePage(self, codePage: int, /) -> None:
        r"""Set the code page used to interpret the bytes of the document as characters. The SC_CP_UTF8 value can be used to enter Unicode mode.

        Sends `SCI_SETCODEPAGE`."""
    def setCommandEvents(self, commandEvents: bool, /) -> None:
        r"""Set whether command events are sent to the container.

        Sends `SCI_SETCOMMANDEVENTS`."""
    def setControlCharSymbol(self, symbol: int, /) -> None:
        r"""Change the way control characters are displayed: If symbol is < 32, keep the drawn way, else, use the given character.

        Sends `SCI_SETCONTROLCHARSYMBOL`."""
    def setCopySeparator(self, separator: str, /) -> None:
        r"""Set the string to separate parts when copying a multiple selection.

        Sends `SCI_SETCOPYSEPARATOR`."""
    def setCurrentPos(self, caret: int, /) -> None:
        r"""Sets the position of the caret.

        Sends `SCI_SETCURRENTPOS`."""
    def setCursor(self, cursorType: int, /) -> None:
        r"""Sets the cursor to one of the SC_CURSOR* values.

        Sends `SCI_SETCURSOR`."""
    def setDefaultFoldDisplayText(self, text: str, /) -> None:
        r"""Set the default fold display text.

        Sends `SCI_SETDEFAULTFOLDDISPLAYTEXT`."""
    def setDocPointer(self, doc: int, /) -> None:
        r"""Change the document object used.

        Sends `SCI_SETDOCPOINTER`."""
    def setDragDropEnabled(self, dragDropEnabled: bool, /) -> None:
        r"""Enable or disable drag-and-drop

        Sends `SCI_SETDRAGDROPENABLED`."""
    def setEOLMode(self, eolMode: int, /) -> None:
        r"""Set the current end of line mode.

        Sends `SCI_SETEOLMODE`."""
    def setEdgeColour(self, edgeColour: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Change the colour used in edge indication.

        Sends `SCI_SETEDGECOLOUR`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def setEdgeColumn(self, column: int, /) -> None:
        r"""Set the column number of the edge. If text goes past the edge then it is highlighted.

        Sends `SCI_SETEDGECOLUMN`."""
    def setEdgeMode(self, edgeMode: int, /) -> None:
        r"""The edge may be displayed by a line (EDGE_LINE/EDGE_MULTILINE) or by highlighting text that goes beyond it (EDGE_BACKGROUND) or not displayed at all (EDGE_NONE).

        Sends `SCI_SETEDGEMODE`."""
    def setElementColour(self, element: int, colourElement: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set the colour of an element. Translucency (alpha) may or may not be significant and this may depend on the platform. The alpha byte should commonly be 0xff for opaque.

        Sends `SCI_SETELEMENTCOLOUR`. Uses a `QColor` (with alpha) where the message uses a packed `0xAABBGGRR` int."""
    def setEmptySelection(self, caret: int, /) -> None:
        r"""Set caret to a position, while removing any existing selection.

        Sends `SCI_SETEMPTYSELECTION`."""
    def setEndAtLastLine(self, endAtLastLine: bool, /) -> None:
        r"""Sets the scroll range so that maximum scroll position has the last line at the bottom of the view (default). Setting this to false allows scrolling one page below the last line.

        Sends `SCI_SETENDATLASTLINE`."""
    def setExtraAscent(self, extraAscent: int, /) -> None:
        r"""Set extra ascent for each line

        Sends `SCI_SETEXTRAASCENT`."""
    def setExtraDescent(self, extraDescent: int, /) -> None:
        r"""Set extra descent for each line

        Sends `SCI_SETEXTRADESCENT`."""
    def setFirstVisibleLine(self, displayLine: int, /) -> None:
        r"""Scroll so that a display line is at the top of the display.

        Sends `SCI_SETFIRSTVISIBLELINE`."""
    def setFocus(self, focus: bool, /) -> None:
        r"""Change internal focus flag.

        Sends `SCI_SETFOCUS`."""
    def setFoldExpanded(self, line: int, expanded: bool, /) -> None:
        r"""Show the children of a header line.

        Sends `SCI_SETFOLDEXPANDED`."""
    def setFoldFlags(self, flags: int, /) -> None:
        r"""Set some style options for folding.

        Sends `SCI_SETFOLDFLAGS`."""
    def setFoldLevel(self, line: int, level: int, /) -> None:
        r"""Set the fold level of a line. This encodes an integer level along with flags indicating whether the line is a header and whether it is effectively white space.

        Sends `SCI_SETFOLDLEVEL`."""
    def setFoldMarginColour(self, useSetting: bool, back: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set one of the colours used as a chequerboard pattern in the fold margin

        Sends `SCI_SETFOLDMARGINCOLOUR`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def setFoldMarginHiColour(self, useSetting: bool, fore: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set the other colour used as a chequerboard pattern in the fold margin

        Sends `SCI_SETFOLDMARGINHICOLOUR`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def setFontLocale(self, localeName: str, /) -> None:
        r"""Set the locale for displaying text.

        Sends `SCI_SETFONTLOCALE`."""
    def setFontQuality(self, fontQuality: int, /) -> None:
        r"""Choose the quality level for text from the FontQuality enumeration.

        Sends `SCI_SETFONTQUALITY`."""
    def setHScrollBar(self, visible: bool, /) -> None:
        r"""Show or hide the horizontal scroll bar.

        Sends `SCI_SETHSCROLLBAR`."""
    def setHighlightGuide(self, column: int, /) -> None:
        r"""Set the highlighted indentation guide column. 0 = no highlighted guide.

        Sends `SCI_SETHIGHLIGHTGUIDE`."""
    def setHotspotActiveBack(self, useSetting: bool, back: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set a back colour for active hotspots.

        Sends `SCI_SETHOTSPOTACTIVEBACK`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def setHotspotActiveFore(self, useSetting: bool, fore: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set a fore colour for active hotspots.

        Sends `SCI_SETHOTSPOTACTIVEFORE`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def setHotspotActiveUnderline(self, underline: bool, /) -> None:
        r"""Enable / Disable underlining active hotspots.

        Sends `SCI_SETHOTSPOTACTIVEUNDERLINE`."""
    def setHotspotSingleLine(self, singleLine: bool, /) -> None:
        r"""Limit hotspots to single line so hotspots on two lines don't merge.

        Sends `SCI_SETHOTSPOTSINGLELINE`."""
    def setILexer(self, ilexer: int, /) -> None:
        r"""Set the lexer from an ILexer*.

        Sends `SCI_SETILEXER`."""
    def setIMEInteraction(self, imeInteraction: int, /) -> None:
        r"""Choose to display the IME in a window or inline.

        Sends `SCI_SETIMEINTERACTION`."""
    def setIdentifier(self, identifier: int, /) -> None:
        r"""Set the identifier reported as idFrom in notification messages.

        Sends `SCI_SETIDENTIFIER`."""
    def setIdentifiers(self, style: int, identifiers: str, /) -> None:
        r"""Set the identifiers that are shown in a particular style

        Sends `SCI_SETIDENTIFIERS`."""
    def setIdleStyling(self, idleStyling: int, /) -> None:
        r"""Sets limits to idle styling.

        Sends `SCI_SETIDLESTYLING`."""
    def setIndent(self, indentSize: int, /) -> None:
        r"""Set the number of spaces used for one level of indentation.

        Sends `SCI_SETINDENT`."""
    def setIndentationGuides(self, indentView: int, /) -> None:
        r"""Show or hide indentation guides.

        Sends `SCI_SETINDENTATIONGUIDES`."""
    def setIndicatorCurrent(self, indicator: int, /) -> None:
        r"""Set the indicator used for IndicatorFillRange and IndicatorClearRange

        Sends `SCI_SETINDICATORCURRENT`."""
    def setIndicatorValue(self, value: int, /) -> None:
        r"""Set the value used for IndicatorFillRange

        Sends `SCI_SETINDICATORVALUE`."""
    def setKeyWords(self, keyWordSet: int, keyWords: str, /) -> None:
        r"""Set up the key words used by the lexer.

        Sends `SCI_SETKEYWORDS`."""
    def setLayoutCache(self, cacheMode: int, /) -> None:
        r"""Sets the degree of caching of layout information.

        Sends `SCI_SETLAYOUTCACHE`."""
    def setLayoutThreads(self, threads: int, /) -> None:
        r"""Set maximum number of threads used for layout

        Sends `SCI_SETLAYOUTTHREADS`."""
    def setLengthForEncode(self, bytes: int, /) -> None:
        r"""Set the length of the utf8 argument for calling EncodedFromUTF8. Set to -1 and the string will be measured to the first nul.

        Sends `SCI_SETLENGTHFORENCODE`."""
    def setLineEndTypesAllowed(self, lineEndBitSet: int, /) -> None:
        r"""Set the line end types that the application wants to use. May not be used if incompatible with lexer or encoding.

        Sends `SCI_SETLINEENDTYPESALLOWED`."""
    def setLineIndentation(self, line: int, indentation: int, /) -> None:
        r"""Change the indentation of a line to a number of columns.

        Sends `SCI_SETLINEINDENTATION`."""
    def setLineState(self, line: int, state: int, /) -> None:
        r"""Used to hold extra styling information for each line.

        Sends `SCI_SETLINESTATE`."""
    def setMainSelection(self, selection: int, /) -> None:
        r"""Set the main selection

        Sends `SCI_SETMAINSELECTION`."""
    def setMarginBackN(self, margin: int, back: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set the background colour of a margin. Only visible for SC_MARGIN_COLOUR.

        Sends `SCI_SETMARGINBACKN`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def setMarginCursorN(self, margin: int, cursor: int, /) -> None:
        r"""Set the cursor shown when the mouse is inside a margin.

        Sends `SCI_SETMARGINCURSORN`."""
    def setMarginLeft(self, pixelWidth: int, /) -> None:
        r"""Sets the size in pixels of the left margin.

        Sends `SCI_SETMARGINLEFT`."""
    def setMarginMaskN(self, margin: int, mask: int, /) -> None:
        r"""Set a mask that determines which markers are displayed in a margin.

        Sends `SCI_SETMARGINMASKN`."""
    def setMarginOptions(self, marginOptions: int, /) -> None:
        r"""Set the margin options.

        Sends `SCI_SETMARGINOPTIONS`."""
    def setMarginRight(self, pixelWidth: int, /) -> None:
        r"""Sets the size in pixels of the right margin.

        Sends `SCI_SETMARGINRIGHT`."""
    def setMarginSensitiveN(self, margin: int, sensitive: bool, /) -> None:
        r"""Make a margin sensitive or insensitive to mouse clicks.

        Sends `SCI_SETMARGINSENSITIVEN`."""
    def setMarginTypeN(self, margin: int, marginType: int, /) -> None:
        r"""Set a margin to be either numeric or symbolic.

        Sends `SCI_SETMARGINTYPEN`."""
    def setMarginWidthN(self, margin: int, pixelWidth: int, /) -> None:
        r"""Set the width of a margin to a width expressed in pixels.

        Sends `SCI_SETMARGINWIDTHN`."""
    def setMargins(self, margins: int, /) -> None:
        r"""Allocate a non-standard number of margins.

        Sends `SCI_SETMARGINS`."""
    def setModEventMask(self, eventMask: int, /) -> None:
        r"""Set which document modification events are sent to the container.

        Sends `SCI_SETMODEVENTMASK`."""
    def setMouseDownCaptures(self, captures: bool, /) -> None:
        r"""Set whether the mouse is captured when its button is pressed.

        Sends `SCI_SETMOUSEDOWNCAPTURES`."""
    def setMouseDwellTime(self, periodMilliseconds: int, /) -> None:
        r"""Sets the time the mouse must sit still to generate a mouse dwell event.

        Sends `SCI_SETMOUSEDWELLTIME`."""
    def setMouseSelectionRectangularSwitch(self, mouseSelectionRectangularSwitch: bool, /) -> None:
        r"""Set whether switching to rectangular mode while selecting with the mouse is allowed.

        Sends `SCI_SETMOUSESELECTIONRECTANGULARSWITCH`."""
    def setMouseWheelCaptures(self, captures: bool, /) -> None:
        r"""Set whether the mouse wheel can be active outside the window.

        Sends `SCI_SETMOUSEWHEELCAPTURES`."""
    def setMoveExtendsSelection(self, moveExtendsSelection: bool, /) -> None:
        r"""Set whether or not regular caret moves will extend or reduce the selection.

        Sends `SCI_SETMOVEEXTENDSSELECTION`."""
    def setMultiPaste(self, multiPaste: int, /) -> None:
        r"""Change the effect of pasting when there are multiple selections.

        Sends `SCI_SETMULTIPASTE`."""
    def setMultipleSelection(self, multipleSelection: bool, /) -> None:
        r"""Set whether multiple selections can be made

        Sends `SCI_SETMULTIPLESELECTION`."""
    def setOvertype(self, overType: bool, /) -> None:
        r"""Set to overtype (true) or insert mode.

        Sends `SCI_SETOVERTYPE`."""
    def setPasteConvertEndings(self, convert: bool, /) -> None:
        r"""Enable/Disable convert-on-paste for line endings

        Sends `SCI_SETPASTECONVERTENDINGS`."""
    def setPhasesDraw(self, phases: int, /) -> None:
        r"""In one phase draw, text is drawn in a series of rectangular blocks with no overlap. In two phase draw, text is drawn in a series of lines allowing runs to overlap horizontally. In multiple phase draw, each element is drawn over the whole drawing area, allowing text to overlap from one line to the next.

        Sends `SCI_SETPHASESDRAW`."""
    def setPositionCache(self, size: int, /) -> None:
        r"""Set number of entries in position cache

        Sends `SCI_SETPOSITIONCACHE`."""
    def setPrintColourMode(self, mode: int, /) -> None:
        r"""Modify colours when printing for clearer printed text.

        Sends `SCI_SETPRINTCOLOURMODE`."""
    def setPrintMagnification(self, magnification: int, /) -> None:
        r"""Sets the print magnification added to the point size of each style for printing.

        Sends `SCI_SETPRINTMAGNIFICATION`."""
    def setPrintWrapMode(self, wrapMode: int, /) -> None:
        r"""Set printing to line wrapped (SC_WRAP_WORD) or not line wrapped (SC_WRAP_NONE).

        Sends `SCI_SETPRINTWRAPMODE`."""
    def setProperty(self, key: str, value: str, /) -> None:
        r"""Set up a value that may be used by a lexer for some optional feature.

        Sends `SCI_SETPROPERTY`."""
    def setPunctuationChars(self, characters: str, /) -> None:
        r"""Set the set of characters making up punctuation characters Should be called after SetWordChars.

        Sends `SCI_SETPUNCTUATIONCHARS`."""
    def setReadOnly(self, readOnly: bool, /) -> None:
        r"""Set to read only or read write.

        Sends `SCI_SETREADONLY`."""
    def setRectangularSelectionAnchor(self, anchor: int, /) -> None:
        r"""Set the anchor position of the rectangular selection.

        Sends `SCI_SETRECTANGULARSELECTIONANCHOR`."""
    def setRectangularSelectionAnchorVirtualSpace(self, space: int, /) -> None:
        r"""Set the virtual space of the anchor of the rectangular selection.

        Sends `SCI_SETRECTANGULARSELECTIONANCHORVIRTUALSPACE`."""
    def setRectangularSelectionCaret(self, caret: int, /) -> None:
        r"""Set the caret position of the rectangular selection.

        Sends `SCI_SETRECTANGULARSELECTIONCARET`."""
    def setRectangularSelectionCaretVirtualSpace(self, space: int, /) -> None:
        r"""Set the virtual space of the caret of the rectangular selection.

        Sends `SCI_SETRECTANGULARSELECTIONCARETVIRTUALSPACE`."""
    def setRectangularSelectionModifier(self, modifier: int, /) -> None:
        r"""Sends `SCI_SETRECTANGULARSELECTIONMODIFIER`."""
    def setRepresentation(self, encodedCharacter: str, representation: str, /) -> None:
        r"""Set the way a character is drawn.

        Sends `SCI_SETREPRESENTATION`."""
    def setRepresentationAppearance(self, encodedCharacter: str, appearance: int, /) -> None:
        r"""Set the appearance of a representation.

        Sends `SCI_SETREPRESENTATIONAPPEARANCE`."""
    def setRepresentationColour(self, encodedCharacter: str, colour: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set the colour of a representation.

        Sends `SCI_SETREPRESENTATIONCOLOUR`. Uses a `QColor` (with alpha) where the message uses a packed `0xAABBGGRR` int."""
    def setSavePoint(self, /) -> None:
        r"""Remember the current position in the undo history as the position at which the document was saved.

        Sends `SCI_SETSAVEPOINT`."""
    def setScrollWidth(self, pixelWidth: int, /) -> None:
        r"""Sets the document width assumed for scrolling.

        Sends `SCI_SETSCROLLWIDTH`."""
    def setScrollWidthTracking(self, tracking: bool, /) -> None:
        r"""Sets whether the maximum width line displayed is used to set scroll width.

        Sends `SCI_SETSCROLLWIDTHTRACKING`."""
    def setSearchFlags(self, searchFlags: int, /) -> None:
        r"""Set the search flags used by SearchInTarget.

        Sends `SCI_SETSEARCHFLAGS`."""
    def setSel(self, anchor: int, caret: int, /) -> None:
        r"""Select a range of text.

        Sends `SCI_SETSEL`."""
    def setSelAlpha(self, alpha: int, /) -> None:
        r"""Set the alpha of the selection.

        Sends `SCI_SETSELALPHA`."""
    def setSelBack(self, useSetting: bool, back: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set the background colour of the main and additional selections and whether to use this setting.

        Sends `SCI_SETSELBACK`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def setSelEOLFilled(self, filled: bool, /) -> None:
        r"""Set the selection to have its end of line filled or not.

        Sends `SCI_SETSELEOLFILLED`."""
    def setSelFore(self, useSetting: bool, fore: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set the foreground colour of the main and additional selections and whether to use this setting.

        Sends `SCI_SETSELFORE`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def setSelection(self, caret: int, anchor: int, /) -> None:
        r"""Set a simple selection

        Sends `SCI_SETSELECTION`."""
    def setSelectionEnd(self, caret: int, /) -> None:
        r"""Sets the position that ends the selection - this becomes the caret.

        Sends `SCI_SETSELECTIONEND`."""
    def setSelectionLayer(self, layer: int, /) -> None:
        r"""Set the layer for drawing selections: either opaquely on base layer or translucently over text

        Sends `SCI_SETSELECTIONLAYER`."""
    def setSelectionMode(self, selectionMode: int, /) -> None:
        r"""Set the selection mode to stream (SC_SEL_STREAM) or rectangular (SC_SEL_RECTANGLE/SC_SEL_THIN) or by lines (SC_SEL_LINES).

        Sends `SCI_SETSELECTIONMODE`."""
    def setSelectionNAnchor(self, selection: int, anchor: int, /) -> None:
        r"""Set the anchor position of the nth selection.

        Sends `SCI_SETSELECTIONNANCHOR`."""
    def setSelectionNAnchorVirtualSpace(self, selection: int, space: int, /) -> None:
        r"""Set the virtual space of the anchor of the nth selection.

        Sends `SCI_SETSELECTIONNANCHORVIRTUALSPACE`."""
    def setSelectionNCaret(self, selection: int, caret: int, /) -> None:
        r"""Set the caret position of the nth selection.

        Sends `SCI_SETSELECTIONNCARET`."""
    def setSelectionNCaretVirtualSpace(self, selection: int, space: int, /) -> None:
        r"""Set the virtual space of the caret of the nth selection.

        Sends `SCI_SETSELECTIONNCARETVIRTUALSPACE`."""
    def setSelectionNEnd(self, selection: int, caret: int, /) -> None:
        r"""Sets the position that ends the selection - this becomes the currentPosition.

        Sends `SCI_SETSELECTIONNEND`."""
    def setSelectionNStart(self, selection: int, anchor: int, /) -> None:
        r"""Sets the position that starts the selection - this becomes the anchor.

        Sends `SCI_SETSELECTIONNSTART`."""
    def setSelectionSerialized(self, selectionString: str, /) -> None:
        r"""Set selection from serialized form.

        Sends `SCI_SETSELECTIONSERIALIZED`."""
    def setSelectionStart(self, anchor: int, /) -> None:
        r"""Sets the position that starts the selection - this becomes the anchor.

        Sends `SCI_SETSELECTIONSTART`."""
    def setStatus(self, status: int, /) -> None:
        r"""Change error status - 0 = OK.

        Sends `SCI_SETSTATUS`."""
    def setStyling(self, length: int, style: int, /) -> None:
        r"""Change style from current styling position for length characters to a style and move the current styling position to after this newly styled segment.

        Sends `SCI_SETSTYLING`."""
    def setStylingEx(self, styles: PySide6.QtCore.QByteArray | bytes | bytearray, /) -> None:
        r"""Set the styles for a segment of the document.

        Sends `SCI_SETSTYLINGEX`. No `length` argument: it's the byte length of the `styles`."""
    def setTabDrawMode(self, tabDrawMode: int, /) -> None:
        r"""Set how tabs are drawn when visible.

        Sends `SCI_SETTABDRAWMODE`."""
    def setTabIndents(self, tabIndents: bool, /) -> None:
        r"""Sets whether a tab pressed when caret is within indentation indents.

        Sends `SCI_SETTABINDENTS`."""
    def setTabMinimumWidth(self, pixels: int, /) -> None:
        r"""Set the minimum visual width of a tab.

        Sends `SCI_SETTABMINIMUMWIDTH`."""
    def setTabWidth(self, tabWidth: int, /) -> None:
        r"""Change the visible size of a tab to be a multiple of the width of a space character.

        Sends `SCI_SETTABWIDTH`."""
    def setTargetEnd(self, end: int, /) -> None:
        r"""Sets the position that ends the target which is used for updating the document without affecting the scroll position.

        Sends `SCI_SETTARGETEND`."""
    def setTargetEndVirtualSpace(self, space: int, /) -> None:
        r"""Sets the virtual space of the target end

        Sends `SCI_SETTARGETENDVIRTUALSPACE`."""
    def setTargetRange(self, start: int, end: int, /) -> None:
        r"""Sets both the start and end of the target in one call.

        Sends `SCI_SETTARGETRANGE`."""
    def setTargetStart(self, start: int, /) -> None:
        r"""Sets the position that starts the target which is used for updating the document without affecting the scroll position.

        Sends `SCI_SETTARGETSTART`."""
    def setTargetStartVirtualSpace(self, space: int, /) -> None:
        r"""Sets the virtual space of the target start

        Sends `SCI_SETTARGETSTARTVIRTUALSPACE`."""
    def setTechnology(self, technology: int, /) -> None:
        r"""Set the technology used.

        Sends `SCI_SETTECHNOLOGY`."""
    def setText(self, text: str, /) -> None:
        r"""Replace the contents of the document with the argument text.

        Sends `SCI_SETTEXT`. Unlike the message (a NUL-terminated string), keeps embedded NUL characters: text containing one is inserted with `SCI_ADDTEXT` and an explicit length instead."""
    def setUndoCollection(self, collectUndo: bool, /) -> None:
        r"""Choose between collecting actions into the undo history and discarding them.

        Sends `SCI_SETUNDOCOLLECTION`."""
    def setUndoCurrent(self, action: int, /) -> None:
        r"""Set action as the current point

        Sends `SCI_SETUNDOCURRENT`."""
    def setUndoDetach(self, action: int, /) -> None:
        r"""Set action as the detach point

        Sends `SCI_SETUNDODETACH`."""
    def setUndoSavePoint(self, action: int, /) -> None:
        r"""Set action as the save point

        Sends `SCI_SETUNDOSAVEPOINT`."""
    def setUndoSelectionHistory(self, undoSelectionHistory: int, /) -> None:
        r"""Enable or disable undo selection history.

        Sends `SCI_SETUNDOSELECTIONHISTORY`."""
    def setUndoTentative(self, action: int, /) -> None:
        r"""Set action as the tentative point

        Sends `SCI_SETUNDOTENTATIVE`."""
    def setUseTabs(self, useTabs: bool, /) -> None:
        r"""Indentation will only use space characters if useTabs is false, otherwise it will use a combination of tabs and spaces.

        Sends `SCI_SETUSETABS`."""
    def setVScrollBar(self, visible: bool, /) -> None:
        r"""Show or hide the vertical scroll bar.

        Sends `SCI_SETVSCROLLBAR`."""
    def setViewEOL(self, visible: bool, /) -> None:
        r"""Make the end of line characters visible or invisible.

        Sends `SCI_SETVIEWEOL`."""
    def setViewWS(self, viewWS: int, /) -> None:
        r"""Make white space characters invisible, always visible or visible outside indentation.

        Sends `SCI_SETVIEWWS`."""
    def setVirtualSpaceOptions(self, virtualSpaceOptions: int, /) -> None:
        r"""Set options for virtual space behaviour.

        Sends `SCI_SETVIRTUALSPACEOPTIONS`."""
    def setVisiblePolicy(self, visiblePolicy: int, visibleSlop: int, /) -> None:
        r"""Set the way the display area is determined when a particular line is to be moved to by Find, FindNext, GotoLine, etc.

        Sends `SCI_SETVISIBLEPOLICY`."""
    def setWhitespaceBack(self, useSetting: bool, back: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set the background colour of all whitespace and whether to use this setting.

        Sends `SCI_SETWHITESPACEBACK`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def setWhitespaceChars(self, characters: str, /) -> None:
        r"""Set the set of characters making up whitespace for when moving or selecting by word. Should be called after SetWordChars.

        Sends `SCI_SETWHITESPACECHARS`."""
    def setWhitespaceFore(self, useSetting: bool, fore: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set the foreground colour of all whitespace and whether to use this setting.

        Sends `SCI_SETWHITESPACEFORE`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def setWhitespaceSize(self, size: int, /) -> None:
        r"""Set the size of the dots used to mark space characters.

        Sends `SCI_SETWHITESPACESIZE`."""
    def setWordChars(self, characters: str, /) -> None:
        r"""Set the set of characters making up words for when moving or selecting by word. First sets defaults like SetCharsDefault.

        Sends `SCI_SETWORDCHARS`."""
    def setWrapIndentMode(self, wrapIndentMode: int, /) -> None:
        r"""Sets how wrapped sublines are placed. Default is fixed.

        Sends `SCI_SETWRAPINDENTMODE`."""
    def setWrapMode(self, wrapMode: int, /) -> None:
        r"""Sets whether text is word wrapped.

        Sends `SCI_SETWRAPMODE`."""
    def setWrapStartIndent(self, indent: int, /) -> None:
        r"""Set the start indent for wrapped lines.

        Sends `SCI_SETWRAPSTARTINDENT`."""
    def setWrapVisualFlags(self, wrapVisualFlags: int, /) -> None:
        r"""Set the display mode of visual flags for wrapped lines.

        Sends `SCI_SETWRAPVISUALFLAGS`."""
    def setWrapVisualFlagsLocation(self, wrapVisualFlagsLocation: int, /) -> None:
        r"""Set the location of visual flags for wrapped lines.

        Sends `SCI_SETWRAPVISUALFLAGSLOCATION`."""
    def setXCaretPolicy(self, caretPolicy: int, caretSlop: int, /) -> None:
        r"""Set the way the caret is kept visible when going sideways. The exclusion zone is given in pixels.

        Sends `SCI_SETXCARETPOLICY`."""
    def setXOffset(self, xOffset: int, /) -> None:
        r"""Set the xOffset (ie, horizontal scroll position).

        Sends `SCI_SETXOFFSET`."""
    def setYCaretPolicy(self, caretPolicy: int, caretSlop: int, /) -> None:
        r"""Set the way the line the caret is on is kept visible. The exclusion zone is given in lines.

        Sends `SCI_SETYCARETPOLICY`."""
    def setZoom(self, zoomInPoints: int, /) -> None:
        r"""Set the zoom level. This number of points is added to the size of all fonts. It may be positive to magnify or negative to reduce.

        Sends `SCI_SETZOOM`."""
    def set_doc(self, pdoc_: ScintillaDocument, /) -> None:
        r"""Make this editor display `doc`.

        The document isn't copied -- multiple `ScintillaEdit` widgets can share it this way."""
    def showLines(self, lineStart: int, lineEnd: int, /) -> None:
        r"""Make a range of lines visible.

        Sends `SCI_SHOWLINES`."""
    def startRecord(self, /) -> None:
        r"""Start notifying the container of all key presses and commands.

        Sends `SCI_STARTRECORD`."""
    def startStyling(self, start: int, unused: int, /) -> None:
        r"""Set the current styling position to start. The unused parameter is no longer used and should be set to 0.

        Sends `SCI_STARTSTYLING`."""
    def status(self, /) -> int:
        r"""Get error status.

        Sends `SCI_GETSTATUS`."""
    def stopRecord(self, /) -> None:
        r"""Stop notifying the container of all key presses and commands.

        Sends `SCI_STOPRECORD`."""
    def stutteredPageDown(self, /) -> None:
        r"""Move caret to bottom of page, or one page down if already at bottom of page.

        Sends `SCI_STUTTEREDPAGEDOWN`."""
    def stutteredPageDownExtend(self, /) -> None:
        r"""Move caret to bottom of page, or one page down if already at bottom of page, extending selection to new caret position.

        Sends `SCI_STUTTEREDPAGEDOWNEXTEND`."""
    def stutteredPageUp(self, /) -> None:
        r"""Move caret to top of page, or one page up if already at top of page.

        Sends `SCI_STUTTEREDPAGEUP`."""
    def stutteredPageUpExtend(self, /) -> None:
        r"""Move caret to top of page, or one page up if already at top of page, extending selection to new caret position.

        Sends `SCI_STUTTEREDPAGEUPEXTEND`."""
    def styleAt(self, pos: int, /) -> int:
        r"""Returns the style byte at the position.

        Sends `SCI_GETSTYLEAT`."""
    def styleBack(self, style: int, /) -> PySide6.QtGui.QColor:
        r"""Get the background colour of a style.

        Sends `SCI_STYLEGETBACK`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def styleBold(self, style: int, /) -> bool:
        r"""Get is a style bold or not.

        Sends `SCI_STYLEGETBOLD`."""
    def styleCase(self, style: int, /) -> int:
        r"""Get is a style mixed case, or to force upper or lower case.

        Sends `SCI_STYLEGETCASE`."""
    def styleChangeable(self, style: int, /) -> bool:
        r"""Get is a style changeable or not (read only). Experimental feature, currently buggy.

        Sends `SCI_STYLEGETCHANGEABLE`."""
    def styleCharacterSet(self, style: int, /) -> int:
        r"""Get the character get of the font in a style.

        Sends `SCI_STYLEGETCHARACTERSET`."""
    def styleCheckMonospaced(self, style: int, /) -> bool:
        r"""Get whether a style may be monospaced.

        Sends `SCI_STYLEGETCHECKMONOSPACED`."""
    def styleClearAll(self, /) -> None:
        r"""Clear all the styles and make equivalent to the global default style.

        Sends `SCI_STYLECLEARALL`."""
    def styleEOLFilled(self, style: int, /) -> bool:
        r"""Get is a style to have its end of line filled or not.

        Sends `SCI_STYLEGETEOLFILLED`."""
    def styleFont(self, style: int, /) -> str:
        r"""Get the font of a style. Returns the length of the fontName Result is NUL-terminated.

        Sends `SCI_STYLEGETFONT`. Returns the result instead of filling a `fontName` buffer; the message's own result (the length) is dropped."""
    def styleFore(self, style: int, /) -> PySide6.QtGui.QColor:
        r"""Get the foreground colour of a style.

        Sends `SCI_STYLEGETFORE`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def styleFromSubStyle(self, subStyle: int, /) -> int:
        r"""For a sub style, return the base style, else return the argument.

        Sends `SCI_GETSTYLEFROMSUBSTYLE`."""
    def styleHotSpot(self, style: int, /) -> bool:
        r"""Get is a style a hotspot or not.

        Sends `SCI_STYLEGETHOTSPOT`."""
    def styleIndexAt(self, pos: int, /) -> int:
        r"""Returns the unsigned style byte at the position.

        Sends `SCI_GETSTYLEINDEXAT`."""
    def styleInvisibleRepresentation(self, style: int, /) -> str:
        r"""Get the invisible representation for a style.

        Sends `SCI_STYLEGETINVISIBLEREPRESENTATION`. Returns the result instead of filling a `representation` buffer; the message's own result (the length) is dropped."""
    def styleItalic(self, style: int, /) -> bool:
        r"""Get is a style italic or not.

        Sends `SCI_STYLEGETITALIC`."""
    def styleResetDefault(self, /) -> None:
        r"""Reset the default style to its state at startup

        Sends `SCI_STYLERESETDEFAULT`."""
    def styleSetBack(self, style: int, back: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set the background colour of a style.

        Sends `SCI_STYLESETBACK`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def styleSetBold(self, style: int, bold: bool, /) -> None:
        r"""Set a style to be bold or not.

        Sends `SCI_STYLESETBOLD`."""
    def styleSetCase(self, style: int, caseVisible: int, /) -> None:
        r"""Set a style to be mixed case, or to force upper or lower case.

        Sends `SCI_STYLESETCASE`."""
    def styleSetChangeable(self, style: int, changeable: bool, /) -> None:
        r"""Set a style to be changeable or not (read only). Experimental feature, currently buggy.

        Sends `SCI_STYLESETCHANGEABLE`."""
    def styleSetCharacterSet(self, style: int, characterSet: int, /) -> None:
        r"""Set the character set of the font in a style.

        Sends `SCI_STYLESETCHARACTERSET`."""
    def styleSetCheckMonospaced(self, style: int, checkMonospaced: bool, /) -> None:
        r"""Indicate that a style may be monospaced over ASCII graphics characters which enables optimizations.

        Sends `SCI_STYLESETCHECKMONOSPACED`."""
    def styleSetEOLFilled(self, style: int, eolFilled: bool, /) -> None:
        r"""Set a style to have its end of line filled or not.

        Sends `SCI_STYLESETEOLFILLED`."""
    def styleSetFont(self, style: int, fontName: str, /) -> None:
        r"""Set the font of a style.

        Sends `SCI_STYLESETFONT`."""
    def styleSetFore(self, style: int, fore: PySide6.QtGui.QColor | str | PySide6.QtGui.QRgba64 | typing.Any | PySide6.QtCore.Qt.GlobalColor | int, /) -> None:
        r"""Set the foreground colour of a style.

        Sends `SCI_STYLESETFORE`. Uses a `QColor` (without alpha) where the message uses a packed `0xBBGGRR` int."""
    def styleSetHotSpot(self, style: int, hotspot: bool, /) -> None:
        r"""Set a style to be a hotspot or not.

        Sends `SCI_STYLESETHOTSPOT`."""
    def styleSetInvisibleRepresentation(self, style: int, representation: str, /) -> None:
        r"""Set the invisible representation for a style.

        Sends `SCI_STYLESETINVISIBLEREPRESENTATION`."""
    def styleSetItalic(self, style: int, italic: bool, /) -> None:
        r"""Set a style to be italic or not.

        Sends `SCI_STYLESETITALIC`."""
    def styleSetSize(self, style: int, sizePoints: int, /) -> None:
        r"""Set the size of characters of a style.

        Sends `SCI_STYLESETSIZE`."""
    def styleSetSizeFractional(self, style: int, sizeHundredthPoints: int, /) -> None:
        r"""Set the size of characters of a style. Size is in points multiplied by 100.

        Sends `SCI_STYLESETSIZEFRACTIONAL`."""
    def styleSetStretch(self, style: int, stretch: int, /) -> None:
        r"""Set the stretch of characters of a style.

        Sends `SCI_STYLESETSTRETCH`."""
    def styleSetUnderline(self, style: int, underline: bool, /) -> None:
        r"""Set a style to be underlined or not.

        Sends `SCI_STYLESETUNDERLINE`."""
    def styleSetVisible(self, style: int, visible: bool, /) -> None:
        r"""Set a style to be visible or not.

        Sends `SCI_STYLESETVISIBLE`."""
    def styleSetWeight(self, style: int, weight: int, /) -> None:
        r"""Set the weight of characters of a style.

        Sends `SCI_STYLESETWEIGHT`."""
    def styleSize(self, style: int, /) -> int:
        r"""Get the size of characters of a style.

        Sends `SCI_STYLEGETSIZE`."""
    def styleSizeFractional(self, style: int, /) -> int:
        r"""Get the size of characters of a style in points multiplied by 100

        Sends `SCI_STYLEGETSIZEFRACTIONAL`."""
    def styleStretch(self, style: int, /) -> int:
        r"""Get the stretch of characters of a style.

        Sends `SCI_STYLEGETSTRETCH`."""
    def styleUnderline(self, style: int, /) -> bool:
        r"""Get is a style underlined or not.

        Sends `SCI_STYLEGETUNDERLINE`."""
    def styleVisible(self, style: int, /) -> bool:
        r"""Get is a style visible or not.

        Sends `SCI_STYLEGETVISIBLE`."""
    def styleWeight(self, style: int, /) -> int:
        r"""Get the weight of characters of a style.

        Sends `SCI_STYLEGETWEIGHT`."""
    def subStyleBases(self, /) -> PySide6.QtCore.QByteArray:
        r"""Get the set of base styles that can be extended with sub styles Result is NUL-terminated.

        Sends `SCI_GETSUBSTYLEBASES`. Returns the result instead of filling a `styles` buffer; the message's own result (the length) is dropped."""
    def subStylesLength(self, styleBase: int, /) -> int:
        r"""The number of sub styles associated with a base style

        Sends `SCI_GETSUBSTYLESLENGTH`."""
    def subStylesStart(self, styleBase: int, /) -> int:
        r"""The starting style number for the sub styles associated with a base style

        Sends `SCI_GETSUBSTYLESSTART`."""
    def supportsFeature(self, feature: int, /) -> bool:
        r"""Get whether a feature is supported

        Sends `SCI_SUPPORTSFEATURE`."""
    def swapMainAnchorCaret(self, /) -> None:
        r"""Swap that caret and anchor of the main selection.

        Sends `SCI_SWAPMAINANCHORCARET`."""
    def tab(self, /) -> None:
        r"""If selection is empty or all on one line replace the selection with a tab character. If more than one line selected, indent the lines.

        Sends `SCI_TAB`."""
    def tabDrawMode(self, /) -> int:
        r"""Retrieve the current tab draw mode. Returns one of SCTD_* constants.

        Sends `SCI_GETTABDRAWMODE`."""
    def tabIndents(self, /) -> bool:
        r"""Does a tab pressed when caret is within indentation indent?

        Sends `SCI_GETTABINDENTS`."""
    def tabMinimumWidth(self, /) -> int:
        r"""Get the minimum visual width of a tab.

        Sends `SCI_GETTABMINIMUMWIDTH`."""
    def tabWidth(self, /) -> int:
        r"""Retrieve the visible size of a tab.

        Sends `SCI_GETTABWIDTH`."""
    def tag(self, tagNumber: int, /) -> str:
        r"""Retrieve the value of a tag from a regular expression search. Result is NUL-terminated.

        Sends `SCI_GETTAG`. Returns the result instead of filling a `tagValue` buffer; the message's own result (the length) is dropped."""
    def tagsOfStyle(self, style: int, /) -> str:
        r"""Retrieve a ' ' separated list of style tags like "literal quoted string". Result is NUL-terminated.

        Sends `SCI_TAGSOFSTYLE`. Returns the result instead of filling a `tags` buffer; the message's own result (the length) is dropped."""
    def targetEnd(self, /) -> int:
        r"""Get the position that ends the target.

        Sends `SCI_GETTARGETEND`."""
    def targetEndVirtualSpace(self, /) -> int:
        r"""Get the virtual space of the target end

        Sends `SCI_GETTARGETENDVIRTUALSPACE`."""
    def targetFromSelection(self, /) -> None:
        r"""Make the target range start and end be the same as the selection range start and end.

        Sends `SCI_TARGETFROMSELECTION`."""
    def targetStart(self, /) -> int:
        r"""Get the position that starts the target.

        Sends `SCI_GETTARGETSTART`."""
    def targetStartVirtualSpace(self, /) -> int:
        r"""Get the virtual space of the target start

        Sends `SCI_GETTARGETSTARTVIRTUALSPACE`."""
    def targetText(self, /) -> str:
        r"""Retrieve the text in the target.

        Sends `SCI_GETTARGETTEXT`. Returns the result instead of filling a `text` buffer; the message's own result (the length) is dropped."""
    def targetWholeDocument(self, /) -> None:
        r"""Sets the target to the whole document.

        Sends `SCI_TARGETWHOLEDOCUMENT`."""
    def technology(self, /) -> int:
        r"""Get the tech.

        Sends `SCI_GETTECHNOLOGY`."""
    def textHeight(self, line: int, /) -> int:
        r"""Retrieve the height of a particular line of text in pixels.

        Sends `SCI_TEXTHEIGHT`."""
    def textLength(self, /) -> int:
        r"""Retrieve the number of characters in the document.

        Sends `SCI_GETTEXTLENGTH`."""
    def textRange(self, start: int, end: int, /) -> str:
        r"""Alias for `get_text_range`."""
    def textWidth(self, style: int, text: str, /) -> int:
        r"""Measure the pixel width of some text in a particular style. NUL terminated text argument. Does not handle tab or control characters.

        Sends `SCI_TEXTWIDTH`."""
    def toggleCaretSticky(self, /) -> None:
        r"""Switch between sticky and non-sticky: meant to be bound to a key.

        Sends `SCI_TOGGLECARETSTICKY`."""
    def toggleFold(self, line: int, /) -> None:
        r"""Switch a header line between expanded and contracted.

        Sends `SCI_TOGGLEFOLD`."""
    def toggleFoldShowText(self, line: int, text: str, /) -> None:
        r"""Switch a header line between expanded and contracted and show some text after the line.

        Sends `SCI_TOGGLEFOLDSHOWTEXT`."""
    def undo(self, /) -> None:
        r"""Undo one action in the undo history.

        Sends `SCI_UNDO`."""
    def undoActionPosition(self, action: int, /) -> int:
        r"""What is the position of an action?

        Sends `SCI_GETUNDOACTIONPOSITION`."""
    def undoActionText(self, action: int, /) -> str:
        r"""What is the text of an action?

        Sends `SCI_GETUNDOACTIONTEXT`. Returns the result instead of filling a `text` buffer; the message's own result (the length) is dropped."""
    def undoActionType(self, action: int, /) -> int:
        r"""What is the type of an action?

        Sends `SCI_GETUNDOACTIONTYPE`."""
    def undoActions(self, /) -> int:
        r"""How many undo actions are in the history?

        Sends `SCI_GETUNDOACTIONS`."""
    def undoCollection(self, /) -> bool:
        r"""Is undo history being collected?

        Sends `SCI_GETUNDOCOLLECTION`."""
    def undoCurrent(self, /) -> int:
        r"""Which action is the current point?

        Sends `SCI_GETUNDOCURRENT`."""
    def undoDetach(self, /) -> int:
        r"""Which action is the detach point?

        Sends `SCI_GETUNDODETACH`."""
    def undoSavePoint(self, /) -> int:
        r"""Which action is the save point?

        Sends `SCI_GETUNDOSAVEPOINT`."""
    def undoSelectionHistory(self, /) -> int:
        r"""Report undo selection history status.

        Sends `SCI_GETUNDOSELECTIONHISTORY`."""
    def undoSequence(self, /) -> int:
        r"""Is an undo sequence active?

        Sends `SCI_GETUNDOSEQUENCE`."""
    def undoTentative(self, /) -> int:
        r"""Which action is the tentative point?

        Sends `SCI_GETUNDOTENTATIVE`."""
    def upperCase(self, /) -> None:
        r"""Transform the selection to upper case.

        Sends `SCI_UPPERCASE`."""
    def usePopUp(self, popUpMode: int, /) -> None:
        r"""Set whether a pop up menu is displayed automatically when the user presses the wrong mouse button on certain areas.

        Sends `SCI_USEPOPUP`."""
    def useTabs(self, /) -> bool:
        r"""Retrieve whether tabs will be used in indentation.

        Sends `SCI_GETUSETABS`."""
    def userListShow(self, listType: int, itemList: str, /) -> None:
        r"""Display a list of strings and send notification when user chooses one.

        Sends `SCI_USERLISTSHOW`."""
    def vCHome(self, /) -> None:
        r"""Move caret to before first visible character on line. If already there move to first character on line.

        Sends `SCI_VCHOME`."""
    def vCHomeDisplay(self, /) -> None:
        r"""Move caret to before first visible character on display line. If already there move to first character on display line.

        Sends `SCI_VCHOMEDISPLAY`."""
    def vCHomeDisplayExtend(self, /) -> None:
        r"""Like VCHomeDisplay but extending selection to new caret position.

        Sends `SCI_VCHOMEDISPLAYEXTEND`."""
    def vCHomeExtend(self, /) -> None:
        r"""Like VCHome but extending selection to new caret position.

        Sends `SCI_VCHOMEEXTEND`."""
    def vCHomeRectExtend(self, /) -> None:
        r"""Move caret to before first visible character on line. If already there move to first character on line. In either case, extend rectangular selection to new caret position.

        Sends `SCI_VCHOMERECTEXTEND`."""
    def vCHomeWrap(self, /) -> None:
        r"""Like VCHome but when word-wrap is enabled goes first to start of display line VCHomeDisplay, then behaves like VCHome.

        Sends `SCI_VCHOMEWRAP`."""
    def vCHomeWrapExtend(self, /) -> None:
        r"""Like VCHomeExtend but when word-wrap is enabled extends first to start of display line VCHomeDisplayExtend, then behaves like VCHomeExtend.

        Sends `SCI_VCHOMEWRAPEXTEND`."""
    def vScrollBar(self, /) -> bool:
        r"""Is the vertical scroll bar visible?

        Sends `SCI_GETVSCROLLBAR`."""
    def verticalCentreCaret(self, /) -> None:
        r"""Centre current line in window.

        Sends `SCI_VERTICALCENTRECARET`."""
    def viewEOL(self, /) -> bool:
        r"""Are the end of line characters visible?

        Sends `SCI_GETVIEWEOL`."""
    def viewWS(self, /) -> int:
        r"""Are white space characters currently visible? Returns one of SCWS_* constants.

        Sends `SCI_GETVIEWWS`."""
    def virtualSpaceOptions(self, /) -> int:
        r"""Return options for virtual space behaviour.

        Sends `SCI_GETVIRTUALSPACEOPTIONS`."""
    def visibleFromDocLine(self, docLine: int, /) -> int:
        r"""Find the display line of a document line taking hidden lines into account.

        Sends `SCI_VISIBLEFROMDOCLINE`."""
    def whitespaceChars(self, /) -> str:
        r"""Get the set of characters making up whitespace for when moving or selecting by word.

        Sends `SCI_GETWHITESPACECHARS`. Returns the result instead of filling a `characters` buffer; the message's own result (the length) is dropped."""
    def whitespaceSize(self, /) -> int:
        r"""Get the size of the dots used to mark space characters.

        Sends `SCI_GETWHITESPACESIZE`."""
    def wordChars(self, /) -> str:
        r"""Get the set of characters making up words for when moving or selecting by word. Returns the number of characters

        Sends `SCI_GETWORDCHARS`. Returns the result instead of filling a `characters` buffer; the message's own result (the length) is dropped."""
    def wordEndPosition(self, pos: int, onlyWordCharacters: bool, /) -> int:
        r"""Get position of end of word.

        Sends `SCI_WORDENDPOSITION`."""
    def wordLeft(self, /) -> None:
        r"""Move caret left one word.

        Sends `SCI_WORDLEFT`."""
    def wordLeftEnd(self, /) -> None:
        r"""Move caret left one word, position cursor at end of word.

        Sends `SCI_WORDLEFTEND`."""
    def wordLeftEndExtend(self, /) -> None:
        r"""Move caret left one word, position cursor at end of word, extending selection to new caret position.

        Sends `SCI_WORDLEFTENDEXTEND`."""
    def wordLeftExtend(self, /) -> None:
        r"""Move caret left one word extending selection to new caret position.

        Sends `SCI_WORDLEFTEXTEND`."""
    def wordPartLeft(self, /) -> None:
        r"""Move to the previous change in capitalisation.

        Sends `SCI_WORDPARTLEFT`."""
    def wordPartLeftExtend(self, /) -> None:
        r"""Move to the previous change in capitalisation extending selection to new caret position.

        Sends `SCI_WORDPARTLEFTEXTEND`."""
    def wordPartRight(self, /) -> None:
        r"""Move to the change next in capitalisation.

        Sends `SCI_WORDPARTRIGHT`."""
    def wordPartRightExtend(self, /) -> None:
        r"""Move to the next change in capitalisation extending selection to new caret position.

        Sends `SCI_WORDPARTRIGHTEXTEND`."""
    def wordRight(self, /) -> None:
        r"""Move caret right one word.

        Sends `SCI_WORDRIGHT`."""
    def wordRightEnd(self, /) -> None:
        r"""Move caret right one word, position cursor at end of word.

        Sends `SCI_WORDRIGHTEND`."""
    def wordRightEndExtend(self, /) -> None:
        r"""Move caret right one word, position cursor at end of word, extending selection to new caret position.

        Sends `SCI_WORDRIGHTENDEXTEND`."""
    def wordRightExtend(self, /) -> None:
        r"""Move caret right one word extending selection to new caret position.

        Sends `SCI_WORDRIGHTEXTEND`."""
    def wordStartPosition(self, pos: int, onlyWordCharacters: bool, /) -> int:
        r"""Get position of start of word.

        Sends `SCI_WORDSTARTPOSITION`."""
    def wrapCount(self, docLine: int, /) -> int:
        r"""The number of display lines needed to wrap a document line

        Sends `SCI_WRAPCOUNT`."""
    def wrapIndentMode(self, /) -> int:
        r"""Retrieve how wrapped sublines are placed. Default is fixed.

        Sends `SCI_GETWRAPINDENTMODE`."""
    def wrapMode(self, /) -> int:
        r"""Retrieve whether text is word wrapped.

        Sends `SCI_GETWRAPMODE`."""
    def wrapStartIndent(self, /) -> int:
        r"""Retrive the start indent for wrapped lines.

        Sends `SCI_GETWRAPSTARTINDENT`."""
    def wrapVisualFlags(self, /) -> int:
        r"""Retrive the display mode of visual flags for wrapped lines.

        Sends `SCI_GETWRAPVISUALFLAGS`."""
    def wrapVisualFlagsLocation(self, /) -> int:
        r"""Retrive the location of visual flags for wrapped lines.

        Sends `SCI_GETWRAPVISUALFLAGSLOCATION`."""
    def xOffset(self, /) -> int:
        r"""Get the xOffset (ie, horizontal scroll position).

        Sends `SCI_GETXOFFSET`."""
    def zoom(self, /) -> int:
        r"""Retrieve the zoom level.

        Sends `SCI_GETZOOM`."""
    def zoomIn(self, /) -> None:
        r"""Magnify the displayed text by increasing the sizes by 1 point.

        Sends `SCI_ZOOMIN`."""
    def zoomOut(self, /) -> None:
        r"""Make the displayed text smaller by decreasing the sizes by 1 point.

        Sends `SCI_ZOOMOUT`."""


# eof
