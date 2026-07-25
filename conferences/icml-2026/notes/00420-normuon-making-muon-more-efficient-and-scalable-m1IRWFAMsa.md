# NorMuon: Making Muon more efficient and scalable

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: m1IRWFAMsa
- Authors: Zichong Li; Liming Liu; Chen Liang; Weizhu Chen; Tuo Zhao
- Primary area: deep_learning->large_language_models
- Keywords: Optimizer;Muon;Adam
- Source URL: https://openreview.net/forum?id=m1IRWFAMsa
- PDF URL: https://openreview.net/pdf?id=m1IRWFAMsa

## Abstract

The choice of optimizer significantly impacts the training efficiency and computational costs of large language models (LLMs). Recently, the Muon optimizer has demonstrated promising results by orthogonalizing parameter updates, improving optimization geometry through better conditioning.
Despite Muon’s emergence as a candidate successor to Adam, the potential for jointly leveraging their strengths—has not been systematically explored.
In this work, we bridge this gap by proposing NorMuon (Neuron-wise Normalized Muon), an optimizer that synergistically combines orthogonalization with neuron-level adaptive learning rates. Our analysis reveals that while Muon effectively reduces condition numbers, the resulting updates exhibit highly non-uniform neuron norms, causing certain neurons to dominate the optimization process. NorMuon addresses this imbalance by maintaining second-moment statistics for each neuron and applying row-wise normalization after orthogonalization, ensuring balanced parameter utilization while preserving Muon's conditioning benefits. To enable practical deployment at scale, we develop an efficient distributed implementation under the FSDP2 framework that distributes orthogonalization computations across devices.
Experiments across multiple model scales demonstrate that NorMuon consistently outperforms both AdamW and Muon, achieving a 21.74\% reduction in training steps relative to AdamW and an 11.31 percentage-point larger efficiency gain than Muon on 1.1B pretraining. Results suggest that orthogonalization and adaptive learning rates are complementary rather than competing, opening new avenues for optimizer design in large-scale deep learning.

## One-Sentence Claim

NorMuon combines Muon's update orthogonalization with neuron-wise adaptive normalization, preserving conditioning benefits while balancing per-neuron update magnitudes for scalable LLM training.

## Problem

Optimizer choice strongly affects LLM training efficiency. Muon improves optimization geometry by orthogonalizing parameter updates, but its updates can have highly non-uniform neuron norms, letting some neurons dominate.

The paper asks whether Muon's conditioning benefits can be combined with adaptive learning-rate ideas from Adam-style optimizers.

## Core Contribution

NorMuon, or Neuron-wise Normalized Muon, maintains second-moment statistics per neuron and applies row-wise normalization after orthogonalization. This balances parameter utilization while preserving Muon's conditioning advantages.

The paper also develops an efficient FSDP2 distributed implementation that distributes orthogonalization computations across devices.

## Method

NorMuon first orthogonalizes updates as in Muon, then normalizes rows using neuron-level second-moment statistics. This adds adaptivity to the orthogonalized update geometry.

The distributed implementation makes the orthogonalization step practical at scale by spreading computation across devices under FSDP2.

## Experiments and Evidence

Evidence reported in the abstract:

- Analysis showing Muon reduces condition numbers but creates non-uniform neuron update norms.
- Neuron-wise second-moment statistics and row-wise normalization.
- Efficient distributed implementation under FSDP2.
- Experiments across multiple model scales.
- Consistently outperforms AdamW and Muon.
- 21.74% reduction in training steps relative to AdamW.
- 11.31 percentage-point larger efficiency gain than Muon on 1.1B pretraining.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: model sizes, compute accounting, stability, and memory overhead.

## Limits and Failure Modes

- Orthogonalization may remain costly despite distributed implementation.
- Row-wise normalization assumptions may differ across layer types.
- Gains on 1.1B pretraining may not extrapolate linearly to much larger models.
- Optimizer comparisons require careful tuning of all baselines.

## Deep Themes

**Optimizer geometry and adaptivity are complementary.** Orthogonal updates and neuron-wise scaling solve different problems.

**Training efficiency is a systems-algorithm co-design problem.** The optimizer needs distributed implementation to matter at scale.

**Balanced neuron utilization is a training objective.** Update norm imbalance can waste capacity or destabilize optimization.

## Subthemes

- Muon optimizer.
- Neuron-wise normalization.
- Orthogonalized updates.
- FSDP2 distributed optimization.
- LLM pretraining efficiency.

## Connections to Other Papers

Connects to POET-X, OPUS, QAT Scaling, WaterSIC, and training-efficiency papers. It complements OPUS: one selects better data updates, the other reshapes optimizer updates.

## Notes for Cross-Paper Synthesis

NorMuon adds another optimizer-level theme: scalable LLM training is increasingly about controlling update geometry, not just choosing data or model architecture.
