# ICML 2026 Spotlight Batch 060 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 296-300:

- TimeRewarder: Learning Dense Reward from Passive Videos via Frame-wise Temporal Distance
- Mind Your Margin and Boundary: Are Your Distilled Datasets Truly Robust?
- BrokenMath: A Benchmark for Sycophancy in Theorem Proving with LLMs
- High-accuracy and dimension-free sampling with diffusions
- From Distribution to Geometry: Stable Graph Generalization via Invariant Barycenters

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 295.

## Emerging Pattern 1: Ordered Observations Can Supervise Control

TimeRewarder learns dense rewards from temporal distances in passive videos. This converts video order into a progress signal that can guide sparse-reward robotic RL.

This extends the trajectory-supervision theme from Latent Action Supervision, Scientific Annotation BC, TerminalTraj, and continual VLA work: the sequence itself carries reusable process information.

## Emerging Pattern 2: Robust Data Compression Must Preserve Boundary Geometry

C2R shows robust dataset distillation should focus on small-margin adversaries and class-boundary separation. A distilled dataset that preserves clean prototypes but misses hard boundary cases will train brittle models.

This ties data curation to robustness: small data must encode the decision surface, not just the class means.

## Emerging Pattern 3: Reasoning Benchmarks Are Targeting Agreement Failure

BrokenMath measures theorem-proving sycophancy: whether models produce proofs for false statements. It complements WZ-LLM's formal verification focus and CausalGame's causal-process evaluation.

The benchmark trend is clear: reasoning systems must reject bad premises, not merely produce fluent chains of thought.

## Emerging Pattern 4: Diffusion Efficiency Has a Numerical-Analysis Track

The dimension-free diffusion sampler uses low-degree approximation and collocation to obtain polylogarithmic accuracy dependence. This is distinct from hardware acceleration or RL post-training; it improves the mathematical solver behind sampling.

Together with FlashSinkhorn, SRMC, and Local Diffusion Composition, it shows numerical structure is a major lever for generative modeling.

## Emerging Pattern 5: Invariance Is Becoming Geometric

DIGL formulates graph OOD invariance as an OT barycenter: a shared distributional prototype distorted by environments. This turns an abstract invariance principle into a concrete geometric object.

This connects directly to language-statistic manifolds, IDCD's Wasserstein aggregation, and manifold-aware generative perturbations.

## Cross-Batch Links

- TimeRewarder connects to Latent Action Supervision, Continual VLA Forgetting, SceneSmith, and Scientific Annotation BC through trajectory-derived supervision.
- C2R connects to MTS Difficulty, HOBIT, Consistent Adversarial Attacks, FeatJND, and S&D through hard-example and margin-aware robustness.
- BrokenMath connects to WZ-LLM, CausalGame, HypoSpace, and TG-RAG through adversarial reasoning evaluation.
- Dimension-Free Diffusion Sampling connects to SRMC, UDM-GRPO, Local Diffusion Composition, and Flowers through sampler/differential-equation structure.
- DIGL connects to FlashSinkhorn, IDCD, HAMC, PSAHS, ENGNN, and DISCO through OT, graph, and invariance geometry.

## Deep Theme Update

Batch 060 emphasizes that supervision and guarantees increasingly come from structure around the data: temporal order becomes reward, robust margins define distilled examples, false theorem statements expose sycophancy, low-degree/collocation structure accelerates sampling, and OT barycenters define invariant graph prototypes.
