# Reasoning with Sampling: Your Base Model is Smarter Than You Think

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: Vsgq2ldr4K
- Authors: Aayush Karan; Yilun Du
- Primary area: foundation or frontier models, including LLMs
- Keywords: LLMs;reasoning;MCMC;sampling;inference-time compute
- Source URL: https://openreview.net/forum?id=Vsgq2ldr4K
- PDF URL: https://openreview.net/pdf?id=Vsgq2ldr4K

## Abstract

Frontier reasoning models have exhibited incredible capabilities across a wide array of disciplines, driven by posttraining large language models (LLMs) with reinforcement learning (RL). However, despite the widespread success of this paradigm, much of the literature has been devoted to disentangling truly novel behaviors that emerge during RL but are not present in the base models. In our work, we approach this question from a different angle, instead asking whether comparable reasoning capabilities can be elicited from base models at inference time by pure sampling, without any additional training. Inspired by Markov chain Monte Carlo (MCMC) techniques for sampling from sharpened distributions, we propose a simple iterative sampling algorithm leveraging the base models' own likelihoods. Over different base models, we show that our algorithm offers substantial boosts in reasoning that nearly match and even outperform those from RL on a wide variety of single-shot tasks, including MATH500, HumanEval, and GPQA. Moreover, our sampler avoids the collapse in diversity over multiple samples that is characteristic of RL-posttraining. Crucially, our method does not require training, curated datasets, or a verifier, suggesting broad applicability beyond easily verifiable domains.

## One-Sentence Claim

This paper shows that base-model reasoning can be substantially elicited at inference time through an MCMC-inspired iterative sampler using only the model's own likelihoods.

## Problem

Frontier reasoning performance is often attributed to RL post-training, but it is unclear how much genuinely new behavior RL creates versus how much it elicits from pretrained base models.

If base models already contain latent reasoning ability, inference-time sampling might recover it without curated data, verifiers, or additional training.

## Core Contribution

The paper proposes a simple iterative sampling algorithm inspired by MCMC sampling from sharpened distributions.

It uses the base model's own likelihoods to improve reasoning outputs without post-training, reward models, curated datasets, or verifiers.

## Method

The sampler repeatedly explores candidate completions under a sharpened distribution derived from the base model likelihood.

The intended effect is to concentrate probability mass around stronger reasoning solutions while preserving diversity better than RL-posttrained models.

## Experiments and Evidence

The abstract reports substantial reasoning gains across base models.

The sampler nearly matches and sometimes outperforms RL gains on single-shot tasks including MATH500, HumanEval, and GPQA, while avoiding diversity collapse across multiple samples.

## Limits and Failure Modes

Inference-time sampling can be compute-intensive, and likelihood sharpening may favor confident but wrong reasoning in some domains. The result is reported for single-shot tasks, so multi-turn agentic settings may differ.

Because this note is abstract-only, details still need checking: sampler algorithm, compute budget, base models, temperature/sharpening settings, diversity metrics, and comparisons to best-of-N or verifier-guided sampling.

## Deep Themes

- Latent base-model capability: post-training may expose abilities already present in pretrained distributions.
- Sampling as reasoning control: inference algorithms can shape reasoning quality without weight updates.
- Diversity-preserving reasoning: avoiding RL-induced mode collapse can matter for multi-sample use.
- Verifier-free test-time compute: stronger answers can emerge from likelihood-only search.

## Subthemes

- MCMC-inspired decoding.
- Base-model reasoning.
- Inference-time compute.
- Diversity versus RL collapse.

## Connections to Other Papers

This connects to p-less sampling, ASAG, HSD, ThinKV, and LongWriter-Zero through test-time and post-training routes to reasoning control.

It also relates to Train-before-Test because both separate latent model potential from direct benchmark behavior.

## Notes for Cross-Paper Synthesis

This paper adds a sharp counterpoint to RL post-training: some reasoning gains may be accessible through better samplers over the base model distribution.
