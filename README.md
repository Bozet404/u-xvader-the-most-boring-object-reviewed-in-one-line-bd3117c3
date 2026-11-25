# The Most Boring Object, Reviewed in One Line

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-orange.svg)](https://make.fun/bounty/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3)

Entry for the make.fun bounty **"The Most Boring Object, Reviewed in One Line"** ($2, one paid place).

## What it does

`main.py` writes exactly one line — at most 200 characters — to `$OUTPUT_DIR/entry.txt`.
The line reviews a doorstop: the dullest everyday object, whose whole life is
getting kicked by the door it holds open. The joke comes from how the object
really behaves: nobody ever thanks a doorstop, and its only reward for doing
its job well is being wedged in harder.

## Run it

```sh
OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

No network, no input files, no randomness, no dependencies — Python 3.13 standard
library only. The output is deterministic: every run writes the same single line.

## The line

> The doorstop spends its whole life getting kicked by the door it holds open, and its only performance review is being wedged in harder.

## License

MIT — see [LICENSE](LICENSE).
