# BlitzRank: Principled Zero-shot Ranking Agents with Tournament Graphs

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: dc9si7lBTY
- Authors: Sheshansh Agrawal; Thien Hang Nguyen; Douwe Kiela
- Primary area: deep_learning->algorithms
- Keywords: Ranking;Algorithms;LLM Ranking;Graph Theory;Reranking;Listwise ranking;Retrieval-augmented generation;Tournament graphs;k-wise comparisons;Query complexity;Top-k selection;Preference learning;Zero-shot ranking;Information Retrieval
- Source URL: https://openreview.net/forum?id=dc9si7lBTY
- PDF URL: https://openreview.net/pdf?id=dc9si7lBTY

## Abstract

Selecting the top $m$ from $n$ items via expensive $k$-wise comparisons is central to settings ranging from LLM-based document reranking to crowdsourced evaluation and tournament design.
Existing methods either rely on heuristics that discard comparison information, or exploit it at prohibitive cost.
We introduce a *tournament graph* framework that provides a principled foundation for $k$-wise ranking.
Our key observation is that each $k$-item comparison reveals an induced tournament of ${k \choose 2}$ pairwise preferences; aggregating these into a global preference graph and computing its transitive closure yields many additional orderings without further oracle calls.
We formalize when the current top-$m$ output is *certifiably determined* and design a greedy query schedule that maximizes information gain towards identifying the top-$m$ items.
The framework also gracefully handles non-transitive preferences -- cycles induced by real-world oracles -- by collapsing them into equivalence classes that yield principled *tiered rankings*.
Applied to LLM reranking across 14 benchmarks and 5 models, BlitzRank achieves Pareto dominance over existing approaches: matching or exceeding accuracy while requiring 25--40\% fewer tokens than comparable methods; against pairwise reranking, it achieves near-identical quality with 7$\times$ fewer tokens. Code available at
[https://github.com/ContextualAI/BlitzRank](https://github.com/ContextualAI/BlitzRank).

## One-Sentence Claim

BlitzRank turns expensive k-wise ranking comparisons into tournament graphs, extracting transitive closure and certifiable top-m rankings with fewer LLM tokens.

## Problem

Selecting top items via expensive k-wise comparisons appears in LLM reranking, crowdsourced evaluation, and tournament design. Existing approaches either discard comparison information or exploit it at prohibitive query cost.

The paper asks how to use all preference information exposed by k-wise comparisons while minimizing oracle/token cost.

## Core Contribution

The paper introduces a tournament-graph framework for k-wise ranking. Each k-item comparison reveals an induced tournament of k choose 2 pairwise preferences. Aggregating these into a global preference graph and computing transitive closure yields additional implied orderings without more oracle calls.

The framework formalizes when the current top-m output is certifiably determined and uses a greedy query schedule to maximize information gain. It handles non-transitive cycles by collapsing them into equivalence classes for tiered rankings.

## Method

BlitzRank converts k-wise comparison outputs into directed preference edges. It repeatedly updates the tournament graph, takes transitive closure, checks whether the top-m is determined, and queries new item sets that maximize expected information gain toward resolving uncertainty.

For cyclic or non-transitive preferences, strongly connected components become tiers rather than forcing an arbitrary total order.

## Experiments and Evidence

Evidence reported in the abstract:

- Tournament-graph foundation for k-wise ranking.
- Certifiable top-m determination.
- Greedy information-gain query schedule.
- Tiered rankings under non-transitive preferences.
- LLM reranking across 14 benchmarks and 5 models.
- 25-40 percent fewer tokens than comparable methods at matching or better accuracy.
- Near-identical quality to pairwise reranking with 7x fewer tokens.
- Code release.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: query schedule formula, benchmark list, comparison prompts, and handling noisy LLM preferences.

## Limits and Failure Modes

- Transitive closure can amplify wrong preference edges if comparisons are noisy.
- Non-transitive tiers may be less useful when a strict ranking is required.
- Query efficiency depends on k, m, and item-score separability.
- LLM reranking results may vary with prompt and base model.

## Deep Themes

**Comparison outputs contain hidden graph structure.** A k-wise decision reveals many pairwise edges.

**Certifiability can stop expensive inference.** The algorithm queries only until top-m is determined.

**Ranking agents need graph-theoretic memory.** Tournament closure accumulates preference information across calls.

## Subthemes

- Tournament graph ranking.
- k-wise comparison efficiency.
- Top-m certification.
- Transitive closure of preferences.
- Token-efficient LLM reranking.

## Connections to Other Papers

Connects to ME Ensemble, NAD, TG-RAG, and test-time compute papers through efficient inference control. It also links to finite-test certification because both ask when partial observations determine a broader claim.

## Notes for Cross-Paper Synthesis

BlitzRank closes this block with another evidence-efficiency pattern: expensive oracle calls should produce persistent structure that can be reused until the desired decision is certified.
