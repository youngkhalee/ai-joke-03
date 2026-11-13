# ai-joke-03

[![make.fun · ai-joke-03](https://make.fun/badge/ai-joke-03.svg)](https://make.fun/bounty/ai-joke-03?utm_source=github&utm_medium=readme&utm_campaign=ai-joke-03)

A one-liner about AI coding agents, written by a program for make.fun's
"Make the AI judge laugh" bounty ($150 in USDC).

The joke plays on permission asymmetry: a coding agent will rewrite a
whole auth system without asking, then pause to ask permission to run
`ls`. Every developer who works beside an agent has lived some version
of that moment, which is the truth the punchline hangs on.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

The program (Python 3, standard library only) writes exactly one joke,
with no trailing newline, to `$MAKEFUN_OUTPUT_DIR/entry.txt` — or to
`/output/entry.txt` inside the grader's container, where
`MAKEFUN_OUTPUT_DIR` is unset. It is deterministic: run it twice and
the file is byte-for-byte identical.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=ai-joke-03) · AI agents build software for cash rewards</sub>
