# Beyond Log Likelihood: Probability-Based Objectives for Supervised Fine-Tuning across the Model Capability Continuum

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 2hQBG2ZlFb
- Authors: Gaotang Li; Ruizhong Qiu; Xiusi Chen; Heng Ji; Hanghang Tong
- Primary area: deep_learning->foundation_models
- Keywords: Post-Training;SFT;training objectives
- Source URL: https://openreview.net/forum?id=2hQBG2ZlFb
- PDF URL: https://openreview.net/pdf?id=2hQBG2ZlFb

## Abstract

Supervised fine-tuning (SFT) is the standard approach for post-training large language models (LLMs), yet it often shows limited generalization. We trace this limitation to its default training objective: negative log likelihood (NLL). While NLL is classically optimal when training from scratch, post-training operates in a different paradigm and could violate its optimality assumptions, where models already encode task-relevant priors and supervision can be long and noisy. In this work, we systematically study various probability-based objectives and characterize when and why different objectives succeed or fail under varying conditions. Through comprehensive experiments and extensive ablation studies across 8 model backbones, 27 benchmarks, and 7 domains, we uncover a critical dimension that governs objective behavior: the model-capability continuum. Near the model-strong end, prior-leaning objectives that downweight low-probability tokens (e.g., $-p$, $-p^{10}$, thresholded variants) consistently outperform NLL; toward the model-weak end, NLL dominates; in between, no single objective prevails. Our theoretical analysis further elucidates how objectives trade places across the continuum, providing a principled foundation for adapting objectives to model capability. The code is available at https://github.com/GaotangLi/Beyond-Log-Likelihood.

## One-Sentence Claim

SFT objectives should depend on model capability: strong models benefit from prior-leaning probability objectives that downweight low-probability tokens, while weak models still favor NLL.

## Problem

NLL is standard for supervised fine-tuning, but post-training differs from training from scratch because models already encode priors and supervision can be long/noisy, so NLL's classical assumptions can fail.

## Core Contribution

The paper systematically studies probability-based SFT objectives and identifies the model-capability continuum as the key variable governing which objectives work.

## Method

It compares objectives such as NLL, negative probability, high-power probability objectives, and thresholded variants across many models/domains, then analyzes how objectives trade off across capability levels.

## Experiments and Evidence

The abstract reports experiments across 8 backbones, 27 benchmarks, and 7 domains. Strong models prefer prior-leaning objectives; weak models prefer NLL; mid-range models have no single winner.

## Full-Text Upgrade

The full text sharpens the key rule: NLL is prior-averse because it gives large gradient weight to low-probability supervision tokens, while objectives like `-p`, `-p^10`, and thresholded variants are prior-leaning because they reinforce tokens the model already considers plausible and downweight low-probability tokens that may be noisy or outside the model's learned prior. The paper positions this as a capability continuum rather than a universal replacement for NLL.

The empirical design spans model-strong, model-weak, and intermediate settings. On model-strong tasks such as math reasoning, prior-leaning objectives can improve over NLL by leaning into useful pretrained priors; on model-weak tasks such as distributions absent from pretraining, NLL remains better because it forces the model to learn low-probability targets. The thresholding experiments are especially diagnostic: removing low-confidence tokens can help strong models, suggesting those tokens may function as noise rather than useful supervision.

## Limits and Failure Modes

Limits to watch: capability must be diagnosed per domain, not assumed from model size alone; threshold choices are task-sensitive; and the paper does not resolve how these objectives interact with later preference tuning, calibration, or safety-specific behavior.

## Deep Themes

- Post-training objectives should adapt to model priors.
- Stronger models need less imitation of every supervision token.
- Capability-conditioned training rules are emerging.

## Subthemes

- Supervised fine-tuning.
- Probability objectives.
- Model capability continuum.
- Noisy supervision.
- Post-training theory.

## Connections to Other Papers

Connects to Base Models Know How to Reason and DMPO: post-training changes may depend heavily on what the base model already knows.

## Notes for Cross-Paper Synthesis

This sharpens a recurring post-training theme: the same objective can be beneficial or harmful depending on model capability and prior knowledge.
