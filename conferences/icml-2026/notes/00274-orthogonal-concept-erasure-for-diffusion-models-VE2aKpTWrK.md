# Orthogonal Concept Erasure for Diffusion Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: VE2aKpTWrK
- Authors: Yuhao Sun; Lingyun Yu; Hao-Xiang Xu; Fengyuan Miao; Zhuoer Xu; Hongtao Xie
- Primary area: social_aspects->safety
- Keywords: Concept erasure;Diffusion models;Unlearning
- Source URL: https://openreview.net/forum?id=VE2aKpTWrK
- PDF URL: https://openreview.net/pdf?id=VE2aKpTWrK

## Abstract

Concept erasure has emerged as a promising approach to mitigate undesired or unsafe content in diffusion models, yet existing methods still face significant limitations. While training-based methods are effective, their high computational cost limits scalability. Editing-based methods are more efficient and deployment-friendly, yet they struggle to simultaneously achieve precise concept erasure and preserve overall generative capacity. We identify this core limitation of the editing-based methods as reliance on additive parameter updates. Our empirical analysis reveals that concept semantics primarily depend on *neuron direction* rather than *neuron magnitude*, while overall generative capacity relies on the *angular geometry* of neurons. As additive updates inherently entangle direction, magnitude, and angular geometry, they inevitably introduce unintended interference between concept erasure and overall generation performance. To address this, we propose **Orthogonal Concept Erasure (OCE)**, which reformulates editing-based erasure as multiplicative parameter updates from a geometric perspective. Specifically, OCE applies layer-wise orthogonal transformations derived from a closed-form solution to the parameters, enabling precise concept erasure while preserving the neuron magnitude and angular geometry. Furthermore, to address conflicting constraints in multi-concept erasure, OCE introduces a subspace-level objective with structured subspace manipulation, yielding a more effective and scalable erasure. Extensive experiments on single- and multi-concept erasure demonstrate that OCE outperforms existing methods in concept erasure and non-target preservation, erasing up to 100 concepts in 4.3 s. Code: https://github.com/HansSunY/OCE.

## One-Sentence Claim

Orthogonal Concept Erasure edits diffusion models with layer-wise multiplicative orthogonal transformations, removing target concepts while preserving neuron magnitudes and angular geometry.

## Problem

Diffusion concept erasure must remove unsafe or unwanted concepts without damaging general generation quality. Training-based methods can work but are expensive. Editing-based methods are efficient but often rely on additive parameter updates that entangle concept direction, neuron magnitude, and angular geometry.

The paper argues this entanglement prevents precise erasure and non-target preservation from being achieved together.

## Core Contribution

The paper identifies concept semantics as primarily direction-dependent, while overall generative capacity depends on angular neuron geometry. Orthogonal Concept Erasure reformulates editing-based erasure as multiplicative parameter updates using layer-wise orthogonal transformations from a closed-form solution.

For multi-concept erasure, OCE adds a subspace-level objective and structured subspace manipulation. It reportedly erases up to 100 concepts in 4.3 seconds.

## Method

OCE modifies parameter geometry through orthogonal transformations rather than additive deltas. Orthogonal updates preserve magnitudes and angular relationships more directly, aiming to rotate away target concept directions without degrading broad generative structure.

For multiple concepts, the method operates at the subspace level so constraints can be reconciled jointly rather than as conflicting independent edits.

## Experiments and Evidence

Evidence reported in the abstract:

- Empirical analysis separating neuron direction, magnitude, and angular geometry roles.
- Closed-form layer-wise orthogonal transformations for concept erasure.
- Single-concept and multi-concept erasure experiments.
- Better concept erasure and non-target preservation than existing methods.
- Erasure of up to 100 concepts in 4.3 seconds.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: concept datasets, safety metrics, non-target preservation metrics, model families, and whether erased concepts reappear under adversarial prompts.

## Limits and Failure Modes

- Direction-based erasure may miss distributed or context-dependent concepts.
- Orthogonal preservation of geometry may not preserve all downstream generation behavior.
- Multi-concept subspaces can overlap, creating tradeoffs not visible from aggregate metrics.
- Safety erasure must be tested against prompt paraphrases and compositional concepts.

## Deep Themes

**Safety edits should respect representation geometry.** OCE changes directions while preserving magnitudes and angular structure.

**Multiplicative transformations can reduce edit interference.** Orthogonal updates avoid some coupling introduced by additive deltas.

**Fast deployment-friendly unlearning is becoming central.** The method targets scalable editing rather than costly retraining.

## Subthemes

- Directional concept semantics.
- Orthogonal parameter updates.
- Multi-concept subspace erasure.
- Non-target preservation.
- Closed-form diffusion editing.

## Connections to Other Papers

Connects to GEM, Adversarial Concept Erasure, PRISM, and SVGT through geometry-aware safety interventions. It also links to SmoothSpike and ENGNN because orthogonal transformations are used as structure-preserving control.

## Notes for Cross-Paper Synthesis

OCE adds a sharp example of geometry-first safety: rather than adding an update and hoping damage is limited, it chooses a transformation class whose invariants match what should be preserved.
