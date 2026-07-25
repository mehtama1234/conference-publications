# Learning Credal Ensembles via Distributionally Robust Optimization

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: cRTbp2pv7X
- Authors: Kaizheng Wang; Ghifari Adam Faza; Fabio Cuzzolin; Siu Lun Chau; David Moens; Hans Hallez
- Primary area: probabilistic_methods->everything_else
- Keywords: Uncertainty Quantification;Epistemic Uncertainty;Credal Sets;Classification
- Source URL: https://openreview.net/forum?id=cRTbp2pv7X
- PDF URL: https://openreview.net/pdf?id=cRTbp2pv7X

## Abstract

Credal predictors are epistemic-uncertainty-aware models that produce a convex set of probabilistic predictions. They provide a principled framework for quantifying predictive epistemic uncertainty (EU) and have been shown to improve model robustness across a range of settings. However, most state-of-the-art (SOTA) methods primarily define EU as disagreement induced by random training initializations, which mainly reflects sensitivity to optimization randomness rather than uncertainty from more substantive sources. In response, we formulate EU as disagreement between models trained under different degrees of relaxation of the i.i.d. assumption between the training and test distributions. Building on this idea, we propose *CreDRO*, which learns an ensemble of plausible models via distributionally robust optimization. As a result, CreDRO captures EU arising not only from training randomness but also from informative disagreement due to potential train–test distribution shifts. Empirically, CreDRO consistently outperforms SOTA credal approaches on downstream tasks, including out-of-distribution detection on extensive benchmarks and selective classification in medical settings.

## One-Sentence Claim

CreDRO learns credal ensembles whose epistemic uncertainty reflects plausible train-test distribution shifts rather than only random initialization disagreement.

## Problem

Credal predictors output convex sets of probabilistic predictions to represent epistemic uncertainty. Most current credal approaches define uncertainty as disagreement among models trained from different random seeds, which mainly measures optimization randomness rather than uncertainty from distribution shift.

The paper asks how to make credal uncertainty reflect substantive ambiguity about the relation between training and test distributions.

## Core Contribution

The paper formulates epistemic uncertainty as disagreement among models trained under different relaxations of the i.i.d. assumption. It proposes CreDRO, which learns an ensemble of plausible models via distributionally robust optimization.

CreDRO captures uncertainty from possible train-test shifts and improves downstream OOD detection and selective classification, including medical settings.

## Method

CreDRO constructs model diversity through DRO rather than random initialization. Each ensemble member corresponds to a different plausible relaxation or robust view of the data distribution. The convex hull of their predictions forms the credal prediction set.

This makes disagreement informative about distributional uncertainty, not only training noise.

## Experiments and Evidence

Evidence reported in the abstract:

- Credal ensemble learned by DRO.
- Epistemic uncertainty defined through relaxation of i.i.d. assumptions.
- Consistent improvement over state-of-the-art credal approaches.
- Extensive OOD detection benchmarks.
- Selective classification in medical settings.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: DRO uncertainty sets, ensemble construction, credal metrics, and calibration under shift.

## Limits and Failure Modes

- DRO uncertainty sets can be conservative or miss real shifts.
- Ensembles add training and inference cost.
- Credal sets can be difficult for users to interpret.
- Medical selective classification needs subgroup and clinical workflow validation.

## Deep Themes

**Epistemic uncertainty should come from plausible worlds.** CreDRO makes disagreement reflect distributional alternatives.

**Credal prediction is robust decision infrastructure.** Convex prediction sets support OOD detection and abstention.

**Random seeds are a weak uncertainty source.** The paper replaces initialization variance with distributional perturbation.

## Subthemes

- Credal ensembles.
- Distributionally robust optimization.
- Epistemic uncertainty under shift.
- OOD detection.
- Medical selective classification.

## Connections to Other Papers

Connects to Bulk-Calibrated Credal Sets, ROCP, TRECA, Distribution Transformers, and uncertainty-aware decision papers. It also links to DISCO and OOD robustness work because distribution shift is explicitly modeled.

## Notes for Cross-Paper Synthesis

CreDRO advances the uncertainty theme by asking whether ensemble disagreement is causally meaningful or merely optimizer noise.
