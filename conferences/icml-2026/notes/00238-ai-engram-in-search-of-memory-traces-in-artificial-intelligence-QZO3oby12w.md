# AI Engram: In Search of Memory Traces in Artificial Intelligence

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: QZO3oby12w
- Authors: Jea Kwon; Dong-Kyum Kim; Jiwon Kim; Yonghyun Kim; Woong Kook; Meeyoung Cha
- Primary area: applications->neuroscience_cognitive_science
- Keywords: Memory Traces;Engram;Mechanistic Interpretability;Machine Unlearning;Geometric Deep Learning;Entanglement;Neuroscience-Inspired AI;Spectral Methods
- Source URL: https://openreview.net/forum?id=QZO3oby12w
- PDF URL: https://openreview.net/pdf?id=QZO3oby12w

## Abstract

Memory formation is fundamental to intelligence, yet whether deep neural networks preserve identifiable memory traces analogous to biological memory units remains an open question. This work introduces a geometric framework to identify such “AI engrams” by formalizing the neuroscientific criteria of specificity, reactivation, sufficiency, and necessity into a constrained inverse problem. We derive a closed-form estimator that isolates individual memory traces from globally entangled parameters, and show that this biologically-derived solution corresponds to a natural gradient update on the parameter manifold. AI engrams enable surgical manipulation of learned knowledge: any subset of memories can be composed or erased through linear arithmetic, without iterative optimization. Experiments ranging from simple MLPs to LLMs demonstrate the causal validity and substantial scalability of AI engrams. Together, these results bridge theories of biological memory and artificial representation learning and offer geometric insight into how deep networks simultaneously support functional specificity within distributed storage.

## One-Sentence Claim

AI Engram identifies neural-network memory traces through a geometric inverse problem and enables linear composition or erasure of selected learned memories.

## Problem

It remains unclear whether deep networks preserve identifiable memory traces analogous to biological engrams despite storing knowledge in distributed, entangled parameters.

## Core Contribution

The paper formalizes neuroscientific engram criteria as specificity, reactivation, sufficiency, and necessity constraints, derives a closed-form estimator, and links it to natural-gradient updates on the parameter manifold.

## Method

The framework solves a constrained inverse problem to isolate individual memories from global parameters, then manipulates subsets of memories through linear arithmetic without iterative optimization.

## Experiments and Evidence

The abstract reports causal validity and scalability across simple MLPs and LLMs, showing memory composition and erasure behavior.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: memory definition, tasks/models, causal intervention metrics, scalability limits, collateral damage during erasure, and relation to machine unlearning guarantees.

## Deep Themes

- Memory can be treated as a geometric object on the parameter manifold.
- Biological criteria can inspire mechanistic AI interventions.
- Linear memory arithmetic suggests structured specificity inside distributed storage.

## Subthemes

- Memory traces.
- Engrams.
- Mechanistic interpretability.
- Machine unlearning.
- Natural gradients.
- Geometric deep learning.

## Connections to Other Papers

Connects to MDA, DiSC, Robust Harmful Features, and unlearning papers through memory localization, causal manipulation, and knowledge retention/erasure.

## Notes for Cross-Paper Synthesis

AI Engram adds a memory-mechanism theme: knowledge may be distributed yet still isolatable through the right geometric inverse formulation.
