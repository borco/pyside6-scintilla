// ScintillaDocumentFixed: the class exposed to Python as ScintillaDocument
// (see __init__.py). The vendored ScintillaDocument takes and returns document
// text as QByteArray, its style as `char`, and emits `modified` with
// QByteArray text; this subclass replaces those members (the originals are
// removed in bindings.xml) so text is QString (Python str) and styles are int,
// matching ScintillaEdit. Text is converted per the document's code page (see
// scintilla_text_encoding.h).
#ifndef SCINTILLA_DOCUMENT_FIXED_H
#define SCINTILLA_DOCUMENT_FIXED_H

#include <QByteArray>
#include <QString>

#include <ScintillaDocument.h>

// Not exported: defined and compiled within _pyside6_scintilla.
class ScintillaDocumentFixed : public ScintillaDocument {
	Q_OBJECT

public:
	explicit ScintillaDocumentFixed(QObject *parent = nullptr, void *pdoc_ = nullptr);

	void insert_string(int position, const QString &text);
	QString get_char_range(int position, int length) const;
	// The same range as stored (in the document's encoding), not decoded.
	QByteArray get_byte_range(int position, int length) const;
	int style_at(int position) const;
	bool set_style_for(int length, int style);

signals:
	void modified(int position, int modification_type, const QString &text, int length, int linesAdded, int line,
		      int foldLevelNow, int foldLevelPrev);
};

#endif /* SCINTILLA_DOCUMENT_FIXED_H */
