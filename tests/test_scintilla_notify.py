"""Lifetime/safety checks for NotificationData, delivered via notify().

ScintillaEditBase.notify(NotificationData *pscn) hands Python a wrapper
around a transient C++ struct that Scintilla reuses across notifications.
Reading a field (e.g. text) during the handler call copies it into a normal
Python object (str for text), which remains valid afterwards. But the
NotificationData wrapper itself must not be retained past the handler: once
later notifications overwrite the underlying struct, its fields no longer
reflect the notification it was received for.
"""

from pytestqt.qtbot import QtBot

from pyside6_scintilla import Scintilla, ScintillaEdit


def test_text_field_is_a_safe_copy_at_access_time(qtbot: QtBot) -> None:
    """NotificationData.text, read during the handler, is an independent str."""
    editor = ScintillaEdit()
    qtbot.addWidget(editor)

    captured_text: str | None = None

    def on_notify(nd: Scintilla.NotificationData) -> None:
        nonlocal captured_text
        if nd.modificationType & int(Scintilla.ModificationFlags.InsertText) and nd.text:
            captured_text = nd.text

    editor.notify.connect(on_notify)
    editor.insertText(0, "hello")

    assert captured_text == "hello"


def test_notification_data_must_not_be_retained_past_the_handler(qtbot: QtBot) -> None:
    """A NotificationData kept after notify() returns reflects later state, not
    a snapshot of the notification it was delivered with."""
    editor = ScintillaEdit()
    qtbot.addWidget(editor)

    retained: list[Scintilla.NotificationData] = []

    def on_notify(nd: Scintilla.NotificationData) -> None:
        if nd.modificationType & int(Scintilla.ModificationFlags.InsertText) and nd.text:
            retained.append(nd)

    editor.notify.connect(on_notify)
    editor.insertText(0, "hello")
    assert retained[0].text == "hello"

    editor.insertText(0, "world")

    assert retained[0].text != "hello"
