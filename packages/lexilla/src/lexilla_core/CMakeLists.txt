# Builds vendored Lexilla (../lexilla_vendor) as a static library that
# src/lexilla/bindings links against. Mirrors pyside6-scintilla's
# src/scintilla_qt/ in spirit, but Lexilla has no Qt/widget layer to add --
# this is just the vendored sources themselves.
#
# Lexilla's own ../lexilla_vendor/src/makefile builds the same source set by
# globbing lexlib/*.cxx and lexers/Lex*.cxx (see LEXLIB_OBJS/LEXERS there) --
# globbing here mirrors that and means newly added lexer files are picked up
# automatically on the next CMake configure, with no list to maintain.

set(LIB_NAME lexilla_core)

set(LEXILLA_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../lexilla_vendor)
set(SCINTILLA_INTERFACE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../scintilla_interface)

file(GLOB LEXLIB_SOURCES ${LEXILLA_DIR}/lexlib/*.cxx)
file(GLOB LEXER_SOURCES ${LEXILLA_DIR}/lexers/Lex*.cxx)

add_library(${LIB_NAME} STATIC
    ${LEXILLA_DIR}/src/Lexilla.cxx
    ${LEXLIB_SOURCES}
    ${LEXER_SOURCES}
)

target_include_directories(${LIB_NAME}
    PUBLIC
    ${LEXILLA_DIR}/include
    ${SCINTILLA_INTERFACE_DIR}/include
    PRIVATE
    ${LEXILLA_DIR}/lexlib
)

set_target_properties(${LIB_NAME} PROPERTIES POSITION_INDEPENDENT_CODE ON)
