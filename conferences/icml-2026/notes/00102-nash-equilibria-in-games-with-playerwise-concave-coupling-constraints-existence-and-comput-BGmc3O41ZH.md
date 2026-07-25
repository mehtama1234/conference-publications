# Nash Equilibria in Games with Playerwise Concave Coupling Constraints: Existence and Computation

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: BGmc3O41ZH
- Authors: Philip Jordan; Maryam Kamgarpour
- Primary area: theory->game_theory
- Keywords: Nash equilibrium;coupling constraints;log barrier methods;potential games;convex-concave games;optimization in games
- Source URL: https://openreview.net/forum?id=BGmc3O41ZH
- PDF URL: https://openreview.net/pdf?id=BGmc3O41ZH

## Abstract

We study the existence and computation of Nash equilibria in concave games where the players' admissible strategies are subject to shared coupling constraints. Under playerwise concavity of constraints, we prove existence of Nash equilibria. Our proof leverages topological fixed point theory and novel structural insights into the contractibility of feasible sets, and relaxes strong assumptions for existence in prior work. Having established existence, we address the question of whether in the presence of coupling constraints, playerwise independent learning dynamics have convergence guarantees. We address this positively for the class of potential games by designing a convergent algorithm. To account for the possibly nonconvex feasible region, we employ a log barrier regularized gradient ascent with adaptive stepsizes.  Starting from an initial feasible strategy profile and under exact gradient feedback, the proposed method converges to an $\epsilon$-approximate constrained Nash equilibrium within $\mathcal{O}(\epsilon^{-3})$ iterations.

## One-Sentence Claim

Nash equilibria exist in concave games with playerwise concave shared coupling constraints, and potential games in this class admit a convergent log-barrier gradient method.

## Problem

Shared coupling constraints can make feasible regions nonconvex and complicate both equilibrium existence and convergence of playerwise independent learning dynamics.

## Core Contribution

The paper proves existence of Nash equilibria under playerwise concavity, relaxes prior assumptions using topological fixed-point arguments, and gives an algorithm for constrained potential games.

## Method

The existence proof uses structural contractibility of feasible sets. For computation, it applies log-barrier regularized gradient ascent with adaptive step sizes from feasible initialization under exact gradient feedback.

## Experiments and Evidence

The abstract states an O(epsilon^-3) iteration guarantee for convergence to an epsilon-approximate constrained Nash equilibrium in the potential-game setting.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: constraint examples, exact concavity assumptions, feasibility initialization, gradient-feedback requirements, and numerical behavior.

## Deep Themes

- Game-theoretic learning needs constraints that reflect shared resources or couplings.
- Equilibrium existence can depend on feasible-set topology.
- Independent learning dynamics can be made convergent under structured potential games.

## Subthemes

- Nash equilibrium.
- Coupling constraints.
- Playerwise concavity.
- Potential games.
- Log-barrier methods.
- Topological fixed points.

## Connections to Other Papers

Connects to ParetoPO, multi-agent debate, non-cooperative LM safety games, and constrained optimization papers through game-theoretic views of learning systems.

## Notes for Cross-Paper Synthesis

This paper contributes a constrained-game theory thread: multi-agent optimization increasingly needs equilibrium concepts under realistic shared constraints.
