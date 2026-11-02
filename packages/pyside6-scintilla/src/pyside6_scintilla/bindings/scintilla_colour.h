// Conversions between QColor and Scintilla's packed colour integers (issue
// #17): `colour` is 0xBBGGRR (red in the low byte) and `colouralpha` is
// 0xAABBGGRR -- the opposite byte order from Qt's 0xAARRGGBB (QColor::rgba()).
//
// Deliberately not included by bindings.h, so shiboken never sees (or binds)
// these -- they're implementation details of the generated ScintillaEditFixed
// methods.
#ifndef SCINTILLA_COLOUR_H
#define SCINTILLA_COLOUR_H

#include <QColor>
#include <QtGlobal>

// `withAlpha` for `colouralpha` messages; plain `colour` ones ignore the
// QColor's alpha (Scintilla reads only the low 24 bits).
inline qint64 colourToScintilla(const QColor &colour, bool withAlpha) {
	const QRgb rgb = colour.rgba();
	const quint32 packed = static_cast<quint32>(qRed(rgb)) | (static_cast<quint32>(qGreen(rgb)) << 8) |
			       (static_cast<quint32>(qBlue(rgb)) << 16) |
			       (withAlpha ? static_cast<quint32>(qAlpha(rgb)) << 24 : 0u);
	return static_cast<qint64>(packed);
}

// A plain `colour` result is always opaque.
inline QColor colourFromScintilla(qint64 value, bool withAlpha) {
	const quint32 packed = static_cast<quint32>(value);
	return QColor(static_cast<int>(packed & 0xFF), static_cast<int>((packed >> 8) & 0xFF),
		      static_cast<int>((packed >> 16) & 0xFF), withAlpha ? static_cast<int>(packed >> 24) : 255);
}

#endif /* SCINTILLA_COLOUR_H */
