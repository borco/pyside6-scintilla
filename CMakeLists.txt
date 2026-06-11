cmake_minimum_required(VERSION 3.25)

if(NOT SKBUILD)
    message(STATUS "Running CMake directly.")
    set(SKBUILD_PROJECT_NAME pyside6_scintilla)
endif()

project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_AUTOMOC ON)

find_package(Qt6 REQUIRED COMPONENTS Core Gui Widgets Core5Compat)
qt6_standard_project_setup()

add_subdirectory(src/scintilla_qt)
add_subdirectory(src/pyside6_scintilla/bindings)
