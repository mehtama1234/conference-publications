# Think in Cloud, Look at Edges: Semantic-Driven Query Decomposition for Efficient Video Reasoning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 9HyDFcKhLV
- Authors: Wenhao Zou; Zhijie Cai; Minchen Yu; Zongshuai Zhang; Guangxu Zhu
- Primary area: applications->computer_vision
- Keywords: Long Video Understanding;Edge-Cloud Collaborative Inference;Video Reasoning;Keyframe Selection
- Source URL: https://openreview.net/forum?id=9HyDFcKhLV
- PDF URL: https://openreview.net/pdf?id=9HyDFcKhLV

## Abstract

Long video understanding faces a critical dilemma: cloud-based Large Multimodal Models (LMMs) offer superior reasoning but suffer from prohibitive bandwidth costs and latency, while edge-based solutions sacrifice perception accuracy for speed. Current collaborative approaches attempt to bridge this gap via similarity-based filtering, yet they treat complex queries as flat semantic vectors. We identify this as a fundamental flaw leading to "Semantic Submergence," where dominant visual features drown out subtle but logically critical cues. To solve this, we introduce SCOPE (Semantic Cloud-Orchestrated Perception at Edge). Shifting the paradigm to "Think in Cloud, Look at Edges," SCOPE utilizes a cloud LMM to decompose complex queries into a structured Directed Acyclic Graph (DAG). This "observation plan" guides the edge to retrieve evidence based on logical necessity rather than mere statistical similarity. Experiments on Video-MME and LongVideoBench demonstrate that SCOPE redefines the Pareto frontier, matching cloud-level accuracy with significantly lower transmission costs and outperforming state-of-the-art baselines on complex reasoning tasks.

## One-Sentence Claim

SCOPE uses a cloud LMM to decompose complex video queries into structured observation plans that guide edge retrieval by logical necessity rather than flat similarity.

## Problem

Long-video reasoning faces a cloud-edge tradeoff: cloud LMMs reason well but are costly and slow, while edge models are fast but less perceptive. Similarity-based filtering can miss subtle logically necessary cues.

## Core Contribution

The paper identifies Semantic Submergence and introduces Semantic Cloud-Orchestrated Perception at Edge, a cloud-edge collaborative inference framework for efficient video reasoning.

## Method

SCOPE has the cloud LMM decompose a complex query into a directed acyclic graph observation plan. The edge side retrieves evidence according to the logical structure of that plan, reducing transmitted video while preserving critical cues.

## Experiments and Evidence

The abstract reports experiments on Video-MME and LongVideoBench showing cloud-level accuracy with much lower transmission costs and stronger performance than state-of-the-art baselines on complex reasoning tasks.

## Limits and Failure Modes

ArXiv search failed with HTTP 429 for this batch, so this note is abstract-only. Details still need checking: DAG construction reliability, edge model assumptions, bandwidth accounting, latency breakdown, and robustness to decomposer errors.

## Deep Themes

- Efficient perception can be orchestrated by semantic task structure.
- Edge-cloud systems need logical query decomposition, not just embedding similarity.
- Long-video reasoning exposes subtle evidence-selection failures.

## Subthemes

- Long video understanding.
- Edge-cloud inference.
- Semantic query decomposition.
- Observation plans.
- Keyframe/evidence selection.
- Bandwidth-latency tradeoffs.

## Connections to Other Papers

Connects to OmniFit, TACO, EcoVLA, and Think-in-Flow through efficient inference under long-context or streaming constraints. It also links to agent-planning papers through DAG-structured decomposition.

## Notes for Cross-Paper Synthesis

SCOPE adds a semantic-compression theme: the system compresses video by preserving logically necessary evidence rather than nearest-neighbor visual similarity.
