"""Write a one-line review of the most boring everyday object to entry.txt.

The program writes exactly one line (at most 200 characters) to
$OUTPUT_DIR/entry.txt (default /output). The line reviews a doorstop:
the dullest everyday object, whose whole existence is being kicked by
the door it holds open. No network, no input files, no randomness.
"""

import os

# One funny, true line reviewing a doorstop.
LINE = "The doorstop spends its whole life getting kicked by the door it holds open, and its only performance review is being wedged in harder."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
