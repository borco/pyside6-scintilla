"""Generate `ScintillaEditFixed`, the class exposed to Python as `ScintillaEdit`.

Replaces upstream's `src/scintilla/qt/ScintillaEdit/WidgetGen.py` output
(`ScintillaEdit.{h,cpp}`), which maps every string parameter to `const char *`
and every string result to `QByteArray`. Python callers then had to pass `str`
(shiboken's `const char *` converter, always UTF-8) and got bytes back, with
byte-length parameters that had to agree with an encoding they never chose
(issue #16). This generator gives every message a consistent type instead:

- text (document text, names, display strings): `QString` in and out, i.e.
  Python `str` only, converted with the document's encoding (see
  `scintilla_text_encoding.h`); a byte-length parameter that only describes
  the string argument is dropped and computed from the encoded text;
- bytes (style bytes, images): `QByteArray` in and out, i.e. bytes-like only;
- everything else keeps WidgetGen's names, `const`-ness, and integer/bool
  types, so non-string methods are unchanged from Python -- except integers
  are `qint64` rather than Scintilla's `sptr_t`: shiboken's signature support
  knows `qint64` is `int`, but not `sptr_t`, which it reported as an
  UNRECOGNIZED RuntimeWarning per method (and `qintptr`, which it does know,
  is converted to Python via a 32-bit `long` on Windows);
- pixel values (`pixels` in Scintilla.iface, since 5.6.4) follow WidgetGen
  too: they're logical pixels, converted to the device pixels the engine uses
  under `SCALE_TECHNIQUE_PIXEL_ALIGNED` (a no-op otherwise), and each such
  method gets a `...F` twin taking/returning unrounded `float` pixels.

Method names follow WidgetGen's Qt-style `normalisedName()`, so existing calls
like `editor.setText(...)` keep working.

Run via `make generate`; `--check` exits non-zero if the checked-in output is
stale (used by CI), e.g. after vendoring a new Scintilla release.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Final

PACKAGE_ROOT: Final = Path(__file__).resolve().parent.parent
SCINTILLA_DIR: Final = PACKAGE_ROOT / "src" / "scintilla"
IFACE_PATH: Final = SCINTILLA_DIR / "include" / "Scintilla.iface"
BINDINGS_DIR: Final = PACKAGE_ROOT / "src" / "pyside6_scintilla" / "bindings"
HEADER_PATH: Final = BINDINGS_DIR / "scintilla_edit_fixed.h"
SOURCE_PATH: Final = BINDINGS_DIR / "scintilla_edit_fixed.cpp"

sys.path.insert(0, str(SCINTILLA_DIR / "scripts"))
import Face  # type: ignore[import-not-found]  # noqa: E402 -- upstream's Scintilla.iface parser

# iface types WidgetGen understands (anything else, e.g. `textrange`/`findtext`,
# is skipped, as upstream does; the hand-written methods cover the useful ones).
UNDERSTOOD_TYPES: Final = {
    "",
    "void",
    "int",
    "bool",
    "position",
    "line",
    "pointer",
    "colour",
    "colouralpha",
    "keymod",
    "pixels",
    "string",
    "stringresult",
    "cells",
}

# Messages whose string data is raw bytes, not text: style bytes (one style
# number per byte), XPM/RGBA image data, and `cells` (char, style) pairs.
BYTES_FEATURES: Final = {
    "AddStyledText",
    "SetStylingEx",
    "MarkerDefinePixmap",
    "RegisterImage",
    "MarkerDefineRGBAImage",
    "RegisterRGBAImage",
    "MarginSetStyles",
    "MarginGetStyles",
    "AnnotationSetStyles",
    "AnnotationGetStyles",
    "GetSubStyleBases",
}

# Messages whose text is always UTF-8 on Qt, whatever the document's encoding
# (PlatQt.cpp builds QFont families with QString::fromUtf8; locales are ASCII).
UTF8_FEATURES: Final = {"SetFontLocale", "GetFontLocale", "StyleSetFont", "StyleGetFont"}

# Not handled by ScintillaQt (only by the Win32/GTK/Cocoa platform layers), so
# they'd always return an empty result; `str` already is the UTF-8/Unicode form.
DROPPED_FEATURES: Final = {"TargetAsUTF8", "EncodedFromUTF8"}

# Returns a `(text, caret)` pair instead of just the text, since its message
# result (the caret's offset in the line) would otherwise be lost.
CUR_LINE_FEATURE: Final = "GetCurLine"

# Document-text setters whose message takes a NUL-terminated string (no length
# argument), so a `str` containing "\0" would be silently truncated. When the
# encoded text contains a NUL, these run this length-based equivalent instead
# (built on SCI_ADDTEXT, which inserts at the caret with an explicit length and
# moves the caret after it), reproducing the message's caret/undo behaviour --
# see the message handlers in src/scintilla/src/Editor.cxx. Otherwise they send
# the message as-is.
NUL_SAFE_FALLBACKS: Final = {
    "SetText": """\
		send(SCI_BEGINUNDOACTION, 0, 0);
		send(SCI_DELETERANGE, 0, send(SCI_GETLENGTH, 0, 0));
		send(SCI_SETEMPTYSELECTION, 0, 0);
		send(SCI_ADDTEXT, textBytes.size(), reinterpret_cast<qint64>(textBytes.constData()));
		send(SCI_SETEMPTYSELECTION, 0, 0);
		send(SCI_ENDUNDOACTION, 0, 0);""",
    "InsertText": """\
		const qint64 current = send(SCI_GETCURRENTPOS, 0, 0);
		const qint64 at = pos == -1 ? current : pos;
		const qint64 lengthBefore = send(SCI_GETLENGTH, 0, 0);
		if (at < 0 || at > lengthBefore)
			return; // as the message does: Document::CheckPosition rejects it

		send(SCI_SETEMPTYSELECTION, at, 0);
		send(SCI_ADDTEXT, textBytes.size(), reinterpret_cast<qint64>(textBytes.constData()));
		const qint64 inserted = send(SCI_GETLENGTH, 0, 0) - lengthBefore;
		send(SCI_SETEMPTYSELECTION, current > at ? current + inserted : current, 0);""",
    "ReplaceSel": """\
		send(SCI_BEGINUNDOACTION, 0, 0);
		send(SCI_REPLACESEL, 0, reinterpret_cast<qint64>(""));
		send(SCI_ADDTEXT, textBytes.size(), reinterpret_cast<qint64>(textBytes.constData()));
		send(SCI_SCROLLCARET, 0, 0);
		send(SCI_ENDUNDOACTION, 0, 0);""",
}

HEADER_PROLOGUE: Final = """\
// GENERATED by tools/generate_scintilla_edit.py from src/scintilla/include/Scintilla.iface.
// Do not edit by hand -- re-run `make generate` instead.
//
// The class exposed to Python as ScintillaEdit (see __init__.py): one typed
// method per Scintilla message, with text as QString (Python str) and raw data
// as QByteArray (Python bytes). See tools/generate_scintilla_edit.py.
#ifndef SCINTILLA_EDIT_FIXED_H
#define SCINTILLA_EDIT_FIXED_H

