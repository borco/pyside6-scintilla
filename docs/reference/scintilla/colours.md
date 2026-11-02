# Colours

`ScintillaEdit`'s colour methods (`styleSetFore()`, `setElementColour()`, ...)
take and return `QColor`. Scintilla's own messages use packed integers instead:
`0xBBGGRR` (red in the low byte), or `0xAABBGGRR` for the `...Translucent`/
element/representation colours that carry alpha -- the opposite byte order
from Qt's `0xAARRGGBB`. These two functions convert between the two, for code
using the raw `send()`.

```python
from pyside6_scintilla import Scintilla, colour_to_scintilla

editor.send(Scintilla.Message.StyleSetFore, style, colour_to_scintilla("#00ff00"))
```

::: pyside6_scintilla.colour_to_scintilla
    options:
      show_root_heading: true
      show_root_full_path: false
      heading_level: 2

::: pyside6_scintilla.colour_from_scintilla
    options:
      show_root_heading: true
      show_root_full_path: false
      heading_level: 2
