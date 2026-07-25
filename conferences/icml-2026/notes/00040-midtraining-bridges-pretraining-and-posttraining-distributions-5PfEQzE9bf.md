# Midtraining Bridges Pretraining and Posttraining Distributions

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 5PfEQzE9bf
- Authors: Emmy Liu; Graham Neubig; Chenyan Xiong
- Primary area: deep_learning->large_language_models
- Keywords: midtraining;domain adaptation;pretraining;supervised fine-tuning;catastrophic forgetting
- Source URL: https://openreview.net/forum?id=5PfEQzE9bf
- PDF URL: https://openreview.net/pdf?id=5PfEQzE9bf

## Abstract

Midtraining, the practice of mixing specialized data with more general pretraining data in an intermediate training phase, has become widespread in language model development, yet there is little understanding of what makes it effective. We propose that midtraining functions as distributional bridging by providing better initialization for posttraining. We conduct controlled pretraining experiments, and find that midtraining benefits are largest for domains distant from general pretraining data, such as code and math, and scale with the proximity advantage the midtraining data provides toward the target distribution. In these domains, midtraining consistently outperforms continued pretraining on specialized data alone both in-domain and in terms of mitigating forgetting. We further conduct an investigation on the starting time and mixture weight of midtraining data, using code as a case study, and find that time of introduction and mixture weight interact strongly such that early introduction of specialized data is amenable to high mixture weights, while late introduction requires lower ones. This suggests that late introduction of specialized data outside a plasticity window cannot be compensated for by increasing data mixtures later in training. Beyond midtraining itself, this suggests that distributional transitions between any training phases may benefit from similar bridging strategies.

## One-Sentence Claim

Midtraining works as distributional bridging: mixing specialized and general data before posttraining gives a better initialization for distant target domains while reducing forgetting.

## Problem

Midtraining is widely used in LLM development, but it is unclear whether it helps because of extra memorization, domain adaptation, better posttraining initialization, or some interaction with training timing and mixture weights.

## Core Contribution

The paper gives a controlled study of midtraining as a bridge between pretraining and posttraining distributions, showing that benefits depend on domain distance, proximity to target data, timing, and mixture weight.

## Method

It runs controlled pretraining/midtraining/posttraining experiments across specialized domains such as code and math, compares midtraining to continued pretraining, measures forgetting on general pretraining data, and analyzes start time and mixture weight.

## Experiments and Evidence

The abstract reports that midtraining gains are largest for domains far from general pretraining data, outperform continued specialized pretraining in code/math, mitigate forgetting, and reveal a plasticity window: early specialized data can use high mixture weights, while late introduction requires lower weights.

## Full-Text Upgrade

The full text defines midtraining as an intermediate phase mixing general pretraining data with specialized distributions before SFT/posttraining. The central mechanism is initialization: midtraining changes the starting point for posttraining so the model can move toward the target with less gradient conflict and less forgetting of the general pretraining distribution.

The empirical design varies domains, mixture ratios, and timing. The paper introduces a token-level proximity advantage metric measuring how much a midtraining mixture moves closer to the downstream target relative to continued C4 pretraining. Code-focused midtraining helps code tasks, math-focused midtraining helps math reasoning, and mismatched midtraining can fail. The timing finding is especially important: late insertion of specialized data appears outside a plasticity window, so increasing specialized-data mixture later cannot fully compensate.

## Limits and Failure Modes

Limits to watch: controlled pretraining experiments may not fully capture frontier-scale training; proximity metrics are proxies; mixture/timing conclusions may vary by architecture and optimizer; and the study focuses on one-stage midtraining rather than full industrial multi-stage curricula.

## Deep Themes

- Training phases should be treated as distributional transitions, not isolated stages.
- Specialization works best when the model is guided gradually toward distant domains.
- Plasticity windows constrain when data can shape capability.

## Subthemes

- Midtraining.
- Distributional bridging.
- Domain adaptation.
- Catastrophic forgetting.
- Code and math specialization.
- Mixture timing and weight.

## Connections to Other Papers

Connects to DiReCT, Beyond Log Likelihood, and h1 as training-procedure papers where phase, curriculum, and model state determine what data or objective is useful.

## Notes for Cross-Paper Synthesis

Midtraining adds a strong training-phase theme: capability development depends on the path between distributions, not just the final target data or objective.
