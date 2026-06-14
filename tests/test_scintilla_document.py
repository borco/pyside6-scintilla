"""Smoke test for the ScintillaDocument binding.

Confirms get_doc()/set_doc() let multiple ScintillaEdit widgets share one
document buffer, and that ScintillaDocument's Qt signals fire as expected.
"""

from pyside6_scintilla import ScintillaEdit


def test_shared_document_keeps_widgets_in_sync(qtbot):
    """Text typed in one editor is visible in another sharing its document."""
    editor_a = ScintillaEdit()
    editor_b = ScintillaEdit()
    qtbot.addWidget(editor_a)
    qtbot.addWidget(editor_b)

    editor_b.set_doc(editor_a.get_doc())

    editor_a.setText("hello")

    assert editor_b.textLength() == editor_a.textLength()
    assert editor_b.getText(editor_b.textLength()).data() == b"hello"


def test_modified_signal_fires_on_edit(qtbot):
    """ScintillaDocument.modified fires when its text changes."""
    editor = ScintillaEdit()
    qtbot.addWidget(editor)

    doc = editor.get_doc()

    with qtbot.waitSignal(doc.modified, timeout=1000):
        editor.setText("hello")
