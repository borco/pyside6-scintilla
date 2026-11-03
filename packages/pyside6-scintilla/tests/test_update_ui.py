"""SCN_UPDATEUI's `Update.Text`/`Update.LineCount` flags and `position` field (Scintilla 5.6.5/5.6.6).

The notification is sent from Scintilla's idle work, which ScintillaQt
queues as a posted Qt event since 5.6.5, so each test waits for it.
"""

from pytestqt.qtbot import QtBot

from pyside6_scintilla import Scintilla, ScintillaEdit

UPDATE = Scintilla.Update


def collect_updates(editor: ScintillaEdit) -> list[tuple[int, int]]:
    """Record each SCN_UPDATEUI's (updated, position), from notify(): only it sets `updated`."""
    updates: list[tuple[int, int]] = []

    def on_notify(nd: Scintilla.NotificationData) -> None:
        if nd.updated:
            updates.append((int(nd.updated), int(nd.position)))

    editor.notify.connect(on_notify)
    return updates


def test_update_flag_values() -> None:
    """The new flags have SC_UPDATE_TEXT/SC_UPDATE_LINE_COUNT's values."""
    assert UPDATE.Text == 0x10
    assert UPDATE.LineCount == 0x20


def test_text_change_reports_text_and_its_start(qtbot: QtBot) -> None:
    """Inserting text sets Update.Text, with `position` at the earliest change."""
    editor = ScintillaEdit()
    qtbot.addWidget(editor)
    editor.setText("hello world")
    qtbot.wait(10)  # flush setText's own update
    updates = collect_updates(editor)

    editor.insertText(6, "big ")
    editor.insertText(9, "!")

    qtbot.waitUntil(lambda: any(updated & UPDATE.Text for updated, _ in updates))
    text_updates = [(updated, position) for updated, position in updates if updated & UPDATE.Text]
    assert text_updates[0][1] == 6
    assert not text_updates[0][0] & UPDATE.LineCount


def test_new_line_reports_line_count(qtbot: QtBot) -> None:
    """Adding a line sets Update.LineCount alongside Update.Text."""
    editor = ScintillaEdit()
    qtbot.addWidget(editor)
    updates = collect_updates(editor)

    editor.insertText(0, "a\nb")

    qtbot.waitUntil(lambda: any(updated & UPDATE.LineCount for updated, _ in updates))
    assert any(updated & UPDATE.Text and position == 0 for updated, position in updates)


def test_selection_change_has_no_position(qtbot: QtBot) -> None:
    """Without a text change, `position` is Scintilla.InvalidPosition."""
    editor = ScintillaEdit()
    qtbot.addWidget(editor)
    editor.setText("hello")
    qtbot.wait(10)
    updates = collect_updates(editor)

    editor.setSel(1, 3)

    qtbot.waitUntil(lambda: any(updated & UPDATE.Selection for updated, _ in updates))
    assert all(position == Scintilla.InvalidPosition for updated, position in updates if not updated & UPDATE.Text)
