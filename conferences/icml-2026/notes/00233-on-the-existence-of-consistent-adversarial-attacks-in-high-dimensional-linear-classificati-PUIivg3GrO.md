# On the Existence of Consistent Adversarial Attacks in High-Dimensional Linear Classification

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: PUIivg3GrO
- Authors: Matteo Vilucchio; Lenka Zdeborová; Bruno Loureiro
- Primary area: theory->learning_theory
- Keywords: high-dimensional statistics;statistical learning theory;adversarial robustness;overparameterization
- Source URL: https://openreview.net/forum?id=PUIivg3GrO
- PDF URL: https://openreview.net/pdf?id=PUIivg3GrO

## Abstract

What fundamentally distinguishes an adversarial attack from a misclassification due to limited model expressivity or finite data? 
In this work, we investigate this question in the setting of high-dimensional binary classification, where statistical effects due to limited data availability play a central role.
We introduce a new error metric that precisely capture this distinction, quantifying model vulnerability to consistent adversarial attacks --- perturbations that preserve the ground-truth labels.
Our main technical contribution is an exact and rigorous asymptotic characterization of these metrics in both well-specified models and latent space models, revealing different vulnerability patterns compared to standard robust error measures. 
The theoretical results demonstrate that as models become more overparameterized, their vulnerability to label-preserving perturbations grows, offering theoretical insight into the mechanisms underlying model sensitivity to adversarial attacks.

## One-Sentence Claim

The paper defines consistent adversarial attacks as label-preserving perturbations and shows overparameterization increases vulnerability in high-dimensional linear classification.

## Problem

Standard robust error can conflate genuine adversarial vulnerability with misclassification from limited expressivity or finite data, obscuring what distinguishes label-preserving attacks.

## Core Contribution

The paper introduces an error metric for vulnerability to consistent adversarial attacks and gives exact asymptotic characterizations in well-specified and latent-space high-dimensional models.

## Method

The theoretical analysis studies binary linear classification in high-dimensional statistical regimes and separates perturbations that preserve ground-truth labels from ordinary errors due to model or data limitations.

## Experiments and Evidence

The abstract is theoretical. It reports different vulnerability patterns from standard robust error and shows vulnerability to label-preserving perturbations grows with overparameterization.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: exact metric, asymptotic regime, perturbation model, latent-space assumptions, finite-sample validation, and relevance to nonlinear deep networks.

## Deep Themes

- Robustness metrics must distinguish attack vulnerability from ordinary error.
- Overparameterization can increase sensitivity even in simple high-dimensional models.
- Ground-truth-preserving perturbations clarify adversarial semantics.

## Subthemes

- Adversarial robustness.
- High-dimensional statistics.
- Linear classification.
- Overparameterization.
- Robust error metrics.
- Learning theory.

## Connections to Other Papers

Connects to safety, robustness, and theory papers through sharper definitions of failure modes and to tail-risk work through distribution-sensitive risk measurement.

## Notes for Cross-Paper Synthesis

This paper adds a metric-clarity theme: robust evaluation must separate label-preserving adversarial vulnerability from baseline statistical error.
