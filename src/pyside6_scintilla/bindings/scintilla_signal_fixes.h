// Non-vendored wrapper classes that re-emit ScintillaEditBase's
// Scintilla::Position/ModificationFlags/FoldLevel/etc.-typed signals with
// plain-int (or QByteArray/QString) signatures.
//
// shiboken can marshal these custom types fine as ordinary method
// arguments (they're registered as primitive-type/enum-type in
// bindings.xml), but Qt's generic meta-call path used to invoke a Python
// slot from a signal emission can't convert them, so a Python slot
// connected directly to e.g. ScintillaEditBase::modified never fires (the
// resulting TypeError is swallowed by Qt's event loop). Re-emitting with
// plain types here sidesteps that, mirroring ScintillaDocument::modified
// (see src/scintilla/qt/ScintillaEdit/ScintillaDocument.h), which works
// because it was already declared with plain-int parameters.
//
// Vendored headers under src/scintilla/ are never hand-edited (see
// CLAUDE.md's vendoring policy), so the fix lives here instead: these
// subclasses are bound in bindings.xml *alongside*
// ScintillaEditBase/ScintillaEdit. Each redeclares the same-named signal
// with a plain-int signature, which simply shadows the inherited
// broken-signature one through normal Python attribute/MRO lookup -- Qt
// signals are exposed to Python via PySide's own metaobject introspection,
// not via bindings.xml, so there's nothing to remove from the typesystem
// for this to work.
#ifndef SCINTILLA_SIGNAL_FIXES_H
#define SCINTILLA_SIGNAL_FIXES_H

#include <QByteArray>
#include <QString>

// moc's lightweight parser chokes on the vendored Scintilla headers (e.g.
// the bitfield-free but otherwise intricate ScintillaStructures.h), even
// though it never needs their contents -- it only needs the
// ScintillaEditBase/ScintillaEdit tokens to record this header's classes'
// base classes in the generated metaobject. Hide the real includes from
// moc's pass and give it bare forward declarations instead; the actual
// compiler (which does need the full definitions, e.g. for the
// member-initializer-list base constructor calls below) always takes the
// #else branch.
#ifdef Q_MOC_RUN
class ScintillaEditBase;
class ScintillaEdit;
#else
#include <ScintillaEditBase.h>
#include <ScintillaEdit.h>
#endif

// Connects `base`'s broken-signature signals to plain-typed re-emissions on
// `target`. `Target` must declare the signals listed below (see
// ScintillaEditBaseFixed/ScintillaEditFixed) -- factored out so both
// subclasses share the wiring instead of duplicating it.
template <typename Target>
void connectFixedScintillaSignals(ScintillaEditBase *base, Target *target) {
	QObject::connect(base, &ScintillaEditBase::linesAdded, target, [target](Scintilla::Position linesAdded) {
		emit target->linesAdded(static_cast<int>(linesAdded));
	});
	QObject::connect(base, &ScintillaEditBase::styleNeeded, target, [target](Scintilla::Position position) {
		emit target->styleNeeded(static_cast<int>(position));
	});
	QObject::connect(base, &ScintillaEditBase::doubleClick, target,
			  [target](Scintilla::Position position, Scintilla::Position line) {
				  emit target->doubleClick(static_cast<int>(position), static_cast<int>(line));
			  });
	QObject::connect(base, &ScintillaEditBase::updateUi, target, [target](Scintilla::Update updated) {
		emit target->updateUi(static_cast<int>(updated));
	});
	QObject::connect(
		base, &ScintillaEditBase::modified, target,
		[target](Scintilla::ModificationFlags type, Scintilla::Position position, Scintilla::Position length,
			  Scintilla::Position linesAdded, const QByteArray &text, Scintilla::Position line,
			  Scintilla::FoldLevel foldNow, Scintilla::FoldLevel foldPrev) {
			emit target->modified(static_cast<int>(type), static_cast<int>(position), static_cast<int>(length),
					       static_cast<int>(linesAdded), text, static_cast<int>(line),
					       static_cast<int>(foldNow), static_cast<int>(foldPrev));
		});
	QObject::connect(base, &ScintillaEditBase::macroRecord, target,
			  [target](Scintilla::Message message, Scintilla::uptr_t wParam, Scintilla::sptr_t lParam) {
				  emit target->macroRecord(static_cast<int>(message), static_cast<quintptr>(wParam),
							    static_cast<qintptr>(lParam));
			  });
	QObject::connect(base, &ScintillaEditBase::marginClicked, target,
			  [target](Scintilla::Position position, Scintilla::KeyMod modifiers, int margin) {
				  emit target->marginClicked(static_cast<int>(position), static_cast<int>(modifiers), margin);
			  });
	QObject::connect(base, &ScintillaEditBase::textAreaClicked, target,
			  [target](Scintilla::Position line, int modifiers) {
				  emit target->textAreaClicked(static_cast<int>(line), modifiers);
			  });
	QObject::connect(base, &ScintillaEditBase::needShown, target,
			  [target](Scintilla::Position position, Scintilla::Position length) {
				  emit target->needShown(static_cast<int>(position), static_cast<int>(length));
			  });
	QObject::connect(base, &ScintillaEditBase::hotSpotClick, target,
			  [target](Scintilla::Position position, Scintilla::KeyMod modifiers) {
				  emit target->hotSpotClick(static_cast<int>(position), static_cast<int>(modifiers));
			  });
	QObject::connect(base, &ScintillaEditBase::hotSpotDoubleClick, target,
			  [target](Scintilla::Position position, Scintilla::KeyMod modifiers) {
				  emit target->hotSpotDoubleClick(static_cast<int>(position), static_cast<int>(modifiers));
			  });
	QObject::connect(base, &ScintillaEditBase::autoCompleteSelection, target,
			  [target](Scintilla::Position position, const QString &text) {
				  emit target->autoCompleteSelection(static_cast<int>(position), text);
			  });
	QObject::connect(base, &ScintillaEditBase::command, target,
			  [target](Scintilla::uptr_t wParam, Scintilla::sptr_t lParam) {
				  emit target->command(static_cast<quintptr>(wParam), static_cast<qintptr>(lParam));
			  });
}

