# ICML 2026 Spotlight Batch 067 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 331-335:

- MACKO: Sparse matrix-vector multiplication for low sparsity
- Conservation Laws for Modern Neural Architectures
- Fast Spectrally Sparse Signal Reconstruction via Jacobi-Preconditioned Gradient Descent
- Monitoring Monitorability
- How much can language models memorize?

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 330.

## Emerging Pattern 1: Efficiency Depends on the Real Bottleneck

MACKO-SpMV makes low unstructured sparsity useful by targeting memory bandwidth and sparse-format overhead, not just parameter count. This echoes FlashOptim, ReQAT, FlashSinkhorn, and Incremental BPE: practical efficiency appears when the implementation bottleneck is named precisely.

## Emerging Pattern 2: Modern Models Need Modern Dynamics Theory

Conservation Laws for Modern Neural Architectures extends gradient-flow invariant analysis to GELU/SiLU/SwiGLU, attention with positional encodings, and MoE. Jacobi Spectral Reconstruction similarly improves optimization by changing the geometry of updates.

Both papers track what optimization preserves or conditions, not just what it minimizes.

## Emerging Pattern 3: Oversight Is a Measurable Capability

Monitoring Monitorability turns process visibility into an evaluation target. CoT access, longer reasoning, monitor test-time compute, and follow-up questions all change how monitorable a system is.

This connects tightly to NAD, Agent0-VL, BrokenMath, and CausalGame: reliable systems need checkable reasoning channels.

## Emerging Pattern 4: Privacy Is About Information Capacity, Not Just Examples

The memorization paper estimates GPT-style capacity at about 3.6 bits per parameter after separating unintended memorization from generalization. This gives privacy and membership-inference discussions a quantitative capacity model.

It also complicates simple intuitions: as data grows and capacity fills, unintended memorization can decrease because models generalize.

## Emerging Pattern 5: Geometry Resolves Ambiguity

Jacobi Spectral Reconstruction uses a generator from factor iterates to matrix space to avoid complex-symmetric factorization ambiguity. This mirrors gauge-aware and low-rank papers where the right quotient or representation makes analysis possible.

## Cross-Batch Links

- MACKO-SpMV connects to FlashOptim, ReQAT, WBMM, FlashSinkhorn, and practical inference kernels.
- Modern Conservation Laws connects to Context-Parameter Equivalence, Diffract, Neural Ricci Flow, and OENN/CENN through dynamics and invariants.
- Jacobi Spectral Reconstruction connects to Lottery Prior, Manifold Perturbations, PRISM, and gauge/factorization geometry.
- Monitoring Monitorability connects to NAD, Agent0-VL, BrokenMath, CausalGame, TG-RAG, and tau2-bench.
- LM Memorization Capacity connects to PRISM, Rashomon Trust, Bayesian Truthful Valuation, and data privacy/governance work.

## Deep Theme Update

Batch 067 is about measuring hidden constraints: sparse inference is constrained by bandwidth, gradient flow by invariants, signal reconstruction by conditioning and factor ambiguity, oversight by monitorability, and privacy by bits of memorized information per parameter.
