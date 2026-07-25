# Sharp Inequalities between Total Variation and Hellinger Distances for Gaussian Mixtures

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: ihMB4kA2SQ
- Authors: Joonhyuk Jung; Chao Gao
- Primary area: theory->learning_theory
- Keywords: Gaussian mixture model;total variation distance;Hellinger distance;entropic characterization;empirical Bayes
- Source URL: https://openreview.net/forum?id=ihMB4kA2SQ
- PDF URL: https://openreview.net/pdf?id=ihMB4kA2SQ

## Abstract

We study the relation between the total variation (TV) and Hellinger distances between two Gaussian location mixtures. Our first result establishes a general upper bound: for any two mixing distributions supported on a compact set, the Hellinger distance between the two mixtures is controlled by the TV distance raised to a power $1-o(1)$, where the $o(1)$ term is of order $1/\log\log(1/\mathrm{TV})$. We also construct two sequences of mixing distributions that demonstrate the sharpness of this bound. Taken together, our results resolve an open problem raised in Jia et al. (2023) and thus lead to an entropic characterization of learning Gaussian mixtures in total variation. Our inequality also yields optimal robust estimation of Gaussian mixtures in Hellinger distance, which has a direct implication for bounding the minimax regret of empirical Bayes under Huber contamination.

## One-Sentence Claim

Sharp TV-to-Hellinger inequalities for Gaussian location mixtures resolve an open problem and yield entropic characterizations and robust-estimation consequences.

## Problem

Learning Gaussian mixtures depends on how different statistical distances relate. Total variation and Hellinger distances are both central, but for Gaussian location mixtures their sharp relationship under compactly supported mixing distributions was unresolved.

The paper asks how tightly Hellinger distance between mixtures can be controlled by TV distance between mixing distributions, and whether that control is optimal.

## Core Contribution

The paper proves a general upper bound: for two compactly supported mixing distributions, the Hellinger distance between the induced Gaussian mixtures is bounded by TV raised to a power 1-o(1), with the o(1) term of order 1/log log(1/TV).

It also constructs two sequences of mixing distributions showing sharpness. This resolves an open problem from Jia et al. and yields an entropic characterization of learning Gaussian mixtures in TV.

## Method

The analysis studies smoothing through the Gaussian location-mixture operator and quantifies how TV perturbations in mixing distributions translate into Hellinger perturbations in mixture densities.

Sharpness constructions show that the exponent cannot be substantially improved, making the inequality an exact boundary rather than a loose comparison.

## Experiments and Evidence

Evidence reported in the abstract:

- General upper bound for compactly supported mixing distributions.
- Sharpness shown by two constructed mixing-distribution sequences.
- Resolution of an open problem from Jia et al. (2023).
- Entropic characterization of Gaussian mixture learning in total variation.
- Optimal robust estimation of Gaussian mixtures in Hellinger distance.
- Implication for minimax regret of empirical Bayes under Huber contamination.

Source depth is abstract/metadata only; this is theory-heavy and needs full-paper checking for assumptions, constants, and proof technique.

## Limits and Failure Modes

- The result targets Gaussian location mixtures with compact support.
- Distance inequalities may not directly produce computationally efficient estimators.
- Asymptotic terms like 1/log log(1/TV) can matter in finite regimes.
- Extensions to covariance mixtures or non-Gaussian kernels may require new arguments.

## Deep Themes

**Metric translation controls learnability.** Understanding one statistical distance through another clarifies sample complexity and robustness.

**Sharp inequalities are infrastructure.** The result supports downstream estimation and empirical Bayes guarantees.

**Smoothing hides but does not erase complexity.** Gaussian convolution changes distance geometry in a precisely quantified way.

## Subthemes

- Gaussian location mixtures.
- Total variation versus Hellinger distance.
- Entropic characterization.
- Robust mixture estimation.
- Empirical Bayes under contamination.

## Connections to Other Papers

Connects to Noisy Sample Compression, DiScoFormer, Distribution Transformers, CreDRO, and robust distribution learning papers. It provides mathematical infrastructure for probabilistic learning under contamination and mixture structure.

## Notes for Cross-Paper Synthesis

This paper reinforces the theory-foundations layer: many practical uncertainty and robustness claims depend on precise distance relationships between distributions.
