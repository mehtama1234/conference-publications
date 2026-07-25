# Progressive Graph Structure Adjustment for Homophily Shift Adaptation

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: OkyO74bJqE
- Authors: Hongwei Wen; Can Zhang; Haoyu He; Hanyuan Hang; Minglong Lei
- Primary area: general_machine_learning->transfer_multitask_and_metalearning
- Keywords: Graph domain adaptation;node homophily shift;graph neural network;graph structure adjustment
- Source URL: https://openreview.net/forum?id=OkyO74bJqE
- PDF URL: https://openreview.net/pdf?id=OkyO74bJqE

## Abstract

We propose *Progressive Structure Adjustment for Homophily Shift* (*PSAHS*), a lightweight method for *Graph Domain Adaptation* (*GDA*) that explicitly addresses cross-domain mismatch in node-level homophily. PSAHS enhances node homophily in the source graph to a prescribed level by reweighting edges and introducing additional intra-class connections for low-homophily nodes, and conservatively refines the target graph using agreement-consistent predictions from a structure-aware *Graph Neural Network* (*GNN*) and an attribute-only *Multi-Layer Perceptron* (*MLP*) to ensure reliability under label scarcity. After each structural refinement, domain-adversarial training is employed to align node representations across domains. PSAHS employs a progressive training scheme that alternates between structure adjustment and representation alignment, where increasingly informative representations enable safer homophily correction, and the refined structure in turn improves representation learning. Extensive experiments on multiple GDA benchmarks demonstrate that PSAHS consistently outperforms strong baselines, with particularly large gains under severe homophily mismatch, highlighting the importance of explicit homophily alignment for effective cross-graph transfer.

## One-Sentence Claim

PSAHS adapts graph neural networks across domains by progressively correcting source and target graph structures for node-homophily mismatch.

## Problem

Graph domain adaptation suffers when source and target graphs differ in node-level homophily, but standard methods align representations without explicitly correcting structural mismatch.

## Core Contribution

The paper introduces a lightweight progressive method that adjusts source homophily, conservatively refines target structure with agreement-consistent predictions, and alternates structure correction with domain-adversarial alignment.

## Method

PSAHS reweights source edges and adds intra-class connections for low-homophily nodes, refines target graphs only when a structure-aware GNN and attribute-only MLP agree, then performs domain-adversarial representation alignment after each refinement.

## Experiments and Evidence

The abstract reports consistent improvements over strong baselines on multiple GDA benchmarks, with especially large gains under severe homophily mismatch.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: homophily estimation, prescribed source homophily level, target-label scarcity assumptions, agreement thresholding, and behavior on heterophilous tasks where homophily should not be increased.

## Deep Themes

- Graph transfer requires structural alignment, not only embedding alignment.
- Progressive refinement can make risky pseudo-structure updates safer.
- Homophily is a domain-shift variable that should be measured and controlled.

## Subthemes

- Graph domain adaptation.
- Homophily shift.
- Structure adjustment.
- Domain-adversarial training.
- Agreement-consistent pseudo-labeling.
- GNN transfer.

## Connections to Other Papers

Connects to graph learning, FlatLand, and SWING through structural graph assumptions and scalable graph representation. It also aligns with progressive correction themes in diffusion and RL.

## Notes for Cross-Paper Synthesis

PSAHS adds a graph-domain-shift theme: transfer fails when relational structure changes, so adaptation must modify the graph itself rather than only the node embeddings.
