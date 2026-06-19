# Roadmap

Ordered list of what's next. Update this file as items complete or priorities
change — it's git-tracked specifically so it survives `git clean -dfx` and
local environment loss.

1. **Survey other popular Python lexers** — check for other widely-used
   Python syntax-highlighting libraries (besides Pygments) and add examples
   for the ones that are both popular and not too complex to wire up.
2. **Finish the Scintilla API docs** — convert the remaining placeholder
   pages under `docs/scintilla/` from the upstream `ScintillaDoc.html` (10/59
   converted as of this writing — see the table in [README.md](https://github.com/borco/pyside6-scintilla/blob/master/README.md)).
3. **Lexilla binding** — wraps Lexilla in a separate project,
   [borco/lexilla-py](https://github.com/borco/lexilla-py), published to PyPI
   as [`lexilla`](https://pypi.org/project/lexilla/) (name reserved). This
   project (`pyside6-scintilla`) will gain examples showing how to use
   `lexilla` together with `ScintillaEdit`, but will **not** depend on it
   directly — keeps the low-level binding goal intact and lets `lexilla` and
   `pyside6-scintilla` version independently.
4. **Linux aarch64 wheels** — deferred. Only take this on when someone
   actually asks for it; not speculative work.
