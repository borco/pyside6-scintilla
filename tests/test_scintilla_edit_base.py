"""Smoke test for the ScintillaEditBase binding.

Confirms the compiled extension, the vendored Scintilla core, and the
send()/sends() message round trip all work end to end.
"""

from pytest_mock import MockerFixture
from pytestqt.qtbot import QtBot

from pyside6_scintilla import Scintilla, ScintillaEditBase


def test_set_and_get_text_length(qtbot: QtBot) -> None:
    """SCI_SETTEXT followed by SCI_GETTEXTLENGTH returns the set text's length."""
    editor = ScintillaEditBase()
    qtbot.addWidget(editor)

    editor.sends(int(Scintilla.Message.SetText), 0, "hello")

    assert editor.send(int(Scintilla.Message.GetTextLength)) == len("hello")


def test_modified_signal_reaches_python_slot(qtbot: QtBot, mocker: MockerFixture) -> None:
    """ScintillaEditBase.modified carries Scintilla::Position/ModificationFlags
    /FoldLevel-typed parameters. A Python slot connected to it must actually
    receive the emission instead of the connection silently failing."""
    editor = ScintillaEditBase()
    qtbot.addWidget(editor)

    slot = mocker.Mock()
    editor.modified.connect(slot)

    editor.sends(int(Scintilla.Message.SetText), 0, "hello")

    assert slot.called
