# Beyond ReLU: Bifurcation, Oversmoothing, and Topological Priors

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: AehiGqd7go
- Authors: Erkan Turan; Gaspard Abel; Maysam Behmanesh; Emery Pierson; Maks Ovsjanikov
- Primary area: deep_learning->graph_neural_networks
- Keywords: GNN;Oversmoothing;Dynamical Systems
- Source URL: https://openreview.net/forum?id=AehiGqd7go
- PDF URL: https://openreview.net/pdf?id=AehiGqd7go

## Abstract

Graph Neural Networks (GNNs) learn node representations through iterative network-based message-passing. While powerful, deep GNNs suffer from oversmoothing, where node features converge to a homogeneous, non-informative state. We re-frame this problem of representational collapse from a \emph{bifurcation theory} perspective, characterizing oversmoothing as convergence to a stable ``homogeneous fixed point.'' Our central contribution is the theoretical discovery that this undesired stability can be broken by replacing standard monotone activations (e.g., ReLU) with a class of functions. Using Lyapunov-Schmidt reduction, we analytically prove that this substitution induces a bifurcation that destabilizes the homogeneous state and creates a new pair of stable, non-homogeneous \emph{patterns} that provably resist oversmoothing. Our theory predicts a precise, nontrivial scaling law for the amplitude of these emergent patterns, which we quantitatively validate in experiments. Finally, we demonstrate the practical utility of our theory by deriving a closed-form, bifurcation-aware initialization and showing its utility in real benchmark experiments.

## One-Sentence Claim

Oversmoothing in deep GNNs can be understood as convergence to a stable homogeneous fixed point, and non-monotone activations can destabilize it through bifurcation.

## Problem

Deep GNN message passing often collapses node features into homogeneous non-informative states, limiting depth and long-range reasoning.

## Core Contribution

The paper reframes oversmoothing with bifurcation theory and shows that replacing standard monotone activations can induce stable non-homogeneous patterns that resist collapse.

## Method

Using Lyapunov-Schmidt reduction, the paper analyzes the homogeneous fixed point and proves that a class of alternative activations destabilizes it, creating new stable patterns. It also derives a bifurcation-aware closed-form initialization.

## Experiments and Evidence

The abstract reports quantitative validation of a predicted scaling law for emergent pattern amplitude and benchmark experiments showing practical utility of the initialization.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition is deferred after repeated rate-limit failures. Details still need checking: activation class, topological prior form, graph assumptions, initialization formula, and benchmark sensitivity.

## Deep Themes

- GNN failure modes can be studied as dynamical-systems stability problems.
- Activation choice can change the topology of representation dynamics.
- Theory can yield direct initialization rules for practical graph models.

## Subthemes

- GNN oversmoothing.
- Bifurcation theory.
- Lyapunov-Schmidt reduction.
- Non-monotone activations.
- Topological priors.
- Dynamical systems.

## Connections to Other Papers

Connects to S3GNN, HyperDepth, Thinking in Flow, and IRNO through dynamical/spectral approaches to stability and long-range information flow.

## Notes for Cross-Paper Synthesis

This paper strengthens the dynamical-systems theme: representation collapse is treated as a fixed-point stability issue that architecture can deliberately destabilize.
