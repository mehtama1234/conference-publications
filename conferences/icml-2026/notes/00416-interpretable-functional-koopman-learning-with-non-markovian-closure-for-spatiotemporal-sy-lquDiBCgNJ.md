# Interpretable Functional Koopman Learning with Non-Markovian Closure for Spatiotemporal Systems

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: lquDiBCgNJ
- Authors: Wanfeng Lu; He Ma; Wei Lin; Qunxi Zhu
- Primary area: general_machine_learning->sequential_network_and_time_series_modeling
- Keywords: partial differential equations;Koopman learning;reduced order modeling;non-Markovian;spatiotemporal forecasting
- Source URL: https://openreview.net/forum?id=lquDiBCgNJ
- PDF URL: https://openreview.net/pdf?id=lquDiBCgNJ

## Abstract

Precise prediction of spatiotemporal dynamics over predictive horizons is constrained by the computational cost of high-fidelity solvers and the sparsity, noise, and irregularity of data. We introduce MERLIN, a Koopman-based framework that lifts dynamics to the evolution of learned *observation functionals* with near-linear progression, enabling full-field reconstruction at arbitrary resolutions. Theoretically, we develop a functional Koopman theory for PDEs and compensate for the loss of finite-dimensional linear invariance via the Mori–Zwanzig formalism, which augments the linear backbone with non-Markovian memory terms to improve predictive accuracy. Practically, MERLIN employs discretization-invariant *function encoders* that map partial, irregular observations to observables, and resolution-free *function decoders* that reconstruct states at arbitrary query points. Training under linear constraints yields an interpretable, low-dimensional model
that captures principal modes and supports reduced-order modeling, while memory
correction further enables stable long-horizon rollouts even in ultra-low-dimensional
latent spaces. Our code is available at: https://github.com/RobinLufdu/MERLIN.

## One-Sentence Claim

MERLIN learns interpretable functional Koopman dynamics for PDE systems, using non-Markovian memory closure to stabilize long-horizon reduced-order forecasting from irregular observations.

## Problem

Spatiotemporal systems are expensive to simulate with high-fidelity solvers, and available observations can be sparse, noisy, irregular, or partial. Standard finite-dimensional Koopman methods seek linear latent dynamics but lose exact invariance and can struggle over long horizons.

The paper asks how to learn low-dimensional, interpretable, resolution-free dynamics while accounting for the memory effects induced by reduction.

## Core Contribution

The contribution is MERLIN, a Koopman framework that lifts PDE dynamics to learned observation functionals with near-linear progression and reconstructs full fields at arbitrary resolutions.

Theoretically, it develops functional Koopman theory for PDEs and uses the Mori-Zwanzig formalism to add non-Markovian memory terms that compensate for lost finite-dimensional linear invariance.

## Method

MERLIN uses discretization-invariant function encoders to map partial irregular observations into observables and resolution-free function decoders to reconstruct states at arbitrary query points.

Training under linear constraints yields a low-dimensional interpretable backbone of principal modes, while memory correction improves stable long-horizon rollouts even in very small latent spaces.

## Experiments and Evidence

Evidence reported in the abstract:

- Functional Koopman theory for PDEs.
- Mori-Zwanzig non-Markovian memory closure.
- Discretization-invariant function encoders.
- Resolution-free function decoders.
- Full-field reconstruction at arbitrary query points.
- Stable long-horizon rollouts in ultra-low-dimensional latent spaces.
- Code released at the listed GitHub URL.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: PDE benchmarks, memory-term parameterization, and reconstruction error.

## Limits and Failure Modes

- Koopman-style linearization may struggle with strongly chaotic or discontinuous dynamics.
- Memory terms improve closure but may add estimation complexity.
- Interpretability of modes depends on learned functionals being physically meaningful.
- Sparse irregular observations can still make latent state inference ambiguous.

## Deep Themes

**Reduction creates memory.** Non-Markovian closure is needed when low-dimensional linear dynamics omit resolved variables.

**Scientific models need resolution-free interfaces.** Function encoders/decoders separate continuous fields from discretization grids.

**Interpretability and forecasting can align.** Koopman modes provide a structured representation for reduced-order dynamics.

## Subthemes

- Functional Koopman learning.
- Mori-Zwanzig memory closure.
- Reduced-order PDE modeling.
- Irregular observation encoding.
- Resolution-free field reconstruction.

## Connections to Other Papers

Connects to Walrus, LoRFS, ReViT, Generative Filtering, LASER, and Dirac-Frenkel-Onsager dynamics. It extends the scientific-ML structure theme through operator-theoretic reduced modeling.

## Notes for Cross-Paper Synthesis

MERLIN adds a memory-closure theme: stable scientific forecasting often requires explicitly modeling what the reduced state has forgotten.
