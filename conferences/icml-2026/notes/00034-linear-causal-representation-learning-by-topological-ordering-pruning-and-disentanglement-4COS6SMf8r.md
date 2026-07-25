# Linear Causal Representation Learning by Topological Ordering, Pruning, and Disentanglement

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 4COS6SMf8r
- Authors: Hao Chen; Lin Liu; Yu Guang Wang
- Primary area: general_machine_learning->causality
- Keywords: causal representation learning;causal discovery;latent variable models;causal graphical models
- Source URL: https://openreview.net/forum?id=4COS6SMf8r
- PDF URL: https://openreview.net/pdf?id=4COS6SMf8r

## Abstract

Causal representation learning (CRL) has garnered increasing interest from the causal inference and artificial intelligence communities due to its potential to disentangle complex data-generating mechanism into causally interpretable latent features by leveraging the heterogeneity of modern datasets. In this paper, we further contribute to the CRL literature, by focusing on the stylized linear structural causal model over latent features and assuming a linear mixing function that maps latent features to the observed data or measurements. Existing linear CRL methods often rely on stringent assumptions, such as access to single-node interventional data or restrictive distributional constraints on latent features and/or exogenous measurement noise. However, these prerequisites can be easy to violate in practice. In this work, we propose a novel linear CRL algorithm that, unlike existing methods, operates under weaker assumptions on environment heterogeneity and data-generating distributions while still recovering latent causal features up to an equivalence class. We further validate our new algorithm via synthetic experiments and an interpretability analysis of large language models, demonstrating both its superiority over competing methods in finite samples and its potential in integrating causality into understanding artificial intelligence. The source code is available at [the accompanying GitHub link](https://github.com/utulie/code_for_linear_crl_paper_creator).

## One-Sentence Claim

Linear causal representations can be recovered under weaker heterogeneity assumptions by inferring topological order, pruning causal influence, and disentangling latent features.

## Problem

Existing linear causal representation learning often assumes single-node interventions or restrictive distributions over latent features and measurement noise, which are easy to violate in heterogeneous real datasets.

## Core Contribution

The paper introduces CREATOR, a linear CRL algorithm that recovers latent causal features and mechanisms up to an equivalence class under weaker assumptions on environment heterogeneity and data-generating distributions.

## Method

The algorithm exploits variations across heterogeneous environments. It first infers topological ordering, then prunes causal influence through iterative variable elimination, and finally disentangles latent features up to the target equivalence class.

## Experiments and Evidence

The abstract reports synthetic experiments and an interpretability analysis of LLM outputs, showing better finite-sample performance than competing methods and potential for causal understanding of AI systems.

## Full-Text Upgrade

The full text situates the paper against interventional CRL methods that require hard or soft interventions on latent variables. Here, environments share a latent linear structural causal model and a linear mixing map to observed measurements, while heterogeneity in exogenous noises across environments provides identifiability leverage.

The algorithmic flow is explicit: infer a causal topological ordering, remove causal effects to expose exogenous noise structure, prune the recovered causal graph, and then refine/disentangle latent features. The authors acknowledge linearity as restrictive but argue that linear CRL can still capture interpretable high-level concepts, including in an LLM hidden-state/output interpretability setting.

## Limits and Failure Modes

Limits to watch: latent dimension is assumed known; the linear structural and linear mixing assumptions may be strong for real data; identifiability depends on sufficient environment heterogeneity; and the LLM interpretability application needs careful validation beyond synthetic recovery.

## Deep Themes

- Causal representation learning is moving toward weaker intervention assumptions.
- Environment heterogeneity can replace direct interventions as an identifiability signal.
- Causal latent features are being used as interpretability tools for AI systems.

## Subthemes

- Linear causal representation learning.
- Latent causal variables.
- Environment heterogeneity.
- Topological ordering.
- Graph pruning.
- Feature disentanglement.
- LLM interpretability.

## Connections to Other Papers

Connects to interpretability-as-intervention papers such as Base Models Know How to Reason and visual-symbolic mechanisms, but with a causal-discovery lens. It also links to missing-covariate robust optimization through explicit modeling of data-generating structure.

## Notes for Cross-Paper Synthesis

This paper adds a causal-structure theme: interpretable representations are not only clusters or concepts, but potentially latent variables with recoverable causal order.
