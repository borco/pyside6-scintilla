# Generates and builds the `_pyside6_scintilla` extension module: shiboken6
# turns bindings.h + bindings.xml into the wrapper sources listed in
# GENERATED_SOURCES below (see docs/BINDINGS.md for what each one contains),
# which are then compiled and linked against `scintilla_qt`
# (../../scintilla_qt) and Qt.

find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)

# Shiboken6Tools isn't found by find_package() out of the box, so locate it
# in the active Python environment's site-packages.
execute_process(
    COMMAND ${Python_EXECUTABLE} -c "import sysconfig; print(sysconfig.get_paths()['purelib'])"
    OUTPUT_VARIABLE Python_SITELIB
    OUTPUT_STRIP_TRAILING_WHITESPACE
)
list(APPEND CMAKE_PREFIX_PATH "${Python_SITELIB}/shiboken6_generator/lib/cmake")

find_package(Shiboken6Tools REQUIRED)

set(SCINTILLA_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../../scintilla)

set(GENERATED_SOURCES
    ${CMAKE_CURRENT_BINARY_DIR}/_pyside6_scintilla/scintilla_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/_pyside6_scintilla/scintilla_notificationdata_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/_pyside6_scintilla/scintillaeditbase_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/_pyside6_scintilla/_pyside6_scintilla_module_wrapper.cpp
)

shiboken_generator_create_binding(
    EXTENSION_TARGET _pyside6_scintilla
    GENERATED_SOURCES ${GENERATED_SOURCES}
    HEADERS ${CMAKE_CURRENT_SOURCE_DIR}/bindings.h
    TYPESYSTEM_FILE ${CMAKE_CURRENT_SOURCE_DIR}/bindings.xml
    LIBRARY_TARGET scintilla_qt
    QT_MODULES Core Gui Widgets
    SHIBOKEN_EXTRA_OPTIONS
        -I${SCINTILLA_DIR}/include
        -I${SCINTILLA_DIR}/src
        -I${SCINTILLA_DIR}/qt/ScintillaEditBase
)

if(WIN32)
    # <windows.h> (pulled in transitively via Python.h before any Qt header
    # can set this) otherwise drags in <commdlg.h>, which #defines FindText
    # as FindTextA/FindTextW and mangles Scintilla::Message::FindText in the
    # generated wrapper sources.
    target_compile_definitions(_pyside6_scintilla PRIVATE WIN32_LEAN_AND_MEAN)
endif()

# _pyside6_scintilla.{pyd,so} links against scintilla_qt; install it into the
# same package directory and point the loader at that directory.
if(APPLE)
    set_target_properties(_pyside6_scintilla PROPERTIES INSTALL_RPATH "@loader_path")
elseif(UNIX)
    set_target_properties(_pyside6_scintilla PROPERTIES INSTALL_RPATH "$ORIGIN")
endif()

install(TARGETS _pyside6_scintilla DESTINATION pyside6_scintilla)
install(TARGETS scintilla_qt
    RUNTIME DESTINATION pyside6_scintilla
    LIBRARY DESTINATION pyside6_scintilla
)

if(WIN32)
    # Qt6Core5Compat isn't bundled with the PySide6 wheel, so scintilla_qt's
    # dependency on it would otherwise only be found via a Qt SDK install on
    # PATH/CMAKE_PREFIX_PATH. Ship it alongside scintilla_qt.dll instead.
    install(FILES $<TARGET_FILE:Qt6::Core5Compat> DESTINATION pyside6_scintilla)
elseif(UNIX AND NOT APPLE)
    # Same as the Windows case above, but scintilla_qt.so records Qt6Core5Compat's
    # SONAME (libQt6Core5Compat.so.6) as its NEEDED entry, not the fully-versioned
    # filename (libQt6Core5Compat.so.6.11.1) that TARGET_FILE gives. Installing
    # TARGET_SONAME_FILE instead would copy that SONAME symlink as a dangling
    # link (its .so.6.11.1 target never gets installed), which scikit-build-core
    # then silently drops from the wheel - so install the real file and rename
    # it to the SONAME the loader/auditwheel expect.
    install(FILES $<TARGET_FILE:Qt6::Core5Compat> DESTINATION pyside6_scintilla RENAME libQt6Core5Compat.so.6)
endif()
