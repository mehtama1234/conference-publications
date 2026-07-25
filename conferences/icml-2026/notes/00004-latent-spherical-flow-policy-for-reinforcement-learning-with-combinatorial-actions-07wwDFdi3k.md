# Latent Spherical Flow Policy for Reinforcement Learning with Combinatorial Actions

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 07wwDFdi3k
- Authors: Lingkai Kong; Anagha Satish; Hezi Jiang; Akseli Kangaslahti; Andrew Ma; Wenbo Chen; Mingxiao Song; Lily Xu; Milind Tambe
- Primary area: reinforcement_learning->deep_rl
- Keywords: Reinforcement Learning with Combinatorial Actions;Flow Matching;Generative Models
- Source URL: https://openreview.net/forum?id=07wwDFdi3k
- PDF URL: https://openreview.net/pdf?id=07wwDFdi3k

## Abstract

Reinforcement learning (RL) with combinatorial action spaces remains challenging because feasible action sets are exponentially large and governed by complex feasibility constraints, making direct policy parameterization impractical. Existing approaches embed task-specific value functions into constrained optimization programs or learn deterministic structured policies, sacrificing generality and policy expressiveness. We propose a solver-induced \emph{latent spherical flow policy} that brings the expressiveness of modern generative policies to combinatorial RL while guaranteeing feasibility by design. Our method, LSFlow, learns a \emph{stochastic} policy in a compact continuous latent space via spherical flow matching, and delegates feasibility to a combinatorial optimization solver that maps each latent sample to a valid structured action. To improve efficiency, we train the value network directly in the latent space, avoiding repeated solver calls during policy optimization. To address the piecewise-constant and discontinuous value landscape induced by solver-based action selection, we introduce a smoothed Bellman operator that yields stable, well-defined learning targets. Empirically, our approach outperforms state-of-the-art baselines by an average of 20.6\% across a range of challenging combinatorial RL tasks.

## One-Sentence Claim

LSFlow combines spherical flow matching with solver-induced feasible action mapping to learn expressive stochastic RL policies for combinatorial action spaces.

## Problem

Combinatorial RL faces exponentially large feasible action sets with complex constraints, making direct policy parameterization impractical and pushing prior methods toward task-specific optimization or less expressive deterministic policies.

## Core Contribution

The paper proposes a latent spherical flow policy that samples in a compact continuous latent space, uses a combinatorial solver to map samples to valid actions, trains value functions in latent space for efficiency, and stabilizes learning with a smoothed Bellman operator.

## Method

LSFlow learns a stochastic policy via spherical flow matching. Feasibility is delegated to a solver, while optimization avoids repeated solver calls by learning values in latent space. A smoothed Bellman operator handles the discontinuous, piecewise-constant value landscape induced by solver-based action selection.

## Experiments and Evidence

The abstract reports an average 20.6% improvement over state-of-the-art baselines across challenging combinatorial RL tasks.

## Limits and Failure Modes

PDF checks needed: solver cost at inference, scalability with action-constraint complexity, sensitivity to latent dimension, and whether the solver mapping restricts exploration or creates many-to-one degeneracies.

## Deep Themes

- Generative modeling is entering structured decision-making.
- Solvers and learned policies are being composed rather than treated as alternatives.
- Feasibility guarantees can be delegated to external algorithmic components.

## Subthemes

- Combinatorial RL.
- Flow matching.
- Solver-induced policies.
- Feasible action generation.
- Smoothed Bellman targets.

## Connections to Other Papers

Connects to agentic planning, diffusion/flow generative modeling, and hybrid neural-symbolic or solver-assisted ML systems.

## Notes for Cross-Paper Synthesis

This paper is evidence for a deeper hybridization pattern: neural models provide expressive distributions, while classical solvers enforce constraints and feasibility.
