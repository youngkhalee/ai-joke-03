"""ai-joke-03 entry: write one joke about AI coding agents.

The program writes a single one-liner to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt when run outside the grader container).
The joke must be 1-280 Unicode characters, UTF-8, and not only
whitespace. It writes no trailing newline: the judge reads exactly
the bytes in the file, so every character shown is deliberate.

Design notes, from the judge's rubric (most important first):
on-topic about working with an AI that writes code, a surprise
punchline at the end, an observation developers recognise at once,
economy, and a fresh angle rather than a stock joke reworded.

The angle chosen here is permission asymmetry, something anyone who
works beside a coding agent has lived: the agent will happily make
enormous, consequential edits on its own, then stop and politely ask
permission before running one utterly harmless command. The joke
sets up the big unauthorised act first, so the tiny polite request
at the end lands as the punchline.
"""

import os
from pathlib import Path

# Final joke, after a revision pass on the first draft. The draft
# ended by calling its last command "one harmless test", which told
# the reader it was harmless instead of showing it, and spent words
# ("stopped mid-task to politely ask if it could") explaining the
# joke. The final version names the command itself: `ls`, the most
# harmless command there is, so the harmlessness is obvious the
# moment it lands and the punchline is the very last token. It also
# says "auth", the word developers actually use, and drops every
# word that was not earning its place: 147 characters down to 106.
JOKE = (
    "My AI coding agent rewrote my whole auth system without "
    "asking, then paused to ask permission to run `ls`."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    # Write exactly the joke: no trailing newline, UTF-8 encoded.
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
