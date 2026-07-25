# Stable-GFlowNet: Toward Diverse and Robust LLM Red-Teaming via Contrastive Trajectory Balance

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: OyPE1ganBR
- Authors: Minchan Kwon; Sunghyun Baek; Minseo Kim; Jaemyung Yu; Dongyoon Han; Junmo Kim
- Primary area: deep_learning->large_language_models
- Keywords: Distribution matching;Reinforcement learning;Red teaming
- Source URL: https://openreview.net/forum?id=OyPE1ganBR
- PDF URL: https://openreview.net/pdf?id=OyPE1ganBR

## Abstract

Large Language Model Red-Teaming, which proactively identifies vulnerabilities of large language models, is an essential process for ensuring safety.
Finding effective and diverse attacks in red team activities is important, but achieving both is challenging.
Generative Flow Networks (GFN) that perform distribution matching are a promising method, but they are notorious for training instability and mode collapse.
In particular, unstable reward functions in red team activities accelerate mode collapse.
We propose Stable-GFN (S-GFN), which eliminates Z estimation in GFN and reduces training instability.
S-GFN avoids Z-estimation through pairwise comparisons and employs a robust masking methodology against noisy rewards.
Additionally, we propose a fluency stabilizer to prevent the model from getting stuck in local optima that produce gibberish.
S-GFN provides more stable training while maintaining the optimal policy of GFN.
We demonstrate the overwhelming attack performance and diversity of S-GFN across various settings.

## One-Sentence Claim

Stable-GFlowNet improves LLM red-teaming by stabilizing GFlowNet training with contrastive trajectory balance, noisy-reward masking, and fluency regularization.

## Problem

Red-teaming needs attacks that are both effective and diverse, but GFlowNets can suffer training instability and mode collapse, especially under unstable red-team reward functions.

## Core Contribution

The paper proposes S-GFN, which avoids partition-function Z estimation through pairwise comparisons, adds robust masking for noisy rewards, and uses a fluency stabilizer to avoid gibberish local optima while preserving GFN optimal policy.

## Method

S-GFN replaces unstable Z-estimation with contrastive trajectory-balance-style pairwise objectives, filters unreliable reward signals, and regularizes generated attacks for fluency.

## Experiments and Evidence

The abstract reports strong attack performance and diversity across various settings.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: target models, red-team tasks, reward models, diversity metrics, harmfulness safeguards, and whether improved attacks are paired with defensive evaluation.

## Deep Themes

- Safety evaluation needs diverse adversarial distributions, not just single best attacks.
- Training stability is central for generative red-team search.
- Noisy rewards and fluency collapse must be handled jointly.

## Subthemes

- LLM red teaming.
- Generative Flow Networks.
- Distribution matching.
- Mode collapse.
- Noisy rewards.
- Attack diversity.

## Connections to Other Papers

Connects to tail-risk estimation, RLVepsR, and jailbreak-mechanism papers through adversarial safety evaluation and reward-noise-aware optimization.

## Notes for Cross-Paper Synthesis

S-GFN adds an adversarial-distribution theme: robust safety testing needs generators that cover diverse high-risk regions without collapsing under noisy reward feedback.
