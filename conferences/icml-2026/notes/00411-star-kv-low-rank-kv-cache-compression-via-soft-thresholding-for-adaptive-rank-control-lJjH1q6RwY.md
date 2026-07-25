# STAR-KV: Low-Rank KV Cache Compression via Soft Thresholding for Adaptive Rank Control

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: lJjH1q6RwY
- Authors: Priyansh Bhatnagar; Ashkan Moradifirouzabadi; Se-Hyun Yang; SeungJae Lee; Jungwook Choi; Mingu Kang
- Primary area: deep_learning->large_language_models
- Keywords: Large Language Models;KV Cache Compression;Low-rank Decomposition;Quantization
- Source URL: https://openreview.net/forum?id=lJjH1q6RwY
- PDF URL: https://openreview.net/pdf?id=lJjH1q6RwY

## Abstract

Low-rank projection has emerged as a promising approach for compressing the KV cache by exploiting hidden-dimension redundancy. However, prior methods rely on fixed or heuristic rank selection and struggle to achieve aggressive compression with minimal accuracy degradation. We propose STAR-KV, an adaptive low-rank KV cache compression framework with fine-grained rank control. STAR-KV encompasses 1) a differentiable thresholding mechanism that enables optimal rank selection at both attention-head and block levels, 2) a hybrid decomposition strategy that applies different low-rank factorizations according to the sensitivity of key and value projections, and 3) a low-rank--aware mixed precision quantization  that leverages data statistics for near lossless low-bit quantization. Evaluated across multiple LLMs and benchmarks, STAR-KV achieves up to 75\%  KV cache compression and up to 20$\times$ overall KV cache reduction when combined with quantization. Enabled by custom Triton-based GPU kernels, STAR-KV delivers up to 6.9$\times$ speedup for the attention module and 3.1$\times$ end-to-end generation throughput. Our code is publicly available at: https://github.com/PriyanshBhatnagar/STAR-KV.

## One-Sentence Claim

STAR-KV compresses KV caches with adaptive low-rank thresholding, hybrid key/value decompositions, and low-rank-aware quantization, yielding large memory and throughput gains.

## Problem

KV cache memory is a major bottleneck for long-context and high-throughput LLM inference. Low-rank projection can exploit hidden-dimension redundancy, but prior methods use fixed or heuristic ranks and struggle to compress aggressively without harming accuracy.

The paper asks how to choose compression rank adaptively at fine granularity while also making the compressed representation efficient on GPU.

## Core Contribution

STAR-KV is an adaptive KV cache compression framework with differentiable soft-thresholding for rank selection at attention-head and block levels. It adds a hybrid decomposition strategy that treats key and value projections according to their sensitivity, plus mixed-precision quantization aware of low-rank statistics.

Custom Triton kernels make the method practical for attention and end-to-end generation throughput.

## Method

The method applies low-rank decompositions to KV cache tensors and uses differentiable thresholding to decide effective rank. Rather than one fixed rank, it adapts rank to heads and blocks.

It then combines low-rank compression with mixed-precision quantization, using data statistics to preserve accuracy under low-bit representations.

## Experiments and Evidence

Evidence reported in the abstract:

- Up to 75% KV cache compression.
- Up to 20x overall KV cache reduction when combined with quantization.
- Up to 6.9x speedup for the attention module.
- Up to 3.1x end-to-end generation throughput.
- Evaluated across multiple LLMs and benchmarks.
- Custom Triton-based GPU kernels.
- Code released at the listed GitHub URL.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: model sizes, context lengths, quality metrics, and kernel assumptions.

## Limits and Failure Modes

- Low-rank structure may vary across domains, prompts, and long-context regimes.
- Adaptive rank control adds complexity and may need calibration.
- Quantization errors can interact with low-rank approximation in hard-to-predict ways.
- Kernel speedups may depend on GPU architecture and batch/context shapes.

## Deep Themes

**Memory compression is inference capability.** KV cache reductions directly expand context, batch size, and serving throughput.

**Compression should be adaptive.** Different heads, blocks, keys, and values have different sensitivity.

**Algorithmic compression needs kernel support.** Practical gains require custom GPU implementation, not just a mathematical factorization.

## Subthemes

- KV cache compression.
- Adaptive low-rank thresholding.
- Head/block rank control.
- Low-rank-aware quantization.
- Triton attention kernels.

## Connections to Other Papers

Connects to CONTINUUM, ThunderAgent, WaterSIC, QAT Scaling, MACKO-SpMV, and ReQAT. It fits the efficiency-as-capability cluster where memory, precision, and kernels shape feasible inference.

## Notes for Cross-Paper Synthesis

STAR-KV adds another systems compression layer: efficient LLM deployment increasingly requires dynamic representations of intermediate state, not only smaller model weights.
