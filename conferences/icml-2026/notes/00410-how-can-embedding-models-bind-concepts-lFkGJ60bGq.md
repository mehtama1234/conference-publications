# How can embedding models bind concepts?

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: lFkGJ60bGq
- Authors: Arnas Uselis; Darina Koishigarina; Seong Joon Oh
- Primary area: general_machine_learning
- Keywords: compositionality;binding;generalization
- Source URL: https://openreview.net/forum?id=lFkGJ60bGq
- PDF URL: https://openreview.net/pdf?id=lFkGJ60bGq

## Abstract

Humans easily determine which color belongs to which shape in multi-object scenes, an ability known as concept binding. Vision–language embedding models such as CLIP struggle with binding: they recognize individual concepts but fail to represent which concepts form which objects. Although CLIP behaves like a bag-of-concepts model in cross-modal retrieval, object information is recoverable from its image and text embeddings separately. We study this tension through the binding function, which maps concepts to scene embeddings.
We find that scene embeddings decompose additively into object representations, explaining why uni-modal probes can recover object information. However, CLIP’s binding function is high-complexity, which likely prevents the image and text encoders from learning a shared binding mechanism that generalizes to unseen concept combinations.
We then ask whether this limitation is fundamental. We show that it is not. In controlled transformer models trained from scratch, binding generalization emerges with sufficient data coverage. These models learn low-complexity binding functions characterized by multiplicative interactions between concepts, enabling systematic generalization.

## One-Sentence Claim

CLIP-like embeddings contain recoverable object information but fail systematic concept binding because their shared binding function is too complex; controlled Transformers can learn low-complexity multiplicative binding with sufficient coverage.

## Problem

Vision-language embedding models can recognize concepts such as colors and shapes but often fail to bind which attribute belongs to which object. This produces bag-of-concepts behavior in retrieval even though object information may be recoverable from each modality separately.

The paper asks how embedding models represent concept-to-object binding and whether the limitation is fundamental.

## Core Contribution

The paper studies the binding function mapping concepts to scene embeddings. It finds that scene embeddings decompose additively into object representations, explaining why unimodal probes recover object information.

However, CLIP's binding function is high-complexity, preventing shared image/text binding mechanisms from generalizing to unseen combinations. Controlled Transformers trained from scratch can learn low-complexity multiplicative binding functions when data coverage is sufficient.

## Method

The analysis probes image and text embeddings separately and jointly to characterize object information and binding behavior. It studies additive decomposition of scene embeddings and complexity of the cross-modal binding function.

Controlled Transformer experiments vary data coverage to test whether systematic binding generalization can emerge from scratch.

## Experiments and Evidence

Evidence reported in the abstract:

- CLIP behaves like a bag-of-concepts model in cross-modal retrieval.
- Object information is recoverable from image and text embeddings separately.
- Scene embeddings decompose additively into object representations.
- CLIP's binding function is high-complexity.
- Controlled Transformers learn low-complexity multiplicative binding with sufficient data coverage.
- Such binding enables systematic generalization to unseen concept combinations.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: datasets, binding-complexity metric, probe methods, and controlled-model setup.

## Limits and Failure Modes

- Controlled synthetic settings may not transfer fully to natural images.
- Sufficient coverage for binding may be expensive in real concept spaces.
- Additive decomposition may obscure interactions such as occlusion or relations.
- Probe recoverability does not guarantee usable cross-modal retrieval behavior.

## Deep Themes

**Concept recognition is not concept binding.** Models may know the pieces without representing which pieces belong together.

**Compositional generalization depends on binding-function complexity.** Low-complexity multiplicative interactions support systematic transfer.

**Data coverage can change mechanism class.** Binding emerges when training exposes enough combinations.

## Subthemes

- Concept binding.
- CLIP bag-of-concepts behavior.
- Additive scene embeddings.
- Multiplicative concept interactions.
- Systematic compositional generalization.

## Connections to Other Papers

Connects to MoCA, Multimodal ICL Circuits, Visual Attribution Streaming, VideoKR, and 2-SAT Robustness. It adds a multimodal representation explanation for failures that benchmarks often expose behaviorally.

## Notes for Cross-Paper Synthesis

This paper strengthens the compositionality theme: robust multimodal reasoning requires binding mechanisms, not just high-quality single-concept embeddings.
