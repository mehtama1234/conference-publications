# How Many Different Outputs Can a Transformer Generate?

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: x4xOtzoYa6
- Authors: Maxime Meyer; Mario Michelessa; Caroline Chaux; Vincent Y. F. Tan
- Primary area: theory->deep_learning
- Keywords: transformers;expressivity;accessible sequences;copying;cramming;scaling;long context
- Source URL: https://openreview.net/forum?id=x4xOtzoYa6
- PDF URL: https://openreview.net/pdf?id=x4xOtzoYa6

## Abstract

We study how we can leverage only a handful of characteristics of a transformer's architecture to closely predict the number of different sequences it can output, both qualitatively and quantitatively.
  We provide an upper bound depending on the length of the prompt, which we show empirically to be tight up to a factor less than 10, across architectures and model sizes.
  Our analysis also provides a theoretical explanation for previously observed empirical failures of transformers on simple sequence tasks—such as copying and cramming.
  Formally, we prove that (i) the maximal length of accessible sequences (those that the transformer can output for some prompt) grows linearly with the prompt length, (ii) beyond a critical threshold, the proportion of accessible sequences decays exponentially with sequence length, and (iii) the linear coefficient relating prompt length to accessible sequence length admits a theoretical upper bound.
  Notably, these results hold even with unbounded context and computation time.

## One-Sentence Claim

Transformer architectures impose quantifiable limits on how many sequences are accessible from prompts, with accessible length scaling only linearly in prompt length and accessibility decaying exponentially past a threshold.

## Problem

Transformers are often treated as universal sequence generators when given long context and enough compute, but architecture may restrict which output sequences can actually be produced from any prompt.

The problem is to predict expressive capacity from a small set of architectural characteristics and to explain failures on simple sequence tasks such as copying and cramming.

## Core Contribution

The paper derives upper bounds on the number and length of accessible sequences a transformer can output, and shows empirically that the bounds are tight within a small factor across architectures and sizes.

It also gives a theoretical explanation for empirical failures on simple sequence tasks, linking those failures to accessible-sequence constraints rather than only optimization or data limitations.

## Method

The analysis defines accessible sequences as sequences that the transformer can output for some prompt. It then relates the size and length of that accessible set to prompt length and architecture-level properties.

The formal results prove linear growth of maximal accessible sequence length with prompt length, exponential decay in accessible-sequence proportion beyond a critical threshold, and an upper bound on the linear coefficient.

## Experiments and Evidence

The abstract reports that the theoretical upper bound is empirically tight up to a factor below 10 across architectures and model sizes.

The results hold even under unbounded context and computation time, suggesting the limitation is structural rather than a finite-window or search-budget artifact.

## Limits and Failure Modes

The abstract does not specify which architectural characteristics drive the bounds or how decoding choices affect accessibility.

Because this note is abstract-only, details still need checking: transformer variants, tokenizer assumptions, decoding rules, prompt construction, empirical measurement method, and whether stochastic decoding changes the accessible-sequence notion.

## Deep Themes

- Expressivity as output accessibility: generation capacity is constrained by which sequences can be reached from prompts.
- Prompt length as capacity budget: longer prompts expand accessible outputs only linearly.
- Architecture-level failure explanation: copying and cramming limits can be structural.
- Scaling limits under unbounded compute: more decoding time cannot erase all representational constraints.

## Subthemes

- Accessible sequence counting.
- Exponential decay beyond critical length.
- Copying and cramming failures.
- Tight theory-to-empirics correspondence.

## Connections to Other Papers

This connects to Rational Transductors, language generation complexity barriers, and reasoning dimensionality through theoretical limits on what sequence models can represent or generate.

It also relates to insertion-based generation and any-order GPT because alternative generation orders may change the effective accessibility landscape.

## Notes for Cross-Paper Synthesis

This paper adds a hard-capacity version of the mechanism-aware theme: even if a model appears open-ended, architecture constrains the set of behaviors that prompting can access.
