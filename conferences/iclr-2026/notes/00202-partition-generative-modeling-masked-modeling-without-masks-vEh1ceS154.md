# Partition Generative Modeling: Masked Modeling Without Masks

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: vEh1ceS154
- Authors: Justin Deschenaux; Lan Tran; Caglar Gulcehre
- Primary area: generative models
- Keywords: masked generative modeling;discrete diffusion;masked diffusion language modeling;diffusion language modeling
- Source URL: https://openreview.net/forum?id=vEh1ceS154
- PDF URL: https://openreview.net/pdf?id=vEh1ceS154

## Abstract

Masked generative models (MGMs) can generate tokens in parallel and in any order, unlike autoregressive models (ARMs), which decode one token at a time, left-to-right. However, MGMs process the full-length sequence at every sampling step, including \mask tokens that carry no information. In contrast, ARMs process only the previously generated tokens.
We introduce ``Partition Generative Models'' (PGMs), which replace masking with partitioning. Tokens are split into two groups that cannot attend to each other, and the model learns to predict each group conditioned on the other, eliminating mask tokens entirely. Because the groups do not interact, PGMs can process only the clean tokens during sampling, like ARMs, while retaining parallel, any-order generation, like MGMs.
On OpenWebText, PGMs achieve $5-5.5\times$ higher throughput than MDLM while producing samples with lower Generative Perplexity. On ImageNet, PGMs reach comparable FID to MaskGIT with a $7.5\times$ throughput improvement. With twice as many steps, the FID improves to 4.56 while remaining $3.9\times$ faster than MGMs. Finally, PGMs remain compatible with existing MGM samplers and distillation methods.

## One-Sentence Claim

Partition Generative Models remove mask tokens by splitting tokens into noninteracting groups, retaining parallel any-order generation while improving sampling throughput.

## Problem

Masked generative models can generate tokens in parallel and any order, but they waste computation by processing full-length sequences with many mask tokens at every sampling step. Autoregressive models avoid mask-token overhead but lose parallel any-order decoding.

## Core Contribution

The paper introduces Partition Generative Models, which replace masking with partitioning. Tokens are divided into groups that cannot attend to each other, and the model learns each group conditioned on the other, enabling clean-token-only sampling.

## Method

PGMs train by splitting sequences into two noninteracting token groups and predicting each group from the other. At sampling time, because groups do not mutually attend, the model can process only already generated clean tokens while retaining compatibility with existing masked-model samplers and distillation methods.

## Experiments and Evidence

On OpenWebText, PGMs reportedly achieve 5x-5.5x higher throughput than MDLM with lower Generative Perplexity. On ImageNet, PGMs match MaskGIT FID with 7.5x throughput improvement; with twice as many steps, FID improves to 4.56 while still being 3.9x faster than MGMs.

## Limits and Failure Modes

Partition independence may restrict interactions that matter for global coherence. The two-group setup might require careful sampling schedules or distillation for difficult dependencies. Full-text review should check partition strategy, likelihood objective, compatibility with arbitrary order samplers, quality metrics, and comparisons under equal compute.

## Deep Themes

- Parallel generation without mask-token waste.
- Training/sampling structure for masked models.
- Efficient discrete diffusion alternatives.
- Any-order generation with clean-token computation.

## Subthemes

- Partitioned attention.
- Masked modeling without masks.
- OpenWebText throughput.
- ImageNet MaskGIT comparison.
- MGM sampler compatibility.

## Connections to Other Papers

Connects to PAPL, Prophet, LPD, SANA-Video, and MotionStream through generation-path efficiency and training-inference alignment.

## Notes for Cross-Paper Synthesis

PGM shows that many generation inefficiencies are representation artifacts: mask tokens are a training convenience that become a sampling cost. Partitioning removes that cost while preserving core MGM flexibility.
