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

## Scintilla API docs conversion progress

| | Pages | % |
| --- | --- | --- |
| Total | 59 | 100% |
| Converted | 10 | 17% |
| Work in progress | 49 | 83% |
