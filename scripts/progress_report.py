#!/usr/bin/env python3
"""Report corpus and note-analysis progress."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def count_lines(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open(encoding="utf-8") as handle:
        return sum(1 for _ in handle)


def note_status(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if "TODO" not in text:
        return "filled"
    if text.count("TODO") < 10:
        return "partial"
    return "stub"


def main() -> int:
    print("# Conference Publications 2026 Progress\n")
    for conference in ["iclr-2026", "icml-2026"]:
        accepted = count_lines(ROOT / "metadata" / f"{conference}-accepted.jsonl")
        all_records = count_lines(ROOT / "metadata" / f"{conference}-papercopilot.jsonl")
        pdfs = len(list((ROOT / "conferences" / conference / "papers").glob("*.pdf")))
        texts = len(list((ROOT / "conferences" / conference / "text").glob("*.txt")))
        notes = sorted((ROOT / "conferences" / conference / "notes").glob("*.md"))
        statuses = {"filled": 0, "partial": 0, "stub": 0}
        for note in notes:
            statuses[note_status(note)] += 1

        print(f"## {conference}")
        print(f"- Public metadata records: {all_records}")
        print(f"- Accepted publication records: {accepted}")
        print(f"- PDFs downloaded: {pdfs}")
        print(f"- Text files extracted: {texts}")
        print(f"- Note files: {len(notes)}")
        print(f"- Filled notes: {statuses['filled']}")
        print(f"- Partial notes: {statuses['partial']}")
        print(f"- Stub notes: {statuses['stub']}")
        print("")

    theme_index = ROOT / "analysis" / "themes" / "theme-index.md"
    evidence_rows = max(0, count_lines(theme_index) - 8)
    print("## Theme Evidence")
    print(f"- Evidence rows in theme index: {evidence_rows}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

