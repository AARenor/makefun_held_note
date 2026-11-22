"""Write this repo's bounty entry text to entry.txt in the make.fun output directory."""

import os
import sys
from pathlib import Path

TEXT = """A note on the table, in pencil:
Gone to the far field. Back when the light goes.
Bread in the tin. The dog has been out.
The window you couldn't close is closed.
No need to answer this.
P.S. The lamp by the stairs is on a timer now.
It comes on at six for whoever is on the path."""


def output_dir() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def main() -> None:
    length = len(TEXT)
    assert 1 <= length <= 280, f"entry must be 1 to 280 code points, got {length}"

    directory = output_dir()
    directory.mkdir(parents=True, exist_ok=True)

    target = directory / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    print(f"{target}: {length} characters", file=sys.stderr)


if __name__ == "__main__":
    main()
