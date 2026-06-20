import lexilla


def test_version():
    """Package version is set (regression test for the dynamic version provider)."""
    assert lexilla.__version__


def test_get_lexer_count():
    """Lexilla's lexer catalogue is populated, not empty."""
    assert lexilla.get_lexer_count() > 0


def test_get_lexer_name():
    """Lexer names are resolvable by catalogue index."""
    assert lexilla.get_lexer_name(0)


def test_create_lexer_unknown_name_returns_none():
    """An unrecognized lexer name returns None instead of raising."""
    assert lexilla.create_lexer("not-a-real-lexer-name") is None


def test_create_lexer_cpp():
    """A known lexer name creates a Lexer with a usable name and pointer."""
    lexer = lexilla.create_lexer("cpp")
    assert lexer is not None
    assert lexer.name == "cpp"
    assert lexer.pointer != 0


def test_lexer_property_get_set():
    """Property values round-trip through PropertySet/PropertyGet."""
    lexer = lexilla.create_lexer("cpp")
    assert lexer is not None
    lexer.property_set("lexer.cpp.track.preprocessor", "0")
    assert lexer.property_get("lexer.cpp.track.preprocessor") == "0"


def test_lexer_detach_then_use_raises():
    """detach() hands back the pointer and stops the wrapper from touching the lexer further."""
    lexer = lexilla.create_lexer("cpp")
    assert lexer is not None
    pointer = lexer.detach()
    assert pointer != 0

    raised = False
    try:
        lexer.name
    except RuntimeError:
        raised = True
    assert raised
