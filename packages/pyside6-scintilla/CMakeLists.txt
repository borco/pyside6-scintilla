cmake_minimum_required(VERSION 3.25)

# scikit-build-core sets SKBUILD/SKBUILD_PROJECT_NAME when building via
# `uv sync`/`pip install`. Default it so `cmake --preset venv` also works for
# local iteration (e.g. re-running shiboken without a full reinstall).
if(NOT SKBUILD)
    message(STATUS "Running CMake directly.")
    set(SKBUILD_PROJECT_NAME pyside6_scintilla)
endif()

project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Required for Scintilla's Qt widgets (ScintillaQt etc.), which use Q_OBJECT.
set(CMAKE_AUTOMOC ON)

include(cmake/MatchingQt.cmake)
find_qt_matching_pyside6()
qt6_standard_project_setup()

if(UNIX AND NOT APPLE AND TARGET WrapOpenGL::WrapOpenGL)
    # Qt6::Gui links OpenGL (libOpenGL/libGLX) into everything that uses it,
    # through this imported target, but nothing here calls OpenGL. Even with
    # --as-needed, ld keeps them: they resolve undefined GL symbols of the Qt
    # SDK's libQt6Gui, which doesn't list them itself. The result was a hard
    # libOpenGL.so.0 dependency (missing on e.g. a minimal Ubuntu 26.04), and
    # auditwheel grafting private libOpenGL/libGLX/libGLdispatch copies into
    # the wheels, next to the system ones PySide6's own Qt6Gui loads (it
    # needs libGL.so.1 itself, so the GL symbols still resolve at runtime).
    # Keep them off our link lines.
    set_target_properties(WrapOpenGL::WrapOpenGL PROPERTIES INTERFACE_LINK_LIBRARIES "")
endif()

# scintilla_qt: vendored Scintilla core + ScintillaEditBase Qt widget (shared library)
add_subdirectory(src/scintilla_qt)
# _pyside6_scintilla: shiboken6-generated Python bindings for ScintillaEditBase
add_subdirectory(src/pyside6_scintilla/bindings)
