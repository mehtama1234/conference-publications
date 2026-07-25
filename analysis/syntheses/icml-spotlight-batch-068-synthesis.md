# ICML 2026 Spotlight Batch 068 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 336-340:

- Distribution Transformers: Fast Approximate Bayesian Inference With On-The-Fly Prior Adaptation
- Accelerating Q-learning through Efficient Value-Sharing across Actions
- UniMapping: Unified SLAM Framework for Map-Centric Embodied Perception
- SurvDiff: A Diffusion Model for Generating Synthetic Data in Survival Analysis
- Effective Model Pruning: Measuring the Redundancy of Model Components

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 335.

## Emerging Pattern 1: Expensive Inference Is Being Amortized as Learned Operators

Distribution Transformers learn prior-to-posterior mappings over GMMs, reducing approximate Bayesian inference from minutes to milliseconds while allowing prior changes. Flow Sampling similarly amortized expensive energy-defined sampling.

The pattern is to turn a repeated inference procedure into a learned distributional operator.

## Emerging Pattern 2: Reparameterization Accelerates Learning

Mean-Expansion Q-learning shares values across actions and learns lower-norm action-value representations. EMP reparameterizes pruning amount as effective sample size from score concentration. Both avoid forcing algorithms to learn or choose poorly scaled quantities directly.

## Emerging Pattern 3: Persistent World Representations Drive Embodied Perception

UniMapping builds neural-descriptor SLAM maps that improve downstream detection and segmentation by accumulating multi-view context. This extends Holi-Spatial, SceneSmith, and DLMR: embodied AI needs durable spatial memory, not just per-frame perception.

## Emerging Pattern 4: Synthetic Data Must Preserve Domain Mechanisms

SurvDiff generates survival data by modeling event times and right-censoring jointly. This mirrors FLIP2, Holi-Spatial, and CausalGame: datasets are useful when they preserve the mechanism that defines downstream evaluation.

## Emerging Pattern 5: Compression Needs Adaptive Redundancy Measures

EMP derives sparsity from the score distribution rather than a fixed target. This sits between pruning criteria and sparse kernels: MACKO makes unstructured sparsity fast, while EMP asks how much sparsity the model can justify.

## Cross-Batch Links

- Distribution Transformer connects to BFTS, ROCP, TRECA, Distributional IRL, and Flow Sampling through uncertainty/inference amortization.
- Mean-Expansion Q-Learning connects to PAVE, T2PO, R2VPO, and value-field RL stabilization.
- UniMapping connects to Holi-Spatial, SceneSmith, RelaxFlow, DLMR, and robotics spatial memory.
- SurvDiff connects to TRECA, ROCP, medical synthetic data, and domain-constrained generation.
- EMP connects to MACKO-SpMV, ReQAT, FlashOptim, FeatJND, Brain Encoding Scale, and Diffract.

## Deep Theme Update

Batch 068 is about making hidden structure operational: priors become inputs to a posterior transformer, Q-values share state-level mass, SLAM maps become reusable neural memory, survival generators preserve censoring mechanisms, and pruning thresholds come from measured redundancy.
