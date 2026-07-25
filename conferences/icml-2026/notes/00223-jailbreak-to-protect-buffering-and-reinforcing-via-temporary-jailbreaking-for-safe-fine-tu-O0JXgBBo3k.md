# Jailbreak to Protect: Buffering and Reinforcing via Temporary Jailbreaking for Safe Fine-Tuning in Large Language Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: O0JXgBBo3k
- Authors: Seokil Ham; Jaehyuk Jang; Wonjun Lee; Changick Kim
- Primary area: social_aspects->safety
- Keywords: Large Language Model;Harmful Finetuning Attack;Safe Finetuning;Parameter Efficient Finetuning
- Source URL: https://openreview.net/forum?id=O0JXgBBo3k
- PDF URL: https://openreview.net/pdf?id=O0JXgBBo3k

## Abstract

Fine-tuning-as-a-Service (FaaS) enables personalization of large language models (LLMs), but it can weaken safety-alignment under harmful fine-tuning attacks. Recent work has shown that activating harmful-behavior modules during fine-tuning can prevent models from learning undesired behaviors, but its mechanism remains unclear. In this paper, we revisit temporary jailbreaking as a defense against harmful fine-tuning and provide a gradient-level analysis showing that it saturates safety-degrading gradients while preserving benign task-relevant gradients. Based on this insight, we propose a **Buffer-and-Reinforce fine-tuning framework** that buffers harmful updates during user fine-tuning and reinforces safety after adaptation. Specifically, BufferLoRA induces temporary jailbreaking as a removable adapter to reduce harmful updates during user fine-tuning. After adaptation, ReinforceLoRA, trained to recover refusal behavior under the temporarily jailbroken state, is integrated with UserLoRA via QR decomposition-based merging to reinforce safety while preserving user-task performance. Extensive experiments show that our framework achieves superior safety and utility with no additional safety data during user fine-tuning and minimal computational cost.

## One-Sentence Claim

Buffer-and-Reinforce uses temporary jailbreaking adapters during fine-tuning to saturate harmful gradients, then merges a safety-reinforcing adapter to preserve refusal behavior and user-task utility.

## Problem

Fine-tuning-as-a-Service personalization can weaken LLM safety alignment under harmful fine-tuning attacks, and the mechanism behind temporary jailbreaking defenses was unclear.

## Core Contribution

The paper provides gradient-level analysis of temporary jailbreaking as a defense and proposes BufferLoRA plus ReinforceLoRA with QR decomposition-based merging for safe PEFT adaptation.

## Method

BufferLoRA induces temporary jailbreaking as a removable adapter during user fine-tuning, buffering safety-degrading updates while preserving benign gradients. ReinforceLoRA is trained to recover refusal under the jailbroken state and then merged with UserLoRA to reinforce safety.

## Experiments and Evidence

The abstract reports superior safety and utility with no additional safety data during user fine-tuning and minimal computational cost.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: threat model, attack datasets, adapter-merging stability, refusal overblocking, no-safety-data assumptions, and robustness to adaptive harmful fine-tuning attacks.

## Deep Themes

- Safety can be protected by manipulating gradient saturation during adaptation.
- Temporary weakening can paradoxically buffer against harmful learning.
- PEFT safety defenses need to preserve user-task utility after merging.

## Subthemes

- Fine-tuning-as-a-Service.
- Harmful fine-tuning attacks.
- Temporary jailbreaking.
- BufferLoRA.
- ReinforceLoRA.
- Safe PEFT merging.

## Connections to Other Papers

Connects to Robust Harmful Features, RLVepsR, GR-LoRA, and safety/unlearning papers through gradient-level safety preservation during adaptation.

## Notes for Cross-Paper Synthesis

This paper adds a counterintuitive safety-adaptation theme: controlled temporary exposure to harmful behavior can saturate harmful gradients and make later fine-tuning safer.
