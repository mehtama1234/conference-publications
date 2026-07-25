# Scaling Atomistic Protein Binder Design with Generative Pretraining and Test-Time Compute

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: qmCpJtFZra
- Authors: Kieran Didi; Zuobai Zhang; Guoqing Zhou; Danny Reidenbach; Zhonglin Cao; Sooyoung Cha; Tomas Geffner; Christian Dallago; Jian Tang; Michael M. Bronstein; Martin Steinegger; Emine Kucukbenli; Arash Vahdat; Karsten Kreis
- Primary area: applications to physical sciences (physics, chemistry, biology, etc.)
- Keywords: binder design;protein design;flow matching;hallucination;inference-time scaling;generative modeling;diffusion models
- Source URL: https://openreview.net/forum?id=qmCpJtFZra
- PDF URL: https://openreview.net/pdf?id=qmCpJtFZra

## Abstract

Protein interaction modeling is central to protein design, which has been transformed by machine learning with broad applications in drug discovery and beyond. In this landscape, structure-based de novo binder design is most often cast as either conditional generative modeling or sequence optimization via structure predictors ("hallucination"). We argue that this is a false dichotomy and propose Complexa, a novel fully atomistic binder generation method unifying both paradigms. We extend recent flow-based latent protein generation architecture and leverage the domain-domain interactions of monomeric computationally predicted protein structures to construct Teddymer, a new large-scale dataset of synthetic binder-target pairs for pretraining. Combined with high-quality experimental multimers, this enables training a strong base model. We then perform inference-time optimization with this generative prior, unifying the strengths of previously distinct generative and hallucination methods. Complexa sets a new state of the art in computational binder design benchmarks: it delivers markedly higher in-silico success rates than existing generative approaches, and our novel test-time optimization strategies greatly outperform previous hallucination methods under normalized compute budgets. We further demonstrate explicit interface hydrogen bond optimization, fold class-guided binder generation, and extensions to small molecule targets and enzyme design tasks, again surpassing prior methods. Code, models and new data will be publicly released.

## One-Sentence Claim

Complexa unifies generative protein binder design and hallucination-style test-time optimization through a fully atomistic flow-based prior pretrained on synthetic and experimental binder-target pairs.

## Problem

Structure-based de novo binder design is often split between conditional generative models and sequence optimization through structure predictors. This split leaves generative methods without enough targeted optimization and hallucination methods without strong generative priors.

## Core Contribution

The paper proposes Complexa, a fully atomistic binder generation method that combines large-scale generative pretraining with inference-time optimization. It introduces Teddymer, a synthetic binder-target pretraining dataset based on domain-domain interactions from computationally predicted monomer structures.

## Method

Complexa extends a flow-based latent protein generation architecture, pretrains on Teddymer and high-quality experimental multimers, then performs test-time optimization with the generative prior. It supports interface hydrogen bond optimization, fold-class guidance, and extensions to small-molecule targets and enzyme design.

## Experiments and Evidence

The abstract reports new state-of-the-art computational binder design results, higher in-silico success rates than existing generative approaches, and test-time optimization outperforming hallucination baselines under normalized compute budgets. It also reports gains on small-molecule target and enzyme tasks.

## Limits and Failure Modes

In-silico success may not translate to wet-lab binding, specificity, expression, or stability. Synthetic Teddymer pretraining could encode biases from predicted monomer structures. Full-text review should check benchmarks, structural predictors, atomistic representation, compute normalization, experimental validation status, and failure modes for interface chemistry.

## Deep Themes

- Generative pretraining plus test-time compute for protein design.
- Fully atomistic binder generation.
- Synthetic scientific data construction.
- Unifying generation and hallucination.

## Subthemes

- Teddymer synthetic binder-target dataset.
- Flow-based latent protein generation.
- Interface hydrogen bond optimization.
- Fold-class guided binder generation.
- Extensions to enzymes and small-molecule targets.

## Connections to Other Papers

Connects to Protein Autoregressive Modeling, quotient-space diffusion, MFP/flow policies, and molecular generation papers through structured scientific generation, and to test-time scaling papers where generative priors are refined at inference.

## Notes for Cross-Paper Synthesis

Complexa is a scientific-domain version of a recurring pattern: pretrain a broad generative prior, then spend targeted test-time compute to satisfy a concrete design objective.
