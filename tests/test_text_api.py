"""The str/bytes contract of the typed API (issue #16).

Text -- document text, names, display strings -- is `str` in and out, encoded
per the document's encoding; raw data (style bytes, images, `sends`/`sendr`)
is bytes in and out. Neither side converts the other implicitly, and a wrong
type is a clean TypeError (not the NameError shiboken's error reporting used
to raise for this module). The stub must promise exactly what the runtime
accepts.
"""

import re
from pathlib import Path
from typing import Final

import pytest
from pytestqt.qtbot import QtBot

from pyside6_scintilla import Scintilla, ScintillaDocument, ScintillaEdit, ScintillaEditBase

STUB_PATH: Final = Path(__file__).resolve().parent.parent / "src" / "pyside6_scintilla" / "_pyside6_scintilla.pyi"

# Text methods: called with one str argument (after any leading int ones).
TEXT_SETTERS: Final = [
    ("setText", ()),
    ("addText", ()),
    ("appendText", ()),
    ("insertText", (0,)),
    ("replaceSel", ()),
    ("styleSetFont", (Scintilla.StylesCommon.Default,)),
    ("setWordChars", ()),
    ("annotationSetText", (0,)),
    ("setProperty", ("key",)),
]

# Bytes methods: called with one bytes argument (after any leading int ones).
BYTES_SETTERS: Final = [
    ("setStylingEx", ()),
    ("addStyledText", ()),
    ("marginSetStyles", (0,)),
    ("annotationSetStyles", (0,)),
]


@pytest.fixture
def editor(qtbot: QtBot) -> ScintillaEdit:
    """A fresh editor, in Scintilla's default UTF-8 mode."""
    widget = ScintillaEdit()
    qtbot.addWidget(widget)
    return widget


@pytest.mark.parametrize(("method", "leading"), TEXT_SETTERS)
def test_text_methods_reject_bytes(editor: ScintillaEdit, method: str, leading: tuple[object, ...]) -> None:
    """Text methods take str only -- bytes isn't decoded implicitly."""
    for value in (b"x", bytearray(b"x")):
        with pytest.raises(TypeError, match=method):
            getattr(editor, method)(*leading, value)


@pytest.mark.parametrize(("method", "leading"), BYTES_SETTERS)
def test_bytes_methods_reject_str(editor: ScintillaEdit, method: str, leading: tuple[object, ...]) -> None:
    """Bytes methods take bytes only -- str isn't encoded implicitly."""
    with pytest.raises(TypeError, match=method):
        getattr(editor, method)(*leading, "x")


def test_raw_sends_rejects_str(qtbot: QtBot) -> None:
    """ScintillaEditBase.sends takes the exact bytes Scintilla receives, never str."""
    base = ScintillaEditBase()
    qtbot.addWidget(base)

    with pytest.raises(TypeError, match="sends"):
        base.sends(Scintilla.Message.SetText, 0, "x")  # type: ignore[arg-type]


def test_non_ascii_text_round_trips(editor: ScintillaEdit) -> None:
    """str in and out, stored as UTF-8 bytes (positions/lengths count those bytes)."""
    editor.setText("héllo\nwörld")

    assert editor.getText() == "héllo\nwörld"
    assert editor.textLength() == len("héllo\nwörld".encode())
    assert editor.getLine(1) == "wörld"
    assert editor.textRange(0, len("hé".encode())) == "hé"


def test_length_parameters_are_computed_from_the_encoded_text(editor: ScintillaEdit) -> None:
    """addText/appendText/replaceTarget take no length: it's the encoded text's byte count."""
    editor.setText("ab")
    editor.appendText("ç€")
    editor.gotoPos(1)
    editor.addText("ü")

    assert editor.getText() == "aüb" + "ç€"

    editor.setTargetRange(0, len("aü".encode()))
    editor.replaceTarget("ÿ")

    assert editor.getText() == "ÿb" + "ç€"


def test_get_bytes_returns_the_stored_bytes(editor: ScintillaEdit) -> None:
    """getBytes() is the undecoded document, in its own encoding -- for byte-offset consumers."""
    editor.appendText("héllo\x00!")  # appendText passes a length, so the NUL is kept
    assert editor.getBytes().data() == "héllo\x00!".encode()

    editor.setCodePage(0)
    editor.setText("é")
    assert editor.getBytes().data() == b"\xe9"


