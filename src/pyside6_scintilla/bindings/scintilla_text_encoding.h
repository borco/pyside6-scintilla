// Conversions between Python-facing text (QString) and the bytes a Scintilla
// document stores, following the document's encoding the same way ScintillaQt
// does internally (ScintillaQt::BytesForDocument/StringFromDocument, which are
// private): UTF-8 when the code page is SC_CP_UTF8, otherwise the codec for the
// default style's character set.
//
// Deliberately not included by bindings.h, so shiboken never sees (or binds)
// these -- they're implementation details of the generated ScintillaEditFixed
// methods and of ScintillaEditBaseFixed/ScintillaDocumentFixed.
#ifndef SCINTILLA_TEXT_ENCODING_H
#define SCINTILLA_TEXT_ENCODING_H

#include <QByteArray>
#include <QString>

class ScintillaDocument;
class ScintillaEditBase;

QByteArray bytesForDocument(const ScintillaEditBase &editor, const QString &text);
QString stringFromDocument(const ScintillaEditBase &editor, const QByteArray &bytes);

// A standalone document has no view, hence no style character set: non-UTF-8
// documents are decoded by their DBCS code page, or as Latin-1 for code page 0
// (Scintilla's default character set).
QByteArray bytesForDocument(const ScintillaDocument &document, const QString &text);
QString stringFromDocument(const ScintillaDocument &document, const QByteArray &bytes);

#endif /* SCINTILLA_TEXT_ENCODING_H */
