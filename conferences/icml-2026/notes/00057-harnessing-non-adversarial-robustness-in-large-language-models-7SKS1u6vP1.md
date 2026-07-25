# Harnessing Non-Adversarial Robustness in Large Language Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 7SKS1u6vP1
- Authors: Qinghua Zhou; Ellina Aleshina; Andrey Lovyagin; Oleg Somov; Mikhail Seleznyov; Alexander Panchenko; Ivan Oseledets; Elena Tutubalina; Ivan Y Tyukin
- Primary area: deep_learning->large_language_models
- Keywords: llms' robustness;data influence;model editing;semantically neutral perturbations
- Source URL: https://openreview.net/forum?id=7SKS1u6vP1
- PDF URL: https://openreview.net/pdf?id=7SKS1u6vP1

## Abstract

The work presents an approach for addressing the challenge of robustness in Large Language Models (LLMs) to alterations and potential errors caused by semantically similar but textually different prompts. Recent works have shown that these kinds of prompt variations can significantly impact the performance of LLMs on tasks. The central question is: can LLMs' robustness to semantically-neutral prompt alterations be acquired without expensive retraining of the entire model? We address this question both theoretically and through experiments. Our theoretical analysis reveals a crucial factor impacting model robustness -- a systematic expected shift or perturbation-induced bias in neural network module outputs. Motivated by this analysis, we show that robustness can be achieved via a simple fine-tuning process: debiasing for robustness. We identify conditions when debiasing helps and when it does not, and demonstrate, through both theory and extensive experiments, that debiasing for robustness may indeed be a quick and efficient tool to enhance robustness and provide certification against random prompt perturbations.

## One-Sentence Claim

LLM robustness to semantically neutral prompt changes can be improved and certified by debiasing perturbation-induced shifts in neural module outputs.

## Problem

Semantically similar but textually different prompts can change LLM behavior, and full retraining or adversarial robustness methods may be too expensive or mismatched for ordinary non-adversarial prompt variation.

## Core Contribution

The paper identifies perturbation-induced bias in module outputs as a key robustness factor and proposes debiasing methods plus certification conditions for random prompt perturbations.

## Method

The theoretical analysis links robustness to expected shifts under perturbation, robustness radii, sparsity, and Lipschitz-like determinants. The mitigation uses input-independent and input-dependent debiasing to compensate module-output shifts.

## Experiments and Evidence

The abstract reports theory and extensive experiments showing when debiasing helps, when it does not, and how it can provide certification against random prompt perturbations.

## Full-Text Upgrade

The full text distinguishes non-adversarial robustness from worst-case jailbreak-style robustness. The target is robustness to semantically neutral prompt perturbations, where performance drops because expected module outputs shift under the perturbation distribution.

The paper's geometric analysis shows multiple regimes: debiasing can improve robustness when perturbation-induced bias moves examples toward a decision boundary, but it may not help if robustness loss is governed by other factors or if the bias already improves margins. Experiments evaluate logits/module-output debiasing and report both per-example and population-level certification metrics, including cases where input-dependent debiasing improves clean and perturbed performance jointly.

## Limits and Failure Modes

Limits to watch: debiasing depends on perturbation distributions; certificates concern random prompt perturbations rather than adaptive adversaries; and gains vary by task/model depending on whether perturbation-induced bias is the actual robustness bottleneck.

## Deep Themes

- Prompt robustness can be treated as distributional debiasing.
- Robustness certificates need not require full model retraining.
- Non-adversarial robustness is distinct from jailbreak robustness and needs separate tools.

## Subthemes

- Semantically neutral perturbations.
- Perturbation-induced bias.
- Robustness certification.
- Logit/module debiasing.
- Random prompt perturbations.
- LoRA/fine-tuning efficiency.

## Connections to Other Papers

Connects to Pressure Reveals Character and Rare Event Analysis through evaluation beyond ordinary prompts, and to activation/representation intervention papers through internal-output correction.

## Notes for Cross-Paper Synthesis

This paper adds a robustness calibration theme: not all prompt sensitivity is adversarial, and some failures can be handled by correcting systematic internal shifts under benign perturbation distributions.
