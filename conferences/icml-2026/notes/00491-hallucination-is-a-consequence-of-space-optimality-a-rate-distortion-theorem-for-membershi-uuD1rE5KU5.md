# Hallucination is a Consequence of Space-Optimality: A Rate-Distortion Theorem for Membership Testing

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: uuD1rE5KU5
- Authors: Anxin Guo; Jingwei Li
- Primary area: theory->everything_else
- Keywords: Information theory;language models;rate distortion theory;hallucination;data structure;KL divergence;mutual information;membership testing;Bloom filters
- Source URL: https://openreview.net/forum?id=uuD1rE5KU5
- PDF URL: https://openreview.net/pdf?id=uuD1rE5KU5

## Abstract

Large language models often hallucinate with high confidence on "random facts" that lack inferable patterns. 
We formalize the memorization of such facts as a membership testing problem, unifying the discrete error metrics of Bloom filters with the continuous log-loss of LLMs. 
By analyzing this problem in the regime where facts are sparse in the universe of plausible claims, we establish a rate-distortion theorem: the optimal memory efficiency is characterized by the minimum KL divergence between score distributions on facts and non-facts. 
This theoretical framework provides a distinctive explanation for hallucination under an idealized setting: even with optimal training, perfect data, and a simplified ``closed world'' setting, the information-theoretically optimal strategy under limited capacity is not to abstain or forget, but to assign high confidence to some non-facts, resulting in hallucination. 
We validate this theory empirically on both synthetic and real-world data, showing that hallucinations persist as a natural consequence of lossy compression.
The same theorem recovers and sharpens classical space lower bounds for Bloom-type filters, pinning down an additive constant left open for two-sided filters.

## One-Sentence Claim

In sparse fact memorization under limited capacity, information-theoretically optimal compression can require assigning high confidence to some non-facts, making hallucination a natural rate-distortion consequence.

## Problem

LLMs often hallucinate random facts that have no inferable pattern. If such facts must be memorized rather than generalized, the question becomes how limited memory should represent a sparse set of true claims within a huge universe of plausible claims.

The paper reframes this as membership testing, connecting LLM log-loss behavior with Bloom-filter-style discrete false positives. This separates hallucination caused by poor training from hallucination caused by optimal lossy compression.

## Core Contribution

The paper establishes a rate-distortion theorem for sparse membership testing. Optimal memory efficiency is characterized by the minimum KL divergence between score distributions on facts and non-facts.

The distinctive claim is that even under perfect data, optimal training, and a closed-world idealization, a capacity-limited system should sometimes assign high confidence to non-facts rather than abstain or forget. The theorem also sharpens classical Bloom-filter lower bounds.

## Method

The framework models random fact memorization as a membership query problem over sparse positives. It unifies binary membership errors and continuous log-loss by considering score distributions for facts and non-facts.

Rate-distortion analysis characterizes the best achievable tradeoff between memory and error. KL divergence between positive and negative score distributions determines the optimal compression boundary.

## Experiments and Evidence

The abstract reports empirical validation on synthetic and real-world data, showing hallucinations persist as a consequence of lossy compression. It also states that the theorem recovers and sharpens Bloom-type space lower bounds, including an additive constant for two-sided filters.

Full-paper reading should verify closed-world assumptions, real-world fact datasets, connection from membership scores to LLM confidence, and whether model hallucinations match the predicted false-positive profile.

## Limits and Failure Modes

The idealized setting covers random facts lacking inferable patterns. Many real hallucinations arise from reasoning errors, retrieval failures, ambiguity, instruction conflict, or distribution shift, not pure membership compression.

The theorem explains why false positives can be optimal under capacity limits, but it does not imply deployed systems should accept high-confidence hallucination; abstention, retrieval, and uncertainty calibration can change the task.

## Deep Themes

- Hallucination as compression artifact: false positives can be optimal under memory constraints.
- Membership testing as fact memorization: random facts resemble sparse set storage.
- Rate-distortion for language models: log-loss connects continuous confidence to discrete truth errors.
- Capacity limits and confidence: high confidence can be a rational compression outcome, not only overconfidence pathology.

## Subthemes

- Sparse fact universes produce Bloom-filter-like tradeoffs.
- KL separation between fact and non-fact scores determines efficiency.
- Perfect training does not eliminate capacity-induced hallucination.
- Abstention is not free unless it is included in the objective.

## Connections to Other Papers

This paper connects to embedding dimensionality collapse and local redundancy through information-theoretic limits on representation capacity. It also relates to LLM annotation limits, adaptive bias, and Assistant Axis because confidence and behavior can be constrained by internal representation rather than prompt intent.

It complements retrieval-augmented and data-selection themes: external memory may be necessary when parametric storage is information-theoretically lossy.

## Notes for Cross-Paper Synthesis

The synthesis point is that some failures are optimal under the wrong resource model. If factual truth is treated as compressed parametric memory, hallucination can be a capacity-efficient false positive.
