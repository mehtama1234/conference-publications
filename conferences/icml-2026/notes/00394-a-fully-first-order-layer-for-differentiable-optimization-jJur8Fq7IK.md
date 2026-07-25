# A Fully First-Order Layer for Differentiable Optimization

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: jJur8Fq7IK
- Authors: Zihao Zhao; Kai-Chia Mo; Shing-Hei Ho; Brandon Amos; Kai Wang
- Primary area: optimization->convex
- Keywords: differentiable optimization;first-order oracle;bilevel optimization;perturbation
- Source URL: https://openreview.net/forum?id=jJur8Fq7IK
- PDF URL: https://openreview.net/pdf?id=jJur8Fq7IK

## Abstract

Differentiable optimization studies how to embed a mathematical program as a differentiable layer in machine learning pipelines. However, existing approaches typically rely on implicit differentiation, involving expensive Hessian computation while differentiating through optimality conditions. To address this challenge, we formulate the differentiable optimization problem as a bilevel optimization instance.
We construct a new active-set Lagrangian as a proxy to compute an $\epsilon$-approximate hypergradient using only near-constant $O(\log (1/\epsilon))$ first-order information. We also show that applying this efficient hypergradient oracle to constrained bilevel optimization improves the overall gradient complexity to $\tilde{O}(\delta^{-1}\epsilon^{-3})$ to reach a $(\delta, \epsilon)$-Goldstein stationary point. We implement our method `FFOLayer`, as a drop-in Python library compatible with existing differentiable optimization solvers. Our algorithm shows significantly faster computation with similar convergence compared to other existing solvers. The source code is available at [https://github.com/GT-KOALA/FFOLayer](https://github.com/GT-KOALA/FFOLayer).

## One-Sentence Claim

FFOLayer differentiates through optimization layers using near-constant first-order information, avoiding expensive Hessian-based implicit differentiation while preserving similar convergence.

## Problem

Differentiable optimization layers embed mathematical programs inside ML pipelines, but differentiating through optimality conditions often requires implicit differentiation and expensive Hessian computations. This is a barrier for bilevel and constrained learning systems.

The paper asks whether hypergradients for optimization layers can be computed efficiently using only first-order oracle information.

## Core Contribution

The paper formulates differentiable optimization as a bilevel optimization problem and constructs an active-set Lagrangian proxy to compute epsilon-approximate hypergradients with near-constant O(log(1/epsilon)) first-order information.

It also gives a gradient-complexity improvement for constrained bilevel optimization and implements FFOLayer as a drop-in Python library compatible with existing differentiable optimization solvers.

## Method

FFOLayer avoids Hessian-based implicit differentiation by using a first-order hypergradient oracle derived from an active-set Lagrangian proxy. The oracle approximates the sensitivity of the optimization solution to upstream parameters.

This hypergradient is then plugged into constrained bilevel optimization, targeting a Goldstein stationary point with improved complexity.

## Experiments and Evidence

Evidence reported in the abstract:

- Epsilon-approximate hypergradient using O(log(1/epsilon)) first-order information.
- Gradient complexity of roughly O~(delta^-1 epsilon^-3) for constrained bilevel optimization to reach a (delta, epsilon)-Goldstein stationary point.
- FFOLayer implemented as a drop-in Python library.
- Compatibility with existing differentiable optimization solvers.
- Significantly faster computation with similar convergence compared to existing solvers.
- Code release at the listed GitHub URL.

Source depth is abstract/metadata only; full details needed for problem class, active-set assumptions, and benchmark tasks.

## Limits and Failure Modes

- Active-set identification can be delicate near degenerate constraints.
- Approximate hypergradients may accumulate error in deep or repeated optimization layers.
- First-order efficiency may trade off with accuracy in ill-conditioned problems.
- Goldstein stationarity is useful for nonsmooth settings but may not match all application metrics.

## Deep Themes

**Differentiable optimization needs cheaper sensitivity.** Hypergradients are the computational bottleneck.

**First-order oracles are becoming infrastructure.** The paper turns expensive implicit differentiation into a library-level first-order layer.

**Optimization layers are part of model architecture.** Making them cheaper expands where structured solvers can be embedded.

## Subthemes

- Differentiable optimization layers.
- First-order hypergradients.
- Bilevel optimization.
- Active-set Lagrangian proxy.
- Hessian-free implicit sensitivity.

## Connections to Other Papers

Connects to Asymmetric Perturbation, Constrained Transformers, FlowOptimizer, and optimization-theory papers. It also relates to systems-efficiency papers because it makes structured optimization practical inside ML models.

## Notes for Cross-Paper Synthesis

FFOLayer strengthens the "structure inside the network" theme: optimization solvers can be differentiable components if their sensitivity computation is made cheap enough.
