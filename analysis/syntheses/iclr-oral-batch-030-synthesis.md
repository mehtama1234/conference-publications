# ICLR Oral Batch 030 Synthesis

## Papers Covered

- EigenBench: A Comparative Behavioral Measure of Value Alignment
- Diffusion Language Model Knows the Answer Before It Decodes
- A Representer Theorem for Hawkes Processes via Penalized Least Squares Minimization
- Sequences of Logits Reveal the Low Rank Structure of Language Models
- Semi-Supervised Preference Optimization with Limited Feedback

## Shared Thesis

This batch is about extracting useful structure from comparisons, intermediate states, and unlabeled signals. EigenBench derives value-alignment scores from model-to-model judgments. Prophet accelerates diffusion language models by detecting early answer convergence. The Hawkes representer theorem turns infinite-dimensional triggering-kernel estimation into a finite efficient estimator. Logit-sequence analysis reveals low-rank structure in black-box LM behavior. SSPO turns limited preference feedback plus unpaired responses into semi-supervised alignment. Across the batch, hidden structure becomes exploitable once the right mathematical or procedural lens is applied.

## Deep Themes

### Label-Free and Weak-Label Evaluation

EigenBench and SSPO both work around missing labels. EigenBench handles subjective value alignment without ground truth by aggregating comparative model judgments. SSPO uses a small labeled preference set to pseudo-label unpaired responses. Both show how alignment research is moving beyond fully labeled preference pairs.

### Early Convergence and Low-Rank Behavior

Prophet and logit-sequence low-rank analysis both find exploitable structure in model outputs before or beyond direct decoding. DLMs often know the answer before completing all refinement steps. LM logits across prompts and responses form low-rank matrices that can be recombined for generation. These are inference-time structure discoveries.

### Classical Theory for Scalable Temporal Modeling

The Hawkes representer theorem is a reminder that exact mathematical structure can remove computation. Analytically fixed dual coefficients turn RKHS event-kernel estimation into a more scalable procedure.

### Alignment Under Scarce Supervision

EigenBench and SSPO point to two complementary scarce-supervision strategies: comparative peer judging for subjective traits and reward-threshold pseudo-labeling for preference training. Both are attempts to reduce dependence on expensive human labels while keeping alignment behavior measurable.

## Cross-Paper Pattern

The shared pattern is hidden compression. Subjective values compress into EigenTrust scores, DLM refinement trajectories compress into early stopping decisions, Hawkes kernels compress into transformed finite bases, LM logits compress into low-rank output spaces, and preference labels compress into reward thresholds for pseudo-labeling. The batch reinforces the broader theme that capability often depends on discovering the compact structure beneath expensive evaluation or inference.

## Subthemes to Track

- Comparative value-alignment scoring.
- Early-commit diffusion LM decoding.
- Representer theorem for Hawkes processes.
- Low-rank logit structure in LMs.
- Semi-supervised preference optimization.

## Confidence and Source Depth

These notes are based on abstracts and local metadata. Formal details, validation protocols, and benchmark settings should be upgraded when PDFs are available.