#include <QByteArray>
#include <QColor>
#include <QPair>
#include <QRect>
#include <QString>

#include <ScintillaDocument.h>

#include "scintilla_edit_base_fixed.h"

class QPaintDevice;

class ScintillaEditFixed : public ScintillaEditBaseFixed {
	Q_OBJECT

public:
	explicit ScintillaEditFixed(QWidget *parent = nullptr);

	// Hand-written (not one-to-one with a Scintilla.iface feature). get_doc()
	// is implemented in Python (__init__.py), so it returns the public
	// ScintillaDocument class rather than the ScintillaDocumentFixed binding.
	QPair<int, int> find_text(int flags, const QString &text, int cpMin, int cpMax) const;
	QPair<int, int> findText(int flags, const QString &text, int cpMin, int cpMax) const;
	QString get_text_range(int start, int end) const;
	QString textRange(int start, int end) const;
	// The document's bytes as stored (in its encoding), without decoding --
	// for byte-offset consumers such as parsers, avoiding a str round trip.
	QByteArray getBytes() const;
	QByteArray getBytes(int start, int end) const;
	void set_doc(ScintillaDocument *pdoc_);
	long format_range(bool draw, QPaintDevice *target, QPaintDevice *measure, const QRect &print_rect,
			  const QRect &page_rect, long range_start, long range_end) const;
	long formatRange(bool draw, QPaintDevice *target, QPaintDevice *measure, const QRect &print_rect,
			 const QRect &page_rect, long range_start, long range_end) const;

	// Generated, one per Scintilla.iface feature.
"""

HEADER_EPILOGUE: Final = """\
};

