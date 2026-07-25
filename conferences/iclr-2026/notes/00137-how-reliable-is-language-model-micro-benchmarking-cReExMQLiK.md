# How Reliable is Language Model Micro-Benchmarking?

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: cReExMQLiK
- Authors: Gregory Yauney; Shahzaib Saqib Warraich; Swabha Swayamdipta
- Primary area: foundation or frontier models, including LLMs
- Keywords: efficient evaluation;meta-evaluation;language models
- Source URL: https://openreview.net/forum?id=cReExMQLiK
- PDF URL: https://openreview.net/pdf?id=cReExMQLiK

## Abstract

Micro-benchmarking offers a solution to the often prohibitive time and cost of language model development: evaluate on a very small subset of existing benchmarks. Can these micro-benchmarks, however,  rank models as consistently as the full benchmarks they replace? And can they rank models more consistently than selecting a random subset of data points? In many scenarios, we find that the answer is no. We introduce a meta-evaluation measure for micro-benchmarking which investigates how well a micro-benchmark can rank two models as a function of their performance difference on the full benchmark. This approach can determine which model pairs can be ranked correctly by a micro-benchmark, allowing for a finer-grained analysis of the trade-off between micro-benchmark size and reliability.
Prior work has suggested selecting as few as 10 examples; we find that no micro-benchmarking method can consistently rank model pairs 3.5 points of accuracy apart on MMLU-Pro or 4 points apart on BIG-bench Hard. In order to consistently rank model pairs with relatively similar performances, we show that often as many as 250 examples must be selected, at which point random sampling is competitive with existing micro-benchmarking methods. When comparing only 8B instruction-tuned models on MMLU-Pro micro-benchmarks with 25 examples, we find that more than half of pairwise comparisons are not likely to be preserved. Our work provides actionable guidance for both micro-benchmark users and developers in navigating the trade-off between evaluation efficiency and reliability.

## One-Sentence Claim

This paper shows many language-model micro-benchmarks are unreliable for ranking similar models and proposes a pairwise meta-evaluation measure for ranking preservation.

## Problem

Micro-benchmarks promise cheaper model evaluation by using tiny subsets of larger benchmarks.

The key risk is ranking instability: small subsets may not preserve the model order of the full benchmark, especially when models are close in performance.

## Core Contribution

The paper introduces a meta-evaluation measure that assesses how well a micro-benchmark ranks two models as a function of their full-benchmark performance gap.

This enables finer analysis of the tradeoff between benchmark size and ranking reliability.

## Method

The study compares micro-benchmark selections against full-benchmark rankings and random subsets.

It estimates which model pairs are likely to be ranked correctly for a given micro-benchmark size and full-benchmark accuracy difference.

## Experiments and Evidence

The abstract reports that in many settings, micro-benchmarks do not consistently rank models better than random subsets.

No method reliably ranks model pairs 3.5 points apart on MMLU-Pro or 4 points apart on BIG-bench Hard. Around 250 examples may be required for close pairs, and 25-example MMLU-Pro micro-benchmarks fail to preserve more than half of pairwise comparisons among 8B instruction-tuned models.

## Limits and Failure Modes

Reliability thresholds may differ for non-accuracy metrics, generative grading, safety benchmarks, or highly heterogeneous task suites.

Because this note is abstract-only, details still need checking: micro-benchmark selection methods, statistical confidence criteria, model pools, benchmarks, and pairwise preservation estimator.

## Deep Themes

- Evaluation efficiency versus ranking reliability: cheaper tests can mislead model selection.
- Pairwise ranking preservation: benchmark utility depends on which comparisons users need to make.
- Random subsets as strong baseline: complex item selection may not beat simple sampling at sufficient size.
- Meta-evaluation for benchmarks: benchmark subsets should themselves be evaluated as measurement instruments.

## Subthemes

- Micro-benchmarking.
- Model ranking.
- MMLU-Pro.
- BIG-bench Hard.

## Connections to Other Papers

This connects to Train-before-Test, AstaBench, SimuHome, OpenApps, TabStruct, and benchmark reliability work.

It also relates to LLM DNA because both question whether narrow evaluation views capture stable model relationships.

## Notes for Cross-Paper Synthesis

This paper adds a measurement-validity theme: fast evaluation is valuable only when it preserves the decisions users actually make from rankings.
