# Tilt Matching for Scalable Sampling and Fine-Tuning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: dQA4Gjt4KU
- Authors: Peter Potaptchik; Lee Cheuk Kit; Michael Samuel Albergo
- Primary area: deep_learning->generative_models_and_autoencoders
- Keywords: Diffusion Models;Flow Matching;Fine-Tuning
- Source URL: https://openreview.net/forum?id=dQA4Gjt4KU
- PDF URL: https://openreview.net/pdf?id=dQA4Gjt4KU

## Abstract

We propose a simple, scalable algorithm based on stochastic interpolants for sampling from unnormalized densities and for fine-tuning generative models. The approach, Tilt Matching, arises from a dynamical equation relating the flow matching velocity to one targeting the same distribution tilted by a reward, implicitly solving a stochastic optimal control problem. The resulting velocity inherits the regularity of stochastic interpolant transports while minimizing an objective with strictly lower variance than flow matching itself. The update to the velocity field can be interpreted as the sum of all joint cumulants between the interpolant velocity and the reward, and to first order is their covariance. The method requires neither reward gradients nor backpropagation through trajectories of the flow or diffusion. We empirically demonstrate that the approach is efficient and highly scalable, providing state-of-the-art results on sampling under Lennard-Jones systems and competitive performance for fine-tuning Stable Diffusion, without requiring reward multipliers. The framework also applies directly to tilting few-step flow map models.

## One-Sentence Claim

Tilt Matching updates flow-matching velocities toward reward-tilted targets with lower-variance objectives and no reward gradients or trajectory backpropagation.

## Problem

Sampling from unnormalized densities and fine-tuning generative models often require reward- or energy-guided dynamics. Existing approaches can need reward gradients, backpropagation through diffusion/flow trajectories, or high-variance objectives.

The paper asks for a scalable way to tilt a generative transport toward reward-preferred distributions.

## Core Contribution

The paper proposes Tilt Matching, based on stochastic interpolants. It derives from a dynamical equation relating the original flow-matching velocity to one targeting the same distribution tilted by a reward, implicitly solving a stochastic optimal control problem.

The velocity update inherits regularity from stochastic interpolant transports and has strictly lower variance than flow matching. It can be interpreted as the sum of joint cumulants between interpolant velocity and reward, with covariance as the first-order term.

## Method

Tilt Matching estimates how reward tilting should modify the velocity field without differentiating through rewards or entire trajectories. It updates the flow using statistics of interpolant velocity and reward, avoiding reward multipliers and expensive trajectory backpropagation.

The method applies to sampling, Stable Diffusion fine-tuning, and few-step flow-map models.

## Experiments and Evidence

Evidence reported in the abstract:

- Stochastic-interpolant-based sampling and fine-tuning algorithm.
- Lower-variance objective than flow matching.
- No reward gradients or trajectory backpropagation.
- State-of-the-art results on Lennard-Jones sampling.
- Competitive Stable Diffusion fine-tuning without reward multipliers.
- Direct applicability to few-step flow maps.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: objective derivation, variance comparison, reward types, and Stable Diffusion evaluation.

## Limits and Failure Modes

- Reward tilting can reduce diversity or exploit reward misspecification.
- Cumulant estimation may require many samples for high-order effects.
- Competitive fine-tuning claims need comparison to RLHF/RLAIF-style baselines.
- Few-step flow-map behavior may differ from long-trajectory diffusion.

## Deep Themes

**Reward guidance can be velocity-field surgery.** The method modifies transport dynamics directly.

**Avoiding reward gradients broadens applicability.** Black-box rewards become usable for fine-tuning.

**Lower-variance objectives are central to scalable generative control.** Tilt Matching targets both statistical and computational efficiency.

## Subthemes

- Stochastic interpolants.
- Reward-tilted flow matching.
- Joint cumulant velocity updates.
- Lennard-Jones sampling.
- Stable Diffusion fine-tuning.

## Connections to Other Papers

Connects to Flow Sampling, UDM-GRPO, TD3B, KPE/KTS, and diffusion control papers. It also links to R2VPO and alignment work through reward-guided optimization with stability concerns.

## Notes for Cross-Paper Synthesis

Tilt Matching reinforces that generative fine-tuning is becoming a control problem over dynamics, where reward information shapes the velocity field rather than only selecting final samples.
