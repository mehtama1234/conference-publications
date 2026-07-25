# On Minimum Depth and Width of Floating-Point Neural Networks for Representing Floating-Point Functions

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 8IxY2DUiBi
- Authors: Sejun Park; Yeachan Park; Geonho Hwang
- Primary area: theory->deep_learning
- Keywords: Universal approximation;Minimum width and depth;Floating-point arithmetic
- Source URL: https://openreview.net/forum?id=8IxY2DUiBi
- PDF URL: https://openreview.net/pdf?id=8IxY2DUiBi

## Abstract

Research on the expressive power of neural networks has identified the minimum depth and width of neural networks that enable universal approximation and memorization. However, existing results are derived under exact arithmetic and cannot be directly applied to real implementations on computers, which can only use a finite set of numbers and inexact machine operations with round-off errors. 
In this work, we study floating-point ReLU networks that have floating-point parameters and use floating-point operations. Specifically, we investigate their minimum depth and width to represent all functions from the set of floating-point vectors $\mathbb F^d$ to the set of floating-point numbers $\mathbb F$. We first show that the minimum depth for representing all functions from $\mathbb F^d$ to $\mathbb F$ is exactly three, where two layers can be sufficient if we consider a smaller domain and/or codomain. We further show that the minimum width for representing all functions from $\mathbb F^d$ to $\mathbb F$ lies between $2d$ and $2d+4$. In addition, if we restrict the domain to non-negative floats, it lies between $d$ and $d+4$, where it can be smaller for a smaller domain, even beyond $d$.  Our results show that the existing results analyzed under exact arithmetic do not extend to the floating-point setup.

## One-Sentence Claim

Minimum depth and width results for neural-network expressivity change when networks are required to use actual floating-point parameters and operations.

## Problem

Universal approximation and memorization theory usually assumes exact real arithmetic, but implemented neural networks operate over finite floating-point sets with round-off behavior.

## Core Contribution

The paper studies floating-point ReLU networks representing all functions from floating-point vector domains to floating-point outputs, proving exact or near-tight minimum depth and width bounds.

## Method

It treats the domain and codomain as finite floating-point sets and analyzes representability under floating-point parameters and operations, rather than real-valued exact arithmetic.

## Experiments and Evidence

The abstract reports that minimum depth for representing all functions from F^d to F is exactly three, with two layers sufficient for smaller domains or codomains. It also places minimum width between 2d and 2d+4, or between d and d+4 for non-negative floating-point domains.

## Limits and Failure Modes

No confident local PDF/arXiv match yet, so proof details still need checking: the precise floating-point model, handling of rounding modes, whether subnormal values are included, and how bounds depend on restricted domains/codomains.

## Deep Themes

- Expressivity theory changes under real implementation arithmetic.
- Finite numerical domains can invalidate exact-arithmetic intuitions.
- Hardware-level constraints belong inside theoretical models when representability is the question.

## Subthemes

- Floating-point ReLU networks.
- Minimum depth.
- Minimum width.
- Universal representation over finite domains.
- Round-off-aware theory.
- Exact arithmetic mismatch.

## Connections to Other Papers

Connects to size-sensitive matroid oracle theory and low-precision training work through a shared theme: theoretical statements change when the computational model reflects actual implementation costs or arithmetic.

## Notes for Cross-Paper Synthesis

This paper reinforces the implementation-aware theory theme: classical expressivity claims do not automatically survive the move from real numbers to machine arithmetic.
