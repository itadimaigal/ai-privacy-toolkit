"""Mask personal data and secrets in text BEFORE you paste it into an AI chat.

    python redact.py notes.txt            # prints the redacted text
    python redact.py < notes.txt          # or read from stdin

It catches common patterns (emails, phone numbers, Aadhaar, PAN, cards, API keys, passwords, IPs).
It cannot catch everything, like names or addresses, so always read the result before you paste.
"""
import re
import sys

# "password: xyz", "db_password = xyz", "token='xyz'": keep the key, hide the value
SECRET_ASSIGNMENT = r"(?i)(\w*(?:password|passwd|pwd|secret|token)\w*[\"']?\s*[:=]\s*)([\"']?)[^\s\"']+\2"

# Order matters: the most specific patterns run first.
PATTERNS = [
    ("API_KEY", r"\b(?:sk|pk|rk|ghp|gho|xox[abps])[-_][A-Za-z0-9_-]{16,}\b"),
    ("API_KEY", r"\bAKIA[0-9A-Z]{16}\b"),                                    # AWS access key ID
    ("EMAIL", r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+"),
    ("CARD", r"\b\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}\b"),
    ("AADHAAR", r"\b\d{4}[ -]?\d{4}[ -]?\d{4}\b"),
    ("PAN", r"\b[A-Z]{5}\d{4}[A-Z]\b"),
    ("PHONE", r"(?:\+91[ -]?)?\b[6-9]\d{4}[ -]?\d{5}\b"),
    ("IP", r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
]


def redact(text):
    """Returns the text with each match replaced by a label such as [EMAIL]."""
    text = re.sub(SECRET_ASSIGNMENT, r"\1\2[SECRET]\2", text)
    for label, pattern in PATTERNS:
        text = re.sub(pattern, f"[{label}]", text)
    return text


if __name__ == "__main__":
    source = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else sys.stdin.read()
    print(redact(source))
