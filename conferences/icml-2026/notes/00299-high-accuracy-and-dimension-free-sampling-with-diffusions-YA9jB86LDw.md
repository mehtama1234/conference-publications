# High-accuracy and dimension-free sampling with diffusions

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: YA9jB86LDw
- Authors: Khashayar Gatmiry; Sitan Chen; Adil Salim
- Primary area: deep_learning->generative_models_and_autoencoders
- Keywords: Theory of diffusion models;collocation;low-degree approximation;discretization analysis
- Source URL: https://openreview.net/forum?id=YA9jB86LDw
- PDF URL: https://openreview.net/pdf?id=YA9jB86LDw

## Abstract

Diffusion models have shown remarkable empirical success in sampling from rich multi-modal distributions. Their inference relies on numerically solving a certain differential equation. This differential equation cannot be solved in closed form, and its resolution via discretization typically requires many small iterations to produce *high-quality* samples.
    More precisely, prior works have shown that the iteration complexity of discretization methods for diffusion models scales polynomially in the ambient dimension and the inverse accuracy $1/\varepsilon$. In this work, we propose a new solver for diffusion models relying on a subtle interplay between low-degree approximation and the collocation method, and we prove that its iteration complexity scales *polylogarithmically* in $1/\varepsilon$, yielding the first "high-accuracy" guarantee for a diffusion-based sampler that only uses (approximate) access to the scores of the data distribution. In addition, our bound does not depend explicitly on the ambient dimension; more precisely, the dimension affects the complexity of our solver only through the *effective radius* of the support of the target distribution.

## One-Sentence Claim

A new diffusion sampler using low-degree approximation and collocation gives polylogarithmic accuracy dependence and no explicit ambient-dimension dependence beyond effective support radius.

## Problem

Diffusion sampling requires numerically solving a differential equation. Standard discretization methods need many small steps, with iteration complexity often polynomial in ambient dimension and inverse accuracy.

The paper asks whether diffusion samplers can achieve high accuracy with much better dependence on epsilon while relying only on approximate score access.

## Core Contribution

The paper proposes a new solver based on a subtle combination of low-degree approximation and the collocation method. It proves iteration complexity polylogarithmic in 1/epsilon, giving the first high-accuracy guarantee for a diffusion-based sampler that only needs approximate score access.

The bound has no explicit ambient-dimension dependence; dimension enters only through the effective radius of the target distribution's support.

## Method

The method replaces standard small-step discretization with an approximation/collocation scheme for solving the diffusion sampling differential equation. Low-degree approximations capture the trajectory more efficiently, while collocation enforces the dynamics at selected points.

The analysis tracks score-approximation error and support-radius dependence to obtain high-accuracy sampling guarantees.

## Experiments and Evidence

Evidence reported in the abstract is theoretical:

- Polylogarithmic dependence on inverse accuracy 1/epsilon.
- No explicit ambient-dimension dependence beyond effective support radius.
- Uses approximate access to data-distribution scores.
- First high-accuracy guarantee of this type for diffusion-based sampling.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: regularity assumptions, score-error model, effective-radius definition, constants, and whether there are empirical solver comparisons.

## Limits and Failure Modes

- Strong smoothness or support assumptions may be required.
- Approximate score access can dominate practical error.
- Polylogarithmic asymptotics may hide large constants.
- The method's implementation complexity and compatibility with neural score models need inspection.

## Deep Themes

**Sampler guarantees are catching up to empirical diffusion.** The paper targets high-accuracy theory, not only heuristic speed.

**Effective dimension can replace ambient dimension.** Complexity depends on support geometry rather than raw coordinate count.

**Numerical analysis is central to generative modeling.** Collocation and approximation theory become diffusion-model tools.

## Subthemes

- High-accuracy diffusion sampling.
- Low-degree approximation.
- Collocation solvers.
- Effective support radius.
- Dimension-free iteration bounds.

## Connections to Other Papers

Connects to SRMC, Local Diffusion Composition, UDM-GRPO, and Flowers through differential-equation and sampler geometry. It also links to theory papers where sharper structural quantities replace crude dimension dependence.

## Notes for Cross-Paper Synthesis

This paper adds to a theoretical efficiency theme: practical generative modeling may require better numerical solvers as much as better score networks.
