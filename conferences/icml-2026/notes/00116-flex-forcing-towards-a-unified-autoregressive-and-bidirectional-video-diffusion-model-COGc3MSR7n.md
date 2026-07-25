# Flex-Forcing: Towards a Unified Autoregressive and Bidirectional Video Diffusion Model

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: COGc3MSR7n
- Authors: Xinyin Ma; Julius Berner; Chao Liu; Arash Vahdat; Weili Nie; Xinchao Wang
- Primary area: deep_learning->generative_models_and_autoencoders
- Keywords: Video Generative Model
- Source URL: https://openreview.net/forum?id=COGc3MSR7n
- PDF URL: https://openreview.net/pdf?id=COGc3MSR7n

## Abstract

Recent progress in large-scale generative models has substantially advanced video generation, yet existing methods remain constrained by a rigid inference paradigm. Bidirectional diffusion models excel at global coherence and visual fidelity but suffer from slow inference, while autoregressive models offer efficient and streaming generation at the cost of long-range consistency and exposure bias. We introduce Flex-Forcing, a unified training and inference framework that enables a video diffusion model to seamlessly operate under both bidirectional and autoregressive generation regimes. The core idea is a flexible chunking mechanism jointly defined over the temporal axis and denoising steps. This design allows the model to (1) perform flexible chunking according to different device budgets, (2) perform bidirectional inference across chunks for global structure planning, while generating frames autoregressively within each chunk for efficient and fine-grained synthesis, and (3) perform any-order, any-timestep autoregressive generation without the strict causal constraint. Extensive experiments on multiple video generation benchmarks demonstrate that Flex-Forcing achieves consistently better video quality, long-video stability than strong baselines with a rigid inference schedule, while offering faster inference.

## One-Sentence Claim

Flex-Forcing lets a video diffusion model operate across bidirectional and autoregressive generation regimes through flexible chunking over time and denoising steps.

## Problem

Bidirectional video diffusion gives coherence and fidelity but is slow, while autoregressive video generation supports streaming and efficiency but suffers from long-range inconsistency and exposure bias.

## Core Contribution

The paper introduces a unified training and inference framework that combines bidirectional planning across chunks with autoregressive generation inside chunks.

## Method

Flex-Forcing defines chunks jointly over temporal axis and denoising steps, enabling generation schedules to adapt to device budgets, use bidirectional inference for global structure, and use any-order/any-timestep autoregressive generation without strict causal constraints.

## Experiments and Evidence

The abstract reports better video quality and long-video stability than strong rigid-schedule baselines while also offering faster inference across multiple video generation benchmarks.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: exact chunking schedule, training objective, benchmark set, memory costs, and failure modes for very long videos.

## Deep Themes

- Generation regimes can be unified through flexible inference schedules.
- Video models need both global planning and efficient local synthesis.
- Device budget can become a first-class generation-control variable.

## Subthemes

- Video diffusion.
- Autoregressive generation.
- Bidirectional generation.
- Flexible chunking.
- Long-video stability.
- Streaming synthesis.

## Connections to Other Papers

Connects to LoMDM, diffusion solver papers, dWorldEval, and efficient video reasoning through generation-process control and long-context media synthesis.

## Notes for Cross-Paper Synthesis

Flex-Forcing adds to the generation-process theme: models increasingly expose inference schedule as a controllable design axis.