#endif /* SCINTILLA_EDIT_FIXED_H */
"""

SOURCE_PROLOGUE: Final = """\
// GENERATED by tools/generate_scintilla_edit.py from src/scintilla/include/Scintilla.iface.
// Do not edit by hand -- re-run `make generate` instead.
#include "scintilla_edit_fixed.h"

#include <QPaintDevice>
#include <QVariant>

#include "scintilla_colour.h"
#include "scintilla_text_encoding.h"

ScintillaEditFixed::ScintillaEditFixed(QWidget *parent) : ScintillaEditBaseFixed(parent) {}

QPair<int, int> ScintillaEditFixed::find_text(int flags, const QString &text, int cpMin, int cpMax) const {
	const QByteArray bytes = bytesForDocument(*this, text);
	Sci_TextToFindFull ft{};
	ft.chrg.cpMin = cpMin;
	ft.chrg.cpMax = cpMax;
	ft.chrgText.cpMin = cpMin;
	ft.chrgText.cpMax = cpMax;
	ft.lpstrText = bytes.constData();
	const qint64 start = send(SCI_FINDTEXTFULL, flags, reinterpret_cast<qint64>(&ft));
	return {static_cast<int>(start), static_cast<int>(ft.chrgText.cpMax)};
}

QPair<int, int> ScintillaEditFixed::findText(int flags, const QString &text, int cpMin, int cpMax) const {
	return find_text(flags, text, cpMin, cpMax);
}

QString ScintillaEditFixed::get_text_range(int start, int end) const {
	return stringFromDocument(*this, getBytes(start, end));
}

QString ScintillaEditFixed::textRange(int start, int end) const {
	return get_text_range(start, end);
}

QByteArray ScintillaEditFixed::getBytes() const {
	return sendr(SCI_GETTEXT, static_cast<quint64>(send(SCI_GETLENGTH, 0, 0)));
}

QByteArray ScintillaEditFixed::getBytes(int start, int end) const {
	// Clamp like Editor::GetTextRange resolves the range (-1 = to the end),
	// so the buffer is sized for what Scintilla actually writes.
	const int length = static_cast<int>(send(SCI_GETLENGTH, 0, 0));
	if (end < 0 || end > length)
		end = length;
	start = qBound(0, start, end);
	QByteArray bytes(end - start + 1, '\\0');
	Sci_TextRangeFull tr{{start, end}, bytes.data()};
	send(SCI_GETTEXTRANGEFULL, 0, reinterpret_cast<qint64>(&tr));
	bytes.chop(1); // the terminating NUL
	return bytes;
}

void ScintillaEditFixed::set_doc(ScintillaDocument *pdoc_) {
	send(SCI_SETDOCPOINTER, 0, reinterpret_cast<qint64>(pdoc_->pointer()));
}

long ScintillaEditFixed::format_range(bool draw, QPaintDevice *target, QPaintDevice *measure,
				      const QRect &print_rect, const QRect &page_rect, long range_start,
				      long range_end) const {
	Sci_RangeToFormatFull to_format{};
	to_format.hdc = target;
	to_format.hdcTarget = measure;
	to_format.rc = {print_rect.left(), print_rect.top(), print_rect.right(), print_rect.bottom()};
	to_format.rcPage = {page_rect.left(), page_rect.top(), page_rect.right(), page_rect.bottom()};
	to_format.chrg.cpMin = range_start;
	to_format.chrg.cpMax = range_end;
	return static_cast<long>(send(SCI_FORMATRANGEFULL, draw, reinterpret_cast<qint64>(&to_format)));
}

long ScintillaEditFixed::formatRange(bool draw, QPaintDevice *target, QPaintDevice *measure,
				     const QRect &print_rect, const QRect &page_rect, long range_start,
				     long range_end) const {
	return format_range(draw, target, measure, print_rect, page_rect, range_start, range_end);
}
"""


def normalised_name(name: str, feature_type: str) -> str:
    """WidgetGen's qtStyle `normalisedName()`: drop "Get" from getters, lowercase the first letter."""
    if feature_type == "get":
        name = name.replace("Get", "")
    return name[0].lower() + name[1:]


def param_name(name: str) -> str:
    """WidgetGen's parameter naming: the iface name with its first letter lowercased."""
    return name[0].lower() + name[1:]


# Scintilla's packed colour types, and whether each carries alpha: `colour`
# is 0xBBGGRR, `colouralpha` 0xAABBGGRR. Exposed as QColor (issue #17),
# converted by scintilla_colour.h.
COLOUR_TYPES: Final = {"colour": False, "colouralpha": True}

