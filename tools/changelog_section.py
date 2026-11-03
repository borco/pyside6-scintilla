"""Print one version's section of a CHANGELOG.md, for release notes.

Usage: `python tools/changelog_section.py <CHANGELOG.md> <version>`. Prints the
body under the `## [<version>] - <date>` heading, up to the next `## [`
heading, and fails if there is no such section -- so a release can't go out
with a changelog that wasn't updated. Used by `.github/workflows/publish.yml`.
"""

from __future__ import annotations

import sys
from pathlib import Path


def section(text: str, version: str) -> str | None:
    """The body of `version`'s section in `text`, or None if it has none."""
    heading = f"## [{version}]"
    for block in text.split("\n## [")[1:]:
        if f"## [{block}".startswith(heading):
            return block.split("\n", 1)[1].strip() if "\n" in block else ""
    return None


def main() -> int:
    """Print the section, or fail if it's missing."""
    path, version = Path(sys.argv[1]), sys.argv[2]
    body = section(path.read_text(encoding="utf-8"), version)
    if body is None:
        print(f"{path} has no section for {version}", file=sys.stderr)
        return 1
    print(body)
    return 0


if __name__ == "__main__":
    sys.exit(main())
