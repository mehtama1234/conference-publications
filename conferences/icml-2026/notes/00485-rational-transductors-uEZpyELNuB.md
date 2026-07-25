# Rational Transductors

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: uEZpyELNuB
- Authors: Mehryar Mohri
- Primary area: theory->learning_theory
- Keywords: learning theory;automata theory;formal language theory;spectral methods;expressivity;Recurrent Neural Networks;transformers;architecture.
- Source URL: https://openreview.net/forum?id=uEZpyELNuB
- PDF URL: https://openreview.net/pdf?id=uEZpyELNuB

## Abstract

Standard Transformers excel at semantic modeling but struggle with rigid
  sequential logic and state tracking.  Theoretical work establishes that
  self-attention is limited to $\mathsf{AC}^0$ (under hard attention) or $\mathsf{TC}^0$ (under
  soft attention), complexity classes that often fail to support robust length
  generalization on sequential problems without intermediate chain-of-thought
  (see hahn2020theoretical and merrill2022saturated).  In this work, we introduce
  \emph{Rational Transductors}, a dual-stream architecture that augments the
  Transformer with a matrix-valued recurrence derived from Weighted Finite
  Automata (WFA).  By injecting rational state information into the attention
  mechanism via a *Deep Rational Injection* scheme, our framework strictly
  generalizes Transformers to capture all Regular Languages, $\mathsf{NC}^1$-complete
  problems (such as Boolean Formula Evaluation), and fundamental separations
  like Parity and Modular Counting, while preserving $O(\log T)$ parallel
  training efficiency.  Theoretical analysis and empirical results demonstrate
  that Rational Transductors solve the "Regular Gap," enabling robust length
  generalization on algorithmic tasks where standard Transformers fail, without
  the sequential computational bottlenecks of traditional RNNs.

## One-Sentence Claim

Rational Transductors augment Transformers with weighted-finite-automata recurrence, closing the regular-language/state-tracking gap while preserving logarithmic parallel training efficiency.

## Problem

Standard Transformers excel at semantic pattern modeling but struggle with rigid sequential logic, state tracking, and length generalization. Theoretical results place hard/soft attention in limited circuit classes that fail on tasks such as parity, modular counting, and some regular languages unless aided by intermediate reasoning.

Traditional RNNs can track state sequentially, but they introduce training bottlenecks. The problem is to add robust automata-like state tracking without losing Transformer parallelism.

## Core Contribution

The paper introduces Rational Transductors, a dual-stream architecture that augments the Transformer with matrix-valued recurrence derived from Weighted Finite Automata.

Through Deep Rational Injection, rational state information enters the attention mechanism. The architecture strictly generalizes Transformers to capture all regular languages, NC1-complete problems such as Boolean Formula Evaluation, and separations like parity and modular counting, while preserving O(log T) parallel training efficiency.

## Method

Rational Transductors maintain a second stream carrying WFA-derived matrix recurrence. This stream computes rational state information over sequences and injects it into Transformer attention through a deep integration scheme.

The design aims to combine automata-theoretic expressivity with Transformer-style parallelism. It targets the Regular Gap: the inability of standard Transformers to robustly generalize on finite-state sequential logic tasks.

## Experiments and Evidence

The abstract reports theoretical expressivity results plus empirical results showing robust length generalization on algorithmic tasks where standard Transformers fail. It claims coverage of all regular languages, NC1-complete tasks, parity, and modular counting.

Full-paper reading should verify formal assumptions, hard/soft attention comparisons, training complexity proof, benchmark tasks, sequence lengths, and whether the architecture scales to natural language or code.

## Limits and Failure Modes

Automata-augmented expressivity may be most valuable for algorithmic tasks and formal languages. It may not automatically improve semantic modeling, commonsense reasoning, or open-ended generation.

The additional recurrence stream may add implementation complexity and inductive bias that helps some tasks while being unnecessary or constraining for others.

## Deep Themes

- Automata-theoretic augmentation of Transformers: explicit state machines repair sequential logic gaps.
- Expressivity with parallelism: recurrent power is added without fully sequential training.
- Length generalization as architecture property: robust extrapolation requires the right computational class.
- Formal language theory for neural design: complexity separations guide architecture construction.

## Subthemes

- WFA recurrence provides rational state information.
- Deep Rational Injection integrates recurrence into attention.
- Parity and modular counting are diagnostic separations.
- Chain-of-thought can mask but not remove architectural limits.

## Connections to Other Papers

Rational Transductors connect to grammar substructure, scaling-law origin, and reasoning-loop papers through formal-language and synthetic reasoning analysis. They also relate to CMRU as another attempt to recover recurrent state benefits under parallel or hardware constraints.

The architecture-level fix contrasts with inference-level fixes such as PoLar or LongCoT prompting: some sequential capabilities may need new computation, not just more tokens.

## Notes for Cross-Paper Synthesis

The synthesis point is that architecture still matters for reasoning. Even as LLMs scale, formal gaps in state tracking motivate hybrid designs that combine attention with automata-like recurrence.
