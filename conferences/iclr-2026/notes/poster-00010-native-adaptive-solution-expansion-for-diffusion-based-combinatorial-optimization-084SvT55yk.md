# Native Adaptive Solution Expansion for Diffusion-based Combinatorial Optimization

## Metadata

- Conference: iclr-2026
- Status: Poster
- OpenReview ID: 084SvT55yk
- Authors: Yu Wang; Yang Li; Jiale Ma; Junchi Yan; Yi Chang
- Primary area: learning on graphs and other geometries & topologies
- Keywords: mask diffusion model;neural combinatorial optimization
- Source URL: https://openreview.net/forum?id=084SvT55yk
- PDF URL: https://openreview.net/pdf?id=084SvT55yk

## Abstract

One central challenge in Neural Combinatorial Optimization (NCO) is handling hard constraints efficiently. Beyond the two classic paradigms, i.e., Local Construction (LC), which sequentially builds feasible solutions but scales poorly, and Global Prediction (GP), which produces one-shot heatmaps yet struggles with constraint conflicts, the recently proposed Adaptive Expansion (AE) shares the advantages of both by progressively growing partial solutions with instance-wise global awareness.
However, existing realizations bolt AE onto external GP predictors, so their solution quality is bounded by the backbone and their inference cost scales with repeated global calls.
In this paper, we fundamentally rethink adaptive expansion and make it native to a generative model, acting as its intrinsic decoding principle  rather than an external wrapper.
We propose NEXCO, a CO-specific masked diffusion framework that turns adaptive expansion into the model’s own iterative unmasking process.
Specifically, it involves a solution-expansion training procedure with a time-agnostic GNN denoiser, which learns diffusion trajectories between fully masked solutions and ground-truth solutions.
With the trained time-agnostic denoiser, we introduce a novel solution expansion scheme at the solving stage, enabling adaptive control over the intermediate solution states. 
It is achieved by constructing candidate sets according to confidence scores and applying feasibility projection to expand the solution while respecting constraints. 
In this way, ``adaptive" is not an afterthought but the decoding itself: intermediate diffusion states are meaningful partial solutions and progress is instance-adaptive rather than schedule-bound.
Extensive experiments on representative CO problems show that NEXCO achieves approximately 50\% improvement in solution quality and up to $4\times$ faster inference compared to prior state-of-the-art solvers.

## One-Sentence Claim

NEXCO makes adaptive solution expansion native to a masked diffusion model for combinatorial optimization, improving solution quality and inference speed over prior solvers.

## Problem

Neural combinatorial optimization struggles with hard constraints. Local construction maintains feasibility but scales poorly, global prediction is efficient but can create constraint conflicts, and previous adaptive expansion methods depend on external global predictors whose quality and cost bound the solver.

## Core Contribution

The paper contributes NEXCO, a combinatorial-optimization-specific masked diffusion framework where adaptive expansion is the model's intrinsic iterative unmasking process rather than an external wrapper. Intermediate diffusion states become meaningful partial solutions.

## Method

NEXCO trains a time-agnostic GNN denoiser on solution-expansion trajectories from fully masked solutions to ground truth. At solving time, it builds candidate sets from confidence scores and applies feasibility projection to adaptively expand the solution while respecting constraints.

## Experiments and Evidence

The abstract reports extensive experiments on representative combinatorial optimization problems, with approximately 50% solution-quality improvement and up to 4x faster inference compared with prior state-of-the-art solvers.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect which CO problems are used, constraint types, feasibility projection cost, baseline tuning, and behavior on larger or out-of-distribution instances. Diffusion-style iterative decoding may still be expensive if many expansion steps are required.

## Deep Themes

- Native adaptive decoding for constrained optimization.
- Masked diffusion as constructive solver.
- Feasible partial solutions as intermediate states.
- Confidence-guided expansion.

## Subthemes

- NEXCO.
- Neural combinatorial optimization.
- Time-agnostic GNN denoiser.
- Feasibility projection.
- Adaptive expansion.

## Connections to Other Papers

Connects to PGM through masked generation without wasteful steps, to GLASS Flows through generative inference reformulation, and to Track-and-Stop/CALIPER through adaptive evidence-driven progression.

## Notes for Cross-Paper Synthesis

NEXCO is a clear instance of process realignment: the generative model's decoding path is made identical to the solver's constructive logic. The deeper pattern is that intermediate states become useful when the model's generation process respects task constraints from the start.
