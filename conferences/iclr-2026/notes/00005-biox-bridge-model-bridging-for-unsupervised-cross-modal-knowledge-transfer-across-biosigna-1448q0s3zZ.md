# BioX-Bridge: Model Bridging for Unsupervised Cross-Modal Knowledge Transfer across Biosignals

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 1448q0s3zZ
- Authors: Chenqi Li; Yu Liu; Timothy Denison; Tingting Zhu
- Primary area: applications to physical sciences (physics, chemistry, biology, etc.)
- Keywords: biosignal;ai for healthcare;humans and ai;unsupervised cross-modal knowledge transfer
- Source URL: https://openreview.net/forum?id=1448q0s3zZ
- PDF URL: https://openreview.net/pdf?id=1448q0s3zZ

## Abstract

Biosignals offer valuable insights into the physiological states of the human body. Although biosignal modalities differ in functionality, signal fidelity, sensor comfort, and cost, they are often intercorrelated, reflecting the holistic and interconnected nature of human physiology. This opens up the possibility of performing the same tasks using alternative biosignal modalities, thereby improving the accessibility, usability, and adaptability of health monitoring systems. However, the limited availability of large labeled datasets presents challenges for training models tailored to specific tasks and modalities of interest. Unsupervised cross-modal knowledge transfer offers a promising solution by leveraging knowledge from an existing modality to support model training for a new modality. Existing methods are typically based on knowledge distillation, which requires running a teacher model alongside student model training, resulting in high computational and memory overhead. This challenge is further exacerbated by the recent development of foundation models that demonstrate superior performance and generalization across tasks at the cost of large model sizes. To this end, we explore a new framework for unsupervised cross-modal knowledge transfer of biosignals by training a lightweight bridge network to align the intermediate representations and enable information flow between foundation models and across modalities. Specifically, we introduce an efficient strategy for selecting alignment positions where the bridge should be constructed, along with a flexible prototype network as the bridge architecture. Extensive experiments across multiple biosignal modalities, tasks, and datasets show that BioX-Bridge reduces the number of trainable parameters by 88-99\% while maintaining or even improving transfer performance compared to state-of-the-art methods.

## One-Sentence Claim

BioX-Bridge transfers knowledge across biosignal modalities by learning lightweight bridges between foundation-model representations, reducing trainable parameters by 88-99% while preserving or improving transfer performance.

## Problem

Biosignal modalities are physiologically related but differ in cost, comfort, fidelity, and availability. Many desired target modalities lack large labeled datasets, while teacher-student distillation from foundation models can be computationally heavy.

## Core Contribution

The paper proposes an unsupervised cross-modal transfer framework that aligns intermediate representations through a lightweight bridge network rather than running a full teacher during student training.

## Method

BioX-Bridge selects representation-alignment positions inside models and uses a flexible prototype bridge network to allow information flow between foundation models and biosignal modalities.

## Experiments and Evidence

The abstract claims experiments across multiple biosignal modalities, tasks, and datasets, with 88-99% fewer trainable parameters and state-of-the-art or better transfer performance. The PDF should be checked for modality set, target tasks, baselines, and whether transfer holds under real sensor noise.

## Limits and Failure Modes

Likely limits include dependence on representation compatibility between modalities, possible degradation when physiology correlations are weak, and unknown robustness across sensor hardware, patient populations, or clinical deployment settings.

## Deep Themes

- Foundation models are being adapted through small interfaces rather than full retraining.
- Scientific/medical domains stress sample efficiency and modality transfer.
- Efficiency, accessibility, and healthcare usability are linked.

## Subthemes

- Cross-modal transfer.
- Biosignal foundation models.
- Lightweight bridging networks.
- Unsupervised healthcare adaptation.
- Parameter-efficient transfer.

## Connections to Other Papers

Connects to LoRA/adapters, subspace training, multimodal grounding, and scientific-domain adaptation. It is a biological-signal analogue of broader bridge/adaptation strategies for foundation models.

## Notes for Cross-Paper Synthesis

This paper supports a recurring pattern: instead of training a new large model for every modality or domain, 2026 work often learns compact translation layers between existing representational spaces.
