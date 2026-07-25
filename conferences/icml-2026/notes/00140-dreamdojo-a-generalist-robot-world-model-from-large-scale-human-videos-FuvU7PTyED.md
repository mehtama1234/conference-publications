# DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: FuvU7PTyED
- Authors: Shenyuan Gao; William Liang; Kaiyuan Zheng; Ayaan Naveed Malik; Seonghyeon Ye; Sihyun Yu; Wei-Cheng Tseng; Yuzhu Dong; Kaichun Mo; Chen-Hsuan Lin; Jiannan Xiang; Yuqi Xie; Ruijie Zheng; Dantong Niu; Pooya Jannaty; Jinwei Gu; Jun Zhang; Jitendra Malik; Pieter Abbeel; Ming-Yu Liu; Yuke Zhu; Joel Jang; Linxi Fan
- Primary area: applications->robotics
- Keywords: World Model;Human Video;Robot Manipulation
- Source URL: https://openreview.net/forum?id=FuvU7PTyED
- PDF URL: https://openreview.net/pdf?id=FuvU7PTyED

## Abstract

Being able to simulate the outcomes of actions in varied environments will revolutionize the development of generalist agents at scale. However, modeling these world dynamics, especially for dexterous robotics tasks, poses significant challenges due to limited data coverage and scarce action labels. As an endeavor towards this end, we introduce DreamDojo, a foundation world model that learns diverse interactions and dexterous controls from 44k hours of egocentric human videos. Our data mixture represents the largest video dataset to date for world model pretraining, spanning a wide range of daily scenarios with diverse objects and skills. To address the scarcity of action labels, we introduce continuous latent actions as unified proxy actions, enhancing interaction knowledge transfer from unlabeled videos. After post-training on small-scale target robot data, DreamDojo demonstrates a strong understanding of physics and precise action controllability. We also devise a distillation pipeline that accelerates DreamDojo to a real-time speed of 10.93 FPS and further improves consistency to the context. Our work enables several important applications based on generative world models, including live teleoperation, policy evaluation, and model-based planning. Systematic evaluation on multiple challenging out-of-distribution (OOD) benchmarks verifies the significance of our method for simulating open-world, contact-rich tasks, paving the way for general-purpose robot world models.

## One-Sentence Claim

DreamDojo learns a generalist robot world model from 44k hours of egocentric human video using continuous latent actions as proxy controls for unlabeled interaction data.

## Problem

Robot world models need broad interaction coverage and action labels, but dexterous robotics data is limited and large human-video corpora usually lack robot action annotations.

## Core Contribution

The paper introduces a foundation world model pretrained on large-scale human videos, post-trained on small robot datasets, and distilled for real-time use.

## Method

DreamDojo uses continuous latent actions as unified proxy actions to transfer interaction knowledge from unlabeled videos, then post-trains on target robot data and distills the model to 10.93 FPS.

## Experiments and Evidence

The abstract reports strong physics understanding, precise action controllability, applications to live teleoperation, policy evaluation, and model-based planning, and OOD benchmarks for contact-rich open-world tasks.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: human-video data mix, latent action learning, robot post-training scale, evaluation metrics, and safety of generated rollouts.

## Deep Themes

- Human video can be a substrate for robot world-model pretraining.
- Latent actions can bridge unlabeled human interactions and robot control.
- Real-time distillation turns world models into interactive robotics infrastructure.

## Subthemes

- Robot world models.
- Egocentric human video.
- Latent actions.
- Dexterous manipulation.
- Policy evaluation.
- Model-based planning.

## Connections to Other Papers

Connects to dWorldEval, RoboMME, SAW-Bench, SpatioLM, and SVL through embodied world modeling and physically grounded evaluation.

## Notes for Cross-Paper Synthesis

DreamDojo strengthens the human-video-to-robotics theme: broad human interaction data may bootstrap generalist robot simulators when action labels are replaced by learned latent controls.
