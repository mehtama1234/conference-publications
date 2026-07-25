# HDFlow: Hierarchical Diffusion-Flow Planning for Long-horizon Tasks

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 3ZFvXHJwmB
- Authors: Gireesh Nandiraju; Yuanliang Ju; Chaoyi Xu; Weiheng Liu; Yuxuan Wan; He Wang
- Primary area: applications->robotics
- Keywords: long-horizon planning;world models;contact-rich manipulation
- Source URL: https://openreview.net/forum?id=3ZFvXHJwmB
- PDF URL: https://openreview.net/pdf?id=3ZFvXHJwmB

## Abstract

Recent advances in generative models have shown promise in generating behavior plans for long-horizon, sparse reward tasks. While these approaches have achieved promising results, they often lack a principled framework for hierarchical decomposition and struggle with the computational demands of real-time execution, due to their iterative denoising process. In this work, we introduce $\textbf{Hierarchical Diffusion-Flow}$ ($\texttt{\textbf{HDFlow}}$), a novel hierarchical planning framework that optimally leverages the strengths of $\textit{diffusion}$ and $\textit{rectified flow}$ models to overcome the limitations of single-paradigm generative planners. $\texttt{\textbf{HDFlow}}$ employs a high-level diffusion planner to generate sequences of strategic subgoals in a learned latent space, capitalizing on diffusion's powerful exploratory capabilities. These subgoals then guide a low-level rectified flow planner that generates smooth and dense trajectories, exploiting the speed and efficiency of ordinary differential equation (ODE)-based trajectory generation. We evaluate $\texttt{\textbf{HDFlow}}$ on four challenging furniture assembly tasks in both simulation and real-world, where it significantly outperforms state-of-the-art methods. Furthermore, we also showcase our method's generalizability on two long-horizon benchmarks comprising diverse locomotion and manipulation tasks. Project website: https://hdflow-page.github.io/

## One-Sentence Claim

HDFlow improves long-horizon robot planning by using diffusion for exploratory high-level latent subgoals and rectified flow for fast low-level trajectory generation.

## Problem

Generative planners can handle sparse-reward long-horizon tasks, but single-paradigm diffusion planners are computationally expensive for real-time execution and may lack principled hierarchical decomposition.

## Core Contribution

The paper proposes a hybrid hierarchical planner that separates strategic subgoal generation from dense trajectory generation, assigning diffusion and rectified flow to the levels where each is strongest.

## Method

A world model learns a structured latent space. A high-level conditional diffusion planner generates sparse subgoal sequences in that latent space, guided to avoid infeasible or dead-end trajectories. A low-level rectified flow model then produces smooth dense latent trajectories between subgoals using ODE-based generation.

## Experiments and Evidence

The abstract reports significant gains over state-of-the-art methods on four furniture assembly tasks in simulation and real-world settings, plus generalization to locomotion and manipulation benchmarks.

## Full-Text Upgrade

The full text shows the planner has two stages: world-model learning creates a semantically structured latent space, and hierarchical planner training learns high-level subgoals plus low-level trajectories. The high-level diffusion model generates a sequence of latent subgoals from current state to goal state, while a manifold-aware energy-based guidance mechanism steers samples toward feasible successful subgoal manifolds.

The low-level planner uses rectified flow because dense diffusion trajectories would be too slow for real-time robotic interaction. Given consecutive latent subgoals, it generates an H-step latent trajectory with an ODE solver, then maps latent transitions to control actions. Evaluation centers on contact-rich FurnitureBench tasks with randomization in simulation and real-world rollout, plus broader long-horizon locomotion/manipulation benchmarks and ablations comparing flat diffusion, hierarchical flow, and hierarchical diffusion.

## Limits and Failure Modes

Limits to watch: performance depends on the quality and structure of the learned latent world model; high-level subgoal feasibility requires effective guidance; and real-world evidence appears concentrated in furniture-assembly settings.

## Deep Themes

- Long-horizon embodied planning benefits from hierarchical generative decomposition.
- Different generative models serve different planning levels.
- Latent-space structure is becoming central to robot planning.

## Subthemes

- Diffusion planning.
- Rectified flow.
- Latent world models.
- Subgoal generation.
- Contact-rich manipulation.
- Real-world robot transfer.

## Connections to Other Papers

Connects to BehaviorVLA and MomaGraph as another embodied-AI paper where temporal structure and intermediate representations make long-horizon tasks tractable.

## Notes for Cross-Paper Synthesis

HDFlow strengthens a recurring embodied theme: robust long-horizon behavior comes from explicit intermediate structure, whether behavioral representations, scene graphs, or latent subgoals.
