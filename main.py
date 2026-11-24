#!/usr/bin/env python3
"""One Sentence, One Journey — make.fun bounty entry (u-gudril-cool-one-sentence-one-journey-410686ca).

Writes the entry line to /output/entry.txt (or <argv[1]>/entry.txt).
Python standard library only. Deterministic: the same bytes on every run.
"""
import os
import sys

LINE = "She missed the last train home, walked forty miles through the rain under a stranger's umbrella, and arrived at dawn to find her mother had left the porch light on for her all night."
MAX_CHARS = 240
assert LINE.count(".") == 1, "entry must be exactly one sentence"

def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else "/output"
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, limit {MAX_CHARS}"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
