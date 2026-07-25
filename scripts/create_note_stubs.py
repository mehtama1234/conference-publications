#!/usr/bin/env python3
"""Create per-paper note stubs from accepted manifests."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def slugify(value: str, max_len: int = 90) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value[:max_len].strip("-") or "untitled"


def load_records(conference: str) -> list[dict]:
    path = ROOT / "metadata" / f"{conference}-accepted.jsonl"
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle]


def render_note(record: dict) -> str:
    authors = record.get("authors", [])
    if isinstance(authors, list):
        authors_text = "; ".join(authors)
    else:
        authors_text = str(authors)
    return f"""# {record.get("title", "Untitled")}

## Metadata

- Conference: {record.get("conference", "")}
- Status: {record.get("status", "")}
- OpenReview ID: {record.get("id", "")}
- Authors: {authors_text}
- Primary area: {record.get("primary_area", "")}
- Keywords: {record.get("keywords", "")}
- Source URL: {record.get("site", "")}
- PDF URL: {record.get("pdf_url", "")}

## Abstract

{record.get("abstract", "")}

## One-Sentence Claim

TODO

## Problem

TODO

## Core Contribution

TODO

## Method

TODO

## Experiments and Evidence

TODO

## Limits and Failure Modes

TODO

## Deep Themes

TODO

## Subthemes

TODO

## Connections to Other Papers

TODO

## Notes for Cross-Paper Synthesis

TODO
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--conference", choices=["iclr-2026", "icml-2026"], required=True)
    parser.add_argument("--status", action="append", help="Filter by status; can be repeated.")
    parser.add_argument("--offset", type=int, default=0, help="Skip this many filtered records before creating notes.")
    parser.add_argument("--limit", type=int, default=25)
    parser.add_argument("--filename-prefix", default="", help="Optional prefix for generated filenames, e.g. poster-.")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    statuses = {status.lower() for status in args.status or []}
    records = load_records(args.conference)
    if statuses:
        records = [record for record in records if str(record.get("status", "")).lower() in statuses]
    records = records[args.offset : args.offset + args.limit]

    out_dir = ROOT / "conferences" / args.conference / "notes"
    out_dir.mkdir(parents=True, exist_ok=True)
    created = 0
    for index, record in enumerate(records, start=args.offset + 1):
        filename = f"{args.filename_prefix}{index:05d}-{slugify(record.get('title', 'untitled'))}-{record.get('id', '')}.md"
        target = out_dir / filename
        if target.exists() and not args.overwrite:
            continue
        target.write_text(render_note(record), encoding="utf-8")
        created += 1

    print(f"created {created} notes in {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
