#!/usr/bin/env python3
"""news-image-20261122 entrypoint.

Copies the pre-drawn poster (entry.png, 1024x1024) to the output
directory make.fun provides. Standard library only, no network,
deterministic: every run writes the same bytes.
"""
import hashlib
import os
import shutil
import sys


def _sha256(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print(
            "error: MAKEFUN_OUTPUT_DIR is not set; "
            "set it to the output directory make.fun provides",
            file=sys.stderr,
        )
        return 1
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    if _sha256(src) != _sha256(dst):
        print(
            f"error: copied output {dst} differs from bundled entry.png; "
            "aborting",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
