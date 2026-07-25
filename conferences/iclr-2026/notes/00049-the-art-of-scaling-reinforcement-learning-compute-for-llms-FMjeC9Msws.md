# The Art of Scaling Reinforcement Learning Compute for LLMs

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: FMjeC9Msws
- Authors: Fnu Devvrit; Lovish Madaan; Rishabh Tiwari; Rachit Bansal; Sai Surya Duvvuri; Manzil Zaheer; Inderjit S Dhillon; David Brandfonbrener; Rishabh Agarwal
- Primary area: foundation or frontier models, including LLMs
- Keywords: Scaling;LLMs;Reasoning
- Source URL: https://openreview.net/forum?id=FMjeC9Msws
- PDF URL: https://openreview.net/pdf?id=FMjeC9Msws

## Abstract

Reinforcement learning (RL) has become central to training large language models (LLMs), yet the field lacks predictive scaling methodologies comparable to those established for pre-training.
    Despite rapidly rising compute budgets, there is no principled understanding of
    how to evaluate algorithmic improvements for scaling RL compute.
    We present the first large-scale systematic study, amounting to more than 400,000 GPU-hours, that defines a principled framework for analyzing and predicting RL scaling in LLMs.
    We fit sigmoidal compute-performance curves for RL training and ablate a wide range of common design choices to analyze their effects on asymptotic performance and compute efficiency. We observe:
    (1)
    Not all recipes yield similar asymptotic  performance,
    Details such as loss aggregation, normalization, curriculum, and off-policy algorithm primarily modulate compute efficiency without materially shifting the asymptote, and
    (3) Stable, scalable recipes follow predictable scaling trajectories, enabling extrapolation from smaller-scale runs.
    Combining these insights, we propose a _best-practice_ recipe, ScaleRL, and demonstrate its effectiveness by successfully scaling and predicting validation performance on a single RL run scaled up to 100,000 GPU-hours.
    Our work provides both a _scientific framework_ for analyzing scaling in RL and a practical recipe that brings RL training closer to the predictability long achieved in pre-training.

## One-Sentence Claim

ScaleRL provides a predictive scaling framework and best-practice recipe for LLM reinforcement learning, showing stable RL runs follow extrapolatable sigmoidal compute-performance curves.

## Problem

LLM RL training is consuming rising compute budgets, but lacks scaling methodologies comparable to pretraining scaling laws.

Without predictive scaling, it is hard to evaluate algorithmic improvements or decide which RL recipe is worth scaling.

## Core Contribution

The paper presents a large-scale systematic RL scaling study exceeding 400,000 GPU-hours.

It fits sigmoidal compute-performance curves, ablates common RL design choices, distinguishes asymptotic performance from compute efficiency, and proposes a best-practice recipe called ScaleRL.

## Method

The study runs RL training under many recipe choices and fits compute-performance curves. It analyzes how loss aggregation, normalization, curriculum, and off-policy algorithms affect efficiency and asymptotic outcomes.

It then validates predictive extrapolation by scaling a single RL run to 100,000 GPU-hours.

## Experiments and Evidence

The abstract reports that not all recipes have the same asymptotic performance. Many details mainly affect compute efficiency rather than the final asymptote.

Stable scalable recipes follow predictable trajectories, and ScaleRL successfully scales and predicts validation performance on a 100,000 GPU-hour run.

## Limits and Failure Modes

Scaling conclusions may depend on reward type, task mix, base model, and evaluation metric. Sigmoidal fits may fail for unstable algorithms or distribution shifts.

Because this note is abstract-only, details still need checking: model sizes, RL algorithms, reward benchmarks, ablation matrix, curve-fitting method, and how validation performance maps to real downstream utility.

## Deep Themes

- RL scaling laws for LLMs: post-training needs predictive compute methodology.
- Efficiency versus asymptote: recipe choices can change speed without changing ultimate performance.
- Stable trajectories enable extrapolation: small runs can predict larger runs only under scalable recipes.
- Scientific recipe evaluation: algorithmic changes should be judged by scaling curves, not one compute point.

## Subthemes

- Sigmoidal RL compute-performance curves.
- Loss aggregation and normalization.
- Curriculum and off-policy ablations.
- 100,000 GPU-hour validation run.

## Connections to Other Papers

This connects to SGD RLVR, Ctrl-R, OpenThoughts, RAGEN-2, and coverage theory through RL post-training for reasoning.

It also relates to pretraining scaling-law papers and phase-retrieval dynamics because it brings scaling analysis to a new training regime.

## Notes for Cross-Paper Synthesis

ScaleRL is a central post-training scaling anchor: RL compute needs its own scaling science rather than borrowing pretraining intuition.
