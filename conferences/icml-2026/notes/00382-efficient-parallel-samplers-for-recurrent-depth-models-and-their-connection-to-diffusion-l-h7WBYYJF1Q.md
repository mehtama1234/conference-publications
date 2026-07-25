# Efficient Parallel Samplers for Recurrent-Depth Models and Their Connection to Diffusion Language Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: h7WBYYJF1Q
- Authors: Jonas Geiping; Xinyu Yang; Guinan Su
- Primary area: deep_learning->large_language_models
- Keywords: Recurrent-Depth;Latent Reasoning;Efficiency;Diffusion Forcing;Parallelization;Inference;Decoding
- Source URL: https://openreview.net/forum?id=h7WBYYJF1Q
- PDF URL: https://openreview.net/pdf?id=h7WBYYJF1Q

## Abstract

Language models with recurrent depth, also referred to as universal or looped when considering transformers, are defined by the capacity to increase their computation through the repetition of layers. Recent efforts in pretraining have demonstrated that these architectures can scale to modern language modeling tasks while exhibiting advantages in reasoning tasks. 
  In this work, we examine the relationship between recurrent-depth models and diffusion language models. Building on their similarities, we develop a new diffusion forcing sampler for these models to accelerate generation. The sampler advances by decoding new tokens at every forward pass of the model, while the latent states of these tokens can be further refined in parallel through recurrence. Theoretically, under a fixed wall-clock budget, generation with our sampler is strictly more expressive than baseline autoregressive generation as it preserves the same recurrent depth while updating a strictly wider front of token positions in parallel, enabling more computation at equal serial depth. 
  Moreover, this sampler, based on principles from diffusion literature, can be directly applied to existing 3.5B recurrent-depth transformers without any tuning, leading to up to a 5x speedup.

## One-Sentence Claim

Recurrent-depth language models can be sampled faster by a diffusion-forcing procedure that decodes new tokens each pass while refining multiple latent token states in parallel.

## Problem

Recurrent-depth or looped Transformers gain reasoning capacity by repeating layers, but autoregressive decoding underuses parallelism: each serial step typically advances one token while recurrence deepens computation. The paper observes similarities between these models and diffusion language models.

The problem is how to preserve recurrent reasoning depth while widening the set of token positions updated per wall-clock step.

## Core Contribution

The paper develops a diffusion-forcing sampler for recurrent-depth models. It decodes new tokens at every forward pass while allowing latent states of multiple tokens to be refined in parallel through recurrence.

Theoretically, under a fixed wall-clock budget, the sampler is strictly more expressive than baseline autoregressive generation because it keeps the same recurrent depth while updating a wider front of token positions. Practically, it applies to existing 3.5B recurrent-depth Transformers without tuning and gives up to a 5x speedup.

## Method

The sampler borrows from diffusion-style iterative refinement. Rather than finalizing one token at a time, it maintains latent token states and refines them through recurrent passes while also adding new decoded positions.

This changes the computation schedule: serial depth is spent on a parallel frontier of tokens, not only the latest token.

## Experiments and Evidence

Evidence reported in the abstract:

- Theoretical expressivity advantage under fixed wall-clock budget.
- Same recurrent depth as baseline autoregressive generation.
- Strictly wider set of token positions updated in parallel.
- Direct application to existing 3.5B recurrent-depth Transformers.
- Up to 5x speedup without tuning.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: quality-speed tradeoff, tasks, recurrent-depth architecture, and decoding error modes.

## Limits and Failure Modes

- Parallel token refinement may introduce consistency errors across positions.
- Speedups may depend on sequence length, batching, and hardware utilization.
- No-tuning deployment may not be optimal for all recurrent-depth models.
- Expressivity under wall-clock budget does not automatically guarantee better generation quality.

## Deep Themes

**Inference scheduling is a capability lever.** The paper improves generation by changing how computation is allocated across positions and depth.

**Diffusion and recurrence are converging.** Iterative refinement ideas migrate from diffusion language models into recurrent-depth Transformers.

**Parallelism can preserve reasoning depth.** The method seeks speed without simply reducing computation per token.

## Subthemes

- Recurrent-depth Transformers.
- Diffusion forcing.
- Parallel token refinement.
- Latent reasoning inference.
- Speed-quality decoding tradeoffs.

## Connections to Other Papers

Connects to KPE/KTS, Distribution Transformers, Incremental BPE, BlitzRank, and ReQAT. It fits the test-time scaling theme: inference algorithms are being redesigned to spend computation more effectively.

## Notes for Cross-Paper Synthesis

This paper adds a decoding-schedule version of test-time scaling: more useful computation can come from updating a broader latent frontier, not only from deeper serial chains.
