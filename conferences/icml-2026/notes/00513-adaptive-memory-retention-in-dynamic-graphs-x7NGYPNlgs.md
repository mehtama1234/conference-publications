# Adaptive Memory Retention in Dynamic Graphs

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: x7NGYPNlgs
- Authors: Fabrizio De Castelli; Alessio Gravina; Moshe Eliasof; Carola-Bibiane Schönlieb; Davide Bacciu
- Primary area: deep_learning->graph_neural_networks
- Keywords: Long-Range Propagation;Snapshot-based Dynamic Graphs;Graph Neural Networks
- Source URL: https://openreview.net/forum?id=x7NGYPNlgs
- PDF URL: https://openreview.net/pdf?id=x7NGYPNlgs

## Abstract

Modeling graphs demands a careful balance between long-range propagation of information across nodes and the controlled dissipation of noisy or redundant signals to ensure stable learning and generalization. This challenge is exacerbated in dynamic graphs, where structural and temporal information interact, leading to uncontrolled information accumulation and amplifying noise, thereby affecting generalization. We introduce LAMP, a dynamic graph model for snapshot-based dynamic graphs that incorporates adaptive, learned dissipation within a principled dynamical systems framework. Our architecture combines impulsive neural ODEs with an antisymmetric parameterization to model conservative information flow, alongside data-driven dissipative dynamics that regulate information retention over space and time. This formulation yields stable yet expressive representations and enables effective long-range dependency modeling while avoiding pathological information buildup. We provide a theoretical analysis establishing stability guarantees and characterizing the representational power. Extensive experiments on synthetic and real-world benchmarks demonstrate state-of-the-art performance, particularly on tasks requiring extended-range dependency modeling.

## One-Sentence Claim

LAMP improves dynamic graph learning by combining conservative information flow with learned dissipation so useful long-range signals persist while noisy accumulated memory decays.

## Problem

Dynamic graphs require information to propagate across nodes and time, but uncontrolled accumulation can amplify noise and redundant signals. This creates instability and hurts generalization.

The problem is balancing long-range dependency modeling against memory dissipation in settings where graph structure and temporal evolution interact.

## Core Contribution

The paper introduces LAMP, a snapshot-based dynamic graph model with adaptive learned dissipation inside a principled dynamical systems framework.

Its core contribution is to separate conservative information flow from dissipative regulation, yielding stable but expressive dynamic graph representations.

## Method

LAMP combines impulsive neural ODEs with an antisymmetric parameterization to model conservative information flow. It then adds data-driven dissipative dynamics that regulate how information is retained over space and time.

This design aims to preserve long-range useful dependencies while preventing pathological information buildup.

## Experiments and Evidence

The abstract reports theoretical stability guarantees and characterization of representational power.

Experiments on synthetic and real-world benchmarks show state-of-the-art performance, especially on tasks requiring extended-range dependency modeling.

## Limits and Failure Modes

The method may depend on snapshot granularity, ODE solver choices, and whether the learned dissipation can distinguish noise from rare long-range signal.

Because this note is abstract-only, details still need checking: benchmark identities, temporal sampling, computational cost, stability theorem assumptions, ablations of conservative versus dissipative components, and scalability to very large dynamic graphs.

## Deep Themes

- Memory retention as learned dynamics: graph history should neither vanish nor accumulate unchecked.
- Conservative-dissipative decomposition: stability comes from balancing flow and decay.
- Long-range propagation under noise: extended dependencies require selective retention.
- Dynamical systems for GNN design: continuous-time structure gives architectural constraints and guarantees.

## Subthemes

- Impulsive neural ODEs for snapshot graphs.
- Antisymmetric parameterization.
- Adaptive dissipation.
- Stability and expressivity guarantees.

## Connections to Other Papers

This connects to temporal graph memory explanation, POPGym memory diagnostics, and path-dependent inference through the theme of remembering the right history without contaminating current decisions.

It also relates to graph expressivity papers such as Relational Lottery Tickets and IO-aware GNN kernels, though LAMP targets temporal dynamics rather than sparse implementation.

## Notes for Cross-Paper Synthesis

This paper contributes a memory-control subtheme: dynamic systems need explicit mechanisms for deciding what information persists and what dissipates.
