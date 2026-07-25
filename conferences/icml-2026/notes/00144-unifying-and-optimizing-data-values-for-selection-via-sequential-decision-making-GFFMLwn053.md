# Unifying and Optimizing Data Values for Selection via Sequential Decision-Making

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: GFFMLwn053
- Authors: Hongliang Chi; Qiong Wu; Zhengyi Zhou; Jonathan Light; Emily Dodwell; Yao Ma
- Primary area: general_machine_learning
- Keywords: Data Valuation;Sequential Decision-Making;Approximate Dynamic Programming
- Source URL: https://openreview.net/forum?id=GFFMLwn053
- PDF URL: https://openreview.net/pdf?id=GFFMLwn053

## Abstract

Data selection has emerged as a crucial downstream application of data valuation, yet the theoretical foundations for using data values in selection remain underexplored. We reformulate data selection as a sequential decision-making problem where the optimal selection sequence arises from dynamic programming, and data values can be understood as encodings of this optimal sequence. This framework unifies and reinterprets existing methods like Data Shapley through the lens of approximate dynamic programming, revealing them as myopic linear approximations to the sequential problem. We further analyze how selection optimality degrades with utility curvature under submodularity, explaining when and why these approximations fail. To bridge theory and practice, we propose an efficient bipartite graph-based surrogate that preserves submodular structure while enabling scalable greedy selection with provable guarantees. Experiments on classical ML benchmarks and large-scale LLM fine-tuning data selection demonstrate substantial improvements over existing methods. Code is publicly available at https://github.com/frankhlchi/SeqDataVal

## One-Sentence Claim

Data values for selection can be understood as approximations to an optimal sequential decision process, enabling better scalable data selection through dynamic programming surrogates.

## Problem

Data valuation is widely used for data selection, but the theory of how values should guide selection sequences is underdeveloped and existing methods can be myopic.

## Core Contribution

The paper reformulates data selection as sequential decision-making, reinterprets methods such as Data Shapley as approximate dynamic programming, and proposes a scalable bipartite graph surrogate.

## Method

It analyzes selection optimality degradation under submodular utility curvature and constructs a graph-based surrogate that preserves submodular structure while allowing efficient greedy selection with guarantees.

## Experiments and Evidence

The abstract reports substantial improvements over existing methods on classical ML benchmarks and large-scale LLM fine-tuning data selection.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: utility function choices, surrogate construction, LLM fine-tuning datasets, and computational cost.

## Deep Themes

- Data selection is sequential, not just pointwise scoring.
- Data values encode approximate policies over selection order.
- Submodular structure can bridge data valuation theory and scalable selection.

## Subthemes

- Data valuation.
- Data selection.
- Approximate dynamic programming.
- Data Shapley.
- Submodularity.
- LLM fine-tuning data.

## Connections to Other Papers

Connects to FAC synthesis, data valuation, data-centric LLM optimization, and sequential decision-making papers through treating data as an optimizable resource.

## Notes for Cross-Paper Synthesis

This paper adds a data-policy theme: selecting data is itself a planning problem, and scalar values are approximations to that plan.
