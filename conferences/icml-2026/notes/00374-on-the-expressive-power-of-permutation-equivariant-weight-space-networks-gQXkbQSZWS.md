# On the Expressive Power of Permutation-Equivariant Weight-Space Networks

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: gQXkbQSZWS
- Authors: Adir Dayan; Yam Eitan; Haggai Maron
- Primary area: deep_learning->everything_else
- Keywords: expressivity;equivariance;permutation;weight space;metanetwork;geometric deep learning;symmetries
- Source URL: https://openreview.net/forum?id=gQXkbQSZWS
- PDF URL: https://openreview.net/pdf?id=gQXkbQSZWS

## Abstract

Weight-space learning studies neural architectures that operate directly on the parameters of other neural networks. Motivated by the growing availability of pretrained models, recent work has demonstrated the effectiveness of weight-space networks across a wide range of tasks.
SOTA weight-space networks rely on permutation-equivariant designs to improve generalization. However, this may negatively affect expressive power, warranting theoretical investigation.
Importantly, unlike other structured domains, weight-space learning targets maps operating on both weight and function spaces, making expressivity analysis particularly subtle.
While a few prior works provide partial expressivity results, a comprehensive characterization is still missing. In this work, we address this gap by developing a systematic theory for expressivity of weight-space networks.
We first prove that all prominent permutation-equivariant networks are equivalent in expressive power. We then establish universality in both weight- and function-space settings under mild, natural assumptions on the input weights, and characterize the edge-case regimes where universality no longer holds. 
Guided by our theoretical results, we show that slight modifications to existing weight-space models yield a 34\% improvement over prior SOTA, demonstrating the practical relevance of our framework.

## One-Sentence Claim

Permutation-equivariant weight-space networks can be universal under natural assumptions, and prominent designs are equivalent in expressive power despite apparent architectural differences.

## Problem

Weight-space learning operates directly on the parameters of other neural networks, an increasingly important setting as pretrained models become plentiful. Many state-of-the-art weight-space networks enforce permutation equivariance to respect neuron-order symmetries, but this raises concern about lost expressive power.

The paper asks for a systematic expressivity theory covering maps in both weight space and function space.

## Core Contribution

The paper proves that prominent permutation-equivariant weight-space network designs are equivalent in expressive power. It establishes universality in both weight-space and function-space settings under mild natural assumptions on input weights, and characterizes edge cases where universality fails.

Guided by the theory, it modifies existing weight-space models and reports a 34% improvement over prior state of the art.

## Method

The analysis formalizes the symmetry group induced by neuron permutations and studies architectures that are equivariant to those transformations. It then compares expressivity classes across existing model families and proves universality under assumptions that avoid degenerate weight configurations.

The practical modifications follow from the identified expressive bottlenecks and edge-case regimes.

## Experiments and Evidence

Evidence reported in the abstract:

- Equivalence in expressive power across prominent permutation-equivariant weight-space networks.
- Universality for weight-space and function-space mappings under mild assumptions.
- Characterization of regimes where universality fails.
- Theory-guided model modifications improving over prior SOTA by 34%.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: tasks, assumptions, architecture families, and what metric the 34% improvement refers to.

## Limits and Failure Modes

- Universality may require assumptions that exclude practically common degeneracies.
- Expressivity does not guarantee learnability or sample efficiency.
- Weight-space maps can be sensitive to training conventions, normalization, and architecture mismatch.
- Theory for fixed architecture families may not cover heterogeneous pretrained-model collections.

## Deep Themes

**Model weights are becoming data.** The paper treats neural network parameters as structured objects for learning.

**Symmetry can preserve expressivity.** Equivariance does not necessarily mean weaker models when the target domain has matching invariances.

**Function-space and weight-space views must be reconciled.** Expressivity in parameter coordinates is subtle because many weights implement the same function.

## Subthemes

- Weight-space learning.
- Permutation-equivariant metanetworks.
- Universality under neuron symmetries.
- Function-space expressivity.
- Pretrained-model collections as datasets.

## Connections to Other Papers

Connects to OENN/CENN, Symmetry ICL Dynamics, Context-Parameter Equivalence, ReViT, and Modern Conservation Laws. All explore how symmetry clarifies or strengthens neural architectures.

## Notes for Cross-Paper Synthesis

This paper adds a meta-learning layer to the symmetry theme: as models themselves become training examples, respecting weight-space symmetries is essential for both generalization and theory.
