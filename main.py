#!/usr/bin/env python3
"""Entry program for the news-image-20261126 bounty.

Copies the front-page image held beside this file to the output
directory, byte for byte, so both grader runs write identical output.
The image itself is composed offline (see README); this program only
delivers it. Python 3.13, standard library only, no network.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    out = os.path.join(OUT_DIR, "entry.png")
    shutil.copyfile(os.path.join(HERE, "entry.png"), out)
    os.chmod(out, 0o644)


if __name__ == "__main__":
    main()
