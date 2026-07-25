# ICLR Oral Batch 013 Synthesis

## Papers Covered

- Mamba-3: Improved Sequence Modeling using State Space Principles
- Rodrigues Network for Learning Robot Actions
- p-less Sampling: A Robust Hyperparameter-Free Approach for LLM Decoding
- MC-Search: Evaluating and Enhancing Multimodal Agentic Search with Structured Long Reasoning Chains
- InfoTok: Adaptive Discrete Video Tokenizer via Information-Theoretic Compression

## Shared Thesis

This batch is about structure-aware compute allocation. The papers do not treat scale as a uniform increase in parameters, tokens, samples, or retrieval calls. They add structure that tells a model where computation should go: Mamba-3 uses state-space recurrence for efficient long-sequence state tracking, RodriNet embeds kinematic structure into action representations, p-less sampling uses the token distribution itself to control decoding, MC-Search evaluates and trains multimodal search as a verified stepwise process, and InfoTok allocates video tokens according to information density.

## Deep Themes

### Efficient sequence and memory mechanisms

Mamba-3 and InfoTok both target the cost of long inputs, but at different layers of the stack. Mamba-3 changes the sequence model so recurrence can retain useful state without quadratic attention cost. InfoTok changes the input representation so long videos do not spend equal token budget on low- and high-information regions. Together they show a broader 2026 pattern: efficiency work is becoming representation- and architecture-aware rather than simply pruning or compressing a finished model.

### Inductive bias as a substitute for brute force

RodriNet is the clearest example of domain structure doing work that a generic model would otherwise need to learn from data. Its Neural Rodrigues Operator turns a classical kinematic primitive into a learnable action-processing module. This mirrors a wider pattern across robotics and scientific modeling papers: strong geometric or physical priors are being reintroduced as trainable components instead of hand-coded pipelines.

### Inference control from internal signals

p-less sampling fits a growing cluster of methods that use internal probability, entropy, attention, or state statistics as control signals at inference time. The important shift is that the decoding policy becomes adaptive without manual threshold selection. This connects to attention-state stopping, entropy-guided cache allocation, and other test-time controllers where the model's own uncertainty shapes resource use.

### Process supervision for agentic systems

MC-Search reflects the evaluation side of the same movement. Agentic multimodal RAG is not just a final-answer problem; it is a planning, retrieval, modality-selection, and evidence-attribution problem. The benchmark and Search-Align make intermediate search decisions first-class training and evaluation objects.

## Cross-Paper Pattern

The common pattern is selective structure. Each paper identifies a place where uniform processing wastes capacity or hides failure: dense attention over long sequences, generic action features for articulated motion, fixed sampling thresholds, final-answer-only RAG evaluation, and fixed-rate video tokenization. The solution in each case is to expose an intermediate control variable: recurrent state, kinematic transformations, probability-distribution thresholds, hop-level retrieval plans, or variable token counts.

## Subthemes to Track

- Inference-first sequence architectures.
- Neuralized classical operators for embodied action.
- Hyperparameter-free decoding and uncertainty-aware sampling.
- Agentic multimodal search with process-level verification.
- Information-theoretic variable-length tokenization.

## Confidence and Source Depth

These notes are currently based on conference metadata and abstracts. The patterns are strong enough for cross-paper indexing, but implementation details should be upgraded after OpenReview or arXiv PDF access succeeds.
