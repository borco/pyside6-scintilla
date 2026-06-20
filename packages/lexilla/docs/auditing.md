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
