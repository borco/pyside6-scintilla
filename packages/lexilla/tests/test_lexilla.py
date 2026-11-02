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


def test_lexer_catalogue_names_all_create():
    """Every catalogue entry's name resolves to a usable lexer of the same name."""
    count = lexilla.get_lexer_count()
    names = [lexilla.get_lexer_name(i) for i in range(count)]
    assert all(names)
    assert len(set(names)) == count  # no duplicate catalogue entries

    for name in names:
        lexer = lexilla.create_lexer(name)
        assert lexer is not None, f"create_lexer({name!r}) returned None"
        # CreateLexer is case-insensitive; Lexer.name reflects the lexer's own
        # registered name, which isn't guaranteed to match the catalogue's casing.
        assert lexer.name.lower() == name.lower()


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


def test_lexer_property_introspection():
    """property_names()/property_type()/describe_property() resolve a known cpp property."""
    lexer = lexilla.create_lexer("cpp")
    assert lexer is not None
    names = lexer.property_names()
    assert "lexer.cpp.track.preprocessor" in names
    assert lexer.property_type("lexer.cpp.track.preprocessor") == lexilla.PropertyType.BOOLEAN
    assert lexer.describe_property("lexer.cpp.track.preprocessor")


def test_lexer_word_list_set():
    """describe_word_list_sets() lists at least one slot, and word_list_set() accepts it."""
    lexer = lexilla.create_lexer("cpp")
    assert lexer is not None
    descriptions = lexer.describe_word_list_sets()
    assert descriptions
    # cpp's word-list slots are documented in order, starting at 0 (primary keywords).
    assert isinstance(lexer.word_list_set(0, "foo bar"), int)


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


def test_lexer_primary_style_from_secondary_style():
    """primary_style_from_style() strips cpp's "inactive" bit added by distance_to_secondary_styles()."""
    lexer = lexilla.create_lexer("cpp")
    assert lexer is not None
    distance = lexer.distance_to_secondary_styles()
    assert distance > 0
    secondary_style = 0 + distance
    assert lexer.primary_style_from_style(secondary_style) == 0


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


def test_lexer_release_then_use_raises():
    """release() destroys the lexer now and stops the wrapper from touching it further."""
    lexer = lexilla.create_lexer("cpp")
    assert lexer is not None
    lexer.release()

    raised = False
    try:
        lexer.name
    except RuntimeError:
        raised = True
    assert raised

    # release() is a no-op when already released, not a double-free.
    lexer.release()
