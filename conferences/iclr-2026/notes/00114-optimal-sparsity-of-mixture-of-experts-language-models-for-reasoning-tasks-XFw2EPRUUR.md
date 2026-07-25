# Optimal Sparsity of Mixture-of-Experts Language Models for Reasoning Tasks

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: XFw2EPRUUR
- Authors: Taishi Nakamura; Satoki Ishikawa; Masaki Kawamura; Takumi Okamoto; Daisuke Nohara; Jun Suzuki; Rio Yokota
- Primary area: foundation or frontier models, including LLMs
- Keywords: Mixture of Experts;memorization;reasoning;scaling laws;large language models
- Source URL: https://openreview.net/forum?id=XFw2EPRUUR
- PDF URL: https://openreview.net/pdf?id=XFw2EPRUUR

## Abstract

Empirical scaling laws have driven the evolution of large language models (LLMs), yet their coefficients shift whenever the model architecture or data pipeline changes.
Mixture‑of‑Experts (MoE) models, now standard in state‑of‑the‑art systems, introduce a new sparsity dimension that current dense‑model frontiers overlook.
We investigate how MoE sparsity influences two distinct capability regimes: memorization skills and reasoning skills.
By training MoE families that vary total parameters, active parameters, and top-$k$ routing under fixed compute budgets, we disentangle pre-training loss from downstream accuracy. 
Our results reveal two principles. First, Active FLOPs: models with identical training loss but greater active compute achieve higher reasoning accuracy. Second, Total tokens per parameter (TPP): memorization tasks improve with more parameters, while reasoning tasks benefit from optimal TPP, indicating that reasoning is data-hungry. 
Neither reinforcement learning post-training (GRPO) nor increased test-time compute alters these trends. 
We therefore argue that optimal MoE sparsity must be determined jointly by active FLOPs and TPP, revising the classical picture of compute-optimal scaling. 
All code, data sources, and logs are released to facilitate reproducibility and future work.

## One-Sentence Claim

Optimal MoE sparsity for reasoning depends jointly on active FLOPs and tokens per parameter, revising dense-model compute-optimal scaling laws.

## Problem

Scaling laws often assume dense architectures, but MoE models introduce sparsity through total parameters, active parameters, and routing choices.

Current frontiers do not fully explain how sparsity affects memorization versus reasoning, especially under fixed compute budgets.

## Core Contribution

The paper studies MoE families varying total parameters, active parameters, and top-k routing to disentangle pretraining loss from downstream accuracy.

It identifies two principles: Active FLOPs for reasoning accuracy at matched loss, and total tokens per parameter for separating memorization from reasoning behavior.

## Method

The authors train MoE model families under fixed compute budgets and evaluate memorization and reasoning tasks separately.

They compare models with similar training loss but different active compute and analyze how TPP affects downstream capabilities.

## Experiments and Evidence

The abstract reports that models with identical training loss but greater active compute achieve better reasoning accuracy.

Memorization improves with more parameters, while reasoning benefits from optimal TPP and appears data-hungry. Neither GRPO post-training nor increased test-time compute changes these trends.

## Limits and Failure Modes

MoE scaling conclusions may depend on routing implementation, data mix, model size range, and task definitions for memorization versus reasoning.

Because this note is abstract-only, details still need checking: model scales, routing settings, compute accounting, benchmark selection, GRPO setup, test-time compute protocol, and released logs.

## Deep Themes

- Sparse scaling laws: MoE adds sparsity as a new axis beyond dense parameter and compute counts.
- Active compute for reasoning: downstream reasoning can diverge from matched pretraining loss.
- Tokens per parameter as capability control: reasoning and memorization prefer different data-parameter regimes.
- Post-training cannot erase pretraining allocation: RL and test-time compute do not change the underlying sparsity trends.

## Subthemes

- Mixture-of-Experts.
- Active FLOPs.
- Total tokens per parameter.
- Memorization versus reasoning.

## Connections to Other Papers

This connects to ERC loss, scaling-law spectra, Train-before-Test, and MoE/router specialization work.

It also relates to reasoning-with-sampling and post-training papers because it argues some capability trends are fixed by pretraining architecture/data allocation.

## Notes for Cross-Paper Synthesis

This paper adds a sparse-scaling theme: reasoning quality depends on active computation and data density, not just total sparse parameter count.
