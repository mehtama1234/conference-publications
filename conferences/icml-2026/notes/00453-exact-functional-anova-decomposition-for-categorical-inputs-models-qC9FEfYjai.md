# Exact Functional ANOVA Decomposition for Categorical Inputs Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: qC9FEfYjai
- Authors: Baptiste Ferrere; Nicolas Bousquet; Fabrice Gamboa; Jean-Michel Loubes; Joseph Muré
- Primary area: general_machine_learning->everything_else
- Keywords: trustworthy machine learning;interpretability;functional ANOVA decomposition;categorical data;discrete fourier analysis
- Source URL: https://openreview.net/forum?id=qC9FEfYjai
- PDF URL: https://openreview.net/pdf?id=qC9FEfYjai

## Abstract

Functional ANOVA offers a principled framework for interpretability by decomposing a model’s prediction into main effects and higher-order interactions. For independent features, this decomposition is well-defined, strongly linked with SHAP values, and serves as a cornerstone of additive explainability. However, the lack of an explicit closed-form expression for general dependent distributions has forced practitioners to rely on costly sampling-based approximations. We completely resolve this limitation for categorical inputs. By bridging functional analysis with the extension of discrete Fourier analysis, we derive a closed-form decomposition without any assumption. Our formulation is computationally very efficient. It seamlessly recovers the classical independent case and extends to arbitrary dependence structures, including distributions with non-rectangular support. Furthermore, leveraging the intrinsic link between SHAP and ANOVA under independence, our framework yields a natural generalization of SHAP values for the general categorical setting.

## One-Sentence Claim

For categorical-input models, functional ANOVA can be computed exactly under arbitrary feature dependence by extending discrete Fourier analysis, yielding efficient interaction decompositions and a natural SHAP generalization.

## Problem

Functional ANOVA decomposes model predictions into main effects and interactions, making it a core tool for additive interpretability. Under independent features the decomposition is well understood and closely linked to SHAP values, but real categorical features are often dependent and may have non-rectangular support.

Without a closed-form decomposition for general dependent distributions, practitioners rely on costly sampling approximations. This limits exact interpretability for many real categorical domains.

## Core Contribution

The paper completely resolves the dependent categorical case by bridging functional analysis with an extension of discrete Fourier analysis. It derives a closed-form functional ANOVA decomposition without independence assumptions.

The framework recovers the classical independent case, handles arbitrary dependence and non-rectangular support, and yields a natural generalization of SHAP values for categorical settings beyond independence.

## Method

The method extends discrete Fourier analysis to categorical feature spaces under general distributions. This provides a basis/decomposition that respects the actual support and dependence structure rather than pretending features vary independently.

By deriving closed-form terms for main effects and higher-order interactions, the framework avoids Monte Carlo approximations and gives efficient exact computation for categorical models.

## Experiments and Evidence

The abstract emphasizes theoretical and computational evidence: an exact closed-form decomposition, efficient computation, recovery of the independent case, extension to arbitrary dependence, and a SHAP-style generalization.

Full-paper reading should verify algorithmic complexity, implementation details, examples on dependent categorical datasets, and how the generalized SHAP values compare with standard interventional or observational SHAP variants.

## Limits and Failure Modes

The result is specialized to categorical inputs. Continuous or mixed continuous-categorical settings may need discretization or separate theory, and high-order interactions can still be numerous even when each term is exactly computable.

Interpretability also depends on whether users can understand interaction decompositions under dependence. Exactness solves the mathematical problem but not necessarily the human-factors problem of communicating complex effects.

## Deep Themes

- Exact interpretability under dependence: explanation methods must respect real feature distributions.
- Fourier structure for categorical models: discrete harmonic analysis becomes an explainability engine.
- SHAP beyond independence: attribution needs a principled dependent-feature generalization.
- Closed-form over sampling: exact decomposition reduces approximation uncertainty in explanations.

## Subthemes

- Non-rectangular support is common in real categorical data.
- Main effects and interactions are distribution-dependent quantities.
- Sampling approximations can obscure exact attribution structure.
- Trustworthy ML needs mathematically well-defined explanation targets.

## Connections to Other Papers

This paper connects to Verified SHAP and NS/IF attribution through exact or theoretically grounded explanations. Verified SHAP uses neural-network verification to bound Shapley values; this paper gives exact ANOVA/SHAP-style decompositions for categorical dependence.

It also relates to fairness and annotation papers because dependent categorical features often occur in social data where naive independent-feature explanations can mislead.

## Notes for Cross-Paper Synthesis

The synthesis point is that interpretability is becoming more distribution-aware. Explanation methods are being rebuilt to respect dependence, exactness, and verifiability instead of relying on convenient independence assumptions.
