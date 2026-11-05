"""Synchronize repository copies only; never install into an agent's home directory."""
from pathlib import Path
import argparse

ROOT = Path(__file__).resolve().parents[1]
PROFILES = ("codex/AGENTS.md", "claude/CLAUDE.md", "shared/AGENTS.md", "agy/AGENTS.md")
BEGIN = "<!-- BEGIN CAPABILITY POLICY v1 -->"
END = "<!-- END CAPABILITY POLICY v1 -->"


def render(original: bytes, policy: str) -> bytes:
    text = original.decode("utf-8")
    newline = "\r\n" if "\r\n" in text else "\n"
    text = text.replace("\r\n", "\n")
    block = BEGIN + "\n" + policy.strip() + "\n" + END
    if text.count(BEGIN) != text.count(END) or text.count(BEGIN) > 1:
        raise ValueError("Malformed or duplicate managed markers")
    if BEGIN in text:
        start, stop = text.index(BEGIN), text.index(END) + len(END)
        if stop <= start:
            raise ValueError("Reversed managed markers")
        text = text[:start] + block + text[stop:]
    else:
        text = text.rstrip("\n") + "\n\n" + block + "\n"
    return text.replace("\n", newline).encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="Check only (the default)")
    mode.add_argument("--write", action="store_true", help="Update only the four repository profiles")
    args = parser.parse_args()
    policy = (ROOT / "shared/CAPABILITY_POLICY.md").read_text(encoding="utf-8")
    drift = []
    for name in PROFILES:
        target = ROOT / name
        before = target.read_bytes()
        after = render(before, policy)
        if before != after:
            drift.append(name)
            if args.write:
                target.write_bytes(after)
    print("PASS: capability policy synchronized" if not drift or args.write else "FAIL: drift in " + ", ".join(drift))
    return int(bool(drift) and not args.write)


if __name__ == "__main__":
    raise SystemExit(main())
