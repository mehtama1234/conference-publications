# Beyond Theorem Proving: Formulation, Framework and Benchmark for Formal Problem-Solving

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: hgMZraPlSv
- Authors: Qi Liu; Xinhao Zheng; Renqiu Xia; Xingzhi Qi; Qinxiang Cao; Junchi Yan
- Primary area: applications
- Keywords: large language model;formal verification;formal theorem proving;question answering
- Source URL: https://openreview.net/forum?id=hgMZraPlSv
- PDF URL: https://openreview.net/pdf?id=hgMZraPlSv

## Abstract

Large language models (LLMs) have achieved remarkable progress in mathematical reasoning, yet persistently suffer from hallucinations and erroneous logic. While formal theorem proving (FTP) shows promise in process-level reliability, it is limited to _verification_ (checking known propositions). This leaves constructive problem-solving (finding unknown terms that satisfy specific conditions) underexplored and disconnected from process-level verifiability.
To bridge this gap, we introduce **FPS** (_**F**ormal **P**roblem-**S**olving_), a principled framework to encompass the end-to-end problem-solving process in Lean 4. In FPS, the answer is an unknown metavariable coupled with a proof obligation, forcing it to be mathematically derived and verified. We further present **D-FPS** (_**D**eductive **FPS**_), which structures solving into forward derivation and backward verification, aligning more closely with human reasoning steps.
Three benchmarks of over 1,000 problems are constructed for evaluation: **FormalMath500**, **MiniF2F-Solving**, and **PutnamBench-Solving**. We further propose **RPE** (_**R**estricted **P**ropositional **E**quivalence_), a symbolic metric that evaluates semantic correctness beyond brittle string matching. Extensive experiments with state-of-the-art provers reveal that solving is significantly harder than proving, highlighting the ``alignment tax'' required to transition from loose validity checking to constructive, human-aligned reasoning.
Code and data are available at [https://github.com/Purewhite2019/formal_problem_solving_main](https://github.com/Purewhite2019/formal_problem_solving_main).

## One-Sentence Claim

Formal Problem-Solving extends Lean-based verification from checking known propositions to constructing unknown answers with proof obligations, revealing that solving is harder than theorem proving.

## Problem

LLMs still hallucinate and make logical errors in math reasoning. Formal theorem proving improves process reliability but mostly verifies known propositions, leaving constructive problem solving underexplored: the model must find unknown terms satisfying conditions, not just prove a given statement.

The paper asks how to formalize end-to-end mathematical problem solving so answers are both constructed and verified.

## Core Contribution

The paper introduces FPS, a Lean 4 framework where the answer is an unknown metavariable paired with a proof obligation. This forces the answer to be mathematically derived and checked.

It also introduces D-FPS, which decomposes solving into forward derivation and backward verification, plus three benchmarks: FormalMath500, MiniF2F-Solving, and PutnamBench-Solving. The RPE metric evaluates semantic correctness beyond brittle string matching.

## Method

In FPS, the system represents the desired answer as a metavariable inside Lean and requires a proof that the filled term satisfies the problem conditions. D-FPS structures the process around deriving candidate information forward and verifying the result backward.

RPE, Restricted Propositional Equivalence, provides a symbolic correctness metric for outputs that may be semantically equivalent despite surface differences.

## Experiments and Evidence

Evidence reported in the abstract:

- FPS framework in Lean 4.
- D-FPS forward-derivation/backward-verification structure.
- Three benchmarks with more than 1,000 problems: FormalMath500, MiniF2F-Solving, and PutnamBench-Solving.
- RPE semantic metric beyond string matching.
- Experiments with state-of-the-art provers show solving is significantly harder than proving.
- Code and data released at the listed GitHub URL.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: prover set, benchmark construction, Lean encodings, and RPE limitations.

## Limits and Failure Modes

- Formalization cost can be high, especially for open-ended problems.
- Lean-based benchmarks may emphasize domains that are easier to encode formally.
- RPE is still a restricted equivalence metric and may miss richer semantic equivalences.
- Constructive solving may require search strategies beyond current theorem-proving pipelines.

## Deep Themes

**Solving is more than proving.** Constructing the object is a distinct capability from verifying a proposition.

**Formal reliability requires answer obligations.** The output is not accepted unless it fills a metavariable and satisfies proof constraints.

**Benchmarks can expose alignment tax.** Moving from loose validity to constructive verified reasoning makes the task harder but more trustworthy.

## Subthemes

- Formal problem solving.
- Lean 4 metavariable answers.
- Forward derivation and backward verification.
- Semantic equivalence metrics.
- Constructive mathematical reasoning.

## Connections to Other Papers

Connects to Learning Randomized Reductions, 2-SAT Robustness, Weak-Strong Verification, Finite Test Certification, and mathematical reasoning RL papers. It shares the verification-backed solving theme.

## Notes for Cross-Paper Synthesis

FPS captures a deep transition in reasoning evaluation: systems should not merely output plausible answers or proofs, but construct objects inside a formal environment where correctness obligations are explicit.
