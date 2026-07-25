# Robust Contextual Optimization with Missing Covariates

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 37KrsS7g7c
- Authors: Qingyuan Xu; Ruiwei Jiang
- Primary area: optimization
- Keywords: Contextual Stochastic Optimization;Missing Data;Data-driven Decision Making;Distributionally Robust Optimization
- Source URL: https://openreview.net/forum?id=37KrsS7g7c
- PDF URL: https://openreview.net/pdf?id=37KrsS7g7c

## Abstract

Modern decision-making increasingly relies on contextual features (covariates) to improve optimization under uncertainty. In practice, however, such covariates are often only partially observed due to, e.g., data source heterogeneity or costly data collection. Nonetheless, most existing methods assume fully observed historical data and can become unreliable when this assumption is violated. We address this gap by proposing a distributionally robust optimization approach that exploits incomplete covariates to produce robust decisions without imputing a complete dataset. Our method builds ambiguity sets from the observed partial data and incorporates the general structure of the missingness mechanism, ensuring candidate distributions remain consistent with what is observed. Across settings with discrete or continuous covariates and outcomes, we derive tractable reformulations and establish finite-sample out-of-sample performance guarantees. Empirical results across a range of contextual decision-making tasks demonstrate that the proposed integrated approach consistently outperforms state-of-the-art baselines, including various impute-then-optimize pipelines, in both out-of-sample performance and reliability.

## One-Sentence Claim

Robust contextual optimization can use partially observed covariates directly by building ambiguity sets consistent with missing-data mechanisms, avoiding brittle impute-then-optimize pipelines.

## Problem

Contextual stochastic optimization typically assumes fully observed historical covariates, but real decision systems often have missing features due to heterogeneous data sources, expensive measurement, or incomplete collection. Imputing missing covariates can introduce unreliable downstream decisions.

## Core Contribution

The paper proposes a distributionally robust optimization framework that constructs ambiguity sets from partial covariate observations and missingness structure, then derives tractable reformulations and finite-sample guarantees.

## Method

Instead of completing the historical dataset, the method constrains candidate distributions to remain consistent with observed partial data and the assumed general structure of missingness. It handles discrete and continuous covariates/outcomes through reformulations suitable for contextual decision-making.

## Experiments and Evidence

The abstract reports empirical gains across contextual decision-making tasks, outperforming state-of-the-art baselines including impute-then-optimize methods in both out-of-sample performance and reliability.

## Limits and Failure Modes

No confident local PDF/arXiv match yet, so details still need checking: assumptions on the missingness mechanism, ambiguity-set conservatism, computational scaling, and how much performance depends on knowing the missingness structure.

## Deep Themes

- Decision robustness requires modeling data incompleteness rather than hiding it behind imputation.
- Optimization pipelines are becoming more statistically honest about observation processes.
- Reliability can improve when uncertainty about covariates is part of the decision problem.

## Subthemes

- Contextual stochastic optimization.
- Missing covariates.
- Distributionally robust optimization.
- Partial-data ambiguity sets.
- Impute-then-optimize alternatives.

## Connections to Other Papers

Connects to LIMSSR, which also treats missing observations as a central modeling problem rather than an inconvenience. It also links to robustness and deployment-oriented papers where data collection assumptions fail in realistic settings.

## Notes for Cross-Paper Synthesis

This paper adds an operations/optimization version of the missing-data theme: robust systems should preserve uncertainty from data acquisition through to final decisions.
