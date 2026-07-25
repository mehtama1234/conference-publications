# Markov Chain Monte Carlo without Evaluating the Target: an Auxiliary Variable Approach

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: dDkl5ZcyTl
- Authors: Wei Yuan; Guanyang Wang
- Primary area: probabilistic_methods->monte_carlo_and_sampling_methods
- Keywords: Markov chain Monte Carlo;auxiliary variable;tall dataset;exchange algorithm;locally--balanced proposal;stochastic gradient Langevin dynamics
- Source URL: https://openreview.net/forum?id=dDkl5ZcyTl
- PDF URL: https://openreview.net/pdf?id=dDkl5ZcyTl

## Abstract

In sampling tasks, it is common for target distributions to be known up to a normalizing constant. However, in many situations, even evaluating the unnormalized distribution can be costly or infeasible. This issue arises in scenarios such as sampling from the Bayesian posterior for tall datasets and the `doubly-intractable' distributions. In this paper, we begin by observing that seemingly different Markov chain Monte Carlo (MCMC) algorithms, such as the exchange algorithm, PoissonMH, and TunaMH, can be unified under a simple common procedure. We then extend this procedure into a novel framework that allows the use of auxiliary variables in both the proposal and the acceptance--rejection step. Several new MCMC algorithms emerge from this framework that uses estimated gradients to guide the proposal moves. They have demonstrated significantly better performance than existing methods on both synthetic and real datasets. We also develop theory for the new framework and use it to simplify and extend results for existing algorithms. The code to reproduce the experimental results can be found at https://github.com/ywwes26/Auxiliary-MCMC.

## One-Sentence Claim

Auxiliary-variable MCMC can sample when even unnormalized target evaluation is costly by using auxiliary variables in both proposals and acceptance decisions with estimated-gradient guidance.

## Problem

Many MCMC settings know the target distribution only up to a normalizing constant, but some problems make even the unnormalized density expensive or infeasible to evaluate. This happens in Bayesian posteriors for tall datasets and doubly-intractable distributions.

The paper asks how to build MCMC algorithms that avoid direct target evaluation while remaining theoretically grounded.

## Core Contribution

The paper observes that exchange algorithms, PoissonMH, and TunaMH share a simple common procedure. It extends this into a framework where auxiliary variables are used in both proposal and acceptance-rejection steps.

This yields new MCMC algorithms guided by estimated gradients, with better performance than existing methods on synthetic and real datasets. The framework also simplifies and extends theory for existing algorithms.

## Method

The method augments the Markov chain with auxiliary variables that stand in for expensive target evaluations. Estimated gradients guide proposal moves, while acceptance decisions also use auxiliary randomness rather than exact target values.

By unifying prior methods, the framework reveals which parts of the algorithm can be generalized.

## Experiments and Evidence

Evidence reported in the abstract:

- Unified view of exchange algorithm, PoissonMH, and TunaMH.
- Auxiliary variables in proposals and acceptance-rejection.
- New gradient-guided MCMC algorithms.
- Significant empirical improvements on synthetic and real datasets.
- Theory simplifying and extending existing algorithm results.
- Code release.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: exact auxiliary distributions, acceptance correctness, gradient-estimator bias, and benchmark details.

## Limits and Failure Modes

- Estimated gradients can bias proposals if not handled carefully.
- Auxiliary-variable methods may increase variance or require tuning.
- Tall-data performance depends on subsampling structure.
- Doubly-intractable models can still be expensive if auxiliary simulation is hard.

## Deep Themes

**Sampling can avoid direct target evaluation.** The algorithm moves uncertainty into auxiliary variables.

**Different MCMC tricks share a common procedure.** Unification reveals new algorithm variants.

**Gradient guidance survives noisy target access.** Estimated gradients help proposals even when exact densities are unavailable.

## Subthemes

- Auxiliary-variable MCMC.
- Doubly-intractable distributions.
- Tall-data posterior sampling.
- Exchange/PoissonMH/TunaMH unification.
- Estimated-gradient proposals.

## Connections to Other Papers

Connects to Flow Sampling, Tilt Matching, SRMC, Distribution Transformers, and high-accuracy diffusion sampling through scalable probabilistic computation. It also links to BFTS and Bayesian decision methods where posterior sampling cost matters.

## Notes for Cross-Paper Synthesis

This paper adds to the inference-efficiency theme: when exact probabilistic quantities are unavailable, introduce auxiliary structure that preserves sampling validity while reducing expensive evaluations.
