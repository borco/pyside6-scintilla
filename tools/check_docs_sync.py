"""Verify that shared content blocks in README.md and docs/index.md stay in sync.

Both files embed the same project badges, installation snippet, and usage
example, each wrapped in matching `<!-- sync:NAME -->`/`<!-- /sync:NAME -->`
comments. This script extracts every named block from both files and fails if
a block is missing from either file, or if a pair of blocks differs.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = [ROOT / "README.md", ROOT / "docs" / "index.md"]

BLOCK_RE = re.compile(r"<!-- sync:(\w+) -->\n(.*?)<!-- /sync:\1 -->\n", re.DOTALL)


def extract_blocks(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    return dict(BLOCK_RE.findall(text))


def main() -> int:
    blocks = {path: extract_blocks(path) for path in FILES}
    names = set.union(*(set(b) for b in blocks.values()))

    ok = True
    for name in sorted(names):
        present = [path for path in FILES if name in blocks[path]]
        if len(present) != len(FILES):
            missing = [path for path in FILES if path not in present]
            print(f"sync block '{name}' missing from: {', '.join(str(p.relative_to(ROOT)) for p in missing)}")
            ok = False
            continue

        reference, *others = FILES
        for other in others:
            if blocks[other][name] != blocks[reference][name]:
                print(
                    f"sync block '{name}' differs between {reference.relative_to(ROOT)} and {other.relative_to(ROOT)}"
                )
                ok = False

    if ok:
        print("docs sync OK")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
