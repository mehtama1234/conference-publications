# ICML 2026 Spotlight Batch 098 Synthesis

Papers covered: 00486-00490.

## Batch Thesis

This batch is about the limits and diagnostics of compression, optimization, and representation capacity. Expressive lottery tickets ask when sparse graph subnetworks retain relational WL power; Adam theory identifies degenerate objectives where adaptive moments give linear convergence; embedding-dimension lower bounds show underdimensioned representations can collapse to trivial accuracy; local redundancy measures plasticity through information-theoretic synthetic memorization; and KDE-based kernel algorithms accelerate matrix computations by changing the access model.

The common pattern is that efficiency and adaptivity are possible only when the hidden structure is preserved: graph expressivity, degenerate curvature, intrinsic dimension, local information capacity, or aggregate kernel mass.

## Cross-Paper Themes

### 1. Compression Has Formal Failure Modes

The lottery-ticket paper gives a positive story: sparse RGNN subnetworks can preserve relational expressivity. The embedding-collapse paper gives the negative counterpart: compressing dimension below the true dimension can destroy triplet accuracy.

Together they sharpen the efficiency theme. Sparsity and dimensionality reduction are not inherently good or bad; their value depends on which structure survives the bottleneck.

### 2. Optimizers Have Objective-Specific Advantages

Adam's advantage on highly degenerate polynomials is not a universal magic property. It emerges from second-moment/gradient decoupling that amplifies effective learning rate in a specific local geometry.

This links to edge-of-stability and NorMuon work: optimizer behavior is best understood through the geometry and degeneracy of the problem it is applied to.

### 3. Future Learnability Needs Its Own Metrics

Local redundancy focuses on plasticity: a model's capacity to adapt to new tasks even when validation loss is flat. This complements SDFT and post-training barrier papers, which study how models acquire new capabilities without forgetting.

The broad lesson is that present performance is not enough. We need diagnostics for what a checkpoint can still learn.

### 4. Access Models Change Algorithmic Possibility

The kernel-algebra paper shows that KDE query access can beat entrywise kernel-matrix access for multiple linear-algebra tasks. This mirrors DHSA, FFCC, and STAR-KV in a theoretical setting: the computational interface determines the feasible algorithm.

## Deep Subthemes

### Relational Lottery Tickets

Sparse graph subnetworks can preserve 1-RWL expressivity under sufficient parameterization. Temporal and cross-graph architectures inherit guarantees via RGNN reformulations.

### Degenerate-Objective Adam Dynamics

Adam can converge linearly where GD and momentum are sublinear, but only inside a stable hyperparameter regime. Spikes and SignGD-like oscillation are adjacent failure regimes.

### Dimensionality Collapse

Embedding dimension is a correctness parameter. If d is too small relative to the true dimension D, almost half of triplet constraints may be violated.

### Plasticity From Synthetic Memorization

Synthetic memorization gradient norms provide a computable proxy for local information redundancy. This predicts downstream adaptability better than common structural metrics.

### KDE as Linear-Algebra Access Primitive

Kernel density queries expose aggregate kernel structure, enabling faster matrix-vector, matrix-matrix, norm, and sum computations.

## Common Pattern

The batch's shared message is that efficient learning is constrained by preserved information. Whether pruning graph models, choosing embedding dimension, selecting checkpoints, tuning Adam, or querying kernels, the critical question is what information the compressed or accelerated process still carries.
