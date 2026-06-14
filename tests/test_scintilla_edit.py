"""Smoke test for the ScintillaEdit binding.

Confirms ScintillaEdit's typed per-message methods (generated from
Scintilla.iface, one per SCI_* message) work end to end on top of the same
compiled extension/vendored Scintilla core as ScintillaEditBase.
"""

from pyside6_scintilla import ScintillaEdit


def test_set_and_get_text(qtbot):
    """setText() followed by textLength()/getText() round trips the text."""
    editor = ScintillaEdit()
    qtbot.addWidget(editor)

    editor.setText("hello")

    assert editor.textLength() == len("hello")
    assert bytes(editor.getText(editor.textLength())) == b"hello"


def test_line_from_position_and_select_all(qtbot):
    """lineFromPosition() and selectAll() behave as expected on multi-line text."""
    editor = ScintillaEdit()
    qtbot.addWidget(editor)

    editor.setText("first\nsecond\nthird")

    assert editor.lineFromPosition(0) == 0
    assert editor.lineFromPosition(editor.textLength()) == 2

    editor.selectAll()

    assert editor.selectionStart() == 0
    assert editor.selectionEnd() == editor.textLength()
