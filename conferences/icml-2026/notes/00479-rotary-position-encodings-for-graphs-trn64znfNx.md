# Rotary Position Encodings for Graphs

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: trn64znfNx
- Authors: Isaac Reid; Arijit Sehanobish; Cederik Höfs; Bruno Kacper Mlodozeniec; Leonhard Vulpius; Federico Barbero; Adrian Weller; Krzysztof Marcin Choromanski; Richard E. Turner; Petar Veličković
- Primary area: deep_learning->attention_mechanisms
- Keywords: RoPE;graphs;spectra;Laplacian;Performers;linear attention
- Source URL: https://openreview.net/forum?id=trn64znfNx
- PDF URL: https://openreview.net/pdf?id=trn64znfNx

## Abstract

We study the extent to which rotary position encodings (RoPE), a recent transformer position encoding algorithm broadly adopted in large language models (LLMs) and vision transformers (ViTs), can be applied to graph-structured data. We find that rotating tokens depending on the spectrum of the graph Laplacian efficiently injects structural information into the attention mechanism, boosting performance in synthetic and real-world graph learning tasks. This approach, coined _Wave-Induced Rotary Encodings_ (WIRE), enjoys intriguing theoretical properties: it recovers regular RoPE on grids, and depends asymptotically on the graph effective resistance. Unlike bias-based relative position encodings, WIRE is compatible with linear attention.

## One-Sentence Claim

Wave-Induced Rotary Encodings extend RoPE to graphs by rotating tokens according to graph Laplacian spectral structure, injecting relative graph geometry while remaining compatible with linear attention.

## Problem

RoPE is widely used in language and vision Transformers, but graph-structured data lacks a simple sequential or grid position system. Graph Transformers need positional encodings that represent graph geometry without relying on dense bias matrices that break linear-attention compatibility.

The paper asks whether RoPE's rotary mechanism can be generalized from ordered or grid domains to arbitrary graphs using spectral structure.

## Core Contribution

The paper proposes WIRE, Wave-Induced Rotary Encodings. It rotates token representations based on the graph Laplacian spectrum, injecting structural information directly into attention.

The theoretical contribution is that WIRE recovers regular RoPE on grids and asymptotically depends on graph effective resistance. Unlike bias-based relative encodings, it remains compatible with linear attention.

## Method

WIRE uses graph Laplacian eigenstructure to define wave-like rotations for graph tokens. These rotations modify query/key representations so attention scores carry structural information about the graph.

Because the position information is encoded through rotations rather than additive pairwise biases, WIRE can be used with Performer-style or other linear attention mechanisms.

## Experiments and Evidence

The abstract reports improved performance on synthetic and real-world graph learning tasks. It also states theoretical properties linking WIRE to grid RoPE and effective resistance.

Full-paper reading should verify graph benchmark suite, spectral computation cost, behavior on large graphs, approximation methods, and comparison against Laplacian PE, random-walk PE, and bias-based encodings.

## Limits and Failure Modes

Spectral methods can be expensive for large graphs and sensitive to graph perturbations, disconnected components, or eigenvalue multiplicities. Approximate spectra may affect encoding quality.

Effective resistance is meaningful for many graph tasks but may not capture all relevant structural roles, especially in heterophilic or attributed graphs.

## Deep Themes

- Positional encoding as geometry injection: graph structure enters attention through rotations.
- Spectral graph inductive bias: Laplacian waves generalize grid positions to irregular domains.
- Linear-attention compatibility: structural encodings must fit scalable attention implementations.
- Effective resistance as latent distance: WIRE links attention geometry to electrical-network graph metrics.

## Subthemes

- RoPE can be reinterpreted spectrally.
- Graph Transformers need relative structure without dense biases.
- Grids are a special case of graph positional encoding.
- Synthetic tasks test whether the encoding captures known structural relations.

## Connections to Other Papers

WIRE connects to ConFlux, DHSA, and STAR-KV through attention efficiency and tokenization/positioning. It also relates to concept binding and representation geometry papers: structural encodings define what relationships attention can easily represent.

It fits with temporal graph explainability because both adapt Transformer/graph methods to graph-specific structure rather than treating graphs as generic token sets.

## Notes for Cross-Paper Synthesis

The synthesis point is that position encoding is domain adaptation. As Transformers move into graphs, time series, and physical systems, positional structure must be rebuilt from the domain's geometry.
