# Foundations of Equivariant Deep Learning: Unifying Graph and Sheaf Neural Networks

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: aIH1jyU37z
- Authors: Yoshihiro Maruyama
- Primary area: theory->deep_learning
- Keywords: Geometric Deep Learning;Topological Deep Learning;Categorical Deep Learning;Equivariant Universal Approximation;Equivariant Bundle;Sheaf Neural Net;Category-Equivariant Neural Network;Categorical Symmetry
- Source URL: https://openreview.net/forum?id=aIH1jyU37z
- PDF URL: https://openreview.net/pdf?id=aIH1jyU37z

## Abstract

Symmetry is everywhere in nature and society. Geometric deep learning exploits symmetries in data to improve the performance and efficiency of deep learning systems. In this paper, we extend geometric deep learning to utilize richer symmetry structures. Specifically, we develop order-equivariant neural networks (OENN), which generalize standard graph message passing and sheaf neural networks via the theory of equivariant bundles over face posets (face categories). We (i) characterize all linear order-equivariant maps, (ii) build OENN layers, and (iii) prove universal approximation theorems (UATs) for continuous order-equivariant maps, which are new results even when restricted to sheaf neural networks (for which no UAT was known before). We illustrate the framework on graph and sheaf models. Our results can also be seen as extending the known UAT for graph neural networks to a more general setting that subsumes sheaf neural networks as well. In addition, we show that OENN can be extended further to CENN, Category-Equivariant Neural Network, which gives the general form of equivariant neural networks as well as of equivariant universal approximation theorems, allowing us to leverage categorical symmetry in data (e.g., non-invertible symmetries on multiple objects with compositional relations on those symmetries).

## One-Sentence Claim

Order-equivariant and category-equivariant neural networks unify graph and sheaf neural networks through equivariant bundles over face posets and categorical symmetry.

## Problem

Geometric deep learning exploits symmetries, but common frameworks often focus on group-like symmetries or graph message passing. Sheaf neural networks and richer topological structures need a more general equivariant theory, including universal approximation guarantees.

The paper asks for a foundational framework that subsumes graph and sheaf neural networks and extends equivariant universal approximation.

## Core Contribution

The paper develops order-equivariant neural networks over equivariant bundles on face posets. It characterizes all linear order-equivariant maps, builds OENN layers, and proves universal approximation theorems for continuous order-equivariant maps, including new UATs for sheaf neural networks.

It further extends the framework to Category-Equivariant Neural Networks, giving a general form of equivariant neural networks and universal approximation theorems over categorical symmetries, including non-invertible symmetries across multiple objects with compositional relations.

## Method

The method uses category/topology-inspired formalism. Face posets or face categories encode ordered cell/face relationships; equivariant bundles specify how features transform across this structure. Linear equivariant maps and nonlinear layers are then characterized in this setting.

CENN generalizes from order symmetry to categorical symmetry, replacing simple group actions with compositional morphisms.

## Experiments and Evidence

Evidence reported in the abstract is theoretical and illustrative:

- Characterization of all linear order-equivariant maps.
- Construction of OENN layers.
- Universal approximation theorems for continuous order-equivariant maps.
- New UATs for sheaf neural networks.
- Illustrations on graph and sheaf models.
- Extension to CENN and categorical symmetry.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: exact categorical assumptions, nonlinearities, compactness/domain conditions, and whether empirical examples are included.

## Limits and Failure Modes

- Highly abstract categorical machinery may be hard to implement or benchmark.
- UATs establish expressivity, not trainability or generalization.
- Practical gains over existing GNN/sheaf architectures remain to be shown.
- Non-invertible symmetries require careful feature-space design.

## Deep Themes

**Equivariance is generalizing beyond groups.** Categorical symmetry handles compositional and non-invertible relations.

**Graph and sheaf networks share a deeper bundle structure.** The framework unifies existing architectures under order equivariance.

**Foundational theory expands the architecture search space.** Universal approximation results make richer symmetry-aware models principled.

## Subthemes

- Order-equivariant neural networks.
- Equivariant bundles over face posets.
- Sheaf neural network UATs.
- Category-equivariant neural networks.
- Non-invertible categorical symmetry.

## Connections to Other Papers

Connects to ENGNN, RECM, DIGL, Neural Ricci Flow, and language-symmetry geometry through symmetry and representation geometry. It also links to graph algorithmic papers by broadening the mathematical foundation of graph neural architectures.

## Notes for Cross-Paper Synthesis

This paper deepens the symmetry theme: 2026 geometric learning is not only applying known equivariances but expanding what counts as a symmetry for neural architectures.
