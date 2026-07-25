# Mitigating Hallucinations in Large Vision-Language Models via Causal Route Gating

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: LIcj73RLX6
- Authors: Zhe Cheng; Wenyu Chen; Fode Zhang; Dehuan Shen
- Primary area: deep_learning->foundation_models
- Keywords: Large vision-language models;Hallucination mitigation;Mechanistic interpretability;Causal attribution
- Source URL: https://openreview.net/forum?id=LIcj73RLX6
- PDF URL: https://openreview.net/pdf?id=LIcj73RLX6

## Abstract

Large vision-language models (LVLMs) often hallucinate content that is fluent yet unsupported by the image, limiting their reliability in real-world deployment. We show that a key failure mode arises from route competition: even when visual tokens receive attention, the final token decision can be dominated by the textual pathway, causing the decoder to follow linguistic priors over visual evidence. To mitigate this, we propose a training-free, decision-aligned intervention that decomposes each attention head into a visual route and a text route, and estimates their token-level effects using an efficient one-forward/one-gradient approximation. These estimates reveal route conflict within heads and identify prior-dominant ones, enabling selective suppression of only the text route while keeping the visual route intact. Across five benchmarks spanning discriminative and generative settings, our method consistently reduces hallucination-related errors across models with limited impact on overall multimodal performance, while incurring a modest inference-time overhead.

## One-Sentence Claim

Causal route gating reduces LVLM hallucinations by identifying attention-head conflicts where text routes dominate visual evidence and suppressing only the prior-dominant text route.

## Problem

LVLMs can hallucinate fluent content unsupported by images because final token decisions may follow linguistic priors even when visual tokens receive attention.

## Core Contribution

The paper proposes a training-free, decision-aligned intervention that decomposes attention heads into visual and text routes, estimates token-level effects, and selectively gates conflicting text pathways.

## Method

The method uses a one-forward/one-gradient approximation to estimate visual-route and text-route token effects inside attention heads, identify prior-dominant route conflicts, and suppress only the text route while preserving visual evidence flow.

## Experiments and Evidence

The abstract reports consistent reductions in hallucination-related errors across five discriminative and generative benchmarks and multiple models, with limited impact on overall multimodal performance and modest inference overhead.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: route decomposition details, benchmark set, hallucination metrics, overhead, failure cases where visual evidence is ambiguous, and effects on creative captioning.

## Deep Themes

- Hallucination can arise from route competition, not absence of visual attention.
- Mechanistic attribution can guide training-free inference interventions.
- Decision-aligned gating preserves useful modality pathways while suppressing harmful priors.

## Subthemes

- LVLM hallucination.
- Causal attribution.
- Attention-head decomposition.
- Visual route versus text route.
- Training-free intervention.
- Multimodal reliability.

## Connections to Other Papers

Connects to VGS, FlowGuard, 3ViewSense, and multimodal safety papers through grounding, route decomposition, and cross-modal consistency.

## Notes for Cross-Paper Synthesis

This paper adds a route-level grounding theme: multimodal failures can persist despite attention to the right modality if the final causal path is dominated by a prior route.
