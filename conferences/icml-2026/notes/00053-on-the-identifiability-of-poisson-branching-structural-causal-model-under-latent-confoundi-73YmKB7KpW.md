# On the Identifiability of Poisson Branching Structural Causal Model Under Latent Confounding

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 73YmKB7KpW
- Authors: Jie Qiao; Zihuai Zeng; Ruichu Cai; Zhengming Chen; Zhifeng Hao
- Primary area: probabilistic_methods->structure_learning
- Keywords: Causal discovery;Causality;Count data;Poisson Branching Structural Causal Model
- Source URL: https://openreview.net/forum?id=73YmKB7KpW
- PDF URL: https://openreview.net/pdf?id=73YmKB7KpW

## Abstract

Causal discovery from observational count data poses unique challenges, particularly when the data exhibit inherent branching structures, such as an upstream ad impression event triggering a downstream purchase event with certain probability. Such branching dynamics are naturally modeled by thinning operators (for branching) and an independent Poisson distribution (for exogenous noise), constituting a Poisson Branching Structural Causal Model (PB-SCM). However, existing approaches based on PB-SCM rely on the restrictive assumption of causal sufficiency, failing to account for ubiquitous latent confounders. In this work, we propose a Latent Confounding Poisson Branching Structural Causal Model (LC-PB-SCM) to bridge this gap. We leverage Probability Generating Function (PGF) to characterize the complex dependencies introduced by latent confounding. Then, we establish a Trie representation theorem that maps the branching structure to algebraic properties of PGF monomials. Based on local PGF, we establish a complete identifiability condition for local 3-variables covering all causal patterns distinguishable up to monomial equivalence. Finally, we propose a practical algorithm to learn causal structures under latent confounding and demonstrate its effectiveness through experiments on both synthetic and real-world datasets.

## One-Sentence Claim

Latent-confounded Poisson branching causal models can be identified locally by representing branching dependencies through probability-generating-function monomials and trie structure.

## Problem

Observational count data often has branching causal dynamics and latent confounding, but existing Poisson Branching SCM methods commonly assume causal sufficiency.

## Core Contribution

The paper introduces LC-PB-SCM, uses probability generating functions to characterize latent-confounded branching dependencies, proves a trie representation theorem, and gives local identifiability conditions for three-variable patterns up to monomial equivalence.

## Method

It models branching with thinning operators and Poisson exogenous noise, then analyzes local PGFs algebraically. Trie representations map causal branching structure to monomial properties, enabling an identifiability condition and practical causal-structure learning algorithm.

## Experiments and Evidence

The abstract reports experiments on synthetic and real-world datasets demonstrating the practical algorithm's effectiveness.

## Limits and Failure Modes

No confident local PDF/arXiv match yet, so details still need checking: exact local three-variable conditions, scalability beyond local patterns, assumptions on count distributions, and robustness to model misspecification.

## Deep Themes

- Causal discovery is becoming more distribution-specific rather than one-size-fits-all.
- Latent confounding can sometimes be handled through algebraic structure in the data-generating family.
- Count-data causality needs mechanisms that respect branching and thinning.

## Subthemes

- Poisson branching SCMs.
- Latent confounding.
- Count data.
- Probability generating functions.
- Trie representation.
- Local identifiability.

## Connections to Other Papers

Connects to Linear Causal Representation Learning through identifiability under weaker assumptions, and to robust contextual optimization through structured modeling of data-generating processes.

## Notes for Cross-Paper Synthesis

This paper adds a causal-identifiability theme: realistic causal models increasingly relax clean assumptions by exploiting domain-specific algebraic or distributional structure.
