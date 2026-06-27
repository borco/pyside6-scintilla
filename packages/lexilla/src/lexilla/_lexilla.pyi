import enum


class PropertyType(enum.IntEnum):
    """
    Value type of a lexer property (see Lexer.property_type), mirroring Scintilla.h's SC_TYPE_*.
    """

    BOOLEAN = 0
    """A property whose value is interpreted as 0/1."""

    INTEGER = 1
    """A property whose value is interpreted as an integer."""

    STRING = 2
    """A property whose value is interpreted as a string."""

class LineEndType(enum.IntEnum):
    """
    Line-end styles a lexer supports (see Lexer.line_end_types_supported), mirroring Scintilla.h's SC_LINE_END_TYPE_*.
    """

    DEFAULT = 0
    r"""Only \r, \n, and \r\n are treated as line ends."""

    UNICODE = 1
    """
    Unicode line-end characters (e.g. U+2028 LINE SEPARATOR) are also treated as line ends.
    """

class LanguageIdentifier(enum.IntEnum):
    """
    Numeric language identifier of a lexer (see Lexer.identifier), mirroring SciLexer.h's SCLEX_*.
    """

    CONTAINER = 0
    """Reserved; SCLEX_CONTAINER is defined but has no associated lexer."""

    NULL = 1
    """Reserved; SCLEX_NULL is defined but has no associated lexer."""

    PYTHON = 2
    """Identifier for the "python" lexer."""

    CPP = 3
    """Identifier for the "cpp" lexer."""

    HTML = 4
    """Identifier for the "hypertext" lexer."""

    XML = 5
    """Identifier for the "xml" lexer."""

    PERL = 6
    """Identifier for the "perl" lexer."""

    SQL = 7
    """Identifier for the "sql" lexer."""

    VB = 8
    """Identifier for the "vb" lexer."""

    PROPERTIES = 9
    """Identifier for the "props" lexer."""

    ERRORLIST = 10
    """Identifier for the "errorlist" lexer."""

    MAKEFILE = 11
    """Identifier for the "makefile" lexer."""

    BATCH = 12
    """Identifier for the "batch" lexer."""

    XCODE = 13
    """Reserved; SCLEX_XCODE is defined but has no associated lexer."""

    LATEX = 14
    """Identifier for the "latex" lexer."""

    LUA = 15
    """Identifier for the "lua" lexer."""

    DIFF = 16
    """Identifier for the "diff" lexer."""

    CONF = 17
    """Identifier for the "conf" lexer."""

    PASCAL = 18
    """Identifier for the "pascal" lexer."""

    AVE = 19
    """Identifier for the "ave" lexer."""

    ADA = 20
    """Identifier for the "ada" lexer."""

    LISP = 21
    """Identifier for the "lisp" lexer."""

    RUBY = 22
    """Identifier for the "ruby" lexer."""

    EIFFEL = 23
    """Identifier for the "eiffel" lexer."""

    EIFFELKW = 24
    """Identifier for the "eiffelkw" lexer."""

    TCL = 25
    """Identifier for the "tcl" lexer."""

    NNCRONTAB = 26
    """Identifier for the "nncrontab" lexer."""

    BULLANT = 27
    """Identifier for the "bullant" lexer."""

    VBSCRIPT = 28
    """Identifier for the "vbscript" lexer."""

    BAAN = 31
    """Identifier for the "baan" lexer."""

    MATLAB = 32
    """Identifier for the "matlab" lexer."""

    SCRIPTOL = 33
    """Identifier for the "scriptol" lexer."""

    ASM = 34
    """Identifier for the "asm" lexer."""

    CPPNOCASE = 35
    """Identifier for the "cppnocase" lexer."""

    FORTRAN = 36
    """Identifier for the "fortran" lexer."""

    F77 = 37
    """Identifier for the "f77" lexer."""

    CSS = 38
    """Identifier for the "css" lexer."""

    POV = 39
    """Identifier for the "pov" lexer."""

    LOUT = 40
    """Identifier for the "lout" lexer."""

    ESCRIPT = 41
    """Identifier for the "escript" lexer."""

    PS = 42
    """Identifier for the "ps" lexer."""

    NSIS = 43
    """Identifier for the "nsis" lexer."""

    MMIXAL = 44
    """Identifier for the "mmixal" lexer."""

    CLW = 45
    """Identifier for the "clarion" lexer."""

    CLWNOCASE = 46
    """Identifier for the "clarionnocase" lexer."""

    LOT = 47
    """Identifier for the "lot" lexer."""

    YAML = 48
    """Identifier for the "yaml" lexer."""

    TEX = 49
    """Identifier for the "tex" lexer."""

    METAPOST = 50
    """Identifier for the "metapost" lexer."""

    POWERBASIC = 51
    """Identifier for the "powerbasic" lexer."""

    FORTH = 52
    """Identifier for the "forth" lexer."""

    ERLANG = 53
    """Identifier for the "erlang" lexer."""

    OCTAVE = 54
    """Identifier for the "octave" lexer."""

    MSSQL = 55
    """Identifier for the "mssql" lexer."""

    VERILOG = 56
    """Identifier for the "verilog" lexer."""

    KIX = 57
    """Identifier for the "kix" lexer."""

    GUI4CLI = 58
    """Identifier for the "gui4cli" lexer."""

    SPECMAN = 59
    """Identifier for the "specman" lexer."""

    AU3 = 60
    """Identifier for the "au3" lexer."""

    APDL = 61
    """Identifier for the "apdl" lexer."""

    BASH = 62
    """Identifier for the "bash" lexer."""

    ASN1 = 63
    """Identifier for the "asn1" lexer."""

    VHDL = 64
    """Identifier for the "vhdl" lexer."""

    CAML = 65
    """Identifier for the "caml" lexer."""

    BLITZBASIC = 66
    """Identifier for the "blitzbasic" lexer."""

    PUREBASIC = 67
    """Identifier for the "purebasic" lexer."""

    HASKELL = 68
    """Identifier for the "haskell" lexer."""

    PHPSCRIPT = 69
    """Identifier for the "phpscript" lexer."""

    TADS3 = 70
    """Identifier for the "tads3" lexer."""

    REBOL = 71
    """Identifier for the "rebol" lexer."""

    SMALLTALK = 72
    """Identifier for the "smalltalk" lexer."""

    FLAGSHIP = 73
    """Identifier for the "flagship" lexer."""

    CSOUND = 74
    """Identifier for the "csound" lexer."""

    FREEBASIC = 75
    """Identifier for the "freebasic" lexer."""

    INNOSETUP = 76
    """Identifier for the "inno" lexer."""

    OPAL = 77
    """Identifier for the "opal" lexer."""

    SPICE = 78
    """Identifier for the "spice" lexer."""

    D = 79
    """Identifier for the "d" lexer."""

    CMAKE = 80
    """Identifier for the "cmake" lexer."""

    GAP = 81
    """Identifier for the "gap" lexer."""

    PLM = 82
    """Identifier for the "PL/M" lexer."""

    PROGRESS = 83
    """Identifier for the "abl" lexer."""

    ABAQUS = 84
    """Identifier for the "abaqus" lexer."""

    ASYMPTOTE = 85
    """Identifier for the "asy" lexer."""

    R = 86
    """Identifier for the "r" lexer."""

    MAGIK = 87
    """Identifier for the "magiksf" lexer."""

    POWERSHELL = 88
    """Identifier for the "powershell" lexer."""

    MYSQL = 89
    """Identifier for the "mysql" lexer."""

    PO = 90
    """Identifier for the "po" lexer."""

    TAL = 91
    """Identifier for the "TAL" lexer."""

    COBOL = 92
    """Identifier for the "COBOL" lexer."""

    TACL = 93
    """Identifier for the "TACL" lexer."""

    SORCUS = 94
    """Identifier for the "sorcins" lexer."""

    POWERPRO = 95
    """Identifier for the "powerpro" lexer."""

    NIMROD = 96
    """Identifier for the "nimrod" lexer."""

    SML = 97
    """Identifier for the "SML" lexer."""

    MARKDOWN = 98
    """Identifier for the "markdown" lexer."""

    TXT2TAGS = 99
    """Identifier for the "txt2tags" lexer."""

    A68K = 100
    """Identifier for the "a68k" lexer."""

    MODULA = 101
    """Identifier for the "modula" lexer."""

    COFFEESCRIPT = 102
    """Identifier for the "coffeescript" lexer."""

    TCMD = 103
    """Identifier for the "tcmd" lexer."""

    AVS = 104
    """Identifier for the "avs" lexer."""

    ECL = 105
    """Identifier for the "ecl" lexer."""

    OSCRIPT = 106
    """Identifier for the "oscript" lexer."""

    VISUALPROLOG = 107
    """Identifier for the "visualprolog" lexer."""

    LITERATEHASKELL = 108
    """Identifier for the "literatehaskell" lexer."""

    STTXT = 109
    """Identifier for the "fcST" lexer."""

    KVIRC = 110
    """Identifier for the "kvirc" lexer."""

    RUST = 111
    """Identifier for the "rust" lexer."""

    DMAP = 112
    """Identifier for the "DMAP" lexer."""

    AS = 113
    """Identifier for the "as" lexer."""

    DMIS = 114
    """Identifier for the "DMIS" lexer."""

    REGISTRY = 115
    """Identifier for the "registry" lexer."""

    BIBTEX = 116
    """Identifier for the "bib" lexer."""

    SREC = 117
    """Identifier for the "srec" lexer."""

    IHEX = 118
    """Identifier for the "ihex" lexer."""

    TEHEX = 119
    """Identifier for the "tehex" lexer."""

    JSON = 120
    """Identifier for the "json" lexer."""

    EDIFACT = 121
    """Identifier for the "edifact" lexer."""

    INDENT = 122
    """Identifier for the "indent" lexer."""

    MAXIMA = 123
    """Identifier for the "maxima" lexer."""

    STATA = 124
    """Identifier for the "stata" lexer."""

    SAS = 125
    """Identifier for the "sas" lexer."""

    NIM = 126
    """Identifier for the "nim" lexer."""

    CIL = 127
    """Identifier for the "cil" lexer."""

    X12 = 128
    """Identifier for the "x12" lexer."""

    DATAFLEX = 129
    """Identifier for the "dataflex" lexer."""

    HOLLYWOOD = 130
    """Identifier for the "hollywood" lexer."""

    RAKU = 131
    """Identifier for the "raku" lexer."""

    FSHARP = 132
    """Identifier for the "fsharp" lexer."""

    JULIA = 133
    """Identifier for the "julia" lexer."""

    ASCIIDOC = 134
    """Identifier for the "asciidoc" lexer."""

    GDSCRIPT = 135
    """Identifier for the "gdscript" lexer."""

    TOML = 136
    """Identifier for the "toml" lexer."""

    TROFF = 137
    """Identifier for the "troff" lexer."""

    DART = 138
    """Identifier for the "dart" lexer."""

    ZIG = 139
    """Identifier for the "zig" lexer."""

    NIX = 140
    """Identifier for the "nix" lexer."""

    SINEX = 141
    """Identifier for the "sinex" lexer."""

    ESCSEQ = 142
    """Identifier for the "escseq" lexer."""

    AUTOMATIC = 1000
    """Sentinel requesting automatic lexer selection; not itself a lexer."""

