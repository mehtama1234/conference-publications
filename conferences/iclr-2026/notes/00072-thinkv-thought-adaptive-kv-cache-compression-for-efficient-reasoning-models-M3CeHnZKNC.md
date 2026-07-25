# ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: M3CeHnZKNC
- Authors: Akshat Ramachandran; Marina Neseem; Charbel Sakr; Rangharajan Venkatesan; Brucek Khailany; Tushar Krishna
- Primary area: generative models
- Keywords: Large Reasoning Models;KV Cache Compression;Quantization;Eviction;Sparsity;Thought-Aware Compression
- Source URL: https://openreview.net/forum?id=M3CeHnZKNC
- PDF URL: https://openreview.net/pdf?id=M3CeHnZKNC

## Abstract

The long-output context generation of large reasoning models enables extended chain of thought (CoT) but also drives rapid growth of the key–value (KV) cache, quickly overwhelming GPU memory. To address this challenge, we propose ThinKV, a thought-adaptive KV cache compression framework. ThinKV is based on the observation that attention sparsity reveals distinct thought types with varying importance within the CoT. It applies a hybrid quantization–eviction strategy, assigning token precision by thought importance and progressively evicting tokens from less critical thoughts as reasoning trajectories evolve. Furthermore, to implement ThinKV, we design a kernel that extends PagedAttention to enable efficient reuse of evicted tokens' memory slots, eliminating compaction overheads. Extensive experiments on DeepSeek-R1-Distill, GPT-OSS, and NVIDIA AceReason across mathematics and coding benchmarks show that ThinKV achieves near-lossless accuracy with less than 5% of the original KV cache, while improving performance with up to 5.8x higher inference throughput over SoTA baselines.

## One-Sentence Claim

ThinKV compresses reasoning-model KV caches by using attention sparsity to identify thought importance, combining adaptive quantization, eviction, and PagedAttention-compatible memory reuse.

## Problem

Large reasoning models produce long chain-of-thought outputs, causing KV caches to grow quickly and overwhelm GPU memory.

Naive compression risks deleting or degrading tokens that remain important for later reasoning, while uniform retention wastes memory on low-value reasoning spans.

## Core Contribution

The paper introduces ThinKV, a thought-adaptive KV cache compression framework for reasoning models.

It assigns token precision by thought importance, progressively evicts less critical thought tokens, and implements efficient memory-slot reuse with a kernel extending PagedAttention.

## Method

ThinKV uses attention sparsity patterns to infer distinct thought types and their relative importance inside the generated reasoning trajectory.

Important thought tokens are retained or represented with higher precision, while less important thoughts are quantized more aggressively or evicted over time. The runtime kernel reuses evicted memory slots to avoid expensive compaction.

## Experiments and Evidence

The abstract reports experiments on DeepSeek-R1-Distill, GPT-OSS, and NVIDIA AceReason across mathematics and coding benchmarks.

ThinKV reaches near-lossless accuracy with less than 5 percent of the original KV cache and improves inference throughput by up to 5.8x over state-of-the-art baselines.

## Limits and Failure Modes

Attention sparsity may be an imperfect proxy for thought importance. Evicting tokens from early reasoning could harm tasks where a subtle premise becomes relevant much later.

Because this note is abstract-only, details still need checking: thought taxonomy, compression schedule, quantization levels, eviction policy, PagedAttention changes, exact memory/latency accounting, and robustness across prompt styles.

## Deep Themes

- Thought-aware systems: reasoning traces are treated as structured objects with variable memory value.
- Adaptive KV compression: cache budget follows inferred importance rather than token position alone.
- Systems support for reasoning models: long CoT requires memory managers tailored to generated thought trajectories.
- Near-lossless serving optimization: practical inference gains depend on preserving benchmark accuracy under aggressive compression.

## Subthemes

- KV cache compression.
- Thought importance.
- Quantization and eviction.
- PagedAttention memory reuse.

## Connections to Other Papers

This connects to EntroKV, ASAG, p-less sampling, and HSD through adaptive test-time control.

It also relates to LongWriter-Zero and PonderLM-2 because long outputs and latent deliberation both increase pressure on inference memory.

## Notes for Cross-Paper Synthesis

ThinKV strengthens the theme that reasoning is becoming an object for systems optimization: not every thought token deserves the same memory budget.
