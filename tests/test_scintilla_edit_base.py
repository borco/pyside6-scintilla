from pyside6_scintilla import Scintilla, ScintillaEditBase


def test_set_and_get_text_length(qtbot):
    editor = ScintillaEditBase()
    qtbot.addWidget(editor)

    editor.sends(int(Scintilla.Message.SetText), 0, "hello")

    assert editor.send(int(Scintilla.Message.GetTextLength)) == len("hello")
