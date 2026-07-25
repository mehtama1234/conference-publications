# WSM: Decay-Free Learning Rate Schedule via Checkpoint Merging for LLM Pre-training

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: HhThhjKyfw
- Authors: Changxin Tian; jiapeng wang; Qian Zhao; Kunlong Chen; Jia Liu; Ziqi Liu; Jiaxin Mao; Xin Zhao; Zhiqiang Zhang; JUN ZHOU
- Primary area: foundation or frontier models, including LLMs
- Keywords: llm pre-training;learning rate schedule;checkpoint merging;decay-free approach
- Source URL: https://openreview.net/forum?id=HhThhjKyfw
- PDF URL: https://openreview.net/pdf?id=HhThhjKyfw

## Abstract

Recent advances in learning rate~(LR) scheduling have demonstrated the effectiveness of decay-free approaches that eliminate the traditional decay phase while maintaining competitive performance. Model merging techniques have emerged as particularly promising solutions in this domain. We present Warmup-Stable and Merge (WSM), a general framework that establishes a formal connection between learning rate decay and model merging. WSM provides a unified theoretical foundation for emulating various decay strategies—including cosine decay, linear decay and inverse square root decay—as principled model averaging schemes, while remaining fully compatible with diverse optimization methods. Through extensive experiments, we identify merge duration—the training window for checkpoint aggregation—as the most critical factor influencing model performance, surpassing the importance of both checkpoint interval and merge quantity. Our framework consistently outperforms the widely-adopted Warmup-Stable-Decay (WSD) approach across multiple benchmarks, achieving significant improvements of +3.5\% on MATH, +2.9\% on HumanEval, and +5.5\% on MMLU-Pro. The performance advantages extend to supervised fine-tuning scenarios, highlighting WSM's potential for long-term model refinement.

## One-Sentence Claim

WSM replaces learning-rate decay with principled checkpoint merging, showing common decay schedules can be emulated as model-averaging schemes.

## Problem

Learning-rate schedules for LLM pretraining traditionally use decay phases, but decay-free approaches and model merging have shown promise.

The problem is to explain how checkpoint merging relates to decay and to identify which merging choices matter for performance.

## Core Contribution

The paper introduces Warmup-Stable and Merge, WSM, a framework connecting learning-rate decay to model averaging.

It provides a theoretical foundation for emulating cosine, linear, and inverse-square-root decay as principled checkpoint-merging schemes, compatible with diverse optimizers.

## Method

WSM trains with warmup and stable phases, then merges checkpoints over a selected duration instead of running an explicit decay schedule.

The analysis treats decay behavior as recoverable through averaging model states. Experiments study merge duration, checkpoint interval, and number of merged checkpoints.

## Experiments and Evidence

The abstract reports that merge duration is the most important factor, more important than checkpoint interval or merge quantity.

WSM outperforms Warmup-Stable-Decay across multiple benchmarks, with improvements of +3.5 percent on MATH, +2.9 percent on HumanEval, and +5.5 percent on MMLU-Pro. Gains extend to supervised fine-tuning.

## Limits and Failure Modes

Checkpoint merging assumes checkpoints lie in compatible regions of parameter space. It may behave differently under unstable training, sharp distribution shifts, or aggressive optimizer changes.

Because this note is abstract-only, details still need checking: model sizes, pretraining budget, exact merge formula, optimizer coverage, benchmark setup, and interaction with downstream SFT.

## Deep Themes

- Learning-rate decay as parameter averaging: schedules can be reinterpreted geometrically.
- Checkpoint merging as training primitive: model averaging is not only post-hoc ensembling.
- Merge duration matters: the training window for aggregation controls final behavior.
- Decay-free pretraining: long-term refinement can avoid explicit LR decay phases.

## Subthemes

- Warmup-Stable-Merge.
- Cosine/linear/inverse-square-root decay emulation.
- Checkpoint aggregation.
- Pretraining and SFT refinement.

## Connections to Other Papers

This connects to Self-Soupervision, model soups, LoRA-Pre, and optimizer-scaling work through parameter-space composition.

It also relates to ScaleRL and coverage theory because training trajectory selection can matter as much as final loss.

## Notes for Cross-Paper Synthesis

WSM adds a trajectory-averaging theme: model quality can be improved by combining checkpoints across a carefully chosen training window rather than only optimizing the final step.
