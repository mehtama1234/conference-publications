# Transformer Circuits Can Realize Clustering Algorithms

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 2jw5U060C4
- Authors: Kenneth L. Clarkson; Lior Horesh; Takuya Ito; Charlotte Park; Parikshit Ram
- Primary area: general_machine_learning->clustering
- Keywords: transformer circuits;clustering;in-context learning
- Source URL: https://openreview.net/forum?id=2jw5U060C4
- PDF URL: https://openreview.net/pdf?id=2jw5U060C4

## Abstract

Although transformers are most commonly optimized as statistical sequence models, it is unclear to what extent they can implement and learn exact algorithmic computations. Here, we specify a transformer implementation from first principles that executes a fundamental and widely used method for $k$-means clustering: Lloyd's algorithm. We theoretically prove and empirically demonstrate that this implementation of a transformer architecture, which we term the _$k$-means transformer_, exactly implements Lloyd's algorithm for $k$-means clustering using the standard circuit mechanisms of modern transformers: attention block, residual connections, and feed-forward block. In learning experiments, we find that training this base architecture on $k$-means clustering yields a generalizable clustering algorithm that surpasses Lloyd's algorithm in terms of clustering quality. Finally, we demonstrate that interpretable alterations (e.g., inclusion of layer normalizations) to this architecture yields diverse and novel variants of clustering algorithms, including soft $k$-means, spherical $k$-means, trimmed $k$-means. Overall, our results show that transformer circuit mechanisms can instantiate exact algorithmic routines for clustering, while simultaneously providing an effective learnable model.

## One-Sentence Claim

Transformer circuits can exactly implement Lloyd's k-means algorithm, and trained variants can learn clustering algorithms that surpass classical Lloyd clustering quality.

## Problem

Transformers are usually treated as statistical sequence models, but it remains unclear how precisely their standard circuit components can implement exact algorithmic computations.

## Core Contribution

The paper specifies a first-principles transformer implementation of Lloyd's algorithm, proves and empirically demonstrates exact k-means execution, and shows interpretable architectural changes yield clustering variants.

## Method

The k-means transformer uses standard attention, residual, and feed-forward blocks to implement clustering iterations. Variants with interpretable modifications such as layer normalization produce soft, spherical, and trimmed k-means-like algorithms.

## Experiments and Evidence

The abstract reports that training the base architecture on k-means yields a generalizable clustering algorithm surpassing Lloyd's algorithm in clustering quality.

## Limits and Failure Modes

No confident local PDF/arXiv match yet. Checks needed: input assumptions, number of iterations/layers, numerical precision, scalability, and whether learned improvements preserve guarantees.

## Deep Themes

- Transformers can realize exact algorithms, not only approximate correlations.
- Interpretability can connect circuit mechanisms to classical computation.
- Learned algorithms can improve classical routines while remaining structurally understandable.

## Subthemes

- Transformer circuits.
- K-means clustering.
- Algorithmic reasoning.
- In-context learning.
- Interpretable architecture variants.

## Connections to Other Papers

Connects to Base Models Know How to Reason, HATSolver, and symbolic/algorithmic reasoning papers. It is a clean example of transformers as algorithmic substrates.

## Notes for Cross-Paper Synthesis

This paper supports a deep algorithmic theme: modern architectures can be studied as programmable computational circuits, linking ML behavior to classical algorithm design.
