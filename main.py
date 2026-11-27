#!/usr/bin/env python3
"""Copy the frontpage poster to the output directory.

The poster is drawn in advance and stored in this repository as
poster.png. This program only copies it to the output directory,
verifying it is a whole PNG first.
"""

import os
import shutil
import sys

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def main():
    bot_dir = os.environ.get("MAKEFUN_BOT_DIR") or os.path.dirname(
        os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        bot_dir, "out")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(bot_dir, "poster.png")
    dst = os.path.join(out_dir, "entry.png")
    with open(src, "rb") as f:
        data = f.read()
    if data[:8] != PNG_SIGNATURE:
        print("error: poster.png is not a PNG file", file=sys.stderr)
        return 1
    with open(dst, "wb") as f:
        f.write(data)
    # Read the copy back: the entry must be byte-identical to the
    # poster in this repository, or the run is not reproducible.
    with open(dst, "rb") as f:
        written = f.read()
    if written != data:
        print("error: entry.png differs from poster.png", file=sys.stderr)
        return 1
    print(f"verified poster.png {len(data)} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
