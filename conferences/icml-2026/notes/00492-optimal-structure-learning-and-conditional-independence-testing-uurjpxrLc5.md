# Optimal structure learning and conditional independence testing

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: uurjpxrLc5
- Authors: Ming Gao; Yuhao Wang; Bryon Aragam
- Primary area: probabilistic_methods->structure_learning
- Keywords: structure learning;conditional independence testing;minimax rate;optimal sample complexity;graphical model;Bayesian network
- Source URL: https://openreview.net/forum?id=uurjpxrLc5
- PDF URL: https://openreview.net/pdf?id=uurjpxrLc5

## Abstract

We establish a fundamental connection between optimal structure learning and optimal conditional independence testing by showing that the minimax optimal rate for structure learning problems is determined by the minimax rate for conditional independence testing in these problems. This is accomplished by establishing a general reduction between these two problems in the case of poly-forests, and demonstrated by deriving optimal rates for several examples, including Bernoulli, Gaussian and nonparametric models. Furthermore, we show that the optimal algorithm in these settings is a suitable modification of the PC algorithm. This theoretical finding provides a unified framework for analyzing the statistical complexity of structure learning through the lens of minimax testing.

## One-Sentence Claim

For poly-forest graphical models, the minimax rate of structure learning is determined by the minimax rate of conditional independence testing, yielding optimal modified-PC algorithms across Bernoulli, Gaussian, and nonparametric settings.

## Problem

Structure learning seeks to recover graphical or Bayesian-network structure from samples. Conditional independence testing is a core primitive in constraint-based algorithms, but the precise statistical relationship between optimal testing and optimal structure learning is not fully unified.

The paper asks whether structure-learning sample complexity can be characterized through the minimax complexity of CI testing in the same model class.

## Core Contribution

The paper establishes a general reduction between structure learning and conditional independence testing for poly-forests. It shows that the minimax optimal rate for structure learning is determined by the minimax rate for CI testing.

It then derives optimal rates for Bernoulli, Gaussian, and nonparametric models and shows that a suitable modification of the PC algorithm is optimal in these settings.

## Method

The theoretical method reduces structure learning to a collection or sequence of conditional independence testing problems. Conversely, hardness of CI testing transfers to structure learning, tying their minimax rates.

The modified PC algorithm uses CI tests tuned to the model class and sample complexity regime. Poly-forest structure provides enough graph constraint to make the reduction precise.

## Experiments and Evidence

The abstract is theory-focused. Evidence consists of the reduction, minimax rate derivations for multiple model families, and optimality of modified PC procedures.

Full-paper reading should verify poly-forest assumptions, rate dependencies on node count and graph degree, CI test choices, and whether empirical simulations support finite-sample behavior.

## Limits and Failure Modes

Poly-forests are structured graphical models; general dense or cyclic causal graphs may not obey the same reduction. CI testing can also be fragile in finite samples, especially in high dimensions or with latent variables.

The result clarifies sample complexity under assumptions, but practical structure learning still faces model misspecification, faithfulness violations, and measurement noise.

## Deep Themes

- Structure learning through testing primitives: graph recovery complexity is governed by CI test complexity.
- Minimax unification: optimal rates become a shared property across statistical tasks.
- PC algorithm rehabilitation: constraint-based methods can be optimal with the right modifications.
- Model-class-specific rates: Bernoulli, Gaussian, and nonparametric settings instantiate the general theorem differently.

## Subthemes

- Poly-forests provide a tractable reduction setting.
- Conditional independence is the statistical bottleneck.
- Optimal algorithms need test calibration to the distribution family.
- Structure learning and causal discovery depend on finite-sample CI reliability.

## Connections to Other Papers

This paper connects to local covariate selection and evolutionary causal selection through graphical identification. It also relates to MIRA and feasible payoff estimation as statistical problems where the target is a structured object, not a scalar prediction.

It strengthens the theory theme that downstream learning rates can often be reduced to a simpler primitive.

## Notes for Cross-Paper Synthesis

The synthesis point is primitive-based complexity. Structure learning is only as easy as the conditional independence tests it needs.
