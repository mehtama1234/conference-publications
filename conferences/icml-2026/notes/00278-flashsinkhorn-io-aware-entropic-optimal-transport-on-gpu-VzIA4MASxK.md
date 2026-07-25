# FlashSinkhorn: IO-Aware Entropic Optimal Transport on GPU

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: VzIA4MASxK
- Authors: Felix X.-F. Ye; Xingjie Li; An Yu; Ming-Ching Chang; LINSONG CHU; Davis Wertheimer
- Primary area: general_machine_learning->scalable_algorithms
- Keywords: Optimal Transport;Sinkhorn Algorithm;Memory-Efficient;GPU Acceleration;Scalable Machine Learning
- Source URL: https://openreview.net/forum?id=VzIA4MASxK
- PDF URL: https://openreview.net/pdf?id=VzIA4MASxK

## Abstract

Entropic optimal transport (EOT) via Sinkhorn iterations is widely used in modern machine learning, yet GPU solvers remain inefficient at scale. Tensorized implementations suffer quadratic HBM traffic from dense $n\times m$ interactions, while existing online backends avoid storing dense matrices but still rely on generic tiled map-reduce reduction kernels with limited fusion. We present **FlashSinkhorn**, an IO-aware EOT solver for squared Euclidean cost that rewrites stabilized log-domain Sinkhorn updates as row-wise LogSumExp reductions of biased dot-product scores, the same normalization as transformer attention. This enables FlashAttention-style fusion and tiling: fused Triton kernels stream tiles through on-chip SRAM and update dual potentials in a single pass, substantially reducing HBM IO per iteration while retaining linear-memory operations. We further provide streaming kernels for transport application, enabling scalable first- and second-order optimization. On A100 GPUs, FlashSinkhorn achieves up to $32\times$ forward-pass and $161\times$ end-to-end speedups over state-of-the-art online baselines on point-cloud OT, improves scalability on OT-based downstream tasks. For reproducibility, we release an open-source implementation at https://github.com/ot-triton-lab/flash-sinkhorn.

## One-Sentence Claim

FlashSinkhorn rewrites stabilized Sinkhorn updates as attention-like tiled LogSumExp reductions, giving entropic optimal transport FlashAttention-style GPU IO efficiency.

## Problem

Entropic optimal transport is widely used, but large-scale GPU solvers are bottlenecked by memory traffic. Dense tensorized implementations materialize or stream quadratic n by m interactions through high-bandwidth memory. Existing online backends avoid dense storage but still use generic tiled reductions with limited fusion.

The paper asks how to make Sinkhorn iterations IO-aware in the same way FlashAttention made attention practical at scale.

## Core Contribution

The paper introduces FlashSinkhorn, an IO-aware EOT solver for squared Euclidean cost. It rewrites stabilized log-domain Sinkhorn updates as row-wise LogSumExp reductions of biased dot-product scores, matching the normalization structure of transformer attention.

This enables fused Triton kernels that stream tiles through on-chip SRAM, update dual potentials in a single pass, and keep memory use linear. It also provides streaming kernels for applying transport plans in first- and second-order optimization.

## Method

The method maps EOT computation onto the same computational pattern as attention: tiled dot-product-like scores plus row-wise LogSumExp normalization. By fusing operations and avoiding dense matrix materialization, kernels reduce HBM traffic per Sinkhorn iteration.

The implementation uses Triton and FlashAttention-style tiling to keep working data in SRAM while streaming through point-cloud interactions.

## Experiments and Evidence

Evidence reported in the abstract:

- A100 GPU benchmarks.
- Up to 32x forward-pass speedup over state-of-the-art online baselines on point-cloud OT.
- Up to 161x end-to-end speedup.
- Improved scalability on OT-based downstream tasks.
- Open-source implementation release.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: problem sizes, numerical stability, backward pass, supported costs beyond squared Euclidean, and downstream task list.

## Limits and Failure Modes

- The abstract focuses on squared Euclidean cost; arbitrary costs may not map as cleanly to biased dot products.
- GPU-specific speedups may not translate to CPU or edge hardware.
- Entropic regularization introduces approximation bias relative to unregularized OT.
- Numerical stabilization details are critical for large costs or small regularization.

## Deep Themes

**Algorithmic progress can come from IO reformulation.** FlashSinkhorn changes the memory movement pattern more than the mathematical objective.

**Attention kernels are becoming a general reduction template.** The LogSumExp structure makes OT compatible with FlashAttention-style fusion.

**Scalability unlocks downstream methods.** Faster OT changes which optimization and geometry methods are practical.

## Subthemes

- IO-aware optimal transport.
- Sinkhorn as attention-like normalization.
- Triton fused kernels.
- Linear-memory transport application.
- GPU-first scientific/ML primitives.

## Connections to Other Papers

Connects to WBMM, WeDLM, and other efficiency papers that recast expensive operators into hardware-friendly primitives. It also links to SoftJAX/SoftTorch and representation-geometry work because optimal transport often appears as a differentiable geometric component.

## Notes for Cross-Paper Synthesis

FlashSinkhorn strengthens the hardware-aligned algorithm theme: once a primitive is expressed in the right computational grammar, entire families of methods become viable at larger scale.
