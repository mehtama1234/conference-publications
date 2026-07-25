# VectorWorld: Efficient Streaming World Model via Diffusion Flow on Vector Graphs

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: yTEEiE3YtD
- Authors: Chaokang Jiang; Desen Zhou; Jiuming Liu; Li Sun
- Primary area: deep_learning->generative_models_and_autoencoders
- Keywords: autonomous driving simulation;closed-loop evaluation;world models;vectorized scene generation;traffic simulation;real-time generation
- Source URL: https://openreview.net/forum?id=yTEEiE3YtD
- PDF URL: https://openreview.net/pdf?id=yTEEiE3YtD

## Abstract

Closed-loop evaluation of autonomous-driving policies requires interactive 
simulation beyond log replay. Existing generative world models suffer three gaps: history-incompatible initialization, sampling latency exceeding real-time budgets, and compounding kinematic infeasibility. We propose VectorWorld, a streaming vector-graph world model that incrementally generates ego-centric lane--agent tiles during rollout. VectorWorld couples a motion-aware gated VAE for history-compatible initialization, an edge-gated relational DiT with interval-conditioned MeanFlow and JVP-based large-step supervision for solver-free outpainting, and $\Delta$Sim, a physics-aligned NPC policy with hybrid discrete--continuous actions and differentiable kinematic logit shaping. On Waymo Open Motion and nuPlan, VectorWorld improves map fidelity, initialization validity, and density calibration, enabling stable real-time $1\mathrm{km}+$ closed-loop rollouts.

## One-Sentence Claim

VectorWorld enables real-time closed-loop autonomous-driving simulation by streaming ego-centric vector-graph world tiles with diffusion-flow outpainting and physics-aligned NPC policies.

## Problem

Closed-loop evaluation of autonomous-driving policies needs interactive simulation rather than passive log replay. Existing generative world models face history-incompatible initialization, sampling latency beyond real-time budgets, and compounding kinematic infeasibility.

The problem is to generate driving worlds that are valid at initialization, fast enough during rollout, and physically plausible over long horizons.

## Core Contribution

The paper proposes VectorWorld, a streaming vector-graph world model that incrementally generates ego-centric lane-agent tiles during rollout.

Its components include a motion-aware gated VAE for history-compatible initialization, an edge-gated relational DiT with interval-conditioned MeanFlow and JVP-based large-step supervision for solver-free outpainting, and DeltaSim, a physics-aligned NPC policy.

## Method

VectorWorld represents scenes as vector graphs rather than rendered pixels. During closed-loop rollout, it streams new ego-centric lane-agent tiles as the policy moves.

MeanFlow-style diffusion flow enables large-step solver-free outpainting, while DeltaSim uses hybrid discrete-continuous actions and differentiable kinematic logit shaping to keep NPC behavior physically aligned.

## Experiments and Evidence

The abstract reports evaluations on Waymo Open Motion and nuPlan. VectorWorld improves map fidelity, initialization validity, and density calibration.

It enables stable real-time closed-loop rollouts longer than 1 km.

## Limits and Failure Modes

Vector-graph simulation may miss visual appearance factors that affect perception stacks, and long rollouts can still accumulate behavioral distribution shift if NPC policies are imperfect.

Because this note is abstract-only, details still need checking: exact rollout speed, closed-loop policy interface, map/lane representation, collision metrics, NPC realism, comparison baselines, and whether real-time performance holds under dense traffic.

## Deep Themes

- Closed-loop world modeling: autonomous-driving evaluation requires interactive futures, not replay.
- Vectorized scene generation: structured lane-agent graphs can be more efficient than pixel simulation.
- History-compatible initialization: simulators must start from states consistent with observed context.
- Physics-aligned generative rollout: learned generation needs kinematic constraints to avoid compounding infeasibility.

## Subthemes

- Streaming ego-centric tiles.
- Relational DiT for vector graphs.
- Solver-free diffusion-flow outpainting.
- Hybrid discrete-continuous NPC actions.

## Connections to Other Papers

This connects to PanoWorld-X and Beyond Language Modeling through world-model generation, but it is more operational: the generated world must support closed-loop policy evaluation.

It also relates to EcoVLA, CoEvol-NO, and physical-domain generation papers because all combine generative modeling with constraints from embodied dynamics.

## Notes for Cross-Paper Synthesis

VectorWorld adds a simulation infrastructure thread: world models become useful when they can run interactively, respect dynamics, and expose controllable state for downstream agents.
