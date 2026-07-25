# Reverse Flow Matching: A Unified Framework for Online Reinforcement Learning with Diffusion and Flow Policies

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: vUpEe4yd1T
- Authors: Zeyang Li; Sunbochen Tang; Navid Azizan
- Primary area: reinforcement_learning->online
- Keywords: Reinforcement learning;flow matching;diffusion;sampling
- Source URL: https://openreview.net/forum?id=vUpEe4yd1T
- PDF URL: https://openreview.net/pdf?id=vUpEe4yd1T

## Abstract

Diffusion and flow policies are gaining prominence in online reinforcement learning (RL) due to their expressive power, yet training them efficiently remains a critical challenge. A fundamental difficulty that distinguishes online RL from standard generative modeling is the lack of direct samples from the target Boltzmann distribution defined by the Q-function. To address this, two seemingly distinct families of methods have been proposed for diffusion policies: a noise-expectation family, which uses a weighted average of noise as the training target, and a gradient-expectation family, which employs a weighted average of Q-function gradients. However, it remains unclear how these objectives are formally related, or whether they can be synthesized into a more general formulation. In this paper, we propose a unified framework, reverse flow matching (RFM), which rigorously addresses the problem of training diffusion and flow models without direct target samples. By adopting a reverse inferential perspective, we formulate the training target as a posterior mean estimation problem given an intermediate noisy sample. Crucially, we introduce Langevin Stein operators to construct zero-mean control variates, deriving a general class of estimators that share the same expectation. We show that existing noise-expectation and gradient-expectation methods are simply two specific instances within this broader class. This unified view yields two key advancements: it extends the capability of targeting Boltzmann distributions from diffusion to flow policies, and it enables the principled combination of Q-value and Q-gradient information to form an effective estimator, thereby improving training efficiency and stability. We instantiate RFM to train a flow policy in online RL and demonstrate improved performance on continuous-control benchmarks compared to diffusion policy baselines.

## One-Sentence Claim

Reverse Flow Matching unifies online RL training of diffusion and flow policies by estimating posterior means for Q-induced Boltzmann targets without direct target samples.

## Problem

Diffusion and flow policies are expressive for online RL, but unlike ordinary generative modeling, RL does not provide direct samples from the target Boltzmann distribution induced by the Q-function.

Existing diffusion-policy methods split into noise-expectation objectives and gradient-expectation objectives. Their relationship is unclear, making it hard to combine Q-value and Q-gradient information principledly.

## Core Contribution

The paper proposes Reverse Flow Matching, a unified framework for training diffusion and flow policies without direct target samples. It interprets the training target as posterior mean estimation given an intermediate noisy sample.

Using Langevin Stein operators, it constructs zero-mean control variates and derives a broad estimator class with shared expectation. Existing noise- and gradient-expectation methods become special cases.

## Method

RFM adopts a reverse inferential view: infer the clean target-related quantity from an intermediate noisy sample under the Q-induced Boltzmann objective. Estimators can combine Q values and Q gradients while preserving unbiased or same-expectation structure.

Langevin Stein control variates supply variance/control flexibility. The framework extends Boltzmann targeting from diffusion policies to flow policies.

## Experiments and Evidence

The abstract reports an instantiation that trains a flow policy in online RL and improves performance on continuous-control benchmarks compared with diffusion-policy baselines.

Full-paper reading should verify benchmark list, estimator variance, Q-function approximation assumptions, stability across online updates, and comparison to standard actor-critic and generative-policy methods.

## Limits and Failure Modes

The framework still depends on Q-function quality. Biased or unstable Q estimates can produce misleading Boltzmann targets, especially in online RL where data distribution changes.

Flow/diffusion policies can be expensive to sample or train compared with simpler Gaussian policies. Efficiency gains depend on estimator stability and implementation.

## Deep Themes

- Generative policies under RL targets: diffusion/flow models must learn from Q-defined distributions, not data samples.
- Unified estimator geometry: noise and gradient objectives are instances of one expectation class.
- Stein control variates for policy training: probabilistic identities improve RL estimator design.
- Flow policies in online RL: expressive generative control extends beyond diffusion.

## Subthemes

- Boltzmann policy targets are implicit in Q-values.
- Posterior mean estimation reframes denoising for RL.
- Q-value and Q-gradient information can be combined.
- Continuous control tests whether expressive policies improve online learning.

## Connections to Other Papers

RFM connects to GWF, any-order GPT, XDLM, and insertion processes through generative-model unification. It also connects to DAWN, ScaleMoE, and policy-gradient post-training through RL optimization around value functions.

It fits a broader theme of translating generative modeling tools into decision-making, where the missing target-sample problem becomes central.

## Notes for Cross-Paper Synthesis

The synthesis point is that generative models become different objects inside RL. The target distribution is defined by value, so training requires inference machinery rather than supervised sample matching.
