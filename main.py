"""One Line of Earned Pride entry.

Writes a single line (1 to 240 characters) to /output/entry.txt: a
quiet, earned moment of pride for someone in a concrete scene. The
competition gate requires UTF-8 text of 1 to 240 characters, not only
white space. The program is deterministic: every run writes exactly
the same bytes.
"""

import os
from pathlib import Path

MAX_CHARS = 240  # competition gate: 1..240 characters

# The line is assembled from its three beats: the long private effort,
# the public moment it was for, and the quiet proof that it landed.
BEATS = (
    "For eleven months, Pak Hassan practised his signature on kopitiam napkins; ",
    "today, signing his daughter's school-loan form at the bank, ",
    "his hand did not shake once.",
)


def build_line() -> str:
    """Assemble the entry line from its beats."""
    return "".join(BEATS).strip()


def validate(text: str) -> None:
    """Check the line against the competition gate before writing."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1..{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def entry_path() -> Path:
    """Return the entry file to write.

    With no override the program writes /output/entry.txt, as the
    competition harness expects. The OUTPUT_DIR environment variable
    names a different output directory, used for isolated local
    verification so a local run never touches the shared /output.
    """
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / "entry.txt"


def main() -> None:
    text = build_line()
    validate(text)
    entry_path().write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
