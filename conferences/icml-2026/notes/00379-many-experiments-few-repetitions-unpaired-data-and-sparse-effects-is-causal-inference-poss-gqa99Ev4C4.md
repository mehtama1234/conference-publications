# Many Experiments, Few Repetitions, Unpaired Data, and Sparse Effects: Is Causal Inference Possible?

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: gqa99Ev4C4
- Authors: Felix Schur; Niklas Pfister; Peng Ding; Sach Mukherjee; Jonas Peters
- Primary area: general_machine_learning->causality
- Keywords: unpaired data;causal inference;lasso;sparsity;instrumental variables;mendelian randomization
- Source URL: https://openreview.net/forum?id=gqa99Ev4C4
- PDF URL: https://openreview.net/pdf?id=gqa99Ev4C4

## Abstract

In many applications, practical constraints prevent measuring covariates and outcomes on the same units, resulting in unpaired data. We study the problem of estimating causal effects under hidden confounding in the following unpaired data setting: we observe some covariates $X$ and an outcome $Y$ under different experimental conditions (environments) but do not observe them jointly -- we either observe $X$ or $Y$. Under appropriate regularity conditions, the problem can be cast as an instrumental variable (IV) regression with the environment acting as a (possibly high-dimensional) instrument. When there are many environments but only a few observations per environment, standard two-sample IV estimators fail to be consistent. We propose a GMM-type estimator based on cross-fold sample splitting of the instrument–covariate sample that also applies in standard IV settings. We prove that it is consistent as the number of environments grows but the sample size per environment remains constant. We further extend the method to sparse causal effects via $\ell_1$-regularized estimation and post-selection refitting.

## One-Sentence Claim

Causal effects can be estimated from many-environment unpaired data by treating environments as instruments and using sample-split GMM, even with few observations per environment.

## Problem

In many experiments, practical constraints prevent measuring covariates and outcomes on the same units. This creates unpaired data: one observes X or Y under different environments, but not jointly.

Under hidden confounding, standard two-sample IV estimators fail when there are many environments but only a few observations per environment. The paper asks whether consistent causal estimation is still possible in this sparse-repetition regime.

## Core Contribution

The paper casts the unpaired-data problem as an instrumental variable regression where the environment acts as a possibly high-dimensional instrument. It proposes a GMM-type estimator based on cross-fold sample splitting of the instrument-covariate sample.

It proves consistency as the number of environments grows while the per-environment sample size remains constant, and extends the method to sparse causal effects with l1-regularized estimation and post-selection refitting.

## Method

The estimator uses environments as instruments and separates the instrument-covariate sample through cross-fold splitting to avoid the inconsistency of standard two-sample IV in the many-environment/few-repetition regime.

For sparse effects, it adds l1 regularization to select relevant covariates/effects, then refits after selection to reduce regularization bias.

## Experiments and Evidence

Evidence reported in the abstract:

- Formal reduction of unpaired causal estimation to IV regression with environments as instruments.
- GMM-type estimator with cross-fold sample splitting.
- Consistency when the number of environments grows and samples per environment stay constant.
- Extension to sparse causal effects via l1 regularization and post-selection refitting.
- Applicability to standard IV settings as well.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: regularity assumptions, hidden-confounding model, asymptotic rates, and empirical demonstrations.

## Limits and Failure Modes

- IV validity of environments is a strong assumption and may fail in practice.
- Constant per-environment sample size makes finite-sample variance a serious concern.
- Sparse-effect recovery depends on design conditions for l1 regularization.
- Unpaired measurements may require careful normalization across environments.

## Deep Themes

**Experimental breadth can substitute for repetition.** Many environments provide identifying variation even when each environment is sparsely sampled.

**Causal estimation must match data logistics.** The method is built around what can actually be measured, not ideal paired samples.

**Instruments can be high-dimensional environments.** The paper turns experimental condition labels into causal leverage.

## Subthemes

- Unpaired causal data.
- Many environments, few repetitions.
- Environment-as-instrument IV.
- Sample-split GMM.
- Sparse causal effects.

## Connections to Other Papers

Connects to OU Identifiability, Source Screening, Noisy Sample Compression, Finite Test Certification, and data-governance themes. It shares the idea that structured experimental variation can compensate for missing direct observations.

## Notes for Cross-Paper Synthesis

This paper adds a causal-data logistics theme: the relevant question is often not whether ideal data exist, but whether the structure of imperfect experiments still identifies the target.
