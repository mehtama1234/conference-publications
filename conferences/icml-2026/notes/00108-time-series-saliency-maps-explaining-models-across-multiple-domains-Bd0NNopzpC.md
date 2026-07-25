# Time series saliency maps: Explaining models across multiple domains

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: Bd0NNopzpC
- Authors: Christodoulos Kechris; Jonathan Dan; David Atienza
- Primary area: applications->time_series
- Keywords: Time series models;Interpretability;Saliency Map;Integrated Gradients
- Source URL: https://openreview.net/forum?id=Bd0NNopzpC
- PDF URL: https://openreview.net/pdf?id=Bd0NNopzpC

## Abstract

Traditional saliency map methods, popularized in computer vision, highlight individual input points that contribute most to a model's output. However, in the context of time series, they offer limited insights because semantically meaningful features are often found in other domains. Thus, we introduce in this paper Cross-domain Integrated Gradients, a generalization of Integrated Gradients that enables feature attributions in any domain formulated as an invertible, differentiable transformation of the time domain. Our derivation extends Integrated Gradients into complex-valued domains, enabling frequency-based attributions, while preserving path independence and completeness. We validate our method via controlled mechanistic experiments, quantitative faithfulness and perturbation-stability tests, and real-world case studies. Across wearable heart-rate extraction, EEG-based seizure detection, and zero-shot forecasting, our proposed Cross-domain Integrated Gradients approach identifies whether predictions rely on heart-rate frequencies or interference, epileptic sources or artifacts, and trend or seasonal components, revealing model behaviour that time-domain saliency does not capture. We release an open-source library with TensorFlow, native PyTorch, and Captum support for plug-and-play cross-domain explainability of time-series models.

## One-Sentence Claim

Cross-domain Integrated Gradients extends saliency maps to transformed domains, such as frequency space, so time-series explanations can target semantically meaningful features.

## Problem

Pointwise time-domain saliency often fails for time series because important signals may be defined in frequency, seasonal, source, or other transformed domains.

## Core Contribution

The paper generalizes Integrated Gradients to any invertible differentiable transformation of the time domain, including complex-valued domains for frequency attributions.

## Method

Cross-domain Integrated Gradients computes attributions after transforming the time signal into another domain while preserving key Integrated Gradients properties such as path independence and completeness.

## Experiments and Evidence

The abstract reports controlled mechanistic tests, faithfulness and perturbation-stability evaluations, and case studies in wearable heart-rate extraction, EEG seizure detection, and zero-shot forecasting.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: transformation choices, complex-gradient implementation, baseline selection, and failure cases when multiple domains interact.

## Deep Themes

- Interpretability should operate in the domain where features are semantically meaningful.
- Attribution methods can preserve formal guarantees across transformations.
- Time-series explanations need frequency/source/seasonal views, not only raw timestamps.

## Subthemes

- Time-series interpretability.
- Integrated Gradients.
- Frequency-domain attribution.
- Complex-valued saliency.
- EEG and wearables.
- Forecasting explanations.

## Connections to Other Papers

Connects to SVD interpretability, LOES, spectral causal discovery, and HyperDepth through spectral/domain-specific interpretability.

## Notes for Cross-Paper Synthesis

This paper reinforces a representation-domain theme: explanations become more useful when expressed in the transformed basis where the phenomenon lives.
