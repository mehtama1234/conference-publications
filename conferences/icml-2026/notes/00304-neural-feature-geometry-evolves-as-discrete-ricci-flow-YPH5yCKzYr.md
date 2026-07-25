# Neural Feature Geometry Evolves as Discrete Ricci Flow

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: YPH5yCKzYr
- Authors: Moritz Hehl; Max von Renesse; Melanie Weber
- Primary area: deep_learning->other_representation_learning
- Keywords: neural feature geometry;discrete geometry;Ricci flow;geometric graphs;representation learning;deep neural networks
- Source URL: https://openreview.net/forum?id=YPH5yCKzYr
- PDF URL: https://openreview.net/pdf?id=YPH5yCKzYr

## Abstract

Deep neural networks learn feature representations via complex geometric transformations of the input data manifold. Despite the models' empirical success across domains, our understanding of neural feature representations is still incomplete. In this work we investigate neural feature geometry through the lens of discrete geometry. Since the input data manifold is typically unobserved, we approximate it using geometric graphs that encode local similarity structure. We provide theoretical results on the evolution of these graphs during training, showing that nonlinear activations play a crucial role in shaping feature geometry in feedforward neural networks. Moreover, we discover that the geometric transformations resemble a discrete Ricci flow on these graphs, suggesting that neural feature geometry evolves analogous to Ricci flow. This connection is supported by experiments on over 20,000 feedforward neural networks trained on binary classification tasks across both synthetic and real-world datasets. We observe that the emergence of class separability corresponds to the emergence of community structure in the associated graph representations, which is known to relate to discrete Ricci flow dynamics. Building on these insights, we introduce a novel framework for locally evaluating geometric transformations through comparison with discrete Ricci flow dynamics. Our experimental results further suggest connections between the evolution of feature geometry, and training time and network depth.

## One-Sentence Claim

Neural feature geometry during training resembles discrete Ricci flow on local-similarity graphs, with class separability emerging alongside graph community structure.

## Problem

Deep networks transform data manifolds into feature representations, but the geometry of this transformation remains poorly understood. Because the true data manifold is unobserved, researchers need tractable proxies for local feature geometry during training.

The paper asks whether discrete geometry can characterize how neural features evolve.

## Core Contribution

The paper approximates input and feature manifolds with geometric graphs encoding local similarity. It provides theoretical results showing nonlinear activations shape feature geometry in feedforward networks, then observes that the transformations resemble discrete Ricci flow on these graphs.

Across more than 20,000 feedforward networks on synthetic and real binary classification tasks, class separability emerges with community structure in graph representations. The paper introduces a framework for locally evaluating neural geometric transformations by comparison with discrete Ricci flow dynamics.

## Method

The method constructs geometric graphs from feature representations during training and tracks their local geometry. Discrete Ricci flow supplies a reference dynamic for how graph curvature and community structure evolve.

Experiments vary networks, datasets, training time, and depth to compare learned feature transformations with Ricci-flow-like behavior.

## Experiments and Evidence

Evidence reported in the abstract:

- Theoretical results on feature-geometry evolution in feedforward networks.
- Role of nonlinear activations in shaping geometry.
- Experiments on more than 20,000 feedforward neural networks.
- Synthetic and real binary classification datasets.
- Emergence of class separability alongside graph community structure.
- Links between feature geometry, training time, and depth.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: graph construction, Ricci curvature definition, datasets, architectures, and statistical strength of the analogy.

## Limits and Failure Modes

- Binary classification and feedforward networks may not generalize to Transformers or generative models.
- Ricci-flow resemblance may be descriptive rather than mechanistically causal unless interventions are shown.
- Graph construction choices can affect measured geometry.
- Scaling to high-dimensional real data may require careful neighborhood estimation.

## Deep Themes

**Training reshapes data geometry.** Feature learning can be studied as a geometric flow rather than only loss minimization.

**Class separability has a graph-geometry signature.** Community structure emerges as representations become discriminative.

**Discrete geometry offers diagnostic tools.** Ricci-flow comparison becomes a local evaluator of learned transformations.

## Subthemes

- Geometric graphs for feature manifolds.
- Discrete Ricci flow analogy.
- Nonlinear activations and geometry.
- Community structure and class separability.
- Training time and depth effects.

## Connections to Other Papers

Connects to language-symmetry geometry, DIGL, ENGNN, and manifold-aware perturbations through geometric representation analysis. It also links to interpretability papers where internal structure is measured rather than inferred from outputs alone.

## Notes for Cross-Paper Synthesis

This paper adds a dynamical geometry perspective to the corpus: representations are not just points or subspaces but evolving graphs whose curvature-like changes track learning.
