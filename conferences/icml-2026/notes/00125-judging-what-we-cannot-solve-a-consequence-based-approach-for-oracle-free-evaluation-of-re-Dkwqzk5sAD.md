# Judging What We Cannot Solve: A Consequence-Based Approach for Oracle-Free Evaluation of Research-Level Math

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: Dkwqzk5sAD
- Authors: Guijin Son; Donghun Yang; Hitesh Laxmichand Patel; Hyunwoo Ko; Amit Agarwal; Sunghee Ahn; Kyong-Ha Lee; Youngjae Yu
- Primary area: general_machine_learning->evaluation
- Keywords: Oracle-Free Evaluation;LLM-Judge;Math
- Source URL: https://openreview.net/forum?id=Dkwqzk5sAD
- PDF URL: https://openreview.net/pdf?id=Dkwqzk5sAD

## Abstract

Recent progress in reasoning models suggests that generating plausible attempts for research-level mathematics may be within reach, but verification remains a bottleneck, consuming scarce expert time. We hypothesize that a meaningful solution should contain enough method-level information that, when applied to a neighborhood of related questions, it should yield better downstream performance than incorrect solutions. Building on this idea, we propose \textbf{Consequence-Based Utility}, an oracle-free evaluator that scores each candidate by testing its value as an in-context exemplar in solving related yet verifiable questions. Our approach is evaluated on an original set of research-level math problems each paired with one expert-written solution and nine LLM-generated solutions. Notably, Consequence-Based Utility consistently outperforms reward models, generative reward models, and LLM judges on ranking quality. Specifically, for GPT-OSS-120B it improves Acc@1 from 67.2 to 76.3 and AUC from 71.4 to 79.6, with similarly large AUC gains on GPT-OSS-20B (69.0 to 79.2). Furthermore, compared to LLM-Judges, it also exhibits a larger solver–evaluator gap, maintaining stronger correct–wrong separation even on instances the underlying solver often fails to solve.

## One-Sentence Claim

Consequence-Based Utility evaluates research-level math solutions without ground-truth solving by testing whether a candidate solution helps solve related verifiable problems.

## Problem

Reasoning models may produce plausible research-level math attempts, but expert verification is scarce and conventional LLM judges or reward models may not reliably rank solutions.

## Core Contribution

The paper proposes an oracle-free evaluator that scores candidate solutions by their downstream usefulness as in-context exemplars for neighborhoods of related questions.

## Method

For each candidate, CBU uses it as an exemplar when solving related but verifiable questions; useful consequences raise the candidate's score. This tests whether a solution contains method-level information that transfers beyond the original problem.

## Experiments and Evidence

The abstract reports an original research-level math set with one expert solution and nine LLM-generated solutions per problem. CBU outperforms reward models, generative reward models, and LLM judges; for GPT-OSS-120B, Acc@1 improves from 67.2 to 76.3 and AUC from 71.4 to 79.6.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: related-question generation, verifier reliability, domain scope, sensitivity to exemplar formatting, and whether wrong methods can help nearby easy questions.

## Deep Themes

- Evaluation can use consequences when direct oracle answers are unavailable.
- Research-level math solutions should transfer method-level value to related tasks.
- Oracle-free judging can be framed as downstream utility measurement.

## Subthemes

- Oracle-free evaluation.
- Research-level math.
- Consequence-based utility.
- LLM judges.
- In-context exemplars.
- Solver-evaluator gap.

## Connections to Other Papers

Connects to Benchmarking at the Edge of Comprehension, DR Tulu, post-comprehension evaluation, and critique-resilient benchmarking through evaluation beyond direct human solution checking.

## Notes for Cross-Paper Synthesis

CBU adds a consequences-as-evidence theme: when correctness is hard to certify directly, a solution's downstream effects can reveal its value.
