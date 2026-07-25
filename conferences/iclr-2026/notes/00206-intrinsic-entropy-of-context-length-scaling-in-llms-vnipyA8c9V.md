# Intrinsic Entropy of Context Length Scaling in LLMs

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: vnipyA8c9V
- Authors: Jingzhe Shi; Qinwei Ma; Hongyi Liu; Hang Zhao; Jenq-Neng Hwang; Lei Li
- Primary area: foundation or frontier models, including LLMs
- Keywords: context length;intrinsic entropy
- Source URL: https://openreview.net/forum?id=vnipyA8c9V
- PDF URL: https://openreview.net/pdf?id=vnipyA8c9V

## Abstract

There has been work discussing the impact of long context on Language Model performance: some find that long irrelevant context could harm performance, while some experimentally summarize loss reduction by relevant long context as Scaling Laws. This calls for a more thorough understanding on how long context impacts Language Modeling. In this work, we (1) propose to use Intrinsic Entropy for explaining the impact of context length on language modeling; and (2) conduct experiments on natural language and synthetic data, validating our proposed theoretical assumptions and deductions. Our theoretical framework can provide practical insights such as establishing that training dataset size dictates an optimal context length and bounds context length scaling for certain cases. We hope our work may inspire new long context Language Models, as well as future work studying Physics for Language Models.

## One-Sentence Claim

The paper argues that intrinsic entropy explains when longer context helps or hurts language modeling, and that dataset size can impose an optimal context length rather than making longer context universally better.

## Problem

Long-context scaling is empirically ambiguous: relevant context can reduce loss, irrelevant context can degrade performance, and simple scaling-law summaries do not explain why these effects differ. A theory is needed for when additional context provides real predictive information and when it adds noise, redundancy, or estimation burden.

## Core Contribution

The contribution is a theoretical framing of context-length scaling through intrinsic entropy, paired with natural-language and synthetic-data experiments that validate the paper's assumptions and deductions. The framing turns context length from a raw architectural knob into an information-theoretic quantity tied to data distribution and training-set size.

## Method

The method models the impact of context length on language modeling through intrinsic entropy: the irreducible uncertainty remaining after conditioning on available context. The paper then reasons about how increasing context changes this entropy under theoretical assumptions, and checks those deductions on both controlled synthetic sequences and natural-language data.

## Experiments and Evidence

The abstract reports experiments on natural language and synthetic data. The evidence is meant to validate the proposed theoretical assumptions and show practical implications, including that training dataset size can dictate an optimal context length and that context-length scaling can be bounded in some regimes.

## Limits and Failure Modes

This note is abstract/metadata-only. The full paper should be checked for the precise definition of intrinsic entropy, how it is estimated, whether assumptions hold for modern long-context transformers, and how sensitive the conclusions are to tokenizer, dataset mixture, retrieval relevance, and evaluation distribution. The theory may clarify average loss behavior while leaving task-specific long-context failures, positional extrapolation, and attention mechanism details partly outside scope.

## Deep Themes

- Information-theoretic explanation of long-context scaling.
- Context length as a data-distribution-dependent resource.
- Limits of monotonic scale intuition in LLMs.
- Physics-style theory for language models.

## Subthemes

- Intrinsic entropy.
- Relevant versus irrelevant context.
- Training dataset size as a context-length constraint.
- Synthetic-data validation of scaling assumptions.
- Natural-language context scaling.

## Connections to Other Papers

Connects to Tool-Augmented SSMs through length generalization, to MotionStream through fixed-context long-horizon generation, and to T3 through the broader problem of deciding which parts of a long trajectory or context are actually informative.

## Notes for Cross-Paper Synthesis

This paper adds a useful counterweight to the corpus's test-time scaling theme: more context is only useful when it reduces intrinsic uncertainty faster than it increases estimation or distraction costs. The emerging pattern is that long-horizon capability depends on selective information structure, not just expanding the window.
