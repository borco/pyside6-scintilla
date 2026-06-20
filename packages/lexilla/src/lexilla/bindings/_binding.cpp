#include <cstdint>
#include <memory>

#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h>
#include <nanobind/stl/unique_ptr.h>

#include "ILexer.h"
#include "Lexilla.h"

namespace nb = nanobind;
using Scintilla::ILexer5;

namespace {

// Wraps a single ILexer5* returned by CreateLexer(). Owns it (and calls
// Release() on destruction) until detach() hands ownership to a Scintilla
// editor via SCI_SETILEXER -- see docs/specs/mission.md's "Cross-binding
// integration" decision.
class Lexer {
public:
    explicit Lexer(ILexer5 *lexer) noexcept : lexer_(lexer) {}
    ~Lexer() { ReleaseIfOwned(); }

    Lexer(const Lexer &) = delete;
    Lexer &operator=(const Lexer &) = delete;

    std::uintptr_t Pointer() const { return reinterpret_cast<std::uintptr_t>(Require()); }

    // Hands ownership to the caller (typically a Scintilla editor via
    // SCI_SETILEXER, which will call Release() itself later). After this,
    // the wrapper no longer touches the lexer.
    std::uintptr_t Detach() {
        const std::uintptr_t ptr = reinterpret_cast<std::uintptr_t>(Require());
        owned_ = false;
        lexer_ = nullptr;
        return ptr;
    }

    // Releases the lexer now instead of waiting for garbage collection.
    // No-op if already detached or released.
    void ReleaseNow() { ReleaseIfOwned(); }

    const char *Name() { return Require()->GetName(); }
    int Identifier() { return Require()->GetIdentifier(); }

    const char *PropertyNames() { return Require()->PropertyNames(); }
    int PropertyType(const char *name) { return Require()->PropertyType(name); }
    const char *DescribeProperty(const char *name) { return Require()->DescribeProperty(name); }
    Sci_Position PropertySet(const char *key, const char *value) { return Require()->PropertySet(key, value); }
    const char *PropertyGet(const char *key) { return Require()->PropertyGet(key); }

    const char *DescribeWordListSets() { return Require()->DescribeWordListSets(); }
    Sci_Position WordListSet(int n, const char *wordList) { return Require()->WordListSet(n, wordList); }

private:
    ILexer5 *Require() const {
        if (!lexer_) {
            throw std::runtime_error("Lexer has been detached or released; this instance no longer owns an ILexer5");
        }
        return lexer_;
    }

    void ReleaseIfOwned() {
        if (owned_ && lexer_) {
            lexer_->Release();
        }
        lexer_ = nullptr;
    }

    ILexer5 *lexer_;
    bool owned_ = true;
};

std::unique_ptr<Lexer> CreateLexerWrapper(const char *name) {
    ILexer5 *lexer = ::CreateLexer(name);
    if (!lexer) {
        return nullptr;
    }
    return std::make_unique<Lexer>(lexer);
}

std::string GetLexerNameWrapper(unsigned int index) {
    char buffer[256];
    ::GetLexerName(index, buffer, sizeof(buffer));
    return std::string(buffer);
}

} // namespace

NB_MODULE(_lexilla, m) {
    nb::class_<Lexer>(m, "Lexer")
        .def_prop_ro("pointer", &Lexer::Pointer,
            "Raw ILexer5* as a plain int, e.g. for SCI_SETILEXER. Does not transfer ownership.")
        .def("detach", &Lexer::Detach,
            "Hand ownership to the caller (e.g. a Scintilla editor) and stop managing this lexer's lifetime.")
        .def("release", &Lexer::ReleaseNow,
            "Release the lexer now rather than waiting for garbage collection. No-op if detached or already released.")
        .def_prop_ro("name", &Lexer::Name,
            "This lexer's name, as passed to create_lexer().")
        .def_prop_ro("identifier", &Lexer::Identifier,
            "This lexer's numeric language identifier (see SCLEX_* in SciLexer.h).")
        .def("property_names", &Lexer::PropertyNames,
            "Newline-separated list of property keys this lexer recognizes via property_set/property_get.")
        .def("property_type", &Lexer::PropertyType, nb::arg("name"),
            "Value type of the named property: 0=boolean, 1=integer, 2=string (SC_TYPE_* in Scintilla.h).")
        .def("describe_property", &Lexer::DescribeProperty, nb::arg("name"),
            "Human-readable description of what the named property controls.")
        .def("property_set", &Lexer::PropertySet, nb::arg("key"), nb::arg("value"),
            "Set a lexer property; returns a Sci_Position invalidation hint (lexer-specific, often 0).")
        .def("property_get", &Lexer::PropertyGet, nb::arg("key"),
            "Current value of a lexer property previously set via property_set, or its default.")
        .def("describe_word_list_sets", &Lexer::DescribeWordListSets,
            "Newline-separated description of each word-list slot accepted by word_list_set.")
        .def("word_list_set", &Lexer::WordListSet, nb::arg("n"), nb::arg("word_list"),
            "Set word-list slot n (see describe_word_list_sets) to a space-separated list of words.");

    m.def("create_lexer", &CreateLexerWrapper, nb::arg("name"),
        "Create a lexer by name (e.g. \"cpp\"), or None if no lexer has that name.");
    m.def("get_lexer_count", &GetLexerCount,
        "Number of lexers in Lexilla's catalogue, for iterating get_lexer_name(0..count-1).");
    m.def("get_lexer_name", &GetLexerNameWrapper, nb::arg("index"),
        "Name of the lexer at the given catalogue index, suitable for passing to create_lexer().");
}
