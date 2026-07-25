# CSPO: Constraint-Sensitive Policy Optimization for Safe Reinforcement Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 3ySR3TCMRP
- Authors: Ayoub Belouadah; Sylvain KUBLER; YVES LE TRAON
- Primary area: reinforcement_learning->deep_rl
- Keywords: Safe Reinforcement Learning;CMDP;Primal-dual optimization;Policy optimization
- Source URL: https://openreview.net/forum?id=3ySR3TCMRP
- PDF URL: https://openreview.net/pdf?id=3ySR3TCMRP

## Abstract

Safe reinforcement learning (Safe RL) aims to maximize expected return while satisfying safety constraints, typically modeled as Constrained Markov Decision Processes (CMDPs). While primal-dual methods scale well to deep RL, they often suffer from delayed constraint correction, leading to oscillatory behavior and prolonged safety violations. In this paper, we propose *Constraint-Sensitive Policy Optimization (CSPO)*, a first-order primal-dual method that incorporates local constraint sensitivity into policy updates. CSPO augments the primal objective with a constraint-sensitive correction derived from the shortest signed distance to the safety boundary, enabling smarter recovery steps back to safety, compensating for delayed Lagrange multiplier updates, reducing oscillations near the boundary, and preserving the KKT solutions of the original constrained problem. Experiments on navigation and locomotion benchmarks demonstrate that CSPO achieves faster safety recovery and high reward preservation, resulting in higher constrained returns compared to state-of-the-art primal-dual and penalty-based methods.

## One-Sentence Claim

CSPO improves safe RL recovery by scaling primal-dual policy updates with local constraint sensitivity derived from signed distance to the safety boundary.

## Problem

Primal-dual safe RL methods scale to deep CMDPs but often correct constraint violations late, causing oscillations near safety boundaries and prolonged unsafe behavior.

## Core Contribution

The paper proposes Constraint-Sensitive Policy Optimization, a first-order primal-dual method that augments the objective with a local safety-boundary correction while preserving the original constrained problem's KKT solutions.

## Method

CSPO uses the shortest signed distance to the feasible set and the norm/local sensitivity of constraint gradients to adjust recovery updates. The practical implementation adds a constraint-sensitive surrogate term to policy optimization while retaining primal-dual structure.

## Experiments and Evidence

The abstract reports faster safety recovery and high reward preservation on navigation and locomotion benchmarks, yielding higher constrained returns than primal-dual and penalty-based baselines.

## Full-Text Upgrade

The full text states the geometric intuition clearly: uniform primal-dual corrections can overshoot in high-sensitivity regions or recover too slowly in low-sensitivity regions. CSPO scales the correction by local constraint sensitivity, making feasibility recovery more stable and task-aware.

The empirical protocol evaluates nine continuous-control safety tasks from Safety Gymnasium, including five locomotion and four navigation tasks. Besides final constrained return, the paper tracks recovery dynamics with time to safety, reward preservation during recovery, and violation frequency. The authors report that CSPO is especially strong in navigation tasks and reduces oscillatory cost dynamics while remaining competitive in locomotion tasks.

## Limits and Failure Modes

Limits to watch: CSPO introduces an additional safety-recovery aggressiveness parameter; normalization affects behavior; stronger recovery can trade off against reward in high-sensitivity regions; and the method is still validated primarily on benchmark CMDPs.

## Deep Themes

- Safe RL needs recovery dynamics, not only final constraint satisfaction.
- Local geometry of constraints can improve primal-dual optimization.
- Safety algorithms are becoming more boundary-aware and process-aware.

## Subthemes

- Safe reinforcement learning.
- CMDPs.
- Primal-dual policy optimization.
- Safety-boundary distance.
- Constraint sensitivity.
- Recovery metrics.

## Connections to Other Papers

Connects to Rare Event Analysis and Pressure Reveals Character through evaluation beyond aggregate success: safety depends on how violations happen and how systems recover. It also links to DiReCT through gradient-geometry-guided updates.

## Notes for Cross-Paper Synthesis

CSPO adds a control/optimization version of the process-evaluation theme: safe behavior is about trajectories around failure boundaries, not just endpoint metrics.
