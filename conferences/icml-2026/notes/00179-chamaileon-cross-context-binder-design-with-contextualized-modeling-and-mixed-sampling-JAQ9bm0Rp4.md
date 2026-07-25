# Chamaileon: Cross-Context Binder Design with Contextualized Modeling and Mixed Sampling

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: JAQ9bm0Rp4
- Authors: Hengyuan Cao; Shizhuo Cheng; Mingxuan Liu; Weicheng Huang; Yunhong Lu; CAI CHENXI; Yan Zhang; Min Zhang
- Primary area: applications->health_medicine
- Keywords: cross-context binder design;in-context generation;mixed sampling;diffusion model;binder design
- Source URL: https://openreview.net/forum?id=JAQ9bm0Rp4
- PDF URL: https://openreview.net/pdf?id=JAQ9bm0Rp4

## Abstract

The rapid evolution of generative models has unlocked new potentials in protein binder design, a pivotal task in structural biology, by facilitating end-to-end generation via joint sequence-structure modeling or hallucination. However, existing approaches are predominantly implemented under a single-target, single-state assumption, limiting their ability to model multi-target or multi-state interactions required for advanced function-oriented protein design. Here, we introduce Chamaileon, which unifies multi-target and multi-state binder design by formulating the problem as cross-context binding landscape modeling. The framework is underpinned by a training paradigm termed \textit{In-Context Complex Co-Design (I3CD)} for context-aware sequence-structure co-modeling. During inference, we employ \textit{Mixture-of-Paths Sampling (MoPS)}, a scalable strategy that optimizes a single sequence across contexts while alleviating the scarcity of high-quality multi-conformational paired data. Extensive evaluation on our newly constructed benchmark, \textit{CROSS}, demonstrates that Chamaileon effectively generates sequences adaptable to diverse conformational landscapes and multi-target requirements.

## One-Sentence Claim

Chamaileon designs protein binders across multiple targets and conformational states by modeling a cross-context binding landscape and sampling sequences that work across contexts.

## Problem

Generative binder-design systems are often built for single-target, single-state settings, which limits function-oriented protein design where binders must satisfy multi-target or multi-state interaction requirements.

## Core Contribution

The paper formulates binder design as cross-context binding landscape modeling, introduces In-Context Complex Co-Design for context-aware sequence-structure modeling, and uses Mixture-of-Paths Sampling for scalable multi-context inference.

## Method

Chamaileon jointly models sequence and structure under contextualized binding settings. At inference, MoPS optimizes a single sequence across multiple contexts while mitigating scarce high-quality multi-conformational paired data.

## Experiments and Evidence

The abstract reports extensive evaluation on a new CROSS benchmark, showing generation of sequences adaptable to diverse conformational landscapes and multi-target requirements.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: benchmark construction, wet-lab validation status, structural scoring metrics, target/state diversity, data scarcity handling, and failure modes for conflicting contexts.

## Deep Themes

- Scientific generation is shifting from single-instance design to context-conditioned landscapes.
- In-context generative modeling can represent multi-state biological constraints.
- Sampling strategy matters when high-quality paired scientific data are scarce.

## Subthemes

- Protein binder design.
- Sequence-structure co-design.
- Diffusion models.
- Multi-target binding.
- Multi-state conformations.
- Mixed/path sampling.

## Connections to Other Papers

Connects to scientific generative modeling, diffusion guidance, and AI-for-science dynamics papers. It also parallels multi-context adaptation themes in VLA and federated learning.

## Notes for Cross-Paper Synthesis

Chamaileon adds a biological-design version of multi-context generalization: useful generated artifacts must satisfy a landscape of constraints rather than optimize a single static target.
