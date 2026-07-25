# ReQAT: Achieving Full-Precision Reasoning Accuracy with 4-bit Floating-Point Quantization-Aware Training

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: aKY52fnzgc
- Authors: Janghwan Lee; Sihwa Lee; Jinseok Kim; Yongjik Kim; Jieun Lim; Jinwook Oh; Jungwook Choi
- Primary area: deep_learning->large_language_models
- Keywords: Quantization;Reasoning;Large Language Models
- Source URL: https://openreview.net/forum?id=aKY52fnzgc
- PDF URL: https://openreview.net/pdf?id=aKY52fnzgc

## Abstract

Large Reasoning Models (LRMs) achieve strong problem-solving through long chain-of-thought, but their deployment is constrained by the high cost of full-precision inference and growing KV cache footprints. Microscaled FP4 formats enable efficient FP4 deployment; however, fully quantizing weights, activations, and KV caches (W4A4KV4) causes severe reasoning degradation that existing PTQ and QAT fail to recover. We identify that FP4 failures concentrate on low-entropy tokens—precise symbolic commitments such as digits and operators—where quantization noise inflates sampling errors that cascade through reasoning traces. Based on this insight, we propose ReQAT, a reasoning-centric FP4 training framework with three components: (i) Trace-Aligned QAT (TAQ), which revisits identical reasoning traces to focus updates on critical low-entropy decisions; (ii) Selective Entropy Minimization (SEM), which reinforces confidence at low-entropy positions; and (iii) Q-FIT, a quantization-friendly initialization that jointly calibrates RoPE-consistent KV cache transformations to stabilize QAT. Under the same training budget, ReQAT not only recovers but surpasses BF16 fine-tuning accuracy, while delivering up to $3.9\times$ throughput speedup on NVIDIA DGX Spark and $3.1\times$ on B200. The project repository is available at https://github.com/aiha-lab/ReQAT.

## One-Sentence Claim

ReQAT recovers full-precision reasoning accuracy under W4A4KV4 FP4 quantization by targeting low-entropy symbolic decision tokens and stabilizing RoPE-consistent KV cache transforms.

## Problem

Large reasoning models rely on long chains of thought, making full-precision inference and KV cache storage expensive. Microscaled FP4 formats promise efficient deployment, but fully quantizing weights, activations, and KV caches causes severe reasoning degradation that existing PTQ and QAT do not recover.

The paper asks why FP4 quantization fails for reasoning and how QAT can focus on the fragile parts of reasoning traces.

## Core Contribution

The paper identifies low-entropy tokens, such as digits and operators, as failure hotspots: quantization noise inflates sampling errors at precise symbolic commitments, and those errors cascade through reasoning traces.

It proposes ReQAT with three components:

- Trace-Aligned QAT revisits identical reasoning traces to focus updates on critical low-entropy decisions.
- Selective Entropy Minimization reinforces confidence at low-entropy positions.
- Q-FIT initializes quantization-friendly weights and jointly calibrates RoPE-consistent KV cache transformations.

Under the same training budget, ReQAT surpasses BF16 fine-tuning accuracy and delivers up to 3.9x throughput speedup on NVIDIA DGX Spark and 3.1x on B200.

## Method

ReQAT aligns quantization-aware training with the structure of reasoning traces. Instead of treating all tokens equally, it emphasizes deterministic symbolic positions where small noise can flip a critical commitment.

Q-FIT prepares weights and KV-cache transformations for FP4 stability, including RoPE consistency, so low-bit inference does not destabilize long-context reasoning.

## Experiments and Evidence

Evidence reported in the abstract:

- W4A4KV4 FP4 quantization of weights, activations, and KV caches.
- Identification of low-entropy reasoning tokens as quantization failure points.
- Trace-Aligned QAT, Selective Entropy Minimization, and Q-FIT.
- Accuracy surpassing BF16 fine-tuning under the same training budget.
- Throughput speedup up to 3.9x on NVIDIA DGX Spark and 3.1x on B200.
- Code release.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: model sizes, reasoning benchmarks, FP4 format, KV-cache calibration, and memory savings.

## Limits and Failure Modes

- Low-entropy token focus may not cover creative or ambiguous reasoning tasks.
- Trace-aligned retraining needs representative reasoning traces.
- Hardware speedups may depend on FP4 kernel maturity and platform support.
- Surpassing BF16 fine-tuning requires careful benchmark and budget normalization.

## Deep Themes

**Reasoning quantization fails at symbolic commitments.** Digits and operators are fragile points where small noise cascades.

**Compression must be task-aware.** ReQAT designs QAT around reasoning traces rather than generic perplexity preservation.

**KV cache quantization is central to long reasoning deployment.** Efficient LRMs require low-bit activations and caches, not just weight-only compression.

## Subthemes

- FP4 W4A4KV4 reasoning quantization.
- Trace-Aligned QAT.
- Selective Entropy Minimization.
- RoPE-consistent KV cache transforms.
- Low-entropy symbolic tokens.

## Connections to Other Papers

Connects to FlashOptim, Brain Encoding Scale, SmoothSpike, FeatJND, and Incremental BPE through compression/efficiency preserving task behavior. It also links to NAD because both identify early/internal reasoning signals that predict correctness.

## Notes for Cross-Paper Synthesis

ReQAT adds a precision-aware reasoning theme: efficient inference succeeds when compression protects the exact token decisions where reasoning traces become brittle.
