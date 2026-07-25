# L2G-NET: Local to Global Spectral Graph Neural Networks via Cauchy Factorizations

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: kD8iJmyn5l
- Authors: Samuel Fernandez; Eduardo Pavez; Antonio Ortega
- Primary area: deep_learning->graph_neural_networks
- Keywords: GNNs;Spectral GNNs;GFT;graph Laplacian;Localization;Cauchy matrices
- Source URL: https://openreview.net/forum?id=kD8iJmyn5l
- PDF URL: https://openreview.net/pdf?id=kD8iJmyn5l

## Abstract

Despite their theoretical advantages, spectral methods based on the graph Fourier transform (GFT) are seldom used in graph neural networks (GNNs) due to the cost of computing the eigenbasis and the lack of vertex-domain locality in the resulting representations. As a result, most GNNs rely on local approximations such as polynomial Laplacian filters or message passing, which limit their ability to model long-range dependencies. In this paper, we introduce an exact factorization of the GFT into operators acting on subgraphs, which are then combined via a sequence of Cauchy matrices. Building on this factorization, we propose a new class of spectral GNNs, termed L2G-Net (Local to Global Net). Unlike existing spectral methods, which are either fully global (when using the GFT) or local (when using polynomial filters), L2G-Net operates by processing the spectral representations of subgraphs and then combining them via structured matrices. Our algorithm avoids full eigendecompositions, exploiting graph topology to construct the factorization with quadratic complexity in the number of nodes, scaled by the maximum cut size between subgraphs. Experiments stressing long-range dependencies on large graphs show that L2G-Net scales to regimes out of reach for the standard GFT, and is competitive with state-of-the-art methods with orders of magnitude fewer learnable parameters.

## One-Sentence Claim

L2G-Net factorizes the graph Fourier transform into subgraph spectral operators linked by Cauchy matrices, enabling scalable spectral GNNs with local-to-global long-range modeling.

## Problem

Spectral GNNs based on the graph Fourier transform can model global structure, but computing the full eigenbasis is expensive and the resulting representations lack vertex-domain locality. Message passing and polynomial Laplacian filters are local and scalable but struggle with long-range dependencies.

The paper asks whether spectral methods can be made both scalable and locality-aware.

## Core Contribution

The paper introduces an exact factorization of the GFT into operators on subgraphs, combined through a sequence of Cauchy matrices. Based on this, it proposes L2G-Net, a spectral GNN that processes subgraph spectral representations and combines them structurally.

The algorithm avoids full eigendecompositions and scales quadratically in node count, multiplied by maximum cut size between subgraphs.

## Method

L2G-Net decomposes the graph into subgraphs, computes or uses spectral representations locally, then assembles global spectral behavior through structured Cauchy matrix factors. This gives the model access to long-range spectral information without a monolithic global GFT.

The design sits between purely local message passing and fully global spectral transforms.

## Experiments and Evidence

Evidence reported in the abstract:

- Exact GFT factorization through subgraph operators and Cauchy matrices.
- Avoids full eigendecomposition.
- Complexity quadratic in node count scaled by maximum cut size.
- Scales to regimes out of reach for standard GFT.
- Competitive with state-of-the-art methods on large graphs stressing long-range dependencies.
- Uses orders of magnitude fewer learnable parameters.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: graph partition method, numerical stability, datasets, and comparison to long-range GNN baselines.

## Limits and Failure Modes

- Performance may depend on graph partition quality and cut size.
- Cauchy matrix operations can be numerically delicate.
- Quadratic scaling may still be high for very large graphs.
- Spectral assumptions may be less effective on heterophilous or highly dynamic graphs.

## Deep Themes

**Local and global graph structure can be factorized.** The method avoids choosing between message passing locality and full spectral globality.

**Classical transforms can be made neural-compatible.** The GFT becomes a structured computational pipeline for GNNs.

**Long-range dependencies need spectral infrastructure.** L2G-Net targets graph tasks where local filters are insufficient.

## Subthemes

- Spectral GNNs.
- Graph Fourier transform factorization.
- Cauchy matrix coupling.
- Local-to-global graph representations.
- Long-range graph dependencies.

## Connections to Other Papers

Connects to OENN/CENN, FlashSketch, Jacobi Spectral Reconstruction, ReViT, and graph/relational learning papers. It shares the theme of using mathematical factorization to make theoretically appealing methods practical.

## Notes for Cross-Paper Synthesis

L2G-Net adds a graph spectral variant of the structure-efficiency theme: exact mathematical factorization can recover global modeling power while keeping computation closer to local methods.
