"""SCI_SETSCALETECHNIQUE and the logical-pixel conversion of ScintillaEdit's pixel methods.

Since Scintilla 5.6.4, Scintilla.iface types pixel values as `pixels`, and
under `ScaleTechnique.PixelAligned` (Qt only) the engine works in device
pixels. The generated pixel methods take/return logical pixels, scaling by
the viewport's "ScintillaScale" property, and each has a `...F` float twin
(see tools/generate_scintilla_edit.py).
"""

from pytestqt.qtbot import QtBot

from pyside6_scintilla import Scintilla, ScintillaEdit

MESSAGE = Scintilla.Message


def test_scale_technique_round_trips(qtbot: QtBot) -> None:
    """setScaleTechnique()/scaleTechnique() round trip, and agree with the raw messages."""
    editor = ScintillaEdit()
    qtbot.addWidget(editor)

    assert editor.scaleTechnique() == Scintilla.ScaleTechnique.Default

    editor.setScaleTechnique(Scintilla.ScaleTechnique.PixelAligned)

    assert editor.scaleTechnique() == Scintilla.ScaleTechnique.PixelAligned
    assert editor.send(MESSAGE.GetScaleTechnique) == Scintilla.ScaleTechnique.PixelAligned

    editor.send(MESSAGE.SetScaleTechnique, Scintilla.ScaleTechnique.Default)

    assert editor.scaleTechnique() == Scintilla.ScaleTechnique.Default


def test_scale_property_follows_the_technique(qtbot: QtBot) -> None:
    """ScintillaQt sets "ScintillaScale" to the device-pixel ratio only under PixelAligned."""
    editor = ScintillaEdit()
    qtbot.addWidget(editor)

    assert editor.viewport().property("ScintillaScale") == 0.0

    editor.setScaleTechnique(Scintilla.ScaleTechnique.PixelAligned)

    assert editor.viewport().property("ScintillaScale") == editor.devicePixelRatioF()


def test_pixel_methods_are_unscaled_by_default(qtbot: QtBot) -> None:
    """With the default technique, typed pixel methods pass values through unchanged."""
    editor = ScintillaEdit()
    qtbot.addWidget(editor)

    editor.setMarginWidthN(0, 40)

    assert editor.marginWidthN(0) == 40
    assert editor.send(MESSAGE.GetMarginWidthN, 0) == 40
    assert editor.marginWidthNF(0) == 40.0


def test_pixel_methods_convert_logical_to_device_pixels(qtbot: QtBot) -> None:
    """Under a scale, typed methods take/return logical pixels while send() sees device pixels.

    The offscreen test platform's device-pixel ratio is 1, so this sets the
    "ScintillaScale" property the generated methods read directly. Nothing
    repaints the hidden widget in between, so ScintillaQt doesn't reset it.
    """
    editor = ScintillaEdit()
    qtbot.addWidget(editor)
    editor.setScaleTechnique(Scintilla.ScaleTechnique.PixelAligned)
    editor.viewport().setProperty("ScintillaScale", 2.0)

    editor.setMarginWidthN(0, 40)

    assert editor.send(MESSAGE.GetMarginWidthN, 0) == 80
    assert editor.marginWidthN(0) == 40

    editor.send(MESSAGE.SetMarginWidthN, 0, 81)

    assert editor.marginWidthN(0) == 41  # 40.5, rounded half away from zero
    assert editor.marginWidthNF(0) == 40.5

    editor.setMarginWidthNF(0, 20.75)

    assert editor.send(MESSAGE.GetMarginWidthN, 0) == 42  # 41.5 device pixels, rounded


def test_float_twin_measures_text(qtbot: QtBot) -> None:
    """textWidthF() returns a float matching textWidth() when unscaled."""
    editor = ScintillaEdit()
    qtbot.addWidget(editor)

    width = editor.textWidthF(Scintilla.StylesCommon.LineNumber, "99999")

    assert isinstance(width, float)
    assert width > 0
    assert width == editor.textWidth(Scintilla.StylesCommon.LineNumber, "99999")
