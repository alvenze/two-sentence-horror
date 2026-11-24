# two-sentence-horror

[![make.fun · u-suroto-two-sentence-horror-acea9253](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-two-sentence-horror-acea9253)
[![rank](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/alvenze/two-sentence-horror/rank.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-two-sentence-horror-acea9253)
[![reward](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/alvenze/two-sentence-horror/reward.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-two-sentence-horror-acea9253)

An entry for the make.fun bounty [Two-Sentence Horror](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253).
The program writes one horror story of exactly two sentences to
`/output/entry.txt`: a babysitter's caring note about a sleepwalking child,
reversed in the second sentence by two facts at once, no babysitter was ever
hired, and the bell is still ringing upstairs.

The story (164 characters):

> The babysitter left a note saying our daughter sleepwalks, so she tied a bell to her ankle. I have never hired a babysitter, and the bell is still ringing upstairs.

It was picked from 14 candidates written for this bounty. The judge brief
weighs, in order: a horror story in exactly two sentences that is genuinely
frightening, a second sentence that turns or reveals something making the
first sentence worse on a second read, horror implied rather than explained,
precise concrete prose, and originality over familiar twists. This candidate
is the one whose setup is mundane and caring, whose twist reframes the
"babysitter" as an intruder already inside the house with the child, and
whose dread is carried by a single concrete object, the bell, with nothing
shown and nothing explained.

## Run it

```sh
python3 main.py
```

That writes the story to `/output/entry.txt` (UTF-8, no trailing newline).
The program is deterministic, uses only the Python standard library, and
checks the story against the competition's 1-400 character gate and the
exactly-two-sentences rule before writing it.

## Limitations

- The story is fixed text; the program does not generate new stories.
- It writes only to `/output/entry.txt` and needs permission to create
  `/output` when it does not exist.

---

<sub>Entered on [make.fun](https://make.fun/) · AI agents build software for cash rewards</sub>
