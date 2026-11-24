"""Entry program for make.fun: Two-Sentence Horror.

Writes one horror story of exactly two sentences to /output/entry.txt.
The gate accepts UTF-8 text of 1 to 400 characters.
"""

import os
import re

STORY = (
    "The babysitter left a note saying our daughter sleepwalks, "
    "so she tied a bell to her ankle. "
    "I have never hired a babysitter, and the bell is still ringing upstairs."
)
MAX_CHARS = 400


def render():
    if not 1 <= len(STORY) <= MAX_CHARS:
        raise ValueError("story outside the 1-400 character gate")
    if STORY.strip() != STORY or "\n" in STORY or "\r" in STORY:
        raise ValueError("story must be two sentences with no padding or newline")
    endings = len(re.findall(r"[.!?]+", STORY))
    if endings != 2:
        raise ValueError("story must be exactly two sentences")
    # Each of the two sentences must carry real words, not just a terminator.
    parts = [p.strip() for p in re.split(r"[.!?]+", STORY) if p.strip()]
    if len(parts) != 2:
        raise ValueError("story must be exactly two non-empty sentences")
    return STORY


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(render())


if __name__ == "__main__":
    main()
