"""Remove the rounded-corner/border artifacts from a Windows window screenshot.

Windows 11's DWM compositor rounds window corners and draws a 1px border;
a screen capture (e.g. Snipping Tool) of a single window is rectangular, so
it includes the desktop showing through the rounded-corner gaps -- an
anti-aliased gradient blending the window's own background colour down to
the desktop colour behind it -- plus that 1px border along all four
straight edges. Naively cropping or alpha-masking a fixed radius can clip
real window content (a title-bar icon, close button, or scrollbar that
happens to sit close to a corner).

Instead, this "unbleeds" each corner: since the gradient is a linear blend
of the window's flat background colour and the desktop colour, and the
desktop is dark/black behind a typical light theme, each blended pixel's
brightness *is* the window's opacity at that point (the desktop's own
contribution is ~0). So alpha = pixel / background, colour = flat
background, recovering a clean anti-aliased rounded corner with no colour
bleed -- verified by reproducing docs/assets/images/examples/bscintillaedit.png
(an existing clean reference) from a fresh, unprocessed capture.

The corner radius is a fixed *physical-pixel* size set by the display's
DPI/scaling, not by the window's dimensions -- CORNER_BOX below doesn't
need to scale with image size, just be larger than the radius. Real window
content (icons, buttons, scrollbars) sits well outside it in practice.

Usage:
    uv run python tools/clean_window_corners.py <image.png> [image2.png ...]
    uv run python tools/clean_window_corners.py --radius 12 --border 1 <image.png>

By default, each original is preserved as "<name>.orig<suffix>" next to it
before the image is cleaned in place. Pass --overwrite to skip the backup
and overwrite the image directly.
"""

import argparse
import shutil
from pathlib import Path
from typing import Final

from PySide6.QtGui import QColor, QImage

CORNER_BOX: Final = 12
BORDER_WIDTH: Final = 1


def clean(path: Path, corner_box: int, border_width: int, overwrite: bool) -> None:
    """Unbleed path's four corners and crop its straight-edge border, in place."""
    if not overwrite:
        backup_path = path.with_suffix(f".orig{path.suffix}")
        shutil.copyfile(path, backup_path)

    image = QImage(str(path)).convertToFormat(QImage.Format.Format_ARGB32)
    width, height = image.width(), image.height()

    # A pixel guaranteed to be the window's own flat background: top edge,
    # centered horizontally, just past the straight border.
    background = image.pixelColor(width // 2, border_width + 2)
    bg_red = background.red()

    # (corner_x, corner_y, x_sign, y_sign): absolute corner pixel plus the
    # direction to step inward from it.
    corners = [
        (0, 0, 1, 1),
        (width - 1, 0, -1, 1),
        (0, height - 1, 1, -1),
        (width - 1, height - 1, -1, -1),
    ]
    for corner_x, corner_y, x_sign, y_sign in corners:
        for dy in range(corner_box):
            for dx in range(corner_box):
                x, y = corner_x + dx * x_sign, corner_y + dy * y_sign
                if not (0 <= x < width and 0 <= y < height):
                    continue
                # Desktop's contribution to the blend is ~0, so the pixel's
                # own brightness already is the window's opacity here.
                red = image.pixelColor(x, y).red()
                alpha = max(0, min(255, round(255 * red / bg_red)))
                image.setPixelColor(x, y, QColor(background.red(), background.green(), background.blue(), alpha))

    cropped = image.copy(border_width, border_width, width - 2 * border_width, height - 2 * border_width)
    cropped.save(str(path))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("images", nargs="+", type=Path, help="screenshot(s) to clean")
    parser.add_argument(
        "-r",
        "--radius",
        type=int,
        default=CORNER_BOX,
        help="corner box size in pixels, larger than the window's actual corner radius (default: %(default)s)",
    )
    parser.add_argument(
        "-b",
        "--border",
        type=int,
        default=BORDER_WIDTH,
        help="straight-edge border width in pixels to crop off all four sides (default: %(default)s)",
    )
    parser.add_argument(
        "-o",
        "--overwrite",
        action="store_true",
        help="overwrite each image in place without keeping a '<name>.orig<suffix>' backup",
    )
    args = parser.parse_args()

    for image in args.images:
        clean(image, args.radius, args.border, args.overwrite)


if __name__ == "__main__":
    main()
