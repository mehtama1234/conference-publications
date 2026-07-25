# Steer Like the LLM: Activation Steering that Mimics Prompting

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 06Nk3dJDMq
- Authors: Geert Heyman; Frederik Vandeputte
- Primary area: deep_learning->large_language_models
- Keywords: Activation Steering;Instruction Following;Interpretability;Large Language Models
- Source URL: https://openreview.net/forum?id=06Nk3dJDMq
- PDF URL: https://openreview.net/pdf?id=06Nk3dJDMq

## Abstract

Large language models can be steered at inference time through prompting or activation interventions, but activation steering methods often underperform compared to prompt-based approaches. We investigate whether activation steering can be improved by learning to mimic the interventions that prompt steering triggers within the model. To this end, we introduce *Prompt Steering Replacement (PSR)* models, a new family of activation steering methods that distill prompt steering behavior into interpretable interventions on model activations. A PSR is an activation steering method that estimates position-specific steering coefficients and is trained to imitate prompt-based interventions. Experiments on persona steering and instruction following across multiple language models demonstrate that PSR models consistently outperform constant-coefficient interventions that are frequently used in the literature and achieve performance close to or exceeding prompt steering while maintaining interpretability.

## One-Sentence Claim

Prompt Steering Replacement models improve activation steering by learning activation interventions that mimic the internal effects of prompt-based steering.

## Problem

Prompting can steer LLM behavior at inference time, but activation steering methods often underperform prompt-based methods despite being more direct and potentially interpretable.

## Core Contribution

The paper introduces PSR models, activation steering methods with position-specific coefficients trained to imitate prompt-triggered internal interventions.

## Method

PSR distills the behavior of prompt steering into activation-space interventions. Instead of using constant steering coefficients, it estimates position-specific coefficients that better match how prompts alter model activations.

## Experiments and Evidence

The abstract reports experiments on persona steering and instruction following across multiple LLMs, where PSR outperforms common constant-coefficient interventions and approaches or exceeds prompt steering while remaining interpretable.

## Limits and Failure Modes

PDF checks needed: how much prompt data is needed to train PSR, whether learned interventions transfer across tasks/models, whether interpretability is qualitative or measurable, and whether activation edits create off-target behavior.

## Deep Themes

- Prompting is being reverse-engineered into reusable internal controls.
- Interpretability and controllability are converging.
- Inference-time interventions are becoming alternatives to fine-tuning.

## Subthemes

- Activation steering.
- Instruction following.
- Persona control.
- Prompt distillation.
- Position-specific interventions.

## Connections to Other Papers

Connects directly to the Tell-Tale Norm through activation-level control and to broader test-time steering/adaptation papers.

## Notes for Cross-Paper Synthesis

This paper supports the pattern that the field is moving from surface prompt engineering toward internal interface engineering: learn what prompts do inside the model, then reproduce or control that effect directly.
