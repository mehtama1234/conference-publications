# Train-before-Test Harmonizes Language Model Rankings

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: ORv3SAzus1
- Authors: Guanhua Zhang; Ricardo Dominguez-Olmedo; Moritz Hardt
- Primary area: foundation or frontier models, including LLMs
- Keywords: Evaluation;Large language model
- Source URL: https://openreview.net/forum?id=ORv3SAzus1
- PDF URL: https://openreview.net/pdf?id=ORv3SAzus1

## Abstract

Existing language model benchmarks provide contradictory model rankings, even for benchmarks that aim to capture similar skills. This dilemma of conflicting rankings hampers model selection, clouds model comparisons, and adds confusion to a growing ecosystem of competing models. In this paper, we take a different perspective on model comparison: instead of relying on out-of-the-box performance via direct evaluation, we compare model potential by providing each model with identical benchmark-specific fine-tuning before evaluation. We call this approach train-before-test. Our primary contribution is a comprehensive empirical evaluation of model potential across 24 benchmarks and 61 models. First, we demonstrate that model potential rankings obtained through train-before-test exhibit remarkable consistency across all benchmarks. Whereas traditional rankings demonstrate little external validity under direct evaluation, they enjoy a significant degree of external validity when applying train-before-test: model potential rankings transfer gracefully from one benchmark to another. Second, train-before-test restores the connection between perplexity and downstream task performance, lost under direct evaluation. Remarkably, even pre-finetuning perplexity of a base model predicts post-finetuning downstream performance, suggesting that ranking consistency reflects inherent model potential rather than fine-tuning artifacts. Finally, train-before-test reduces the model-score matrix to essentially rank one, indicating that model potential is dominated by one latent factor, uncovered by train-before-test. While direct evaluation remains useful for assessing deployment-ready performance, train-before-test provides a complementary lens for understanding achievable performance of models after adaptation.

## One-Sentence Claim

Train-before-test compares language models by their post-adaptation potential and produces more consistent, transferable rankings than direct benchmark evaluation.

## Problem

LLM benchmarks often give contradictory rankings, even when they target similar skills. This makes model selection and scientific comparison noisy.

Direct evaluation measures deployment-ready behavior, but it can conflate pretraining quality with instruction tuning, prompting sensitivity, format familiarity, and benchmark-specific quirks.

## Core Contribution

The paper proposes train-before-test: fine-tune every model on identical benchmark-specific training data before evaluating it.

The approach reframes comparison around model potential after adaptation, not only out-of-the-box benchmark performance.

## Method

The study applies benchmark-specific fine-tuning to each model under controlled conditions, then evaluates downstream performance.

It compares the external validity of rankings across 24 benchmarks and 61 models, and analyzes the relationship between perplexity and downstream results before and after adaptation.

## Experiments and Evidence

The abstract reports that train-before-test rankings are remarkably consistent across benchmarks, while direct-evaluation rankings show little external validity.

It also restores the link between perplexity and downstream performance. Pre-finetuning base-model perplexity predicts post-finetuning performance, and the model-score matrix becomes approximately rank one, suggesting a dominant latent factor of model potential.

## Limits and Failure Modes

Train-before-test is complementary to direct evaluation, not a replacement. It may understate deployment differences due to alignment, tool use, latency, safety, or instruction-following polish.

Because this note is abstract-only, details still need checking: fine-tuning budgets, data sizes, model families, benchmark tasks, rank-one analysis, and whether adaptation protocols are realistic for users.

## Deep Themes

- Model potential versus deployment readiness: evaluation should distinguish what a model can learn from what it does zero-shot.
- Ranking external validity: good benchmarks should predict performance across related tasks.
- Perplexity rehabilitation: adaptation can reveal relationships hidden by direct prompting.
- Latent-factor model comparison: broad model quality may collapse to one dominant potential axis under controlled adaptation.

## Subthemes

- Benchmark ranking consistency.
- Benchmark-specific fine-tuning.
- External validity.
- Rank-one model-score structure.

## Connections to Other Papers

This connects to AstaBench, MC-Search, SimuHome, and WebDevJudge through benchmark-design concerns.

It also relates to LongWriter-Zero and AgentFlow because both demonstrate that training procedure changes observed capability.

## Notes for Cross-Paper Synthesis

Train-before-test adds a measurement theme: rankings can be unstable not because models lack an ordering, but because direct benchmarks observe a noisy slice of adaptable potential.
