# Privacy-Aware Video Anomaly Detection through Orthogonal Subspace Projection

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: fjUUmUCy9m
- Authors: Lei Wang; Wenxiang Diao; Andrew Busch; Jun Zhou; Yongsheng Gao
- Primary area: general_machine_learning->representation_learning
- Keywords: video anomaly detection;privacy-aware AI;privacy-preserving learning;representation learning;orthogonal projection;feature disentanglement;interpretable machine learning;trustworthy AI
- Source URL: https://openreview.net/forum?id=fjUUmUCy9m
- PDF URL: https://openreview.net/pdf?id=fjUUmUCy9m

## Abstract

Video anomaly detection (VAD) systems often prioritize accuracy while overlooking privacy concerns, limiting their suitability for real-world deployment. We propose the Orthogonal Projection Layer (OPL), a lightweight module that removes task-irrelevant variations to produce representations focused on anomaly-relevant cues. To address privacy risks in human-centered scenarios, we introduce Guided OPL (G-OPL), which suppresses facial attributes using weak supervision from face-presence signals while preserving non-identifying features such as pose and motion. A cosine alignment objective enforces consistent capture and removal of facial information without identity labels or adversarial training. We further present a privacy-aware evaluation framework that jointly assesses detection performance and privacy preservation, and enables analysis of how sensitive information is filtered. Experiments show that embedding privacy constraints into model design reduces sensitive information while maintaining or improving detection accuracy, supporting projection-based architectures as a principled approach for privacy-aware VAD.

## One-Sentence Claim

Orthogonal subspace projection can suppress facial privacy information in video anomaly detection while preserving or improving anomaly-relevant performance.

## Problem

Video anomaly detection is often deployed in human-centered environments where models may encode sensitive identity or facial attributes. Optimizing only detection accuracy makes these systems harder to deploy responsibly.

The paper asks how to build privacy constraints into representation learning without relying on identity labels or adversarial training.

## Core Contribution

The contribution is the Orthogonal Projection Layer (OPL), a lightweight module that removes task-irrelevant variation, and Guided OPL (G-OPL), which uses weak face-presence supervision to suppress facial attributes while preserving pose and motion cues.

It also proposes a privacy-aware evaluation framework that jointly measures anomaly detection and privacy preservation, including analysis of how sensitive information is filtered.

## Method

OPL projects representations into subspaces intended to preserve anomaly-relevant information while removing irrelevant variation. G-OPL guides this projection using weak face-presence signals and a cosine alignment objective that consistently captures and removes facial information.

Because it avoids identity labels and adversarial training, the method is positioned as a lightweight architectural privacy intervention.

## Experiments and Evidence

Evidence reported in the abstract:

- Sensitive facial information reduced.
- Detection accuracy maintained or improved.
- Weak supervision from face-presence signals, not identity labels.
- Cosine alignment objective for capture/removal of facial information.
- Privacy-aware evaluation framework for detection and privacy jointly.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: datasets, privacy probes, anomaly metrics, and whether non-face sensitive attributes remain.

## Limits and Failure Modes

- Face-presence signals address facial privacy but not all sensitive attributes.
- Projection may remove useful anomaly cues when faces are relevant to the event.
- Weak supervision can miss subtle identity leakage.
- Privacy probes may underestimate what stronger attackers can recover.

## Deep Themes

**Privacy can be an architectural constraint.** The paper embeds privacy into the representation pathway rather than treating it as post-hoc filtering.

**Disentanglement is deployment infrastructure.** Useful behavior depends on separating anomaly-relevant pose/motion from sensitive identity cues.

**Evaluation must be multi-objective.** Accuracy without privacy is not sufficient for real-world VAD.

## Subthemes

- Orthogonal Projection Layer.
- Guided privacy projection.
- Face-attribute suppression.
- Privacy-aware anomaly detection.
- Weakly supervised sensitive-feature removal.

## Connections to Other Papers

Connects to CreDRO, Distributional IRL, GFD-EMVC, MoCA, and VenusBench-Mobile. It also relates to unlearning/privacy papers because it removes unwanted information while preserving task function.

## Notes for Cross-Paper Synthesis

This paper contributes to a practical safety/privacy theme: models should be designed to discard sensitive features before deployment pressure makes leakage a governance problem.
