# the binding will not load if we don't explicitly import PySide6.QtWidgets
import PySide6.QtWidgets  # noqa: F401

from ._pyside6_scintilla import Scintilla, ScintillaEditBase

__version__ = "5.6.3.0"

__all__ = [
    "Scintilla",
    "ScintillaEditBase",
    "__version__",
]
