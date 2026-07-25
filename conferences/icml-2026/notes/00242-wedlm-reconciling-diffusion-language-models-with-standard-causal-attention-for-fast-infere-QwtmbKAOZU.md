# WeDLM: Reconciling Diffusion Language Models with Standard Causal Attention for Fast Inference

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: QwtmbKAOZU
- Authors: Aiwei Liu; Minghua He; Shaoxun Zeng; Sijun Zhang; Linhao Zhang; Chuhan Wu; Wei Jia; Yuan Liu; Zhou Xiao; Jie Zhou
- Primary area: deep_learning->large_language_models
- Keywords: Diffusion Language Models;Large Language Models;Parallel Decoding;Inference Acceleration
- Source URL: https://openreview.net/forum?id=QwtmbKAOZU
- PDF URL: https://openreview.net/pdf?id=QwtmbKAOZU

## Abstract

Autoregressive (AR) generation is the standard decoding paradigm for Large Language Models (LLMs), but its token-by-token nature limits parallelism at inference time. Diffusion Language Models (DLLMs) offer parallel decoding by recovering multiple masked tokens per step; however, in practice they often fail to translate this parallelism into speed gains over optimized AR engines (e.g., vLLM). A key reason is that many DLLMs rely on bidirectional attention, which breaks standard prefix KV caching.
We propose WeDLM, a diffusion decoding framework built entirely on standard causal attention to make parallel generation prefix-cache friendly. The core idea is to let each masked position condition on all observed tokens while keeping a causal mask, achieved by Topological Reordering that moves observed tokens to the physical prefix while preserving their logical positions. Building on this, we introduce a streaming decoding procedure that continuously commits confident tokens into a growing left-to-right prefix, avoiding the stop-and-wait behavior common in block diffusion methods. Experiments show that WeDLM preserves the quality of strong AR backbones while delivering substantial speedups, approaching 3× on challenging reasoning benchmarks and up to 10× in low-entropy generation regimes; critically, our comparisons are against AR baselines served by vLLM under matched deployment settings.

## One-Sentence Claim

WeDLM makes diffusion language model parallel decoding compatible with causal attention and prefix KV caching, enabling substantial speedups under matched vLLM deployment settings.

## Problem

Diffusion language models can decode multiple masked tokens in parallel, but bidirectional attention often breaks prefix caching and prevents practical speed gains over optimized autoregressive serving.

## Core Contribution

The paper introduces causal-attention diffusion decoding through Topological Reordering and streaming commitment of confident tokens into a growing left-to-right prefix.

## Method

Topological Reordering moves observed tokens into the physical prefix while preserving logical positions, letting masked positions condition on observed tokens under a causal mask. Streaming decoding continuously commits high-confidence tokens to avoid block-diffusion stop-and-wait behavior.

## Experiments and Evidence

The abstract reports preserved quality of strong AR backbones, roughly 3x speedups on challenging reasoning benchmarks, and up to 10x speedups in low-entropy regimes versus vLLM-served AR baselines under matched deployment settings.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: decoding schedules, quality metrics, low-entropy task definition, cache implementation, model sizes, and failure cases where token confidence is miscalibrated.

## Deep Themes

- Inference algorithms must be compatible with serving infrastructure.
- Parallel decoding needs cache-friendly causal structure to realize speedups.
- Logical token order and physical cache order can be decoupled.

## Subthemes

- Diffusion language models.
- Causal attention.
- Prefix KV caching.
- Parallel decoding.
- Streaming token commitment.
- vLLM comparison.

## Connections to Other Papers

Connects to ECHO, Top-W, and LatentLM through inference-time generation control and to systems papers that judge speed under realistic deployment baselines.

## Notes for Cross-Paper Synthesis

WeDLM adds a practical decoding theme: theoretical parallelism matters only when the algorithm respects the memory/cache abstractions of production serving.
