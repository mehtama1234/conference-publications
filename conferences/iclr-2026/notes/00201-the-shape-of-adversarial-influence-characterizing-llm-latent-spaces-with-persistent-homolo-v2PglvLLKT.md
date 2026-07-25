# The Shape of Adversarial Influence: Characterizing LLM Latent Spaces with Persistent Homology

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: v2PglvLLKT
- Authors: Aideen Fay; Inés García-Redondo; Qiquan Wang; Haim Dubossarsky; Anthea Monod
- Primary area: interpretability and explainable AI
- Keywords: Persistent Homology;Interpretability;Topological Data Analysis;Representation Geometry;Large Language Models;AI Security;Adversarial Attacks;Sparse Autoencoders
- Source URL: https://openreview.net/forum?id=v2PglvLLKT
- PDF URL: https://openreview.net/pdf?id=v2PglvLLKT

## Abstract

Existing interpretability methods for Large Language Models (LLMs) often fall short by focusing on linear directions or isolated features, overlooking the high-dimensional, nonlinear, and relational geometry within model representations. This study focuses on how adversarial inputs systematically affect the internal representation spaces of LLMs, a topic which remains poorly understood. We propose the application of persistent homology (PH) to measure and understand the geometry and topology of the representation space when the model is under external adversarial influence. Specifically, we use PH to systematically interpret six state-of-the-art models under two distinct adversarial conditions—indirect prompt injection and backdoor fine-tuning—and uncover a consistent topological signature of adversarial influence. Across architectures and model sizes, adversarial inputs induce "topological compression'', where the latent space becomes structurally simpler, collapsing from varied, compact, small-scale features into fewer, dominant, and more dispersed large-scale ones. This topological signature is statistically robust across layers, highly discriminative, and provides interpretable insights into how adversarial effects emerge and propagate. By quantifying the shape of activations and neuron-level information flow, our architecture-agnostic framework reveals fundamental invariants of representational change, offering a complementary perspective to existing interpretability methods.

## One-Sentence Claim

Persistent homology reveals a robust topological compression signature in LLM activations under adversarial influence, across prompt injection and backdoor fine-tuning.

## Problem

Many interpretability methods focus on linear directions or isolated sparse features, which can miss nonlinear and relational changes in representation space. The internal geometry of LLMs under adversarial inputs remains poorly characterized, especially across different adversarial mechanisms.

## Core Contribution

The paper applies persistent homology to LLM representation spaces under indirect prompt injection and backdoor fine-tuning, identifying a consistent topological signature of adversarial influence and proposing an architecture-agnostic analysis framework.

## Method

The method computes persistent-homology summaries over activation geometry and neuron-level information flow across layers for six state-of-the-art models. It compares normal and adversarial conditions to detect how representation topology changes under attack.

## Experiments and Evidence

Across architectures and model sizes, adversarial inputs reportedly induce topological compression: varied compact small-scale features collapse into fewer dominant, dispersed large-scale structures. The signature is statistically robust across layers, highly discriminative, and interpretable.

## Limits and Failure Modes

Persistent homology can be computationally expensive and sensitive to representation sampling, distance metrics, and layer choice. The adversarial settings may not cover all attack families. Full-text review should check PH pipeline, statistical tests, model list, attack construction, discriminative baselines, and whether topological compression predicts downstream harm.

## Deep Themes

- Topological interpretability of LLM representations.
- Adversarial influence as representation-geometry shift.
- Architecture-agnostic attack diagnostics.
- Nonlinear latent-space analysis beyond features.

## Subthemes

- Persistent homology.
- Topological compression.
- Indirect prompt injection.
- Backdoor fine-tuning.
- Neuron-level information flow.

## Connections to Other Papers

Connects to divergent causal interventions, low-rank logits, representation-geometry papers, and security benchmarks through internal diagnostics for adversarial or unsafe behavior.

## Notes for Cross-Paper Synthesis

This paper adds a topological layer to the interpretability-as-diagnostics theme: attacks can reshape the global geometry of activations, not just trigger isolated features.
