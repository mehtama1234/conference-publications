# One Intervention per Component is Enough: Towards Identifiability in Linear Stochastic Dynamics from Steady State

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: g07aDcWYJ9
- Authors: Saber Salehkaleybar
- Primary area: general_machine_learning->causality
- Keywords: Causal Inference;Stochastic Differential Equation;Interventions;Causal Discovery;Ornstein–Uhlenbeck Process;Identifiability
- Source URL: https://openreview.net/forum?id=g07aDcWYJ9
- PDF URL: https://openreview.net/pdf?id=g07aDcWYJ9

## Abstract

We study the problem of recovering the parameters of a multivariate Ornstein–Uhlenbeck (OU) process from steady-state observational and interventional data. In many applications, such as large-scale gene perturbation experiments, only stationary “snapshot” measurements are available, making standard stochastic differential equation estimation methods that rely on time-series trajectories inapplicable. We first establish an identifiability result: one intervention per strongly connected component (SCC) of the drift graph suffices to recover all OU process parameters generically up to a global scaling factor. This holds provided that the SCC condensation graph is connected with a single root and certain spectral nondegeneracy assumptions hold. We propose a recursive learning algorithm that orders SCCs topologically and, for each component, isolates its marginal dynamics and solves a linear system derived from the steady-state moment equations, leveraging parameters recovered for upstream components. Building on this theoretical foundation, we propose a regularized least-squares estimator that jointly minimizes residuals of the steady-state mean and covariance equations across observational and interventional data. Experiments on synthetic and real datasets demonstrate the effectiveness of our method in recovering parameters and predicting unseen interventions.

## One-Sentence Claim

For multivariate Ornstein-Uhlenbeck systems observed only at steady state, one intervention per strongly connected component generically identifies all parameters up to global scale under graph and spectral conditions.

## Problem

Many systems, such as large-scale gene perturbation experiments, provide stationary snapshot measurements rather than time-series trajectories. Standard stochastic differential equation estimation methods need trajectories, so they cannot directly recover dynamic parameters from steady-state data.

The paper asks how much interventional data is needed to identify linear stochastic dynamics from stationary observational and interventional moments.

## Core Contribution

The main theoretical result is that one intervention per strongly connected component of the drift graph suffices to recover all OU process parameters generically up to a global scaling factor, assuming a connected condensation graph with a single root and spectral nondegeneracy.

The paper also provides a recursive learning algorithm over topologically ordered SCCs and a regularized least-squares estimator using steady-state mean and covariance equations.

## Method

The recursive algorithm orders SCCs topologically. For each component, it isolates marginal dynamics and solves a linear system derived from steady-state moment equations, using upstream parameters recovered earlier.

The practical estimator jointly minimizes residuals across observational and interventional steady-state mean/covariance equations, enabling prediction of unseen interventions.

## Experiments and Evidence

Evidence reported in the abstract:

- Generic identifiability up to global scaling with one intervention per SCC.
- Conditions involving connected single-root SCC condensation and spectral nondegeneracy.
- Recursive learning algorithm based on steady-state moments.
- Regularized least-squares estimator.
- Synthetic and real datasets showing parameter recovery and unseen-intervention prediction.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: intervention type, graph assumptions, real dataset domain, and estimator robustness.

## Limits and Failure Modes

- Identifiability is generic and condition-dependent, not universal.
- Global scale remains unresolved.
- Steady-state moment estimates can be noisy in finite samples.
- Nonlinear dynamics, hidden confounders, or misspecified interventions may violate assumptions.

## Deep Themes

**Minimal interventions can unlock dynamics.** The paper quantifies how little intervention is needed when graph structure is favorable.

**Steady-state data can still identify processes.** Snapshot measurements are not hopeless if interventions reveal the right components.

**Graph decomposition structures learning.** SCC topology turns a global identification problem into recursive component recovery.

## Subthemes

- Ornstein-Uhlenbeck process identifiability.
- Steady-state causal discovery.
- One intervention per SCC.
- Moment-equation learning.
- Gene-perturbation-style snapshot data.

## Connections to Other Papers

Connects to Source Screening, Noisy Sample Compression, Jacobi Spectral Reconstruction, and causal identifiability work. It also relates to finite-test certification because both ask how much structured evidence is enough.

## Notes for Cross-Paper Synthesis

This paper fits the evidence-efficiency theme: carefully placed interventions can substitute for dense time-series observation when the system's graph structure is exploitable.
