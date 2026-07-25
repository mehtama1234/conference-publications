# HATSolver: Learning Gröbner Bases with Hierarchical Attention Transformers

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 5C3LljOEGC
- Authors: Mohamed Malhou; Ludovic Perret; Kristin E. Lauter
- Primary area: other topics in machine learning (i.e., none of the above)
- Keywords: Hierarchical Attention Transformer;Groebner Basis;Symbolic Computation;Multivariate Polynomial Equations
- Source URL: https://openreview.net/forum?id=5C3LljOEGC
- PDF URL: https://openreview.net/pdf?id=5C3LljOEGC

## Abstract

At NeurIPS 2024, Kera (2311.12904) introduced the use of transformers for computing Groebner bases, a central object in computer algebra with numerous practical applications. In this paper, we improve this approach by applying Hierarchical Attention Transformers (HATs) to solve systems of multivariate polynomial equations via Groebner bases computation. The HAT architecture incorporates a tree-structured inductive bias that enables the modeling of hierarchical relationships present in the data and thus achieves significant computational savings compared to conventional flat attention models. We generalize to arbitrary depths and include a detailed computational cost analysis. Combined with curriculum learning, our method solves instances that are much larger than those in Kera (2311.12904).

## One-Sentence Claim

HATSolver improves transformer-based Groebner basis computation by using hierarchical attention to exploit tree-structured relationships in polynomial systems and scale beyond prior flat-attention approaches.

## Problem

Computing Groebner bases is central in computer algebra but can be computationally hard, and prior transformer approaches such as Kera were limited in scale and did not fully exploit hierarchical structure.

## Core Contribution

The paper applies Hierarchical Attention Transformers to systems of multivariate polynomial equations, generalizes the architecture to arbitrary depths, and analyzes computational cost.

## Method

HATSolver uses a tree-structured inductive bias in attention to model hierarchical relationships in polynomial data. It combines this architecture with curriculum learning to solve larger instances.

## Experiments and Evidence

The abstract reports significant computational savings over flat attention and successful solution of instances much larger than those in Kera.

## Limits and Failure Modes

No confident local PDF/arXiv match yet. Checks needed: polynomial families, term ordering, exactness versus approximate generation, symbolic verification, and generalization to real algebra-system workloads.

## Deep Themes

- Transformers are entering symbolic computation domains.
- Inductive bias matters when applying neural models to formal algebra.
- Curriculum learning is a route to scaling formal problem solving.

## Subthemes

- Groebner bases.
- Hierarchical attention.
- Symbolic computation.
- Polynomial systems.
- Neural algebra solvers.

## Connections to Other Papers

Connects to theorem/proof/formal reasoning and solver-neural hybrids, including LSFlow and Quotient-Space Diffusion as examples of neural methods respecting formal structure.

## Notes for Cross-Paper Synthesis

HATSolver expands the structured-reasoning theme into computer algebra: neural models are being paired with domain-specific structure rather than used as generic sequence predictors.
