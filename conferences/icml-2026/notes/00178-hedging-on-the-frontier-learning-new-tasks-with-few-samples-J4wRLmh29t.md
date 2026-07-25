# Hedging on the Frontier: Learning New Tasks with Few Samples

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: J4wRLmh29t
- Authors: Tobias Wegel; Federico Di Gennaro; Geelon So; Fanny Yang
- Primary area: theory->domain_adaptation_and_transfer_learning
- Keywords: Transfer Learning;Model Selection;Aggregation;Benchmarks
- Source URL: https://openreview.net/forum?id=J4wRLmh29t
- PDF URL: https://openreview.net/pdf?id=J4wRLmh29t

## Abstract

When a learner faces a new task with few samples, it must leverage any available side information. In practice, this often comes in the form of model evaluations on related tasks in public benchmarks. A key question then is how to model task relatedness such that it is both realistic and the benchmark evaluations lead to provable gains. Empirically, we observe that *weak monotonicity* is often approximately satisfied: if a model dominates another on many benchmarks, it also tends to outperform on the new task. We explore the statistical complexity of learning under (approximate) weak monotonicity, leveraging it within two learning paradigms: transfer learning and model selection aggregation. We show that not only can we prune the model class based on monotonicity, but we can also further adapt to the geometry of the available trade-offs by *hedging on the frontier*.

## One-Sentence Claim

The paper exploits approximate weak monotonicity across benchmark evaluations to prune and aggregate models for new few-sample tasks by hedging on the performance frontier.

## Problem

When learning a new task with few samples, practitioners often have public benchmark evaluations for candidate models but lack a realistic, provable way to translate related-task rankings into new-task gains.

## Core Contribution

The paper studies the statistical complexity of transfer learning and model-selection aggregation under approximate weak monotonicity, showing how benchmark dominance can prune model classes and adapt to tradeoff geometry.

## Method

The authors empirically motivate weak monotonicity, then analyze algorithms that use dominance relations across related benchmarks to reduce the candidate set and hedge among models on the frontier of available tradeoffs.

## Experiments and Evidence

The abstract reports empirical observation that weak monotonicity often approximately holds: models dominating others on many benchmarks tend to outperform them on new tasks. The main evidence claim is theoretical/statistical rather than benchmark-specific in the abstract.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: monotonicity violation tolerance, benchmark domains, sample complexity bounds, aggregation algorithms, and behavior when public benchmarks are contaminated or weakly related.

## Deep Themes

- Benchmark histories as side information for few-shot model choice.
- Transfer assumptions should be weak enough to match practice but strong enough for guarantees.
- Frontier hedging handles model tradeoffs better than choosing a single average winner.

## Subthemes

- Transfer learning.
- Model selection.
- Aggregation.
- Weak monotonicity.
- Few-sample learning.
- Benchmark geometry.

## Connections to Other Papers

Connects to Prescriptive Scaling and ATLAS through evaluation-derived decision-making, and to data/model selection papers that convert existing performance records into future-task guidance.

## Notes for Cross-Paper Synthesis

This paper adds a decision-theoretic layer to evaluation: benchmarks are not just scoreboards, but side information for selecting or aggregating models under sparse new-task data.
