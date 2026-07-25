# FlatLand: Personalized Graph Federated Learning via Tailored Lorentz Space

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: H6PagZKyil
- Authors: Jiahong Liu; Ram Samarth B B; Xinyu Fu; Menglin Yang; Weixi Zhang; Rex Ying; Irwin King
- Primary area: social_aspects->privacy
- Keywords: Federated Learning;Hyperbolic Geometry
- Source URL: https://openreview.net/forum?id=H6PagZKyil
- PDF URL: https://openreview.net/pdf?id=H6PagZKyil

## Abstract

Personalization has become a pivotal field of study in contemporary intelligent systems. 
Federated learning enables privacy-preserving collaborative training, but highly heterogeneous client data remain challenging, especially in graph federated learning where clients possess structurally diverse graphs. Existing personalized federated learning (PFL) methods ignore the intrinsic geometric properties of diverse graph structures. We propose FlatLand, a novel personalized Federated learning method that embeds different clients' data in tailored Lorentz space of hyperbolic geometry. Our key insight is that hyperbolic geometry naturally accommodates the intrinsic negative curvature prevalent in real-world graphs, while the time-like dimension in Lorentz space provides a principled way to encode client-specific heterogeneity. We develop a parameter decoupling strategy that separates heterogeneous information (captured in time-like parameters) from common knowledge (preserved in space-like parameters), enabling direct aggregation without requiring client similarity estimation and extra calculation modules. Empirical results on diverse federated graph learning tasks demonstrate that FlatLand achieves superior performance, particularly in low-dimensional settings. Code is available in our GitHub repository.

## One-Sentence Claim

FlatLand personalizes graph federated learning by embedding each client in a tailored Lorentz space that separates client-specific heterogeneity from shared graph knowledge.

## Problem

Federated graph learning must train across clients with structurally diverse graphs, but standard personalized federated learning methods often ignore the geometry of graph data and require extra client-similarity estimation.

## Core Contribution

The paper introduces a hyperbolic-geometry approach to personalization where Lorentz-space dimensions encode the split between heterogeneous client information and aggregatable common structure.

## Method

FlatLand embeds client data in tailored Lorentz spaces, using the time-like dimension to represent client-specific heterogeneity and space-like parameters to preserve common knowledge. A parameter-decoupling strategy enables direct aggregation without separate similarity modules.

## Experiments and Evidence

The abstract reports superior results on diverse federated graph learning tasks, especially in low-dimensional settings where hyperbolic geometry should be most useful for representing negatively curved graph structure.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: datasets, privacy threat model, communication cost, client sampling assumptions, curvature/tailoring procedure, and whether low-dimensional gains trade off against high-dimensional flexibility.

## Deep Themes

- Geometry as an architectural prior for heterogeneous distributed learning.
- Personalization through parameter factorization rather than client clustering.
- Privacy-preserving collaboration under structural non-IID graph data.

## Subthemes

- Federated learning.
- Graph neural networks.
- Hyperbolic/Lorentz geometry.
- Client heterogeneity.
- Low-dimensional representation.
- Direct aggregation.

## Connections to Other Papers

Connects to graph algorithm-learning papers through structural representation limits and to privacy/data-governance papers through decentralized training constraints. It also shares the corpus's geometry motif with papers using representation space as a lever for robustness or personalization.

## Notes for Cross-Paper Synthesis

FlatLand adds a distributed-systems version of the geometry theme: choosing the right representation manifold can make aggregation, personalization, and heterogeneity handling simpler rather than adding heuristic coordination machinery.
