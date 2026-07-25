# ICLR 2026 Oral Batch 007 Synthesis

## Papers

- Compactness and Consistency: A Conjoint Framework for Deep Graph Clustering
- How Do Transformers Learn to Associate Tokens: Gradient Leading Terms Bring Mechanistic Interpretability
- The Coverage Principle: How Pre-Training Enables Post-Training
- Half-order Fine-Tuning for Diffusion Model: A Recursive Likelihood Ratio Optimizer
- Fast Escape, Slow Convergence: Learning Dynamics of Phase Retrieval under Power-Law Data

## Source Depth

All five notes are abstract/metadata-only in the current local workspace. OpenReview remains the preferred source, and arXiv fallback should be retried for this ICLR oral range when access and rate limits clear.

## Shared Thesis

This batch is about finding the right latent quantity that explains why training works: compact graph embeddings for clustering, leading gradient terms for token associations, coverage for post-training success, half-order likelihood-ratio gradients for diffusion alignment, and spectral decay for anisotropic phase-retrieval scaling.

The common pattern is explanatory compression. Each paper replaces a complex training phenomenon with a more precise intermediate object: low-rank compact embeddings, basis functions from corpus statistics, probability mass on good responses, unbiased recursive estimators, or spectral-tail dynamics.

## Subthemes

### Compact graph representation

CoCo treats graph clustering as a local/global view alignment and denoising problem. Compactness removes redundancy while consistency transfers semantics between graph perspectives.

### Training dynamics as mechanism

The transformer association paper derives closed-form early-weight expressions from gradient leading terms. It connects corpus statistics to transformer mechanisms through bigram, token-interchangeability, and context bases.

### Coverage as pretraining value

The coverage principle argues that cross entropy is not the right downstream predictor. What post-training and Best-of-N need is support over high-quality responses.

### Recursive diffusion fine-tuning

RLR reframes diffusion model fine-tuning around an estimator matched to recursive generation. The key tension is unbiasedness and variance, not just reward choice.

### Spectral scaling dynamics

The phase-retrieval paper shows anisotropic power-law data induces fast escape, slow convergence, and spectral-tail learning. Learning curves reflect spectrum, not just sample count.

## Cross-Batch Connections

CoCo connects to MV-FGAD, LAMP, and ICML graph representation papers through compact and consistent graph embeddings.

Transformer association dynamics connect to transformer circuits, Rational Transductors, accessible sequence bounds, and DAVE through mechanistic interpretability grounded in architecture.

Coverage connects to PonderLM-2, OpenThoughts, Ctrl-R, ASAG, and reasoning-dimensionality work because it explains when downstream reasoning improvement can exploit pretrained support.

RLR connects to RealUID, DFM theory, DivIn, Reverse Flow Matching, and AGSM through diffusion/flow alignment and optimization.

Phase-retrieval dynamics connect to Gaussian single-index learning, alignment-sensitive spectral algorithms, and scaling-law papers through spectral structure as the driver of rates.

## Emerging Pattern

The broader pattern is that learning curves and downstream success are better explained by specific hidden structures than by generic loss: compactness, gradients, coverage, estimator variance, and spectrum.
