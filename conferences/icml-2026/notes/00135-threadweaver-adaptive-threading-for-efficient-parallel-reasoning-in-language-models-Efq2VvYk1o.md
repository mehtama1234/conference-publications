# ThreadWeaver: Adaptive Threading for Efficient Parallel Reasoning in Language Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: Efq2VvYk1o
- Authors: Long Lian; Sida Wang; Felix Juefei-Xu; Tsu-Jui Fu; Xiuyu Li; Adam Yala; Trevor Darrell; Alane Suhr; Yuandong Tian; Xi Victoria Lin
- Primary area: deep_learning->large_language_models
- Keywords: Adaptive parallel reasoning;inference-time scaling;chain-of-thought;test-time scaling
- Source URL: https://openreview.net/forum?id=Efq2VvYk1o
- PDF URL: https://openreview.net/pdf?id=Efq2VvYk1o

## Abstract

Scaling inference-time computation has enabled Large Language Models (LLMs) to achieve strong reasoning performance, but their inherently sequential decoding incurs substantial latency, motivating parallelization of the generation process. However, existing parallel reasoning approaches suffer from performance degradation compared to their sequential counterparts, and often rely on specialized inference engines. We introduce ThreadWeaver, a framework for adaptive parallel reasoning that matches the accuracy of comparably sized sequential reasoning models while significantly reducing inference latency via three key innovations: 1) a two-stage parallel trajectory generator that produces high-quality parallel chain-of-thought data for supervised fine-tuning; 2) a trie-based rollout design that enables parallel reasoning on any off-the-shelf autoregressive inference engine; and 3) a parallelization-aware reinforcement learning framework that trains the model to balance reasoning accuracy with effective parallelization. Across six challenging math reasoning benchmarks, ThreadWeaver trained on top of Qwen3-8B achieves performance on par with cutting-edge sequential reasoning models (79.9% on AIME24 and 71.9% on average) while delivering up to 1.53x speedup in token latency, establishing a new Pareto frontier between accuracy and efficiency.

## One-Sentence Claim

ThreadWeaver trains language models for adaptive parallel chain-of-thought reasoning, matching sequential accuracy while reducing inference latency on standard autoregressive engines.

## Problem

Inference-time scaling improves reasoning but sequential decoding is slow; existing parallel reasoning often loses accuracy or depends on specialized inference systems.

## Core Contribution

The paper introduces ThreadWeaver with parallel trajectory generation, trie-based rollouts, and parallelization-aware reinforcement learning.

## Method

A two-stage parallel trajectory generator creates high-quality parallel CoT data for supervised fine-tuning. Trie-based rollouts enable parallel reasoning on off-the-shelf AR engines, and RL trains the model to balance accuracy with parallelization effectiveness.

## Experiments and Evidence

The abstract reports Qwen3-8B-based ThreadWeaver achieving 79.9% on AIME24 and 71.9% average across six math benchmarks, with up to 1.53x token-latency speedup while matching cutting-edge sequential reasoning models.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: trie rollout mechanics, data generation cost, parallel hardware assumptions, benchmark variance, and failure cases where reasoning dependencies are strongly sequential.

## Deep Themes

- Test-time reasoning needs parallelism to reduce latency.
- Chain-of-thought can be reorganized into adaptive threads.
- Efficiency and accuracy can be jointly optimized through parallelization-aware RL.

## Subthemes

- Parallel reasoning.
- Chain-of-thought.
- Test-time scaling.
- Trie rollouts.
- Math reasoning.
- Latency reduction.

## Connections to Other Papers

Connects to TTT-Discover, MaxRL, semantic fixed-point early exit, and efficient inference papers through test-time compute as an optimized process.

## Notes for Cross-Paper Synthesis

ThreadWeaver strengthens the inference-process theme: reasoning is becoming something models schedule and parallelize, not just a token-by-token chain.
