# Roadmap

Ordered list of what's next. Update this file as items complete or priorities
change — it's git-tracked specifically so it survives `git clean -dfx` and
local environment loss.

1. **Fix the `modified`-style signal marshalling** — `ScintillaEditBase`
   signals like `modified` carry `Scintilla::Position`/`Scintilla::FoldLevel`
   etc.-typed parameters that shiboken can't marshal to a Python slot
   (silently swallowed `TypeError`, signal never reaches Python). Needs
   either Qt meta-type registration for these types or a hand-written
   wrapper re-emitting the affected signals with plain-int signatures.
   Drive this with TDD — write failing `pytest-qt`/`pytest-mock` tests
   (e.g. asserting a connected slot actually receives the `modified`
   emission) before changing the binding. Once fixed, update
   `pygments_highlighter.py` and `tree_sitter_highlighter.py` (and their
   examples/docs) to connect to `editor.modified` directly instead of the
   `editor.get_doc().modified` workaround.
2. **Finish the Scintilla API docs** — convert the remaining placeholder
   pages under `docs/scintilla/` from the upstream `ScintillaDoc.html` (see
   the conversion progress table below).
3. **Lexilla binding** — wraps Lexilla in a separate project,
   [borco/lexilla-py](https://github.com/borco/lexilla-py), published to PyPI
   as [`lexilla`](https://pypi.org/project/lexilla/) (name reserved). This
   project (`pyside6-scintilla`) will gain examples showing how to use
   `lexilla` together with `ScintillaEdit`, but will **not** depend on it
   directly — keeps the low-level binding goal intact and lets `lexilla` and
   `pyside6-scintilla` version independently.
4. **Linux aarch64 wheels** — deferred. Only take this on when someone
   actually asks for it; not speculative work.

## Scintilla API docs conversion progress

| | Pages | % |
| --- | --- | --- |
| Total | 59 | 100% |
| Converted | 10 | 17% |
| Work in progress | 49 | 83% |
