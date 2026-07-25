# Learning Human-Robot Collaboration via Heterogeneous-Agent Lyapunov Policy Optimization

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: uBvlUE2wrP
- Authors: Hao Zhang; Yaru Niu; Yikai Wang; Ding Zhao; Eric H. Tseng
- Primary area: applications->robotics
- Keywords: human–robot collaboration;multi-agent reinforcement learning;rationality gap;Lyapunov policy optimization
- Source URL: https://openreview.net/forum?id=uBvlUE2wrP
- PDF URL: https://openreview.net/pdf?id=uBvlUE2wrP

## Abstract

To improve generalization and resilience in human–robot collaboration (HRC), robots must contend with diverse combinations of human behaviors and contexts, motivating multi-agent reinforcement learning (MARL). However, inherent heterogeneity between robots and humans creates a rationality gap (RG), where decentralized policy updates deviate from cooperative joint optimization. The resulting learning problem is a general-sum differentiable game, so independent policy-gradient updates can oscillate or diverge without added structure. We propose heterogeneous-agent Lyapunov policy optimization (HALO), a framework that stabilizes decentralized MARL by enforcing Lyapunov-based contraction in policy-parameter space. Unlike Lyapunov-based safe RL, which targets state/trajectory constraints in constrained Markov decision processes, HALO uses Lyapunov certification to stabilize decentralized policy learning. HALO rectifies decentralized gradients via optimal quadratic projections, ensuring monotonic contraction of RG and enabling effective exploration of open-ended interaction spaces. Extensive simulations and real-world humanoid-robot experiments show that this certified stability improves generalization and robustness in collaborative corner cases.

## One-Sentence Claim

HALO stabilizes human-robot MARL by enforcing Lyapunov-based contraction of the rationality gap in policy-parameter space, improving robust collaboration under heterogeneous human and robot behavior.

## Problem

Human-robot collaboration involves heterogeneous agents with different rationality, objectives, and behavior patterns. Independent decentralized policy-gradient updates can deviate from cooperative joint optimization, creating a rationality gap.

The resulting learning problem is a general-sum differentiable game where naive updates can oscillate or diverge. Robots need stable learning dynamics while still exploring open-ended interaction spaces.

## Core Contribution

The paper proposes Heterogeneous-Agent Lyapunov Policy Optimization. Unlike Lyapunov safe RL that constrains states or trajectories, HALO uses Lyapunov certification to stabilize decentralized policy learning itself.

HALO rectifies decentralized gradients through optimal quadratic projections, ensuring monotonic contraction of the rationality gap and improving generalization and robustness in collaborative corner cases.

## Method

HALO defines a Lyapunov function over policy-parameter dynamics tied to the rationality gap between decentralized updates and cooperative joint optimization. Gradient updates are projected into directions that certify contraction.

The projection is formulated as an optimal quadratic adjustment, minimally modifying decentralized gradients while enforcing stability. This lets agents explore while keeping learning dynamics from diverging.

## Experiments and Evidence

The abstract reports extensive simulations and real-world humanoid-robot experiments. Certified stability improves generalization and robustness in collaborative corner cases.

Full-paper reading should verify human-behavior models, robot platforms, real-world protocols, rationality-gap measurement, Lyapunov certificates, and comparison against centralized, independent, and safe-RL baselines.

## Limits and Failure Modes

Lyapunov contraction in policy-parameter space depends on how the rationality gap is defined and estimated. Human behavior can be nonstationary, strategic, or irrational in ways that violate assumptions.

Projection can also trade off learning speed for stability. In some collaboration tasks, overly constrained updates may prevent adaptation to genuinely novel human strategies.

## Deep Themes

- Stability of learning, not only behavior: HALO certifies decentralized update dynamics.
- Rationality gap as a coordination metric: heterogeneous agents need a measure of deviation from cooperative optimization.
- Lyapunov methods for MARL: control-theoretic stability tools migrate into policy learning.
- Human-robot robustness: collaboration requires handling corner cases, not only average simulated partners.

## Subthemes

- General-sum differentiable games can make independent gradients oscillate.
- Quadratic projections rectify policy gradients.
- Human and robot heterogeneity creates structural coordination difficulty.
- Real-world humanoid experiments raise the evidential bar.

## Connections to Other Papers

HALO connects to JoSE, WestWorld, ScaleMoE, and SOL in embodied/RL systems. It also relates to conformal policy control: both regulate policy improvement, but HALO targets decentralized learning stability while CPC targets deployment risk.

It fits the broader theme of importing control theory into ML training and deployment.

## Notes for Cross-Paper Synthesis

The synthesis point is that safe collaboration requires stable learning dynamics, not merely safe trajectories. In multi-agent settings, the update rule itself can be the hazard.
