"""The QColor contract of the typed API (issue #17).

Scintilla's `colour` messages take a packed 0xBBGGRR int and its `colouralpha`
ones 0xAABBGGRR -- the opposite byte order from Qt's 0xAARRGGBB. ScintillaEdit
takes and returns QColor instead, converting exactly; the raw `send` keeps
Scintilla's ints.
"""

from typing import Final

import pytest
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from pytestqt.qtbot import QtBot

from pyside6_scintilla import Scintilla, ScintillaEdit, colour_from_scintilla, colour_to_scintilla

STYLE: Final = Scintilla.StylesCommon.Default


@pytest.fixture
def editor(qtbot: QtBot) -> ScintillaEdit:
    """A fresh editor."""
    widget = ScintillaEdit()
    qtbot.addWidget(widget)
    return widget


def test_colour_round_trips_as_qcolor(editor: ScintillaEdit) -> None:
    """styleSetFore/styleFore take and return a QColor."""
    editor.styleSetFore(STYLE, QColor(0x12, 0x34, 0x56))

    assert editor.styleFore(STYLE) == QColor(0x12, 0x34, 0x56)


def test_colour_reaches_scintilla_in_its_byte_order(editor: ScintillaEdit) -> None:
    """Red is 0x0000FF to Scintilla (red in the low byte), not Qt's 0xFF0000."""
    editor.styleSetFore(STYLE, QColor(Qt.GlobalColor.red))

    assert editor.send(Scintilla.Message.StyleGetFore, STYLE) == 0x0000FF


def test_plain_colour_ignores_alpha_and_returns_opaque(editor: ScintillaEdit) -> None:
    """A `colour` message has no alpha: it's dropped on the way in, opaque on the way out."""
    editor.styleSetBack(STYLE, QColor(10, 20, 30, 40))

    assert editor.send(Scintilla.Message.StyleGetBack, STYLE) == 0x1E140A
    assert editor.styleBack(STYLE) == QColor(10, 20, 30, 255)


def test_colour_alpha_round_trips_with_alpha(editor: ScintillaEdit) -> None:
    """A `colouralpha` message keeps the alpha, packed as 0xAABBGGRR."""
    element = Scintilla.Element.Caret
    editor.setElementColour(element, QColor(0x11, 0x22, 0x33, 0x44))

    assert editor.send(Scintilla.Message.GetElementColour, element) == 0x44332211
    assert editor.elementColour(element) == QColor(0x11, 0x22, 0x33, 0x44)


def test_global_colours_are_accepted(editor: ScintillaEdit) -> None:
    """Qt.GlobalColor converts to QColor, as everywhere in PySide6."""
    editor.styleSetFore(STYLE, Qt.GlobalColor.blue)

    assert editor.styleFore(STYLE) == QColor(Qt.GlobalColor.blue)


def test_ints_are_qt_rgb_not_scintilla_packed(editor: ScintillaEdit) -> None:
    """An int converts to QColor as everywhere in PySide6: Qt's 0xRRGGBB, alpha dropped.

    Deliberately kept (issue #17): consistent with Qt, at the cost that code
    written for the old API, passing Scintilla's 0xBBGGRR ints, now gets red
    and blue swapped. send() still takes Scintilla's packed ints.
    """
    editor.styleSetFore(STYLE, 0xFF0000)
    assert editor.styleFore(STYLE) == QColor(Qt.GlobalColor.red)

    editor.setElementColour(Scintilla.Element.Caret, 0x80FF0000)
    assert editor.elementColour(Scintilla.Element.Caret) == QColor(255, 0, 0, 255)


@pytest.mark.parametrize(
    ("colour", "alpha", "packed"),
    [
        ("#00ff00", False, 0x00FF00),
        ("red", False, 0x0000FF),
        (Qt.GlobalColor.blue, False, 0xFF0000),
        (QColor(0x11, 0x22, 0x33), False, 0x332211),
        (QColor(0x11, 0x22, 0x33, 0x44), False, 0x332211),
        (QColor(0x11, 0x22, 0x33, 0x44), True, 0x44332211),
    ],
)
def test_colour_to_scintilla_packs_in_scintilla_byte_order(
    colour: QColor | Qt.GlobalColor | str, alpha: bool, packed: int
) -> None:
    """Names, global colours and QColors pack to 0xBBGGRR (0xAABBGGRR with alpha)."""
    assert colour_to_scintilla(colour, alpha) == packed


def test_colour_from_scintilla_is_the_inverse() -> None:
    """Unpacking restores the colour; without alpha the result is opaque."""
    assert colour_from_scintilla(0x332211) == QColor(0x11, 0x22, 0x33)
    assert colour_from_scintilla(0x44332211) == QColor(0x11, 0x22, 0x33)
    assert colour_from_scintilla(0x44332211, alpha=True) == QColor(0x11, 0x22, 0x33, 0x44)


def test_colour_helpers_match_the_typed_methods(editor: ScintillaEdit) -> None:
    """The helpers agree with what the typed methods send and read back."""
    editor.styleSetFore(STYLE, QColor("#123456"))

    assert editor.send(Scintilla.Message.StyleGetFore, STYLE) == colour_to_scintilla("#123456")
    editor.send(Scintilla.Message.StyleSetBack, STYLE, colour_to_scintilla("#abcdef"))
    assert editor.styleBack(STYLE) == colour_from_scintilla(colour_to_scintilla("#abcdef"))


def test_colour_to_scintilla_rejects_ints_and_invalid_colours() -> None:
    """An int is ambiguous (which byte order?) and an unknown name is an error, not black."""
    with pytest.raises(TypeError):
        colour_to_scintilla(0xFF0000)  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="nonsense"):
        colour_to_scintilla("nonsense")
