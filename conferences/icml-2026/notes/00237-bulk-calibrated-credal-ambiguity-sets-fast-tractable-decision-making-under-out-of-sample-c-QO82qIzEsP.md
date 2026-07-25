# Bulk-Calibrated Credal Ambiguity Sets: Fast, Tractable Decision Making under Out-of-Sample Contamination

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: QO82qIzEsP
- Authors: Mengqi Chen; Thomas Berrett; Theodoros Damoulas; Michele Caprio
- Primary area: probabilistic_methods
- Keywords: Distributional Robustness;Imprecise Probability;Stochastic Optimisation;Huber Contamination
- Source URL: https://openreview.net/forum?id=QO82qIzEsP
- PDF URL: https://openreview.net/pdf?id=QO82qIzEsP

## Abstract

Distributionally robust optimisation (DRO) minimises the worst-case expected loss over an ambiguity set that can capture distributional shifts in out-of-sample environments. While Huber (linear-vacuous) contamination is a classical minimal-assumption model for an $\varepsilon$-fraction of arbitrary perturbations, including it in an ambiguity set can make the worst-case risk infinite and the DRO objective vacuous unless one imposes strong boundedness or support assumptions. We address these challenges by introducing bulk-calibrated credal ambiguity sets: we learn a high-mass bulk set from data while considering contamination inside the bulk and bounding the remaining tail contribution separately. This leads to a closed-form, finite $\mathrm{mean}+\sup$ robust objective and tractable linear or second-order cone programs for common losses and bulk geometries. Through this framework, we highlight and exploit the equivalence between the imprecise probability (IP) notion of upper expectation and the worst-case risk, demonstrating how IP credal sets translate into DRO objectives with interpretable tolerance levels. Experiments on heavy-tailed inventory control, geographically shifted house-price regression, and demographically shifted text classification show competitive robustness-accuracy trade-offs and efficient optimisation times, using Bayesian, frequentist, or empirical reference distributions.

## One-Sentence Claim

Bulk-calibrated credal ambiguity sets make DRO under Huber contamination finite and tractable by robustifying the learned high-mass bulk while separately bounding tail contribution.

## Problem

Huber contamination captures arbitrary out-of-sample perturbations, but naive inclusion in DRO ambiguity sets can make worst-case risk infinite unless strong support or boundedness assumptions are imposed.

## Core Contribution

The paper introduces bulk-calibrated credal ambiguity sets, links imprecise-probability upper expectation to DRO worst-case risk, and derives closed-form finite mean-plus-sup objectives with tractable LP/SOCP formulations.

## Method

The framework learns a high-mass bulk set from data, accounts for contamination within that bulk, bounds remaining tail risk separately, and supports Bayesian, frequentist, or empirical reference distributions.

## Experiments and Evidence

The abstract reports competitive robustness-accuracy tradeoffs and efficient optimization on heavy-tailed inventory control, geographically shifted house-price regression, and demographically shifted text classification.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: bulk-set calibration, epsilon selection, tail bounds, loss/geometric assumptions, LP/SOCP scalability, and sensitivity to reference-distribution misspecification.

## Deep Themes

- Robust decision-making needs ambiguity sets that are expressive but nonvacuous.
- Separating bulk and tail can tame arbitrary contamination.
- Imprecise probability offers interpretable robustness tolerances for ML decisions.

## Subthemes

- Distributional robustness.
- Credal sets.
- Huber contamination.
- Stochastic optimization.
- Upper expectation.
- Heavy-tailed and shifted data.

## Connections to Other Papers

Connects to loss-aware OT-DRO and tail-risk papers through robust decision-making under distribution shift and rare/outlier behavior.

## Notes for Cross-Paper Synthesis

This paper adds a nonvacuous-robustness theme: robust objectives must cover contamination without becoming so pessimistic that decision-making collapses.
