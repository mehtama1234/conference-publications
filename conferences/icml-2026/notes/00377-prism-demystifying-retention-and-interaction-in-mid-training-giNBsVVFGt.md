# PRISM: Demystifying Retention and Interaction in Mid-Training

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: giNBsVVFGt
- Authors: Bharat Runwal; Ashish Sunil Agrawal; Anurag Roy; Rameswar Panda
- Primary area: deep_learning->large_language_models
- Keywords: Mid Training;Large Language Models;Reinforcement learning
- Source URL: https://openreview.net/forum?id=giNBsVVFGt
- PDF URL: https://openreview.net/pdf?id=giNBsVVFGt

## Abstract

Mid-training is increasingly used to improve the reasoning capabilities of large language models (LLMs), yet its design choices and interaction with evaluation and reinforcement learning (RL) remain poorly understood. Prior work often focuses on narrow domain gains, overlooking retention of general abilities, long-context performance, and RL compatibility. We present $\textbf{PRISM}$ (Demystifying Retention and Interaction in Mid-Training), a holistic empirical study that analyzes mid-training design choices, what to evaluate, and how domain mixtures and training stages interact across model families. Experiments on Granite-3.3 8B, LLaMA-3.1 8B, and Mistral-7B/24B base models show that a relatively small, high-quality mid-training phase of $\textbf{$\sim$27B}$ tokens acts as a critical stabilizing stage for reasoning. Across models, PRISM yields consistent gains of $\textbf{$\sim$6–10}$ points on coding benchmarks and $\textbf{$\sim$17–30}$ points on mathematical reasoning benchmarks while preserving general performance. RL applied on top of PRISM-mid-trained models produces stable, monotonic improvements, adding a further $\textbf{$\sim$3–8}$ points across coding and math tasks such as LiveCodeBench, Codeforces, AIME and MATH500, and $\textbf{$\sim$17–20}$ points on science (GPQA-Diamond), whereas RL applied directly to base models is substantially less effective. Our results demonstrate that retention-aware mid-training is a necessary intermediate step for reliable reasoning enhancement and RL scaling, and provide practical guidance for designing robust mid-training pipelines for modern LLMs.

## One-Sentence Claim

PRISM shows that a compact, retention-aware mid-training stage can stabilize reasoning improvements and make later RL substantially more effective across LLM families.

## Problem

Mid-training is widely used to improve LLM reasoning, but its design choices are often evaluated narrowly. Gains in coding or math can come with hidden losses in general ability, long-context behavior, or compatibility with later RL.

The paper asks how domain mixtures and training stages interact, and whether mid-training should be treated as a stabilizing bridge between base pretraining and RL.

## Core Contribution

PRISM is a holistic empirical study of retention and interaction in mid-training. Across Granite-3.3 8B, LLaMA-3.1 8B, and Mistral-7B/24B base models, it finds that about 27B high-quality mid-training tokens act as a critical stabilizing stage for reasoning.

The study reports large coding and math gains while preserving general performance, and shows that RL on top of PRISM-mid-trained models improves stably and monotonically, whereas RL directly on base models is less effective.

## Method

The work varies mid-training design choices, domain mixtures, evaluation coverage, and subsequent RL stages across multiple model families. It evaluates reasoning, coding, math, science, general retention, and long-context concerns.

PRISM's methodological emphasis is interaction: mid-training is judged not only by immediate benchmark gains but by how it changes the effectiveness of later RL.

## Experiments and Evidence

Evidence reported in the abstract:

- Experiments on Granite-3.3 8B, LLaMA-3.1 8B, and Mistral-7B/24B.
- Roughly 27B high-quality mid-training tokens.
- About 6-10 point gains on coding benchmarks.
- About 17-30 point gains on mathematical reasoning benchmarks.
- General performance preserved.
- RL on PRISM-mid-trained models adds about 3-8 points on coding/math and 17-20 points on GPQA-Diamond.
- RL directly on base models is substantially less effective.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: exact data mixtures, retention benchmarks, RL algorithm, and compute budget.

## Limits and Failure Modes

- Results may depend heavily on the quality and composition of the 27B-token mixture.
- Retention claims need broad benchmark coverage and contamination controls.
- The right mid-training recipe may differ for larger models or already instruction-tuned models.
- Empirical interaction studies can be expensive to replicate.

## Deep Themes

**Training stages interact.** Mid-training is not just an isolated capability booster; it changes the optimization landscape for RL.

**Retention is an explicit objective.** The paper treats preserved general ability as part of success, not an afterthought.

**Reasoning scale needs staging.** Reliable RL gains appear to require a prepared model substrate.

## Subthemes

- Retention-aware mid-training.
- RL compatibility.
- Reasoning stabilization.
- Domain-mixture design.
- Multi-family LLM empirical study.

## Connections to Other Papers

Connects to daVinci-Dev, Hista/Numca, RePO, T2PO, and VideoKR. It complements data-design papers by showing that the order and mixture of training data can determine whether later RL works.

## Notes for Cross-Paper Synthesis

PRISM adds a pipeline-level theme: capability improvements depend on the sequence of training stages, and a good intermediate distribution can make downstream optimization tractable.
