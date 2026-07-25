# DiffusionNFT: Online Diffusion Reinforcement with Forward Process

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: VJZ477R89F
- Authors: Kaiwen Zheng; Huayu Chen; Haotian Ye; Haoxiang Wang; Qinsheng Zhang; Kai Jiang; Hang Su; Stefano Ermon; Jun Zhu; Ming-Yu Liu
- Primary area: generative models
- Keywords: Diffusion Models;Reinforcement Learning;Flow Matching
- Source URL: https://openreview.net/forum?id=VJZ477R89F
- PDF URL: https://openreview.net/pdf?id=VJZ477R89F

## Abstract

Online reinforcement learning (RL) has been central to post-training language models, but its extension to diffusion models remains challenging due to intractable likelihoods. Recent works discretize the reverse sampling process to enable GRPO-style training, yet they inherit fundamental drawbacks, including solver restrictions, forward–reverse inconsistency, and complicated integration with classifier-free guidance (CFG). We introduce Diffusion Negative-aware FineTuning (DiffusionNFT), a new online RL paradigm that optimizes diffusion models directly on the forward process via flow matching. DiffusionNFT contrasts positive and negative generations to define an implicit policy improvement direction, naturally incorporating reinforcement signals into the supervised learning objective. 
This formulation enables training with arbitrary black-box solvers, eliminates the need for likelihood estimation, and requires only clean images rather than sampling trajectories for policy optimization. DiffusionNFT is up to $25\times$ more efficient than FlowGRPO in head-to-head comparisons, while being CFG-free. For instance, DiffusionNFT improves the GenEval score from 0.24 to 0.98 within 1k steps, while FlowGRPO achieves 0.95 with over 5k steps and additional CFG employment. By leveraging multiple reward models, DiffusionNFT significantly boosts the performance of SD3.5-Medium in every benchmark tested.

## One-Sentence Claim

DiffusionNFT performs online reward optimization for diffusion models through forward-process flow matching, avoiding likelihood estimation, solver restrictions, and CFG dependence.

## Problem

Online RL post-training is effective for language models, but diffusion models are harder to optimize with RL because likelihoods are intractable.

Reverse-process discretization methods enable GRPO-style training but introduce solver restrictions, forward-reverse inconsistency, and awkward interactions with classifier-free guidance.

## Core Contribution

The paper introduces Diffusion Negative-aware FineTuning, an online RL paradigm for diffusion models.

It optimizes the forward process via flow matching and contrasts positive and negative generations to define an implicit policy-improvement direction within a supervised objective.

## Method

DiffusionNFT uses reward signals to distinguish positive and negative generations, then incorporates that contrast into forward-process training.

Because it avoids reverse trajectory likelihood estimation, it can work with arbitrary black-box solvers, requires only clean images rather than full sampling trajectories, and removes the need for CFG in the reported setup.

## Experiments and Evidence

The abstract reports head-to-head comparisons against FlowGRPO.

DiffusionNFT is up to 25x more efficient, improves GenEval from 0.24 to 0.98 within 1,000 steps, while FlowGRPO reaches 0.95 with over 5,000 steps plus CFG. With multiple reward models, it improves SD3.5-Medium across every benchmark tested.

## Limits and Failure Modes

Reward-model quality is central; optimizing multiple reward models can still produce reward hacking or aesthetic overfitting. Forward-process optimization may also behave differently across modalities and solvers.

Because this note is abstract-only, details still need checking: positive/negative sampling construction, flow-matching loss, reward models, benchmark set, solver compatibility, and comparisons under equal compute.

## Deep Themes

- Diffusion RL without likelihoods: reward optimization moves to the tractable forward process.
- Positive-negative contrast as policy improvement: preferences shape supervised diffusion updates.
- Solver-agnostic post-training: diffusion adaptation should not be tied to one reverse sampler.
- CFG-free reward alignment: guidance can be replaced by learned reward-conditioned updates.

## Subthemes

- Online diffusion RL.
- Forward-process flow matching.
- Negative-aware fine-tuning.
- Reward-model guided image generation.

## Connections to Other Papers

This connects to SafeDPO, LongWriter-Zero, AgentFlow, and RLVR work through objective design for post-training.

It also relates to DCFold, PCD, and HyCa because all adapt or accelerate diffusion-style generative systems.

## Notes for Cross-Paper Synthesis

DiffusionNFT broadens the RL post-training theme beyond LLMs: reward optimization is being reformulated for generative families whose likelihoods are not directly usable.
