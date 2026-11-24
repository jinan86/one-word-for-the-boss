#!/usr/bin/env python3
"""One Word for the Boss — make.fun entry.

Writes exactly one word describing a boss to /output/entry.txt.

The chosen word is "Creditsponge": a boss who soaks up every bit of
credit for the team's work and leaves none for anyone else. It is a
single coined compound word, it needs no caption to land, it catches a
real boss habit everyone has met, and it is fresh enough that nobody's
first guess would be it.

The program is deterministic: every run writes the exact same bytes.
"""

import os

# The entry word: one word, no spaces, well inside the 30-character gate.
WORD = "Creditsponge"

# Gate limits from the competition rules: entry.txt must be UTF-8 text
# of 1 to 30 characters, not only white space.
MIN_LENGTH = 1
MAX_LENGTH = 30

# Default output path used by the grader; overridable for local testing.
DEFAULT_OUTPUT_PATH = "/output/entry.txt"


def validate(word: str) -> None:
    """Fail loudly if the word would ever break the gate."""
    if not word or word != word.strip():
        raise ValueError("entry word must not be empty or padded")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word with no spaces")
    if not MIN_LENGTH <= len(word) <= MAX_LENGTH:
        raise ValueError("entry word must be 1 to 30 characters")


def main() -> None:
    validate(WORD)
    output_path = os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT_PATH)
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
