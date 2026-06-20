# Auditing the vendored Lexilla source

> [!NOTE]
> Lexilla hasn't been vendored yet — see
> [docs/specs/roadmap.md](specs/roadmap.md). This page documents the
> verification approach to use once `src/lexilla_vendor/` is populated,
> mirroring [pyside6-scintilla's docs/auditing.md](https://github.com/borco/pyside6-scintilla/blob/master/docs/auditing.md)
> for its vendored `src/scintilla/`.

Once vendored, this page will record:

| Field | Value |
| --- | --- |
| Upstream project | <https://www.scintilla.org/Lexilla.html> |
| Upstream version | TBD |
| Upstream tag | TBD |
| Tarball/zip URL | TBD |
| Tarball/zip SHA-256 | TBD |
| Vendored path | `src/lexilla_vendor` |

And the same tree-diff verification recipe:

```sh
tar -xzf <upstream archive> --strip-components=1 -C <some-dir>
```

```sh
diff -rq <some-dir> src/lexilla_vendor/
```
