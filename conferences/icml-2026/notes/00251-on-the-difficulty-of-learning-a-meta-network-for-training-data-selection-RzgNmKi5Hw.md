# On the Difficulty of Learning a Meta-network for Training Data Selection

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: RzgNmKi5Hw
- Authors: Zilin Du; Junqi Zhao; Boyang Li
- Primary area: general_machine_learning->transfer_multitask_and_metalearning
- Keywords: Data Selection;Bi-Level Optimization;Gradient Singal-to-Noise Ratio;Hypergradient;Image Classification
- Source URL: https://openreview.net/forum?id=RzgNmKi5Hw
- PDF URL: https://openreview.net/pdf?id=RzgNmKi5Hw

## Abstract

Synthetic data are increasingly used to train neural networks, yet distributional mismatch with real data limits their effectiveness when used indiscriminately. A common strategy is to learn data weights via bi-level optimization, which we refer to as Meta-learning for Training-data Selection (MTS). Interestingly, in practice, MTS often performs below expectation. We identify two obstacles in properly training MTS: a poor gradient signal-to-noise ratio (GSNR), which causes optimization difficulties, and lack of informative features that correlates with data quality. We present a mathematical analysis of MTS, which reveals the dynamics of normalized data weights and the relation between disparate data quality and poor GSNR. The analysis suggests a a simple yet effective solution: increasing the batch size. Further, we propose a set of informative features that capture the positions of training data in their distributions and training dynamics. Experiments across four benchmarks show consistent improvements, achieving average gains of 5.49\% over training without selection and 2.89\% over the strongest baseline.

## One-Sentence Claim

The paper explains why meta-learning data-selection weights often underperforms, identifying poor hypergradient signal-to-noise and weak data-quality features as bottlenecks, and improves MTS with larger batches and better features.

## Problem

Synthetic data can help training, but distribution mismatch means indiscriminate use is harmful; learned data weighting via bilevel meta-selection is attractive yet often unreliable in practice.

## Core Contribution

The paper analyzes Meta-learning for Training-data Selection, links disparate data quality to poor gradient signal-to-noise ratio, and proposes both a batch-size remedy and informative distribution/training-dynamics features.

## Method

The authors mathematically analyze normalized data-weight dynamics and hypergradient GSNR, then use larger batches and data-position/training-dynamics features to make the meta-network's quality signal more learnable.

## Experiments and Evidence

The abstract reports experiments across four benchmarks with average gains of 5.49% over training without selection and 2.89% over the strongest baseline.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: benchmark identities, synthetic-data generation, batch-size cost, feature definitions, hypergradient estimator, and whether results transfer beyond image classification.

## Deep Themes

- Data selection fails when the meta-objective has weak gradient signal.
- Training-data quality needs informative, learnable features.
- Bilevel optimization can be limited by statistical signal rather than objective design alone.

## Subthemes

- Synthetic data.
- Training-data selection.
- Bilevel optimization.
- Hypergradients.
- Gradient signal-to-noise ratio.
- Image classification.

## Connections to Other Papers

Connects to Sequential Data Values, HOBIT, power-law compositional reasoning, and FAC Synthesis through data curation as an optimization problem.

## Notes for Cross-Paper Synthesis

This paper adds a meta-selection diagnostics theme: data-selection methods need enough gradient signal and feature information before their learned weighting can outperform simpler heuristics.
