# Instilling an Active Mind in Avatars via Cognitive Simulation

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 80JylHgQn1
- Authors: Jianwen Jiang; Weihong Zeng; Zerong Zheng; Jiaqi Yang; Chao Liang; Wang Liao; Han Liang; Weifeng Chen; XING WANG; Yuan Zhang; Mingyuan Gao
- Primary area: applications to computer vision, audio, language, and other modalities
- Keywords: Video Generatio;Human Animation;Avatar;Multimedia
- Source URL: https://openreview.net/forum?id=80JylHgQn1
- PDF URL: https://openreview.net/pdf?id=80JylHgQn1

## Abstract

Current video avatar models can generate fluid animations but struggle to capture a character's authentic essence, primarily synchronizing motion with low-level audio cues instead of understanding higher-level semantics like emotion or intent. To bridge this gap, we propose a novel framework for generating character animations that are not only physically plausible but also semantically rich and expressive. Our model is built on two technical innovations. First, we employ Multimodal Large Language Models to generate a structured textual representation from input conditions, providing high-level semantic guidance for creating contextually and emotionally resonant actions. Second, to ensure robust fusion of multimodal signals, we introduce a specialized Multimodal Diffusion Transformer architecture featuring a novel Pseudo Last Frame design. This allows our model to accurately interpret the joint semantics of audio, images and text, generating motions that are deeply coherent with the overall context. Comprehensive experiments validate the superiority of our method, which achieves compelling results in lip-sync accuracy, video quality, motion naturalness, and semantic consistency. The approach also shows strong generalization to challenging scenarios, including multi-person and non-human subjects. Our video results are linked in https://omnihuman-lab.github.io/v1_5/ .

## One-Sentence Claim

The paper improves avatar animation by adding high-level cognitive-semantic simulation so motion reflects emotion, intent, and context rather than only low-level audio cues.

## Problem

Current video-avatar systems can produce fluid animation and lip-sync, but often miss the character's authentic expressive essence. They primarily synchronize motion to low-level audio features rather than understanding semantic context.

The problem is to generate avatar motion that is physically plausible and semantically aligned with emotion, intent, and multimodal context.

## Core Contribution

The paper proposes a framework for semantically rich character animation built on two innovations: MLLM-generated structured textual representations as high-level guidance, and a Multimodal Diffusion Transformer with a Pseudo Last Frame design for robust multimodal fusion.

The contribution is to put cognitive simulation between raw input conditions and motion generation.

## Method

The system uses multimodal large language models to transform input conditions into structured textual guidance. This guidance encodes high-level context and emotion for action generation.

A specialized Multimodal Diffusion Transformer combines audio, images, and text. The Pseudo Last Frame design helps the model interpret joint semantics and generate context-coherent motion.

## Experiments and Evidence

The abstract reports improvements in lip-sync accuracy, video quality, motion naturalness, and semantic consistency.

It also reports generalization to challenging scenarios including multi-person and non-human subjects.

## Limits and Failure Modes

Semantic animation quality may depend heavily on the MLLM's interpretation of intent and emotion. Misread context could produce plausible but wrong expressions.

Because this note is abstract-only, details still need checking: dataset, evaluation metrics, human-study design, MLLM prompting, diffusion architecture, Pseudo Last Frame mechanics, and failure cases for ambiguous emotions.

## Deep Themes

- Cognitive simulation for generation: high-level intent representations guide low-level motion.
- Semantic control of avatars: expressive animation requires more than audio synchrony.
- Multimodal fusion under temporal constraints: audio, image, and text signals must align in generated video.
- Generalized embodiment: avatar methods are tested beyond single human talking heads.

## Subthemes

- MLLM-generated structured guidance.
- Multimodal Diffusion Transformer.
- Pseudo Last Frame design.
- Emotion and intent-aware animation.

## Connections to Other Papers

This connects to MetaphorVU and Learning-to-Theorize through high-level semantic interpretation over video. It also relates to PanoWorld-X, VectorWorld, and EgoTactile through generative models that must preserve physical or expressive coherence over time.

It fits the multimodal embodied generation cluster, especially where latent semantics control visible motion.

## Notes for Cross-Paper Synthesis

This paper adds a semantic embodiment thread: generated agents and avatars need internal high-level state, not just surface-level motion alignment.
