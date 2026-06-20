

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
    def identifier(self) -> int:
        """This lexer's numeric language identifier (see SCLEX_* in SciLexer.h)."""

    def property_names(self) -> str:
        """
        Newline-separated list of property keys this lexer recognizes via property_set/property_get.
        """

    def property_type(self, name: str) -> int:
        """
        Value type of the named property: 0=boolean, 1=integer, 2=string (SC_TYPE_* in Scintilla.h).
        """

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
