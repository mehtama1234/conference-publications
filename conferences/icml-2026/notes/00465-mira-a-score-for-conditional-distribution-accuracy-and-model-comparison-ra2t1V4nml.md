# MIRA: A Score for Conditional Distribution Accuracy and Model Comparison

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: ra2t1V4nml
- Authors: Sammy Nasser Sharief; Justine Zeghal; Gabriel Missael Barco; Pablo Lemos; Yashar Hezaveh; Laurence Perreault-Levasseur
- Primary area: probabilistic_methods->everything_else
- Keywords: Bayesian Inference;Bayesian Model Comparsion;Sample-based Metrics
- Source URL: https://openreview.net/forum?id=ra2t1V4nml
- PDF URL: https://openreview.net/pdf?id=ra2t1V4nml

## Abstract

We introduce MIRA, a sample-based score for assessing the accuracy of a candidate conditional distribution using only joint samples from the true data-generating process. Relying on the principle that distributions coincide if they assign equal probability mass to all regions, we derive an analytic expression for the MIRA statistic, whose average defines the MIRA score. This formulation further allows us to compute theoretical reference values and uncertainty estimates when the candidate distribution matches the true one. This framework enables model comparison by quantifying the alignment between the conditional distribution of a candidate model and the true data generating process. Consequently, MIRA enables Bayesian model comparison through direct posterior validation, bypassing the challenging evidence computation. We demonstrate its effectiveness across several toy problems and Bayesian inference tasks.

## One-Sentence Claim

MIRA evaluates candidate conditional distributions from joint samples by measuring regional probability-mass agreement, enabling posterior validation and Bayesian model comparison without evidence computation.

## Problem

Many probabilistic models output conditional distributions, but evaluating whether those conditionals match the true data-generating process is difficult when only joint samples are available. Bayesian model comparison is especially hard because computing marginal evidence can be intractable.

The paper targets sample-based conditional-distribution validation: compare a candidate conditional model to the true process without requiring analytic likelihoods or evidence integrals.

## Core Contribution

MIRA is a sample-based score derived from the principle that two distributions are equal if they assign equal probability mass to all regions. The paper derives an analytic expression for a MIRA statistic whose average defines the score.

The framework provides theoretical reference values and uncertainty estimates when the candidate conditional matches the true distribution. This turns conditional model checking into a calibrated comparison tool.

## Method

Given joint samples from the true process and a candidate conditional distribution, MIRA evaluates how well the candidate assigns mass across regions. The score aggregates the analytic statistic over samples.

Because reference values and uncertainty estimates are available under correct specification, MIRA can be used not only to rank models but to assess whether observed score differences are meaningful.

## Experiments and Evidence

The abstract reports demonstrations across toy problems and Bayesian inference tasks. It claims MIRA enables Bayesian model comparison through direct posterior validation, bypassing evidence computation.

Full-paper reading should verify sample complexity, dimensional sensitivity, region construction or kernel choices, calibration of uncertainty estimates, and performance against existing posterior predictive or simulation-based calibration methods.

## Limits and Failure Modes

Distribution comparison from finite samples can be difficult in high dimensions. MIRA's power may depend on how regions are represented and whether sample sizes are sufficient to detect local conditional errors.

Bypassing evidence computation is valuable, but posterior validation is not identical to model evidence; users need to understand what model-comparison question MIRA answers.

## Deep Themes

- Conditional distribution validation: evaluate probabilistic models where predictions are distributions, not points.
- Sample-based Bayesian comparison: posterior accuracy can be tested directly from joint samples.
- Calibrated scoring: reference values and uncertainty estimates make model comparison statistically interpretable.
- Regional mass agreement: distribution equality is operationalized through probability assigned to regions.

## Subthemes

- Joint samples can replace inaccessible evidence integrals.
- Candidate conditionals are judged against the true data-generating process.
- Uncertainty estimates are necessary for comparing close models.
- Toy and Bayesian inference tasks test calibration and discrimination.

## Connections to Other Papers

MIRA connects to uncertainty and evaluation work, including ambiguity-averse MDPs and CV relative instability. It also relates to benchmark papers because it is an evaluator, but for probabilistic conditionals rather than generated code or apps.

It complements causal and Bayesian-method papers by focusing on whether inferred conditional distributions are accurate enough for downstream decisions.

## Notes for Cross-Paper Synthesis

The synthesis point is evaluation of distributions rather than outputs. As ML systems expose posteriors, policies, and conditionals, scoring the full conditional object becomes as important as scoring a predicted label.
