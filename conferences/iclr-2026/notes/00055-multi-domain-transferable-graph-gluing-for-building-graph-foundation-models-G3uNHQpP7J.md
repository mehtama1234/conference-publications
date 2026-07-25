# Multi-Domain Transferable Graph Gluing for Building Graph Foundation Models

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: G3uNHQpP7J
- Authors: Li Sun; Zhenhao Huang; Silei Chen; Lanxu Yang; Junda Ye; Sen Su; Philip S. Yu
- Primary area: learning on graphs and other geometries & topologies
- Keywords: Multi-domain graph pre-training;graph neural network;graph foundation model;Riemannian geometry
- Source URL: https://openreview.net/forum?id=G3uNHQpP7J
- PDF URL: https://openreview.net/pdf?id=G3uNHQpP7J

## Abstract

Multi-domain graph pre-training integrates knowledge from diverse domains to enhance performance in the target domains, which is crucial for building graph foundation models. Despite initial success, existing solutions often fall short of answering a fundamental question: how is knowledge integrated or transferred across domains? This theoretical limitation motivates us to rethink the consistency and transferability between the pre-trained model and target domains. In this paper, we propose a fresh differential geometry perspective, whose core idea is to merge any graph dataset into a unified, smooth Riemannian manifold, enabling a systematic understanding of knowledge integration and transfer. To achieve this, our key contribution is the theoretical establishment of neural manifold gluing,
which first characterizes local geometry using an adaptive orthogonal frame and then “glues” the local pieces together into a coherent whole. Building on this theory, we present the GraphGlue framework, which supports batched pre-training with EMA prototyping and provides a transferability measure based on geometric consistence. Extensive experiments demonstrate its superior performance across diverse graph domains. Moreover, we empirically validated GraphGlue’s geometric scaling law, showing that larger quantities of datasets improve model transferability by producing a smoother manifold.

## One-Sentence Claim

GraphGlue builds graph foundation models by treating multi-domain graph pretraining as gluing local graph geometries into a smooth Riemannian manifold.

## Problem

Multi-domain graph pretraining seeks to transfer knowledge across graph domains, but existing methods often lack a theory of how knowledge is integrated or why pretrained models transfer to target domains.

The problem is to understand and measure consistency between pretraining domains and target graph domains.

## Core Contribution

The paper proposes a differential-geometry view of multi-domain graph pretraining, centered on neural manifold gluing.

It characterizes local graph-domain geometry using adaptive orthogonal frames, glues local pieces into a coherent Riemannian manifold, and builds the GraphGlue framework with EMA prototyping and a geometric transferability measure.

## Method

GraphGlue treats graph datasets as local geometric pieces. Adaptive orthogonal frames capture local structure, and manifold gluing aligns these pieces into a unified smooth representation space.

The framework supports batched pretraining and uses EMA prototypes to stabilize domain-level representation. Transferability is measured by geometric consistency.

## Experiments and Evidence

The abstract reports superior performance across diverse graph domains.

It also reports an empirical geometric scaling law: adding more datasets improves transferability by producing a smoother manifold.

## Limits and Failure Modes

The Riemannian gluing view may depend on whether graph domains are compatible enough to be represented as a smooth manifold. Heterogeneous graph types or conflicting semantics may break smoothness assumptions.

Because this note is abstract-only, details still need checking: graph domains, adaptive-frame construction, gluing objective, EMA prototype update, transferability metric, and scaling-law evidence.

## Deep Themes

- Graph foundation models need transfer theory: multi-domain pretraining should explain integration, not only aggregate datasets.
- Manifold gluing: local domain geometries become a global representation space.
- Geometric transferability: consistency can be measured through smoothness and alignment.
- Dataset scaling as manifold smoothing: more domains may improve transfer by filling geometry.

## Subthemes

- Neural manifold gluing.
- Adaptive orthogonal frames.
- EMA prototyping.
- Multi-domain graph pretraining.

## Connections to Other Papers

This connects to CoCo, MV-FGAD, LAMP, and Relational Lottery Tickets through graph representation geometry.

It also relates to Beyond Language Modeling and foundation-model scaling papers because it asks how multi-domain pretraining produces transferable structure.

## Notes for Cross-Paper Synthesis

GraphGlue adds a geometric foundation-model theme: cross-domain transfer can be framed as making local data manifolds cohere into one smoother global space.
