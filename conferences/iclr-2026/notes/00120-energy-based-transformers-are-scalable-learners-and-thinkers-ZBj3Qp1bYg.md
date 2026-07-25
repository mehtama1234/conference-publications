# Energy-Based Transformers are Scalable Learners and Thinkers

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: ZBj3Qp1bYg
- Authors: Alexi Gladstone; Ganesh Nanduru; Md Mofijul Islam; Peixuan Han; Hyeonjeong Ha; Aman Chadha; Yilun Du; Heng Ji; Jundong Li; Tariq Iqbal
- Primary area: generative models
- Keywords: Energy-Based Models;System 2 Thinking;Reasoning;Verification;Scaling;Transformers;Generative Modeling
- Source URL: https://openreview.net/forum?id=ZBj3Qp1bYg
- PDF URL: https://openreview.net/pdf?id=ZBj3Qp1bYg

## Abstract

Inference-time computation, analogous to human System 2 Thinking, has recently become popular for improving model performance. However, most existing approaches suffer from several limitations: they are modality-specific (e.g., working only in text), problem-specific (e.g., verifiable domains like math and coding), or require additional supervision/training on top of unsupervised pretraining (e.g., verifiers or verifiable rewards). In this paper, we ask the question “Is it possible to generalize these System 2 Thinking approaches, and develop models that learn to think solely from unsupervised learning?” We find the answer is yes, by learning to explicitly verify the compatibility between inputs and candidate-predictions, and then re-framing prediction problems as optimization with respect to this verifier. Specifically, we train Energy-Based Transformers (EBTs)---a new class of Energy-Based Models (EBMs)---to assign an energy value to every input and candidate-prediction, enabling predictions through energy minimization until convergence. To support this approach, we introduce several key techniques for stable and parallelizable training, which enable the emergence of strong System 2 Thinking capabilities and scalable EBMs. Across discrete and continuous modalities, we find EBTs outperform the Transformer++ approach, scaling up to 35% faster during pretraining, and improving inference-time performance by up to 29%. EBTs also surpass Diffusion Transformers on image denoising while requiring 99% fewer forward passes. Moreover, System 2 Thinking with EBTs yields larger performance gains on data that is farther out-of-distribution, and EBTs achieve better results than existing models on most downstream tasks despite achieving the same or worse pretraining performance, enabling EBTs to generalize better than existing approaches. Consequently, EBTs are a flexible and exciting new approach for scaling both the learning and thinking capabilities of models.

## One-Sentence Claim

Energy-Based Transformers learn unsupervised input-candidate compatibility functions that enable prediction by energy minimization and generalize inference-time thinking across modalities.

## Problem

Inference-time computation improves model performance, but many approaches are modality-specific, problem-specific, or require extra supervision such as verifiers or verifiable rewards.

The paper asks whether models can learn a general form of System 2-style thinking from unsupervised learning alone.

## Core Contribution

The paper introduces Energy-Based Transformers, a scalable class of energy-based models that assign energy to input and candidate-prediction pairs.

Prediction is reframed as optimization over candidate outputs with respect to the learned compatibility verifier.

## Method

EBTs train to evaluate compatibility between inputs and candidate predictions, then perform inference by minimizing energy until convergence.

The authors introduce techniques for stable, parallelizable training so energy-based prediction can scale across discrete and continuous modalities.

## Experiments and Evidence

The abstract reports that EBTs outperform Transformer++ across modalities, scale up to 35 percent faster during pretraining, and improve inference-time performance by up to 29 percent.

They outperform Diffusion Transformers on image denoising with 99 percent fewer forward passes, gain more on out-of-distribution data, and often beat existing models downstream despite equal or worse pretraining performance.

## Limits and Failure Modes

Energy minimization can add inference cost or convergence sensitivity, and energy landscapes may have local minima. Claims of general thinking require careful task diversity and comparison to strong test-time compute baselines.

Because this note is abstract-only, details still need checking: energy architecture, training objective, optimization steps, modality benchmarks, OOD setup, and pretraining-performance comparison.

## Deep Themes

- Learned verification from unsupervised data: compatibility scoring becomes a general prediction mechanism.
- Prediction as optimization: inference-time thinking is energy minimization rather than direct decoding alone.
- Cross-modal test-time compute: the same framework targets text, image, and continuous outputs.
- Pretraining loss is not full capability: downstream and OOD performance can improve despite worse conventional pretraining metrics.

## Subthemes

- Energy-Based Transformers.
- System 2 inference.
- Input-candidate compatibility.
- Energy minimization.

## Connections to Other Papers

This connects to Reasoning with Sampling, p-less sampling, DiffusionNFT, DCFold, and SFA through inference-time optimization and generative modeling.

It also relates to Train-before-Test because both challenge simple direct-pretraining metrics as the full measure of model potential.

## Notes for Cross-Paper Synthesis

EBTs add a broad test-time optimization theme: learned verifiers can make thinking a modality-general inference procedure rather than a text-only RL artifact.
