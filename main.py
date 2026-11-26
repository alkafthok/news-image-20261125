#!/usr/bin/env python3
"""Write the 25 November 2026 world-news image to the output directory.

The entry image is bundled in this repository as entry.png. This program
copies its bytes to <output>/entry.png unchanged, so both grading runs
produce identical output. Standard library only, no network access.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    with open(source, "rb") as src, open(dest, "wb") as dst:
        shutil.copyfileobj(src, dst)
    # Verify the copy is byte-identical to the bundled image.
    with open(source, "rb") as src, open(dest, "rb") as dst:
        if src.read() != dst.read():
            print("entry.png copy mismatch", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
