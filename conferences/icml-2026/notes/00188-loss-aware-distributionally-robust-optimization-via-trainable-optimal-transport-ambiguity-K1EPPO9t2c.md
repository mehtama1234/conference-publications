# Loss-Aware Distributionally Robust Optimization via Trainable Optimal Transport Ambiguity Sets

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: K1EPPO9t2c
- Authors: Jonas Ohnemus; Marta Fochesato; Riccardo Zuliani; John Lygeros
- Primary area: optimization->nonconvex
- Keywords: Bilevel optimization;DRO;nonsmooth optimization;optimal transport
- Source URL: https://openreview.net/forum?id=K1EPPO9t2c
- PDF URL: https://openreview.net/pdf?id=K1EPPO9t2c

## Abstract

Optimal-transport distributionally robust optimization (OT-DRO) robustifies data-driven decision-making under uncertainty by capturing the sampling-induced statistical error via optimal transport ambiguity sets. The standard OT-DRO pipeline consists of a two-step procedure, where the ambiguity set is first designed and subsequently embedded into the downstream OT-DRO problem. However, this separation between uncertainty quantification and optimization may lead to excessive conservatism. We introduce an end-to-end pipeline to automatically learn decision-focused ambiguity sets for OT-DRO problems, where the loss function informs the shape of the ambiguity set, leading to less conservative decisions whose distributional robustness is enforced via data-driven bootstrapping. We formulate the learning problem as a bilevel optimization program and solve it via a hypergradient-based method. By leveraging the recently introduced nonsmooth conservative implicit function theorem, we establish convergence to a critical point of the bilevel problem. We present experiments validating our method on standard portfolio optimization and linear regression tasks.

## One-Sentence Claim

The paper learns loss-aware optimal-transport ambiguity sets end to end for less conservative distributionally robust decisions.

## Problem

Standard OT-DRO first designs an ambiguity set and then solves the downstream robust optimization problem, but separating uncertainty quantification from the loss can make decisions overly conservative.

## Core Contribution

The paper formulates decision-focused ambiguity-set learning as a bilevel optimization problem, trains OT ambiguity sets informed by the downstream loss, and proves convergence to critical points using nonsmooth conservative implicit-function theory.

## Method

The method uses data-driven bootstrapping to enforce robustness, optimizes ambiguity-set parameters through hypergradients in a bilevel program, and shapes uncertainty sets according to the downstream loss landscape.

## Experiments and Evidence

The abstract reports validation on portfolio optimization and linear regression tasks, showing less conservative but still robust decisions.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: ambiguity parameterization, bootstrap procedure, hypergradient stability, nonconvex/nonsmooth assumptions, baseline comparisons, and out-of-sample robustness metrics.

## Deep Themes

- Robustness should be decision-focused rather than detached from the loss.
- Ambiguity sets can be learned instead of manually specified.
- Bilevel optimization connects uncertainty modeling with downstream action quality.

## Subthemes

- Distributionally robust optimization.
- Optimal transport.
- Bilevel optimization.
- Hypergradients.
- Nonsmooth analysis.
- Portfolio optimization.

## Connections to Other Papers

Connects to robust optimization and uncertainty-estimation papers through loss-aware risk control, and to data-selection/valuation work where selection criteria are optimized for downstream utility.

## Notes for Cross-Paper Synthesis

This paper reinforces a decision-centered theme: uncertainty representations are most useful when shaped by the loss and deployment decision they will actually support.
