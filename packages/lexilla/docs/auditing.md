# Auditing the vendored Lexilla source

> [!NOTE]
> `src/lexilla_vendor/` is vendored unmodified from Lexilla's official
> release. If you'd like to confirm that for yourself, here's one way --
> use whatever approach you're comfortable with. Mirrors
> [pyside6-scintilla's docs/auditing.md](https://github.com/borco/pyside6-scintilla/blob/master/docs/auditing.md)
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

Rather than vendor the whole Scintilla tree (which would reintroduce the
"this package has no Scintilla/Qt dependency" coupling the project
deliberately avoids — see `docs/specs/mission.md`), only these three headers
are vendored, unmodified, under `src/scintilla_interface/include/`. They are
pure interface/constant declarations (no implementation, no Qt) and are
stable across Scintilla releases.

| Field | Value |
| --- | --- |
| Upstream project | <https://www.scintilla.org/> |
| Upstream version | 5.5.0 (matches the vendored Lexilla version above) |
| Upstream tag | `rel-5-5-0` (per `version.txt`: `550`) |
| Tarball URL | <https://www.scintilla.org/scintilla550.tgz> |
| Tarball SHA-256 | `e553e95509f01f92aa157fa02d06a712642e13d69a11ec1a02a7ddf22c406231` |
| Files vendored | `include/ILexer.h`, `include/Sci_Position.h`, `include/Scintilla.h` |
| Vendored path | `src/scintilla_interface` |

To verify the files are byte-identical to upstream:

```sh
tar -xzf scintilla550.tgz --strip-components=1 -C <some-dir>
```

```sh
diff <some-dir>/include/ILexer.h src/scintilla_interface/include/ILexer.h
diff <some-dir>/include/Sci_Position.h src/scintilla_interface/include/Sci_Position.h
diff <some-dir>/include/Scintilla.h src/scintilla_interface/include/Scintilla.h
```

### Keeping it in sync with the Lexilla version

Because `ILexer5`'s shape (and the `Sci_Position`/`Sci_PositionU` types it
uses) is part of the ABI that Lexilla's `CreateLexer` and the bindings in
`src/lexilla/bindings/` depend on, these three headers must track a
compatible Scintilla release, not whatever Scintilla release is newest. Scintilla and
Lexilla share the same author and bump their *major.minor* together (e.g.
both had a `5.5.x` and a `5.4.x` line), but their *patch* numbers drift
independently within that line — Scintilla released `5.4.0`–`5.4.3` while
Lexilla released `5.4.1`–`5.4.9` over the same `5.4` line. So "same version
number" only holds at the major.minor level; don't assume an exact patch
match exists upstream. Concretely, whenever `src/lexilla_vendor/` is
re-vendored for a new Lexilla release (see the table above):

1. Find the newest Scintilla release tarball sharing Lexilla's major.minor
   (e.g. Lexilla `5.5.1` → look for the newest `scintilla55*.tgz`; if none
   has been published yet for that minor, the previous minor's latest patch
   is the best available match). Check
   <https://www.scintilla.org/LexillaDownload.html> and
   <https://www.scintilla.org/ScintillaDownload.html> for what's current.
2. Diff its `include/ILexer.h`, `include/Sci_Position.h`, and
   `include/Scintilla.h` against the currently vendored copies in
   `src/scintilla_interface/include/`. If `ILexer5`/`ILexer4`/`IDocument`
   only gained new virtual methods (rare, and typically called out in
   Scintilla's release notes), the binding in
   `src/lexilla/bindings/_binding.cpp` will need updating to match — a
   binding that's missing newly-added pure-virtual methods won't link.
3. Replace the three files and update this table's version/tag/URL/checksum
   to match.
4. Re-run `make build` (or `uv sync --reinstall-package lexilla`) — a
   mismatch between the vendored interface and what `_binding.cpp` assumes
   will surface as a compile error, not a silent runtime bug, since
   `ILexer5` is an abstract C++ interface.

### No constant values actually cross between lexilla-py and pyside6-scintilla

`Scintilla.h` also `#define`s ~1300 protocol constants (`SCI_*` messages,
`SC_*`/`SCN_*` flags and notification codes — e.g. `SCI_SETILEXER 4033`,
`SC_FOLDLEVELBASE`). It's tempting to assume these are a point of coupling
between lexilla-py and pyside6-scintilla, but neither package actually
passes any of these constants to the other:

- lexilla-py's `_binding.cpp` never registers any of them as a Python
  attribute -- they're consumed only while *compiling* the vendored lexer
  `.cxx` files (for `INVALID_POSITION` and the `SC_FOLDLEVEL*` flags) and
  never appear in the `lexilla` package's Python surface.
- pyside6-scintilla doesn't expose the legacy `#define` macros either. It
  binds Scintilla's *modern* `enum class Message`/`FoldLevel`/etc. (from
  `include/ScintillaMessages.h`) via shiboken instead, so Python sees
  `Scintilla.Message.SetILexer`, not a bare `SCI_SETILEXER` int.

So there's no "did this constant come from lexilla-py or pyside6-scintilla"
ambiguity for a caller, because no constant is ever obtained from
lexilla-py in the first place -- a value common to both vendored copies of
the legacy `Scintilla.h` macros (verified identical for all 1277 shared
names across the 5.5.0/5.6.3 versions each project happens to vendor) is
purely an internal implementation detail of each package's own build, not
something either package's API surfaces or relies on the other to agree on.

### What *is* shared: the `ILexer5` interface shape and `Sci_Position`'s type

The one thing that does cross the boundary between the two packages is the
`ILexer5*` pointer itself: `lexilla-py`'s `create_lexer()` returns the
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

**This is not automatically enforced.** lexilla-py and pyside6-scintilla
are separate repositories that vendor independently. Today they happen to
agree (`ILexer.h` and `Sci_Position.h` are byte-identical between Scintilla
5.5.0, vendored here, and 5.6.3, vendored by pyside6-scintilla), but nothing
prevents that from drifting if a future Scintilla release adds a virtual
method to `ILexer4`/`ILexer5` and only one of the two projects re-vendors
past that point. If that happens, handing lexilla-py's pointer to
pyside6-scintilla's `setILexer()` would be undefined behavior (mismatched
vtable layout), not a clean error.

**Checklist addition**: whenever either project re-vendors its Scintilla
headers (see "Keeping it in sync with the Lexilla version" above), also
diff `ILexer.h`/`Sci_Position.h` against the *other* project's currently
vendored copy (not just against upstream). If `ILexer4`/`ILexer5` gained or
lost virtual methods between the two, treat the cross-package pointer
handoff as broken until both projects vendor a mutually-compatible version
-- pin both to the same Scintilla release if needed, even if their Lexilla
and Qt-binding version cadences otherwise differ.

There is no automated check for this today (the project doesn't vendor a
live Scintilla checkout to diff against) — it's a manual step in the
re-vendoring checklist above.
