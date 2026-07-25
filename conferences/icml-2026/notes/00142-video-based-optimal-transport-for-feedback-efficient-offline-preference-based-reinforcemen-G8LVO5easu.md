# Video-Based Optimal Transport for Feedback-Efficient Offline Preference-Based Reinforcement Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: G8LVO5easu
- Authors: Tung Minh Luu; Hwanhee Kim; Younghwan Lee; Chang D. Yoo
- Primary area: reinforcement_learning->batchoffline
- Keywords: Preference-based Reinforcement Learning;Offline Reinforcement Learning;Feedback Efficiency;Optimal Transport;Video Foundation Models;Semi-supervised Learning;Robotics
- Source URL: https://openreview.net/forum?id=G8LVO5easu
- PDF URL: https://openreview.net/pdf?id=G8LVO5easu

## Abstract

Conveying complex objectives to reinforcement learning (RL) agents often requires meticulous reward engineering. Preference-based RL (PbRL) offers a promising alternative by learning reward functions from human feedback, but its scalability is hindered by high labeling costs. Inspired by advances in Video Foundation Models (ViFMs), we present Video-based Optimal Transport Preference (VOTP), a semi-supervised framework that learns effective reward functions from only a handful of labels. By leveraging optimal transport to align visual trajectories within the rich representation space of ViFMs, VOTP effectively generates high-fidelity pseudo-labels for large amounts of unlabeled data, substantially reducing human supervision. Extensive experiments across locomotion and manipulation benchmarks demonstrate the superiority of VOTP, which outperforms state-of-the-art offline PbRL methods under limited feedback budgets. We also showcase the robustness of VOTP in the presence of visual distractors and validate its utility on real robotic tasks, where it learns meaningful rewards with minimal human input.

## One-Sentence Claim

VOTP uses video foundation model representations and optimal transport to propagate sparse preference labels into high-quality pseudo-labels for offline preference-based RL.

## Problem

Preference-based RL reduces reward engineering but requires costly human labels, limiting scalability for robotics and complex control tasks.

## Core Contribution

The paper introduces Video-based Optimal Transport Preference, a semi-supervised reward-learning framework for feedback-efficient offline PbRL.

## Method

VOTP aligns visual trajectories in ViFM representation space using optimal transport, then generates pseudo-labels for unlabeled data to train reward functions with only a small number of human labels.

## Experiments and Evidence

The abstract reports superiority over state-of-the-art offline PbRL under limited feedback budgets across locomotion and manipulation, robustness to visual distractors, and validation on real robot tasks.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: ViFM choice, label budget, OT cost definition, pseudo-label noise, and real-robot evaluation scale.

## Deep Themes

- Preference labels can be amplified through representation geometry.
- Video foundation models can reduce human feedback burden in robotics.
- Optimal transport can align trajectories for reward learning.

## Subthemes

- Preference-based RL.
- Offline RL.
- Video foundation models.
- Optimal transport.
- Semi-supervised reward learning.
- Robotics feedback efficiency.

## Connections to Other Papers

Connects to MAPF optimal transport, DreamDojo, RoboMME, RGR-GRPO, and reward-modeling papers through feedback-efficient embodied learning.

## Notes for Cross-Paper Synthesis

VOTP reinforces the representation-as-label-propagation theme: foundation model embeddings can turn scarce human preferences into broader reward supervision.
