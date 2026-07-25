# Divide-and-Denoise: A Game-Theoretic Method for Fairly Composing Diffusion Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 9voQUicsc2
- Authors: Abhi Gupta; Polina Barabanshchikova; Vikas K Garg; Samuel Kaski; Tommi Jaakkola
- Primary area: deep_learning->generative_models_and_autoencoders
- Keywords: diffusion models;fairness;inference-time;coordination
- Source URL: https://openreview.net/forum?id=9voQUicsc2
- PDF URL: https://openreview.net/pdf?id=9voQUicsc2

## Abstract

The abundance of pre-trained diffusion models provides an opportunity for composition. Combining several models, however, runs the risk of one model dominating or models disagreeing with each other. Here, we propose Divide-and-Denoise, a method for coordinating multiple pre-trained diffusion models during sampling. Much like managing a specialized workforce, our method creates a fair but efficient division of labor across models. Central to our method is the notion of an allocation which defines the responsibility of each model to every region of the noisy sample. At every timestep, we then denoise by (i) updating the allocation by solving a fair division game, where we divide the sample into regions that maximize total utility under fairness constraints, and (ii) aligning the models with this allocation, where we guide each model to denoise within its assigned region. This leads to a new composite denoising process that evolves in tandem with a division process. We evaluate Divide-and-Denoise on conditional image generation. Across several quality metrics, including the GenEval benchmark, our method outperforms baselines and resolves common failures including missing objects and mismatched attributes. Experiments show that Divide-and-Denoise utilizes each model's expertise without neglecting any other model.

## One-Sentence Claim

Divide-and-Denoise coordinates multiple pretrained diffusion models during sampling by assigning each model fair responsibility over regions of the noisy sample.

## Problem

Composing pretrained diffusion models can cause one model to dominate or models to disagree, producing missing objects, mismatched attributes, or unfair use of specialized expertise.

## Core Contribution

The paper introduces an inference-time game-theoretic composition method that alternates between fair allocation of sample regions and model-aligned denoising.

## Method

At each denoising timestep, the method solves a fair division game to allocate noisy-sample regions to models under utility and fairness constraints, then guides each model to denoise its assigned region. The denoising process and division process evolve together.

## Experiments and Evidence

The abstract reports conditional image-generation results, including GenEval, where the method beats baselines and reduces missing-object and mismatched-attribute failures while using each model's expertise.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition is deferred after repeated rate-limit failures. Details still need checking: utility definition, fairness constraints, computational overhead, compatibility with model families, and failure cases when models strongly disagree.

## Deep Themes

- Generative model composition needs coordination, not only score averaging.
- Fair division can allocate responsibility among specialized models.
- Inference-time governance can prevent domination by one model.

## Subthemes

- Diffusion composition.
- Game-theoretic allocation.
- Fair denoising.
- Conditional image generation.
- Specialist model coordination.
- Inference-time control.

## Connections to Other Papers

Connects to ParetoPO, constrained diffusion, Rex, and multimodal/generative evaluation papers through coordinated inference and multi-objective generation.

## Notes for Cross-Paper Synthesis

Divide-and-Denoise adds a model-coordination theme: composing pretrained systems requires allocating responsibility and resolving conflicts during inference.
