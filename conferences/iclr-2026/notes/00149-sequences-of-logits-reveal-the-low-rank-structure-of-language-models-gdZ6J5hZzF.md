# Sequences of Logits Reveal the Low Rank Structure of Language Models

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: gdZ6J5hZzF
- Authors: Noah Golowich; Allen Liu; Abhishek Shetty
- Primary area: learning theory
- Keywords: Large language models;low-rank structure
- Source URL: https://openreview.net/forum?id=gdZ6J5hZzF
- PDF URL: https://openreview.net/pdf?id=gdZ6J5hZzF

## Abstract

A major problem in the study of large language models  is to understand their inherent low-dimensional structure.  We introduce an approach to study the low-dimensional structure of language models at a model-agnostic level: as sequential probabilistic models. We first empirically demonstrate that a wide range of modern language models exhibit low-rank structure: in particular, matrices built from the model's logits for varying sets of prompts and responses have low approximate rank. We then show that this low-rank structure can be leveraged for generation --- in particular, we can generate a response to a target prompt using a linear combination of the model's outputs on unrelated, or even nonsensical prompts.

On the theoretical front, we observe that studying the approximate rank of language models in the sense discussed above yields a simple universal abstraction whose theoretical predictions parallel our experiments. We then analyze the representation power of the abstraction and give provable learning guarantees.

## One-Sentence Claim

This paper shows that matrices built from language-model logits across prompts and responses have low approximate rank, and that this structure can be used for generation.

## Problem

Understanding the low-dimensional structure of LLMs is difficult because most analyses are architecture-specific or tied to internal weights.

A model-agnostic view is needed that treats language models as sequential probabilistic systems through their observable outputs.

## Core Contribution

The paper introduces a logit-sequence approach to studying low-rank structure in language models.

It empirically demonstrates low approximate rank across modern LMs and develops a theoretical abstraction whose predictions match experiments, including learning guarantees.

## Method

The method constructs matrices from model logits evaluated over varying prompts and responses.

Low-rank structure is then analyzed empirically and theoretically. The authors show generation for a target prompt can be formed from linear combinations of model outputs on unrelated or nonsensical prompts.

## Experiments and Evidence

The abstract reports broad empirical evidence across modern language models.

It also demonstrates a generation application exploiting the low-rank logit structure and provides theoretical representation-power and learning-guarantee results.

## Limits and Failure Modes

Low-rank structure may depend on prompt/response sampling, tokenizer, logit normalization, and model family. Generation from unrelated prompts may be fragile or limited to specific regimes.

Because this note is abstract-only, details still need checking: matrix construction, rank metrics, model set, generation algorithm, theoretical assumptions, and task quality evaluation.

## Deep Themes

- Output-level model geometry: low-dimensional structure can be found in observable logits, not only hidden states.
- Model-agnostic abstraction: sequential probabilistic behavior becomes the object of theory.
- Linear combination generation: model outputs can be recombined in surprising ways.
- Low-rank capability structure: LLM behavior may live on a much smaller manifold than vocabulary dimension suggests.

## Subthemes

- Logit matrices.
- Low approximate rank.
- Sequential probabilistic models.
- Linear-combination generation.

## Connections to Other Papers

This connects to LLM DNA, scaling-law spectra, latent vector fields, and representation-geometry papers.

It also relates to Reasoning with Sampling because both exploit latent structure in base model outputs at inference time.

## Notes for Cross-Paper Synthesis

This paper adds a behavioral low-rank theme: observable model outputs can reveal compressed structure useful for theory and generation.
