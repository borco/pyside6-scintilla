#include <nanobind/nanobind.h>

namespace nb = nanobind;

// Placeholder module: proves the nanobind + CMake + scikit-build-core
// toolchain builds, installs, and loads end to end. Replace with real
// CreateLexer/ILexer5 bindings once vendor/lexilla/ is vendored
// (see docs/specs/roadmap.md).
NB_MODULE(_lexilla, m) {
    m.def("smoke_test", []() { return "lexilla"; });
}
