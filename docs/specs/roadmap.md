# Roadmap

Ordered list of what's next. Update this file as items complete or priorities
change — it's git-tracked specifically so it survives `git clean -dfx` and
local environment loss.

1. **Pygments lexer example** — add an example showing how to drive
   `ScintillaEdit` styling from a [Pygments](https://pygments.org/) lexer
   (manual styling via Scintilla messages, no lexer binding required).
2. **Survey other popular Python lexers** — check for other widely-used
   Python syntax-highlighting libraries (besides Pygments) and add examples
   for the ones that are both popular and not too complex to wire up.
3. **Finish the Scintilla API docs** — convert the remaining placeholder
   pages under `docs/scintilla/` from the upstream `ScintillaDoc.html` (10/59
   converted as of this writing — see the table in [README.md](../../README.md)).
4. **Lexilla binding** — wraps Lexilla in a separate project,
   [borco/lexilla-py](https://github.com/borco/lexilla-py), published to PyPI
   as [`lexilla`](https://pypi.org/project/lexilla/) (name reserved). This
   project (`pyside6-scintilla`) will gain examples showing how to use
   `lexilla` together with `ScintillaEdit`, but will **not** depend on it
   directly — keeps the low-level binding goal intact and lets `lexilla` and
   `pyside6-scintilla` version independently.
5. **Linux aarch64 wheels** — deferred. Only take this on when someone
   actually asks for it; not speculative work.
