# SVL: Empowering Spiking Neural Networks for Efficient 3D Open-World Understanding

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: Ai3a79cTvr
- Authors: Xuerui Qiu; Shaowei Gu; Peixi Wu; JiaKui Hu; Yaozhi Wen; Yuqi Pan; Xinhao Luo; Bo XU; Guoqi Li
- Primary area: applications->neuroscience_cognitive_science
- Keywords: Vision-language models; Spike-driven; Spike Point Transformer;Spiking Neural Network;
- Source URL: https://openreview.net/forum?id=Ai3a79cTvr
- PDF URL: https://openreview.net/pdf?id=Ai3a79cTvr

## Abstract

Spiking Neural Networks (SNNs) offer an energy--efficient route to 3D spatio--temporal perception, yet they lag behind Artificial Neural Networks (ANNs) due to weak pretraining and heavy inference stacks, limiting generalization and multimodal reasoning (e.g., zero--shot 3D classification and open--world QA). We present a universal \textbf{S}pike--based \textbf{V}ision--\textbf{L}anguage pretraining framework (SVL) that equips SNNs with open--world 3D understanding while preserving end--to--end spike efficiency. SVL comprises two core components: (i) {Multi--scale Triple Alignment} (MTA), a label--free triplet contrastive objective aligning 3D, image, and text; and (ii) {Re--parameterizable Vision--Language Integration} (Rep--VLI), which converts offline text embeddings into lightweight weights for text--encoder--free inference. Moreover, we present the first fully spike--driven point Transformer, {Spike-driven PointFormer}, whose 3D spike--driven self--attention (3D-SDSA) reduces interactions to sparse additions, enabling faster, more efficient training. Extensive experiments show that SVL attains strong zero--shot 3D classification (85.4% top--1) and consistently outperforms prior SNNs on downstream tasks (e.g., +6.1% 3D cls, +2.1% DVS actions, +1.1% detection, +2.1% segmentation) while enabling open--world 3D question answering, sometimes outperforming ANNs. To the best of our knowledge, SVL represents the first scalable, generalizable, and hardware-friendly paradigm for 3D open-world understanding, effectively bridging the gap between SNNs and ANNs in complex open-world understanding tasks.

## One-Sentence Claim

SVL gives spiking neural networks open-world 3D vision-language capabilities through spike-efficient multimodal pretraining and a spike-driven point Transformer.

## Problem

SNNs are energy-efficient for spatio-temporal perception but lag ANNs in pretraining, multimodal reasoning, and open-world generalization for 3D tasks.

## Core Contribution

The paper introduces a spike-based vision-language pretraining framework with Multi-scale Triple Alignment, Re-parameterizable Vision-Language Integration, and Spike-driven PointFormer.

## Method

MTA aligns 3D, image, and text using label-free triplet contrastive learning. Rep-VLI converts offline text embeddings into lightweight weights for text-encoder-free inference. Spike-driven PointFormer uses 3D spike-driven self-attention with sparse additions.

## Experiments and Evidence

The abstract reports 85.4% zero-shot 3D classification top-1, gains over prior SNNs across classification, DVS actions, detection, and segmentation, plus open-world 3D QA that sometimes outperforms ANNs.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition is deferred after repeated rate-limit failures. Details still need checking: hardware energy measurements, pretraining data, QA benchmark construction, ANN baselines, and spike-attention implementation.

## Deep Themes

- Efficient neuromorphic models are being connected to foundation-model-style pretraining.
- Vision-language alignment can transfer open-world semantics into spiking architectures.
- Hardware-friendly inference is becoming compatible with multimodal reasoning goals.

## Subthemes

- Spiking neural networks.
- 3D open-world understanding.
- Vision-language pretraining.
- Spike-driven point Transformer.
- Multiscale alignment.
- Text-encoder-free inference.

## Connections to Other Papers

Connects to CAT-Q, TetraJet-v2, OmniFit, and 3D/spatial intelligence papers through efficient deployment of multimodal capability. It also links to neuroscience/cognitive-science-inspired architectures.

## Notes for Cross-Paper Synthesis

SVL adds an energy-efficient foundation-model theme: open-world multimodal understanding is moving into spike-driven architectures, not only dense ANNs.
