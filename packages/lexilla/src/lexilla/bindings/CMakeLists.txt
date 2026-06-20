# _lexilla: nanobind-generated Python bindings for Lexilla (currently a
# placeholder -- see _binding.cpp and docs/specs/roadmap.md)
nanobind_add_module(_lexilla _binding.cpp)

install(TARGETS _lexilla LIBRARY DESTINATION lexilla)
