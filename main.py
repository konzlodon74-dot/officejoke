#!/usr/bin/env python3
"""Write the funniest office joke to /output/entry.txt.

One line, deterministic: every run writes byte-identical output.
Standard library only, no network.
"""

import os

JOKE = "The office fire drill went so well that half the team is still outside, working from the car park."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # The bounty gate: /output/entry.txt must be UTF-8 text of 1-200
    # characters, not only white space. Refuse to write anything invalid.
    if not (1 <= len(JOKE) <= 200) or not JOKE.strip():
        raise ValueError("joke must be 1-200 non-blank characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
