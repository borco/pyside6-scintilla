#include "scintilla_text_encoding.h"

#include <QTextCodec>

#include <ScintillaDocument.h>
#include <ScintillaEditBase.h>

namespace {

// Qt codec name for a Scintilla SC_CHARSET_* value. Mirrors CharacterSetID()
// in PlatQt.cpp, which isn't exported from the scintilla_qt library.
const char *codecNameForCharacterSet(qint64 characterSet) {
	switch (characterSet) {
	case SC_CHARSET_BALTIC:
		return "ISO 8859-13";
	case SC_CHARSET_CHINESEBIG5:
		return "Big5";
	case SC_CHARSET_EASTEUROPE:
		return "ISO 8859-2";
	case SC_CHARSET_GB2312:
		return "GB18030-0";
	case SC_CHARSET_GREEK:
		return "ISO 8859-7";
	case SC_CHARSET_HANGUL:
		return "CP949";
	case SC_CHARSET_MAC:
		return "Apple Roman";
	case SC_CHARSET_RUSSIAN:
		return "KOI8-R";
	case SC_CHARSET_CYRILLIC:
		return "Windows-1251";
	case SC_CHARSET_SHIFTJIS:
		return "Shift-JIS";
	case SC_CHARSET_TURKISH:
		return "ISO 8859-9";
	case SC_CHARSET_HEBREW:
		return "ISO 8859-8";
	case SC_CHARSET_ARABIC:
		return "ISO 8859-6";
	case SC_CHARSET_VIETNAMESE:
		return "Windows-1258";
	case SC_CHARSET_THAI:
		return "TIS-620";
	case SC_CHARSET_8859_15:
		return "ISO 8859-15";
	default:
		return "ISO 8859-1";
	}
}

// Qt codec name for one of the DBCS code pages Scintilla supports (see
// ScintillaQt::ValidCodePage), or null for a single-byte code page (0), where
// the character set decides.
const char *codecNameForCodePage(int codePage) {
	switch (codePage) {
	case 932:
		return "Shift-JIS";
	case 936:
		return "GB18030-0";
	case 949:
		return "CP949";
	case 950:
		return "Big5";
	default:
		return nullptr;
	}
}

// The one lookup both the editor and the document overloads use, so text
// written through one is read back the same way through the other: a DBCS
// code page names the codec itself; otherwise the character set does (the
// editor's default style; a standalone document has none, so Scintilla's
// default character set, i.e. Latin-1). Null means UTF-8.
const char *codecName(int codePage, qint64 characterSet) {
	if (codePage == SC_CP_UTF8)
		return nullptr;
	if (const char *name = codecNameForCodePage(codePage))
		return name;
	return codecNameForCharacterSet(characterSet);
}

// Latin-1 if Qt has no codec by that name (a byte-preserving fallback).
QByteArray encode(const char *codecName, const QString &text) {
	if (text.isEmpty())
		return QByteArray();
	if (!codecName)
		return text.toUtf8();
	QTextCodec *codec = QTextCodec::codecForName(codecName);
	return codec ? codec->fromUnicode(text) : text.toLatin1();
}

QString decode(const char *codecName, const QByteArray &bytes) {
	if (bytes.isEmpty())
		return QString();
	if (!codecName)
		return QString::fromUtf8(bytes);
	QTextCodec *codec = QTextCodec::codecForName(codecName);
	return codec ? codec->toUnicode(bytes) : QString::fromLatin1(bytes);
}

const char *codecName(const ScintillaEditBase &editor) {
	const int codePage = static_cast<int>(editor.send(SCI_GETCODEPAGE, 0, 0));
	if (codePage == SC_CP_UTF8)
		return nullptr;
	return codecName(codePage, editor.send(SCI_STYLEGETCHARACTERSET, STYLE_DEFAULT, 0));
}

const char *codecName(const ScintillaDocument &document) {
	return codecName(document.get_code_page(), SC_CHARSET_DEFAULT);
}

} // namespace

QByteArray bytesForDocument(const ScintillaEditBase &editor, const QString &text) {
	return text.isEmpty() ? QByteArray() : encode(codecName(editor), text);
}

QString stringFromDocument(const ScintillaEditBase &editor, const QByteArray &bytes) {
	return bytes.isEmpty() ? QString() : decode(codecName(editor), bytes);
}

QByteArray bytesForDocument(const ScintillaDocument &document, const QString &text) {
	return text.isEmpty() ? QByteArray() : encode(codecName(document), text);
}

QString stringFromDocument(const ScintillaDocument &document, const QByteArray &bytes) {
	return bytes.isEmpty() ? QString() : decode(codecName(document), bytes);
}
