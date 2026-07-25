#!/usr/bin/env python3
"""Create aggregate summaries from local conference metadata."""

from __future__ import annotations

import argparse
import collections
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "in",
    "into",
    "is",
    "it",
    "its",
    "of",
    "on",
    "or",
    "our",
    "that",
    "the",
    "their",
    "this",
    "to",
    "via",
    "we",
    "with",
}

THEME_QUERIES = {
    "test-time scaling and inference-time compute": [
        "test-time",
        "inference-time",
        "chain-of-thought",
        "reasoning",
        "search",
        "mcts",
        "self-consistency",
    ],
    "LLM agents, tool use, and planning": [
        "agent",
        "agents",
        "tool",
        "tools",
        "planning",
        "workflow",
        "browser",
        "multi-agent",
    ],
    "retrieval, memory, and grounding": [
        "retrieval",
        "rag",
        "memory",
        "grounding",
        "knowledge",
        "database",
        "documents",
    ],
    "alignment, preference optimization, and feedback": [
        "alignment",
        "preference",
        "rlhf",
        "dpo",
        "reward model",
        "human feedback",
        "constitutional",
    ],
    "safety, robustness, and adversarial behavior": [
        "safety",
        "robust",
        "robustness",
        "adversarial",
        "jailbreak",
        "attack",
        "defense",
        "certified",
    ],
    "diffusion and flow generative modeling": [
        "diffusion",
        "flow matching",
        "score-based",
        "denoising",
        "rectified flow",
        "generative",
    ],
    "multimodal and embodied models": [
        "multimodal",
        "vision-language",
        "vlm",
        "video",
        "audio",
        "robot",
        "embodied",
    ],
    "efficient training, adaptation, and compression": [
        "efficient",
        "efficiency",
        "compression",
        "quantization",
        "lora",
        "adapter",
        "pruning",
        "distillation",
    ],
    "data quality, synthetic data, and curation": [
        "synthetic data",
        "data curation",
        "dataset",
        "data quality",
        "annotation",
        "benchmark",
    ],
    "evaluation, benchmarks, and measurement": [
        "evaluation",
        "benchmark",
        "metrics",
        "measure",
        "leaderboard",
        "generalization",
    ],
    "privacy, federated learning, and security": [
        "privacy",
        "federated",
        "secure",
        "confidential",
        "differential privacy",
        "membership inference",
    ],
    "causality, uncertainty, and scientific modeling": [
        "causal",
        "causality",
        "uncertainty",
        "bayesian",
        "scientific",
        "physics",
    ],
}


def load_records(conference: str, accepted_only: bool) -> list[dict]:
    suffix = "accepted" if accepted_only else "papercopilot"
    path = ROOT / "metadata" / f"{conference}-{suffix}.jsonl"
    records = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            records.append(json.loads(line))
    return records


def tokenize(text: str) -> list[str]:
    return [
        token
        for token in re.findall(r"[a-z][a-z0-9-]{2,}", text.lower())
        if token not in STOPWORDS
    ]


def matches(record: dict, terms: list[str]) -> bool:
    text = " ".join(
        str(record.get(field, ""))
        for field in ["title", "abstract", "tldr", "keywords", "primary_area"]
    ).lower()
    return any(term in text for term in terms)


def summarize_conference(conference: str, records: list[dict]) -> str:
    status_counts = collections.Counter(record.get("status") or "unknown" for record in records)
    area_counts = collections.Counter(record.get("primary_area") or "unknown" for record in records)
    keyword_counts: collections.Counter[str] = collections.Counter()
    token_counts: collections.Counter[str] = collections.Counter()

    for record in records:
        for keyword in str(record.get("keywords", "")).split(";"):
            keyword = keyword.strip().lower()
            if keyword:
                keyword_counts[keyword] += 1
        token_counts.update(tokenize(f"{record.get('title', '')} {record.get('abstract', '')}"))

    lines = [f"## {conference.upper()}", "", f"Records: {len(records)}", ""]
    lines.append("### Status Counts")
    for status, count in status_counts.most_common(20):
        lines.append(f"- {status}: {count}")
    lines.append("")
    lines.append("### Top Primary Areas")
    for area, count in area_counts.most_common(25):
        lines.append(f"- {area}: {count}")
    lines.append("")
    lines.append("### Top Keywords")
    for keyword, count in keyword_counts.most_common(30):
        lines.append(f"- {keyword}: {count}")
    lines.append("")
    lines.append("### Top Abstract/Title Terms")
    for token, count in token_counts.most_common(40):
        lines.append(f"- {token}: {count}")
    return "\n".join(lines)


def summarize_themes(all_records: list[dict]) -> str:
    lines = ["# Metadata-Derived Theme Scaffold", ""]
    lines.append(
        "This is a first-pass scaffold from titles, abstracts, keywords, areas, and statuses. It should be refined after PDF-level reading."
    )
    lines.append("")
    for theme, terms in THEME_QUERIES.items():
        hits = [record for record in all_records if matches(record, terms)]
        by_conf = collections.Counter(record["conference"] for record in hits)
        lines.append(f"## {theme.title()}")
        lines.append("")
        lines.append(f"Records matched: {len(hits)}")
        for conference, count in by_conf.most_common():
            lines.append(f"- {conference}: {count}")
        lines.append("")
        lines.append("Example papers:")
        for record in hits[:8]:
            title = record.get("title", "").replace("\n", " ")
            status = record.get("status", "")
            lines.append(f"- {record['conference']} / {status}: {title} ({record.get('site', '')})")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--conference", action="append", choices=["iclr-2026", "icml-2026"])
    parser.add_argument("--accepted-only", action="store_true")
    args = parser.parse_args()

    conferences = args.conference or ["iclr-2026", "icml-2026"]
    records_by_conf = {
        conference: load_records(conference, args.accepted_only) for conference in conferences
    }
    scope = "Accepted Publications" if args.accepted_only else "All Public Records"
    output = [f"# Corpus Metadata Summary: {scope}", ""]
    for conference, records in records_by_conf.items():
        output.append(summarize_conference(conference, records))
        output.append("")

    stem = "accepted-metadata" if args.accepted_only else "metadata"
    summary_path = ROOT / "analysis" / "syntheses" / f"{stem}-summary.md"
    summary_path.write_text("\n".join(output).strip() + "\n", encoding="utf-8")

    theme_path = ROOT / "analysis" / "themes" / f"{stem}-theme-scaffold.md"
    all_records = [record for records in records_by_conf.values() for record in records]
    theme_path.write_text(summarize_themes(all_records), encoding="utf-8")

    print(f"wrote {summary_path}")
    print(f"wrote {theme_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
