# _lexilla: nanobind-generated Python bindings for Lexilla's CreateLexer/
# ILexer5 (see _binding.cpp), linked against the vendored sources built by
# src/lexilla_core/.
#
# STABLE_ABI compiles against Python's limited API (Py_LIMITED_API=0x030C0000)
# so one cp312 build is forward-compatible with 3.13, 3.14, etc. (cp312-abi3
# wheel tag, one per platform instead of one per Python version). nanobind
# requires CPython >= 3.12 for this, hence lexilla's requires-python.
nanobind_add_module(_lexilla STABLE_ABI _binding.cpp)
target_link_libraries(_lexilla PRIVATE lexilla_core)

install(TARGETS _lexilla LIBRARY DESTINATION lexilla)
