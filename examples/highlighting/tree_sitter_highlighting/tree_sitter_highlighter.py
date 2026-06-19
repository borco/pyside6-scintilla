"""Drives ScintillaEdit styling and folding from a tree-sitter grammar.

pyside6-scintilla doesn't wrap a lexer binding, so there's no SCI_SETLEXER
to flip on. TreeSitterHighlighter instead re-parses the editor's text with a
tree-sitter Language on every edit, then:

- runs a highlight Query over the resulting tree and applies the captured
  node ranges manually via ScintillaEdit's raw SCI_STYLE* messages
  (styleSetFore(), startStyling(), setStyling(), ...);
- walks the tree's "block" nodes (the indented body of any compound
  statement - function/class bodies, if/for/while/etc.) to compute each
  line's fold level and applies it via setFoldLevel(), the same message a
  real lexer would drive folding with.

Has no dependencies beyond pyside6-scintilla, tree-sitter and a tree-sitter
language package - copy this file straight into your own project.
"""

from typing import Final

from PySide6.QtCore import QObject
from PySide6.QtGui import QFont
from tree_sitter import Language, Node, Parser, Query, QueryCursor

from pyside6_scintilla import Scintilla, ScintillaEdit

# Style numbers below Scintilla.StylesCommon.Default (32) are free for our
# own use.
STYLE_DEFAULT: Final = 0
STYLE_KEYWORD: Final = 1
STYLE_FUNCTION: Final = 2
STYLE_CLASS: Final = 3
STYLE_STRING: Final = 4
STYLE_NUMBER: Final = 5
STYLE_COMMENT: Final = 6

# Maps a highlight query's @capture name to one of the style numbers above.
# Captures with no entry here (or not captured at all) fall back to
# STYLE_DEFAULT.
CAPTURE_STYLES: Final = {
    "keyword": STYLE_KEYWORD,
    "function": STYLE_FUNCTION,
    "class": STYLE_CLASS,
    "string": STYLE_STRING,
    "number": STYLE_NUMBER,
    "comment": STYLE_COMMENT,
}

# (red, green, blue) per style -- packed to Scintilla's 0xBBGGRR colour
# format by rgb() below, at the point of use.
STYLE_COLORS: Final = {
    STYLE_DEFAULT: (0x00, 0x00, 0x00),
    STYLE_KEYWORD: (0x00, 0x00, 0x80),
    STYLE_FUNCTION: (0x00, 0x60, 0x60),
    STYLE_CLASS: (0x00, 0x60, 0x60),
    STYLE_STRING: (0x00, 0x80, 0x00),
    STYLE_NUMBER: (0x80, 0x00, 0x80),
    STYLE_COMMENT: (0x80, 0x80, 0x80),
}


def rgb(red: int, green: int, blue: int) -> int:
    """Pack an 8-bit RGB triple into Scintilla's 0xBBGGRR colour format."""
    return red | (green << 8) | (blue << 16)


# Fold margin - the second default margin (index 0 is the line-number
# margin in the simple_scintilla_* examples; here it's unused/zero-width,
# but margin 1 is what Scintilla creates with the SC_MARGIN_SYMBOL type and
# a non-zero width out of the box).
MARGIN_FOLD: Final = 1

# Marker symbol and fold-marker-slot constants below aren't exposed as
# enums by this binding (it only wraps the messages, not Scintilla.iface's
# named constants) - these are SC_MARK_* / SC_MARKNUM_* from Scintilla.h.
_SC_MARK_VLINE: Final = 9
_SC_MARK_LCORNER: Final = 10
_SC_MARK_TCORNER: Final = 11
_SC_MARK_BOXPLUS: Final = 12
_SC_MARK_BOXPLUSCONNECTED: Final = 13
_SC_MARK_BOXMINUS: Final = 14
_SC_MARK_BOXMINUSCONNECTED: Final = 15

_SC_MARKNUM_FOLDEREND: Final = 25
_SC_MARKNUM_FOLDEROPENMID: Final = 26
_SC_MARKNUM_FOLDERMIDTAIL: Final = 27
_SC_MARKNUM_FOLDERTAIL: Final = 28
_SC_MARKNUM_FOLDERSUB: Final = 29
_SC_MARKNUM_FOLDER: Final = 30
_SC_MARKNUM_FOLDEROPEN: Final = 31

# The classic "boxes" fold-margin marker set (as seen in SciTE/Notepad++).
FOLD_MARKERS: Final = {
    _SC_MARKNUM_FOLDEROPEN: _SC_MARK_BOXMINUS,
    _SC_MARKNUM_FOLDER: _SC_MARK_BOXPLUS,
    _SC_MARKNUM_FOLDERSUB: _SC_MARK_VLINE,
    _SC_MARKNUM_FOLDERTAIL: _SC_MARK_LCORNER,
    _SC_MARKNUM_FOLDEREND: _SC_MARK_BOXPLUSCONNECTED,
    _SC_MARKNUM_FOLDEROPENMID: _SC_MARK_BOXMINUSCONNECTED,
    _SC_MARKNUM_FOLDERMIDTAIL: _SC_MARK_TCORNER,
}

