cmake_minimum_required(VERSION 3.25)

# scikit-build-core sets SKBUILD/SKBUILD_PROJECT_NAME when building via
# `uv sync`/`pip install`. Default it so `cmake --preset venv` also works for
# local iteration.
if(NOT SKBUILD)
    message(STATUS "Running CMake directly.")
    set(SKBUILD_PROJECT_NAME lexilla)
endif()

project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Python 3.11 REQUIRED COMPONENTS Interpreter Development.Module)

# nanobind ships as a Python package, not a CMake package on disk -- ask it
# for its own CMake config dir and add that to the search path.
execute_process(
    COMMAND "${Python_EXECUTABLE}" -m nanobind --cmake_dir
    OUTPUT_STRIP_TRAILING_WHITESPACE
    OUTPUT_VARIABLE NB_DIR)
list(APPEND CMAKE_PREFIX_PATH "${NB_DIR}")
find_package(nanobind CONFIG REQUIRED)

# _lexilla: nanobind-generated Python bindings for Lexilla (currently a
# placeholder -- see src/lexilla/bindings/_binding.cpp and
# docs/specs/roadmap.md). Once src/lexilla_vendor/ is vendored, a
# lexilla_core-style subdirectory will build it and this target will link
# against it, mirroring pyside6-scintilla's src/scintilla_qt/.
add_subdirectory(src/lexilla/bindings)
