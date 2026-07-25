# Decision Transformers As Zero-Shot Learners via Text-Behavior Alignment

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: jqLPUccarO
- Authors: Xin Zhang; Jonathan Martinez; Yanhua Li; Yingxue Zhang
- Primary area: reinforcement_learning->batchoffline
- Keywords: Offline meta RL
- Source URL: https://openreview.net/forum?id=jqLPUccarO
- PDF URL: https://openreview.net/pdf?id=jqLPUccarO

## Abstract

Offline meta-reinforcement learning (meta-RL) aims to train agents that can generalize to unseen tasks using pre-collected data from related tasks. Recent approaches leverage the scalability of transformer architectures to model behavior sequences and support task adaptation using target task demonstrations. However, such data is often unavailable in real-world settings, where the task objective may be known but cannot be easily demonstrated. In contrast, humans routinely interpret and perform new tasks based solely on natural language instructions. In this work, we explore the potential of using natural language task descriptions to enable zero-shot task adaptation in offline meta-RL without requiring any data from the target task. We propose the Text-Guided Decision Transformer (TG-DT), a framework that enables zero-shot generalization by grounding policy learning in natural language. TG-DT learns a shared embedding space between task descriptions and behavioral trajectories via a dual contrastive and matching-based objective, ensuring robust alignment. A transformer-based policy is then conditioned on these aligned representations to generate task-appropriate actions. At test time, TG-DT synthesizes policies for unseen tasks using only their text descriptions and can optionally leverage a description-guided data sharing strategy to enhance adaptation. Experiments on standard offline meta-RL benchmarks, including MuJoCo and Meta-World, demonstrate that TG-DT achieves strong generalization to unseen tasks.

## One-Sentence Claim

Text-Guided Decision Transformers enable zero-shot offline meta-RL by aligning natural-language task descriptions with behavioral trajectories.

## Problem

Offline meta-RL aims to generalize to unseen tasks using data from related tasks. Many Transformer-based approaches still need target-task demonstrations at adaptation time, which may be unavailable even when a natural-language objective is known.

The paper asks whether text descriptions alone can condition offline RL policies for unseen tasks.

## Core Contribution

The contribution is TG-DT, a Text-Guided Decision Transformer that learns a shared embedding space between task descriptions and behavioral trajectories. The aligned representation lets the policy generate task-appropriate actions for unseen tasks from text alone.

The method optionally uses description-guided data sharing to enhance adaptation without target demonstrations.

## Method

TG-DT uses dual contrastive and matching-based objectives to align natural-language descriptions with behavior trajectories. A Transformer policy conditions on these aligned embeddings to produce actions.

At test time, the system receives only a text description of a new task and synthesizes a corresponding policy behavior.

## Experiments and Evidence

Evidence reported in the abstract:

- Zero-shot task adaptation without target-task data.
- Shared embedding between task descriptions and behavioral trajectories.
- Dual contrastive and matching-based alignment objective.
- Optional description-guided data sharing.
- Strong generalization on MuJoCo and Meta-World offline meta-RL benchmarks.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: description generation, task split, baseline comparison, and language ambiguity.

## Limits and Failure Modes

- Natural-language descriptions may omit control-relevant details.
- Alignment can overfit benchmark task phrasing.
- Zero-shot behavior may fail when text describes tasks outside the offline data support.
- Decision Transformer conditioning may struggle with long-horizon sparse rewards.

## Deep Themes

**Language becomes a policy interface.** Text replaces target demonstrations as the adaptation signal.

**Behavior and descriptions need shared geometry.** Generalization depends on aligning trajectory space with semantic task space.

**Offline RL is absorbing foundation-model conditioning patterns.** Decision Transformers become instruction-conditioned policies.

## Subthemes

- Text-guided Decision Transformers.
- Offline meta-RL.
- Zero-shot task adaptation.
- Text-behavior contrastive alignment.
- Description-guided data sharing.

## Connections to Other Papers

Connects to EcoVLA, Agent0-VL, PRISM, VideoKR, and style-conditioned offline RL. It also links to FutureCAD because both use language to control structured action generation.

## Notes for Cross-Paper Synthesis

TG-DT extends the language-grounding theme into offline control: natural language is increasingly used as a compact, human-authored task specification for policies.
