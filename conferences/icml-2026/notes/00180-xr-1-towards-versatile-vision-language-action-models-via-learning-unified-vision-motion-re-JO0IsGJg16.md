# XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: JO0IsGJg16
- Authors: Shichao Fan; Kun Wu; Zhengping Che; Xinhua Wang; Di Wu; Fei Liao; Ning Liu; Yixue Zhang; Zhen Zhao; Zhiyuan Xu; Meng Li; Qingjie Liu; Shanghang Zhang; Min Wan; Jian Tang
- Primary area: applications->robotics
- Keywords: Embodied AI;Imitation learning;VLA
- Source URL: https://openreview.net/forum?id=JO0IsGJg16
- PDF URL: https://openreview.net/pdf?id=JO0IsGJg16

## Abstract

Recent progress in large-scale robotic datasets and vision-language models (VLMs) has advanced research on vision-language-action (VLA) models.  However, existing VLA models still face two fundamental challenges: (\textit{i}) producing precise low-level actions from high-dimensional observations, (\textit{ii}) bridging domain gaps across heterogeneous data sources, including diverse robot embodiments and human demonstrations. Existing methods often encode latent variables from either visual dynamics or robotic actions to guide policy learning, but they fail to fully exploit the complementary multi-modal knowledge present in large-scale, heterogeneous datasets. In this work, we present \textbf{XR-1}, a novel framework for versatile and scalable VLA learning across diverse robots, tasks, and environments.
At its core, XR-1 introduces the \emph{Unified Vision-Motion Codes (UVMC)}, a discrete latent representation learned via a dual-branch VQ-VAE that jointly encodes visual dynamics and robotic motion.  UVMC addresses these challenges by (\textit{i}) serving as an intermediate representation between the observations and actions, and  (\textit{ii}) aligning multimodal dynamic information from heterogeneous data sources to capture complementary knowledge. To effectively exploit UVMC, we propose a \emph{three-stage training paradigm}: (\textit{i}) self-supervised UVMC learning, (\textit{ii}) UVMC-guided pretraining on large-scale cross-embodiment robotic datasets, and (\textit{iii}) task-specific post-training.  We validate XR-1 through extensive real-world experiments with more than 12,000 rollouts on six different robot embodiments, spanning over 120 diverse manipulation tasks. XR-1 consistently outperforms state-of-the-art baselines such as $\pi_0$ and GR00T-N1.5 while demonstrating strong generalization to novel objects, background variations, distractors, and illumination changes. Our project is at \href{https://xr-1-vla.github.io/}{https://xr-1-vla.github.io/}.

## One-Sentence Claim

XR-1 learns unified discrete vision-motion codes to bridge heterogeneous robot and human demonstration data for scalable vision-language-action policy learning.

## Problem

VLA models struggle to produce precise low-level actions from high-dimensional observations and to bridge domain gaps across robot embodiments, environments, and human demonstrations.

## Core Contribution

The paper introduces Unified Vision-Motion Codes, learned with a dual-branch VQ-VAE, plus a three-stage training pipeline for cross-embodiment VLA learning.

## Method

XR-1 first learns UVMC self-supervised from visual dynamics and robotic motion, then uses the codes to guide pretraining on large heterogeneous cross-embodiment datasets, followed by task-specific post-training.

## Experiments and Evidence

The abstract reports more than 12,000 real-world rollouts on six robot embodiments across 120 manipulation tasks, outperforming baselines including pi_0 and GR00T-N1.5 and generalizing to new objects, backgrounds, distractors, and illumination changes.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: dataset composition, robot embodiments, policy architecture, rollout protocol, failure rates, human-demo alignment, and whether discrete codes bottleneck fine motor control.

## Deep Themes

- Intermediate representations bridge perception, language, and action.
- Cross-embodiment robotics needs shared latent structure across heterogeneous data.
- Large-scale real-world rollout evidence is becoming central for VLA claims.

## Subthemes

- Vision-language-action models.
- Embodied AI.
- Imitation learning.
- VQ-VAE codes.
- Cross-embodiment pretraining.
- Manipulation generalization.

## Connections to Other Papers

Connects to 3ViewSense, VGGT-Motion, VOTP, Posterior Behavioral Cloning, and spatial/robotics papers through embodied representations, low-level control, and adaptation from heterogeneous data.

## Notes for Cross-Paper Synthesis

XR-1 adds a robotics-scale example of the intermediate-code theme: versatile embodied models may depend on learned latent interfaces that align visual dynamics with action across embodiments.
