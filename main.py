"""One office-life joke for the AI judge: the open-door policy.

Writes the joke to /output/entry.txt (UTF-8, one line, 1-199 chars
so the file stays within the 200-character gate including its newline).
"""

import os

LINE = "My boss calls it an 'open-door policy' — the door is open, but every time I walk through it I leave with a project."

# Gate: entry.txt must be 1-200 characters; keep the line itself under 200
# so the trailing newline still fits inside the gate.
MAX_CHARS = 199


def validate(line: str) -> str:
    """Return the line if it is a valid single-line entry, else raise."""
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if line != line.strip():
        raise ValueError("entry line must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry line must be 1-{MAX_CHARS} chars, got {len(line)}")
    return line


def main() -> None:
    line = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # Read back and confirm the file holds exactly the validated line,
    # so a write error can never ship a truncated or altered entry.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != line + "\n":
        raise ValueError("entry.txt does not match the validated line")


if __name__ == "__main__":
    main()