// Bound in bindings.xml; Python-visible as ScintillaEditBase (see
// __init__.py). Not exported (unlike ScintillaEditBase/ScintillaEdit,
// which live in scintilla_qt.dll and need EXPORT_IMPORT_API to be usable
// from this separate module): this class is defined and compiled entirely
// within the _pyside6_scintilla module itself.
class ScintillaEditBaseFixed : public ScintillaEditBase {
	Q_OBJECT

public:
	explicit ScintillaEditBaseFixed(QWidget *parent = nullptr) : ScintillaEditBase(parent) {
		connectFixedScintillaSignals(this, this);
	}

signals:
	void linesAdded(int linesAdded);
	void styleNeeded(int position);
	void doubleClick(int position, int line);
	void updateUi(int updated);
	void modified(int type, int position, int length, int linesAdded, const QByteArray &text, int line, int foldNow,
		      int foldPrev);
	void macroRecord(int message, quintptr wParam, qintptr lParam);
	void marginClicked(int position, int modifiers, int margin);
	void textAreaClicked(int line, int modifiers);
	void needShown(int position, int length);
	void hotSpotClick(int position, int modifiers);
	void hotSpotDoubleClick(int position, int modifiers);
	void autoCompleteSelection(int position, const QString &text);
	void command(quintptr wParam, qintptr lParam);
};

// Bound in bindings.xml; Python-visible as ScintillaEdit (see __init__.py).
// ScintillaEdit inherits the same broken-signature signals directly from
// the vendored ScintillaEditBase, not from ScintillaEditBaseFixed, hence a
// second subclass repeating the fix rather than subclassing
// ScintillaEditBaseFixed (which doesn't have ScintillaEdit's API).
class ScintillaEditFixed : public ScintillaEdit {
	Q_OBJECT

public:
	explicit ScintillaEditFixed(QWidget *parent = nullptr) : ScintillaEdit(parent) {
		connectFixedScintillaSignals(this, this);
	}

signals:
	void linesAdded(int linesAdded);
	void styleNeeded(int position);
	void doubleClick(int position, int line);
	void updateUi(int updated);
	void modified(int type, int position, int length, int linesAdded, const QByteArray &text, int line, int foldNow,
		      int foldPrev);
	void macroRecord(int message, quintptr wParam, qintptr lParam);
	void marginClicked(int position, int modifiers, int margin);
	void textAreaClicked(int line, int modifiers);
	void needShown(int position, int length);
	void hotSpotClick(int position, int modifiers);
	void hotSpotDoubleClick(int position, int modifiers);
	void autoCompleteSelection(int position, const QString &text);
	void command(quintptr wParam, qintptr lParam);
};

#endif /* SCINTILLA_SIGNAL_FIXES_H */
