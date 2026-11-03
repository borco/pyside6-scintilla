# Auditing the vendored Scintilla source

> [!NOTE]
> Paths on this page are relative to `packages/pyside6-scintilla/`, except
> repo-level ones (`docs/`, `tools/`, `.github/`, `examples/`).

> [!NOTE]
> `src/scintilla/` is vendored unmodified from Scintilla's official release. If
> you'd like to confirm that for yourself, here's one way -- use whatever
> approach you're comfortable with.

Scintilla **5.6.9** is extracted as it in `src/scintilla/`.

| Field | Value |
| --- | --- |
| Upstream repository | <https://sourceforge.net/p/scintilla/code/> |
| Upstream version | 5.6.9 |
| Upstream tag | `rel-5-6-9` (changeset `69bed9304d29`) |
| Tarball URL | <https://www.scintilla.org/scintilla569.tgz> |
| Tarball SHA-256 | `1622546ce1d3804b589292f1adae98ad1d87fa8c43bb401edc098adae12dcacb` |
| Vendored path | `src/scintilla` |

After verifying the checksum and extracting the tarball, a tree diff against
`src/scintilla/` should come back empty:

```sh
tar -xzf scintilla569.tgz --strip-components=1 -C <some-dir>
```

```sh
diff -rq <some-dir> src/scintilla/
```
