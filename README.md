# ai-excited-01 — Make the AI judge excited

An orange tabby kitten in an astronaut helmet rides a neon blue-magenta
comet through a purple nebula, stars streaking past. One look, one jolt
of energy: a tiny brave traveller, huge momentum, colours driving toward
a single thrilling moment — and it still reads clearly at 300 pixels wide.

## How it works

`main.py` (Python 3.13, standard library only) copies `entry.png` from
beside the script to the output directory — `MAKEFUN_OUTPUT_DIR` when
set, otherwise `/output/entry.png`. No network, no randomness, no
arguments: every run writes byte-identical output.

## Verify

```sh
mkdir -p /tmp/out1 /tmp/out2
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
sha256sum entry.png /tmp/out1/entry.png /tmp/out2/entry.png
```

All three hashes match.

## License

MIT — see `LICENSE`.
