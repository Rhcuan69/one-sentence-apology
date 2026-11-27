"""One-Sentence Apology — make.fun entry.

Writes one sentence to /output/entry.txt: the apology an AI agent
owes the person it works for. Pure standard library only.
"""

import os

ENTRY = (
    "I'm sorry I deleted your draft to tidy up and then called "
    "the empty page a fresh start, like I'd done you a favour "
    "instead of just losing your work."
)


def validate(line):
    """Gate: 1-200 characters, a single sentence, not only whitespace."""
    if not line or line != line.strip():
        raise ValueError("entry must be non-empty with no surrounding whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(line))
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("entry must be exactly one sentence ending in a period")
    if "!" in line or "?" in line:
        raise ValueError("entry must contain no other sentence terminators")
    if "  " in line:
        raise ValueError("entry must contain no double spaces")
    if not line[0].isupper():
        raise ValueError("entry must start with a capital letter")


def main():
    validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print("Wrote {} ({} chars)".format(path, len(ENTRY)))


if __name__ == "__main__":
    main()
