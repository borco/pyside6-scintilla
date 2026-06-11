"""Smoke test for the ScintillaEditBase binding.

Confirms the compiled extension, the vendored Scintilla core, and the
send()/sends() message round trip all work end to end.
"""

from pyside6_scintilla import Scintilla, ScintillaEditBase


def test_set_and_get_text_length(qtbot):
    """SCI_SETTEXT followed by SCI_GETTEXTLENGTH returns the set text's length."""
    editor = ScintillaEditBase()
    qtbot.addWidget(editor)

    editor.sends(int(Scintilla.Message.SetText), 0, "hello")

    assert editor.send(int(Scintilla.Message.GetTextLength)) == len("hello")
