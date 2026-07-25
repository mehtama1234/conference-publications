# ECHO: Elastic Speculative Decoding with Sparse Gating for High-Concurrency Scenarios

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: L31hKCWRsN
- Authors: Xinyi. Hu; Yuhao Shen; Zhang Baolin; Hengxin Zhang; Jun Dai; Shuang Ge; Chen Lei; Yue Li; Mingcheng Wan
- Primary area: deep_learning->generative_models_and_autoencoders
- Keywords: LLM Inference;Speculative Decoding
- Source URL: https://openreview.net/forum?id=L31hKCWRsN
- PDF URL: https://openreview.net/pdf?id=L31hKCWRsN

## Abstract

Speculative Decodin promises to accelerate Large Language Model inference, yet its efficacy often degrades in production-grade scenarios. Existing evaluations typically overlook the compute-bound nature of high-concurrency regimes, where verification compute becomes the dominant bottleneck. Consequently, prior methods face a dilemma: static trees incur massive verification waste, while dynamic trees suffer from cumulative misjudgments and kernel incompatibility.
To bridge this gap, we introduce ECHO, a high concurrency-oriented framework integrated into SGLang that reformulates speculative execution as a budgeted scheduling problem.
Crucially, ECHO employs sparse confidence gating to manage the batch as a unified super-tree, elastically pivoting budget between depth and width to co-optimize the trade-off between reducing global verification steps and maximizing per-step efficiency.
Extensive evaluations across diverse model scales—particularly the industrial-grade Qwen3-235B—demonstrate that ECHO consistently outperforms state-of-the-art baselines in both low-load and high-load scenarios, achieving up to 5.35$\times$ walltime speedup and delivering over 20\% relative speedup gain against the strongest baselines.

## One-Sentence Claim

ECHO accelerates high-concurrency LLM inference by treating speculative decoding as budgeted scheduling over a sparsely gated batch-level super-tree.

## Problem

Speculative decoding can degrade in production high-concurrency regimes because verification compute becomes the bottleneck; static trees waste verification and dynamic trees accumulate misjudgments or break kernel compatibility.

## Core Contribution

The paper introduces an SGLang-integrated speculative execution framework that elastically reallocates budget between tree depth and width to reduce global verification steps while preserving per-step efficiency.

## Method

ECHO uses sparse confidence gating to manage a batch as a unified super-tree, formulating speculative decoding as a budgeted scheduling problem for high-load serving.

## Experiments and Evidence

The abstract reports consistent gains across model scales, including Qwen3-235B, with up to 5.35x walltime speedup and over 20% relative speedup over the strongest baselines in low- and high-load settings.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: hardware setup, concurrency levels, draft/target model choices, acceptance rates, kernel implementation, latency-tail behavior, and compatibility with other serving optimizations.

## Deep Themes

- Inference acceleration depends on production load regimes, not just single-request benchmarks.
- Scheduling and sparse gating can make speculative decoding elastic.
- Verification compute is a first-class bottleneck in deployed LLM systems.

## Subthemes

- LLM inference.
- Speculative decoding.
- High concurrency.
- Sparse confidence gating.
- SGLang.
- Budgeted scheduling.

## Connections to Other Papers

Connects to Top-W, compute-bounded RL, LiDAR, and other test-time control papers through inference-time algorithms that improve fixed-model behavior under compute constraints.

## Notes for Cross-Paper Synthesis

ECHO adds a systems-serving version of test-time scaling: the right inference algorithm depends on batch structure, concurrency, and verification cost, not only model quality.