def test_byte_range_getters_match_the_text_ones(editor: ScintillaEdit) -> None:
    """getBytes(start, end)/get_byte_range are textRange/get_char_range, undecoded."""
    editor.setText("aé€b")
    start, end = 1, len("aé€".encode())

    assert editor.getBytes(start, end).data() == "é€".encode()
    assert editor.textRange(start, end) == "é€"
    doc = editor.get_doc()
    assert doc.get_byte_range(start, end - start).data() == "é€".encode()


def caret_and_text_after(editor: ScintillaEdit, method: str, *args: object) -> tuple[int, str, int]:
    """(caret, text, undo steps to the original text) after calling `method` on "ab|cd" (caret at 2, "b|c" selected)."""
    editor.setText("abcd")
    editor.emptyUndoBuffer()
    editor.setSel(1, 2)
    getattr(editor, method)(*args)
    caret, text = editor.currentPos(), editor.getText()
    undo_steps = 0
    while editor.canUndo():
        editor.undo()
        undo_steps += 1
    return caret, text, undo_steps


@pytest.mark.parametrize(
    ("method", "leading"),
    [("setText", ()), ("insertText", (3,)), ("insertText", (-1,)), ("replaceSel", ())],
)
def test_nul_terminated_setters_keep_embedded_nuls(
    editor: ScintillaEdit, method: str, leading: tuple[object, ...]
) -> None:
    """Text with a NUL isn't truncated, and behaves like the message does with NUL-free text."""
    plain = caret_and_text_after(editor, method, *leading, "XY")
    with_nul = caret_and_text_after(editor, method, *leading, "X\x00")

    assert with_nul[1] == plain[1].replace("XY", "X\x00")
    assert with_nul[0] == plain[0]
    assert with_nul[2] == plain[2]


def test_stub_docs_name_the_message_and_its_differences() -> None:
    """Each generated method's hover doc maps it back to Scintilla's documentation."""
    stub = STUB_PATH.read_text(encoding="utf-8").split("class ScintillaEditFixed(", 1)[1]

    add_text_doc = stub.split("def addText(", 1)[1].split("def ", 1)[0]
    assert "Sends `SCI_ADDTEXT`." in add_text_doc
    assert "No `length` argument" in add_text_doc
    get_text_doc = stub.split("def getText(", 1)[1].split("def ", 1)[0]
    assert "Sends `SCI_GETTEXT`." in get_text_doc
    assert "instead of filling" in get_text_doc


def test_byte_range_getters_clamp_to_the_document(editor: ScintillaEdit) -> None:
    """-1 means "to the end", as in Scintilla; a range past the end is clamped, not NUL-filled."""
    editor.setText("hello world")

    assert editor.textRange(6, -1) == "world"
    assert editor.textRange(0, 100) == "hello world"
    assert editor.getBytes(-5, 5).data() == b"hello"
    assert editor.getBytes(8, 3).data() == b""


def test_dbcs_code_page_is_shared_by_editor_and_document(editor: ScintillaEdit) -> None:
    """In a DBCS code page the code page picks the codec, on both sides, so text round trips."""
    editor.setCodePage(932)
    editor.setText("日本")
    assert editor.getBytes().data() == "日本".encode("shift_jis")
    assert editor.getText() == "日本"

    doc = editor.get_doc()
    doc.insert_string(0, "語")
    assert doc.get_byte_range(0, 2).data() == "語".encode("shift_jis")
    assert editor.getText() == "語日本"


@pytest.mark.parametrize("method", ["annotationSetText", "eOLAnnotationSetText", "marginSetText"])
def test_none_clears_a_line_annotation(editor: ScintillaEdit, method: str) -> None:
    """`None` is the message's NULL, which removes the annotation; an empty str is an empty annotation (as upstream)."""
    editor.setText("a\nb")
    getter = {"annotationSetText": "annotationText", "eOLAnnotationSetText": "eOLAnnotationText"}.get(
        method, "marginText"
    )
    getattr(editor, method)(0, "note")
    assert getattr(editor, getter)(0) == "note"

    getattr(editor, method)(0, None)
    assert getattr(editor, getter)(0) == ""
    if method == "annotationSetText":
        assert editor.annotationLines(0) == 0
        editor.annotationSetText(0, "")
        assert editor.annotationLines(0) == 1


