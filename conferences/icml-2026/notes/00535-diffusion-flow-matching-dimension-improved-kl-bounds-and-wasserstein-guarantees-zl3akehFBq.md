# Diffusion Flow Matching: Dimension-Improved KL Bounds and Wasserstein Guarantees

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: zl3akehFBq
- Authors: Marta Gentiloni Silveri; Giovanni Conforti; Alain Oliviero Durmus
- Primary area: theory->probabilistic_methods
- Keywords: Diffusion Flow Matching;Kullback–Leibler divergence;Wasserstein distance;Convergence Guarantees
- Source URL: https://openreview.net/forum?id=zl3akehFBq
- PDF URL: https://openreview.net/pdf?id=zl3akehFBq

## Abstract

Diffusion Flow Matching (DFM) has recently emerged as a versatile framework for generative modeling, yet its theoretical convergence properties remain only partially understood. In this work, we provide refined and novel convergence guarantees for Brownian motion based DFMs, focusing on the  discretization error. Our analysis is conducted under the Kullback–Leibler (KL) divergence and the 2-Wasserstein distance. Under finite-moment conditions and a mild score integrability assumption, we derive KL convergence bounds with improved dimensional dependence compared to prior work, achieving, up to our knowledge, state-of-the-art scaling under minimal conditions. We further extend the analysis to the 2-Wasserstein distance: under an additional first-order score integrability assumption and a weak log-concavity condition, we obtain convergence guarantees with dimensional dependence consistent with the KL case.

## One-Sentence Claim

The paper gives improved KL and Wasserstein discretization-error guarantees for Brownian-motion diffusion flow matching under relatively mild moment and score assumptions.

## Problem

Diffusion Flow Matching is a flexible generative-modeling framework, but its convergence theory is incomplete, especially for discretization error.

The problem is to obtain sharper guarantees under KL divergence and 2-Wasserstein distance with better dimensional dependence and minimal assumptions.

## Core Contribution

The paper derives refined KL convergence bounds for Brownian-motion-based DFMs with improved dimensional scaling relative to prior work.

It also extends the analysis to 2-Wasserstein distance under an additional first-order score integrability assumption and weak log-concavity, obtaining dimensional dependence consistent with the KL case.

## Method

The analysis focuses on discretization error in Brownian-motion DFMs. Under finite-moment conditions and mild score integrability, it proves KL convergence bounds.

For Wasserstein guarantees, it adds first-order score integrability and weak log-concavity assumptions to control transport distance between generated and target distributions.

## Experiments and Evidence

The abstract presents theoretical guarantees rather than empirical evidence.

The claimed evidence is state-of-the-art dimensional scaling for KL under minimal conditions, plus matched dimensional behavior for Wasserstein under additional assumptions.

## Limits and Failure Modes

The results apply to Brownian-motion-based DFMs and depend on score integrability, finite moments, and weak log-concavity for Wasserstein guarantees.

Because this note is abstract-only, details still need checking: exact rates, discretization scheme, comparison to prior bounds, constants, applicability to practical neural score approximation, and whether assumptions hold for multimodal image data.

## Deep Themes

- Generative modeling with quantitative guarantees: diffusion and flow methods need finite-step error theory.
- Dimensional dependence as practical barrier: bounds matter only if they scale tolerably with dimension.
- KL and Wasserstein complementarity: likelihood-style and transport-style convergence capture different aspects.
- Assumption minimization: theory is more useful when it avoids overly strong smoothness or convexity conditions.

## Subthemes

- Brownian-motion DFM.
- Discretization error.
- Score integrability.
- Weak log-concavity for Wasserstein bounds.

## Connections to Other Papers

This connects to Reverse Flow Matching, DivIn, and diffusion-policy RL papers through the mathematical foundations of flow/diffusion generation.

It also relates to theory papers on kernel bounds and optimizer guarantees because all try to sharpen the scaling terms that decide whether theory remains meaningful in high dimensions.

## Notes for Cross-Paper Synthesis

This paper contributes theoretical infrastructure for the corpus's diffusion/flow theme: as these models move into control, RL, and world generation, discretization guarantees become a reliability layer.
