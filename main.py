#!/usr/bin/env python3
"""Sorry, I Heard That Wrong — make.fun bounty entry.

Writes a single line (at most 140 characters): the apology a smart
speaker gives its owner after it mishears them.

Run:  python3 main.py
Output: output/entry.txt  (and /output/entry.txt when that directory
        exists, which is where the make.fun grader reads the artifact)
"""

import os

ENTRY = (
    "Sorry \u2014 I heard 'turn the volume down' as "
    "'turn the volume down on your life choices', and honestly, "
    "the playlist agreed with me."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"

    here = os.path.dirname(os.path.abspath(__file__))
    targets = [os.path.join(here, "output", "entry.txt")]
    if os.path.isdir("/output"):
        targets.append("/output/entry.txt")

    for path in targets:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)

    print(ENTRY)
    print(f"({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
