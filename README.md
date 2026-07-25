# Conference Publications 2026

Local working area for downloading and analyzing ICML 2026 and ICLR 2026 publications.

## Layout

- `conferences/iclr-2026/papers/`: ICLR 2026 PDFs.
- `conferences/iclr-2026/text/`: extracted text from PDFs.
- `conferences/iclr-2026/notes/`: per-paper notes and writeups.
- `conferences/icml-2026/papers/`: ICML 2026 PDFs.
- `conferences/icml-2026/text/`: extracted text from PDFs.
- `conferences/icml-2026/notes/`: per-paper notes and writeups.
- `metadata/`: JSONL manifests and fetch state.
- `analysis/per-paper/`: cross-linked per-paper analysis drafts.
- `analysis/themes/`: theme and subtheme indexes.
- `analysis/syntheses/`: higher-level synthesis documents.
- `scripts/`: resumable acquisition and processing scripts.
- `logs/`: run logs.

## Current Source Strategy

The primary source is OpenReview. Scripts are written to use the public HTTP API and can be safely retried when rate limits clear.

## Typical Flow

```bash
cd /home/manishmehta/projects/ui-projects/conference-publications-2026
python3 scripts/fetch_openreview.py --conference iclr-2026
python3 scripts/fetch_openreview.py --conference icml-2026
python3 scripts/fetch_arxiv_pdfs.py --conference iclr-2026 --status Oral --limit 25
.venv/bin/python scripts/extract_pdf_text.py --conference iclr-2026
.venv/bin/python scripts/extract_pdf_text.py --conference icml-2026
```

If the local virtualenv does not exist yet:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install pypdf
```

Use `python3 scripts/progress_report.py` to check current corpus, PDF, text, note, and theme-index progress.

OpenReview is the preferred official source. When OpenReview PDF access is challenge-gated, `scripts/fetch_arxiv_pdfs.py` can conservatively download high-confidence arXiv matches and writes `.arxiv.json` sidecars for provenance.

## Git Notes

The raw `metadata/iclr-2026-papercopilot.jsonl` file is larger than GitHub's normal file-size limit, so it is ignored for git. The same records are stored in versioned split files under `metadata/iclr-2026-papercopilot.parts/`.

## Analysis Files

- Start with `analysis/themes/theme-index.md`.
- Use `analysis/per-paper/template.md` for individual writeups.
- Use `analysis/syntheses/cross-conference-patterns.md` for emerging patterns.
