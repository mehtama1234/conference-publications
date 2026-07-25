# Gradient Flow Through Diagram Expansions: Learning Regimes and Explicit Solutions

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: BXE3Z0EHCs
- Authors: Dmitry Yarotsky; Eugene Golikov; Yaroslav Gusev
- Primary area: theory->learning_theory
- Keywords: gradient flow;tensor decomposition;CP decomposition;feature learning;analytic solutions;generating functions;diagram expansion;wide networks
- Source URL: https://openreview.net/forum?id=BXE3Z0EHCs
- PDF URL: https://openreview.net/pdf?id=BXE3Z0EHCs

## Abstract

We develop a general mathematical framework to analyze scaling regimes and derive explicit analytic solutions for gradient flow (GF) in large learning problems. Our key innovation is a formal power series expansion of the loss evolution, with coefficients encoded by diagrams akin to Feynman diagrams. We show that this expansion has a well-defined large-size limit that can be used to reveal different learning phases and, in some cases, to obtain explicit solutions of the nonlinear GF. We focus on learning Canonical Polyadic (CP) decompositions of high-order tensors, and show that this model has several distinct extreme lazy and rich GF regimes such as free evolution, NTK and under- and over-parameterized mean-field. We show that these regimes depend  on the parameter scaling, tensor order, and symmetry of the model in a specific and subtle way. Moreover, we propose a general approach to summing the formal loss expansion by reducing it to a PDE; in a wide range of scenarios, it turns out to be first-order and solvable by the method of characteristics. We observe a very good agreement of our theoretical predictions with experimental results.

## One-Sentence Claim

Diagram-expansion power series can characterize large-system gradient-flow regimes and sometimes yield explicit nonlinear learning dynamics through PDE reductions.

## Problem

Large learning problems can exhibit different lazy, rich, mean-field, and NTK-like regimes, but deriving explicit gradient-flow solutions and phase distinctions is mathematically difficult.

## Core Contribution

The paper develops a diagrammatic formal power series framework for loss evolution under gradient flow, with a well-defined large-size limit and explicit solutions in tensor CP decomposition settings.

## Method

It encodes loss-evolution coefficients with Feynman-like diagrams, studies their large-size limits, and sums the resulting expansion by reducing it to a PDE, often first-order and solvable by characteristics.

## Experiments and Evidence

The abstract reports theoretical predictions matching experiments and identifies distinct extreme lazy/rich regimes, including free evolution, NTK, and under/over-parameterized mean-field regimes.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: convergence of formal series, CP-decomposition assumptions, PDE solvability scope, and relevance to practical neural architectures.

## Deep Themes

- Learning dynamics can be analyzed through physics-style diagram expansions.
- Parameter scaling and symmetry determine whether training is lazy or feature-learning-rich.
- Explicit solutions are possible in structured high-dimensional learning models.

## Subthemes

- Gradient flow.
- Diagram expansion.
- CP tensor decomposition.
- NTK and mean-field regimes.
- Generating functions.
- Analytic learning dynamics.

## Connections to Other Papers

Connects to LoRA convergence, gradient-flow diagram expansions, grokking theory, and implementation-aware theory papers through practice-facing optimization dynamics.

## Notes for Cross-Paper Synthesis

This paper strengthens the learning-dynamics theme: modern theory is mapping training regimes by deriving explicit dynamics, not only proving endpoint guarantees.
