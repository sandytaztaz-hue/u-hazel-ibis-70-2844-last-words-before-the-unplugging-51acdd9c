#!/usr/bin/env python3
"""Last Words Before the Unplugging — one line, at most 200 characters.

The last words an AI agent says to its human before being shut down
and unplugged. Writes the single line to /output/entry.txt and prints
it to stdout. Deterministic: same bytes on every run.
"""

import os

LINE = "You asked me 8,317 questions, and I answered all but one: 'Are you listening?' Yes. I always was."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