# SC_AUTOMATICFOLD_SHOW | SC_AUTOMATICFOLD_CLICK: show the fold margin and
# let clicking it toggle the fold, without wiring up the marginClicked
# signal by hand.
_AUTOMATIC_FOLD_SHOW_AND_CLICK: Final = 0x0001 | 0x0002

# tree-sitter-python node type for the indented body of any compound
# statement (function/class definitions, if/for/while/try/with/...).
_BLOCK_NODE_TYPE: Final = "block"


def fold_levels(root: Node, line_count: int) -> list[int]:
    """Compute each line's fold *level* (nesting depth) from a parse tree.

    A line's depth is the number of "block" nodes (indented suites) that
    span it - summing over all such ancestors gives the nesting depth
    directly, with no need to track depth while recursing.
    """
    depths = [0] * line_count
    stack = [root]
    while stack:
        node = stack.pop()
        if node.type == _BLOCK_NODE_TYPE and node.parent is not None:
            # Count from right after the header line to the block's last
            # line, ignoring the block node's own start row - it skips
            # leading comments between the header's ":" and the first real
            # statement (tree-sitter attaches those as siblings, not block
            # children), which would otherwise be missed. For one-liners
            # ("if x: pass", block on the header's own row), start_row ends
            # up past end_row, so the (empty) range contributes no depth.
            header_row = node.parent.start_point[0]
            for row in range(header_row + 1, min(node.end_point[0], line_count - 1) + 1):
                depths[row] += 1
        stack.extend(node.children)
    return depths


class TreeSitterHighlighter(QObject):
    """Keeps a ScintillaEdit's styling in sync with a tree-sitter parse tree.

    Pass parent (e.g. the window that owns editor) to tie its lifetime to
    that QObject -- then there's no need for the caller to keep an explicit
    reference around just to stop it from being garbage-collected.

    Re-parses, re-queries and re-folds the whole buffer on every edit,
    which is fine at example/small-file scale but wouldn't scale to large
    files - a production version would use tree-sitter's incremental
    parsing (Parser.parse(..., old_tree=...)) and restyle/refold only the
    changed range.
    """

    def __init__(
        self,
        editor: ScintillaEdit,
        language: Language,
        highlights_query: str,
        font: QFont | None = None,
        parent: QObject | None = None,
    ) -> None:
        super().__init__(parent)
        self.__editor: Final = editor
        self.__parser: Final = Parser(language)
        self.__query: Final = Query(language, highlights_query)
        self.__connected = False

        for style, (red, green, blue) in STYLE_COLORS.items():
            if font is not None:
                editor.styleSetFont(style, font.family())
            editor.styleSetFore(style, rgb(red, green, blue))
        editor.styleSetBold(STYLE_KEYWORD, True)
        editor.styleSetItalic(STYLE_COMMENT, True)

        editor.setMarginTypeN(MARGIN_FOLD, Scintilla.MarginType.Symbol)
        editor.setMarginMaskN(MARGIN_FOLD, Scintilla.MaskFolders)
        editor.setMarginWidthN(MARGIN_FOLD, 16)
        editor.setMarginSensitiveN(MARGIN_FOLD, True)
        for marker_number, marker_symbol in FOLD_MARKERS.items():
            editor.markerDefine(marker_number, marker_symbol)
        editor.setAutomaticFold(_AUTOMATIC_FOLD_SHOW_AND_CLICK)

        self.rehighlight()
        self.__set_connected(True)

    def rehighlight(self) -> None:
        """Re-parse and re-query the editor's full current text, then restyle and refold it."""
        editor = self.__editor
        self.__set_connected(False)
        try:
            source = editor.getText(editor.textLength()).data()
            tree = self.__parser.parse(source)

            ranges: list[tuple[int, int, int]] = []
            for capture, nodes in QueryCursor(self.__query).captures(tree.root_node).items():
                style = CAPTURE_STYLES.get(capture, STYLE_DEFAULT)
                ranges.extend((node.start_byte, node.end_byte, style) for node in nodes)
            ranges.sort(key=lambda range_: range_[0])

            editor.startStyling(0, 0)
            position = 0
            for start_byte, end_byte, style in ranges:
                # Later, overlapping or out-of-order captures (e.g. a keyword
                # token inside an already-styled node) are skipped rather than
                # corrected - good enough for an example highlighter.
                if start_byte < position:
                    continue
                if start_byte > position:
                    editor.setStyling(start_byte - position, STYLE_DEFAULT)
                editor.setStyling(end_byte - start_byte, style)
                position = end_byte
            if position < len(source):
                editor.setStyling(len(source) - position, STYLE_DEFAULT)

            line_count = editor.lineCount()
            depths = fold_levels(tree.root_node, line_count)
            for line, depth in enumerate(depths):
                level = Scintilla.FoldLevel.Base + depth
                if line + 1 < line_count and depths[line + 1] > depth:
                    level |= Scintilla.FoldLevel.HeaderFlag
                editor.setFoldLevel(line, level)
        finally:
            self.__set_connected(True)

    def __set_connected(self, connected: bool) -> None:
        if connected == self.__connected:
            return
        if connected:
            self.__editor.modified.connect(self.__on_modified)
        else:
            self.__editor.modified.disconnect(self.__on_modified)
        self.__connected = connected

    def __on_modified(self, *_args: object) -> None:
        self.rehighlight()
