# Real-Time Visual Attribution Streaming in Thinking Model

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: eVr10aZZIw
- Authors: Seil Kang; Woojung Han; Junhyeok Kim; Jinyeong Kim; Youngeun Kim; Seong Jae Hwang
- Primary area: applications->computer_vision
- Keywords: Reasoning Model;Vision-Language Model;Visual Attribution;Efficient Attribution;Faithfulness
- Source URL: https://openreview.net/forum?id=eVr10aZZIw
- PDF URL: https://openreview.net/pdf?id=eVr10aZZIw

## Abstract

We present an amortized framework for real-time visual attribution streaming in multimodal thinking models. When these models generate code from a screenshot or solve math problems from images, their long reasoning traces should be grounded in visual evidence. However, verifying this reliance is challenging: faithful causal methods require costly repeated backward passes or perturbations, while raw attention maps offer instant access, they lack causal validity. To resolve this, we introduce an amortized approach that learns to estimate the causal effects of semantic regions directly from the rich signals encoded in attention features. Across five diverse benchmarks and four thinking models, our approach achieves faithfulness comparable to exhaustive causal methods while enabling visual attribution streaming, where users observe grounding evidence as the model reasons, not after. Our results demonstrate that real-time, faithful attribution in multimodal thinking models is achievable through lightweight learning, not brute-force computation.

## One-Sentence Claim

Faithful visual attribution for multimodal thinking models can be streamed in real time by amortizing causal attribution from attention-derived features.

## Problem

Multimodal thinking models produce long reasoning traces over images and screenshots, but users need to know whether each reasoning step is grounded in the visual evidence. Existing faithful attribution methods require expensive backward passes or perturbation sweeps, while attention maps are cheap but not causally reliable.

The paper targets the gap between usable real-time attribution and faithful causal grounding.

## Core Contribution

The contribution is an amortized framework that learns to estimate causal effects of semantic visual regions from attention features. This enables attribution streaming as the model reasons, rather than post-hoc explanation after generation.

The paper's framing is important: it does not accept raw attention as explanation, but uses attention features as inputs to a learned estimator of causal attribution.

## Method

The method trains a lightweight attribution model to map rich attention-derived signals to estimates of region-level causal effects. Once trained, the estimator can run online during generation and update the user's view of visual grounding as the reasoning trace unfolds.

This amortizes the cost of exhaustive causal attribution over training, making inference-time attribution cheap enough for streaming.

## Experiments and Evidence

Evidence reported in the abstract:

- Five diverse benchmarks.
- Four multimodal thinking models.
- Faithfulness comparable to exhaustive causal methods.
- Real-time visual attribution streaming during reasoning.
- Lightweight learning rather than repeated backward or perturbation calls.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: semantic-region definition, causal target construction, latency, and whether attribution changes user decisions.

## Limits and Failure Modes

- Amortized estimators can inherit bias from the causal attribution procedure used as supervision.
- Attention features may be insufficient when evidence is encoded outside visible attention patterns.
- Region-level attribution may miss compositional or temporal dependencies across image elements.
- Streaming explanations can create misplaced trust if users overinterpret partial attribution.

## Deep Themes

**Interpretability is becoming real-time infrastructure.** Explanations are integrated into the reasoning process rather than generated afterward.

**Attention is not explanation, but can be evidence.** The paper occupies a pragmatic middle ground: use attention as a feature source, not as the final causal claim.

**Faithfulness and latency are jointly optimized.** The goal is explanation users can inspect while the model is still thinking.

## Subthemes

- Amortized causal attribution.
- Visual grounding for reasoning traces.
- Streaming interpretability.
- Attention-feature attribution estimators.
- Human-observable multimodal reasoning.

## Connections to Other Papers

Connects to MoCA, Agent0-VL, VenusBench-Mobile, Monitoring Monitorability, and NAD. It shares MoCA's concern with separating visual evidence from reasoning quality, and Monitoring Monitorability's concern with oversight visibility.

## Notes for Cross-Paper Synthesis

This paper adds a real-time interface layer to the verification theme: oversight improves when evidence attribution appears during generation, not only after a final answer is produced.
