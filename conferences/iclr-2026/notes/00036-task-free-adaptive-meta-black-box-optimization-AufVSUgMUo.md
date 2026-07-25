# Task-free Adaptive Meta Black-box Optimization

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: AufVSUgMUo
- Authors: Chao Wang; Licheng Jiao; Lingling Li; Jiaxuan Zhao; Guanchun Wang; Fang Liu; Shuyuan Yang
- Primary area: optimization
- Keywords: Meta Black-box Optimization;Evolutionary Algorithms
- Source URL: https://openreview.net/forum?id=AufVSUgMUo
- PDF URL: https://openreview.net/pdf?id=AufVSUgMUo

## Abstract

Handcrafted optimizers become prohibitively inefficient for complex black-box optimization (BBO) tasks. MetaBBO addresses this challenge by meta-learning to automatically configure optimizers for low-level BBO tasks, thereby eliminating heuristic dependencies. However, existing methods typically require extensive handcrafted training tasks to learn meta-strategies that generalize to target tasks, which poses a critical limitation for realistic applications with unknown task distributions. To overcome the issue, we propose the Adaptive meta Black-box Optimization Model (ABOM), which performs online parameter adaptation using solely optimization data from the target task, obviating the need for predefined task distributions. Unlike conventional metaBBO frameworks that decouple meta-training and optimization phases, ABOM introduces a closed-loop adaptive parameter learning mechanism, where parameterized evolutionary operators continuously self-update by leveraging generated populations during optimization. This paradigm shift enables zero-shot optimization: ABOM achieves competitive performance on synthetic BBO benchmarks and realistic unmanned aerial vehicle path planning problems without any handcrafted training tasks. Visualization studies reveal that parameterized evolutionary operators exhibit statistically significant search patterns, including natural selection and genetic recombination.

## One-Sentence Claim

ABOM performs meta black-box optimization without handcrafted training tasks by adapting evolutionary operators online using only target-task optimization data.

## Problem

Handcrafted black-box optimizers can be inefficient on complex tasks. MetaBBO learns optimizer configuration, but existing methods typically require many handcrafted training tasks and assumptions about the target-task distribution.

Real applications often have unknown task distributions, so task-dependent meta-training becomes a bottleneck.

## Core Contribution

The paper proposes Adaptive meta Black-box Optimization Model, ABOM, which learns optimizer parameters online during the target optimization run.

It replaces the decoupled meta-training/optimization split with a closed-loop mechanism where parameterized evolutionary operators self-update from generated populations.

## Method

ABOM uses evolutionary operators whose parameters are updated continuously as optimization proceeds. The generated populations provide the data for adaptation.

This enables zero-shot optimization without predefined training tasks or handcrafted task distributions.

## Experiments and Evidence

The abstract reports competitive performance on synthetic BBO benchmarks and realistic unmanned aerial vehicle path-planning problems without handcrafted training tasks.

Visualization studies show statistically significant search patterns in the learned evolutionary operators, including natural selection and genetic recombination.

## Limits and Failure Modes

Online adaptation may be unstable on very noisy objectives or tasks where early populations are misleading. It may also require careful control of exploration and exploitation.

Because this note is abstract-only, details still need checking: parameterization of evolutionary operators, adaptation objective, benchmark set, UAV planning setup, compute budget, and comparisons to task-trained MetaBBO.

## Deep Themes

- Task-free meta-optimization: optimizers adapt from the target task instead of a curated training distribution.
- Closed-loop optimizer learning: search behavior is learned while optimizing.
- Evolutionary operators as parameterized policies: selection and recombination become learnable mechanisms.
- Zero-shot black-box optimization: meta-learning shifts from pretraining to online adaptation.

## Subthemes

- Meta black-box optimization.
- Online parameter adaptation.
- Evolutionary search patterns.
- UAV path planning.

## Connections to Other Papers

This connects to JitRL and other gradient-free policy improvement work through online adaptation without gradients.

It also relates to optimizer-state papers such as LoRA-Pre, Beyond Muon, and SGD RLVR because all question inherited optimizer assumptions.

## Notes for Cross-Paper Synthesis

ABOM adds an online-adaptation thread: when the task distribution is unknown, optimization itself becomes the data source for learning the optimizer.
