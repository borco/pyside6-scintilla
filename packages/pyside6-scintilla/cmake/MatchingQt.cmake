# Finds the Qt SDK matching the PySide6 this build compiles against.
#
# PySide6's headers only compile against the Qt release they were built for
# (issue #15), so the Qt SDK's major.minor must equal PySide6's. If
# CMAKE_PREFIX_PATH (the CMake variable or the environment variable) already
# provides a matching Qt -- as in CI -- it's used as is. Otherwise the standard
# install locations are searched for the PySide6 version, e.g.
# C:/Qt/6.12.0/msvc2022_64 or ~/Qt/6.12.0/macos, and the newest matching patch
# release found is prepended to CMAKE_PREFIX_PATH (issue #25). find_qt_matching_pyside6()
# then finds Qt6 and fails with a clear message if its version doesn't match.

# The Qt version a Qt6 SDK prefix provides, or "" if it isn't one.
function(_qt_sdk_version prefix out_var)
    set(impl "${prefix}/lib/cmake/Qt6/Qt6ConfigVersionImpl.cmake")
    set(version "")
    if(EXISTS "${impl}")
        file(STRINGS "${impl}" line REGEX "set\\(PACKAGE_VERSION \"[0-9.]+\"\\)" LIMIT_COUNT 1)
        if(line MATCHES "\"([0-9.]+)\"")
            set(version "${CMAKE_MATCH_1}")
        endif()
    endif()
    set(${out_var} "${version}" PARENT_SCOPE)
endfunction()

# Qt's directory name for this platform's desktop SDK under <root>/<version>/.
function(_qt_sdk_arch_dirs out_var)
    if(WIN32)
        if(CMAKE_SYSTEM_PROCESSOR MATCHES "ARM64|arm64")
            set(dirs msvc2022_arm64)
        else()
            set(dirs msvc2022_64)
        endif()
    elseif(APPLE)
        set(dirs macos clang_64)
    elseif(CMAKE_SYSTEM_PROCESSOR MATCHES "aarch64|arm64")
        set(dirs gcc_arm64)
    else()
        set(dirs gcc_64)
    endif()
    set(${out_var} ${dirs} PARENT_SCOPE)
endfunction()

macro(find_qt_matching_pyside6)
    find_package(Python COMPONENTS Interpreter REQUIRED)
    execute_process(
        COMMAND ${Python_EXECUTABLE} -c "import importlib.metadata as m; print(m.version('PySide6-Essentials'))"
        OUTPUT_VARIABLE PYSIDE6_VERSION
        OUTPUT_STRIP_TRAILING_WHITESPACE
        RESULT_VARIABLE _pyside6_result
    )
    if(NOT _pyside6_result EQUAL 0 OR NOT PYSIDE6_VERSION MATCHES "^([0-9]+\\.[0-9]+)")
        message(FATAL_ERROR "PySide6-Essentials isn't installed for ${Python_EXECUTABLE}; it's a build requirement.")
    endif()
    set(_pyside6_minor "${CMAKE_MATCH_1}")

    # Does CMAKE_PREFIX_PATH already provide a matching Qt?
    set(_qt_matching "")
    foreach(_prefix IN LISTS CMAKE_PREFIX_PATH)
        _qt_sdk_version("${_prefix}" _version)
        if(_version MATCHES "^${_pyside6_minor}\\.")
            set(_qt_matching "${_prefix}")
            break()
        endif()
    endforeach()
    if(NOT _qt_matching AND DEFINED ENV{CMAKE_PREFIX_PATH})
        cmake_path(CONVERT "$ENV{CMAKE_PREFIX_PATH}" TO_CMAKE_PATH_LIST _env_prefixes)
        foreach(_prefix IN LISTS _env_prefixes)
            _qt_sdk_version("${_prefix}" _version)
            if(_version MATCHES "^${_pyside6_minor}\\.")
                set(_qt_matching "${_prefix}")
                break()
            endif()
        endforeach()
    endif()

    # If not, look in the standard install locations, preferring PySide6's
    # exact version, then the newest patch release of the same minor.
    if(NOT _qt_matching)
        set(_roots "")
        if(WIN32)
            list(APPEND _roots "C:/Qt")
        endif()
        foreach(_home_var IN ITEMS HOME USERPROFILE)
            if(DEFINED ENV{${_home_var}})
                cmake_path(CONVERT "$ENV{${_home_var}}" TO_CMAKE_PATH_LIST _home)
                list(APPEND _roots "${_home}/Qt")
            endif()
        endforeach()
        if(UNIX)
            list(APPEND _roots "/opt/Qt" "/opt/qt")
        endif()
        _qt_sdk_arch_dirs(_arch_dirs)
        set(_candidates "")
        foreach(_root IN LISTS _roots)
            file(GLOB _version_dirs LIST_DIRECTORIES true "${_root}/${_pyside6_minor}.*")
            list(SORT _version_dirs COMPARE NATURAL ORDER DESCENDING)
            foreach(_version_dir IN LISTS _version_dirs)
                foreach(_arch IN LISTS _arch_dirs)
                    _qt_sdk_version("${_version_dir}/${_arch}" _version)
                    if(_version STREQUAL PYSIDE6_VERSION)
                        list(PREPEND _candidates "${_version_dir}/${_arch}")
                    elseif(_version MATCHES "^${_pyside6_minor}\\.")
                        list(APPEND _candidates "${_version_dir}/${_arch}")
                    endif()
                endforeach()
            endforeach()
        endforeach()
        if(_candidates)
            list(GET _candidates 0 _qt_matching)
            list(PREPEND CMAKE_PREFIX_PATH "${_qt_matching}")
            message(STATUS "Using Qt SDK ${_qt_matching} (matches PySide6 ${PYSIDE6_VERSION})")
        endif()
    endif()

    find_package(Qt6 COMPONENTS Core Gui Widgets Core5Compat)
    if(NOT Qt6_FOUND OR NOT Qt6_VERSION MATCHES "^${_pyside6_minor}\\.")
        if(Qt6_FOUND)
            set(_found "found Qt ${Qt6_VERSION} at ${Qt6_DIR}")
        else()
            set(_found "found no Qt6 SDK")
        endif()
        message(FATAL_ERROR
            "PySide6 ${PYSIDE6_VERSION} needs a Qt ${_pyside6_minor}.x SDK with the Qt 5 Compatibility "
            "module, but CMake ${_found}. Install Qt ${PYSIDE6_VERSION} with the Qt "
            "MaintenanceTool (into C:/Qt or ~/Qt, where it's found automatically) or point "
            "CMAKE_PREFIX_PATH at it.")
    endif()
endmacro()
