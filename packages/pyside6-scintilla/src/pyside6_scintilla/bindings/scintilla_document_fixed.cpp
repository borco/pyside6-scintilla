#include "scintilla_document_fixed.h"

#include "scintilla_text_encoding.h"

ScintillaDocumentFixed::ScintillaDocumentFixed(QObject *parent, void *pdoc_) : ScintillaDocument(parent, pdoc_) {
	connect(this, &ScintillaDocument::modified, this,
		[this](int position, int modification_type, const QByteArray &text, int length, int linesAdded, int line,
		       int foldLevelNow, int foldLevelPrev) {
			emit modified(position, modification_type, stringFromDocument(*this, text), length, linesAdded, line,
				      foldLevelNow, foldLevelPrev);
		});
}

void ScintillaDocumentFixed::insert_string(int position, const QString &text) {
	ScintillaDocument::insert_string(position, bytesForDocument(*this, text));
}

QString ScintillaDocumentFixed::get_char_range(int position, int length) const {
	return stringFromDocument(*this, get_byte_range(position, length));
}

QByteArray ScintillaDocumentFixed::get_byte_range(int position, int length) const {
	return ScintillaDocument::get_char_range(position, length);
}

int ScintillaDocumentFixed::style_at(int position) const {
	return static_cast<unsigned char>(ScintillaDocument::style_at(position));
}

bool ScintillaDocumentFixed::set_style_for(int length, int style) {
	return ScintillaDocument::set_style_for(length, static_cast<char>(style));
}
