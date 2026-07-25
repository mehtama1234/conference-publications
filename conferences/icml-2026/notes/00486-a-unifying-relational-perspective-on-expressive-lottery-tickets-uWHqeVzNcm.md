# A Unifying Relational Perspective on Expressive Lottery Tickets

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: uWHqeVzNcm
- Authors: Lorenz Kummer; Samir Moustafa; Anatol Ehrlich; Franka Bause; Marco Nennstiel; Przemysław Andrzej Wałęga; Nils Morten Kriege
- Primary area: deep_learning->graph_neural_networks
- Keywords: Graph Neural Networks;Lottery Ticket Hypothesis;GNNs;LTH;Pruning
- Source URL: https://openreview.net/forum?id=uWHqeVzNcm
- PDF URL: https://openreview.net/pdf?id=uWHqeVzNcm

## Abstract

Graph neural networks (GNNs) are widely used, but how parameter sparsity affects the expressivity of relational (RGNNs) and temporal (TGNNs) variants is poorly understood. The Strong Expressive Lottery Ticket Hypothesis (SELTH) posits the existence of sparse GNNs that preserve Weisfeiler-Leman (WL) expressivity on static graphs. We generalize this existence result to a probabilistic statement for multi-relational and temporal domains via the relational WL (RWL). We prove that sufficiently parameterized RGNNs contain sparse subnetworks that maintain 1-RWL expressivity and derive a lower bound on the probability that a random pruning yields such a subnetwork. We show that common TGNNs and cross-graph message passing schemes admit RGNN reformulations such that they inherit these guarantees and, moreover, that the expressivity of a sparse RGNN is connected to its optimization behavior under common update regimes. Experiments instantiate the bound, compare it to empirical probabilities on synthetic data, and study how pre-training expressivity relates to optimization and prediction quality metrics on temporal and molecular benchmarks.

## One-Sentence Claim

Expressive lottery-ticket guarantees extend from static GNNs to relational and temporal graph neural networks, with sparse subnetworks preserving relational WL expressivity with quantifiable probability.

## Problem

Lottery-ticket work studies whether sparse subnetworks can preserve the expressive power of dense models. For GNNs, the Strong Expressive Lottery Ticket Hypothesis claims sparse subnetworks can retain Weisfeiler-Leman expressivity on static graphs.

But many practical graph models are relational or temporal, and the impact of sparsity on their expressivity is less understood. Sparse pruning may save computation while silently degrading the relational distinctions the model can represent.

## Core Contribution

The paper generalizes expressive lottery-ticket existence to multi-relational and temporal domains through relational Weisfeiler-Leman expressivity. It proves that sufficiently parameterized RGNNs contain sparse subnetworks maintaining 1-RWL expressivity.

It also derives a lower bound on the probability that random pruning finds such a subnetwork, shows that common TGNNs and cross-graph message-passing schemes admit RGNN reformulations, and connects sparse RGNN expressivity to optimization behavior.

## Method

The theoretical framework reformulates relational, temporal, and cross-graph message-passing architectures in RGNN terms. Expressivity is measured through relational WL tests.

Sparse subnetwork existence and random-pruning probability are then analyzed under sufficient parameterization. Experiments instantiate the bound and compare theoretical probabilities with empirical behavior.

## Experiments and Evidence

The abstract reports experiments on synthetic data, temporal benchmarks, and molecular benchmarks. These compare theoretical lower bounds with empirical probabilities and study links between pretraining expressivity, optimization, and prediction quality.

Full-paper reading should verify pruning regimes, sparsity levels, RGNN/TGNN architectures, WL expressivity definitions, and how expressivity metrics predict task performance.

## Limits and Failure Modes

WL-style expressivity is an important but incomplete proxy for downstream performance. A sparse model can preserve WL distinctions while still optimizing poorly or lacking useful inductive bias.

Random-pruning lower bounds may be loose, and practical pruning methods may behave differently. The guarantees require sufficient parameterization and may not cover all temporal graph mechanisms.

## Deep Themes

- Expressivity-preserving sparsity: compression can maintain formal graph-discrimination power.
- Relational unification: temporal and cross-graph models inherit guarantees through RGNN reformulation.
- Probabilistic lottery tickets: random pruning success is bounded, not just asserted existentially.
- Expressivity and optimization linkage: sparse structure affects both what a model can represent and how it trains.

## Subthemes

- Relational WL generalizes static WL analysis.
- TGNNs can be viewed through relational message passing.
- Sparse subnetworks need formal capability guarantees.
- Molecular and temporal tasks test whether theory maps to practice.

## Connections to Other Papers

This paper connects to MoE compression, STAR-KV, and FFCC through efficiency without losing capability. It also connects to WIRE and temporal graph explainability through graph-specific structure.

It fits the broader theory-engineering theme: pruning should be analyzed for the formal behavior it preserves, not only parameter count.

## Notes for Cross-Paper Synthesis

The synthesis point is that sparsity is not one property. In graph models, useful sparsity must preserve relational expressivity and optimization behavior.
