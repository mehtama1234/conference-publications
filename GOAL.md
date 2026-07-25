# Long-Horizon Goal: ICML and ICLR 2026 Theme Mining

## Objective

Build a local corpus of ICML 2026 and ICLR 2026 publications, then analyze the papers one by one to identify deep themes, subthemes, recurring mechanisms, methodological patterns, evaluation patterns, and broader research directions.

## Target Output

- Downloaded publication corpus organized by conference.
- Metadata manifests for each conference.
- Extracted text for each downloaded paper when possible.
- Per-paper writeups with rich detail.
- Theme index with evidence linked back to papers.
- Cross-conference synthesis identifying common patterns and divergences.

## Operating Principles

- Keep all work resumable. Every script should be safe to re-run.
- Preserve source metadata and original PDFs.
- Separate raw material from interpretation.
- Write per-paper notes before global synthesis.
- Record uncertainty when a theme is inferred rather than directly stated.

## Analysis Passes

1. Corpus acquisition
   - Fetch official metadata for ICLR 2026 and ICML 2026.
   - Download PDFs into conference-specific folders.
   - Track download status in manifests.

2. Per-paper reading
   - Extract title, authors, abstract, claimed contribution, method, experiments, limits, and implications.
   - Assign initial tags and subthemes.
   - Save one writeup per paper.

3. Theme consolidation
   - Cluster repeated ideas across papers.
   - Distinguish surface topics from deeper research moves.
   - Track which papers support each theme.

4. Cross-conference synthesis
   - Compare ICML and ICLR emphases.
   - Identify shared methodological patterns.
   - Identify gaps, tensions, and emerging directions.

5. Final synthesis
   - Produce a rich taxonomy of themes and subthemes.
   - Write a narrative summary of the field-level patterns.
   - Include concrete paper evidence for every major claim.

