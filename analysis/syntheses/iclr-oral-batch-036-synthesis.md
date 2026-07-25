# ICLR Oral Batch 036 Synthesis

## Papers Covered

- FlashRNN: Unlocking Parallel Training of Nonlinear RNNs for Large Language Models
- Learning with Dual-level Noisy Correspondence for Multi-modal Entity Alignment
- SANA-Video: Efficient Video Generation with Block Linear Diffusion Transformer
- Probabilistic Kernel Function for Fast Angle Testing
- BIRD-INTERACT: Re-imagining Text-to-SQL Evaluation via Lens of Dynamic Interactions

## Shared Thesis

This batch is about scaling systems by replacing brittle assumptions with better computational structure. FlashRNN removes the sequential training bottleneck for nonlinear recurrence. RULE replaces clean-correspondence assumptions in multimodal entity alignment with reliability-aware learning. SANA-Video makes long high-resolution video generation practical through linear attention and constant-memory state. The angle-testing paper replaces Gaussian random projections with deterministic reference-angle kernels for faster vector search. BIRD-INTERACT replaces static text-to-SQL evaluation with dynamic executable interaction. Across the batch, performance improves when the method matches the structure of the real workload.

## Deep Themes

### Parallelism Beyond Standard Architectures

FlashRNN and SANA-Video both show that the bottleneck is not necessarily the model family itself but the computation pattern. FlashRNN reformulates nonlinear recurrences as parallel solvable systems; SANA-Video uses linear attention state to avoid duration-growing memory. Both papers turn architecture design into systems design.

### Robust Alignment Under Noisy Correspondence

RULE studies multimodal entity alignment when both entity-attribute and cross-graph correspondences are noisy. Its reliability-aware fusion and correspondence reasoning fit a larger theme: real-world multimodal alignment cannot assume clean pairs, clean labels, or clean graph links.

### Geometric Kernels as Retrieval Infrastructure

Fast angle testing is a low-level contribution with broad implications. Retrieval-heavy systems depend on high-dimensional similarity operations, and deterministic projection kernels can improve throughput if they preserve angular decisions with fewer assumptions.

### Dynamic Evaluation for Agents

BIRD-INTERACT extends the executable-agent benchmark trend into text-to-SQL. It tests clarification, environment exploration, execution-error recovery, and CRUD operations rather than a single generated query. The reported low GPT-5 completion rates show that interactive database work is still far from solved.

## Cross-Paper Pattern

The shared pattern is structural realism. FlashRNN respects nonlinear recurrence but changes how it is solved. RULE respects noisy multimodal graph correspondences. SANA-Video respects long-video memory constraints. The kernel paper respects the geometry of angle decisions. BIRD-INTERACT respects the interactive nature of database assistance. These papers argue that benchmark or algorithm assumptions must move closer to deployment conditions.

## Subthemes to Track

- Parallel nonlinear recurrent LLM training.
- Dual-level noisy correspondence in MMEA.
- Constant-memory linear-attention video diffusion.
- Deterministic-reference angle kernels.
- Dynamic interactive text-to-SQL benchmarks.

## Confidence and Source Depth

These notes are based on abstracts and local metadata. Formal details, validation protocols, and benchmark settings should be upgraded when PDFs are available.
