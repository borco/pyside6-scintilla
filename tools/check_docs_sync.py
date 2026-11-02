"""Verify that each package's README and its docs-site page share their common blocks.

Each package's README.md (also its PyPI page) and its docs-site landing page
embed the same badges, installation snippet, and usage example, each wrapped
in matching `<!-- sync:NAME -->`/`<!-- /sync:NAME -->` comments. This script
extracts every named block from each pair of files and fails if a block is
missing from either file, or if the two copies differ.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAIRS = [
    (ROOT / "packages" / "pyside6-scintilla" / "README.md", ROOT / "docs" / "pyside6-scintilla" / "index.md"),
    (ROOT / "packages" / "lexilla" / "README.md", ROOT / "docs" / "lexilla" / "index.md"),
]

BLOCK_RE = re.compile(r"<!-- sync:(\w+) -->\n(.*?)<!-- /sync:\1 -->\n", re.DOTALL)


def extract_blocks(path: Path) -> dict[str, str]:
    """The `<!-- sync:NAME -->` blocks in `path`, by name."""
    text = path.read_text(encoding="utf-8")
    return dict(BLOCK_RE.findall(text))


def check_pair(readme: Path, page: Path) -> bool:
    """Whether `readme` and `page` have the same set of blocks, each with identical content."""
    readme_blocks, page_blocks = extract_blocks(readme), extract_blocks(page)
    ok = True
    for name in sorted(set(readme_blocks) | set(page_blocks)):
        missing = [path for path, blocks in ((readme, readme_blocks), (page, page_blocks)) if name not in blocks]
        if missing:
            print(f"sync block '{name}' missing from: {', '.join(str(p.relative_to(ROOT)) for p in missing)}")
            ok = False
        elif readme_blocks[name] != page_blocks[name]:
            print(f"sync block '{name}' differs between {readme.relative_to(ROOT)} and {page.relative_to(ROOT)}")
            ok = False
    return ok


def main() -> int:
    """Check every pair; report all mismatches, not just the first."""
    results = [check_pair(readme, page) for readme, page in PAIRS]
    if all(results):
        print("docs sync OK")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
