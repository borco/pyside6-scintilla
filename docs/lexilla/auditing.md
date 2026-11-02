# Auditing the vendored Lexilla source

> [!NOTE]
> Paths on this page are relative to `packages/lexilla/`, except
> repo-level ones (`docs/`, `tools/`, `.github/`, `examples/`).

> [!NOTE]
> `src/lexilla_vendor/` is vendored unmodified from Lexilla's official
> release. If you'd like to confirm that for yourself, here's one way --
> use whatever approach you're comfortable with. Mirrors
> [pyside6-scintilla's docs/auditing.md](https://github.com/borco/scintilla-py/blob/master/docs/auditing.md)
> for its vendored `src/scintilla/`.

Lexilla **5.5.0** is extracted as-is in `src/lexilla_vendor/`.

| Field | Value |
| --- | --- |
| Upstream project | <https://www.scintilla.org/Lexilla.html> |
| Upstream version | 5.5.0 |
| Upstream tag | `rel-5-5-0` (per `version.txt`: `550`) |
| Tarball/zip URL | <https://www.scintilla.org/lexilla550.tgz> |
| Tarball/zip SHA-256 | `8532414359b851e0f100af802c64dfbb5be7fe35d60a8a467331c939d905f6e2` |
| Vendored path | `src/lexilla_vendor` |

After verifying the checksum and extracting the tarball, a tree diff against
`src/lexilla_vendor/` should come back empty:

```sh
tar -xzf lexilla550.tgz --strip-components=1 -C <some-dir>
```

```sh
diff -rq <some-dir> src/lexilla_vendor/
```

## `src/scintilla_interface/` — the two headers Lexilla needs but doesn't ship

`Lexilla.h` says "Must have already included `ILexer.h` to have
`Scintilla::ILexer5` defined" — but `ILexer.h` is a *Scintilla* header, not a
Lexilla one, so it isn't part of the Lexilla tarball above. `ILexer5`
(the interface this binding wraps), `ILexer4`, `IDocument`, and the
`Sci_Position`/`Sci_PositionU` typedefs it uses are all declared there and in
the `Sci_Position.h` it includes. Separately, the individual lexer
implementations under `src/lexilla_vendor/lexers/` `#include "Scintilla.h"`
for a handful of fold-level flag constants and `INVALID_POSITION`
(`SC_FOLDLEVELBASE`, `SC_FOLDLEVELWHITEFLAG`, `SC_FOLDLEVELHEADERFLAG`,
`SC_FOLDLEVELNUMBERMASK`, `SC_FOLDLEVELBOXFOOTERFLAG`) — not, as it might
seem, the per-language `SCE_*` style constants (those already live in
Lexilla's own vendored `include/SciLexer.h`, no extra vendoring needed).

Rather than depend on the whole Scintilla tree (which would reintroduce the
"this package has no Scintilla/Qt dependency" coupling the project
deliberately avoids -- see [lexilla's mission](../specs/lexilla-mission.md)),
only these three headers are copied, unmodified, into
`src/scintilla_interface/include/` (with Scintilla's `License.txt` and
`version.txt`). They are pure interface/constant declarations (no
implementation, no Qt).

### Where the copy comes from

Since the move into the monorepo, the copy is the **Scintilla release the
repo vendors** for pyside6-scintilla (`packages/pyside6-scintilla/src/scintilla/`,
currently 5.6.3 -- see [Verifying vendored Scintilla](../auditing.md) for its
tarball and checksum), byte for byte. `tools/sync_scintilla_headers.py`
copies it, and its `--check` mode (in `make lint` and CI) fails if the copy
drifts. lexilla keeps a copy at all, rather than including the vendored tree,
only because its sdist must build on its own.

(Before the monorepo, lexilla-py vendored the headers from the Scintilla
release matching its Lexilla version's major.minor, 5.5.0. ILexer5,
`Sci_Position` and the fold-level constants are stable across those
releases; the 5.6 `Scintilla.h` only adds messages.)

| Field | Value |
| --- | --- |
| Source | `packages/pyside6-scintilla/src/scintilla/` (the vendored Scintilla) |
| Version | per `src/scintilla_interface/version.txt` (`563` = 5.6.3) |
| Files copied | `include/ILexer.h`, `include/Sci_Position.h`, `include/Scintilla.h`, `License.txt`, `version.txt` |
| Copy path | `src/scintilla_interface` |

To verify, from the repo root:

```sh
uv run python tools/sync_scintilla_headers.py --check
```

### When either vendored release changes

1. **New Scintilla release vendored** (for pyside6-scintilla): run
   `make sync-headers` to refresh the copy. If `ILexer5`/`ILexer4`/
   `IDocument` gained new virtual methods (rare, and typically called out in
   Scintilla's release notes), `src/lexilla/bindings/_binding.cpp` will need
   updating to match -- a binding that's missing newly-added pure-virtual
   methods won't link.
2. **New Lexilla release vendored**: check its release notes for a newer
   minimum Scintilla interface; if it needs one, that's a Scintilla upgrade
   first (step 1).
3. Either way, re-run `uv sync --reinstall-package lexilla` -- a mismatch
   between the interface and what `_binding.cpp` assumes surfaces as a
   compile error, not a silent runtime bug, since `ILexer5` is an abstract
   C++ interface.
4. Lexilla's lexers are also built against these headers; their test suite
   (`uv run pytest packages/lexilla/tests`) exercises lexing end to end.
5. Separately, whenever `src/lexilla_vendor/` itself is re-vendored (a new
   Lexilla release, not just a Scintilla interface-header refresh), re-run
   `make lexilla-enums` (see
   [docs/bindings.md](bindings.md#typed-enums-instead-of-bare-intsstrings-propertytype-languageidentifier-language))
   and review/commit the diff to `LanguageIdentifier` (in `_binding.cpp`)
   and `src/lexilla/_languages.py` -- new Lexilla releases can add lexers
   (new `Language`/`LanguageIdentifier` members) or, in principle, new
   `SCLEX_*` values. Unlike step 2 above, a missed regeneration here does
   **not** fail at compile time (`static_cast` to an enum always succeeds)
   -- it surfaces as a nanobind runtime error the first time `.identifier`
   is read on a lexer whose `SCLEX_*` value isn't yet in the enum.

### No constant values actually cross between lexilla and pyside6-scintilla

`Scintilla.h` also `#define`s ~1300 protocol constants (`SCI_*` messages,
`SC_*`/`SCN_*` flags and notification codes — e.g. `SCI_SETILEXER 4033`,
`SC_FOLDLEVELBASE`). It's tempting to assume these are a point of coupling
between lexilla and pyside6-scintilla, but neither package actually
passes any of these constants to the other:

- lexilla's `_binding.cpp` never registers any of them as a Python
  attribute -- they're consumed only while *compiling* the vendored lexer
  `.cxx` files (for `INVALID_POSITION` and the `SC_FOLDLEVEL*` flags) and
  never appear in the `lexilla` package's Python surface.
- pyside6-scintilla doesn't expose the legacy `#define` macros either. It
  binds Scintilla's *modern* `enum class Message`/`FoldLevel`/etc. (from
  `include/ScintillaMessages.h`) via shiboken instead, so Python sees
  `Scintilla.Message.SetILexer`, not a bare `SCI_SETILEXER` int.

So there's no "did this constant come from lexilla or pyside6-scintilla"
ambiguity for a caller, because no constant is ever obtained from
lexilla in the first place -- a value common to both vendored copies of
the legacy `Scintilla.h` macros (verified identical for all 1277 shared
names across the 5.5.0/5.6.3 versions each project happens to vendor) is
purely an internal implementation detail of each package's own build, not
something either package's API surfaces or relies on the other to agree on.

### What *is* shared: the `ILexer5` interface shape and `Sci_Position`'s type

The one thing that does cross the boundary between the two packages is the
`ILexer5*` pointer itself: `lexilla`'s `create_lexer()` returns the
address of a C++ object, and pyside6-scintilla's engine later calls virtual
methods on that same address (`Lex`, `Fold`, `PropertySet`, ...) once you
hand it to `editor.setILexer(lexer.pointer)`. For that call to be safe, both
sides must agree on:

- The **exact shape of the `ILexer4`/`ILexer5` vtable** -- same virtual
  methods, in the same order, with the same signatures. This comes from
  each side's own vendored copy of `ILexer.h`.
- The **definition of `Sci_Position`/`Sci_PositionU`/`Sci_PositionCR`** used
  in those signatures (`ptrdiff_t`/`size_t`/`long` respectively) -- not any
  particular *value* of that type, but the type itself, so a `Sci_Position`
  parameter is the same size and signedness on both sides of the call.

This is a structural/ABI agreement, not a value-sharing one -- and unlike
the `Scintilla.h` constants above, nothing here is exposed to Python on
either side; it only matters to the C++ compilers that built each package's
extension module.

**Within one commit of this repo, this is enforced**: both packages compile
against the same Scintilla headers -- pyside6-scintilla against its vendored
tree, lexilla against a byte-identical copy that `tools/sync_scintilla_headers.py
--check` guards in CI -- and lexilla's tests hand a lexer to the
pyside6-scintilla built from the same commit.

**Across releases it still isn't**: the two packages are published
separately, so a user can combine a lexilla built against one Scintilla's
headers with a pyside6-scintilla built against another's. If a future
Scintilla release adds a virtual method to `ILexer4`/`ILexer5`, handing
lexilla's pointer to pyside6-scintilla's `setILexer()` across those versions
would be undefined behavior (mismatched vtable layout), not a clean error.
So when a Scintilla upgrade changes `ILexer.h`'s interfaces, release both
packages together, and state the matching pyside6-scintilla version in
lexilla's changelog (lexilla has no hard dependency on it -- its glue module
just imports it).
