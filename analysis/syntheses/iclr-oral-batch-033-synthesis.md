# ICLR Oral Batch 033 Synthesis

## Papers Covered

- Overthinking Reduction with Decoupled Rewards and Curriculum Data Scheduling
- From Markov to Laplace: How Mamba In-Context Learns Markov Chains
- Neon: Negative Extrapolation From Self-Training Improves Image Generation
- Latent Speech-Text Transformer
- Vid-LLM: A Compact Video-based 3D Multimodal LLM with Reconstruction-Reasoning Synergy

## Shared Thesis

This batch is about finding better internal units of computation. DECS separates useful exploratory reasoning tokens from redundant reasoning tokens. The Mamba paper shows that a selective state-space model can represent an optimal statistical estimator through convolutional structure. Neon treats the direction of synthetic self-training collapse as a useful negative signal. LST compresses raw speech tokens into latent patches better aligned with text. Vid-LLM aligns reconstructed geometry with multimodal reasoning through compact adapters. Across the batch, progress comes from changing how information is represented, compressed, or penalized inside the system.

## Deep Themes

### Efficient Reasoning as Reward Decomposition

DECS frames overthinking as a reward-design problem. Length penalties are too blunt because they punish exploratory tokens and can reward partial redundancy. Decoupled token-level rewards are a more surgical attempt to optimize reasoning cost without degrading correctness.

### Architecture Theory as Statistical Estimation

The Mamba paper links an efficient sequence architecture to Laplacian smoothing for Markov-chain in-context learning. This contributes to a larger theme in the corpus: theory is becoming a way to identify when efficient non-transformer mechanisms can implement optimal estimators, rather than only a way to explain post-hoc behavior.

### Failure Directions as Learning Signals

Neon is notable because it uses degradation from synthetic self-training as a signal. Instead of treating model collapse as merely a hazard, it extracts the harmful update direction and moves away from it. This is another instance of process diagnostics becoming training signal.

### Tokenization and Latent Units for Multimodal Scaling

LST shows that raw modality tokens can be the bottleneck. By patching speech into latent units, the model reduces compute imbalance and improves speech-text alignment. Vid-LLM similarly uses intermediate geometric priors and adapters rather than feeding raw 3D data into a general MLLM.

### Intermediate Structure for Grounded Reasoning

Vid-LLM and LST both depend on intermediate representations: speech patches and metric geometric priors. These are not merely compression artifacts. They make cross-modal transfer and reasoning more stable by creating better aligned units between modalities.

## Cross-Paper Pattern

The common pattern is representational correction. DECS corrects token-level reward attribution. Mamba theory identifies the estimator represented by convolutional sequence structure. Neon corrects self-training by reversing the collapse direction. LST corrects speech-text imbalance through latent patching. Vid-LLM corrects 2D-to-3D reasoning gaps through geometric adapters. The broader theme is that capability often depends on finding the right level of abstraction for the signal.

## Subthemes to Track

- Decoupled rewards for overthinking reduction.
- Mamba ICL as Laplacian smoothing.
- Negative extrapolation from synthetic self-training.
- Latent speech patching for multimodal scaling.
- Video-based 3D MLLMs with geometric priors.

## Confidence and Source Depth

These notes are based on abstracts and local metadata. Formal details, validation protocols, and benchmark settings should be upgraded when PDFs are available.
