# Language Model Circuits Are Sparse in the Neuron Basis

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: OrviwFWcN4
- Authors: Aryaman Arora; Zhengxuan Wu; Jacob Steinhardt; Sarah Schwettmann
- Primary area: social_aspects->accountability_transparency_and_interpretability
- Keywords: language models;circuit tracing;interpretability
- Source URL: https://openreview.net/forum?id=OrviwFWcN4
- PDF URL: https://openreview.net/pdf?id=OrviwFWcN4

## Abstract

The high-level concepts that a neural network uses to perform computation need not be aligned to individual neurons (Smolensky, 1986).
Language model interpretability research has thus turned to techniques which decompose the neuron basis into more interpretable units of model computation, such as sparse autoencoders (SAEs).
However, not all neuron-based representations are uninterpretable. 
For the first time, we empirically show that **MLP neurons are as sparse a feature basis as SAEs**.
We use this finding to develop an end-to-end gradient-based attribution pipeline for circuit tracing on the MLP neuron basis, which surfaces causally effective neurons on a variety of tasks.
On a standard subject-verb agreement benchmark (Marks et al., 2025), a circuit of $\approx 10^2$ MLP neurons is enough to control model behaviour. 
On the multi-hop city-state-capital task from Lindsey et al. (2025), we find a circuit in which small sets of neurons encode specific latent reasoning steps (e.g. mapping a city to its state), and can be steered to change the model's output. 
This work thus advances automated interpretability of language models without imposing additional training costs.

## One-Sentence Claim

The paper shows MLP neurons can be as sparse a feature basis as SAEs and uses neuron-basis attribution to trace compact causal circuits in language models.

## Problem

Interpretability work often assumes neuron bases are too entangled and turns to trained sparse autoencoders, but this may overlook useful sparsity already present in MLP neurons.

## Core Contribution

The paper empirically demonstrates neuron-basis sparsity comparable to SAEs and develops an end-to-end gradient-based circuit-tracing pipeline over MLP neurons without extra training.

## Method

The pipeline attributes model behavior to causally effective MLP neurons, then validates circuits through control/steering on tasks such as subject-verb agreement and multi-hop city-state-capital reasoning.

## Experiments and Evidence

The abstract reports that roughly 100 MLP neurons can control behavior on a subject-verb agreement benchmark, and that small neuron sets encode specific latent reasoning steps in multi-hop city-state-capital tasks and can be steered to change outputs.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: model sizes, sparsity metrics, comparison to SAE features, circuit validation protocol, task breadth, and whether neuron-basis circuits remain sparse in larger LLMs.

## Deep Themes

- Native neuron bases may already expose interpretable computation.
- Circuit tracing can avoid additional representation training when neurons are sparse enough.
- Small causal neuron sets can encode multi-step reasoning subroutines.

## Subthemes

- Language-model interpretability.
- Circuit tracing.
- MLP neurons.
- Sparse autoencoders.
- Gradient attribution.
- Causal steering.

## Connections to Other Papers

Connects to SVD interpretability, FAC Synthesis, FlashTrace, and Robust Harmful Features through internal model mechanisms as intervention targets.

## Notes for Cross-Paper Synthesis

This paper adds a minimal-basis interpretability theme: before adding learned feature decompositions, it may be worth testing whether the native neuron basis already contains sparse causal structure.
