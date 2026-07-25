# OXE-AugE: A Large-Scale Robot Augmentation of OXE for Scaling Cross-Embodiment Policy Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: LcswwEzzX7
- Authors: Guanhua Ji; Harsha Polavaram; Lawrence Yunliang Chen; Sandeep Bajamahal; Zehan Ma; Simeon Adebola; Chenfeng Xu; Ken Goldberg
- Primary area: applications->robotics
- Keywords: robot learning;scaling;augmentation
- Source URL: https://openreview.net/forum?id=LcswwEzzX7
- PDF URL: https://openreview.net/pdf?id=LcswwEzzX7

## Abstract

Large and diverse datasets are needed for training generalist robot policies that can control a variety of robot embodiments--robot arm and gripper combinations--across diverse tasks and environments. As re-collecting demonstrations and retraining for each new embodiment are prohibitively costly, we study whether existing robot data can be augmented to improve transfer and generalization across embodiments. The Open X-Embodiment (OXE) dataset, which aggregates demonstrations from over 60 robot datasets, has been widely used for training generalist policies. However, it is highly imbalanced: the top four robot types account for over 85% of its real data, which risks overfitting to robot--scene combinations. We present AugE-Toolkit, a scalable robot augmentation pipeline, and OXE-AugE, a high-quality open-source dataset that augments OXE with 9 different robot embodiments. OXE-AugE provides over 4.4 million trajectories, more than triple the size of the original OXE. We conduct a systematic study of how scaling robot augmentation impacts cross-embodiment learning. Results suggest that augmenting datasets with diverse arms and grippers improves policy performance not only on the augmented robots, but also on unseen robots and even the original robots under distribution shifts. In physical experiments, fine-tuning generalist policies such as OpenVLA and $\pi_0$ on OXE-AugE improves success rates by 24-45% on unseen robot-gripper combinations across four real-world manipulation tasks. Project website: https://OXE-AugE.github.io/.

## One-Sentence Claim

OXE-AugE scales cross-embodiment robot policy learning by augmenting Open X-Embodiment data with diverse arms and grippers, improving transfer to unseen robots and distribution shifts.

## Problem

Generalist robot policies need broad embodiment diversity, but collecting new demonstrations is expensive and OXE is imbalanced, with four robot types comprising more than 85% of real data.

## Core Contribution

The paper introduces AugE-Toolkit and OXE-AugE, an open-source augmented robot dataset with nine robot embodiments and over 4.4 million trajectories, more than tripling the original OXE size.

## Method

The augmentation pipeline transforms existing robot demonstrations across diverse arm/gripper embodiments, then evaluates how scaling augmentation affects cross-embodiment policy learning and fine-tuning of generalist policies.

## Experiments and Evidence

The abstract reports improved performance on augmented robots, unseen robots, and original robots under distribution shift. Physical experiments fine-tuning OpenVLA and pi_0 on OXE-AugE improve success rates by 24-45% on unseen robot-gripper combinations across four manipulation tasks.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: augmentation realism, embodiment mapping assumptions, task diversity, physical evaluation setup, sim-to-real effects, and whether augmented data introduces kinematic artifacts.

## Deep Themes

- Data augmentation can rebalance embodiment coverage for generalist robotics.
- Cross-embodiment transfer depends on diverse robot morphology, not only task diversity.
- Existing demonstrations can be reused to reduce collection and retraining costs.

## Subthemes

- Robot learning.
- Open X-Embodiment.
- Cross-embodiment policy learning.
- Data augmentation.
- Generalist policies.
- Real-world manipulation.

## Connections to Other Papers

Connects to XR-1, VOTP, Posterior Behavioral Cloning, and APB through robotics transfer, policy adaptation, and data diversity for embodied systems.

## Notes for Cross-Paper Synthesis

OXE-AugE adds a data-scaling robotics theme: embodied generalization may require actively reshaping dataset embodiment balance, not only increasing total demonstrations.