class Lexer:
    @property
    def pointer(self) -> int:
        """
        Raw ILexer5* as a plain int, e.g. for SCI_SETILEXER. Does not transfer ownership.
        """

    def detach(self) -> int:
        """
        Hand ownership to the caller (e.g. a Scintilla editor) and stop managing this lexer's lifetime.
        """

    def release(self) -> None:
        """
        Release the lexer now rather than waiting for garbage collection. No-op if detached or already released.
        """

    @property
    def name(self) -> str:
        """This lexer's name, as passed to create_lexer()."""

    @property
    def identifier(self) -> LanguageIdentifier:
        """This lexer's language identifier (see the LanguageIdentifier enum)."""

    def property_names(self) -> str:
        """
        Newline-separated list of property keys this lexer recognizes via property_set/property_get.
        """

    def property_type(self, name: str) -> PropertyType:
        """Value type of the named property (see the PropertyType enum)."""

    def describe_property(self, name: str) -> str:
        """Human-readable description of what the named property controls."""

    def property_set(self, key: str, value: str) -> int:
        """
        Set a lexer property; returns a Sci_Position invalidation hint (lexer-specific, often 0).
        """

    def property_get(self, key: str) -> str:
        """
        Current value of a lexer property previously set via property_set, or its default.
        """

    def describe_word_list_sets(self) -> str:
        """
        Newline-separated description of each word-list slot accepted by word_list_set.
        """

    def word_list_set(self, n: int, word_list: str) -> int:
        """
        Set word-list slot n (see describe_word_list_sets) to a space-separated list of words.
        """

    def named_styles(self) -> int:
        """
        Number of named styles this lexer defines (including allocated sub-styles), for iterating name_of_style/tags_of_style/description_of_style(0..named_styles()-1).
        """

    def name_of_style(self, style: int) -> str:
        """
        Symbolic name of a style number (e.g. "SCE_C_DEFAULT" for cpp style 0).
        """

    def tags_of_style(self, style: int) -> str:
        """
        Space-separated semantic tags for a style number (e.g. "literal numeric").
        """

    def description_of_style(self, style: int) -> str:
        """Human-readable description of what a style number represents."""

    def allocate_sub_styles(self, style_base: int, number_styles: int) -> int:
        """
        Allocate number_styles new style numbers derived from style_base (e.g. per-identifier-class highlighting); returns the first allocated style number, or -1 if none could be allocated.
        """

    def sub_styles_start(self, style_base: int) -> int:
        """
        First sub-style number allocated from style_base via allocate_sub_styles, or -1 if none.
        """

    def sub_styles_length(self, style_base: int) -> int:
        """
        Number of sub-styles allocated from style_base via allocate_sub_styles.
        """

    def style_from_sub_style(self, sub_style: int) -> int:
        """Base style a previously allocated sub-style number was derived from."""

    def primary_style_from_style(self, style: int) -> int:
        """
        Primary style a secondary style number maps to (see distance_to_secondary_styles).
        """

    def free_sub_styles(self) -> None:
        """Release all sub-styles previously allocated via allocate_sub_styles."""

    def set_identifiers(self, style: int, identifiers: str) -> None:
        """
        Assign a space-separated list of identifiers to a sub-style number, so the lexer recognizes them as that class (e.g. known type names).
        """

    def distance_to_secondary_styles(self) -> int:
        """
        Offset added to a primary style number to reach its secondary-style counterpart, or 0 if this lexer has none.
        """

    def get_sub_style_bases(self) -> str:
        """
        Style numbers that allocate_sub_styles can be called on for this lexer, as a string with one style number per character (cast each char to int).
        """

    @property
    def line_end_types_supported(self) -> LineEndType:
        """Line-end styles this lexer supports (see the LineEndType enum)."""

    def private_call(self, operation: int, pointer: int) -> int:
        """
        Lexer-specific opaque escape hatch; operation and the address-sized pointer/return value are defined by the individual lexer, if it implements this at all. No lexer in vendored Lexilla 5.5.0 currently does (all stub it as a no-op returning 0).
        """

def create_lexer(name: str) -> Lexer:
    """
    Create a lexer by name (e.g. "cpp"), or None if no lexer has that name.
    """

def get_lexer_count() -> int:
    """
    Number of lexers in Lexilla's catalogue, for iterating get_lexer_name(0..count-1).
    """

def get_lexer_name(index: int) -> str:
    """
    Name of the lexer at the given catalogue index, suitable for passing to create_lexer().
    """
