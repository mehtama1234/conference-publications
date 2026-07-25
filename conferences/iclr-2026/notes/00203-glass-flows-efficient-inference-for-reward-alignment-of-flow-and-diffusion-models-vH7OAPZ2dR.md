# GLASS Flows: Efficient Inference for Reward Alignment of Flow and Diffusion Models

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: vH7OAPZ2dR
- Authors: Peter Holderrieth; Uriel Singer; Tommi Jaakkola; Ricky T. Q. Chen; Yaron Lipman; Brian Karrer
- Primary area: generative models
- Keywords: Flow Matching; Diffusion Models; Reward Alignment; Reward Adaptation; Inference-time scaling; Feynman-Kac Steering; Markov transitions; Sampling methods
- Source URL: https://openreview.net/forum?id=vH7OAPZ2dR
- PDF URL: https://openreview.net/pdf?id=vH7OAPZ2dR

## Abstract

The performance of flow matching and diffusion models can be greatly improved at inference time using reward adaptation algorithms, yet efficiency remains a major limitation. While several algorithms were proposed, we demonstrate that a common bottleneck is the *sampling* method these algorithms rely on: many algorithms require to sample Markov transitions via SDE sampling, which is significantly less efficient and often less performant than ODE sampling. To remove this bottleneck, we introduce GLASS Flows, a new sampling paradigm that simulates a ''flow matching model within a flow matching model'' to sample Markov transitions. As we show in this work, this ''inner'' flow matching model can be retrieved from any pre-trained model without any re-training, effectively combining the efficiency of ODEs with the stochastic evolution of SDEs. On large-scale text-to-image models, we show that GLASS Flows eliminate the trade-off between stochastic evolution and efficiency. GLASS Flows improve state-of-the-art performance in text-to-image generation, making it a simple, drop-in solution for inference-time scaling of flow and diffusion models.

## One-Sentence Claim

GLASS Flows make inference-time reward alignment of flow and diffusion models efficient by sampling Markov transitions through an inner flow model extracted from the pretrained model without retraining.

## Problem

Reward adaptation can improve flow matching and diffusion models at inference time, but many algorithms rely on SDE Markov transition sampling, which is slower and often less performant than ODE sampling. This creates a tradeoff between stochastic evolution and efficiency.

## Core Contribution

The paper introduces GLASS Flows, a sampling paradigm that simulates a flow matching model within a flow matching model to sample Markov transitions. It recovers the inner model from any pretrained model without retraining.

## Method

GLASS Flows replaces direct SDE transition sampling with an inner flow-matching construction that preserves stochastic transition behavior while using efficient ODE-style sampling. It acts as a drop-in sampling method for inference-time reward adaptation algorithms.

## Experiments and Evidence

On large-scale text-to-image models, GLASS Flows reportedly removes the efficiency/stochasticity tradeoff and improves state-of-the-art text-to-image reward-aligned generation as a simple inference-time scaling solution.

## Limits and Failure Modes

Reward alignment can over-optimize reward models, reduce diversity, or introduce artifacts. The inner-flow construction may depend on assumptions about pretrained model dynamics. Full-text review should check derivation, compatibility with diffusion versus flow models, reward models used, latency, diversity metrics, and failure cases.

## Deep Themes

- Efficient inference-time reward adaptation.
- Flow matching inside pretrained generative models.
- ODE efficiency with stochastic transition behavior.
- Drop-in sampling for aligned generation.

## Subthemes

- Feynman-Kac steering.
- Markov transition sampling.
- Text-to-image reward alignment.
- Inference-time scaling.
- Flow/diffusion sampler design.

## Connections to Other Papers

Connects to Complexa, Prophet, PAPL, and diffusion/flow alignment papers through inference-time control, and to reward-modeling work where learned objectives guide generation after pretraining.

## Notes for Cross-Paper Synthesis

GLASS Flows fits the broad pattern of moving optimization into inference while controlling compute cost. It makes the sampler itself the bottleneck and the intervention point.
