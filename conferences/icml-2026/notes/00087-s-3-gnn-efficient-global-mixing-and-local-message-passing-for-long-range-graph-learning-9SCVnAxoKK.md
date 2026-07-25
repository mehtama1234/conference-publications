# S$^3$GNN: Efficient Global Mixing and Local Message Passing for Long-Range Graph Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 9SCVnAxoKK
- Authors: Dai Shi; Luke Thompson; Linhan Luo; Lequan Lin; Andi Han; Junbin Gao; José Miguel Hernández-Lobato
- Primary area: deep_learning->graph_neural_networks
- Keywords: Graph Neural Networks;Long-range Graph Learning
- Source URL: https://openreview.net/forum?id=9SCVnAxoKK
- PDF URL: https://openreview.net/pdf?id=9SCVnAxoKK

## Abstract

Message-passing neural networks (MPNNs) often suffer from an information bottleneck when capturing long-range dependencies, leading to the oversquashing (OSQ) phenomenon. Alongside spatial connectivity enrichment (e.g., rewiring), recent studies have shown that spectral filtering can yield strong long-range learning outcomes, as spectral operators enable global information mixing that alleviates OSQ. These approaches achieve this either by stabilizing the Jacobian energies in deep propagation or by guaranteeing OSQ mitigation under strong theoretical assumptions. We examine the practical attainability of these guarantees and show that the associated Jacobian sensitivity lower bound is generally difficult to achieve in practice. We then propose S$^3$GNN, which mitigates OSQ without such restrictive assumptions by lightweightly reintroducing omitted components with substantially lower computational complexity, while standard stability constraints on feature transformations remain effective under our new dynamics. Extensive experiments across diverse domains (e.g., long-range benchmarks, KGQA, and mesh-based fluid dynamics) demonstrate that S$^3$GNN achieves up to an order-of-magnitude error reduction with up to 50\% fewer parameters. Our code can be found in https://github.com/EEthanShi/S3-GNN.git.

## One-Sentence Claim

S3GNN mitigates oversquashing by combining efficient global spectral mixing with local message passing without relying on hard-to-attain Jacobian sensitivity assumptions.

## Problem

MPNNs struggle with long-range dependencies because information is compressed through narrow graph bottlenecks, and some spectral oversquashing guarantees depend on restrictive assumptions that may not hold in practice.

## Core Contribution

The paper proposes S3GNN, a lightweight long-range graph learning architecture that reintroduces omitted components at lower computational complexity while preserving useful stability constraints.

## Method

S3GNN revisits spectral-filtering approaches to oversquashing mitigation, argues that a key Jacobian sensitivity lower bound is difficult to realize, and modifies graph dynamics to combine global mixing with local propagation more practically.

## Experiments and Evidence

The abstract reports experiments across long-range graph benchmarks, KGQA, and mesh-based fluid dynamics, with up to an order-of-magnitude error reduction and up to 50% fewer parameters.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv is currently being deferred after repeated 429/503 errors. Details still need checking: exact S3 dynamics, computational complexity, spectral assumptions, benchmark splits, and comparison with rewiring methods.

## Deep Themes

- Oversquashing mitigation is moving from theory-heavy guarantees to practical attainable dynamics.
- Graph models need both global mixing and local message passing.
- Spectral methods are becoming a bridge between theory and scalable graph architectures.

## Subthemes

- Long-range graph learning.
- Oversquashing.
- Spectral filtering.
- Global mixing.
- Local message passing.
- Mesh/fluid graph domains.

## Connections to Other Papers

Connects to HyperDepth, PhenoBrain, LOES, and spectral causal-discovery work through spectral geometry as an operational modeling primitive. It also links to scientific ML via mesh-based dynamics.

## Notes for Cross-Paper Synthesis

S3GNN strengthens the spectral-structure theme: long-range reasoning in graphs requires architectures that make global communication practical, not just theoretically possible.
