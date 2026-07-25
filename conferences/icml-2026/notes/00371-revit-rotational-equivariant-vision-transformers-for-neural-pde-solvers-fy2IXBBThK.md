# ReViT: Rotational-equivariant Vision Transformers for Neural PDE Solvers

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: fy2IXBBThK
- Authors: Hao Wei; Björn List; Nils Thuerey
- Primary area: applications->chemistry_physics_and_earth_sciences
- Keywords: Machine learning for sciences;Rotational equivariant networks;Neural PDE solvers
- Source URL: https://openreview.net/forum?id=fy2IXBBThK
- PDF URL: https://openreview.net/pdf?id=fy2IXBBThK

## Abstract

Physics obeys strict symmetries like rotational equivariance. However, the standard Transformer architectures widely used in physics foundation models do not enforce these constraints by construction. We introduce ReViT, a rotationally equivariant Vision Transformer framework for neural PDE solvers operating on grid-based physical fields that achieves exact equivariance for the discrete groups $C_4$ (2D) and the chiral octahedral group $O$ (3D), with bounded approximate $\mathrm{SO}(d)$ equivariance for continuous rotations. ReViT maps scalar and vector inputs into locally invariant representations derived from physics-based canonical bases, enabling the use of standard self-attention without symmetry violations. Built on a hierarchical Swin-style backbone with a precomputed reference basis pyramid, ReViT preserves equivariance across multi-scale operations. 
We evaluate ReViT on a wide range of 2D and 3D PDE benchmarks, such as Magnetohydrodynamics and Turbulent Channel Flows, demonstrating significant gains over state-of-the-art baselines. ReViT exhibits strong generalization, and reduces MSE by up to 65\% compared with the best-performing alternatives.

## One-Sentence Claim

ReViT builds rotational equivariance into Vision Transformers for grid-based PDE fields, improving scientific generalization by preventing symmetry violations in attention backbones.

## Problem

Physical systems obey symmetries such as rotational equivariance, but standard Transformer architectures used in physics foundation models do not enforce those constraints. This can waste data, weaken generalization, and produce predictions that violate known physics.

The paper asks how to retain the flexibility of Vision Transformers while guaranteeing the rotation behavior required by PDE fields.

## Core Contribution

The contribution is ReViT, a rotationally equivariant Vision Transformer framework for neural PDE solvers. It achieves exact equivariance for discrete rotation groups C4 in 2D and chiral octahedral group O in 3D, with bounded approximate SO(d) equivariance for continuous rotations.

ReViT maps scalar and vector fields into locally invariant representations using physics-based canonical bases, then applies standard self-attention without breaking the symmetry.

## Method

The method constructs local invariant representations from canonical bases and uses a hierarchical Swin-style backbone. A precomputed reference-basis pyramid preserves equivariance across multi-scale operations.

This design isolates the symmetry-handling layer from the attention computation: self-attention operates on representations already made safe with respect to rotations.

## Experiments and Evidence

Evidence reported in the abstract:

- 2D and 3D PDE benchmarks.
- Tasks including magnetohydrodynamics and turbulent channel flows.
- Significant gains over state-of-the-art baselines.
- Strong generalization.
- MSE reductions up to 65% compared with best-performing alternatives.
- Exact equivariance for C4 and O, and bounded approximate SO(d) equivariance.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: benchmark splits, vector-field handling, basis construction, and compute overhead.

## Limits and Failure Modes

- Exact guarantees cover discrete groups; continuous rotations are only approximately bounded.
- Canonical-basis construction may be domain- or grid-dependent.
- Strong symmetry constraints can be harmful if data or boundary conditions break the assumed symmetry.
- Multi-scale equivariant infrastructure may add implementation complexity.

## Deep Themes

**Symmetry is a scientific prior.** ReViT encodes known physics into the architecture rather than asking data to learn it.

**Transformers can be made physics-compatible.** The paper keeps attention but changes the representation entering attention.

**Generalization comes from respecting invariances.** PDE solvers benefit when architecture and governing equations share symmetry structure.

## Subthemes

- Rotational-equivariant Vision Transformers.
- Canonical basis representations.
- Grid-based PDE solvers.
- Discrete and approximate continuous equivariance.
- Physics foundation-model architecture.

## Connections to Other Papers

Connects to LoRFS, Dirac-Frenkel-Onsager dynamics, OENN/CENN, Symmetry ICL Dynamics, and Modern Conservation Laws. All use mathematical structure to make neural systems respect the domain rather than relearn it.

## Notes for Cross-Paper Synthesis

ReViT strengthens the scientific-ML pattern: the most reliable architectures in physical domains increasingly hard-code symmetry, basis, or conservation structure before scaling model size.
