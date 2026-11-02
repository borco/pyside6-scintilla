"""Keep lexilla's copy of the Scintilla interface headers identical to the vendored Scintilla.

lexilla compiles against three Scintilla headers (`ILexer.h`, `Sci_Position.h`,
`Scintilla.h`). It keeps its own copy in `packages/lexilla/src/scintilla_interface/`
rather than including pyside6-scintilla's vendored tree, because lexilla's sdist
must build on its own -- an sdist contains only its package directory. This
script copies the files byte for byte (plus `License.txt` and `version.txt`)
from `packages/pyside6-scintilla/src/scintilla/`, so the copy can't drift from
the Scintilla release the repo vendors.

Run via `make sync-headers` after vendoring a new Scintilla release; `--check`
(run by `make lint` and CI) fails if the copy is stale.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Final

ROOT: Final = Path(__file__).resolve().parent.parent
SOURCE_DIR: Final = ROOT / "packages" / "pyside6-scintilla" / "src" / "scintilla"
COPY_DIR: Final = ROOT / "packages" / "lexilla" / "src" / "scintilla_interface"
FILES: Final = ("include/ILexer.h", "include/Sci_Position.h", "include/Scintilla.h", "License.txt", "version.txt")


def main() -> int:
    """Copy (or, with --check, compare) the interface headers."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="fail if the copy differs from the vendored Scintilla")
    check = parser.parse_args().check

    stale = []
    for name in FILES:
        source, copy = SOURCE_DIR / name, COPY_DIR / name
        data = source.read_bytes()
        if copy.exists() and copy.read_bytes() == data:
            continue
        if check:
            stale.append(name)
        else:
            copy.parent.mkdir(parents=True, exist_ok=True)
            copy.write_bytes(data)
            print(f"copied {name}")
    if stale:
        print(f"stale in {COPY_DIR.relative_to(ROOT)}: {', '.join(stale)} -- run `make sync-headers`", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
