# Long-Context Modeling with Dynamic Hierarchical Sparse Attention for Memory-Constrained LLM Inference

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: o3gN27ITWV
- Authors: Siheng Xiong; Joe Zou; Faramarz Fekri; Yae Jee Cho
- Primary area: deep_learning->large_language_models
- Keywords: Long-context language models;Sparse attention;Dynamic sparsity;On-device inference;Efficient LLMs
- Source URL: https://openreview.net/forum?id=o3gN27ITWV
- PDF URL: https://openreview.net/pdf?id=o3gN27ITWV

## Abstract

The quadratic cost of attention limits the scalability of long-context LLMs, especially under limited hardware memory budgets. While attention is often sparse, existing static sparse methods cannot adapt to task- or input-dependent variations, and recent dynamic approaches rely on predefined templates or heuristics that may sacrifice generality. We propose Dynamic Hierarchical Sparse Attention (DHSA), a data-driven framework that predicts attention sparsity online while keeping the LLM backbone frozen. DHSA performs hierarchical routing by estimating importance at the chunk level and propagating it to token-level interactions, preserving causally important dependencies while enabling efficient sparsification. Across Needle-in-a-Haystack test, LongBench and RULER, DHSA maintains near-dense accuracy in highly sparse regimes, achieving 12--20% relative accuracy gains over Block Sparse Attention at comparable prefill cost. With a memory-efficient tiled backend, DHSA delivers up to $10\times$ prefill speedup at 128K context length. On LLaMA-3.1-8B (4-bit), DHSA scales to 100K context on a single 24GB GPU, where dense attention fails. We provide complementary GPU and CPU backends, enabling DHSA to run across diverse hardware environments and multiple open-weight model families. These results demonstrate DHSA as an efficient and adaptable solution for memory-constrained long-context LLM inference. Code is available at: https://github.com/xiongsiheng/DHSA.

## One-Sentence Claim

Dynamic Hierarchical Sparse Attention predicts task-dependent sparse attention online, preserving long-context accuracy while enabling memory-constrained LLM inference up to 100K context on a single 24GB GPU.

## Problem

Dense attention scales quadratically with context length, making long-context inference expensive and often impossible under constrained memory. Static sparse attention reduces cost but cannot adapt to input-specific dependencies, while heuristic dynamic approaches may hard-code templates that fail across tasks.

The paper targets a practical deployment problem: long-context inference should remain accurate, adaptive, and runnable on limited hardware rather than requiring large multi-GPU systems.

## Core Contribution

DHSA contributes a data-driven sparse-attention framework that keeps the LLM backbone frozen and predicts sparsity online. It uses hierarchical routing from chunk-level importance to token-level interactions, aiming to preserve causally important dependencies while removing unnecessary attention computation.

The broader contribution is to connect algorithmic sparsity with systems backends. The method includes memory-efficient tiled execution and both GPU and CPU backends, making sparsity a deployable inference primitive rather than only a modeling idea.

## Method

DHSA estimates importance first at the chunk level, then propagates selected structure to token-level attention interactions. This hierarchy makes routing cheaper than scoring all token pairs directly and lets sparsity adapt to the current input and task.

The LLM backbone remains frozen, which makes the method more compatible with existing open-weight models. A tiled backend manages memory during long-context prefill, and complementary hardware backends broaden deployment coverage.

## Experiments and Evidence

The abstract reports evaluation on Needle-in-a-Haystack, LongBench, and RULER. DHSA maintains near-dense accuracy in highly sparse regimes, improves relative accuracy by 12-20 percent over Block Sparse Attention at comparable prefill cost, and delivers up to 10x prefill speedup at 128K context.

On LLaMA-3.1-8B in 4-bit precision, DHSA scales to 100K context on a single 24GB GPU where dense attention fails. Full-paper reading should verify exact sparsity levels, latency/memory measurement setup, and whether downstream generation quality remains stable beyond retrieval-style tests.

## Limits and Failure Modes

Sparse attention can fail when seemingly unimportant tokens become important later, especially in tasks with diffuse evidence or adversarially placed dependencies. Online routing introduces its own prediction errors, and chunk-level summaries may miss fine-grained token interactions.

The reported speedups depend on backend implementation, hardware, model family, quantization, and context distribution. The method's generality across architectures and real workloads needs careful full-text inspection.

## Deep Themes

- Adaptive inference sparsity: efficiency comes from predicting which dependencies matter for each input.
- Frozen-backbone augmentation: long-context capability can be extended without retraining the base LLM.
- Hardware-aware algorithm design: sparse attention only matters operationally when paired with memory-efficient kernels/backends.
- Hierarchical routing as compression: chunk-level structure reduces token-level search.

## Subthemes

- Long-context benchmarks increasingly test both recall and systems feasibility.
- Static sparsity is too rigid for heterogeneous tasks.
- Prefill cost is a central bottleneck for long-context deployments.
- Single-GPU long-context inference is an important accessibility target.

## Connections to Other Papers

DHSA connects to STAR-KV, NorMuon, and vAttention-style sparse attention work through efficiency as a capability enabler. Compared with STAR-KV's KV-cache compression, DHSA attacks the prefill attention cost through dynamic sparsity.

It also relates to LongCoT and other long-horizon reasoning benchmarks: long-context infrastructure is necessary but not sufficient for reliable extended reasoning, and efficiency papers define what contexts can be processed at all.

## Notes for Cross-Paper Synthesis

DHSA is a clear example of 2026 efficiency work becoming deployment-specific. The subtheme is not generic compression but adaptive, hardware-aware sparsity that changes what long-context applications are feasible on commodity devices.
