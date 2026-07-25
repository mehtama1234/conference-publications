# Efficient numeracy in language models through single-token number embeddings

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: Bh4Ubk80M8
- Authors: Linus Kreitner; Paul Hager; Jonathan Mengedoht; Georgios Kaissis; Daniel Rueckert; Martin J. Menten
- Primary area: deep_learning->large_language_models
- Keywords: language model;LLM;arithmetic;numeracy;benchmark;single-token number embedding;tokenization;math
- Source URL: https://openreview.net/forum?id=Bh4Ubk80M8
- PDF URL: https://openreview.net/pdf?id=Bh4Ubk80M8

## Abstract

To drive progress in science and engineering, large language models (LLMs) must be able to process large amounts of numerical data and solve long calculations efficiently. This is currently only possible through the use of external tools or extensive reasoning chains, either weakening the numerical representations of LLMs or limiting the length of problems they can solve. We show that frontier LLMs require excessive amounts of reasoning tokens to solve even basic calculations, which is exacerbated by their tokenization strategies that split single numbers into multiple tokens. This motivates the need for efficient and effective single-token number encodings. We introduce a set of desiderata for such encodings and show that existing approaches fail to fulfill them. To address these shortcomings, we propose BitTokens, a novel encoding strategy that represents any number as a single token using its IEEE 754 binary floating-point representation. Through extensive experiments we show that our BitTokens allow even small language models to learn algorithms that solve basic arithmetic operations nearly perfectly. This newly gained efficiency could expand the length and complexity of problems language models can solve.

## One-Sentence Claim

BitTokens encode any number as a single token using IEEE 754 floating-point bits, enabling small language models to learn arithmetic algorithms more efficiently.

## Problem

LLMs waste many reasoning tokens on basic calculations, and conventional tokenizers split numbers into multiple tokens, weakening numerical representations and limiting long calculations.

## Core Contribution

The paper defines desiderata for single-token number encodings and proposes BitTokens as an efficient numerical representation for language models.

## Method

BitTokens represent numbers directly through their IEEE 754 binary floating-point representation as single-token embeddings, aligning model input structure with machine-number semantics.

## Experiments and Evidence

The abstract reports that BitTokens let even small language models learn basic arithmetic operations nearly perfectly across extensive experiments.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: supported numeric ranges, precision handling, tokenizer integration, non-arithmetic reasoning transfer, and behavior on natural-language numerals.

## Deep Themes

- Tokenization can be a bottleneck for reasoning capability.
- Numeric representations should respect computational structure, not just text frequency.
- Efficient numeracy may expand solvable problem length without external tools.

## Subthemes

- LLM numeracy.
- Number tokenization.
- IEEE 754 embeddings.
- Arithmetic algorithms.
- Single-token encoding.
- Reasoning efficiency.

## Connections to Other Papers

Connects to floating-point neural-network theory, efficient inference, and long-context reasoning papers through representation choices that affect computational capability.

## Notes for Cross-Paper Synthesis

BitTokens adds a tokenization-as-capability theme: the basic unit of language-model input can determine whether numerical algorithms are easy or wasteful.
