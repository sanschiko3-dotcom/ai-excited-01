"""ai-excited-01 entry: write the image that excites the AI judge.

The repository holds entry.png beside this script. Running the program
copies that image, byte for byte, to the output location:

  * MAKEFUN_OUTPUT_DIR/entry.png when MAKEFUN_OUTPUT_DIR is set, or
  * /output/entry.png otherwise.

Standard library only. No network, no randomness, no arguments:
two runs always produce identical bytes.
"""

import os
import shutil
import sys

IMAGE_NAME = "entry.png"


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, IMAGE_NAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    destination = os.path.join(out_dir, IMAGE_NAME)
    shutil.copyfile(source, destination)
    return 0


if __name__ == "__main__":
    sys.exit(main())
