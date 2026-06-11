# Builds vendored Scintilla (../scintilla) plus its Qt widget glue
# (PlatQt/ScintillaQt/ScintillaEditBase) as a shared library. This is the
# library that src/pyside6_scintilla/bindings links against.
#
# The source list mirrors ../scintilla/qt/ScintillaEditBase/ScintillaEditBase.pro.
# When vendoring a new Scintilla release, diff that .pro file's SOURCES/HEADERS
# against the list below and add/remove entries to match (see docs/BINDINGS.md).

set(LIB_NAME scintilla_qt)

set(SCINTILLA_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../scintilla)

qt_add_library(${LIB_NAME} SHARED
    # vendored Scintilla core (from scintilla/qt/ScintillaEditBase/ScintillaEditBase.pro)
    ${SCINTILLA_DIR}/include/ILexer.h
    ${SCINTILLA_DIR}/include/Scintilla.h
    ${SCINTILLA_DIR}/src/AutoComplete.cxx
    ${SCINTILLA_DIR}/src/AutoComplete.h
    ${SCINTILLA_DIR}/src/CallTip.cxx
    ${SCINTILLA_DIR}/src/CallTip.h
    ${SCINTILLA_DIR}/src/CaseConvert.cxx
    ${SCINTILLA_DIR}/src/CaseConvert.h
    ${SCINTILLA_DIR}/src/CaseFolder.cxx
    ${SCINTILLA_DIR}/src/CaseFolder.h
    ${SCINTILLA_DIR}/src/CellBuffer.cxx
    ${SCINTILLA_DIR}/src/CellBuffer.h
    ${SCINTILLA_DIR}/src/ChangeHistory.cxx
    ${SCINTILLA_DIR}/src/ChangeHistory.h
    ${SCINTILLA_DIR}/src/CharacterCategoryMap.cxx
    ${SCINTILLA_DIR}/src/CharacterCategoryMap.h
    ${SCINTILLA_DIR}/src/CharacterType.cxx
    ${SCINTILLA_DIR}/src/CharacterType.h
    ${SCINTILLA_DIR}/src/CharClassify.cxx
    ${SCINTILLA_DIR}/src/CharClassify.h
    ${SCINTILLA_DIR}/src/ContractionState.cxx
    ${SCINTILLA_DIR}/src/ContractionState.h
    ${SCINTILLA_DIR}/src/DBCS.cxx
    ${SCINTILLA_DIR}/src/Decoration.cxx
    ${SCINTILLA_DIR}/src/Decoration.h
    ${SCINTILLA_DIR}/src/Document.cxx
    ${SCINTILLA_DIR}/src/Document.h
    ${SCINTILLA_DIR}/src/EditModel.cxx
    ${SCINTILLA_DIR}/src/Editor.cxx
    ${SCINTILLA_DIR}/src/Editor.h
    ${SCINTILLA_DIR}/src/EditView.cxx
    ${SCINTILLA_DIR}/src/Geometry.cxx
    ${SCINTILLA_DIR}/src/Geometry.h
    ${SCINTILLA_DIR}/src/Indicator.cxx
    ${SCINTILLA_DIR}/src/Indicator.h
    ${SCINTILLA_DIR}/src/KeyMap.cxx
    ${SCINTILLA_DIR}/src/KeyMap.h
    ${SCINTILLA_DIR}/src/LineMarker.cxx
    ${SCINTILLA_DIR}/src/LineMarker.h
    ${SCINTILLA_DIR}/src/MarginView.cxx
    ${SCINTILLA_DIR}/src/Partitioning.h
    ${SCINTILLA_DIR}/src/PerLine.cxx
    ${SCINTILLA_DIR}/src/PerLine.h
    ${SCINTILLA_DIR}/src/Platform.h
    ${SCINTILLA_DIR}/src/PositionCache.cxx
    ${SCINTILLA_DIR}/src/PositionCache.h
    ${SCINTILLA_DIR}/src/RESearch.cxx
    ${SCINTILLA_DIR}/src/RESearch.h
    ${SCINTILLA_DIR}/src/RunStyles.cxx
    ${SCINTILLA_DIR}/src/RunStyles.h
    ${SCINTILLA_DIR}/src/ScintillaBase.cxx
    ${SCINTILLA_DIR}/src/ScintillaBase.h
    ${SCINTILLA_DIR}/src/Selection.cxx
    ${SCINTILLA_DIR}/src/Selection.h
    ${SCINTILLA_DIR}/src/SplitVector.h
    ${SCINTILLA_DIR}/src/Style.cxx
    ${SCINTILLA_DIR}/src/Style.h
    ${SCINTILLA_DIR}/src/UndoHistory.cxx
    ${SCINTILLA_DIR}/src/UndoHistory.h
    ${SCINTILLA_DIR}/src/UniConversion.cxx
    ${SCINTILLA_DIR}/src/UniConversion.h
    ${SCINTILLA_DIR}/src/UniqueString.cxx
    ${SCINTILLA_DIR}/src/ViewStyle.cxx
    ${SCINTILLA_DIR}/src/ViewStyle.h
    ${SCINTILLA_DIR}/src/XPM.cxx
    ${SCINTILLA_DIR}/src/XPM.h

    # Qt widget: ScintillaEditBase
    ${SCINTILLA_DIR}/qt/ScintillaEditBase/PlatQt.cpp
    ${SCINTILLA_DIR}/qt/ScintillaEditBase/PlatQt.h
    ${SCINTILLA_DIR}/qt/ScintillaEditBase/ScintillaEditBase.cpp
    ${SCINTILLA_DIR}/qt/ScintillaEditBase/ScintillaEditBase.h
    ${SCINTILLA_DIR}/qt/ScintillaEditBase/ScintillaQt.cpp
    ${SCINTILLA_DIR}/qt/ScintillaEditBase/ScintillaQt.h
)

target_include_directories(${LIB_NAME}
    PUBLIC
    ${SCINTILLA_DIR}/include
    ${SCINTILLA_DIR}/qt/ScintillaEditBase
    # ScintillaEditBase.h pulls in Debugging.h/Geometry.h/Platform.h from here
    ${SCINTILLA_DIR}/src
)

target_link_libraries(${LIB_NAME}
    PUBLIC
    Qt6::Widgets
    Qt6::Core5Compat # vendored Scintilla's PlatQt.cpp uses QTextCodec
)

target_compile_definitions(${LIB_NAME}
    PUBLIC
    SCINTILLA_QT=1

    # On Windows, MAKING_LIBRARY=1 makes EXPORT_IMPORT_API expand to dllexport
    # while building this library, and dllimport when consumed by the bindings.
    PRIVATE
    MAKING_LIBRARY=1
)

# By default the prefix of the shared library is "lib" on UNIX; use no prefix everywhere.
set_property(TARGET ${LIB_NAME} PROPERTY PREFIX "")
