#!/usr/bin/env python3
"""Extract text from downloaded PDFs when pypdf is available."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_reader():
    try:
        from pypdf import PdfReader

        return PdfReader
    except ImportError:
        try:
            from PyPDF2 import PdfReader

            return PdfReader
        except ImportError as exc:
            raise SystemExit(
                "PDF extraction requires pypdf or PyPDF2. Install one with: python3 -m pip install --user pypdf"
            ) from exc


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--conference", choices=["iclr-2026", "icml-2026"], required=True)
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()

    PdfReader = load_reader()
    pdf_dir = ROOT / "conferences" / args.conference / "papers"
    text_dir = ROOT / "conferences" / args.conference / "text"
    text_dir.mkdir(parents=True, exist_ok=True)

    pdfs = sorted(pdf_dir.glob("*.pdf"))
    if args.limit is not None:
        pdfs = pdfs[: args.limit]

    for pdf in pdfs:
        target = text_dir / f"{pdf.stem}.txt"
        if target.exists() and target.stat().st_size > 0:
            continue
        try:
            reader = PdfReader(str(pdf))
            pages = []
            for page_number, page in enumerate(reader.pages, start=1):
                text = page.extract_text() or ""
                pages.append(f"\\n\\n--- page {page_number} ---\\n\\n{text}")
            target.write_text("".join(pages).strip() + "\\n", encoding="utf-8", errors="replace")
            print(f"extracted {target.name}")
        except Exception as exc:
            print(f"failed {pdf.name}: {exc}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
