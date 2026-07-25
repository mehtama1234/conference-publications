# Geometric and Stochastic Analysis of Discontinuities in Sparse Mixture-of-Experts

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: AyrNR1ExN5
- Authors: Tho Tran Huu; Huu-Tuan Nguyen; Thien-Hai Nguyen; Nhat-Tri Ho; Viet-Hoang Tran; Tho Quan; Tan Minh Nguyen
- Primary area: deep_learning->theory
- Keywords: Discontinuities in Mixture of Expert;Stochastic Analysis
- Source URL: https://openreview.net/forum?id=AyrNR1ExN5
- PDF URL: https://openreview.net/pdf?id=AyrNR1ExN5

## Abstract

Sparse Mixture-of-Experts (SMoE) architectures are now widely deployed in state-of-the-art language and vision models, where conditional routing allows scaling to very large networks. However, this very Top-$k$ expert selection that enables conditional routing also renders the SMoE map inherently discontinuous. In the vicinity of these discontinuity surfaces, even inputs that are arbitrarily close may activate substantially different sets of experts resulting in significantly different outputs. In this work we give a rigorous geometric and stochastic analysis of these discontinuities. We first classify them by order, determined by the number of tied experts at a switching event. Using measure-theoretic slicing arguments, we establish asymptotic volume estimates for the thickened discontinuity surfaces, showing that lower-order discontinuity sets dominate, whereas higher-order ones occupy a vanishingly small relative volume. Next, modeling random perturbations in the input space via a diffusion process, we prove that the path eventually encounter a discontinuity, and moreover that the first hit almost surely occurs on an order-1 discontinuity with explicit finite-time probability bounds. We further derive occupation-time bounds that quantify the duration the random path spend in the neighborhoods of each discontinuity order. These theoretical results imply that inputs are more likely to lie near lower order discontinuities. Motivated by this insight, we propose a simple smoothing mechanism that can be directly applied to existing SMoEs, softly incorporating experts near discontinuities; our analysis guarantees that the added computational overhead remains small while providing localized smoothing near discontinuities, and experiments across language and vision tasks show that smoothing not only enforces continuity of the SMoE map but also enhances empirical performance.

## One-Sentence Claim

Sparse MoE top-k routing creates geometric discontinuity surfaces, and localized smoothing near the dominant low-order discontinuities can improve continuity and empirical performance with small overhead.

## Problem

Top-k expert selection enables conditional computation but makes the SMoE input-output map discontinuous, so nearby inputs can trigger different expert sets and sharply different outputs.

## Core Contribution

The paper gives a geometric and stochastic analysis of SMoE discontinuities by order, proves volume and hitting-time properties, and proposes a smoothing mechanism for existing sparse MoEs.

## Method

It classifies discontinuities by the number of tied experts at switching events, estimates thickened discontinuity-surface volumes with measure-theoretic slicing, and models random input perturbations as diffusion paths to analyze first hits and occupation time near discontinuities.

## Experiments and Evidence

The abstract reports that lower-order discontinuities dominate volume and are almost surely the first encountered under random perturbations. Experiments across language and vision tasks show smoothing enforces continuity and improves performance.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: smoothing formula, router/top-k variants, overhead measurement, benchmark coverage, and interaction with expert load balancing.

## Deep Themes

- Conditional computation creates discontinuities that need geometric analysis.
- Robustness around routing boundaries matters for deployed sparse models.
- Local smoothing can target the high-probability boundary cases rather than all experts.

## Subthemes

- Sparse MoE.
- Top-k routing.
- Discontinuity surfaces.
- Stochastic perturbations.
- Local smoothing.
- Conditional computation.

## Connections to Other Papers

Connects to TetraJet-v2, SSO, and optimization-stability papers through hidden failure modes in scalable LLM architectures. It also links to dynamical/stochastic analyses in Thinking in Flow and graph oversmoothing work.

## Notes for Cross-Paper Synthesis

This paper adds a routing-boundary theme: scaling through sparsity introduces non-smooth geometry that becomes a first-class object of analysis.
