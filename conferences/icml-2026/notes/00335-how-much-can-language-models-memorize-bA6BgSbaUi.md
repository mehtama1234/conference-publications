# How much can language models memorize?

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: bA6BgSbaUi
- Authors: John Xavier Morris; Chawin Sitawarin; Chuan Guo; Narine Kokhlikyan; G. Edward Suh; Alexander M Rush; Kamalika Chaudhuri; Saeed Mahloujifar
- Primary area: general_machine_learning
- Keywords: memorization;LLMs;pretraining;double descent
- Source URL: https://openreview.net/forum?id=bA6BgSbaUi
- PDF URL: https://openreview.net/pdf?id=bA6BgSbaUi

## Abstract

We propose a new method for estimating how much a model knows about a datapoint and use it to measure the capacity of modern language models. Prior studies of language model memorization have struggled to disentangle memorization from generalization. We formally separate memorization into two components: unintended memorization, the information a model contains about a specific dataset, and generalization, the information a model contains about the true data-generation process. When we completely eliminate generalization, we can compute the total memorization, which provides an estimate of model capacity: our measurements estimate that GPT-style models have a capacity of approximately 3.6 bits per parameter. We train language models on datasets of increasing size and observe that models memorize until their capacity fills, at which point unintended memorization decreases as models begin to generalize. We train hundreds of transformer language models ranging from 500K to 1.5B parameters and produce a series of scaling laws relating model capacity and data size to membership inference.

## One-Sentence Claim

GPT-style language models have measurable memorization capacity around 3.6 bits per parameter, and unintended memorization decreases once capacity fills and models begin to generalize.

## Problem

Language-model memorization studies often conflate two quantities: information about a specific dataset and information about the true data-generating process. Without separating memorization from generalization, it is hard to estimate model capacity or privacy risk.

The paper asks how much modern language models can memorize and how capacity, data size, and membership inference relate.

## Core Contribution

The paper proposes a method for estimating how much a model knows about a datapoint. It formally separates unintended memorization from generalization. By eliminating generalization, it estimates total memorization and thereby model capacity.

Measurements across hundreds of Transformer LMs from 500K to 1.5B parameters estimate GPT-style capacity at about 3.6 bits per parameter. Training on increasing data sizes shows models memorize until capacity fills, then unintended memorization decreases as they generalize. The paper derives scaling laws relating model capacity/data size to membership inference.

## Method

The method constructs settings where generalization is eliminated or controlled, allowing dataset-specific information stored by the model to be measured. It then scales model size and dataset size to estimate bits-per-parameter capacity and link it to membership inference vulnerability.

This separates privacy-relevant memorization from useful compression of the data-generating distribution.

## Experiments and Evidence

Evidence reported in the abstract:

- New method estimating model knowledge about datapoints.
- Formal split between unintended memorization and generalization.
- Hundreds of Transformer LMs trained from 500K to 1.5B parameters.
- Estimated capacity around 3.6 bits per parameter for GPT-style models.
- Dataset-size experiments showing memorization until capacity fills.
- Scaling laws for capacity, data size, and membership inference.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: memorization estimator, synthetic data setup, architecture/training details, and membership inference definitions.

## Limits and Failure Modes

- Capacity estimates may depend on architecture, tokenizer, optimizer, and data distribution.
- Eliminating generalization may use artificial settings.
- Results up to 1.5B parameters may not extrapolate cleanly to frontier scale.
- Memorization risk also depends on decoding and extraction attacks, not only stored information.

## Deep Themes

**Memorization is not the opposite of generalization.** The paper separates dataset-specific information from process-level information.

**Capacity saturation changes privacy risk.** More data can reduce unintended memorization once the model begins generalizing.

**Bits per parameter is a governance-relevant quantity.** Model capacity links scaling, privacy, and membership inference.

## Subthemes

- Unintended memorization.
- Generalization as data-generating-process information.
- Bits-per-parameter capacity.
- Double-descent-like memorization dynamics.
- Membership inference scaling laws.

## Connections to Other Papers

Connects to PRISM, Rashomon Trust, Bayesian Truthful Valuation, and data-governance papers through privacy and information leakage. It also links to Brain Encoding Scale and compression papers because both ask what information model parameters actually carry.

## Notes for Cross-Paper Synthesis

This paper gives the corpus a quantitative privacy/capacity axis: how much information models can store determines both utility and leakage risk.
