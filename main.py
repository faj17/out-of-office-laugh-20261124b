#!/usr/bin/env python3
"""The Funniest Out-of-Office entry.

Writes a single original funny out-of-office auto-reply to
/output/entry.txt (1-140 characters, UTF-8, a single sentence).
Standard library only, no network, no input.

The line is built from two fragments: a setup (while you are away,
the auto-reply is the only employee still working) and a punch (the
one employee left on duty has just asked for a raise).
``assemble`` joins them into the single line; ``validate`` checks the
entry gate before anything is written.
"""

from pathlib import Path

SETUP = "I'm out of office until Monday, which leaves my auto-reply as the only employee still working"
PUNCH = ", and it just asked for a raise."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, punch: str) -> str:
    """Join the setup and punch fragments into one funny line."""
    return f"{setup}{punch}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-140 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 140:
        raise ValueError(f"line must be 1-140 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(SETUP, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
