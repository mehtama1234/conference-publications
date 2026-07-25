# TimeRewarder: Learning Dense Reward from Passive Videos via Frame-wise Temporal Distance

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: XztRm216YS
- Authors: Yuyang Liu; Chuan Wen; Yihang Hu; Dinesh Jayaraman; Yang Gao
- Primary area: reinforcement_learning
- Keywords: Reward Learning;Robotic Manipulation;Vision-based RL
- Source URL: https://openreview.net/forum?id=XztRm216YS
- PDF URL: https://openreview.net/pdf?id=XztRm216YS

## Abstract

Designing dense rewards is crucial for reinforcement learning (RL), yet in robotics it often demands extensive manual effort and lacks scalability. One promising solution is to view task progress as a dense reward signal, as it quantifies the degree to which actions advance the system toward task completion over time. We present TimeRewarder, a simple yet effective reward learning method that derives progress estimation signals from passive videos, including robot demonstrations and human videos, by modeling temporal distances between frame pairs. We then demonstrate how TimeRewarder can supply step-wise proxy rewards to guide reinforcement learning. In our comprehensive experiments on ten challenging Meta-World tasks, we show that TimeRewarder dramatically improves RL for sparse-reward tasks, achieving nearly perfect success in 9/10 tasks with only 200,000 interactions per task with the environment. This approach outperforms previous methods and even the manually designed environment dense reward on both the final success rate and sample efficiency. Moreover, we show that TimeRewarder pretraining can exploit real-world human videos, highlighting its potential as a scalable approach to rich reward signals from diverse video sources.

## One-Sentence Claim

TimeRewarder learns dense robotic RL rewards from passive video by estimating temporal progress through frame-wise temporal distance.

## Problem

Dense reward design is crucial for reinforcement learning but expensive and hard to scale in robotics. Sparse rewards often make exploration inefficient, while manually engineered dense rewards require task-specific effort and may not transfer.

The paper asks whether task progress can be learned from passive videos, including demonstrations and human videos, and converted into step-wise proxy rewards for RL.

## Core Contribution

The paper introduces TimeRewarder, a reward-learning method that models temporal distances between video frame pairs to estimate progress. These progress estimates become dense proxy rewards for reinforcement learning.

The method can pretrain from real-world human videos, suggesting a route to scalable reward signals beyond robot-collected demonstrations.

## Method

TimeRewarder learns a temporal-distance model over frame pairs from passive videos. If two frames are far apart in task time, the model infers progress; during RL, current observations are scored by their estimated temporal advancement toward task completion.

This converts unlabeled video ordering into a dense reward function.

## Experiments and Evidence

Evidence reported in the abstract:

- Ten challenging Meta-World tasks.
- Nearly perfect success on 9 of 10 sparse-reward tasks.
- Only 200,000 environment interactions per task.
- Outperforms previous methods and manually designed dense environment rewards in success and sample efficiency.
- Pretraining can exploit real-world human videos.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: video sources, temporal-distance objective, reward shaping formula, Meta-World task list, and sim-to-real assumptions.

## Limits and Failure Modes

- Temporal progress in videos may not align with causal action quality.
- Human videos may differ from robot embodiments and camera viewpoints.
- Tasks with non-monotonic progress or required backtracking could confuse distance-based rewards.
- Learned rewards may be exploitable unless grounded in task success checks.

## Deep Themes

**Passive video can become reward infrastructure.** Temporal order supplies supervision without manual reward engineering.

**Progress is a dense latent variable.** Reward is estimated as advancement through task time rather than hand-coded state distance.

**Embodied learning is borrowing from observational data.** Human videos become useful even without robot actions.

## Subthemes

- Frame-wise temporal distance.
- Dense reward learning.
- Passive human/robot videos.
- Sparse-reward manipulation.
- Sample-efficient vision-based RL.

## Connections to Other Papers

Connects to Latent Action Supervision, Continual VLA Forgetting, SceneSmith, and Scientific Annotation BC through trajectory/process supervision. It also links to R2VPO and PAVE through RL signal design and stability.

## Notes for Cross-Paper Synthesis

TimeRewarder adds to the process-data theme: ordered observations can supervise control even when explicit actions, rewards, or labels are unavailable.
