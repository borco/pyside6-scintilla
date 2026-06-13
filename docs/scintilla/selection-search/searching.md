# Searching [:material-link-variant:](https://www.scintilla.org/ScintillaDoc.html#Searching "Upstream documentation"){ .heading-link }

!!! note
    This page is adapted from the upstream Scintilla **5.6.3** documentation
    (`ScintillaDoc.html`), converted to Markdown for this site. It documents
    the underlying `ScintillaEditBase.send`/`sends` message API -- see the
    [API reference](../../reference.md) for the Python bindings themselves.

There are methods to search for text and for regular expressions. Most applications should use [`SCI_SEARCHINTARGET`](#SCI_SEARCHINTARGET) as the basis for their search implementations. Other calls augment this or were implemented before `SCI_SEARCHINTARGET`.

The base regular expression support is limited and should only be used for simple cases and initial development. The C++ runtime `<regex>` library may be used by setting the `SCFIND_CXX11REGEX` search flag. The C++11 `<regex>` support may be disabled by compiling Scintilla with `NO_CXX11_REGEX` defined. A different regular expression library can be integrated into Scintilla or can be called from the container using direct access to the buffer contents through `SCI_GETCHARACTERPOINTER`.

## Search and replace using the target [:material-link-variant:](https://www.scintilla.org/ScintillaDoc.html#SearchAndReplaceUsingTheTarget "Upstream documentation"){ .heading-link }

Searching can be performed within the target range with `SCI_SEARCHINTARGET`, which uses a counted string to allow searching for null characters. It returns the position of the start of the matching text range or -1 for failure, in which case the target is not moved. The flags used by `SCI_SEARCHINTARGET` such as `SCFIND_MATCHCASE`, `SCFIND_WHOLEWORD`, `SCFIND_WORDSTART`, and `SCFIND_REGEXP` can be set with `SCI_SETSEARCHFLAGS`.

- [`SCI_SETTARGETSTART(position start)`](#SCI_SETTARGETSTART)
- [`SCI_GETTARGETSTART → position`](#SCI_GETTARGETSTART)
- [`SCI_SETTARGETSTARTVIRTUALSPACE(position space)`](#SCI_SETTARGETSTARTVIRTUALSPACE)
- [`SCI_GETTARGETSTARTVIRTUALSPACE → position`](#SCI_GETTARGETSTARTVIRTUALSPACE)
- [`SCI_SETTARGETEND(position end)`](#SCI_SETTARGETEND)
- [`SCI_GETTARGETEND → position`](#SCI_GETTARGETEND)
- [`SCI_SETTARGETENDVIRTUALSPACE(position space)`](#SCI_SETTARGETENDVIRTUALSPACE)
- [`SCI_GETTARGETENDVIRTUALSPACE → position`](#SCI_GETTARGETENDVIRTUALSPACE)
- [`SCI_SETTARGETRANGE(position start, position end)`](#SCI_SETTARGETRANGE)
- [`SCI_TARGETFROMSELECTION`](#SCI_TARGETFROMSELECTION)
- [`SCI_TARGETWHOLEDOCUMENT`](#SCI_TARGETWHOLEDOCUMENT)
- [`SCI_SETSEARCHFLAGS(int searchFlags)`](#SCI_SETSEARCHFLAGS)
- [`SCI_GETSEARCHFLAGS → int`](#SCI_GETSEARCHFLAGS)
- [`SCI_SEARCHINTARGET(position length, const char *text) → position`](#SCI_SEARCHINTARGET)
- [`SCI_GETTARGETTEXT(<unused>, char *text) → position`](#SCI_GETTARGETTEXT)
- [`SCI_REPLACETARGET(position length, const char *text) → position`](#SCI_REPLACETARGET)
- [`SCI_REPLACETARGETMINIMAL(position length, const char *text) → position`](#SCI_REPLACETARGETMINIMAL)
- [`SCI_REPLACETARGETRE(position length, const char *text) → position`](#SCI_REPLACETARGETRE)
- [`SCI_GETTAG(int tagNumber, char *tagValue) → int`](#SCI_GETTAG)

### `SCI_SETTARGETSTART(position start)` {: #SCI_SETTARGETSTART }

### `SCI_GETTARGETSTART → position` {: #SCI_GETTARGETSTART }

### `SCI_SETTARGETSTARTVIRTUALSPACE(position space)` {: #SCI_SETTARGETSTARTVIRTUALSPACE }

### `SCI_GETTARGETSTARTVIRTUALSPACE → position` {: #SCI_GETTARGETSTARTVIRTUALSPACE }

### `SCI_SETTARGETEND(position end)` {: #SCI_SETTARGETEND }

### `SCI_GETTARGETEND → position` {: #SCI_GETTARGETEND }

### `SCI_SETTARGETENDVIRTUALSPACE(position space)` {: #SCI_SETTARGETENDVIRTUALSPACE }

### `SCI_GETTARGETENDVIRTUALSPACE → position` {: #SCI_GETTARGETENDVIRTUALSPACE }

### `SCI_SETTARGETRANGE(position start, position end)` {: #SCI_SETTARGETRANGE }

These functions set and return the start and end of the target. When searching you can set start greater than end to find the last matching text in the target rather than the first matching text. Setting a target position with `SCI_SETTARGETSTART`, `SCI_SETTARGETEND`, or `SCI_SETTARGETRANGE` sets the virtual space to 0. The target is also set by a successful `SCI_SEARCHINTARGET`.

The virtual space of the target range can be set and retrieved with the corresponding `...VIRTUALSPACE` methods. This allows text to be inserted in virtual space more easily.

### `SCI_TARGETFROMSELECTION` {: #SCI_TARGETFROMSELECTION }

Set the target start and end to the start and end positions of the selection.

### `SCI_TARGETWHOLEDOCUMENT` {: #SCI_TARGETWHOLEDOCUMENT }

Set the target start to the start of the document and target end to the end of the document.

### `SCI_SETSEARCHFLAGS(int searchFlags)` {: #SCI_SETSEARCHFLAGS }

### `SCI_GETSEARCHFLAGS → int` {: #SCI_GETSEARCHFLAGS }

These get and set the [`searchFlags`](#searchFlags) used by `SCI_SEARCHINTARGET`. There are several option flags including a simple regular expression search.

### `SCI_SEARCHINTARGET(position length, const char *text) → position` {: #SCI_SEARCHINTARGET }

This searches for the first occurrence of a text string in the target defined by `SCI_SETTARGETSTART` and `SCI_SETTARGETEND`. The text string is not zero terminated; the size is set by `length`. The search is modified by the search flags set by `SCI_SETSEARCHFLAGS`. If the search succeeds, the target is set to the found text and the return value is the position of the start of the matching text. If the search fails, the result is -1.

### `SCI_GETTARGETTEXT(<unused>, char *text) → position` {: #SCI_GETTARGETTEXT }

Retrieve the value in the target.

### `SCI_REPLACETARGET(position length, const char *text) → position` {: #SCI_REPLACETARGET }

If `length` is -1, `text` is a zero terminated string, otherwise `length` sets the number of character to replace the target with. After replacement, the target range refers to the replacement text. The return value is the length of the replacement string.
Note that the recommended way to delete text in the document is to set the target to the text to be removed, and to perform a replace target with an empty string.

### `SCI_REPLACETARGETMINIMAL(position length, const char *text) → position` {: #SCI_REPLACETARGETMINIMAL }

This is similar to [`SCI_REPLACETARGET`](#SCI_REPLACETARGET) but tries to minimize change history when the current target text shares a common prefix or suffix with the replacement. Only the text that is actually different is marked as changed. This might be used when automatically reformatting some text so that the whole area formatted doesn't show change marks. If `length` is -1, `text` is a zero terminated string, otherwise `length` sets the number of character to replace the target with. After replacement, the target range refers to the replacement text. The return value is the length of the replacement string.
Note that the recommended way to delete text in the document is to set the target to the text to be removed, and to perform a replace target with an empty string.

### `SCI_REPLACETARGETRE(position length, const char *text) → position` {: #SCI_REPLACETARGETRE }

This replaces the target using regular expressions. If `length` is -1, `text` is a zero terminated string, otherwise `length` is the number of characters to use. The replacement string is formed from the text string with any sequences of `\1` through `\9` replaced by tagged matches from the most recent regular expression search. `\0` is replaced with all the matched text from the most recent search. After replacement, the target range refers to the replacement text. The return value is the length of the replacement string.

### `SCI_GETTAG(int tagNumber, char *tagValue NUL-terminated) → int` {: #SCI_GETTAG }

Discover what text was matched by tagged expressions in a regular expression search. This is useful if the application wants to interpret the replacement string itself.

See also: [`SCI_FINDTEXT`](#SCI_FINDTEXT)

### `searchFlags` {: #searchFlags }

Several of the search routines use flag options, which include a simple regular expression search. Combine the flag options by adding them:

| | |
| --- | --- |
| `SCFIND_NONE` | Default setting is case-insensitive literal match. |
| `SCFIND_MATCHCASE` | A match only occurs with text that matches the case of the search string. |
| `SCFIND_WHOLEWORD` | A match only occurs if the characters before and after are not word characters as defined by `SCI_SETWORDCHARS`. |
| `SCFIND_WORDSTART` | A match only occurs if the character before is not a word character as defined by `SCI_SETWORDCHARS`. |
| `SCFIND_REGEXP` | The search string should be interpreted as a regular expression. Uses Scintilla's base implementation unless combined with `SCFIND_CXX11REGEX`. |
| `SCFIND_POSIX` | Treat regular expression in a more POSIX compatible manner by interpreting bare ( and ) for tagged sections rather than `\(` and `\)`. Has no effect when `SCFIND_CXX11REGEX` is set. |
| `SCFIND_CXX11REGEX` | This flag may be set to use C++11 `<regex>` instead of Scintilla's basic regular expressions. If the regular expression is invalid then -1 is returned and status is set to `SC_STATUS_WARN_REGEX`. The ECMAScript flag is set on the regex object and UTF-8 documents will exhibit Unicode-compliant behaviour. For MSVC, where wchar_t is 16-bits, the regular expression ".." will match a single astral-plane character. There may be other differences between compilers. Must also have `SCFIND_REGEXP` set. |

In a regular expression, using Scintilla's base implementation, special characters interpreted are:

| | |
| --- | --- |
| `.` | Matches any character |
| `\(` | This marks the start of a region for tagging a match. |
| `\)` | This marks the end of a tagged region. |
| `\n` | Where `n` is 1 through 9 refers to the first through ninth tagged region when replacing. For example, if the search string was `Fred\([1-9]\)XXX` and the replace string was `Sam\1YYY`, when applied to `Fred2XXX` this would generate `Sam2YYY`. `\0` refers to all of the matching text. |
| `\<` | This matches the start of a word using Scintilla's definitions of words. |
| `\>` | This matches the end of a word using Scintilla's definition of words. |
| `\x` | This allows you to use a character x that would otherwise have a special meaning. For example, `\[` would be interpreted as `[` and not as the start of a character set. |
| `[...]` | This indicates a set of characters, for example, `[abc]` means any of the characters a, b or c. You can also use ranges, for example `[a-z]` for any lower case character. |
| `[^...]` | The complement of the characters in the set. For example, `[^A-Za-z]` means any character except an alphabetic character. |
| `^` | This matches the start of a line (unless used inside a set, see above). |
| `$` | This matches the end of a line. |
| `*` | This matches 0 or more times. For example, `Sa*m` matches `Sm`, `Sam`, `Saam`, `Saaam` and so on. |
| `+` | This matches 1 or more times. For example, `Sa+m` matches `Sam`, `Saam`, `Saaam` and so on. |

Regular expressions will only match ranges within a single line, never matching over multiple lines.

When using `SCFIND_CXX11REGEX` more features are available, generally similar to regular expression support in JavaScript. See the documentation of your C++ runtime for details on what is supported.

- [`SCI_FINDTEXT(int searchFlags, Sci_TextToFind *ft) → position`](#SCI_FINDTEXT)
- [`SCI_FINDTEXTFULL(int searchFlags, Sci_TextToFindFull *ft) → position`](#SCI_FINDTEXTFULL)
- [`SCI_SEARCHANCHOR`](#SCI_SEARCHANCHOR)
- [`SCI_SEARCHNEXT(int searchFlags, const char *text) → position`](#SCI_SEARCHNEXT)
- [`SCI_SEARCHPREV(int searchFlags, const char *text) → position`](#SCI_SEARCHPREV)

### `SCI_FINDTEXT(int searchFlags, Sci_TextToFind *ft) → position` {: #SCI_FINDTEXT }

### `SCI_FINDTEXTFULL(int searchFlags, Sci_TextToFindFull *ft) → position` {: #SCI_FINDTEXTFULL }

These messages search for text in the document. They do not use or move the current selection. The `searchFlags` argument controls the search type, which includes regular expression searches.

You can search backwards to find the previous occurrence of a search string by setting the end of the search range before the start.

The `Sci_TextToFind` and `Sci_TextToFindFull` structures are defined in `Scintilla.h`; set `chrg.cpMin` and `chrg.cpMax` with the range of positions in the document to search. You can search backwards by setting `chrg.cpMax` less than `chrg.cpMin`. Set the `lpstrText` member of `Sci_TextToFind` to point at a zero terminated text string holding the search pattern. If your language makes the use of `Sci_TextToFind` difficult, you should consider using `SCI_SEARCHINTARGET` instead. On 64-bit Win32, `SCI_FINDTEXT` is limited to the first 2G of text and `SCI_FINDTEXTFULL` removes this limitation.

The return value is -1 if the search fails or the position of the start of the found text if it succeeds. The `chrgText.cpMin` and `chrgText.cpMax` members of `Sci_TextToFind` are filled in with the start and end positions of the found text.

See also: [`SCI_SEARCHINTARGET`](#SCI_SEARCHINTARGET)

### `Sci_TextToFind` {: #Sci_TextToFind }

This structure is defined to have exactly the same shape as the Win32 structure `FINDTEXTEX` for old code that treated Scintilla as a RichEdit control.

```c
struct Sci_TextToFind {
    struct Sci_CharacterRange chrg;     // range to search
    const char *lpstrText;                // the search pattern (zero terminated)
    struct Sci_CharacterRange chrgText; // returned as position of matching text
};
```

### `Sci_TextToFindFull` {: #Sci_TextToFindFull }

This structure extends `Sci_TextToFind` to support huge documents on Win32.

```c
struct Sci_TextToFindFull {
    struct Sci_CharacterRangeFull chrg;     // range to search
    const char *lpstrText;                // the search pattern (zero terminated)
    struct Sci_CharacterRangeFull chrgText; // returned as position of matching text
};
```

### `SCI_SEARCHANCHOR` {: #SCI_SEARCHANCHOR }

### `SCI_SEARCHNEXT(int searchFlags, const char *text) → position` {: #SCI_SEARCHNEXT }

### `SCI_SEARCHPREV(int searchFlags, const char *text) → position` {: #SCI_SEARCHPREV }

These messages provide relocatable search support. This allows multiple incremental interactive searches to be macro recorded while still setting the selection to found text so the find/select operation is self-contained. These three messages send `SCN_MACRORECORD` notifications if macro recording is enabled.

`SCI_SEARCHANCHOR` sets the search start point used by `SCI_SEARCHNEXT` and `SCI_SEARCHPREV` to the start of the current selection, that is, the end of the selection that is nearer to the start of the document. You should always call this before calling either of `SCI_SEARCHNEXT` or `SCI_SEARCHPREV`.

`SCI_SEARCHNEXT` and `SCI_SEARCHPREV` search for the next and previous occurrence of the zero terminated search string pointed at by text. The search is modified by the `searchFlags`.

The return value is -1 if nothing is found, otherwise the return value is the start position of the matching text. The selection is updated to show the matched text, but is not scrolled into view.

See also: [`SCI_SEARCHINTARGET`](#SCI_SEARCHINTARGET), [`SCI_FINDTEXT`](#SCI_FINDTEXT)
