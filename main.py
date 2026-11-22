#!/usr/bin/env python3
"""news-image-20261122 entrypoint.

Copies the pre-drawn poster (entry.png, 1024x1024) to the output
directory make.fun provides. Standard library only, no network,
deterministic: every run writes the same bytes.
"""
import os
import shutil
import sys


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