# A graphical position or size. Methods take/return logical pixels, as
# upstream's WidgetGen does since 5.6.4: the engine works in device pixels
# under SCALE_TECHNIQUE_PIXEL_ALIGNED, so they scale by the viewport's
# "ScintillaScale" property, which ScintillaQt sets to the device-pixel ratio
# in that mode and to 0.0 (meaning: don't scale) otherwise.
PIXELS_TYPE: Final = "pixels"

# Suffix of a pixels method's twin with unrounded `double` pixels (WidgetGen's
# qtStyle `floatSuffix()`).
FLOAT_SUFFIX: Final = "F"

PIXEL_SCALE_PROLOGUE: Final = """\
	const double sciScaleProp = viewport()->property("ScintillaScale").toDouble();
	const double sciScale = sciScaleProp ? sciScaleProp : 1.0;"""


def scalar_type(iface_type: str, float_variant: bool = False) -> str:
    """C++ type of a non-string iface type: QColor for colours, double for a float twin's pixels, else bool/integer."""
    if iface_type in COLOUR_TYPES:
        return "QColor"
    if float_variant and iface_type == PIXELS_TYPE:
        return "double"
    return "bool" if iface_type == "bool" else "qint64"


def has_pixels(feature: dict[str, str]) -> bool:
    """Whether any of this feature's slots is a pixel value (and so gets a float twin)."""
    return PIXELS_TYPE in (feature["ReturnType"], feature["Param1Type"], feature["Param2Type"])


def is_generated(feature: dict[str, str]) -> bool:
    """Whether WidgetGen would emit a method for this feature (non-deprecated, understood types)."""
    if feature["FeatureType"] not in ("fun", "get", "set") or feature["Category"] == "Deprecated":
        return False
    types = (feature["ReturnType"], feature["Param1Type"], feature["Param2Type"])
    return all(t in UNDERSTOOD_TYPES or Face.IsEnumeration(t) for t in types)


