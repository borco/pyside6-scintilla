# Lexilla API

Lexilla's own API is small: a few library-level functions to create lexers by
name and list them, and the `ILexer5` interface every lexer implements. The
`lexilla` package exposes it as-is:

| Lexilla (C++) | `lexilla` (Python) |
| --- | --- |
| `CreateLexer(name)` | [`create_lexer(name)`](../../reference/lexilla.md) -- `name` is a `Language` member or its string |
| `GetLexerCount()`, `GetLexerName(index)` | `get_lexer_count()`, `get_lexer_name(index)` |
| `ILexer5` | `Lexer` -- properties, word lists, named styles, sub-styles |
| `SCLEX_*` identifiers | `LanguageIdentifier` |
| `SC_TYPE_*` property types | `PropertyType` |

The upstream reference is [LexillaDoc.html](https://www.scintilla.org/LexillaDoc.html).
What each lexer does with its properties, keyword sets and styles is
lexer-specific; ask the lexer itself:

```python
from lexilla import Language, create_lexer

lexer = create_lexer(Language.CPP)
assert lexer is not None
print(lexer.property_names())          # one property name per line
print(lexer.describe_property("fold"))
print(lexer.describe_word_list_sets())  # what each setKeyWords() set is for
for style in range(lexer.named_styles()):
    print(style, lexer.name_of_style(style), lexer.description_of_style(style))
```

Once a lexer is handed to an editor (`set_lexer()`, or `SCI_SETILEXER`), it's
configured through the editor's Scintilla messages instead -- `setProperty()`,
`setKeyWords()`, `styleSetFore()`, ... -- see the
[Scintilla API](../scintilla/index.md)'s Styling & Lexing section and the
[lexilla highlighting example](../../highlighting/lexilla_highlighting.md).
