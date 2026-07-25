# A Dirac-Frenkel-Onsager Principle: Instantaneous Residual Minimization with Gauge Momentum for Nonlinear Parametrizations of PDE Solutions

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: aDPbUSUCwh
- Authors: Matteo Raviola; Benjamin Peherstorfer
- Primary area: applications->chemistry_physics_and_earth_sciences
- Keywords: Neural Galerkin;Dirac-Frenkel principle;Onsager principle;momentum;gauge freedom;partial differential equations;nonlinear approximations
- Source URL: https://openreview.net/forum?id=aDPbUSUCwh
- PDF URL: https://openreview.net/pdf?id=aDPbUSUCwh

## Abstract

Dirac-Frenkel instantaneous residual minimization evolves nonlinear parametrizations of PDE solutions in time, but ill-conditioning can render the parameter dynamics non-unique. We interpret this non-uniqueness as a gauge freedom: nullspace directions that leave the 
time derivative unchanged can be used to select better-conditioned parameter velocities. Building on Onsager's minimum-dissipation principle, we introduce a history variable---interpretable as momentum---and inject it only along the nullspace directions. The resulting Dirac-Frenkel-Onsager dynamics preserve instantaneous residual minimization, in contrast to standard regularization that can introduce bias, while promoting temporally smooth parameter evolution. Examples demonstrate that the approach leads to increased robustness in singular and near-singular regimes.

## One-Sentence Claim

Dirac-Frenkel-Onsager dynamics stabilize nonlinear PDE parameter evolution by injecting momentum only along gauge nullspace directions, preserving residual minimization without bias.

## Problem

Dirac-Frenkel instantaneous residual minimization evolves nonlinear parametrizations of PDE solutions over time. But ill-conditioning can make parameter dynamics non-unique: multiple parameter velocities produce the same time derivative.

Standard regularization can select a velocity but may bias the residual-minimization objective. The paper asks how to use this non-uniqueness constructively without corrupting the PDE approximation.

## Core Contribution

The paper interprets non-unique parameter velocities as gauge freedom: nullspace directions that leave the time derivative unchanged. Building on Onsager's minimum-dissipation principle, it introduces a history variable interpretable as momentum and injects it only along nullspace directions.

The resulting Dirac-Frenkel-Onsager dynamics preserve instantaneous residual minimization while producing smoother, better-conditioned parameter trajectories.

## Method

The method decomposes parameter velocity into components that affect the represented time derivative and gauge/nullspace components that do not. Momentum is applied only in the gauge component, so it improves temporal smoothness without changing the instantaneous residual-minimizing solution.

This differs from ordinary damping or regularization, which can bias the represented PDE dynamics.

## Experiments and Evidence

Evidence reported in the abstract:

- Theoretical interpretation of ill-conditioning as gauge freedom.
- Onsager-inspired momentum history variable.
- Momentum injected only along nullspace directions.
- Preservation of instantaneous residual minimization.
- Examples showing increased robustness in singular and near-singular regimes.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: PDE examples, nonlinear parametrizations, nullspace computation, and robustness metrics.

## Limits and Failure Modes

- Computing nullspace directions may be expensive or unstable in high-dimensional neural parametrizations.
- Gauge momentum helps non-uniqueness but may not solve model approximation error.
- Singular-regime examples may not cover chaotic or stiff PDEs.
- The method likely depends on differentiability and accurate residual evaluation.

## Deep Themes

**Non-identifiability can be useful gauge freedom.** The paper turns null directions from a pathology into a smoothing control.

**Stabilization should preserve the governing objective.** Gauge-only momentum avoids biasing residual minimization.

**PDE learning increasingly imports geometric mechanics.** Dirac-Frenkel, Onsager, and gauge language become practical design tools.

## Subthemes

- Dirac-Frenkel residual minimization.
- Onsager minimum dissipation.
- Gauge nullspace momentum.
- Nonlinear PDE parametrizations.
- Singular and near-singular robustness.

## Connections to Other Papers

Connects to Flowers, NeuronCtrl, Flow Sampling, Dimension-Free Diffusion Sampling, and scientific PDE/operator papers. It also links to PRISM and OCE because all exploit gauge or geometry-preserving directions to avoid harmful coordinate artifacts.

## Notes for Cross-Paper Synthesis

This paper adds a precise gauge-control example: when parameters are non-identifiable, stable learning/control should operate in directions that preserve the represented function.
