#include "scintilla_edit_base_fixed.h"

#include "scintilla_text_encoding.h"

ScintillaEditBaseFixed::ScintillaEditBaseFixed(QWidget *parent) : ScintillaEditBase(parent) {
	connect(this, &ScintillaEditBase::linesAdded, this,
		[this](Scintilla::Position added) { emit linesAdded(static_cast<int>(added)); });
	connect(this, &ScintillaEditBase::styleNeeded, this,
		[this](Scintilla::Position position) { emit styleNeeded(static_cast<int>(position)); });
	connect(this, &ScintillaEditBase::doubleClick, this, [this](Scintilla::Position position, Scintilla::Position line) {
		emit doubleClick(static_cast<int>(position), static_cast<int>(line));
	});
	connect(this, &ScintillaEditBase::updateUi, this,
		[this](Scintilla::Update updated) { emit updateUi(static_cast<int>(updated)); });
	connect(this, &ScintillaEditBase::modified, this,
		[this](Scintilla::ModificationFlags type, Scintilla::Position position, Scintilla::Position length,
		       Scintilla::Position linesAdded, const QByteArray &text, Scintilla::Position line,
		       Scintilla::FoldLevel foldNow, Scintilla::FoldLevel foldPrev) {
			emit modified(static_cast<int>(type), static_cast<int>(position), static_cast<int>(length),
				      static_cast<int>(linesAdded), stringFromDocument(*this, text), static_cast<int>(line),
				      static_cast<int>(foldNow), static_cast<int>(foldPrev));
		});
	connect(this, &ScintillaEditBase::macroRecord, this,
		[this](Scintilla::Message message, Scintilla::uptr_t wParam, Scintilla::sptr_t lParam) {
			emit macroRecord(static_cast<int>(message), static_cast<quint64>(wParam), static_cast<qint64>(lParam));
		});
	connect(this, &ScintillaEditBase::marginClicked, this,
		[this](Scintilla::Position position, Scintilla::KeyMod modifiers, int margin) {
			emit marginClicked(static_cast<int>(position), static_cast<int>(modifiers), margin);
		});
	connect(this, &ScintillaEditBase::textAreaClicked, this,
		[this](Scintilla::Position line, int modifiers) { emit textAreaClicked(static_cast<int>(line), modifiers); });
	connect(this, &ScintillaEditBase::needShown, this, [this](Scintilla::Position position, Scintilla::Position length) {
		emit needShown(static_cast<int>(position), static_cast<int>(length));
	});
	connect(this, &ScintillaEditBase::hotSpotClick, this,
		[this](Scintilla::Position position, Scintilla::KeyMod modifiers) {
			emit hotSpotClick(static_cast<int>(position), static_cast<int>(modifiers));
		});
	connect(this, &ScintillaEditBase::hotSpotDoubleClick, this,
		[this](Scintilla::Position position, Scintilla::KeyMod modifiers) {
			emit hotSpotDoubleClick(static_cast<int>(position), static_cast<int>(modifiers));
		});
	connect(this, &ScintillaEditBase::autoCompleteSelection, this, [this](Scintilla::Position position, const QString &text) {
		emit autoCompleteSelection(static_cast<int>(position), text);
	});
	connect(this, &ScintillaEditBase::command, this, [this](Scintilla::uptr_t wParam, Scintilla::sptr_t lParam) {
		emit command(static_cast<quint64>(wParam), static_cast<qint64>(lParam));
	});
}

qint64 ScintillaEditBaseFixed::send(unsigned int iMessage, qint64 wParam, qint64 lParam) const {
	return ScintillaEditBase::send(iMessage, static_cast<uptr_t>(wParam), lParam);
}

qint64 ScintillaEditBaseFixed::sends(unsigned int iMessage, qint64 wParam, const QByteArray &data) const {
	return ScintillaEditBase::sends(iMessage, static_cast<uptr_t>(wParam), data.constData());
}

QByteArray ScintillaEditBaseFixed::sendr(unsigned int iMessage, qint64 wParam) const {
	return stringResult(iMessage, wParam);
}

QByteArray ScintillaEditBaseFixed::stringResult(unsigned int iMessage, qint64 wParam, bool lengthInWParam,
						qint64 *fillResult) const {
	const qint64 size = send(iMessage, lengthInWParam ? 0 : wParam, 0);
	if (size <= 0)
		return QByteArray();
	QByteArray result(static_cast<qsizetype>(size) + 1, '\0');
	const qint64 filled = send(iMessage, lengthInWParam ? size : wParam, reinterpret_cast<qint64>(result.data()));
	if (fillResult)
		*fillResult = filled;
	result.resize(static_cast<qsizetype>(size));
	return result;
}
