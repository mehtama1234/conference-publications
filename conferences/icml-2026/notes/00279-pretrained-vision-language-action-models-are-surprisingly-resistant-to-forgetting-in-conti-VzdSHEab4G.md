# Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: VzdSHEab4G
- Authors: Huihan Liu; Changyeon Kim; Bo Liu; Minghuan Liu; Yuke Zhu
- Primary area: applications->robotics
- Keywords: continual learning;lifelong learning;robot learning;vision-language-action (VLA) models
- Source URL: https://openreview.net/forum?id=VzdSHEab4G
- PDF URL: https://openreview.net/pdf?id=VzdSHEab4G

## Abstract

Continual learning is a long-standing challenge in robot policy learning, where a policy must acquire new skills over time without catastrophically forgetting previously learned ones. While prior work has extensively studied continual learning in relatively small behavior cloning (BC) policy models trained from scratch, its behavior in modern large-scale pretrained Vision-Language-Action (VLA) models remains underexplored. In this work, we find that pretrained VLAs are remarkably resistant to forgetting compared with smaller policy models trained from scratch. Simple Experience Replay (ER) works surprisingly well on VLAs, sometimes achieving zero forgetting even with a small replay data size. Our analysis reveals that pretraining plays a critical role in downstream continual learning performance: large pretrained models mitigate forgetting with a small replay buffer size while maintaining strong forward learning capabilities. Furthermore, we find that VLAs can retain relevant knowledge from prior tasks despite performance degradation during learning new tasks. This knowledge retention enables rapid recovery of seemingly forgotten skills through finetuning. Together, these insights imply that large-scale pretraining fundamentally changes the dynamics of continual learning, enabling models to continually acquire new skills over time with simple replay.

## One-Sentence Claim

Large pretrained VLA models are far more resistant to continual-learning forgetting than small scratch-trained policies, and simple replay can often preserve prior skills.

## Problem

Robot policies must acquire new skills over time without catastrophically forgetting old ones. Continual learning has mostly been studied in smaller behavior-cloning policies trained from scratch, leaving the dynamics of modern pretrained vision-language-action models unclear.

The paper asks whether large-scale pretraining changes the forgetting and recovery behavior of robot policies.

## Core Contribution

The paper finds that pretrained VLAs are remarkably resistant to forgetting. Simple experience replay works well, sometimes achieving zero forgetting with a small replay buffer, while maintaining forward learning.

It also finds that degraded performance does not necessarily mean relevant knowledge has been erased: VLAs can retain latent prior-task knowledge and rapidly recover skills through finetuning.

## Method

The method is an empirical continual-learning study comparing pretrained VLA models against smaller scratch-trained behavior-cloning policies. It evaluates sequential skill learning, replay-buffer size, forgetting, forward learning, and recovery through additional finetuning.

The central variable is pretraining: the paper isolates how large pretrained representations change adaptation dynamics.

## Experiments and Evidence

Evidence reported in the abstract:

- Pretrained VLAs forget less than smaller policies trained from scratch.
- Simple Experience Replay performs surprisingly well.
- Small replay buffers can sometimes achieve zero forgetting.
- Pretraining supports both retention and forward learning.
- Previously degraded skills can rapidly recover through finetuning, suggesting retained knowledge.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: VLA models, robot task suite, replay sizes, forgetting metrics, and finetuning recovery protocol.

## Limits and Failure Modes

- The conclusion may depend on task similarity and pretraining coverage.
- Replay can preserve old data but may raise storage, privacy, or data-selection constraints.
- "Resistance to forgetting" may not hold for long sequences of diverse skills.
- Rapid recovery is useful but still implies a deployment-time maintenance process.

## Deep Themes

**Pretraining changes continual-learning dynamics.** Large pretrained models may store reusable skill structure that small scratch models never acquire.

**Observed forgetting may mask latent retention.** Performance drops can be recoverable if internal representations remain intact.

**Simple baselines become stronger at foundation-model scale.** Experience replay is not obsolete; pretraining can make it unexpectedly effective.

## Subthemes

- Continual robot learning.
- Experience replay in VLA models.
- Latent skill retention.
- Recovery from apparent forgetting.
- Forward learning under small replay buffers.

## Connections to Other Papers

Connects to Latent Action Supervision, EcoVLA, DLMR, and Scientific Annotation BC through embodied/process learning. It also links to DiSC and continual post-training papers where new knowledge is added while preserving prior capabilities.

## Notes for Cross-Paper Synthesis

This paper adds nuance to the forgetting theme: at foundation-model scale, capability preservation may come less from elaborate continual-learning machinery and more from robust pretrained representations plus modest replay.
