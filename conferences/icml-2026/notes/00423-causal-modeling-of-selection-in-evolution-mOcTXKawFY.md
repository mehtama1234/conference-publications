# Causal Modeling of Selection in Evolution

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: mOcTXKawFY
- Authors: Haoyue Dai; Zeyu Tang; Peter Spirtes; Kun Zhang
- Primary area: general_machine_learning->causality
- Keywords: causal discovery;selection bias;evolution;graphical models
- Source URL: https://openreview.net/forum?id=mOcTXKawFY
- PDF URL: https://openreview.net/pdf?id=mOcTXKawFY

## Abstract

Understanding potential selection in data is crucial for causal discovery; we argue that "selection" in common narratives takes two forms, which we term _static_ and _evolutionary_ selection, respectively. Static selection refers to a one-shot filtering process where observed data consist of a _subset_ of the population of interest, as in survey volunteer bias. Evolutionary selection, in contrast, operates through repeated rounds of differential fitness in reproduction, where observed data constitute the latest _generation_ shaped by a historical trajectory, as in immune adaptation, antibiotic resistance, and social norm emergence. Existing methods largely conflate these two forms and rely on an identical graphical model of selection. We show that this model is valid for static settings but fails to characterize data under evolution, yielding false discovery results. To address this, we introduce a new model that specifically characterizes evolutionary selection, and develop a sound and complete procedure for identifying such models from data across one or multiple environments or generations. Experimental results validate the method's ability to uncover the relevant mechanisms underlying evolution from data.

## One-Sentence Claim

Evolutionary selection requires a different causal graphical model than static selection because observed data are the latest generation of repeated fitness filtering, not a one-shot population subset.

## Problem

Selection bias is central to causal discovery, but common narratives conflate static selection with evolutionary selection. Static selection is one-shot filtering, while evolutionary selection occurs through repeated differential reproduction over historical trajectories.

The paper argues that using the same graphical model for both can produce false causal discoveries.

## Core Contribution

The paper distinguishes static and evolutionary selection and introduces a causal model specifically for evolutionary selection. It shows that the standard selection model is valid for static filtering but fails for evolutionary data.

It develops a sound and complete procedure for identifying evolutionary-selection models from data across one or multiple environments or generations.

## Method

The method formalizes evolutionary selection as a process over generations, where observed variables reflect historical fitness dynamics. It then derives graphical constraints and an identification procedure tailored to that process.

Data across environments or generations provide evidence for uncovering the mechanisms underlying evolution.

## Experiments and Evidence

Evidence reported in the abstract:

- Distinction between static and evolutionary selection.
- Demonstration that common selection graphical models fail under evolution.
- New model for evolutionary selection.
- Sound and complete identification procedure.
- Works with data across one or multiple environments/generations.
- Experimental validation of mechanism recovery.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: model assumptions, graph semantics, and experimental domains.

## Limits and Failure Modes

- Evolutionary processes can include hidden mechanisms, mutation, migration, and feedback not captured by the model.
- Identifiability may depend on available environments or generations.
- Real biological and social evolution data can be sparse and confounded.
- Distinguishing static from evolutionary selection may itself be difficult from snapshots.

## Deep Themes

**Selection is not one phenomenon.** Static filtering and repeated evolutionary filtering create different causal signatures.

**Causal graphs need process semantics.** The same selection node cannot represent all data-generating histories.

**Temporal history shapes observed distributions.** Latest-generation data encode path-dependent mechanisms.

## Subthemes

- Evolutionary selection.
- Static selection bias.
- Causal discovery under selection.
- Multi-generation data.
- Sound and complete graphical identification.

## Connections to Other Papers

Connects to DiCoLa, Unpaired Causal IV, OU Identifiability, and causal fairness bandits. It adds a process-aware selection-bias model to the causal-learning theme.

## Notes for Cross-Paper Synthesis

This paper extends the corpus's causal theme by showing that the same observed bias can require different models depending on the historical process that produced it.
