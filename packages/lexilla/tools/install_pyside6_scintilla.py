"""Install pyside6-scintilla for lexilla's wheel tests (cibuildwheel's before-test).

lexilla's tests exercise its `lexilla.pyside6_scintilla` glue module, so they
need pyside6-scintilla. In CI (`.github/workflows/wheels.yml`) that's the
pyside6-scintilla wheel built in the same run, downloaded into the directory
given as the only argument -- so a lexilla release is always tested against
the matching pyside6-scintilla source, never whatever is on PyPI. Without
local wheels there (e.g. a plain local cibuildwheel run) it falls back to PyPI.

The local wheel is installed without dependencies (`--no-index` can't reach
PySide6), then its dependencies come from PyPI as usual.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def pip_install(*args: str) -> None:
    """Run `pip install` in the interpreter running this script (cibuildwheel's test venv)."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", *args])


def main() -> int:
    """Install the local pyside6-scintilla wheel matching this platform, or PyPI's."""
    deps = Path(sys.argv[1])
    wheels = sorted(deps.glob("pyside6_scintilla-*.whl")) if deps.is_dir() else []
    if not wheels:
        print(f"no pyside6-scintilla wheels in {deps}; installing it from PyPI", file=sys.stderr)
        pip_install("pyside6-scintilla")
        return 0
    version = wheels[0].name.split("-")[1]
    # pip picks the wheel matching this platform/architecture among the ones
    # downloaded for every OS.
    pip_install("--no-index", "--no-deps", "--find-links", str(deps), f"pyside6-scintilla=={version}")
    pip_install(f"pyside6-scintilla=={version}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
