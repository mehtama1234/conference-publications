# Taming Momentum: Rethinking Optimizer States Through Low-Rank Approximation

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 9Q0dNBYeEY
- Authors: Zhengbo Wang; Jian Liang; Ran He; Zilei Wang; Tieniu Tan
- Primary area: foundation or frontier models, including LLMs
- Keywords: Large Language Models; Efficient Training; Low-Rank; LoRA
- Source URL: https://openreview.net/forum?id=9Q0dNBYeEY
- PDF URL: https://openreview.net/pdf?id=9Q0dNBYeEY

## Abstract

Modern optimizers like Adam and Muon are central to training large language models, but their reliance on first- and second-order momenta introduces significant memory overhead, which constrains scalability and computational efficiency. 
In this work, we re-frame the exponential moving average (EMA) used in these momenta as the training of a linear regressor via online gradient flow. 
Building on this equivalence, we introduce LoRA-Pre, a novel low-rank optimizer designed for efficient pre-training. 
Specifically, LoRA-Pre reduces the optimizer's memory footprint by decomposing the full momentum matrix into a compact low-rank subspace within the online linear learner, thereby maintaining optimization performance while improving memory efficiency. 
We empirically validate LoRA-Pre's efficacy by pre-training models from the Llama architecture family, scaling from 60M to 1B parameters. 
LoRA-Pre achieves the highest performance across all model sizes.
Notably, LoRA-Pre demonstrates remarkable rank efficiency, achieving comparable or superior results using only 1/8 the rank of baseline methods. 
Beyond pre-training, we evaluate LoRA-Pre's effectiveness in fine-tuning scenarios. 
With the same rank, LoRA-Pre consistently outperforms all efficient fine-tuning baselines.
Specifically, compared to standard LoRA, LoRA-Pre achieves substantial improvements of 3.14 points on Llama-3.1-8B and 6.17 points on Llama-2-7B, validating our approach's effectiveness across both pre-training and fine-tuning paradigms.

## One-Sentence Claim

LoRA-Pre reduces optimizer-state memory by treating momentum EMA as online linear learning and storing the momentum matrix in a compact low-rank subspace.

## Problem

Adam, Muon, and related optimizers are central to LLM training, but their first- and second-order moment states consume substantial memory. This limits scalability and efficiency in pretraining and finetuning.

The problem is to retain optimizer performance while reducing the memory footprint of momentum states.

## Core Contribution

The paper reframes EMA momentum as training a linear regressor through online gradient flow. From that equivalence it proposes LoRA-Pre, a low-rank optimizer for efficient pretraining.

LoRA-Pre decomposes the full momentum matrix into a compact low-rank subspace inside the online linear learner.

## Method

LoRA-Pre maintains optimizer momentum through a low-rank representation rather than a full dense state. This reduces memory while attempting to preserve the useful direction-tracking behavior of momentum.

The method is evaluated both for pretraining and finetuning, comparing against efficient training and LoRA-style baselines.

## Experiments and Evidence

The abstract reports pretraining Llama-family models from 60M to 1B parameters, where LoRA-Pre achieves the highest performance across model sizes.

It reports strong rank efficiency, matching or exceeding baselines at 1/8 the rank. In finetuning, LoRA-Pre outperforms efficient baselines and improves over standard LoRA by 3.14 points on Llama-3.1-8B and 6.17 points on Llama-2-7B.

## Limits and Failure Modes

Low-rank momentum may fail when useful optimizer state is high-rank or rapidly changing. The results need validation at larger pretraining scales and across more architectures.

Because this note is abstract-only, details still need checking: memory accounting, rank schedules, optimizer-state decomposition, baselines, tasks, finetuning metrics, and wall-clock overhead.

## Deep Themes

- Optimizer state as learnable structure: momentum can be reinterpreted as online regression.
- Low-rank training infrastructure: memory compression applies to optimizer dynamics, not only model weights.
- Rank efficiency: useful update information may occupy a smaller subspace than dense states suggest.
- Unified pretraining and finetuning efficiency: the same optimizer idea can affect both regimes.

## Subthemes

- EMA as online gradient flow.
- Low-rank momentum matrices.
- Llama-family pretraining.
- LoRA-compatible finetuning gains.

## Connections to Other Papers

This connects to ICML Beyond Muon, SGD RLVR, Adam degeneracy, and EntroKV through rethinking default training/inference memory.

It also relates to efficient adaptation papers such as BioX-Bridge and LoRA/expert-routing work because low-rank structure becomes an efficiency primitive.

## Notes for Cross-Paper Synthesis

LoRA-Pre adds another optimizer-geometry theme: reducing memory is possible when optimizer state is treated as structured representation rather than dense bookkeeping.
