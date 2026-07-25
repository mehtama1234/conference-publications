# Optimal and Scalable MAPF via Multi-Marginal Optimal Transport and Schrödinger Bridges

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: Cxdj2GYZ4c
- Authors: Usman Khan; Joseph W Durham
- Primary area: optimization->discrete_and_combinatorial_optimization
- Keywords: Multiagent Path Finding;Optimal Transport;Schrodinger Bridge;Multimarginal Sinkhorn
- Source URL: https://openreview.net/forum?id=Cxdj2GYZ4c
- PDF URL: https://openreview.net/pdf?id=Cxdj2GYZ4c

## Abstract

We consider anonymous multi-agent path finding (MAPF) where a set of robots is tasked to travel to a set of targets on a finite, connected graph. We show that MAPF can be cast as a special class of multi-marginal optimal transport (MMOT) problems with an underlying Markovian structure, under which the exponentially large MMOT collapses to a linear program (LP) polynomial in size. Focusing on the anonymous setting, we establish conditions under which the corresponding LP is feasible, totally unimodular, and yields min-cost, integral~$(\{0,1\})$ transports that do not overlap in both space and time. To adapt the approach to large-scale problems, we cast the MAPF-MMOT in a probabilistic framework via Schrödinger bridges. Under standard assumptions, we show that the Schrödinger bridge formulation reduces to an entropic regularization of the corresponding MMOT that admits an iterative Sinkhorn-type solution. The Schrödinger bridge, being a probabilistic framework, provides a shadow (fractional) transport that we use as a template to solve a reduced LP and demonstrate that it results in near-optimal, integral transports at a significant reduction in complexity. Extensive experiments highlight the optimality and scalability of the proposed approaches.

## One-Sentence Claim

Anonymous multi-agent path finding can be formulated as structured multi-marginal optimal transport, then scaled with Schrödinger bridge regularization and Sinkhorn-style solvers.

## Problem

MAPF requires assigning many robots to targets without space-time collisions, but exact formulations can become combinatorially large and difficult to scale.

## Core Contribution

The paper casts anonymous MAPF as Markov-structured MMOT that collapses to a polynomial-size LP, proves integrality conditions, and introduces a scalable Schrödinger bridge approximation.

## Method

The exact formulation uses a MAPF-MMOT LP that can be feasible, totally unimodular, and min-cost integral under stated conditions. The scalable variant entropically regularizes the MMOT as a Schrödinger bridge, solves it with iterative Sinkhorn updates, and uses the fractional transport to form a reduced LP.

## Experiments and Evidence

The abstract reports extensive experiments showing optimality and scalability, with near-optimal integral transports at substantially reduced complexity.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: graph assumptions, target anonymity limits, collision constraints, Sinkhorn convergence, and reduced-LP rounding behavior.

## Deep Themes

- Multi-agent planning can be reframed as transport over space-time.
- Entropic bridges provide scalable approximations to combinatorial routing.
- Fractional probabilistic plans can guide exact reduced optimization.

## Subthemes

- Multi-agent path finding.
- Multi-marginal optimal transport.
- Schrödinger bridges.
- Sinkhorn algorithms.
- Collision-free routing.
- Anonymous robot assignment.

## Connections to Other Papers

Connects to OSM+ traffic policy control, constrained games, robotics/world-model evaluation, and optimal-transport generative methods through scalable multi-agent coordination.

## Notes for Cross-Paper Synthesis

This paper strengthens the transport-as-coordination theme: large multi-agent motion problems can be solved by exploiting probabilistic transport structure.