class Method:
    """One generated ScintillaEditFixed method: its declaration and definition."""

    def __init__(self, name: str, feature: dict[str, str], float_variant: bool = False) -> None:
        self.__iface_name: Final = name
        self.__feature: Final = feature
        # Whether this is a pixels method's `...F` twin, with `double` pixels.
        self.__float_variant: Final = float_variant
        self.__message: Final = "SCI_" + name.upper()
        self.__kind: Final = "bytes" if name in BYTES_FEATURES else "utf8" if name in UTF8_FEATURES else "text"
        self.__string_result: Final = feature["Param2Type"] == "stringresult"
        # A `position length` first parameter that only sizes the second
        # (string, cells or result buffer) argument: computed, not passed.
        self.__computed_length: Final = feature["Param1Name"] == "length" and feature["Param2Type"] in (
            "string",
            "cells",
            "stringresult",
        )
        self.__base_name: Final = normalised_name(name, feature["FeatureType"])
        self.__name: Final = self.__base_name + (FLOAT_SUFFIX if float_variant else "")
        self.__const: Final = " const" if feature["FeatureType"] == "get" else ""

    def __string_param_type(self) -> str:
        """C++ type of a string/cells parameter of this method."""
        return "const QByteArray &" if self.__kind == "bytes" else "const QString &"

    def __params(self) -> list[tuple[str, str, str]]:
        """(iface type, C++ type, name) of each C++ parameter, in order."""
        params = []
        for slot in ("Param1", "Param2"):
            iface_type, name = self.__feature[slot + "Type"], self.__feature[slot + "Name"]
            if not iface_type or iface_type == "stringresult":
                continue
            if slot == "Param1" and self.__computed_length:
                continue
            if iface_type in ("string", "cells"):
                cpp_type = self.__string_param_type()
            elif iface_type in COLOUR_TYPES:
                cpp_type = f"const {scalar_type(iface_type)} &"
            else:
                cpp_type = scalar_type(iface_type, self.__float_variant) + " "
            params.append((iface_type, cpp_type, param_name(name)))
        return params

    def __return_type(self) -> str:
        """C++ return type of this method."""
        if self.__iface_name == CUR_LINE_FEATURE:
            return "QPair<QString, int>"
        if self.__string_result:
            return "QByteArray" if self.__kind == "bytes" else "QString"
        return_type = self.__feature["ReturnType"]
        return "void" if return_type == "void" else scalar_type(return_type, self.__float_variant)

    def __signature(self, qualified: bool) -> str:
        """`<return> [ScintillaEditFixed::]<name>(<params>)[ const]`."""
        params = ", ".join(f"{cpp_type}{name}" for _, cpp_type, name in self.__params())
        scope = "ScintillaEditFixed::" if qualified else ""
        return f"{self.__return_type()} {scope}{self.__name}({params}){self.__const}"

    def __bytes_var(self, name: str) -> str:
        """Variable holding the bytes passed to Scintilla for string parameter `name`."""
        return name if self.__kind == "bytes" else f"{name}Bytes"

    def __encode(self, name: str) -> str:
        """Expression turning QString parameter `name` into the bytes Scintilla expects."""
        if self.__kind == "utf8":
            return f"{name}.toUtf8()"
        return f"bytesForDocument(*this, {name})"

    def __decode(self, name: str) -> str:
        """Expression turning result buffer `name` into this method's return value."""
        if self.__kind == "bytes":
            return name
        if self.__kind == "utf8":
            return f"QString::fromUtf8({name})"
        return f"stringFromDocument(*this, {name})"

    @property
    def name(self) -> str:
        """The method's (Python-visible) name."""
        return self.__name

    @property
    def base_name(self) -> str:
        """The name of the method this one is a float twin of; its own name otherwise."""
        return self.__base_name

    def doc_note(self) -> str:
        """Docstring note naming the wrapped message and how this method's signature differs from it.

        Lets someone reading Scintilla's own documentation map each message to
        this API; the general rules (text is `str`, positions are bytes) are
        documented once, in docs/pyside6-scintilla/bindings.md, not repeated per method.
        """
        param2 = param_name(self.__feature["Param2Name"]) if self.__feature["Param2Name"] else ""
        notes = [f"Sends `{self.__message}`."]
        if self.__string_result:
            note = f"Returns the result instead of filling a `{param2}` buffer"
            if self.__computed_length:
                note += ", so there's no `length` buffer-size argument"
            if self.__iface_name == CUR_LINE_FEATURE:
                note += "; returns `(text, caret)`, the caret's byte offset in the line being the message's result"
            elif self.__feature["ReturnType"] != "void":
                note += "; the message's own result (the length) is dropped"
            notes.append(note + ".")
        elif self.__computed_length:
            encoded = "" if self.__kind == "bytes" else "encoded "
            notes.append(f"No `length` argument: it's the byte length of the {encoded}`{param2}`.")
        colour_types = sorted(
            {self.__feature[k] for k in ("ReturnType", "Param1Type", "Param2Type")} & COLOUR_TYPES.keys()
        )
        if colour_types:
            packed = " / ".join("`0xAABBGGRR`" if COLOUR_TYPES[c] else "`0xBBGGRR`" for c in colour_types)
            alpha = "with" if "colouralpha" in colour_types else "without"
            note = f"Uses a `QColor` ({alpha} alpha) where the message uses a packed {packed} int."
            if self.__feature["ReturnType"] == "colouralpha":
                note += " The message's 0 result for an unset value is `QColor(0, 0, 0, 0)`, transparent black."
            notes.append(note)
        if has_pixels(self.__feature):
            if self.__float_variant:
                notes.append(f"Like `{self.__base_name}()`, but with pixels as unrounded `float` logical pixels.")
            else:
                notes.append(
                    "Pixels are logical pixels: under `ScaleTechnique.PixelAligned` they're converted (rounded) "
                    "to/from the device pixels the message uses, so `send()` differs from this method there. "
                    f"`{self.__base_name}{FLOAT_SUFFIX}()` is the unrounded `float` form."
                )
        if self.__iface_name in NUL_SAFE_FALLBACKS:
            notes.append(
                "Unlike the message (a NUL-terminated string), keeps embedded NUL characters: "
                "text containing one is inserted with `SCI_ADDTEXT` and an explicit length instead."
            )
        return " ".join(notes)

    def declaration(self) -> str:
        """Header line declaring this method."""
        return f"\t{self.__signature(qualified=False)};"

    def definition(self) -> str:
        """Source block defining this method."""
        body: list[str] = [PIXEL_SCALE_PROLOGUE] if has_pixels(self.__feature) else []
        args: dict[str, str] = {}
        for iface_type, _, name in self.__params():
            if iface_type in ("string", "cells"):
                if self.__kind != "bytes":
                    body.append(f"\tconst QByteArray {name}Bytes = {self.__encode(name)};")
                args[name] = f"reinterpret_cast<qint64>({self.__bytes_var(name)}.constData())"
            elif iface_type in COLOUR_TYPES:
                with_alpha = "true" if COLOUR_TYPES[iface_type] else "false"
                args[name] = f"colourToScintilla({name}, {with_alpha})"
            elif iface_type == PIXELS_TYPE:
                args[name] = f"qRound64({name} * sciScale)"
            else:
                args[name] = name
        fallback = NUL_SAFE_FALLBACKS.get(self.__iface_name)
        if fallback:
            body += ["\tif (textBytes.contains('\\0')) {", fallback, "\t\treturn;", "\t}"]

        def arg(slot: str) -> str:
            """Expression passed as this slot's wParam/lParam."""
            iface_type, name = self.__feature[slot + "Type"], self.__feature[slot + "Name"]
            if not iface_type:
                return "0"
            if slot == "Param1" and self.__computed_length:
                if self.__string_result:
                    return "size"
                return f"{self.__bytes_var(param_name(self.__feature['Param2Name']))}.size()"
            return args[param_name(name)]

        if self.__string_result:
            wparam = "0" if self.__computed_length else arg("Param1")
            length_in_wparam = "true" if self.__computed_length else "false"
            if self.__iface_name == CUR_LINE_FEATURE:
                body.append("\tqint64 caret = 0;")
                body.append(f"\tconst QByteArray result = stringResult({self.__message}, 0, true, &caret);")
                body.append(f"\treturn {{{self.__decode('result')}, static_cast<int>(caret)}};")
            else:
                body.append(
                    f"\treturn {self.__decode(f'stringResult({self.__message}, {wparam}, {length_in_wparam})')};"
                )
        else:
            send = f"send({self.__message}, {arg('Param1')}, {arg('Param2')})"
            return_type = self.__return_type()
            if return_type == "void":
                body.append(f"\t{send};")
            elif return_type == "bool":
                body.append(f"\treturn {send} != 0;")
            elif return_type == "QColor":
                with_alpha = "true" if COLOUR_TYPES[self.__feature["ReturnType"]] else "false"
                body.append(f"\treturn colourFromScintilla({send}, {with_alpha});")
            elif self.__feature["ReturnType"] == PIXELS_TYPE:
                scaled = f"{send} / sciScale"
                body.append(f"\treturn {scaled if self.__float_variant else f'qRound64({scaled})'};")
            else:
                body.append(f"\treturn {send};")
        return "\n".join([self.__signature(qualified=True) + " {", *body, "}", ""])


