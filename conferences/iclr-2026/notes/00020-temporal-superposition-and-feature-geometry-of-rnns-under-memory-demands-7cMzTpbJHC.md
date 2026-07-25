# Temporal superposition and feature geometry of RNNs under memory demands

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 7cMzTpbJHC
- Authors: Pratyaksh Sharma; Alexandra Maria Proca; Lucas Prieto; Pedro A. M. Mediano
- Primary area: interpretability and explainable AI
- Keywords: RNNs;superposition;representational geometry;features;capacity;memory demands
- Source URL: https://openreview.net/forum?id=7cMzTpbJHC
- PDF URL: https://openreview.net/pdf?id=7cMzTpbJHC

## Abstract

Understanding how populations of neurons represent information is a central challenge across machine learning and neuroscience. Recent work in both fields has begun to characterize the representational geometry and functionality underlying complex distributed activity. For example, artificial neural networks trained on data with more features than neurons compress data by representing features non-orthogonally in so-called *superposition*. However, the effect of time (or memory), an additional capacity-constraining pressure, on underlying representational geometry in recurrent models is not well understood. Here, we study how memory demands affect representational geometry in recurrent neural networks (RNNs), introducing the concept of temporal superposition. We develop a theoretical framework in RNNs with linear recurrence trained on a delayed serial recall task to better understand how properties of the data, task demands, and network dimensionality lead to different representational strategies, and show that these insights generalize to nonlinear RNNs. Through this, we identify an effectively linear, dense regime and a sparse regime where RNNs utilize an interference-free space, characterized by a phase transition in the angular distribution of features and decrease in spectral radius. Finally, we analyze the interaction of spatial and temporal superposition to observe how RNNs mediate different representational tradeoffs. Overall, our work offers a mechanistic, geometric explanation of representational strategies RNNs learn, how they depend on capacity and task demands, and why.

## One-Sentence Claim

Memory demands induce temporal superposition in RNNs, creating distinct dense and sparse representational regimes governed by capacity, task structure, and feature geometry.

## Problem

Superposition explains how networks represent more features than neurons by allowing non-orthogonal feature directions, but most work studies static representations. Recurrent networks add time and memory as additional capacity constraints.

The problem is to understand how memory demands reshape representational geometry in RNNs.

## Core Contribution

The paper introduces temporal superposition and develops a theoretical framework for linear recurrent networks trained on delayed serial recall.

It identifies an effectively linear dense regime and a sparse interference-free regime, with a phase transition in angular feature distributions and a decrease in spectral radius.

## Method

The authors study linear recurrence under delayed serial recall to derive how data properties, memory demands, and network dimensionality shape representational strategies.

They then show the insights generalize to nonlinear RNNs and analyze interactions between spatial and temporal superposition.

## Experiments and Evidence

The abstract reports a phase transition in feature-angle distributions and a decrease in spectral radius when moving into the sparse regime.

It also reports that the linear theory provides insights that carry over to nonlinear RNNs.

## Limits and Failure Modes

The framework begins with delayed serial recall and linear recurrence, so generalization to arbitrary recurrent tasks or gated architectures needs verification.

Because this note is abstract-only, details still need checking: task distribution, exact phase transition criterion, nonlinear RNN experiments, dimensional scaling, and relation to LSTMs/GRUs/modern sequence models.

## Deep Themes

- Temporal superposition: memory creates its own representational compression pressure.
- Geometry under capacity constraints: feature angles and spectral radius reveal strategy shifts.
- Dense versus sparse memory regimes: RNNs can either tolerate interference or allocate interference-free space.
- Mechanistic bridges to neuroscience: population activity and artificial recurrence share representational geometry questions.

## Subthemes

- Delayed serial recall.
- Spatial-temporal superposition interaction.
- Spectral-radius changes.
- Feature-angle phase transition.

## Connections to Other Papers

This connects to ICML's linear recurrent memory paper, POPGym, LAMP, and temporal graph memory explanation through how memory is represented under capacity limits.

It also relates to transformer accessible-sequence bounds and reasoning dimensionality because both analyze capacity through geometry rather than only performance.

## Notes for Cross-Paper Synthesis

Temporal superposition adds a geometric memory theme: memory is not just stored or forgotten; it is packed into a representational space with interference tradeoffs.
