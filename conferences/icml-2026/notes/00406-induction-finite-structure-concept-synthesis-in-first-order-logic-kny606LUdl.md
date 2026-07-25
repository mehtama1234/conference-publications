# INDUCTION: Finite-Structure Concept Synthesis in First-Order Logic

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: kny606LUdl
- Authors: Serafim Batzoglou
- Primary area: deep_learning->large_language_models
- Keywords: first-order logic;concept learning;inductive logic programming;large language models;benchmark;symbolic reasoning;knowledge representation
- Source URL: https://openreview.net/forum?id=kny606LUdl
- PDF URL: https://openreview.net/pdf?id=kny606LUdl

## Abstract

Induction is the search for a general rule that explains observations. We study logical induction in finite relational worlds: each problem gives small structures over a fixed vocabulary, labels objects belonging to an unknown unary concept, and asks for one first-order formula φ(x) that accounts for those labels across worlds. Finite domains make formulas mechanically checkable by exact evaluation and SMT. We introduce INDUCTION, a benchmark for finite-structure concept synthesis with three regimes: FULLOBS (full observation), where all facts are observed; CI (contrastive induction), where YES/NO worlds require discriminative hypotheses; and EC (existential completion), where validity is defined by world-local completion of unknown facts. We evaluate frontier language models, include symbolic synthesis baselines, and score both validity and formula size. Prompted models show real but incomplete capability, with sharp difficulty gradients and hard structural families. Held-out evaluation shows that compact formulas generalize far better than bloated ones; parsimony separates concept recovery from finite-world fit.

## One-Sentence Claim

INDUCTION benchmarks whether models can synthesize compact first-order formulas that explain labeled objects across finite relational worlds.

## Problem

Induction requires finding a general rule from observations, but language-model reasoning benchmarks often blur rule synthesis, pattern matching, and finite-instance fitting. First-order logic over finite structures provides a setting where hypotheses can be mechanically checked.

The paper asks whether frontier models can recover compact symbolic concepts rather than overfit finite worlds with bloated formulas.

## Core Contribution

The contribution is INDUCTION, a benchmark for finite-structure concept synthesis. Each problem gives small relational structures, object labels for an unknown unary concept, and asks for one first-order formula that accounts for labels across worlds.

It defines three regimes: FULLOBS with complete facts, CI with contrastive YES/NO worlds, and EC with existential completion of unknown facts. Models are scored on validity and formula size.

## Method

Candidate formulas are evaluated exactly on finite domains and through SMT, allowing mechanical validity checks. The benchmark compares prompted language models with symbolic synthesis baselines.

Held-out evaluation distinguishes compact formulas that generalize from large formulas that merely fit the observed finite structures.

## Experiments and Evidence

Evidence reported in the abstract:

- Three benchmark regimes: FULLOBS, CI, and EC.
- Exact evaluation and SMT-based checking.
- Frontier language model evaluation.
- Symbolic synthesis baselines.
- Metrics for validity and formula size.
- Prompted models show real but incomplete capability.
- Sharp difficulty gradients and hard structural families.
- Compact formulas generalize better than bloated ones.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: benchmark size, model set, symbolic baselines, and SMT encoding.

## Limits and Failure Modes

- Finite relational worlds may not capture all natural-language induction.
- Formula-size penalties depend on the chosen logical language and normal form.
- Prompted models may be sensitive to serialization of structures.
- SMT-checkable validity helps evaluation but does not explain model search strategy.

## Deep Themes

**Parsimony separates rule learning from fitting.** Compact formulas generalize better than bloated explanations.

**Symbolic hypotheses can be mechanically checked.** Finite structures make concept synthesis verifiable.

**Induction needs structural benchmarks.** The task isolates logical rule synthesis rather than final-answer accuracy.

## Subthemes

- First-order concept synthesis.
- Finite relational structures.
- Contrastive induction.
- Existential completion.
- Formula-size generalization.

## Connections to Other Papers

Connects to Formal Problem-Solving, 2-SAT Robustness, Learning Randomized Reductions, Finite Test Certification, and Identity Bridge. It extends the formal reasoning/evaluation cluster from proof checking to inductive rule synthesis.

## Notes for Cross-Paper Synthesis

INDUCTION adds a parsimony-centered evaluation theme: reliable symbolic reasoning is not just validity on seen cases but compact structure that transfers.
