# Robust Harmful Features Under Jailbreak Attacks: Mechanistic Evidence from Attention Head Specialization in Large Language Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: LTF6LtBo0E
- Authors: Yanchen Yin; Dongqi Han; Linghui Li
- Primary area: deep_learning->large_language_models
- Keywords: Large Language Models;Jailbreak Attacks;Safety Mechanisms;Attention Heads
- Source URL: https://openreview.net/forum?id=LTF6LtBo0E
- PDF URL: https://openreview.net/pdf?id=LTF6LtBo0E

## Abstract

Jailbreak attacks bypass LLM safety alignment, yet their mechanisms remain poorly understood. We provide evidence that attacks do not comprehensively eliminate safety features, but instead selectively suppress specific attention heads. We identify two functionally differentiated types: **Adversarially Compromised Heads (ACHs)** concentrated in early layers, which are suppressed under attacks, and **Safety-Aligned Heads (SAHs)** in mid-layers, which maintain robust activations even when attacks succeed. Ablation studies support the causal role of ACHs and the contribution of SAHs to robust activations: suppressing a small number of ACHs is sufficient to induce jailbreak-like behavior on normally refused inputs, while removing SAHs substantially weakens mid-layer safety activations. Token-level attribution further shows that ACH suppression is driven specifically by attack-template tokens, providing a mechanistic account of why attacks can bypass refusal decisions through ACH suppression while leaving internal safety signals sustained by SAHs—a phenomenon we term **Robust Harmful Features**. To validate the practical significance of this robustness, we show that simply reading these persistent activations—without any training—yields competitive aggregate detection performance with strong adversarial robustness.

## One-Sentence Claim

Jailbreaks suppress specific early-layer compromised heads while mid-layer safety-aligned heads retain harmful-feature activations that can be read out for robust detection.

## Problem

Jailbreak attacks bypass aligned refusal behavior, but it is unclear whether they erase safety features or selectively disrupt the heads that route those features into decisions.

## Core Contribution

The paper identifies Adversarially Compromised Heads and Safety-Aligned Heads, shows their causal roles through ablation and attribution, and uses persistent harmful activations for training-free adversarially robust detection.

## Method

The authors compare attention-head activations under attacks, ablate small sets of ACHs and SAHs, trace token-level attribution to attack-template tokens, and read persistent mid-layer activations without training as a detector.

## Experiments and Evidence

The abstract reports that suppressing a small number of ACHs induces jailbreak-like behavior on normally refused inputs, removing SAHs weakens mid-layer safety activations, and reading robust harmful features yields competitive detection with strong adversarial robustness.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: model families, jailbreak datasets, head-selection stability, detector thresholds, adaptive attack resistance, and whether "harmful features" generalize across languages and domains.

## Deep Themes

- Safety features may persist internally even when refusal behavior fails.
- Jailbreaks can be route/head suppression attacks rather than total feature erasure.
- Mechanistic readouts can support training-free safety monitoring.

## Subthemes

- Jailbreak attacks.
- Attention-head specialization.
- Safety-aligned heads.
- Adversarially compromised heads.
- Token-level attribution.
- Training-free detection.

## Connections to Other Papers

Connects to tail-risk estimation, FlowGuard, and route-gating hallucination control through internal safety diagnostics and deployment risk detection.

## Notes for Cross-Paper Synthesis

This paper deepens the safety-mechanisms theme: failure at the output layer does not necessarily mean the model lacks internal safety evidence; the issue may be whether that evidence controls the decision.
