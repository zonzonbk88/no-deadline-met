#!/usr/bin/env python3
"""One-line joke excusing a missed deadline.

Writes a single line (1-200 chars, no trailing newline) to entry.txt.
Deterministic, standard library only, no network.
"""
import os

ENTRY = (
    "I had it done by noon, but my laptop auto-updated, my Wi-Fi died, "
    "and my motivation \u2014 spotting a pattern \u2014 followed them both "
    "out the door."
)


def main() -> None:
    # Gate check: single line, 1-200 chars, no trailing newline.
    assert 1 <= len(ENTRY) <= 200, "entry outside 1-200 char gate"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
