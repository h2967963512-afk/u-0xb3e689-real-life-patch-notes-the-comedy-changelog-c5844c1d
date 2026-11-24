"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one patch note, 124 characters — inside the
# 160-character gate. It targets the doorway effect: the real,
# recognisable bug where walking through a doorway wipes the reason
# you entered the room. Version number, terse engineering register,
# fix stated as if it shipped.
# Revision note: re-read the gate after running; the version prefix
# counts toward the 160 characters.
import os

TEXT = (
    "v2.4.1: fixed a bug where walking through a doorway deleted "
    "the reason you entered the room; the reason was not recoverable."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
