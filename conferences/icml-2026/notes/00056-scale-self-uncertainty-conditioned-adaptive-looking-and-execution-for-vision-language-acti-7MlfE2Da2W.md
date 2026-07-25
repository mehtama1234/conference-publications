# SCALE: Self-uncertainty Conditioned Adaptive Looking and Execution for Vision-Language-Action Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 7MlfE2Da2W
- Authors: Hyeonbeom Choi; Daechul Ahn; Youhan Lee; Taewook Kang; Seongwon Cho; Jonghyun Choi
- Primary area: applications->robotics
- Keywords: Vision-Language-Action Models;Robotic Manipulation
- Source URL: https://openreview.net/forum?id=7MlfE2Da2W
- PDF URL: https://openreview.net/pdf?id=7MlfE2Da2W

## Abstract

Vision-Language-Action (VLA) models have emerged as a promising paradigm for general-purpose robotic control, with test-time scaling (TTS) gaining attention to enhance robustness beyond training. However, existing TTS methods for VLAs require additional training, verifiers, and multiple forward passes, making them impractical for deployment. Moreover, they intervene only at action decoding while keeping visual representations fixed—insufficient under perceptual ambiguity, where reconsidering how to perceive is as important as deciding what to do. To address these limitations, we propose SCALE, a simple inference strategy that jointly modulates visual perception and action based on 'self-uncertainty', inspired by uncertainty-driven exploration in Active Inference theory—requiring no additional training, no verifier, and only a single forward pass. SCALE broadens exploration in both perception and action under high uncertainty, while focusing on exploitation when confident—enabling adaptive execution across varying conditions. Experiments on simulated and real-world benchmarks demonstrate that SCALE improves state-of-the-art VLAs and outperforms existing TTS methods while maintaining single-pass efficiency. Our code is publicly available at https://github.com/snumprlab/scale.

## One-Sentence Claim

SCALE improves VLA test-time robustness by using the model's own uncertainty to adapt both visual attention and action sampling in a single forward pass.

## Problem

Existing test-time scaling for VLA models often requires extra training, verifiers, or multiple rollouts, and usually intervenes only in action decoding while leaving perception fixed under visual ambiguity.

## Core Contribution

The paper proposes a training-free, verifier-free inference strategy that jointly modulates how the model looks and acts based on self-uncertainty.

## Method

SCALE estimates self-uncertainty from the output token distribution, capturing both full distributional ambiguity and decisiveness about the top action. It uses token-level uncertainty to set action sampling temperature and step-level uncertainty to adjust visual-attention temperature.

## Experiments and Evidence

The abstract reports improvements over state-of-the-art VLA models and existing test-time scaling methods on simulated and real-world benchmarks while retaining single-pass efficiency.

## Full-Text Upgrade

The full text frames SCALE as adaptive looking and execution. Under low uncertainty, the policy sharpens visual attention and behaves near-greedily; under high uncertainty, it broadens visual attention and samples more exploratively. This is motivated by Active Inference-style uncertainty-driven exploration and active perception in robotics.

The uncertainty score is designed specifically for autoregressive VLAs. Ordinary entropy only measures distributional spread, while SCALE compares the predicted distribution against low-uncertainty one-hot and high-uncertainty uniform references, giving a bounded continuous signal that reflects both ambiguity and top-1 decisiveness. The method then closes the loop: uncertainty at one step affects both the action token sampled and the visual features used at subsequent steps.

## Limits and Failure Modes

Limits to watch: the method depends on the quality/calibration of the VLA output distribution; exploration under uncertainty can still choose bad actions; and full benchmark details are needed to separate gains from backbone-specific effects.

## Deep Themes

- Test-time control can use internal uncertainty rather than extra verifiers.
- Robust embodied action requires adaptive perception, not only better action decoding.
- Single-pass inference remains important for deployable robot policies.

## Subthemes

- Vision-language-action models.
- Test-time scaling.
- Self-uncertainty.
- Adaptive visual attention.
- Action temperature control.
- Active perception.

## Connections to Other Papers

Connects to BehaviorVLA, HDFlow, and MomaGraph through embodied AI, and to The Tell-Tale Norm and internal-control papers through using endogenous model signals for inference control.

## Notes for Cross-Paper Synthesis

SCALE adds an embodied test-time-control theme: robust robot policies may improve by modulating perception and action jointly from internal uncertainty signals.
