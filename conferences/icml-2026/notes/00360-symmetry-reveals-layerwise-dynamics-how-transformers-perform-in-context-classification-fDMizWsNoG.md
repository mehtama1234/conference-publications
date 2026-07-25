# Symmetry Reveals Layerwise Dynamics: How Transformers Perform In-Context Classification

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: fDMizWsNoG
- Authors: Patrick Lutz; Themistoklis Haris; Arjun Chandra; Aditya Gangrade; Venkatesh Saligrama
- Primary area: deep_learning
- Keywords: in-context learning;interpretability;transfromers
- Source URL: https://openreview.net/forum?id=fDMizWsNoG
- PDF URL: https://openreview.net/pdf?id=fDMizWsNoG

## Abstract

Transformers can perform in-context classification from a few labeled examples, yet the inference-time algorithm remains opaque. We study multi-class linear classification in the hard no-margin regime and make the computation identifiable by enforcing feature- and label-permutation equivariance at every layer. This enables interpretability while maintaining functional equivalence and yields highly structured weights. From these models we extract an explicit depth-indexed recursion: an end-to-end identified, emergent update rule inside a softmax transformer, to our knowledge the first of its kind. Attention matrices formed from mixed feature-label Gram structure drive coupled updates of training points, labels, and the test probe. The resulting dynamics implement a geometry-driven algorithmic motif, which can provably amplify class separation and yields robust expected class alignment.

## One-Sentence Claim

Enforcing feature- and label-permutation equivariance makes Transformer in-context classification interpretable enough to extract an explicit layerwise update rule.

## Problem

Transformers can perform few-shot in-context classification, but the algorithm implemented by their layers is difficult to identify. Standard trained models mix useful computation with symmetries and redundancies that obscure the actual update dynamics.

The paper studies multi-class linear classification in a hard no-margin setting and uses symmetry constraints to make the computation identifiable.

## Core Contribution

The contribution is an end-to-end identified, depth-indexed recursion inside a softmax Transformer for in-context classification. By enforcing feature- and label-permutation equivariance at every layer, the model retains functional equivalence while producing highly structured weights.

The extracted dynamics use mixed feature-label Gram structures in attention matrices to update training points, labels, and the test probe. The resulting algorithmic motif can amplify class separation and support robust expected class alignment.

## Method

The authors constrain the Transformer architecture or learned representation to respect feature and label permutation symmetries layer by layer. These constraints remove arbitrary degrees of freedom and reveal structured weights.

They then analyze the induced attention matrices and derive a recursion that describes how examples, labels, and test probes evolve through depth.

## Experiments and Evidence

Evidence reported in the abstract:

- Multi-class linear classification in the hard no-margin regime.
- Feature- and label-permutation equivariance enforced at every layer.
- Extraction of an explicit depth-indexed recursion from softmax Transformers.
- Attention matrices formed from mixed feature-label Gram structure.
- Provable amplification of class separation and robust expected class alignment.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: architecture restrictions, proof assumptions, training setup, and empirical validation.

## Limits and Failure Modes

- The identified dynamics may rely on symmetry constraints that natural models only approximately satisfy.
- Linear classification and no-margin assumptions may not transfer directly to richer in-context tasks.
- Interpretability gained through constrained models may miss mechanisms used by unconstrained large models.
- Class-separation amplification can clarify behavior but not necessarily explain all failure modes.

## Deep Themes

**Symmetry can make mechanisms legible.** The paper uses equivariance as an interpretability tool, not just an inductive bias.

**In-context learning is algorithmic dynamics.** The model is analyzed as an iterative procedure over examples, labels, and probes.

**Representation geometry drives reasoning.** Gram structures and class alignment explain how depth improves classification.

## Subthemes

- Feature-permutation equivariance.
- Label-permutation equivariance.
- Identified Transformer recursions.
- In-context classification dynamics.
- Geometry-driven class separation.

## Connections to Other Papers

Connects to Context-Parameter Equivalence, Constrained Transformers, Modern Conservation Laws, OENN/CENN, and Fisher Memory Dynamics. All use mathematical structure to expose otherwise opaque neural computation.

## Notes for Cross-Paper Synthesis

This paper reinforces the theory-unifies-practice thread: constraining a model by the right symmetry can turn black-box in-context behavior into an analyzable iterative algorithm.
