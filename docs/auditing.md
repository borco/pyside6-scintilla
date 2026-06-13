# Auditing the vendored Scintilla source

!!! note
    `src/scintilla/` is vendored unmodified from Scintilla's official release. If
    you'd like to confirm that for yourself, here's one way -- use whatever
    approach you're comfortable with.

Scintilla **5.6.3** is extracted as it in `src/scintilla/`.

| Field | Value |
| --- | --- |
| Upstream repository | <https://sourceforge.net/p/scintilla/code/> |
| Upstream version | 5.6.3 |
| Upstream tag | `rel-5-6-3` (changeset `05e3f21b251d`) |
| Tarball URL | <https://www.scintilla.org/scintilla563.tgz> |
| Tarball SHA-256 | `f64339c504960c5a95510e6c3306ab5e95f23abaf8aed82897e57bff78e74616` |
| Vendored path | `src/scintilla` |

After verifying the checksum and extracting the tarball, a tree diff against
`src/scintilla/` should come back empty:

```sh
tar -xzf scintilla563.tgz --strip-components=1 -C <some-dir>
```

```sh
diff -rq <some-dir> src/scintilla/
```
