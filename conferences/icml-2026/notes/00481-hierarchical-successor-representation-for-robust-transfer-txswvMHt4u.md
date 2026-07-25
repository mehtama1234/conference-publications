# Hierarchical Successor Representation for Robust Transfer

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: txswvMHt4u
- Authors: Changmin Yu; Máté Lengyel
- Primary area: reinforcement_learning
- Keywords: Hierarchical reinforcement learning;representation learning;successor representation
- Source URL: https://openreview.net/forum?id=txswvMHt4u
- PDF URL: https://openreview.net/pdf?id=txswvMHt4u

## Abstract

The successor representation (SR) provides a powerful framework for decoupling
  predictive dynamics from rewards, enabling rapid generalisation across reward
  configurations. However, the classical SR is limited by its inherent policy
  dependence: policies change due to ongoing learning, environmental
  non-stationarities, and changes in task demands, making established predictive
  representations obsolete. Furthermore, in topologically complex environments,
  SRs suffer from spectral diffusion, leading to dense and overlapping features
  that scale poorly. Here we propose the Hierarchical Successor Representation
  (HSR) for overcoming these limitations. By incorporating temporal abstractions
  into the construction of predictive representations, HSR learns stable state
  features which are robust to task-induced policy changes. Applying
  non-negative matrix factorisation (NMF) to the HSR yields a sparse, low-rank
  state representation that facilitates highly sample-efficient transfer to
  novel tasks in multi-compartmental environments. Further analysis reveals that
  HSR-NMF discovers interpretable topological structures, providing a
  policy-agnostic hierarchical map that effectively bridges model-free
  optimality and model-based flexibility. Beyond providing a useful basis for
  task-transfer, we show that HSR's temporally extended predictive structure can
  also be leveraged to drive efficient exploration, effectively scaling to
  large, procedurally generated environments.

## One-Sentence Claim

Hierarchical Successor Representations use temporal abstraction to build sparse, policy-robust predictive features that transfer efficiently across changing rewards and complex environments.

## Problem

Classical successor representations decouple dynamics from rewards, enabling fast transfer across reward changes. But SRs are policy-dependent: when policies shift through learning, nonstationarity, or task demands, the learned predictive representation can become obsolete.

In topologically complex environments, SRs also suffer from spectral diffusion, producing dense overlapping features that scale poorly and become hard to reuse.

## Core Contribution

The paper proposes Hierarchical Successor Representation, which incorporates temporal abstractions into predictive representations. HSR learns more stable state features that remain robust to task-induced policy changes.

Applying non-negative matrix factorization to HSR yields sparse, low-rank, interpretable representations that support sample-efficient transfer and expose topological structure in multi-compartment environments.

## Method

HSR builds successor-style predictive structure over temporally extended abstractions rather than only primitive one-step dynamics. This makes the representation less sensitive to local policy changes.

NMF decomposes the HSR into sparse low-rank state features. These features act as a hierarchical map that can support reward transfer and guide exploration in larger procedurally generated environments.

## Experiments and Evidence

The abstract reports highly sample-efficient transfer to novel tasks in multi-compartment environments, interpretable topological structures from HSR-NMF, and efficient exploration in large procedurally generated environments.

Full-paper reading should verify environment families, abstraction construction, transfer metrics, NMF rank choices, exploration protocol, and comparisons to classical SR, options, and model-based methods.

## Limits and Failure Modes

The method depends on temporal abstractions that preserve useful topology. Poor abstractions could create misleading predictive features or miss task-relevant fine details.

NMF interpretability and sparsity may depend on rank and preprocessing choices. In environments with rapidly changing dynamics rather than rewards, HSR may still become stale.

## Deep Themes

- Predictive representations with temporal abstraction: hierarchy stabilizes successor features.
- Transfer through topology: sparse components reveal reusable environment structure.
- Policy-agnostic maps: HSR bridges model-free value reuse and model-based flexibility.
- Exploration from predictive structure: temporally extended SRs can guide discovery, not only transfer.

## Subthemes

- Classical SR's policy dependence limits robustness.
- Spectral diffusion causes dense overlapping features.
- NMF extracts sparse low-rank state factors.
- Procedural environments test scalability of learned maps.

## Connections to Other Papers

HSR connects to SOL, JoSE, ScaleMoE, and DAWN in the RL representation/control cluster. SOL scales options for long-horizon training; HSR uses hierarchy to stabilize predictive representations.

It also relates to grammar substructure and latent distribution matching: all decompose complex behavior into reusable latent structure.

## Notes for Cross-Paper Synthesis

The synthesis point is that transfer depends on representations that outlive a policy. Hierarchy can make predictive structure less brittle when rewards or tasks change.
