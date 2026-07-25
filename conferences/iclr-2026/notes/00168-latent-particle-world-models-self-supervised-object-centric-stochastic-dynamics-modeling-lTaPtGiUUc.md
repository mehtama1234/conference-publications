# Latent Particle World Models: Self-supervised Object-centric Stochastic Dynamics Modeling

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: lTaPtGiUUc
- Authors: Tal Daniel; Carl Qi; Dan Haramati; Amir Zadeh; Chuan Li; Aviv Tamar; Deepak Pathak; David Held
- Primary area: unsupervised, self-supervised, semi-supervised, and supervised representation learning
- Keywords: World Model;Self-supervised;unsupervised;object-centric;video prediciton;video generation;imitation learning;latent particles;vae
- Source URL: https://openreview.net/forum?id=lTaPtGiUUc
- PDF URL: https://openreview.net/pdf?id=lTaPtGiUUc

## Abstract

We introduce Latent Particle World Model (LPWM), a self-supervised object-centric world model scaled to real-world multi-object datasets and applicable in decision-making. LPWM autonomously discovers keypoints, bounding boxes, and object masks directly from video data, enabling it to learn rich scene decompositions without supervision. Our architecture is trained end-to-end purely from videos and supports flexible conditioning on actions, language, and image goals. LPWM models stochastic particle dynamics via a novel latent action module and achieves state-of-the-art results on diverse real-world and synthetic datasets. Beyond stochastic video modeling, LPWM is readily applicable to decision-making, including goal-conditioned imitation learning, as we demonstrate in the paper. Code, and pre-trained models will be made publicly available. Video rollouts are available: https://sites.google.com/view/lpwm

## One-Sentence Claim

LPWM learns object-centric stochastic world models from videos by discovering latent particles, object masks, boxes, and keypoints without supervision, then uses those dynamics for generation and decision-making.

## Problem

World models need structured scene decompositions to handle multi-object dynamics and decision-making, but supervised object annotations are costly and many models do not scale well to real-world video. The challenge is learning object-centric stochastic dynamics directly from raw video.

## Core Contribution

The paper introduces Latent Particle World Model, a self-supervised architecture that discovers object-centric representations from video, supports conditioning on actions, language, and image goals, and applies the learned dynamics to video modeling and goal-conditioned imitation learning.

## Method

LPWM trains end to end on videos and autonomously identifies keypoints, bounding boxes, and object masks. It represents scene entities as latent particles and models stochastic dynamics with a latent action module, allowing flexible conditioning for prediction, generation, and control.

## Experiments and Evidence

The abstract reports state-of-the-art performance on diverse real-world and synthetic datasets, plus applicability to decision-making through goal-conditioned imitation learning. Code, pretrained models, and video rollouts are planned for release.

## Limits and Failure Modes

Object-centric discovery can struggle with occlusion, object permanence, deformable objects, camera motion, and ambiguous part/object boundaries. Decision-making quality may depend on whether learned particles preserve task-relevant causal state. Full-text review should check datasets, supervision leakage, rollout horizons, conditioning mechanisms, imitation-learning setup, and ablations on latent actions.

## Deep Themes

- Self-supervised object-centric world modeling.
- Latent particles as scene state.
- Stochastic video dynamics.
- World models for decision-making.

## Subthemes

- Keypoint, box, and mask discovery.
- Latent action modules.
- Flexible action/language/image-goal conditioning.
- Goal-conditioned imitation learning.
- Real-world multi-object video modeling.

## Connections to Other Papers

Connects to MomaGraph and Vid-LLM through structured scene representations, to ExDM and AIGB-Pearl through generative models for control, and to embodied/robotics papers where world models support planning or imitation.

## Notes for Cross-Paper Synthesis

LPWM fits a strong corpus theme: useful world models are increasingly object-structured and decision-aware. The representation is not just predictive; it is designed to expose entities and dynamics that downstream policies can use.
