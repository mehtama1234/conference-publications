# Pinet: Optimizing hard-constrained neural networks with orthogonal projection layers

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: EJ680UQeZG
- Authors: Panagiotis D. Grontas; Antonio Terpin; Efe C. Balta; Raffaello D'Andrea; John Lygeros
- Primary area: optimization
- Keywords: hard constrained neural networks;network architecture;implicit layers;operator splitting;optimization
- Source URL: https://openreview.net/forum?id=EJ680UQeZG
- PDF URL: https://openreview.net/pdf?id=EJ680UQeZG

## Abstract

We introduce an output layer for neural networks that ensures satisfaction of convex constraints. Our approach, $\Pi$net, leverages operator splitting for rapid and reliable projections in the forward pass, and the implicit function theorem for backpropagation. We deploy $\Pi$net as a feasible-by-design optimization proxy for parametric constrained optimization problems and obtain modest-accuracy
solutions faster than traditional solvers when solving a single problem, and significantly faster for a batch of problems. 
We surpass state-of-the-art learning approaches by orders of magnitude in terms of training time, solution quality, and robustness to hyperparameter tuning, while maintaining similar inference times. Finally, we tackle multi-vehicle motion planning with non-convex trajectory preferences and provide $\Pi$net as a GPU-ready package implemented in JAX.

## One-Sentence Claim

Pi-net adds an orthogonal projection output layer so neural networks produce convex-constraint-feasible outputs by design while remaining trainable through implicit differentiation.

## Problem

Neural networks used as optimization proxies can be fast but may violate hard constraints, which is unacceptable in constrained optimization and planning.

Traditional solvers ensure feasibility but can be slow, especially for batches of parametric problems.

## Core Contribution

The paper introduces Pi-net, an output layer that enforces convex constraints through projection.

It uses operator splitting for reliable projections in the forward pass and the implicit function theorem for backpropagation, yielding feasible-by-design neural optimization proxies.

## Method

Pi-net appends a projection layer that maps network outputs onto the feasible set defined by convex constraints. Operator splitting makes the projection fast and stable.

Backpropagation through the projection is handled with implicit differentiation, allowing end-to-end training.

## Experiments and Evidence

The abstract reports modest-accuracy solutions faster than traditional solvers for single problems and much faster for batches.

It claims orders-of-magnitude improvements over state-of-the-art learning approaches in training time, solution quality, and robustness to hyperparameter tuning, with similar inference times. It also tackles multi-vehicle motion planning with non-convex trajectory preferences and provides a GPU-ready JAX package.

## Limits and Failure Modes

The hard feasibility guarantee applies to convex constraints; non-convex preferences are handled separately and may not be guaranteed. Projection cost can still grow with constraint complexity.

Because this note is abstract-only, details still need checking: constraint classes, operator-splitting method, projection accuracy, implicit-gradient stability, benchmark problems, and motion-planning formulation.

## Deep Themes

- Feasible-by-design learning: constraints should be built into outputs, not only penalized.
- Projection layers as optimization primitives: neural networks can call structured solvers internally.
- Implicit differentiation for constrained architectures: training can pass through solver layers.
- Batch optimization acceleration: learned proxies matter most when solving many related constrained problems.

## Subthemes

- Orthogonal projection output layer.
- Operator splitting.
- Convex hard constraints.
- Multi-vehicle motion planning.

## Connections to Other Papers

This connects to conformal policy control, safe generation, robust nonlinear systems, and control-barrier methods through hard constraints in learned systems.

It also relates to scientific/systems papers where solver structure is integrated into neural models rather than replaced.

## Notes for Cross-Paper Synthesis

Pi-net adds a constraint-in-the-architecture theme: reliability improves when feasibility is enforced structurally rather than hoped for through training loss.
