# Distributional Equivalence in Linear Non-Gaussian Latent-Variable Cyclic Causal Models: Characterization and Learning

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: b8TlYh6PN6
- Authors: Haoyue Dai; Immanuel Albrecht; Peter Spirtes; Kun Zhang
- Primary area: causal reasoning
- Keywords: causal discovery;latent variables;equivalence;rank constraints;linear non-Gaussian models;cycles
- Source URL: https://openreview.net/forum?id=b8TlYh6PN6
- PDF URL: https://openreview.net/pdf?id=b8TlYh6PN6

## Abstract

Causal discovery with latent variables is a fundamental task. Yet most existing methods rely on strong structural assumptions, such as enforcing specific indicator patterns for latents or restricting how they can interact with others. We argue that a core obstacle to a general, structural-assumption-free approach is the lack of an equivalence characterization: without knowing what can be identified, one generally cannot design methods for how to identify it. In this work, we aim to close this gap for linear non-Gaussian models. We establish the graphical criterion for when two graphs with arbitrary latent structure and cycles are distributionally equivalent, that is, they induce the same observed distribution set. Key to our approach is a new tool, edge rank constraints, which fills a missing piece in the toolbox for latent-variable causal discovery in even broader settings. We further provide a procedure to traverse the whole equivalence class and develop an algorithm to recover models from data up to such equivalence. To our knowledge, this is the first equivalence characterization with latent variables in any parametric setting without structural assumptions, and hence the first structural-assumption-free discovery method. Code and an interactive demo are available at https://equiv.cc.

## One-Sentence Claim

This paper characterizes distributional equivalence for linear non-Gaussian causal models with arbitrary latent variables and cycles, enabling structural-assumption-free discovery up to equivalence.

## Problem

Causal discovery with latent variables is fundamental but often relies on strong structural assumptions about latent indicators or interaction patterns.

Without knowing which graphs are distributionally equivalent, researchers cannot know what is identifiable or design general discovery algorithms.

## Core Contribution

The paper gives a graphical criterion for when two graphs with arbitrary latent structure and cycles induce the same observed distribution set.

It introduces edge rank constraints as a new tool for latent-variable causal discovery, provides a procedure to traverse equivalence classes, and develops a data-recovery algorithm up to equivalence.

## Method

The analysis focuses on linear non-Gaussian models with latent variables and cycles.

Edge rank constraints capture distributional restrictions that remain visible in observed variables, helping characterize equivalence without assuming special latent structures.

## Experiments and Evidence

The abstract emphasizes theoretical characterization and an algorithmic procedure.

It also reports code and an interactive demo, suggesting the equivalence traversal and learning method are implemented for exploration.

## Limits and Failure Modes

The result is for linear non-Gaussian models; nonlinear, Gaussian, time-varying, or selection-biased systems may require different equivalence tools.

Because this note is abstract-only, details still need checking: exact graphical criterion, edge rank constraint definition, proof scope, learning algorithm, finite-sample behavior, and demo examples.

## Deep Themes

- Identifiability before estimation: discovery methods require knowing what can be recovered.
- Latent-variable equivalence: arbitrary hidden structure and cycles can be characterized without special indicator assumptions.
- Rank constraints as causal signal: algebraic restrictions become tools for graph equivalence.
- Discovery up to equivalence: honest causal learning returns identifiable classes rather than overclaiming a single graph.

## Subthemes

- Causal discovery.
- Linear non-Gaussian models.
- Latent variables and cycles.
- Edge rank constraints.

## Connections to Other Papers

This connects to Neural Effect Search, causal identifiability papers, source screening, and representation-invariance work.

It also relates to TabStruct because both focus on hidden causal structure when direct ground truth is unavailable.

## Notes for Cross-Paper Synthesis

This paper strengthens the causal-theory theme: robust causal ML often begins with equivalence characterization, not with a new estimator.
