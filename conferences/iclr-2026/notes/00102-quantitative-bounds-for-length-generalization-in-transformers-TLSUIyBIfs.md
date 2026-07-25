# Quantitative Bounds for Length Generalization in Transformers

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: TLSUIyBIfs
- Authors: Zachary Izzo; Eshaan Nichani; Jason D. Lee
- Primary area: learning theory
- Keywords: transformers;theory;length generalization
- Source URL: https://openreview.net/forum?id=TLSUIyBIfs
- PDF URL: https://openreview.net/pdf?id=TLSUIyBIfs

## Abstract

We study the problem of length generalization (LG) in transformers: the ability of a model trained on shorter sequences to maintain performance when evaluated on much longer, previously unseen inputs. Prior work by Huang et al. (2024) established that transformers eventually achieve length generalization once the training sequence length exceeds some finite threshold, but left open the question of how large it must be. In this work, we provide the first quantitative bounds on the required training length for length generalization to occur.
Motivated by previous empirical and theoretical work, we analyze LG in several distinct problem settings: $\ell_\infty$ error control vs. average error control over an input distribution, infinite-precision softmax attention vs. finite-precision attention (which reduces to an argmax) in the transformer, as well as for one- or two-layer transformers. In all scenarios, we prove that LG occurs when the internal behavior of the transformer on longer sequences can be ``simulated'' by its behavior on shorter sequences seen during training. Our bounds give qualitative estimates for the required length of training data required for a transformer to generalize, and we verify these insights empirically. These results sharpen our theoretical understanding of the mechanisms underlying extrapolation in transformers, and formalize the intuition that richer training data is required for generalization on more complex tasks.

## One-Sentence Claim

This paper gives quantitative training-length bounds for transformer length generalization by showing when long-sequence behavior can be simulated by shorter training examples.

## Problem

Length generalization asks whether a transformer trained on short sequences can maintain performance on much longer unseen inputs. Prior theory established eventual generalization past some finite threshold but did not quantify how long training sequences must be.

Without quantitative thresholds, empirical length-generalization recipes lack guidance about required data complexity.

## Core Contribution

The paper provides the first quantitative bounds on training sequence length needed for length generalization in several transformer settings.

It analyzes different error notions, attention precision regimes, and one- versus two-layer architectures.

## Method

The analysis compares length generalization under infinity-norm error versus average error over an input distribution, infinite-precision softmax attention versus finite-precision argmax-like attention, and shallow transformer depths.

The core principle is simulation: long-sequence internal behavior generalizes when it can be reproduced by behavior on shorter sequences observed during training.

## Experiments and Evidence

The abstract reports theoretical bounds and empirical verification of the qualitative insights.

The bounds estimate how training-data length requirements grow with task complexity and model/attention setting.

## Limits and Failure Modes

The theory targets simplified transformer settings and may not directly quantify large decoder-only LLMs, realistic token distributions, or learned positional encodings.

Because this note is abstract-only, details still need checking: formal task classes, constants in the bounds, attention assumptions, empirical tasks, and how simulation is defined.

## Deep Themes

- Length generalization as internal-behavior coverage: training data must cover the computations needed at longer lengths.
- Quantitative theory for extrapolation: finite thresholds become explicit bounds.
- Precision matters: softmax versus finite-precision attention changes extrapolation behavior.
- Richer data for complex tasks: generalization length depends on task structure, not sequence length alone.

## Subthemes

- Transformer theory.
- Length extrapolation.
- Internal simulation.
- Attention precision.

## Connections to Other Papers

This connects to Mamba-3, Softmax Turing, Rational Transductors, and other sequence-theory papers.

It also relates to long-context evaluation and retrieval work because model behavior over long sequences is a recurring bottleneck across the corpus.

## Notes for Cross-Paper Synthesis

This paper strengthens the long-context theory theme: extrapolation depends on whether short training data induces the right internal computations, not just on larger context windows.
