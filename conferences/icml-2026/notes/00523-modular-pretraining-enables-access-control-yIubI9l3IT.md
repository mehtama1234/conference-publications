# Modular Pretraining Enables Access Control

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: yIubI9l3IT
- Authors: Ethan Roland; Murat Cubuktepe; Erick Martinez; Stijn Servaes; Keenan Pepper; Michael Vaiana; Diogo S de Lucena; Judd Rosenblatt; Addie Foote; Cem Anil; Alex Cloud
- Primary area: deep_learning
- Keywords: Modularity;Safety;Access Control;Unlearning;Pretraining
- Source URL: https://openreview.net/forum?id=yIubI9l3IT
- PDF URL: https://openreview.net/pdf?id=yIubI9l3IT

## Abstract

AI developers face a dual-use dilemma. A model capability that helps one user cure a disease can help another synthesize one. This dilemma could be resolved with access control, limiting dual-use AI capabilities to trusted deployments with a legitimate need. A gold standard for access control would be to serve separate models with different capabilities to different users. However, training and deploying multiple models is prohibitively expensive. To address this challenge, we propose gradient-routed auxiliary modules (GRAM), a pre-training method that adds modules to a neural network and selectively updates them to induce specialization. Ablating a module at inference time removes its capability from the network, approximating a model trained on filtered data. We evaluate GRAM on synthetic stories and realistic dual-use data spanning virology, cybersecurity, nuclear physics, and specialized code. These experiments show that GRAM preserves selected retain capabilities while disabling forgotten capabilities, and limits recovery better than post-hoc unlearning. Most importantly, a Chinchilla-optimal scaling analysis from 50M to 5B parameters shows that the forget capability gap between data-filtered and full-data models widens with scale while the retain gap stays constant, and that GRAM closely tracks data filtering. GRAM's training cost is independent of the number of supported capability profiles, yielding a 5x cost reduction in our 5-profile setting.

## One-Sentence Claim

Gradient-routed auxiliary modules enable scalable capability access control by making selected pretrained capabilities removable at inference time through module ablation.

## Problem

Dual-use capabilities create an access-control dilemma: the same model capability can support legitimate work and harmful misuse. Serving separate filtered models for different users would be ideal but too expensive.

Post-hoc unlearning often struggles to remove capabilities robustly, especially as models scale.

## Core Contribution

The paper proposes GRAM, a modular pretraining method that adds auxiliary modules and selectively updates them to induce capability specialization.

Ablating a module at inference time removes its associated capability, approximating a model trained on filtered data while avoiding separate full pretraining runs for each capability profile.

## Method

GRAM uses gradient routing during pretraining so different auxiliary modules specialize around different capabilities or data regions. At deployment, modules can be enabled or disabled depending on access rights.

The training cost is independent of the number of supported capability profiles, making multiple access tiers cheaper than training multiple separate models.

## Experiments and Evidence

The abstract reports experiments on synthetic stories and realistic dual-use data spanning virology, cybersecurity, nuclear physics, and specialized code.

GRAM preserves retained capabilities while disabling forgotten capabilities, limits recovery better than post-hoc unlearning, and tracks data filtering in a Chinchilla-optimal scaling analysis from 50M to 5B parameters. In a five-profile setting it gives a reported 5x cost reduction.

## Limits and Failure Modes

Access control through module ablation depends on clean capability localization. Capabilities may be entangled, recoverable through prompting or finetuning, or partially present in the shared backbone.

Because this note is abstract-only, details still need checking: module architecture, routing rule, access-profile construction, recovery attacks, retain/forget metrics, scaling-law setup, and whether ablation causes hidden degradation on adjacent benign tasks.

## Deep Themes

- Capability-level access control: safety can be enforced by serving different capability subsets.
- Modular pretraining: capability boundaries are shaped during training, not repaired afterward.
- Unlearning versus data filtering: robust removal is benchmarked against the gold standard of never training on restricted data.
- Scalable governance: one model can support multiple deployment profiles if capabilities are modular enough.

## Subthemes

- Gradient-routed auxiliary modules.
- Dual-use capability profiles.
- Inference-time module ablation.
- Scaling behavior of retain and forget gaps.

## Connections to Other Papers

This connects to GoodDiffusion through proactive access control inside generative systems. It also connects to unlearning, copyright, and robust safety papers because it treats governance as a training-time architectural property.

It relates to ScaleMoE and modular expert routing because modularity becomes both a systems tool and a safety-control mechanism.

## Notes for Cross-Paper Synthesis

This paper is a major access-control anchor: it reframes safety from "remove bad behavior after training" to "pretrain capability compartments that can be served selectively."
