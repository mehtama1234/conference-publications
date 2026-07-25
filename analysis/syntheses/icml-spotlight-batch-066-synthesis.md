# ICML 2026 Spotlight Batch 066 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 326-330:

- Chebyshev Policies and the Mountain Car Problem: Reinforcement Learning for Low-Dimensional Control Tasks
- Prototype-guided Bilateral Alignment Multimodal Federated Learning
- GFD-EMVC: Evolutionary Multi-View Classification with Label Noise via Gradient and Feature Dual-Perception
- A Constrained Optimization Perspective of Unrolled Transformers
- Equivalence of Context and Parameter Updates in Modern Transformer Blocks

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 325.

## Emerging Pattern 1: Structured Small Models Can Beat Generic Neural Baselines

Chebyshev Policies analytically solves Mountain Car and shows a compact polynomial policy class can outperform neural policies with far fewer parameters. This fits a recurring counter-scaling pattern from Lottery Prior, Brain Encoding Scale, and BFTS.

The message is domain-specific: when the task is low-dimensional and smooth, the right basis can matter more than generic capacity.

## Emerging Pattern 2: Collaboration Requires Alignment Across Spaces and Incentives

MFedPBA aligns heterogeneous multimodal federated clients at feature and decision levels. This extends FedPissa's low-rank client-conflict theme from parameter updates to feature spaces and logit prototypes.

The broader federated-learning pattern is that aggregation is not averaging; it is conflict-aware alignment.

## Emerging Pattern 3: Data Noise Corrupts the Optimization Landscape

GFD-EMVC frames label noise as fitness evaluation bias in evolutionary multi-view classification. The repair combines gradient-space detection and feature-prototype calibration.

This connects to C2R and MTS Difficulty: data quality matters because it changes the gradients, margins, or fitness scores that steer learning.

## Emerging Pattern 4: Internal Trajectories Can Be Constrained to Improve Robustness

Constrained Transformers enforce layerwise descent constraints with primal-dual training so intermediate representations monotonically reduce loss in expectation. This aligns with FlowOptimizer, PAVE, and NAD: the process path itself is a control target.

## Emerging Pattern 5: Context and Parameters Are Converging

Context-Parameter Equivalence shows modern Transformer context effects can be represented as implicit rank-1 MLP patches and normalization-scale patches under controllability conditions. This gives theory behind why prompts, adapters, and low-rank updates can appear functionally related.

## Cross-Batch Links

- Chebyshev Policies connects to PAVE, TimeRewarder, BFTS, Lottery Prior, and compact structured modeling papers.
- MFedPBA connects to FedPissa, PRISM, IDCD, DIGL, and optimal-transport alignment methods.
- GFD-EMVC connects to C2R, MTS Difficulty, HOBIT, DISCO, and noisy-label robust curation.
- Constrained Transformers connects to FlowOptimizer, NAD, ReQAT, PAVE, and process-shaped robustness.
- Context-Parameter Equivalence connects to Diffract, FedPissa, PRISM, DiSC, Neuron-Basis Circuits, and in-context learning theory.

## Deep Theme Update

Batch 066 is about replacing generic assumptions with structural constraints: polynomial policies for smooth control, bilateral alignment for federated multimodality, gradient/prototype purification for noisy labels, layerwise descent for robust Transformers, and controllability-based equivalence between prompts and parameter updates.
