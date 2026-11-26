"""Entry for make.fun bounty u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443.

Writes the cat's voicemail greeting to entry.txt in MAKEFUN_OUTPUT_DIR.
"""

import os
import stat

ENTRY_TEXT = (
    "You've reached the cat. I knocked the phone off the shelf at 04:12, "
    "approved my own greeting, and forgot to record one."
)


def main() -> None:
    # Gate: one line, 1-120 characters, not only whitespace.
    assert 1 <= len(ENTRY_TEXT) <= 120, len(ENTRY_TEXT)
    assert ENTRY_TEXT.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY_TEXT, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
