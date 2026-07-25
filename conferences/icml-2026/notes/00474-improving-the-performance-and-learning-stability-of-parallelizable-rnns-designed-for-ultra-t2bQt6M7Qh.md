# Improving the Performance and Learning Stability of Parallelizable RNNs Designed for Ultra-Low Power Applications

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: t2bQt6M7Qh
- Authors: Julien Brandoit; Arthur Fyon; Damien Ernst; Guillaume Drion
- Primary area: deep_learning->sequential_models_time_series
- Keywords: Recurrent Neural Networks;Bistable Memory Recurrent Unit;Persistent Memory;Parallelizable RNNs;Long-Range Dependencies;Sequence Modeling;Analog Neural Networks
- Source URL: https://openreview.net/forum?id=t2bQt6M7Qh
- PDF URL: https://openreview.net/pdf?id=t2bQt6M7Qh

## Abstract

Sequence learning is dominated by Transformers and parallelizable recurrent neural networks (RNNs) such as state-space models, yet learning long-term dependencies remains challenging, and state-of-the-art designs trade power consumption for performance. The Bistable Memory Recurrent Unit (BMRU) was introduced to enable hardware-software co-design of ultra-low power RNNs: quantized states with hysteresis provide persistent memory while mapping directly to analog primitives. However, BMRU performance lags behind parallelizable RNNs on complex sequential tasks. In this paper, we identify gradient blocking during state updates as a key limitation and propose a cumulative update formulation that restores gradient flow while preserving persistent memory, creating skip-connections through time. This leads to the Cumulative Memory Recurrent Unit (CMRU) and its relaxed variant, the $\alpha$CMRU. Experiments show that the cumulative formulation dramatically improves convergence stability and reduces initialization sensitivity. The CMRU and $\alpha$CMRU match or outperform Linear Recurrent Units (LRUs) and minimal Gated Recurrent Units (minGRUs) across diverse benchmarks at small model sizes, with particular advantages on tasks requiring discrete long-range retention, while the CMRU retains quantized states, persistent memory, and noise-resilient dynamics essential for analog implementation.

## One-Sentence Claim

CMRU restores gradient flow in ultra-low-power bistable-memory RNNs through cumulative state updates, improving stability and performance while preserving quantized persistent memory for analog implementation.

## Problem

Transformers and parallelizable recurrent models dominate sequence learning, but low-power applications need architectures that map efficiently to hardware. Bistable Memory Recurrent Units offer quantized states with hysteresis and persistent memory suitable for analog primitives, but they lag on complex sequential tasks.

The paper identifies gradient blocking during state updates as a key reason BMRUs are hard to train and underperform stronger parallelizable RNNs.

## Core Contribution

The paper proposes a cumulative update formulation that restores gradient flow while retaining persistent memory. This creates skip-connections through time and leads to the Cumulative Memory Recurrent Unit and relaxed alphaCMRU variant.

The contribution is to improve trainability without giving up the hardware-relevant properties of BMRU: quantized states, persistent memory, and noise-resilient dynamics.

## Method

Instead of updating state in a way that blocks gradients, CMRU accumulates updates over time so gradients can propagate through temporal skip connections. The alphaCMRU variant relaxes the formulation, likely trading strict quantized behavior for smoother learning.

The architecture remains parallelizable and compatible with ultra-low-power analog implementation constraints, preserving the original motivation of BMRU while improving optimization.

## Experiments and Evidence

The abstract reports dramatically improved convergence stability and reduced initialization sensitivity. CMRU and alphaCMRU match or outperform Linear Recurrent Units and minimal GRUs across diverse benchmarks at small model sizes, with advantages on tasks requiring discrete long-range retention.

Full-paper reading should verify benchmark set, power/analog assumptions, parallelization details, model-size comparisons, and whether hardware measurements or only hardware-motivated properties are reported.

## Limits and Failure Modes

Hardware suitability depends on actual analog implementations, noise characteristics, and quantization constraints. Software benchmarks may not fully predict low-power hardware behavior.

The architecture may be strongest for discrete long-range retention and smaller models, but less competitive on broad language or multimodal tasks where large Transformers dominate.

## Deep Themes

- Hardware-software co-design for sequence models: architecture is shaped by analog low-power constraints.
- Persistent memory with trainable gradients: cumulative updates reconcile retention and optimization.
- RNN revival under deployment constraints: recurrent models remain relevant where power is scarce.
- Discrete state retention: quantized memory can be an advantage for certain long-range tasks.

## Subthemes

- Gradient blocking explains BMRU instability.
- Temporal skip connections improve recurrent credit assignment.
- Initialization sensitivity is a practical training barrier.
- Noise-resilient dynamics matter for analog computation.

## Connections to Other Papers

CMRU connects to DHSA, TabSwift, STAR-KV, and MoE compression through efficient deployment, but from a hardware-architecture angle. It also relates to LLapDiff and ConFlux through sequence/time-series modeling beyond Transformers.

It fits the broader theme that efficiency constraints produce new model families, not just compressed versions of existing ones.

## Notes for Cross-Paper Synthesis

The synthesis point is that sequence-model progress is hardware-contingent. Low-power applications may favor architectures whose memory dynamics map naturally to physical primitives.
