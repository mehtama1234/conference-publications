# Token-Importance Guided Direct Preference Optimization

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: cMEnMVvMw9
- Authors: Ning Yang; Hai Lin; Yibo Liu; Baoliang Tian; Guoqing Liu; Haijun Zhang
- Primary area: foundation or frontier models, including LLMs
- Keywords: LLMs;RLHF;DPO;Human Preference Alignment;Token-lmportance;Triplet Loss
- Source URL: https://openreview.net/forum?id=cMEnMVvMw9
- PDF URL: https://openreview.net/pdf?id=cMEnMVvMw9

## Abstract

Aligning Large Language Models (LLMs) with human preferences is crucial for safe and effective AI interactions. While popular methods like Direct Preference Optimization (DPO) have simplified alignment, they remain sensitive to data noise and overlook the differential importance of individual tokens. Existing token-level approaches often rely on probability prediction or simplistic weighting schemes to obtain token importance, which still cannot fully address these issues. To solve this problem, we propose the Token-Importance Guided Direct Preference Optimization (TI-DPO), a framework that achieves fine-grained semantic control through two synergistic innovations. 
First, we propose a novel hybrid weighting mechanism that combines gradient attribution with a Gaussian prior, ensuring both the accuracy and robustness of token importance scores. Second, we employ a triplet loss to provide structured guidance for the optimization, explicitly guiding model outputs to approach preferred responses and diverge from non-preferred ones. Experimental results show that TI-DPO achieves higher accuracy and stronger generative diversity, providing more stable and computationally efficient solutions compared with DPO and other RLHF methods.

## One-Sentence Claim

TI-DPO improves preference alignment by weighting tokens with gradient-attribution and Gaussian-prior importance scores, then adding triplet loss to separate preferred from rejected responses.

## Problem

DPO simplifies human-preference alignment, but it is sensitive to noisy preference data and treats tokens too uniformly.

Different tokens contribute unequally to semantic preference, so sentence-level preference optimization can overfit irrelevant tokens or underweight decisive content.

## Core Contribution

The paper introduces Token-Importance Guided Direct Preference Optimization.

It combines a hybrid token-weighting mechanism with triplet loss to provide fine-grained semantic control during preference optimization.

## Method

TI-DPO estimates token importance using gradient attribution combined with a Gaussian prior for robustness.

The triplet objective pulls model outputs closer to preferred responses and pushes them away from non-preferred responses, adding structured semantic guidance beyond ordinary DPO likelihood ratios.

## Experiments and Evidence

The abstract reports higher accuracy, stronger generative diversity, improved stability, and better computational efficiency than DPO and other RLHF methods.

Exact tasks and model scales are not given in the abstract.

## Limits and Failure Modes

Gradient attribution can be noisy, and token importance may not capture discourse-level or long-range preference reasons. A Gaussian prior may impose a shape that fails for sparse decisive tokens.

Because this note is abstract-only, details still need checking: attribution method, Gaussian prior form, triplet construction, datasets, baselines, model scales, and diversity metrics.

## Deep Themes

- Token-level alignment control: preference learning should weight semantically decisive tokens more.
- Robust importance estimation: gradient attribution is stabilized with a prior rather than used directly.
- Structured preference geometry: triplet loss creates explicit preferred/rejected separation.
- Noise-aware DPO variants: direct alignment methods are being modified to handle preference-data imperfections.

## Subthemes

- Direct Preference Optimization.
- Token importance.
- Gradient attribution.
- Triplet loss.

## Connections to Other Papers

This connects to AuxDPO, SafeDPO, DPO/RLHF equivalence, and preference-optimization papers.

It also relates to TROLL because both refine post-training at the token/action level.

## Notes for Cross-Paper Synthesis

TI-DPO adds a fine-grained alignment theme: preference optimization is moving from response-level objectives toward token-level causal or semantic attribution.