def test_raw_send_accepts_negative_wparam(editor: ScintillaEdit) -> None:
    """Scintilla reads wParam as signed, and several messages take -1 there (e.g. InsertText's pos)."""
    editor.setText("ab")
    editor.gotoPos(1)

    editor.sends(Scintilla.Message.InsertText, -1, b"X")

    assert editor.getText() == "aXb"


def test_nul_safe_insert_text_rejects_out_of_range_positions_like_the_message(editor: ScintillaEdit) -> None:
    """The NUL fallback mirrors Document::CheckPosition instead of clamping."""
    editor.setText("hello")

    editor.insertText(100, "XY")
    editor.insertText(100, "X\x00")

    assert editor.getText() == "hello"


def test_get_text_has_no_padding(editor: ScintillaEdit) -> None:
    """The whole document, without the NUL padding the old QByteArray getters had."""
    editor.setText("hello\nworld")

    assert editor.getText() == "hello\nworld"


def test_get_cur_line_returns_text_and_caret(editor: ScintillaEdit) -> None:
    """getCurLine() returns (line text, caret byte offset in the line)."""
    editor.setText("first\nsecond")
    editor.gotoPos(len("first\nsec"))

    assert editor.getCurLine() == ("second", len("sec"))


def test_non_utf8_code_page_uses_the_document_encoding(editor: ScintillaEdit) -> None:
    """In code page 0 (default character set), text is stored as Latin-1, not UTF-8."""
    editor.setCodePage(0)
    editor.setText("é")

    assert editor.textLength() == 1
    assert editor.sendr(Scintilla.Message.GetText, editor.textLength() + 1).data() == b"\xe9"
    assert editor.getText() == "é"


def test_bytes_methods_keep_embedded_nuls(editor: ScintillaEdit) -> None:
    """Style bytes are raw data: NULs (style 0) aren't string terminators."""
    editor.marginSetText(0, "abc")
    editor.marginSetStyles(0, b"\x01\x00\x02")

    assert editor.marginStyles(0).data() == b"\x01\x00\x02"


def test_sends_and_sendr_round_trip_bytes(qtbot: QtBot) -> None:
    """The raw layer passes bytes through unchanged."""
    base = ScintillaEditBase()
    qtbot.addWidget(base)

    base.sends(Scintilla.Message.SetText, 0, "héllo".encode())

    assert base.sendr(Scintilla.Message.GetText, base.send(Scintilla.Message.GetTextLength)).data() == (
        "héllo".encode()
    )


def test_document_text_is_str(editor: ScintillaEdit) -> None:
    """ScintillaDocument's text members take/return str and styles are ints."""
    doc = editor.get_doc()
    assert isinstance(doc, ScintillaDocument)

    doc.insert_string(0, "ü!")

    assert doc.get_char_range(0, len("ü!".encode())) == "ü!"
    assert editor.getText() == "ü!"
    assert doc.style_at(0) == 0


def test_modified_signal_text_is_str(editor: ScintillaEdit, qtbot: QtBot) -> None:
    """The editor's and the document's `modified` signals deliver decoded text."""
    doc = editor.get_doc()
    edit_texts: list[str] = []
    doc_texts: list[str] = []
    editor.modified.connect(lambda *args: edit_texts.append(args[4]))
    doc.modified.connect(lambda *args: doc_texts.append(args[2]))

    editor.setText("ça")

    assert "ça" in edit_texts
    assert "ça" in doc_texts


def stub_param_type(method: str) -> str:
    """The annotation of `method`'s last parameter in the ScintillaEditFixed stub."""
    stub = STUB_PATH.read_text(encoding="utf-8")
    class_body = stub.split("class ScintillaEditFixed(", 1)[1]
    match = re.search(rf"def {method}\(self, (.*)\) -> ", class_body)
    assert match, method
    last_param = [p for p in match.group(1).split(", ") if p != "/"][-1]
    return last_param.split(": ", 1)[1]


@pytest.mark.parametrize(("method", "leading"), TEXT_SETTERS)
def test_stub_types_text_methods_as_str(method: str, leading: tuple[object, ...]) -> None:
    """The stub promises str, and only str, for text parameters."""
    assert stub_param_type(method) == "str"


@pytest.mark.parametrize(("method", "leading"), BYTES_SETTERS)
def test_stub_types_bytes_methods_as_bytes(method: str, leading: tuple[object, ...]) -> None:
    """The stub promises exactly what PySide6's QByteArray converter accepts."""
    assert stub_param_type(method) == "PySide6.QtCore.QByteArray | bytes | bytearray"
