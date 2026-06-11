#ifndef BINDINGS_H
#define BINDINGS_H

#include <cstdint>

#include <ScintillaTypes.h>
#include <ScintillaMessages.h>

// ScintillaStructures.h forward-declares "enum class Message;" (in case
// ScintillaMessages.h isn't included) in addition to the full definition
// above. shiboken sees these as two separate enums and emits duplicate
// converters/type indices for Scintilla::Message, which fails to compile.
// Rename the forward declaration (and the NotificationData::message field
// of that type, removed from the typesystem in bindings.xml) to an unused
// enum so only the real Scintilla::Message definition is seen.
#define Message ScintillaMessageFwdDeclUnused
#include <ScintillaStructures.h>
#undef Message

#include <ScintillaEditBase.h>

// <windows.h> (pulled in transitively via Qt/Python headers) defines FindText
// as a macro to FindTextA/FindTextW, which mangles Scintilla::Message::FindText
// in shiboken-generated code. Undo it for the rest of this translation unit.
#ifdef FindText
#undef FindText
#endif

#endif