def methods(face: Face.Face) -> list[Method]:
    """Every generated method, in Scintilla.iface order, each pixels method followed by its float twin."""
    result = []
    for name in face.order:
        feature = face.features[name]
        if name in DROPPED_FEATURES or not is_generated(feature):
            continue
        result.append(Method(name, feature))
        if has_pixels(feature):
            result.append(Method(name, feature, float_variant=True))
    return result


def read_face() -> Face.Face:
    """The parsed vendored Scintilla.iface."""
    face = Face.Face()
    face.ReadFromFile(str(IFACE_PATH))
    return face


def doc_notes() -> dict[str, str]:
    """Each generated method's `Method.doc_note()`, by method name -- used by tools/generate_pyi.py."""
    return {m.name: m.doc_note() for m in methods(read_face())}


def float_twin_bases() -> dict[str, str]:
    """Each `...F` float twin's name, mapped to the method it's a twin of -- used by tools/generate_pyi.py."""
    return {m.name: m.base_name for m in methods(read_face()) if m.name != m.base_name}


def render(face: Face.Face) -> tuple[str, str]:
    """The generated header and source text."""
    all_methods = methods(face)
    header = HEADER_PROLOGUE + "\n".join(m.declaration() for m in all_methods) + "\n" + HEADER_EPILOGUE
    source = SOURCE_PROLOGUE + "\n" + "\n".join(m.definition() for m in all_methods)
    return header, source


def main() -> int:
    """Write (or, with --check, verify) scintilla_edit_fixed.{h,cpp}."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="fail if the checked-in output is out of date")
    check = parser.parse_args().check

    stale = []
    for path, text in zip((HEADER_PATH, SOURCE_PATH), render(read_face()), strict=True):
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current == text:
            continue
        if check:
            stale.append(path)
        else:
            path.write_text(text, encoding="utf-8", newline="\n")
            print(f"wrote {path.relative_to(PACKAGE_ROOT)}")
    if stale:
        names = ", ".join(str(p.relative_to(PACKAGE_ROOT)) for p in stale)
        print(f"out of date: {names} -- run `make generate`", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
