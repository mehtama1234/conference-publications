# Mechanistic Data Attribution: Tracing the Training Origins of Interpretable LLM Units

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: PQaxfoEcRc
- Authors: Jianhui Chen; Yuzhang Luo; Liangming Pan
- Primary area: social_aspects->accountability_transparency_and_interpretability
- Keywords: Large Language Models;Mechanistic Interpretability;In-context Learning
- Source URL: https://openreview.net/forum?id=PQaxfoEcRc
- PDF URL: https://openreview.net/pdf?id=PQaxfoEcRc

## Abstract

While mechanistic interpretability has identified interpretable circuits in large language models (LLMs), their causal origins in training data remain elusive. We introduce *mechanistic data attribution* (MDA), a scalable framework that employs influence functions to trace interpretable units back to specific training samples. Through extensive experiments on the Pythia family, we causally validate that targeted intervention—removing or augmenting a small fraction of high-influence samples—significantly modulates the emergence of interpretable heads, whereas random interventions show no effect. Our analysis reveals that repetitive structural data (e.g., LaTeX, XML) acts as a mechanistic catalyst. Furthermore, we observe that interventions targeting induction head formation induce a concurrent change in the model’s in-context learning (ICL) capability. This provides direct causal evidence for the long-standing hypothesis regarding the functional link between induction heads and ICL. Finally, we propose a mechanistic data augmentation pipeline that consistently accelerates circuit convergence across model scales, providing a principled methodology for steering the developmental trajectories of LLMs.

## One-Sentence Claim

Mechanistic Data Attribution traces interpretable LLM units back to influential training samples and shows targeted data interventions can modulate circuit emergence and in-context learning.

## Problem

Mechanistic interpretability can identify circuits, but the causal origins of those circuits in training data are usually unknown.

## Core Contribution

The paper introduces MDA, a scalable influence-function framework linking interpretable units to training examples, and uses it to causally manipulate the emergence of heads and accelerate circuit convergence.

## Method

MDA computes influence of training samples on interpretable units, then validates causality by removing or augmenting high-influence samples in Pythia-family training experiments and measuring circuit formation and ICL behavior.

## Experiments and Evidence

The abstract reports that small targeted interventions significantly modulate interpretable head emergence while random interventions do not; repetitive structural data such as LaTeX and XML acts as a mechanistic catalyst; induction-head interventions concurrently change ICL capability; and mechanistic data augmentation accelerates circuit convergence across scales.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: influence-function approximation, compute cost, Pythia scales, retraining protocol, circuit metrics, and whether findings generalize beyond induction-like heads.

## Deep Themes

- Circuits have data lineages that can be traced and edited.
- Training data can catalyze specific mechanisms, not just improve aggregate loss.
- Mechanistic interpretability can guide data augmentation.

## Subthemes

- Mechanistic interpretability.
- Data attribution.
- Influence functions.
- Induction heads.
- In-context learning.
- Structural training data.

## Connections to Other Papers

Connects to neuron-basis circuits, FAC Synthesis, SVD interpretability, and data-selection papers through causal links between data and internal mechanisms.

## Notes for Cross-Paper Synthesis

MDA adds a developmental interpretability theme: to understand a circuit, trace not only what it does now but which training examples caused it to form.
