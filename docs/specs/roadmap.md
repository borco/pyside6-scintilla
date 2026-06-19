# Roadmap

Ordered list of what's next. Update this file as items complete or priorities
change — it's git-tracked specifically so it survives `git clean -dfx` and
local environment loss.

1. **Finish the Scintilla API docs** — convert the remaining placeholder
   pages under `docs/scintilla/` from the upstream `ScintillaDoc.html` (see
   the conversion progress table below).
2. **Lexilla binding** — wraps Lexilla in a separate project,
   [borco/lexilla-py](https://github.com/borco/lexilla-py), published to PyPI
   as [`lexilla`](https://pypi.org/project/lexilla/) (name reserved). This
   project (`pyside6-scintilla`) will gain examples showing how to use
   `lexilla` together with `ScintillaEdit`, but will **not** depend on it
   directly — keeps the low-level binding goal intact and lets `lexilla` and
   `pyside6-scintilla` version independently.
3. **Linux aarch64 wheels** — deferred. Only take this on when someone
   actually asks for it; not speculative work.
4. **Claude skill for upgrading to a new Scintilla release** — deferred.
   Automate [docs/bindings.md](../bindings.md)'s "Updating to a new Scintilla
   release" procedure (vendoring the new tarball, diffing
   `ScintillaEditBase.pro`/`CMakeLists.txt`, adding new `bindings.xml`
   type entries, re-checking the duplicate-`Message`-enum workaround,
   version bump, rebuild/test) plus the docs side (regenerating
   `_pyside6_scintilla.pyi` via `tools/generate_pyi.py`, refreshing the
   Scintilla API docs conversion table below for new/changed messages).
   Only worth building once a second real Scintilla update happens --
   premature to generalize from a single (the original Phase 1) migration.

## Scintilla API docs conversion progress

| | Pages | % |
| --- | --- | --- |
| Total | 59 | 100% |
| Converted | 10 | 17% |
| Work in progress | 49 | 83% |
