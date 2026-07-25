# Securing Multimodal AI through Internal Information Decomposition

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: GEzZIUmEqE
- Authors: Jehyeok Yeon; Hyeonjeong Ha; Qiusi Zhan; Heng Ji
- Primary area: social_aspects->safety
- Keywords: Vision-Language Models;AI Safety;Jailbreaking;Adversarial Robustness;Information Theory;Anomaly Detection
- Source URL: https://openreview.net/forum?id=GEzZIUmEqE
- PDF URL: https://openreview.net/pdf?id=GEzZIUmEqE

## Abstract

Multimodal large language models introduce attack surfaces absent in unimodal systems: adversaries can distribute malicious intent across modalities to evade unimodal safeguards. This motivates using cross-modal consistency as a detection signal rather than inspecting each modality in isolation. Our key observation is that benign inputs induce compatible predictive behavior from text-only and vision-only reasoning that stabilizes when fused, whereas adversarial manipulation disrupts this consistency, causing abnormal multimodal behavior. Existing defenses that examine raw inputs or outputs overlook this internal fusion process, rendering them brittle and computationally expensive. We propose FlowGuard, a lightweight inference-time framework that detects harmful inputs by monitoring internal multimodal consistency. Unlike approaches that rely on scalar confidence metrics, FlowGuard derives FlowVectors inspired by Partial Information Decomposition that quantify cross-modal redundancy, synergy, and modality-specific dominance, capturing whether multimodal fusion aligns with unimodal semantic evidencebetween unimodal and fused multimodal output distributions. In a one-class classification problem trained solely on benign data, FlowGuard reduces Attack Success Rates from $>90\%$ to $<15\%$ on unseen attacks, with $<3\%$ utility loss and up to a $6\times$ latency reduction. Our results demonstrate that monitoring cross-modal consistency offers an efficient and effective defense for multimodal reasoning.

## One-Sentence Claim

FlowGuard detects multimodal attacks by monitoring internal cross-modal consistency through information-decomposition-inspired FlowVectors.

## Problem

Multimodal adversaries can split malicious intent across text and images, bypassing defenses that inspect each modality separately or only analyze raw inputs/outputs.

## Core Contribution

The paper proposes a lightweight inference-time multimodal safety framework trained only on benign data as a one-class detector.

## Method

FlowGuard compares text-only, vision-only, and fused multimodal output distributions, deriving FlowVectors that quantify redundancy, synergy, and modality-specific dominance to detect abnormal fusion behavior.

## Experiments and Evidence

The abstract reports reducing attack success from above 90% to below 15% on unseen attacks, with under 3% utility loss and up to 6x latency reduction.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: PID approximation, attack suite, one-class thresholding, utility metrics, and model-family generalization.

## Deep Themes

- Multimodal safety requires monitoring fusion, not only individual modalities.
- Cross-modal consistency can act as an internal anomaly signal.
- Information decomposition provides interpretable safety features.

## Subthemes

- Multimodal safety.
- Jailbreaking.
- Cross-modal consistency.
- Partial Information Decomposition.
- One-class anomaly detection.
- Inference-time defense.

## Connections to Other Papers

Connects to VISUALSWAP, SpatioLM, Jailbreak Foundry, Concept Removal Guidance, and activation-based safety auditing.

## Notes for Cross-Paper Synthesis

FlowGuard adds a fusion-consistency theme: multimodal systems are vulnerable at the interaction layer, so defenses must inspect internal cross-modal agreement.
