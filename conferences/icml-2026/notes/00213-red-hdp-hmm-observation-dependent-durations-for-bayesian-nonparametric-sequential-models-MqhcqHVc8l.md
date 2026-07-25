# RED-HDP-HMM: Observation-Dependent Durations for Bayesian Nonparametric Sequential Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: MqhcqHVc8l
- Authors: Mikołaj Słupiński; Piotr Lipinski
- Primary area: probabilistic_methods->bayesian_models_and_methods
- Keywords: Hidden Markov Models;Bayesian Nonparametric Modeling;Recurrent Modeling
- Source URL: https://openreview.net/forum?id=MqhcqHVc8l
- PDF URL: https://openreview.net/pdf?id=MqhcqHVc8l

## Abstract

The Hierarchical Dirichlet Process Hidden Markov Model (HDP-HMM) is a Bayesian nonparametric extension of the classical Hidden Markov Model, well-suited for learning from (spatio-)temporal data. To relax the restrictive geometric assumption on state durations, the HDP Hidden Semi-Markov Model was introduced. However, both models assume stationary state durations, which limits their expressive power. In this work, we extend the HDP-HMM framework by incorporating recurrent explicit duration modeling, resulting in a more general and flexible model: the Recurrent Explicit Duration HDP-HMM (RED-HDP-HMM). We propose a Gibbs sampling method for efficient inference in this model. Empirical results on both synthetic and real-world segmentation tasks demonstrate that RED-HDP-HMM consistently outperforms the disentangled sticky HDP-HMM and the standard sticky HDP-HMM.

## One-Sentence Claim

RED-HDP-HMM extends Bayesian nonparametric HMMs with recurrent explicit duration modeling so state durations can depend on observations rather than remain stationary.

## Problem

HDP-HMMs and HDP-HSMMs are useful for temporal data but impose restrictive geometric or stationary duration assumptions that limit expressiveness.

## Core Contribution

The paper introduces Recurrent Explicit Duration HDP-HMM, a more flexible Bayesian nonparametric sequential model, and an efficient Gibbs sampler for inference.

## Method

RED-HDP-HMM incorporates observation-dependent recurrent duration dynamics into the HDP-HMM family, relaxing stationary state-duration assumptions while retaining nonparametric state flexibility.

## Experiments and Evidence

The abstract reports consistent improvements over disentangled sticky HDP-HMM and standard sticky HDP-HMM on synthetic and real-world segmentation tasks.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: recurrent duration parameterization, sampler mixing, segmentation datasets, state-count behavior, computational scaling, and robustness to misspecified duration dynamics.

## Deep Themes

- Duration modeling is central for realistic temporal segmentation.
- Bayesian nonparametric models remain useful when extended with learned recurrence.
- Observation-dependent time structure improves sequential expressiveness.

## Subthemes

- HDP-HMM.
- Hidden semi-Markov models.
- Explicit duration modeling.
- Gibbs sampling.
- Temporal segmentation.
- Bayesian nonparametrics.

## Connections to Other Papers

Connects to CoCLD, SDEVI, and irregular-sequence papers through richer temporal dynamics, but from a probabilistic nonparametric rather than neural continuous-time angle.

## Notes for Cross-Paper Synthesis

RED-HDP-HMM adds a duration-specific temporal theme: real sequences often require state persistence to depend on observations rather than a fixed stationary clock.
