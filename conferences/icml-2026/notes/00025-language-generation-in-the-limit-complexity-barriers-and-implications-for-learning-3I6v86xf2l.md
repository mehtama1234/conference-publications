# Language Generation in the Limit: Complexity Barriers and Implications for Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 3I6v86xf2l
- Authors: Marcelo Arenas; Pablo Barcelo; Luis Cofré; Alexander Kozachinskiy
- Primary area: theory->learning_theory
- Keywords: Language generation;formal inference;generative AI
- Source URL: https://openreview.net/forum?id=3I6v86xf2l
- PDF URL: https://openreview.net/pdf?id=3I6v86xf2l

## Abstract

Kleinberg and Mullainathan showed that language generation in the limit is always possible
at the level of computability: given enough positive examples, a learner can eventually
generate data indistinguishable from a target language. However, such existence results do
not address feasibility.
We study the sample complexity of language generation in the limit for several canonical
classes of formal languages. Our results show that infeasibility already appears for
context-free and regular languages, and persists even for strict subclasses such as locally threshold
testable languages, as well as for incomparable classes such as non-erasing pattern
languages, a well-studied class in the theory of language identification.
Overall, our results establish a clear gap between the theoretical possibility of
language generation in the limit and its computational feasibility.

## One-Sentence Claim

Language generation in the limit may be computable in principle, but canonical formal-language classes expose sample-complexity barriers that make feasible learning impossible or sharply constrained.

## Problem

Prior work showed that generation in the limit is computably possible from positive examples, but computability does not answer whether a learner can do so with feasible sample complexity.

## Core Contribution

The paper studies sample complexity for language generation in the limit across canonical formal-language classes and establishes gaps between theoretical learnability and feasible learnability.

## Method

It analyzes formal-language families including context-free languages, regular languages, locally threshold testable languages, and non-erasing pattern languages, asking whether positive-example generation in the limit is sample-efficient.

## Experiments and Evidence

The abstract reports impossibility or infeasibility results that already appear for context-free and regular languages and persist for strict subclasses and incomparable pattern-language classes.

## Limits and Failure Modes

No confident local PDF/arXiv match yet, so theorem statements, exact complexity measures, distributional assumptions, and implications for neural language models still need full-text verification.

## Deep Themes

- Computability is too weak a success criterion for generative learning.
- Formal language theory can expose feasibility barriers hidden by broad existence theorems.
- Sample complexity matters even when generation is possible in the limit.

## Subthemes

- Language generation in the limit.
- Formal inference.
- Sample complexity.
- Regular and context-free languages.
- Pattern languages.
- Learnability barriers.

## Connections to Other Papers

Connects to Transformer Circuits and HATSolver as part of the algorithmic/theoretical cluster, but from the opposite direction: instead of showing what neural or transformer systems can implement, it clarifies where generation is infeasible despite formal possibility.

## Notes for Cross-Paper Synthesis

This paper adds a cautionary theory theme: asymptotic existence claims can obscure the practical sample requirements that determine whether a learning target is reachable.
