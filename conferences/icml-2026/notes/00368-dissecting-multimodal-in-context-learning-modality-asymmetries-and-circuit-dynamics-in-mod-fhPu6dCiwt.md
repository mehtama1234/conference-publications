# Dissecting Multimodal In-Context Learning: Modality Asymmetries and Circuit Dynamics in modern Transformers

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: fhPu6dCiwt
- Authors: Yiran Huang; Karsten Roth; Quentin Bouniot; Wenjia Xu; Zeynep Akata
- Primary area: deep_learning->attention_mechanisms
- Keywords: In-Context learning;Transformer learning
- Source URL: https://openreview.net/forum?id=fhPu6dCiwt
- PDF URL: https://openreview.net/pdf?id=fhPu6dCiwt

## Abstract

Transformer-based multimodal large language models often exhibit in-context learning (ICL) capabilities. Motivated by this phenomenon, we ask: how do transformers learn to associate information across modalities from in-context examples? We investigate this through controlled experiments on small transformers trained on synthetic classification tasks, enabling precise manipulation of data statistics and model architecture. We begin by revisiting core principles of unimodal ICL in modern transformers. While several prior findings replicate, we find that Rotary Position Embeddings (RoPE) can delay the onset of ICL circuits. Extending to the multimodal setting reveals a fundamental learning asymmetry: when pretrained on high-diversity data from a primary modality, surprisingly low data complexity in the secondary modality suffices for multimodal ICL to emerge. Mechanistic analysis shows that both settings rely on an induction-style mechanism that copies labels from matching in-context exemplars; multimodal training refines and extends these circuits across modalities. Our findings provide a mechanistic foundation for understanding multimodal ICL in modern transformers and introduce a controlled testbed for future investigation. Code is available at: https://github.com/YiranHuangIrene/multimodal-icl

## One-Sentence Claim

Controlled transformer experiments show that multimodal in-context learning emerges through induction-style circuits with strong asymmetry between primary and secondary modalities.

## Problem

Modern multimodal transformers can learn from in-context examples, but the mechanism by which they associate information across modalities is poorly understood. Large pretrained models are difficult to manipulate, making causal circuit analysis hard.

The paper builds a controlled synthetic setting to ask how data diversity, architecture, and modality roles shape multimodal ICL circuits.

## Core Contribution

The paper identifies a modality asymmetry: when a model is pretrained on high-diversity data from a primary modality, surprisingly low complexity in a secondary modality is enough for multimodal ICL to emerge. It also finds that RoPE can delay the onset of ICL circuits.

Mechanistically, both unimodal and multimodal settings rely on an induction-style mechanism that copies labels from matching in-context exemplars, with multimodal training refining and extending these circuits across modalities.

## Method

The authors train small transformers on synthetic classification tasks where data statistics and architecture can be precisely manipulated. They revisit unimodal ICL principles, then extend the setup to paired multimodal tasks.

Mechanistic analysis tracks circuit dynamics, especially induction-like label copying, and studies how RoPE and modality diversity influence emergence.

## Experiments and Evidence

Evidence reported in the abstract:

- Controlled synthetic classification tasks.
- Replication of several unimodal ICL findings.
- Finding that RoPE can delay ICL circuit onset.
- Discovery of primary-secondary modality asymmetry.
- Mechanistic evidence for induction-style label-copying circuits.
- Code release at the listed GitHub URL.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: synthetic task construction, circuit probes, model sizes, and whether findings transfer to real multimodal LLMs.

## Limits and Failure Modes

- Small synthetic transformers may not capture all mechanisms in production-scale multimodal models.
- Primary/secondary modality asymmetry may depend on the chosen task distribution.
- RoPE effects could interact with length, architecture, and training schedule.
- Induction-style circuits explain matching-label tasks but may not explain richer multimodal reasoning.

## Deep Themes

**Multimodal capability can piggyback on a strong primary modality.** Diversity in one modality may scaffold lower-complexity learning in another.

**ICL is circuit dynamics.** The paper treats in-context learning as an emergent algorithm implemented by attention circuits.

**Architectural details shift capability onset.** RoPE is not neutral; it can delay when ICL mechanisms appear.

## Subthemes

- Multimodal in-context learning.
- Modality asymmetry.
- Induction-style label copying.
- RoPE-delayed circuit emergence.
- Synthetic mechanistic testbeds.

## Connections to Other Papers

Connects to Symmetry ICL Dynamics, Context-Parameter Equivalence, MoCA, Agent0-VL, and Real-Time Visual Attribution. Together these papers analyze how multimodal or in-context reasoning is represented internally rather than only measured behaviorally.

## Notes for Cross-Paper Synthesis

This paper extends the mechanistic ICL theme into multimodality: cross-modal learning may be less symmetric than benchmarks imply, with one modality providing most of the reusable algorithmic scaffold.
