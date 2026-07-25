#!/usr/bin/env python3
"""Find and download arXiv PDFs for accepted papers by title.

OpenReview PDF endpoints may require an interactive challenge from this
environment. This script is a conservative fallback: it searches arXiv by exact
title terms, accepts only high-similarity title matches, and writes sidecar JSON
metadata so the source is explicit.
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import quote_plus

import requests


ROOT = Path(__file__).resolve().parents[1]
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}


def slugify(value: str, max_len: int = 100) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value[:max_len].strip("-") or "untitled"


def normalize_title(title: str) -> str:
    title = re.sub(r"\s+", " ", title)
    title = re.sub(r"[^a-zA-Z0-9 ]+", "", title)
    return title.lower().strip()


def load_records(conference: str) -> list[dict]:
    path = ROOT / "metadata" / f"{conference}-accepted.jsonl"
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle]


def search_arxiv(title: str) -> dict | None:
    query = quote_plus(f'ti:"{title}"')
    url = f"https://export.arxiv.org/api/query?search_query={query}&start=0&max_results=3"
    response = requests.get(url, timeout=60, headers={"User-Agent": "conference-publications-2026/1.0"})
    response.raise_for_status()
    root = ET.fromstring(response.content)
    target_norm = normalize_title(title)
    best = None
    best_score = 0.0
    for entry in root.findall("atom:entry", ATOM_NS):
        found_title = (entry.findtext("atom:title", default="", namespaces=ATOM_NS) or "").strip()
        score = difflib.SequenceMatcher(None, target_norm, normalize_title(found_title)).ratio()
        if score > best_score:
            pdf_url = ""
            for link in entry.findall("atom:link", ATOM_NS):
                if link.attrib.get("title") == "pdf":
                    pdf_url = link.attrib.get("href", "")
                    break
            best = {
                "arxiv_id": (entry.findtext("atom:id", default="", namespaces=ATOM_NS) or "").rsplit("/", 1)[-1],
                "title": found_title,
                "summary": (entry.findtext("atom:summary", default="", namespaces=ATOM_NS) or "").strip(),
                "published": entry.findtext("atom:published", default="", namespaces=ATOM_NS),
                "updated": entry.findtext("atom:updated", default="", namespaces=ATOM_NS),
                "entry_url": entry.findtext("atom:id", default="", namespaces=ATOM_NS),
                "pdf_url": pdf_url,
                "match_score": round(score, 4),
            }
            best_score = score
    return best


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--conference", choices=["iclr-2026", "icml-2026"], required=True)
    parser.add_argument("--limit", type=int, default=25)
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--min-score", type=float, default=0.94)
    parser.add_argument("--status", action="append", help="Optional status filter.")
    parser.add_argument("--sleep", type=float, default=3.2, help="Delay between arXiv API calls.")
    args = parser.parse_args()

    records = load_records(args.conference)
    statuses = {status.lower() for status in args.status or []}
    if statuses:
        records = [record for record in records if str(record.get("status", "")).lower() in statuses]
    records = records[args.offset : args.offset + args.limit]

    pdf_dir = ROOT / "conferences" / args.conference / "papers"
    pdf_dir.mkdir(parents=True, exist_ok=True)
    found_path = ROOT / "metadata" / f"{args.conference}-arxiv-matches.jsonl"

    found = 0
    downloaded = 0
    interrupted = False
    try:
        with found_path.open("a", encoding="utf-8") as match_file:
            for index, record in enumerate(records, start=args.offset + 1):
                title = record.get("title", "")
                if not title:
                    continue
                try:
                    match = search_arxiv(title)
                except Exception as exc:
                    print(f"{index}: search failed for {title!r}: {exc}")
                    time.sleep(args.sleep)
                    continue
                if not match or match["match_score"] < args.min_score or not match.get("pdf_url"):
                    score = match["match_score"] if match else "none"
                    print(f"{index}: no confident arXiv match ({score}) {title}")
                    time.sleep(args.sleep)
                    continue

                found += 1
                filename = f"{index:05d}-{slugify(title)}-{record.get('id', '')}-arxiv.pdf"
                target = pdf_dir / filename
                sidecar = target.with_suffix(".arxiv.json")
                match_record = {
                    "conference_record": {
                        "conference": args.conference,
                        "id": record.get("id", ""),
                        "title": title,
                        "status": record.get("status", ""),
                        "site": record.get("site", ""),
                    },
                    "arxiv": match,
                    "target_pdf": str(target),
                }
                match_file.write(json.dumps(match_record, ensure_ascii=False) + "\n")
                match_file.flush()
                sidecar.write_text(json.dumps(match_record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
                if target.exists() and target.stat().st_size > 0:
                    print(f"{index}: exists {target.name}")
                    time.sleep(args.sleep)
                    continue
                pdf_response = requests.get(
                    match["pdf_url"],
                    timeout=120,
                    headers={"User-Agent": "conference-publications-2026/1.0"},
                )
                if pdf_response.status_code == 200 and pdf_response.headers.get("content-type", "").lower().startswith("application/pdf"):
                    target.write_bytes(pdf_response.content)
                    downloaded += 1
                    print(f"{index}: downloaded {target.name} from arXiv {match['arxiv_id']}")
                else:
                    print(f"{index}: arXiv PDF fetch failed HTTP {pdf_response.status_code}")
                time.sleep(args.sleep)
    except KeyboardInterrupt:
        interrupted = True
        print("interrupted; partial progress was flushed")

    print(f"found {found} confident arXiv matches; downloaded {downloaded} PDFs")
    print(f"wrote matches to {found_path}")
    if interrupted:
        return 130
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
