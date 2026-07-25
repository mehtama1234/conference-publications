# Modality-free Graph In-context Alignment

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: cDc95lucVL
- Authors: Wei Zhuo; Siqiang Luo
- Primary area: learning on graphs and other geometries & topologies
- Keywords: Graph foundation model;In-context learning;Pretraining
- Source URL: https://openreview.net/forum?id=cDc95lucVL
- PDF URL: https://openreview.net/pdf?id=cDc95lucVL

## Abstract

In-context learning (ICL) converts static encoders into task-conditioned reasoners, enabling adaptation to new data from just a few examples without updating pretrained parameters. This capability is essential for graph foundation models (GFMs) to approach LLM-level generality. Yet current GFMs struggle with cross-domain alignment, typically relying on modality-specific encoders that fail when graphs are pre-vectorized or raw data is inaccessible. In this paper, we introduce **M**odality-**F**ree **G**raph **I**n-context **A**lignment (MF-GIA), a framework that makes a pretrained graph encoder promptable for few-shot prediction across heterogeneous domains without modality assumptions. MF-GIA captures domain characteristics through gradient fingerprints, which parameterize lightweight transformations that align pre-encoded features and indexed labels into unified semantic spaces. During pretraining, a dual prompt-aware attention mechanism with episodic objective learns to match queries against aligned support examples to establish prompt-based reasoning capabilities. At inference, MF-GIA performs parameter-update-free adaptation using only a few-shot support set to trigger cross-domain alignment and enable immediate prediction on unseen domains. Experiments demonstrate that MF-GIA achieves superior few-shot performance across diverse graph domains and strong generalization to unseen domains. The code is available at https://github.com/JhuoW/MF-GIA.

## One-Sentence Claim

MF-GIA makes pretrained graph encoders promptable across heterogeneous domains by using gradient fingerprints to align pre-encoded features and labels without modality assumptions.

## Problem

Graph foundation models need in-context learning to adapt to new graph domains from a few examples without parameter updates.

Current GFMs often rely on modality-specific encoders, which fail when only pre-vectorized graph features are available or raw modality data cannot be accessed.

## Core Contribution

The paper introduces Modality-Free Graph In-context Alignment.

MF-GIA captures domain characteristics through gradient fingerprints, parameterizes lightweight transformations to align pre-encoded features and indexed labels, and trains prompt-aware attention for few-shot reasoning.

## Method

During pretraining, MF-GIA uses a dual prompt-aware attention mechanism with an episodic objective so queries can be matched against aligned support examples.

At inference, it performs parameter-update-free adaptation from a few-shot support set, using gradient-fingerprint-conditioned transformations to align unseen domains.

## Experiments and Evidence

The abstract reports superior few-shot performance across diverse graph domains.

MF-GIA also shows strong generalization to unseen domains while making no assumptions about raw input modality.

## Limits and Failure Modes

Gradient fingerprints may depend on support-set quality and may be noisy with very few examples. Pre-encoded features can also lose information that no alignment method can recover.

Because this note is abstract-only, details still need checking: fingerprint computation, transformation family, graph datasets, support sizes, encoder types, and unseen-domain split design.

## Deep Themes

- Modality-free graph adaptation: graph reasoning should work even when raw node/edge modalities are unavailable.
- Promptable graph encoders: static graph representations become few-shot task-conditioned reasoners.
- Gradient fingerprints as domain descriptors: small support sets encode domain alignment signals.
- Parameter-free inference adaptation: domain shifts are handled through prompts and lightweight alignment, not fine-tuning.

## Subthemes

- Graph foundation models.
- In-context learning.
- Gradient fingerprints.
- Cross-domain alignment.

## Connections to Other Papers

This connects to Actions Speak Louder than Prompts, UniImb, GNN exchangeability, and graph anomaly/federated graph papers.

It also relates to Train-before-Test and WAVE because all examine task-conditioned representations and adaptation.

## Notes for Cross-Paper Synthesis

MF-GIA adds a graph-foundation-model theme: few-shot graph adaptation needs domain alignment that does not assume access to raw modality-specific encoders.
