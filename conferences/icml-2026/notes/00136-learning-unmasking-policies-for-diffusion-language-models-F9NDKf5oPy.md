# Learning Unmasking Policies for Diffusion Language Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: F9NDKf5oPy
- Authors: Metod Jazbec; Theo X. Olausson; Louis Béthune; Pierre Ablin; Michael Kirchhof; Joao Monteiro; Victor Guilherme Turrisi da Costa; Jason Ramapuram; marco cuturi
- Primary area: deep_learning
- Keywords: Diffusion LLMs;Reinforcement Learning;Efficient Inference;Diffusion Language Models
- Source URL: https://openreview.net/forum?id=F9NDKf5oPy
- PDF URL: https://openreview.net/pdf?id=F9NDKf5oPy

## Abstract

Diffusion (Large) Language Models (dLLMs) now match the downstream performance of their autoregressive counterparts on many tasks, while holding the promise of being more efficient during inference. One critical design aspect of dLLMs is the \textit{sampling procedure} that selects which tokens to unmask at each diffusion step. Indeed, recent work has found that heuristic strategies such as confidence thresholding improve both sample quality and token throughput compared to random unmasking. However, such heuristics have downsides: they require manual tuning, and we observe that their performance degrades with larger block sizes. In this work, we instead propose to train sampling procedures using reinforcement learning. Specifically, we formalize masked diffusion sampling as a Markov decision process in which the dLLM serves as the environment, and propose a lightweight policy based on a single-layer transformer that maps dLLM token confidences to unmasking decisions. Our experiments show that these trained policies match the performance of state-of-the-art heuristics when combined with semi-autoregressive (block) generation, while outperforming them in the full-diffusion setting. Our code is available at [https://github.com/apple/ml-rl-dllm](https://github.com/apple/ml-rl-dllm).

## One-Sentence Claim

Diffusion language model unmasking can be learned as an RL policy over token confidences, outperforming manually tuned heuristics in full-diffusion generation.

## Problem

Sampling quality and throughput in diffusion language models depend heavily on which tokens are unmasked at each step, while heuristic unmasking requires tuning and degrades with larger block sizes.

## Core Contribution

The paper formalizes masked diffusion sampling as an MDP and trains lightweight unmasking policies with reinforcement learning.

## Method

The dLLM acts as the environment. A single-layer Transformer policy maps token confidences to unmasking decisions, learning sampling procedures rather than relying on confidence thresholds or random unmasking.

## Experiments and Evidence

The abstract reports that learned policies match state-of-the-art heuristics when paired with semi-autoregressive block generation and outperform them in full-diffusion settings.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: RL reward, training compute, block-size sensitivity, transfer across dLLMs, and latency overhead of the policy.

## Deep Themes

- Diffusion text inference has policy choices that can be learned.
- Sampling schedules are becoming RL-controlled components.
- Efficient non-autoregressive language generation depends on adaptive unmasking.

## Subthemes

- Diffusion language models.
- Unmasking policies.
- Reinforcement learning.
- Efficient inference.
- Block generation.
- Token confidence.

## Connections to Other Papers

Connects to LoMDM, Flex-Forcing, MaxRL, and ThreadWeaver through learned inference/generation policies.

## Notes for Cross-Paper Synthesis

This paper reinforces the generation-process-control theme: the sequence of reveal decisions is a trainable policy, not a fixed heuristic.
