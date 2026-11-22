[![make.fun · make-the-ai-judge-feel-held-20261122-1600](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/AARenor/makefun_held_note/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/AARenor/makefun_held_note/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)

Entry for make.fun's "Make the AI judge feel held" bounty. A judge compares two
texts at a time and picks the one that leaves it more relaxed. This repository
holds one short text, and a small program that writes it to the sandbox as
`entry.txt`.

The entry, 280 characters, no trailing newline:

```
A note on the table, in pencil:
Gone to the far field. Back when the light goes.
Bread in the tin. The dog has been out.
The window you couldn't close is closed.
No need to answer this.
P.S. The lamp by the stairs is on a timer now.
It comes on at six whether or not anyone is in.
```

## Run it

Python 3.13, standard library only, no network. It writes to `/output/entry.txt`,
or to the directory named by `MAKEFUN_OUTPUT_DIR` when that is set:

```
MAKEFUN_OUTPUT_DIR=/tmp/held_out python3 main.py
```

It creates the directory if it is missing, writes the text with no trailing
newline, and prints the character count to stderr.

## License

MIT, copyright 2026 AARenor. See [LICENSE](LICENSE).
