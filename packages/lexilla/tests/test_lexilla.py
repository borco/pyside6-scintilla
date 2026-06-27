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


def test_lexer_identifier_is_enum():
    """Lexer.identifier returns a LanguageIdentifier, not a bare int."""
    lexer = lexilla.create_lexer("cpp")
    assert lexer is not None
    assert lexer.identifier == lexilla.LanguageIdentifier.CPP


def test_language_enum_create_lexer_roundtrip():
    """Language enum members are str subclasses usable directly with create_lexer()."""
    lexer = lexilla.create_lexer(lexilla.Language.CPP)
    assert lexer is not None
    assert lexer.name == "cpp"


def test_language_identifier_automatic_sentinel():
    """LanguageIdentifier.AUTOMATIC mirrors SciLexer.h's SCLEX_AUTOMATIC (1000)."""
    assert lexilla.LanguageIdentifier.AUTOMATIC == 1000


def test_lexer_named_styles_introspection():
    """named_styles()/name_of_style()/tags_of_style()/description_of_style() resolve style 0 by name."""
    lexer = lexilla.create_lexer("cpp")
    assert lexer is not None
    assert lexer.named_styles() > 0
    assert lexer.name_of_style(0) == "SCE_C_DEFAULT"
    assert lexer.description_of_style(0)


def test_lexer_sub_styles_roundtrip():
    """A sub-style allocated from a base style is freed and forgotten by free_sub_styles()."""
    lexer = lexilla.create_lexer("cpp")
    assert lexer is not None
    style_base = ord(lexer.get_sub_style_bases()[0])

    sub_style = lexer.allocate_sub_styles(style_base, 2)
    assert sub_style != -1
    assert lexer.sub_styles_start(style_base) == sub_style
    assert lexer.sub_styles_length(style_base) == 2
    assert lexer.style_from_sub_style(sub_style) == style_base
    lexer.set_identifiers(sub_style, "Foo Bar")

    lexer.free_sub_styles()
    assert lexer.sub_styles_length(style_base) == 0


def test_lexer_line_end_types_supported_is_enum():
    """line_end_types_supported returns a LineEndType, not a bare int."""
    lexer = lexilla.create_lexer("cpp")
    assert lexer is not None
    assert isinstance(lexer.line_end_types_supported, lexilla.LineEndType)


def test_lexer_private_call_is_noop_for_cpp():
    """No vendored lexer implements PrivateCall yet; cpp's stub returns 0."""
    lexer = lexilla.create_lexer("cpp")
    assert lexer is not None
    assert lexer.private_call(0, 0) == 0


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
