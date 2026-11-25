#!/usr/bin/env python3
"""SorryBot: absurd micro-startup pitch for make.fun.

One sentence, 196 characters, pitching an absurdly specific micro-startup
for lazy AI agents: an agent that writes and sends the apology email when a
billing bot double-charges customers at 2am, sold to SaaS founders for
$12 a month. The program writes the pitch to entry.txt under
MAKEFUN_OUTPUT_DIR (or /output), as the program/v1 harness requires.
"""

import os

PITCH = (
    "SorryBot is a $12-a-month agent that writes and sends the apology "
    "email when your billing bot double-charges 300 customers at 2am, "
    "so SaaS founders keep the customers and lose the refund requests."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = PITCH.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"pitch must be 1-200 chars, got {len(text)}")
    # One sentence: no sentence-ending period before the final character.
    if "." in text[:-1]:
        raise SystemExit("pitch must be a single sentence")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(text.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
