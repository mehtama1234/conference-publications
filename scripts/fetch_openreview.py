#!/usr/bin/env python3
"""Fetch OpenReview metadata and PDFs for 2026 conference papers.

The script is intentionally resumable:
- Metadata is written as JSONL.
- Existing PDFs are skipped.
- HTTP 429 and transient errors are retried with backoff.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path
from typing import Any
from urllib.parse import urlencode

import requests


ROOT = Path(__file__).resolve().parents[1]
API_BASE = "https://api2.openreview.net/notes"
PDF_BASE = "https://openreview.net/pdf"

CONFERENCES = {
    "iclr-2026": {
        "venue_id": "ICLR.cc/2026/Conference",
        "invitation": "ICLR.cc/2026/Conference/-/Submission",
    },
    "icml-2026": {
        "venue_id": "ICML.cc/2026/Conference",
        "invitation": "ICML.cc/2026/Conference/-/Submission",
    },
}


def slugify(value: str, max_len: int = 100) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value[:max_len].strip("-") or "untitled"


def get_content(note: dict[str, Any], key: str, default: Any = "") -> Any:
    value = note.get("content", {}).get(key, default)
    if isinstance(value, dict) and "value" in value:
        return value["value"]
    return value


def request_json(session: requests.Session, url: str, *, retries: int = 8) -> dict[str, Any]:
    delay = 5
    for attempt in range(retries):
        response = session.get(url, timeout=60)
        if response.status_code == 200:
            return response.json()
        if response.status_code in {429, 500, 502, 503, 504}:
            retry_after = response.headers.get("Retry-After")
            sleep_for = int(retry_after) if retry_after and retry_after.isdigit() else delay
            print(f"retryable HTTP {response.status_code}; sleeping {sleep_for}s", file=sys.stderr)
            time.sleep(sleep_for)
            delay = min(delay * 2, 120)
            continue
        response.raise_for_status()
    raise RuntimeError(f"failed after {retries} attempts: {url}")


def iter_notes(session: requests.Session, conference: str, limit: int | None) -> list[dict[str, Any]]:
    config = CONFERENCES[conference]
    collected: list[dict[str, Any]] = []
    offset = 0
    page_limit = 100

    while True:
        remaining = None if limit is None else limit - len(collected)
        if remaining is not None and remaining <= 0:
            break
        current_limit = min(page_limit, remaining) if remaining is not None else page_limit
        query = {
            "content.venueid": config["venue_id"],
            "limit": current_limit,
            "offset": offset,
            "details": "replyCount,presentation",
        }
        url = f"{API_BASE}?{urlencode(query)}"
        payload = request_json(session, url)
        notes = payload.get("notes", [])
        if not notes:
            break
        collected.extend(notes)
        print(f"{conference}: fetched {len(collected)} metadata records", file=sys.stderr)
        offset += len(notes)

    return collected


def write_manifest(conference: str, notes: list[dict[str, Any]]) -> Path:
    manifest = ROOT / "metadata" / f"{conference}-openreview.jsonl"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    with manifest.open("w", encoding="utf-8") as handle:
        for note in notes:
            title = get_content(note, "title", "")
            authors = get_content(note, "authors", [])
            record = {
                "id": note.get("id"),
                "forum": note.get("forum"),
                "number": note.get("number"),
                "title": title,
                "authors": authors,
                "abstract": get_content(note, "abstract", ""),
                "venue": get_content(note, "venue", ""),
                "venueid": get_content(note, "venueid", ""),
                "pdf_url": f"{PDF_BASE}?id={note.get('id')}",
                "source_url": f"https://openreview.net/forum?id={note.get('forum') or note.get('id')}",
            }
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    return manifest


def download_pdfs(session: requests.Session, conference: str, notes: list[dict[str, Any]]) -> None:
    pdf_dir = ROOT / "conferences" / conference / "papers"
    pdf_dir.mkdir(parents=True, exist_ok=True)

    for index, note in enumerate(notes, start=1):
        note_id = note.get("id")
        title = get_content(note, "title", "")
        filename = f"{index:05d}-{slugify(str(title))}-{note_id}.pdf"
        target = pdf_dir / filename
        if target.exists() and target.stat().st_size > 0:
            continue
        url = f"{PDF_BASE}?id={note_id}"
        delay = 5
        for attempt in range(8):
            response = session.get(url, timeout=120)
            if response.status_code == 200 and response.headers.get("content-type", "").lower().startswith("application/pdf"):
                target.write_bytes(response.content)
                print(f"downloaded {target.name}", file=sys.stderr)
                break
            if response.status_code in {429, 500, 502, 503, 504}:
                retry_after = response.headers.get("Retry-After")
                sleep_for = int(retry_after) if retry_after and retry_after.isdigit() else delay
                print(f"{note_id}: HTTP {response.status_code}; sleeping {sleep_for}s", file=sys.stderr)
                time.sleep(sleep_for)
                delay = min(delay * 2, 120)
                continue
            print(f"{note_id}: skipped PDF HTTP {response.status_code}", file=sys.stderr)
            break


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--conference", choices=sorted(CONFERENCES), required=True)
    parser.add_argument("--limit", type=int, default=None, help="Optional small test limit.")
    parser.add_argument("--metadata-only", action="store_true")
    args = parser.parse_args()

    session = requests.Session()
    session.headers.update({"User-Agent": "conference-publications-2026-local-research/1.0"})
    notes = iter_notes(session, args.conference, args.limit)
    manifest = write_manifest(args.conference, notes)
    print(f"wrote {manifest} ({len(notes)} records)")
    if not args.metadata_only:
        download_pdfs(session, args.conference, notes)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

