# Score-Repellent Monte Carlo: Toward Efficient Non-Markovian Sampler with Constant Memory in General State Spaces

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: PN8EiOzMuT
- Authors: Jie Hu; Lingyun Chen; Geeho Kim; Jinyoung Choi; Bohyung Han; Do Young Eun
- Primary area: probabilistic_methods->monte_carlo_and_sampling_methods
- Keywords: MCMC;Non-Markovian;Score-Repellent Monte Carlo;Score-Tilted Surrogate;Asymptotic Unbiasedness;Central Limit Theorem
- Source URL: https://openreview.net/forum?id=PN8EiOzMuT
- PDF URL: https://openreview.net/pdf?id=PN8EiOzMuT

## Abstract

History-dependent sampling can reduce long-run Monte Carlo variance by discouraging redundant revisits, but existing schemes typically encode history through empirical measure on finite state spaces, which is infeasible in high-dimensional discrete configuration spaces or ill-posed in continuous domains. We propose *Score-Repellent Monte Carlo* (SRMC) framework that summarizes trajectory history by a running average of score evaluations in $\mathbb{R}^d$, where $d$ is the dimension of the score and state representation. This history is converted into a surrogate target through an exponential *score tilt*, indexed with $\alpha$ that represents the *strength of repellence* in controlling the magnitude of the history-based repulsion. The surrogate family is normalization-free in the standard MCMC sense, yielding a generic wrapper: at each iteration, any base kernel targeting $\pi$ can instead be run on the current surrogate $\pi_{\theta_n}$ while the history is updated online. We analyze the coupled evolution of the history recursion and Monte Carlo estimators using stochastic approximation with controlled Markovian noise, establishing almost sure convergence and a joint central limit theorem. We further identify regimes in which the asymptotic covariance decreases as $\alpha$ increases, with scaling $O(1/\alpha)$, extending the near-zero-variance effect of finite-state history-dependent samplers to general state spaces with constant memory. Experiments on continuous targets and discrete energy-based models demonstrate improved estimator variance and mode coverage, while retaining $O(d)$ memory usage and modest per-iteration overhead.

## One-Sentence Claim

Score-Repellent Monte Carlo uses a constant-memory running average of score evaluations to repel samplers from redundant revisits and reduce long-run variance in general state spaces.

## Problem

History-dependent samplers can reduce variance, but existing empirical-measure histories work mainly in finite state spaces and become infeasible or ill-posed in high-dimensional or continuous domains.

## Core Contribution

The paper introduces SRMC, a generic non-Markovian wrapper that converts score-history summaries into normalization-free score-tilted surrogate targets, with convergence and CLT guarantees.

## Method

SRMC maintains a running average of score evaluations in representation space, uses an exponential score tilt controlled by repellence strength alpha to define a surrogate target, runs any base MCMC kernel on the current surrogate, and updates history online.

## Experiments and Evidence

The abstract reports almost sure convergence, a joint central limit theorem, regimes where asymptotic covariance decreases as O(1/alpha), and experiments on continuous targets plus discrete energy-based models showing lower estimator variance and better mode coverage with O(d) memory.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: score availability, alpha tuning, base-kernel assumptions, high-dimensional scaling, bias at finite time, and robustness when score estimates are noisy.

## Deep Themes

- Sampling efficiency can improve through compact history summaries.
- Non-Markovian behavior need not require unbounded memory.
- Score geometry can guide exploration away from redundant regions.

## Subthemes

- MCMC.
- Non-Markovian sampling.
- Score-tilted surrogates.
- Stochastic approximation.
- Central limit theorem.
- Mode coverage.

## Connections to Other Papers

Connects to high-accuracy sampling, LiDAR diffusion sampling, and test-time control papers through better sampling dynamics under computational constraints.

## Notes for Cross-Paper Synthesis

SRMC adds a memory-efficient exploration theme: a low-dimensional statistic of trajectory history can reduce redundancy without storing the trajectory itself.
