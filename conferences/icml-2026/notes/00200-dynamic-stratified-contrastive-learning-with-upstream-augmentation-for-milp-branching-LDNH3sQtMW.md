# Dynamic Stratified Contrastive Learning with Upstream Augmentation for MILP Branching

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: LDNH3sQtMW
- Authors: Tongkai Lu; Shuai Ma; Chongyang Tao
- Primary area: optimization->discrete_and_combinatorial_optimization
- Keywords: Mixed-Integer Linear Programming (MILP); Learning-Based Branching; Upstream-Augmented MILP Derivation; Dynamic Stratified Contrastive Learning
- Source URL: https://openreview.net/forum?id=LDNH3sQtMW
- PDF URL: https://openreview.net/pdf?id=LDNH3sQtMW

## Abstract

Mixed Integer Linear Programming (MILP) is a fundamental NP-hard problem that has garnered significant attention from both academia and industry.
The Branch-and-Bound (B&B) algorithm is the dominant approach for solving MILPs, where branching decisions play a critical role and have recently been enhanced by neural methods.
However, these methods still struggle with semantic variation across depths, the scarcity of upstream nodes, and the costly collection of strong branching samples. 
To address these issues, we propose SC-MILP, a Dynamic Stratified  Contrastive Training Framework for MILP Branching.
Our method groups B&B nodes based on their feature distributions and learns depth-aware, fine-grained node representations through dynamic stratified contrastive training.
To address data scarcity and imbalance at upstream nodes, we introduce an upstream-augmented MILP derivation procedure that generates both theoretically equivalent and perturbed instances.
Experiments on both synthetic and real-world MILP benchmarks, including large-scale instances, show that SC-MILP significantly improves branching accuracy, reduces solving time, with particularly strong gains at upstream nodes.

## One-Sentence Claim

SC-MILP improves learning-based MILP branching with dynamic stratified contrastive representations and upstream-augmented instance derivations.

## Problem

Neural branching methods for branch-and-bound struggle with semantic variation across search depths, scarce upstream nodes, and expensive strong-branching supervision.

## Core Contribution

The paper proposes a contrastive training framework that groups B&B nodes by feature distributions, learns depth-aware node representations, and augments upstream data with equivalent and perturbed MILP instances.

## Method

SC-MILP dynamically stratifies nodes, trains fine-grained depth-aware representations contrastively, and uses upstream-augmented MILP derivation to create more supervision for early branch-and-bound decisions.

## Experiments and Evidence

The abstract reports improved branching accuracy and reduced solving time on synthetic and real-world MILP benchmarks, including large-scale instances, with particularly strong upstream-node gains.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: MILP families, strong-branching sample cost, augmentation validity, solver integration, large-instance runtime, and generalization across problem distributions.

## Deep Themes

- Optimization learning needs depth-aware representations of solver state.
- Data augmentation can target scarce but strategically important search regions.
- Contrastive structure can improve decision policies in combinatorial solvers.

## Subthemes

- Mixed-integer linear programming.
- Branch-and-bound.
- Learning-based branching.
- Stratified contrastive learning.
- Upstream node augmentation.
- Large-scale combinatorial optimization.

## Connections to Other Papers

Connects to decision-focused optimization, graph/algorithm learning, and data augmentation papers that improve learned solvers by structuring state representations and scarce supervision.

## Notes for Cross-Paper Synthesis

SC-MILP adds a solver-in-the-loop learning theme: ML improves classical optimization when it targets the high-leverage decision points where data are scarce and errors compound.
