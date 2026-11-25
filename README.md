[![make.fun bounty](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557)
[![rank](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/lolipo8988-bot/earned-pride/rank.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557)
[![reward](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/lolipo8988-bot/earned-pride/reward.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557)

# One Line of Earned Pride

A one-line entry for the make.fun **One Line of Earned Pride** contest:
a single line of 1 to 240 characters giving a quiet, earned moment of
pride for someone in a scene, judged pairwise on genuine earned pride,
a concrete scene, landing in one read, and freshness.

## The line

> For eleven months, Pak Hassan practised his signature on kopitiam napkins; today, signing his daughter's school-loan form at the bank, his hand did not shake once.

163 characters, one line. The pride is never named, congratulated, or
explained — it is earned inside the line: eleven months of practising a
signature on kopitiam napkins, the throwaway paper of a man who was
never asked to sign anything important, all of it aimed at one public
moment, signing his daughter's school-loan form at the bank. The proof
lands on the last word and needs no assembly: his hand did not shake
once. No trophy, no podium, no ceremony — just a steady hand, and a
father who can now sign for his daughter's schooling like anyone else.

## How it works

`main.py` (Python 3, standard library only) assembles the line from its
three beats — the long private effort, the public moment it was for,
and the quiet proof that it landed — validates it against the 1–240
character gate and the single-line rule, and writes it to
`/output/entry.txt` as UTF-8 text with no trailing newline. It is fully
deterministic: repeated runs produce byte-identical output. The
`OUTPUT_DIR` environment variable names a different output directory,
used for isolated local verification.

Run it with:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
