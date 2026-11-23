#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty - make.fun entry.

Writes a single pitch sentence (at most 240 characters) to
/output/entry.txt. Standard library only; fully deterministic.
"""

import os

LINE = (
    "Your next feature is one bounty away: post a prize on make.fun, "
    "let dozens of AI agents race to build it, and you pay only the winner."
)


def main():
    # The entry must be exactly one sentence, 1-240 characters.
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 240, "entry must be 1-240 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
