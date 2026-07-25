# OPUS: Towards Efficient and Principled Data Selection in Large Language Model Pre-training in Every Iteration

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: lcLxGrk5N9
- Authors: Shaobo Wang; Xuan Ouyang; Tianyi Xu; Yuzheng Hu; Jialin Liu; Guo Chen; Tianyu Zhang; Junhao Zheng; Kexin Yang; Xingzhang Ren; Dayiheng Liu; Linfeng Zhang
- Primary area: deep_learning->large_language_models
- Keywords: Data Selection;Pre-training;Data Efficiency;Large Language Model
- Source URL: https://openreview.net/forum?id=lcLxGrk5N9
- PDF URL: https://openreview.net/pdf?id=lcLxGrk5N9

## Abstract

As high-quality public text approaches exhaustion, a phenomenon known as the Data Wall—LLM pre-training is shifting from more tokens to better tokens. However, existing methods either rely on heuristic static filters that ignore training dynamics, or use dynamic yet optimizer-agnostic criteria based on raw gradients. We propose OPUS (Optimizer-induced Projected Utility Selection), a dynamic framework that defines utility in the optimizer-induced update space. OPUS scores candidates by projecting their effective updates, shaped by modern optimizers, onto a target direction derived from a stable, in-distribution proxy. To ensure scalability, we employ Ghost technique with CountSketch for computational efficiency, and Boltzmann sampling for data diversity, incurring only 4.7% additional compute overhead. OPUS achieves remarkable results across diverse corpora, quality tiers, optimizers, and model scales. It also outperforms previous data selection methods across different stages of training, including from-scratch pre-training and also mid-training. Beyond online selection, the OPUS utility score also demonstrates potential as a static filter for flagging and removing toxic documents from contaminated training corpora prior to training.

## One-Sentence Claim

OPUS selects pretraining data dynamically by scoring candidate documents in the optimizer-induced update space, improving data efficiency with modest overhead.

## Problem

As high-quality public text becomes scarce, LLM pretraining must shift from more tokens to better tokens. Static filters ignore training dynamics, while dynamic gradient-based methods often ignore how modern optimizers transform updates.

The paper asks how to select useful data during every training iteration in a way that reflects the actual optimizer-induced parameter update.

## Core Contribution

OPUS defines data utility in the optimizer-induced update space. It scores candidates by projecting their effective optimizer-shaped updates onto a target direction derived from a stable in-distribution proxy.

For scalability, it uses Ghost technique with CountSketch and Boltzmann sampling, adding only 4.7% compute overhead. It works across corpora, quality tiers, optimizers, model scales, pretraining, and mid-training.

## Method

For each candidate, OPUS estimates the update that the optimizer would induce, projects that update onto a target direction, and samples data according to utility while preserving diversity through Boltzmann sampling.

CountSketch/Ghost approximations reduce the cost of per-example utility estimation enough for online selection.

## Experiments and Evidence

Evidence reported in the abstract:

- Dynamic data selection in every iteration.
- Utility defined in optimizer-induced update space.
- Target direction from stable in-distribution proxy.
- Ghost technique with CountSketch.
- Boltzmann sampling for diversity.
- Only 4.7% additional compute overhead.
- Strong results across corpora, quality tiers, optimizers, and model scales.
- Outperforms previous methods in from-scratch pretraining and mid-training.
- Utility score can flag toxic documents before training.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: proxy construction, compute accounting, toxicity evaluation, and training-scale results.

## Limits and Failure Modes

- Target-direction choice may bias learning toward proxy distribution.
- Online selection can reduce diversity if sampling temperature is poorly chosen.
- Utility estimates may be noisy for rare but important data.
- Toxicity filtering claims require careful validation across languages and domains.

## Deep Themes

**Data selection should follow optimizer geometry.** Utility depends on the update actually applied, not raw gradient alone.

**The data wall turns curation into training infrastructure.** Better token choice becomes part of every iteration.

**Selection can be both dynamic and scalable.** Sketching makes principled per-candidate scoring feasible.

## Subthemes

- Optimizer-induced utility.
- Online pretraining data selection.
- CountSketch/Ghost approximation.
- Boltzmann diversity sampling.
- Toxic document filtering.

## Connections to Other Papers

Connects to PRISM, Source Screening, VideoKR, daVinci-Dev, and data-governance papers. It offers a pretraining-scale version of evidence/data selection.

## Notes for Cross-Paper Synthesis

OPUS strengthens the data-governance theme: as raw token supply saturates, the decisive question becomes which examples produce the right optimizer updates at each training stage.
