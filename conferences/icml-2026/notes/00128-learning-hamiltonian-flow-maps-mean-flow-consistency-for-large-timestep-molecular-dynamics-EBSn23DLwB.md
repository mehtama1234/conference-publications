# Learning Hamiltonian Flow Maps: Mean Flow Consistency for Large-Timestep Molecular Dynamics

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: EBSn23DLwB
- Authors: Winfried Ripken; Michael Plainer; Gregor Lied; Thorben Frank; Oliver T. Unke; Stefan Chmiela; Frank Noe; Klaus Robert Muller
- Primary area: applications->chemistry_physics_and_earth_sciences
- Keywords: Hamiltonian Mechanics;Molecular Dynamics;Integration;Flow Maps;Mean Flow
- Source URL: https://openreview.net/forum?id=EBSn23DLwB
- PDF URL: https://openreview.net/pdf?id=EBSn23DLwB

## Abstract

Simulating the long-time evolution of Hamiltonian systems is limited by the small timesteps required for stable numerical integration. To overcome this constraint, we introduce a framework to learn *Hamiltonian Flow Maps* by predicting the *mean* phase-space evolution over a chosen time span $\Delta t$, enabling stable large-timestep updates far beyond the stability limits of classical integrators. To this end, we impose a *Mean Flow* consistency condition for time-averaged Hamiltonian dynamics. Unlike prior approaches, this allows training on independent phase-space samples without access to future states, avoiding expensive trajectory generation. Validated across diverse Hamiltonian systems, our method in particular improves upon molecular dynamics simulations using machine-learned force fields (MLFF). Our models maintain comparable training and inference cost, but support significantly larger integration timesteps while trained directly on widely-available *trajectory-free* MLFF datasets.

## One-Sentence Claim

Hamiltonian Flow Maps learn mean phase-space evolution over large time spans, enabling stable large-timestep molecular dynamics from trajectory-free MLFF datasets.

## Problem

Long-time Hamiltonian simulation is limited by the small timesteps required for stable classical integration, and trajectory generation for training can be expensive.

## Core Contribution

The paper introduces a framework for learning Hamiltonian flow maps using a Mean Flow consistency condition for time-averaged dynamics.

## Method

The model predicts mean phase-space evolution over a chosen Delta t and trains on independent phase-space samples without requiring future states, avoiding expensive trajectory data.

## Experiments and Evidence

The abstract reports validation across diverse Hamiltonian systems and improved molecular dynamics with machine-learned force fields, supporting much larger timesteps at comparable training and inference cost.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: conservation properties, stability over long rollouts, Delta t limits, dataset assumptions, and comparison to symplectic/neural integrators.

## Deep Themes

- Scientific simulation is shifting from stepwise integration to learned flow maps.
- Trajectory-free datasets can train dynamics models if consistency constraints are right.
- Large-timestep stability is a key capability for molecular simulation.

## Subthemes

- Hamiltonian systems.
- Molecular dynamics.
- Flow maps.
- Mean Flow consistency.
- Machine-learned force fields.
- Large-timestep integration.

## Connections to Other Papers

Connects to IRNO, Rex, diffusion bridges, and scientific sampling papers through numerical-methods-as-ML-infrastructure.

## Notes for Cross-Paper Synthesis

This paper adds to the learned-solver theme: models can learn coarse evolution operators directly, bypassing small-step integration bottlenecks.
