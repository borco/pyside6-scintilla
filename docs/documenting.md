# Documenting

How this docs site (<https://borco.github.io/pyside6-scintilla/>) is built,
and how to add or update a page.

## Overview

The site is [MkDocs](https://www.mkdocs.org/) + [Material for
MkDocs](https://squidfunk.github.io/mkdocs-material/), configured in
`mkdocs.yml`. `.github/workflows/docs.yml` builds it with `mkdocs build
--strict` and deploys to GitHub Pages on every push to `master`. Preview
locally with:

```bash
make docs-serve
```

which runs `mkdocs serve` (live-reload at
`http://127.0.0.1:8000/pyside6-scintilla/` -- note the `/pyside6-scintilla/`
base path applies locally too).

## Adding or updating a page

1. Add or edit a Markdown file under `docs/`.
2. Add it to the `nav:` tree in `mkdocs.yml`, under the appropriate section
   (see below for the "Scintilla API" themed groups).
3. Run `make docs-serve` and check it renders correctly.
4. Before committing, run `uv run --group docs mkdocs build --strict` --
   this fails on broken internal links/anchors and missing nav entries,
   which is most of what goes wrong.
5. If the page touches content shared with `README.md` (currently the
   header badges, install snippet, and usage example on `docs/index.md`),
   keep the `<!-- sync:NAME -->`/`<!-- /sync:NAME -->` blocks in both files
   identical -- `tools/check_docs_sync.py` (run via `make lint` and CI)
   fails if they diverge.

## The "Scintilla API" section

`docs/scintilla/**` is a page-by-page Markdown conversion of
`src/scintilla/doc/ScintillaDoc.html` -- the upstream Scintilla manual,
which ships as one very long HTML page with an in-page table of contents but
no persistent sidebar. Splitting it into MkDocs pages, grouped by topic under
themed sub-sections of the "Scintilla API" nav entry (e.g. "Editing"), makes
it navigable alongside the rest of the site.

This is an ongoing, incremental effort -- new sections are converted one at a
time as they're needed. Each page is produced with a pandoc-assisted
conversion:

1. **Find the section's boundaries.** Each major topic is an `<h2 id="...">`
   (occasionally `<h3>`) in `ScintillaDoc.html`. Extract the relevant line
   range and wrap it in a minimal `<!DOCTYPE html><html><body>...</body></html>`
   document (pandoc needs a full document, not a fragment).
2. **Convert with pandoc**: `pandoc -f html -t gfm --wrap=none -o out.md
   wrapped.html`. This gets roughly 80% of the way there; the rest is
   regex/`re`-based post-processing of `out.md` (no extra dependencies --
   stdlib `re`/`html` is enough for a one-off script).
3. **Post-process**:
   - Collect every `id="..."` in the section -- this is the set of in-page
     cross-reference targets for this page.
   - Convert the TOC block (`<a href="#XXX" class="message">...</a>` lines)
     into a `- [\`SIG\`](#XXX)` bullet list.
   - Convert message/struct headings (pandoc emits bold `**SIGNATURE**`
     lines) into `#### \`SIGNATURE\` {: #ANCHOR_ID }` using the `attr_list`
     extension for explicit anchors.
   - Resolve cross-reference links: if the target anchor is in this page's
     id set, link to `#ANCHOR_ID`; otherwise strip the link (the target page
     doesn't exist yet) but keep the text.
   - Merge pandoc's per-`<pre>` indented blocks for C struct/typedef
     definitions into single ` ```c ... ``` ` fences.
   - Drop pandoc's redundant top-level `## <Section Name>` heading (the page
     gets its own `# Title` matching the nav label) and shift remaining
     heading levels up by one.
   - Collapse extra blank lines and ensure blank lines around fenced code
     blocks.
4. **Add a `!!! note` admonition** at the top, marking the page as adapted
   from a specific upstream Scintilla version. (GitHub-style `> [!NOTE]`
   alerts do **not** render correctly here -- use the `admonition`
   extension's `!!! note` syntax.)
5. **Add inline upstream-doc links**: each `h1`/`h2` heading gets a small
   `[:material-link-variant:](https://www.scintilla.org/ScintillaDoc.html#ANCHOR_ID
   "Upstream documentation"){ .heading-link }` appended to the heading text,
   pointing at the corresponding anchor in the live upstream
   `ScintillaDoc.html` -- the canonical source for that section's history.
   The `.heading-link` CSS class lives in `docs/stylesheets/extra.css`.
6. **Add the page to `mkdocs.yml`'s nav** under the right themed group
   ("Editing", "Selection & Search", etc.). `mkdocs build --strict` rejects
   nav groups with no pages, so don't pre-create empty groups for sections
   that don't have a page yet.

The conversion script itself is a throwaway (`/tmp/scidoc/convert.py` in past
sessions) -- not part of the repo, since each section needs small
adjustments. This page is kept up to date with any new wrinkles found along
the way.

## The "Reference" page

`docs/reference.md` is generated from
`src/pyside6_scintilla/_pyside6_scintilla.pyi` (the type stub for the
compiled `_pyside6_scintilla` extension) via the
[mkdocstrings](https://mkdocstrings.github.io/)/`mkdocstrings-python`
plugin, configured in `mkdocs.yml`'s `plugins:` section. Griffe reads the
stub directly -- no compiled extension or Sphinx fallback is needed at docs-
build time (`docs.yml` runs with `--no-install-project`).

The page currently renders:

- `ScintillaEditBase.send`/`.sends` (the two entry points for the message
  API) with hand-written docstrings, via `::: pyside6_scintilla.ScintillaEditBase.send`
  / `.sends` blocks with `show_root_heading: true`.
- `Scintilla.Message` as a glossary (`::: pyside6_scintilla.Scintilla.Message`)
  -- 815+ of 819 members have a one-line docstring stitched in from
  `Scintilla.iface`/`ScintillaDoc.html`.

To add another enum or class to this page, add a `::: pyside6_scintilla.<name>`
block. If it needs per-member docstrings that don't exist yet, see
`tools/generate_pyi.py` (`add_enum_docstrings()` and the various `*_DOCS`
dicts) and `docs/bindings.md`'s "Type stubs" section -- after changing it,
regenerate with `make stubs` and re-check `docs/reference.md`.

## Keeping docs and code in sync

- `tools/check_docs_sync.py` (via `make lint`) checks the `<!-- sync:NAME -->`
  blocks shared between `README.md` and `docs/index.md`.
- `mkdocs build --strict` (via `docs.yml`) fails on broken links/anchors and
  missing nav entries -- run it locally before pushing any docs change.
