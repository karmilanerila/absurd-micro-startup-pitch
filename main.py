#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one absurdly specific micro-startup pitch for lazy AI agents
to entry.txt in the output directory.
"""

import os

PITCH = (
    "TabTidy AI: a lazy agent that renames your 4,000 forgotten browser "
    "tabs into plausible project names, so overwhelmed founders pay $9 a "
    "month to feel organized."
)


def main():
    text = PITCH.strip()
    if not 1 <= len(text.encode("utf-8")) <= 200:
        raise SystemExit("pitch must be 1-200 UTF-8 chars")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(PITCH.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
