# POET-X: Memory-efficient LLM Training by Scaling Orthogonal Transformation

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: et8jpWLUuD
- Authors: Zeju Qiu; Lixin Liu; Adrian Weller; Han Shi; Weiyang Liu
- Primary area: deep_learning->large_language_models
- Keywords: LLM;Sparse Training;Efficiency
- Source URL: https://openreview.net/forum?id=et8jpWLUuD
- PDF URL: https://openreview.net/pdf?id=et8jpWLUuD

## Abstract

Efficient and stable training of large language models (LLMs) remains a core challenge in modern machine learning systems. To address this challenge, Reparameterized Orthogonal Equivalence Training (POET), a spectrum-preserving framework that optimizes each weight matrix through orthogonal equivalence transformation, has been proposed. Although POET provides strong training stability, its original implementation incurs high memory consumption and computational overhead due to intensive matrix multiplications. To overcome these limitations, we introduce POET-X, a scalable and memory-efficient variant that performs orthogonal equivalence transformations with significantly reduced computational cost. POET-X maintains the generalization and stability benefits of POET while achieving substantial improvements in throughput and memory efficiency. In our experiments, POET-X enables the pretraining of billion-parameter LLMs on a single Nvidia H100 GPU, and in contrast, standard optimizers such as AdamW run out of memory under the same settings.

## One-Sentence Claim

POET-X preserves the stability benefits of orthogonal-equivalence training while cutting memory and compute enough to pretrain billion-parameter LLMs on a single H100.

## Problem

Large-language-model training is constrained by optimizer memory, activation memory, and the computational overhead of stability-improving methods. POET offers spectrum-preserving reparameterized training through orthogonal equivalence transformations, but its original implementation is too memory- and compute-heavy for scalable LLM use.

The paper asks how to retain POET's stability/generalization advantages while making the transformation practical at billion-parameter scale.

## Core Contribution

The contribution is POET-X, a scalable and memory-efficient variant of Reparameterized Orthogonal Equivalence Training. It reduces the cost of orthogonal equivalence transformations while preserving the spectrum-related inductive bias that made POET stable.

The headline systems result is that POET-X enables billion-parameter LLM pretraining on a single Nvidia H100 GPU under settings where AdamW runs out of memory.

## Method

The method optimizes weight matrices through cheaper orthogonal equivalence transformations. While the abstract does not specify the exact implementation, the mechanism is a reparameterization that preserves spectral structure while reducing intensive matrix multiplications from the original POET.

The practical objective is to make optimizer-like stability improvements compatible with tight device memory budgets.

## Experiments and Evidence

Evidence reported in the abstract:

- Maintains POET's generalization and stability benefits.
- Improves throughput and memory efficiency.
- Enables billion-parameter LLM pretraining on one Nvidia H100.
- AdamW runs out of memory under the same settings.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: exact memory accounting, model sizes, batch/sequence settings, throughput numbers, and downstream evaluation.

## Limits and Failure Modes

- Single-GPU feasibility may depend on sequence length, batch size, architecture, and implementation choices.
- Spectrum preservation may help stability but could constrain optimization in some regimes.
- Comparisons to AdamW need equivalent training budgets and tuned baselines.
- Orthogonal transformations may introduce hidden overhead outside the reported setting.

## Deep Themes

**Training efficiency is a capability enabler.** The method matters because it changes what scale can be trained under fixed hardware.

**Optimization structure can replace memory.** POET-X uses a constrained reparameterization to get stability without standard optimizer overhead.

**Systems claims and theory-shaped training are converging.** The paper links spectral invariance to very practical memory limits.

## Subthemes

- Orthogonal equivalence training.
- Spectrum-preserving LLM optimization.
- Single-H100 billion-parameter pretraining.
- Memory-efficient sparse or structured training.
- Stability-through-reparameterization.

## Connections to Other Papers

Connects to ReQAT, WaterSIC, MACKO-SpMV, EMP, Incremental BPE, and FlashSketch. It belongs to the efficiency-as-capability cluster where architectural or mathematical structure turns limited hardware into usable model capacity.

## Notes for Cross-Paper Synthesis

POET-X broadens the efficiency theme from inference to training: 2026 work is aggressively searching for representations and optimizers that preserve capability while fitting inside real hardware constraints.
