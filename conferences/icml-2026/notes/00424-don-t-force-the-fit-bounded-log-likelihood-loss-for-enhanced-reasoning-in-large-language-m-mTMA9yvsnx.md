# Don't Force the Fit: Bounded Log-Likelihood Loss for Enhanced Reasoning in Large Language Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: mTMA9yvsnx
- Authors: Feng Zhao; Hong Zhang; Yu Yang; Ruilin Zhao; Guandong Xu
- Primary area: deep_learning->large_language_models
- Keywords: Supervised Fine-Tuning;Reasoning in Large Language Models;Optimization Objectives
- Source URL: https://openreview.net/forum?id=mTMA9yvsnx
- PDF URL: https://openreview.net/pdf?id=mTMA9yvsnx

## Abstract

Supervised fine-tuning (SFT) is central to aligning large language models (LLMs) with instruction following and task-specific reasoning. Despite its success, SFT optimizes token-level likelihoods under the implicit assumption that strictly fitting all tokens in expert demonstrations induces the desired downstream behavior. However, in reasoning tasks where correctness is defined by logical validity or final outcomes rather than exact token realizations, this assumption can lead to optimization misalignment. We empirically observe that low-probability tokens in reasoning demonstrations often correspond to realization-specific or stylistic variations, and that reducing their influence during training consistently improves generalization on reasoning benchmarks. Motivated by this insight, we propose the *Bounded Log-Likelihood Loss* (BLL-Loss), a simple and parameter-free alternative to standard likelihood training that bounds gradient contributions from low-probability tokens while preserving conventional optimization behavior. We provide theoretical insights and extensive empirical results demonstrating that BLL-Loss improves reasoning generalization across diverse model scales and challenging benchmarks.

## One-Sentence Claim

Bounded Log-Likelihood Loss improves reasoning SFT by limiting gradient influence from low-probability demonstration tokens that often encode stylistic rather than logically essential variation.

## Problem

SFT trains LLMs to match expert demonstrations token by token, assuming exact likelihood fitting induces the desired behavior. For reasoning, correctness depends on logical validity or final outcome, not exact token realization.

The paper observes that low-probability tokens in demonstrations often reflect realization-specific or stylistic choices, and forcing the model to fit them can hurt generalization.

## Core Contribution

The paper proposes Bounded Log-Likelihood Loss, a simple parameter-free alternative to standard likelihood training. It bounds gradient contributions from low-probability tokens while preserving ordinary optimization behavior for the rest.

Theoretical insights and empirical results show improved reasoning generalization across model scales and benchmarks.

## Method

BLL-Loss modifies token-level SFT so unusually low-probability tokens do not dominate gradients. Instead of forcing all expert tokens equally, it caps the influence of tokens likely to be idiosyncratic or stylistic.

The method is parameter-free, making it a drop-in loss change rather than a new data pipeline.

## Experiments and Evidence

Evidence reported in the abstract:

- Empirical observation that low-probability reasoning tokens often reflect stylistic or realization-specific variation.
- Parameter-free Bounded Log-Likelihood Loss.
- Preserves conventional behavior while bounding low-probability token gradients.
- Improves reasoning generalization across diverse model scales.
- Improves on challenging reasoning benchmarks.
- Theoretical insights provided.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: exact bound, benchmark suite, model scales, and comparison to token filtering.

## Limits and Failure Modes

- Some low-probability tokens may be essential reasoning pivots, not style.
- Parameter-free clipping may not suit all domains or tokenization schemes.
- Improvements may depend on demonstration quality.
- Loss-level fixes cannot correct logically flawed training data.

## Deep Themes

**Exact imitation can be misaligned.** Reasoning quality is not equivalent to matching every demonstration token.

**SFT loss should reflect task semantics.** Token likelihood is a proxy that needs adjustment for reasoning.

**Generalization may improve by ignoring idiosyncrasy.** Bounding gradients reduces overfitting to incidental wording.

## Subthemes

- Supervised fine-tuning.
- Bounded log-likelihood.
- Low-probability token gradients.
- Reasoning generalization.
- Outcome versus realization mismatch.

## Connections to Other Papers

Connects to RePO, Critique-GRPO, PRISM, Identity Bridge, and DPO Unchained. It adds another training-objective critique: the loss must match what the task considers correct.

## Notes for Cross-Paper Synthesis

BLL-Loss strengthens the objective-design theme: many failures arise when optimization rewards exact surface fit rather than the latent behavior we actually want.
