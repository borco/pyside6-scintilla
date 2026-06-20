Lexilla's release source goes here, vendored unmodified (mirroring
pyside6-scintilla's `src/scintilla/`). Not vendored yet — see
[docs/specs/roadmap.md](../../docs/specs/roadmap.md) and
[docs/auditing.md](../../docs/auditing.md).

Named `lexilla_vendor` rather than `lexilla` so it never collides with
`src/lexilla/` (the Python package) on case-insensitive filesystems — see
[docs/specs/mission.md](../../docs/specs/mission.md).
