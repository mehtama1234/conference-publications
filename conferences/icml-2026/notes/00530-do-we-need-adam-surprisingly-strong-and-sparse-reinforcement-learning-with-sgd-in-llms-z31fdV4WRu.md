# Do We Need Adam? Surprisingly Strong and Sparse Reinforcement Learning with SGD in LLMs

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: z31fdV4WRu
- Authors: Sagnik Mukherjee; Lifan Yuan; Pavan Jayasinha; Dilek Hakkani-Tür; Hao Peng
- Primary area: deep_learning->large_language_models
- Keywords: RLVR;Large Language Models;Optimization;Post-training
- Source URL: https://openreview.net/forum?id=z31fdV4WRu
- PDF URL: https://openreview.net/pdf?id=z31fdV4WRu

## Abstract

Reinforcement learning (RL), particularly RL from verifiable reward (RLVR), has become a crucial phase of training large language models (LLMs) and a key focus of current scaling efforts. 
However, optimization practices in RL largely follow those of next-token-prediction stages (e.g., pretraining and supervised fine-tuning), despite the fundamental differences between RL and these stages emphasized by recent work.
One such practice is the use of the AdamW optimizer, which is widely adopted for training large-scale transformers despite its high memory overhead. 
Our analysis shows that both momentum and adaptive learning rate of AdamW are less influential in RL than in SFT, leading us to hypothesize that RL benefits less from Adam’s per-parameter adaptive learning rates and momentum.
Confirming our hypothesis, our experiments demonstrate that the substantially more memory-efficient SGD, which is known to perform poorly in supervised learning of large-scale transformers, matches or even outperforms AdamW in RL for LLMs.
Remarkably, full fine-tuning with SGD updates fewer than 0.02% of model without any sparsity-promoting regularization, more than 1,000 times fewer than AdamW. Our analysis offers potential reasons for this update sparsity.
Our findings provide fresh insights into the optimization dynamics of RL in LLMs and demonstrate that RL can be substantially more parameter-efficient than previously recognized.

## One-Sentence Claim

In LLM RLVR post-training, memory-efficient SGD can match or outperform AdamW and naturally produces extremely sparse full-finetuning updates.

## Problem

LLM RL post-training often inherits optimizer choices from pretraining and supervised fine-tuning, especially AdamW. But RLVR differs from next-token prediction, and AdamW's momentum and adaptive learning rates carry high memory cost.

The problem is whether AdamW is actually necessary for RLVR, or whether simpler optimizers can exploit the different optimization dynamics of verifiable-reward training.

## Core Contribution

The paper analyzes AdamW components in RL and finds that momentum and adaptive learning rates are less influential than in SFT.

It demonstrates experimentally that SGD, despite poor reputation for supervised large-transformer training, can match or outperform AdamW in LLM RL while using much less optimizer memory.

## Method

The authors compare optimization behavior in RLVR versus SFT, isolating the effects of AdamW momentum and adaptive learning rates.

They train LLMs with SGD during RL and analyze update sparsity. Full finetuning with SGD updates fewer than 0.02 percent of model parameters without explicit sparsity regularization.

## Experiments and Evidence

The abstract reports that SGD matches or beats AdamW in LLM RL experiments.

It also reports that SGD updates more than 1,000 times fewer parameters than AdamW under full finetuning, suggesting RLVR can be more parameter-efficient than expected.

## Limits and Failure Modes

The result may depend on RLVR reward structure, model scale, rollout setup, learning-rate tuning, and task distribution. SGD may be less stable in noisier or less sparse reward regimes.

Because this note is abstract-only, details still need checking: model sizes, RL algorithm, benchmarks, learning-rate schedules, optimizer memory accounting, sparsity measurement, and whether SGD preserves general capabilities.

## Deep Themes

- RL optimization differs from SFT: post-training may not need the same adaptive machinery as next-token prediction.
- Optimizer memory as scaling bottleneck: replacing AdamW can reduce serving or training resource pressure.
- Emergent update sparsity: RLVR may alter only a tiny subset of parameters even under full finetuning.
- Parameter efficiency in alignment: useful policy changes can be much sparser than expected.

## Subthemes

- AdamW component ablation.
- SGD for LLM RLVR.
- Sparse full finetuning without regularization.
- Optimizer choice under verifiable rewards.

## Connections to Other Papers

This connects to Beyond Muon, Adam degeneracy, SlaClip, and optimizer phase-analysis papers through reassessing standard optimizer assumptions.

It also links to DAWN, Ctrl-R, RAGEN-2, and Obfuscation Atlas because all study how RL post-training dynamics differ from supervised language modeling.

## Notes for Cross-Paper Synthesis

This paper reinforces a post-training-specific optimization theme: RLVR has different geometry from SFT, so inherited optimizer defaults may be overbuilt or misleading.
