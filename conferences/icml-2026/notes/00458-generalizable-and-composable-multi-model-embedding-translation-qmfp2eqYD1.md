# Generalizable and Composable Multi-Model Embedding Translation

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: qmfp2eqYD1
- Authors: Beining Yang; Yang Cao
- Primary area: general_machine_learning->representation_learning
- Keywords: embedding translation;embedding transformation;representation alignment
- Source URL: https://openreview.net/forum?id=qmfp2eqYD1
- PDF URL: https://openreview.net/pdf?id=qmfp2eqYD1

## Abstract

Embedding translation enables interoperability across embedding models, allowing embedding vectors to be reused without costly re-embedding.  However, existing methods are typically evaluated under simplified pairwise and i.i.d. settings and behave as black boxes at inference time, leading to unreliable performance under out-of-distribution (OOD) inputs, multi-model mixing, and composed translations.  We analyze embedding translation from a geometric perspective and derive an interpretable error bound that explains systematic error amplification under OOD inputs, mixing and chaining.  Building on this, we propose a geometry-aware confidence metric and a Hierarchical Mixture of Experts (HMoE) framework with localized, parameter-efficient adaptation.  Following the MTEB leaderboard, we conduct large-scale experiments over 10 embedding models and 6 datasets across 90 pairwise translation settings.  HMoE outperforms every baseline for every model pair over every dataset under OOD scenarios. Furthermore, multi-model mixing and chaining only degrade our performance in Recall@100 by $0.5\% -- 2.6\%$, compared to $7.2\% -- 92.3\%$ recall drop by existing methods.

## One-Sentence Claim

Embedding translation becomes reliable under OOD inputs, model mixing, and chained translations when guided by geometric error bounds, confidence estimates, and localized hierarchical MoE adaptation.

## Problem

Embedding ecosystems are fragmented: different models produce incompatible vector spaces, and re-embedding large corpora is expensive. Translation between embedding spaces could enable interoperability, but existing methods are often tested only in pairwise i.i.d. settings.

Real usage requires out-of-distribution robustness, mixing embeddings from multiple source models, and composing translations across model pairs. Naive black-box translators can amplify errors badly under these operations.

## Core Contribution

The paper analyzes embedding translation geometrically and derives an interpretable error bound explaining systematic amplification under OOD inputs, mixing, and chaining. It then proposes a geometry-aware confidence metric and a Hierarchical Mixture-of-Experts framework for localized, parameter-efficient adaptation.

The core contribution is to make translation composable. Rather than only fit model A to model B, the method reasons about when translations are trustworthy and how local experts can handle heterogeneous regions of embedding space.

## Method

The geometric analysis characterizes how translation errors grow when inputs move away from the training distribution, embeddings from multiple models are mixed, or translations are chained. This motivates a confidence metric tied to translation geometry.

HMoE uses hierarchical expert routing with localized parameter-efficient adaptation. Different experts can specialize to local regions or model-pair conditions, reducing the burden on one global translator.

## Experiments and Evidence

The abstract reports large-scale experiments over 10 embedding models, 6 datasets, and 90 pairwise translation settings following MTEB. HMoE outperforms every baseline for every model pair over every dataset under OOD scenarios.

For multi-model mixing and chaining, HMoE loses only 0.5-2.6 percent Recall@100, compared with 7.2-92.3 percent drops for existing methods. Full-paper reading should verify model/dataset mix, training data sizes, and confidence-calibration quality.

## Limits and Failure Modes

Translation may still fail when two embedding models encode fundamentally different semantics or task objectives. A geometric translator can align spaces only to the extent that useful information is preserved in both representations.

HMoE adds routing and calibration complexity. In production retrieval systems, small translation errors can have large ranking effects, so confidence metrics must be tied to downstream retrieval risk.

## Deep Themes

- Representation interoperability: embedding vectors become reusable assets across model families.
- Compositional alignment: translation must survive mixing and chaining, not only pairwise conversion.
- Geometry-aware confidence: reliability is estimated from representation geometry rather than hidden in black-box outputs.
- Local expert adaptation: heterogeneous embedding spaces need localized translators.

## Subthemes

- Re-embedding avoidance is an infrastructure motivation.
- OOD inputs reveal systematic translation error amplification.
- Recall@100 degradation is the key operational metric.
- HMoE applies expert specialization to representation alignment.

## Connections to Other Papers

This paper connects to FedARC, concept binding, and Fair Posthoc Control through representation alignment. FedARC aligns client embeddings; this paper aligns embedding-model spaces; concept-binding work studies when representations encode compositional structure.

It also relates to MoE scaling/compression: here MoE is used not for generation but for localized translation reliability.

## Notes for Cross-Paper Synthesis

The synthesis point is that embedding spaces are becoming infrastructure. Once embeddings are deployed as databases and APIs, translation, confidence, and composability become systems problems.
