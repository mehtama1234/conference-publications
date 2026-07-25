#!/usr/bin/env python3
"""Create accepted-publication manifests from conference metadata."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ACCEPTED_STATUSES = {"poster", "spotlight", "oral"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--conference", action="append", choices=["iclr-2026", "icml-2026"])
    args = parser.parse_args()

    conferences = args.conference or ["iclr-2026", "icml-2026"]
    for conference in conferences:
        source = ROOT / "metadata" / f"{conference}-papercopilot.jsonl"
        target = ROOT / "metadata" / f"{conference}-accepted.jsonl"
        accepted = []
        with source.open(encoding="utf-8") as handle:
            for line in handle:
                record = json.loads(line)
                status = str(record.get("status", "")).strip().lower()
                if status in ACCEPTED_STATUSES:
                    accepted.append(record)
        with target.open("w", encoding="utf-8") as handle:
            for record in accepted:
                handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        print(f"wrote {target} ({len(accepted)} accepted records)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

