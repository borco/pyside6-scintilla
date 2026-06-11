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

find_package(Qt6 REQUIRED COMPONENTS Core Gui Widgets Core5Compat)
qt6_standard_project_setup()

# scintilla_qt: vendored Scintilla core + ScintillaEditBase Qt widget (shared library)
add_subdirectory(src/scintilla_qt)
# _pyside6_scintilla: shiboken6-generated Python bindings for ScintillaEditBase
add_subdirectory(src/pyside6_scintilla/bindings)
