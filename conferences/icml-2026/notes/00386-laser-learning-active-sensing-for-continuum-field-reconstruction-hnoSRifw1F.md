# LASER: Learning Active Sensing for Continuum Field Reconstruction

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: hnoSRifw1F
- Authors: Huayu Deng; Jinghui Zhong; Xiangming Zhu; Yunbo Wang; Xiaokang Yang
- Primary area: deep_learning->algorithms
- Keywords: Continuum field reconstruction;active sensing;reinforcement learning
- Source URL: https://openreview.net/forum?id=hnoSRifw1F
- PDF URL: https://openreview.net/pdf?id=hnoSRifw1F

## Abstract

High-fidelity measurements of continuum physical fields are essential for scientific discovery and engineering design but remain challenging under sparse and constrained sensing. Conventional reconstruction methods typically rely on fixed sensor layouts, which cannot adapt to evolving physical states. We propose LASER, a unified, closed-loop framework that formulates active sensing as a Partially Observable Markov Decision Process (POMDP). At its core, LASER employs a continuum field latent world model that captures the underlying physical dynamics and provides intrinsic reward feedback. This enables a reinforcement learning policy to simulate ''what-if'' sensing scenarios within a latent imagination space. By conditioning sensor movements on predicted latent states, LASER navigates toward potentially high-information regions beyond current observations. Our experiments demonstrate that LASER consistently outperforms static and offline-optimized strategies, achieving high-fidelity reconstruction under sparsity across diverse continuum fields.

## One-Sentence Claim

LASER frames continuum-field sensing as closed-loop POMDP control, using a latent world model to move sensors toward high-information regions for sparse physical-field reconstruction.

## Problem

Scientific and engineering applications need high-fidelity measurements of continuum physical fields, but dense sensing is often expensive or physically constrained. Fixed sensor layouts cannot adapt to evolving physical states, so they may waste measurements in low-information regions.

The paper asks how sensing itself can become an adaptive policy that reacts to predicted field dynamics.

## Core Contribution

The contribution is LASER, a closed-loop active sensing framework for continuum field reconstruction. It formulates sensor placement and movement as a POMDP and uses a continuum-field latent world model to predict physical dynamics and supply intrinsic reward feedback.

The system lets an RL policy simulate what-if sensing actions in latent imagination space and condition future sensor movement on predicted latent states.

## Method

LASER learns a latent world model of the continuum field from sparse observations. The active-sensing policy uses that model to imagine candidate sensing trajectories, receive intrinsic rewards tied to information value or reconstruction utility, and move sensors toward regions expected to improve reconstruction.

This replaces static or offline-optimized sensing layouts with closed-loop, state-dependent control.

## Experiments and Evidence

Evidence reported in the abstract:

- Diverse continuum-field reconstruction tasks.
- Consistent outperformance over static sensing strategies.
- Outperformance over offline-optimized strategies.
- High-fidelity reconstruction under sparse sensing.
- Latent imagination used for what-if sensing scenarios.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: field domains, sensor constraints, intrinsic reward definition, and robustness under model error.

## Limits and Failure Modes

- Active sensing can fail if the latent world model is wrong in high-uncertainty regions.
- POMDP/RL training may be expensive or brittle across physical systems.
- Real sensors may face dynamics, latency, calibration, and motion constraints not captured in simulation.
- Intrinsic reward may overvalue novelty rather than reconstruction relevance.

## Deep Themes

**Measurement is a policy.** The paper treats sensing as sequential decision-making rather than passive data collection.

**World models guide scientific instrumentation.** Latent imagination is used to choose where to measure next.

**Sparse data can be amplified by adaptivity.** With the right control loop, fewer measurements can recover more field information.

## Subthemes

- Active sensing as POMDP.
- Continuum-field latent world models.
- Intrinsic reward for information gathering.
- Sparse physical-field reconstruction.
- Closed-loop sensor movement.

## Connections to Other Papers

Connects to NeuronCtrl, LoRFS, ReViT, Dirac-Frenkel-Onsager dynamics, and delayed-observation RL. It extends scientific ML from solving or generating physical fields to actively deciding what to observe.

## Notes for Cross-Paper Synthesis

LASER adds an active-data-acquisition theme: in scientific domains, model quality may depend as much on adaptive measurement policy as on the reconstruction architecture.
