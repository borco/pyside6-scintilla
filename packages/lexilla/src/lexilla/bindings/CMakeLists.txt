# _lexilla: nanobind-generated Python bindings for Lexilla's CreateLexer/
# ILexer5 (see _binding.cpp), linked against the vendored sources built by
# src/lexilla_core/.
nanobind_add_module(_lexilla _binding.cpp)
target_link_libraries(_lexilla PRIVATE lexilla_core)

install(TARGETS _lexilla LIBRARY DESTINATION lexilla)
