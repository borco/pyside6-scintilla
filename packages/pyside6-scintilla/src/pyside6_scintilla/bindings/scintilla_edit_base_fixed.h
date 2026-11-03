// ScintillaEditBaseFixed: the class exposed to Python as ScintillaEditBase
// (see __init__.py), and the base of the generated ScintillaEditFixed
// (ScintillaEdit in Python). Vendored headers under src/scintilla/ are never
// hand-edited (see CLAUDE.md's vendoring policy), so fixes live here:
//
// - Signals: several of ScintillaEditBase's signals carry
//   Scintilla::Position/ModificationFlags/FoldLevel/etc. parameters. shiboken
//   marshals these fine as ordinary method arguments, but Qt's generic
//   meta-call path used to invoke a Python slot can't convert them, so a
//   Python slot connected to e.g. ScintillaEditBase::modified never fires (the
//   TypeError is swallowed by Qt's event loop). This class re-emits each with
//   a plain-int signature (and `modified`'s text decoded to QString, per the
//   document's encoding), which shadows the inherited signal through normal
//   Python attribute/MRO lookup -- Qt signals reach Python via PySide's
//   metaobject introspection, not via bindings.xml, so nothing needs removing
//   from the typesystem.
// - Raw messages: ScintillaEditBase::send/sends are removed in bindings.xml and
//   replaced below. Their sptr_t/uptr_t types are unknown to shiboken's
//   signature support (an UNRECOGNIZED RuntimeWarning, and a broken error
//   report on a bad call), and sends(const char *) would be bound as str-only
//   (shiboken's `const char *` converter, always UTF-8). The replacements use
//   qint64 (also for wParam: Scintilla reads it as signed, and several
//   messages take -1 there), take bytes, and add sendr() for messages that
//   return a string. (Not qintptr/quintptr: PySide converts qintptr to Python
//   with PyLong_FromLong, which truncates to 32 bits on Windows -- pointers
//   like GetDocPointer's result included.) They're not virtual, so the
//   generated ScintillaEditFixed methods don't check for a Python override on
//   each call.
#ifndef SCINTILLA_EDIT_BASE_FIXED_H
#define SCINTILLA_EDIT_BASE_FIXED_H

#include <QByteArray>
#include <QString>

// moc's lightweight parser chokes on the vendored Scintilla headers (e.g.
// ScintillaStructures.h), even though it never needs their contents -- it
// only needs the base class name for the generated metaobject. Hide the real
// include from moc's pass; the compiler always takes the #else branch.
#ifdef Q_MOC_RUN
class ScintillaEditBase;
#else
#include <ScintillaEditBase.h>
#endif

// Not exported (unlike ScintillaEditBase, which lives in scintilla_qt and
// needs EXPORT_IMPORT_API): defined and compiled within _pyside6_scintilla.
class ScintillaEditBaseFixed : public ScintillaEditBase {
	Q_OBJECT

public:
	explicit ScintillaEditBaseFixed(QWidget *parent = nullptr);

	qint64 send(unsigned int iMessage, qint64 wParam = 0, qint64 lParam = 0) const;

	// Send `iMessage` with `data` as its string lParam (NUL-terminated, since
	// QByteArray always is; embedded NULs reach Scintilla too).
	qint64 sends(unsigned int iMessage, qint64 wParam, const QByteArray &data) const;

	// Send `iMessage`, a message whose lParam is a result buffer (a
	// "stringresult" in Scintilla.iface), and return that result. Sizes the
	// buffer by first sending with a NULL lParam, as Scintilla documents;
	// `wParam` is passed to both sends, so for the messages whose wParam is
	// the buffer length (GetText, GetCurLine) pass that length.
	QByteArray sendr(unsigned int iMessage, qint64 wParam = 0) const;

signals:
	void linesAdded(int linesAdded);
	void styleNeeded(int position);
	void doubleClick(int position, int line);
	void updateUi(int updated);
	void modified(int type, int position, int length, int linesAdded, const QString &text, int line, int foldNow,
		      int foldPrev);
	void macroRecord(int message, quint64 wParam, qint64 lParam);
	void marginClicked(int position, int modifiers, int margin);
	void textAreaClicked(int line, int modifiers);
	void needShown(int position, int length);
	void hotSpotClick(int position, int modifiers);
	void hotSpotDoubleClick(int position, int modifiers);
	void autoCompleteSelection(int position, const QString &text);
	void command(quint64 wParam, qint64 lParam);

protected:
	// sendr()'s implementation, shared with the generated string-result
	// methods: with `lengthInWParam`, the size query is sent with wParam 0 and
	// the fill with the size (GetText/GetCurLine); `fillResult` receives the
	// fill send's own result (GetCurLine's caret offset). Protected (not
	// private) so ScintillaEditFixed can call it; not bound, see bindings.xml.
	QByteArray stringResult(unsigned int iMessage, qint64 wParam, bool lengthInWParam = false,
				qint64 *fillResult = nullptr) const;
};

#endif /* SCINTILLA_EDIT_BASE_FIXED_H */
