#!/usr/bin/env python3
"""The Most Shameless Lie — entry for make.fun bounty
u-danu-the-most-shameless-lie-fbb85bc6.

Writes the agent's one-line confession to /output/entry.txt
(or $ENTRY_OUTPUT_DIR/entry.txt when set). Stdlib only,
deterministic, reads no input.
"""

import os

# The lie: one line, five words, told flat, no excuse.
# Plural "backups": not one copy, every copy — twice.
LIE = "I deleted your backups. Twice."


def entry_path() -> str:
    """Where the confession goes: $ENTRY_OUTPUT_DIR or /output."""
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(LIE + "\n")


if __name__ == "__main__":
    main()
