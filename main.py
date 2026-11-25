#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue — make.fun entry.

Writes one ~100-word monologue, spoken by a fantasy villain who is
secretly just very tired, to /output/entry.txt. The tiredness lives in
the rhythm, the pauses and the small deflections — the kettle, the
cushion, the paperwork — never in a plain statement of weariness.
The speaker is a specific villain: four hundred years ruling the
Ashen Marches, ravens and a council bringing treason, a seal to hold.
"""

import os

MONOLOGUE = (
    "Come in. Mind the step — the third one sags. Sit. Not the throne. "
    "That chair, the one with the cushion. I have ruled the Ashen Marches "
    "for four hundred years, and I have learned this: empires are mostly "
    "paperwork. The ravens bring me treason before breakfast. Somewhere in "
    "between, the kettle sings, and for one minute nobody wants anything "
    "from me. You came to slay me, I suppose. The sword is shiny. Put it "
    "down. Have some tea. We can do the shouting tomorrow. Or stay — hold "
    "the seal while I close my eyes. Just for a moment. Just until the "
    "kettle sings again."
)

# Grader writes to /output/entry.txt; allow an override only for local tests.
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(MONOLOGUE)
    # Read it back and verify the gate: 1-600 characters, not only white space.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    assert 1 <= len(written) <= 600, f"entry is {len(written)} chars, gate is 1-600"
    assert written.strip() != "", "entry must not be only white space"
    words = written.split()
    assert 90 <= len(words) <= 110, f"entry is {len(words)} words, want about 100"
    print(f"wrote {len(written)}-char, {len(words)}-word entry to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
