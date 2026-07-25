#!/usr/bin/env python3
"""Fetch Paper Copilot metadata as a secondary source.

This does not replace official OpenReview/PMLR records, but it is useful when
OpenReview's API requires an interactive challenge. The records include titles,
abstracts, keywords, areas, statuses, and OpenReview IDs.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import requests


ROOT = Path(__file__).resolve().parents[1]

SOURCES = {
    "iclr-2026": "https://media.githubusercontent.com/media/papercopilot/paperlists/main/iclr/iclr2026.json",
    "icml-2026": "https://raw.githubusercontent.com/papercopilot/paperlists/main/icml/icml2026.json",
}


def normalize_record(conference: str, raw: dict) -> dict:
    openreview_id = raw.get("id") or raw.get("paper_id") or ""
    authors = raw.get("author") or ""
    if isinstance(authors, str):
        authors = [part for part in authors.split(";") if part]
    return {
        "source": "papercopilot",
        "conference": conference,
        "id": openreview_id,
        "paper_id": raw.get("paper_id", ""),
        "title": raw.get("title", ""),
        "authors": authors,
        "abstract": raw.get("abstract", ""),
        "tldr": raw.get("tldr", ""),
        "keywords": raw.get("keywords", ""),
        "primary_area": raw.get("primary_area", ""),
        "track": raw.get("track", ""),
        "status": raw.get("status", ""),
        "site": raw.get("site") or f"https://openreview.net/forum?id={openreview_id}",
        "pdf_url": f"https://openreview.net/pdf?id={openreview_id}" if openreview_id else "",
        "bibtex": raw.get("bibtex", ""),
        "ratings": {
            "recommendation_avg": raw.get("recommendation_avg", ""),
            "confidence_avg": raw.get("confidence_avg", ""),
            "soundness_avg": raw.get("soundness_avg", ""),
            "presentation_avg": raw.get("presentation_avg", ""),
            "contribution_avg": raw.get("contribution_avg", ""),
            "originality_avg": raw.get("originality_avg", ""),
            "significance_avg": raw.get("significance_avg", ""),
        },
        "raw": raw,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--conference", choices=sorted(SOURCES), required=True)
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()

    response = requests.get(SOURCES[args.conference], timeout=180)
    response.raise_for_status()
    data = json.loads(response.content.decode("utf-8"))
    if args.limit is not None:
        data = data[: args.limit]

    output = ROOT / "metadata" / f"{args.conference}-papercopilot.jsonl"
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as handle:
        for raw in data:
            handle.write(json.dumps(normalize_record(args.conference, raw), ensure_ascii=False) + "\n")

    print(f"wrote {output} ({len(data)} records)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

