# PACT: Self-Evolving Physical Safety Alignment for Diffusion Policies in Embodied Manipulation

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: ePFvXPdvhM
- Authors: Lingxuan Wu; Zijian Zhu; Lizhong Wang; Chengyang Ying; Huayu Chen; Xiao Yang; Fangming Liu; Jun Zhu
- Primary area: applications->robotics
- Keywords: Diffusion Policy;Safety Alignment
- Source URL: https://openreview.net/forum?id=ePFvXPdvhM
- PDF URL: https://openreview.net/pdf?id=ePFvXPdvhM

## Abstract

Diffusion policies have achieved remarkable success in robotic manipulation, yet they often fail to satisfy strict physical constraints required for safe deployment.  Existing approaches impose safety either prematurely during training or reactively via external guardrails at test time, limiting policy expressivity and overall scalability. We propose Physical safety Alignment for Constrained Trajectories (PACT), a self-evolving post-training framework that projects pretrained diffusion policies onto constraint-feasible regions without accessing demonstration data or task rewards. PACT distills constraint gradients into the diffusion model through a reverse-KL objective with dense supervision across timesteps. It incorporates a curriculum that progressively tightens constraints while maintaining theoretically bounded policy shift and monotone improvement, mitigating the safety-performance trade-off from catastrophic forgetting. On simulated and real-world embodied manipulation benchmarks, PACT significantly reduces safety violations by 31.0% on average while improving task success by 30.7%.

## One-Sentence Claim

PACT post-trains diffusion policies toward physically feasible trajectories by distilling constraint gradients while bounding policy shift and preserving task competence.

## Problem

Diffusion policies can generate effective manipulation behavior but may violate hard physical constraints during deployment. Training-time safety constraints can overrestrict learning, while test-time guardrails are reactive and may degrade performance or scalability.

The paper targets a practical embodied-learning problem: make a pretrained policy safer without demonstrations or task rewards.

## Core Contribution

PACT is a self-evolving post-training framework that projects pretrained diffusion policies toward constraint-feasible regions. It distills constraint gradients into the diffusion model through a reverse-KL objective with dense supervision across diffusion timesteps.

The method uses a curriculum that progressively tightens constraints while maintaining bounded policy shift and monotone improvement, directly addressing catastrophic forgetting and the safety-performance tradeoff.

## Method

PACT computes constraint information over generated trajectories and uses those gradients as supervision for post-training. Reverse KL keeps the updated policy close to the original while biasing it toward feasible regions.

The curriculum begins with looser constraints and tightens them over training. Dense timestep supervision lets the policy internalize safety across the denoising process rather than relying on a final-stage filter.

## Experiments and Evidence

Evidence reported in the abstract:

- Simulated and real-world embodied manipulation benchmarks.
- Average safety violations reduced by 31.0%.
- Task success improved by 30.7%.
- No access to demonstration data or task rewards.
- Theoretical claims of bounded policy shift and monotone improvement.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: constraint classes, robot tasks, real-world setup, reverse-KL estimator, and curriculum schedule.

## Limits and Failure Modes

- The method assumes usable constraint gradients; non-differentiable or poorly specified safety constraints may be harder.
- Safety alignment is only as complete as the constraint set.
- Reverse-KL closeness may preserve unsafe modes if constraints do not expose them clearly.
- Real-world deployment needs guarantees under perception error, dynamics shift, and contact-rich edge cases.

## Deep Themes

**Safety alignment is shifting from rejection to internalization.** PACT trains the policy to produce feasible trajectories rather than filtering after the fact.

**Post-training is becoming a general alignment layer.** The method adapts a pretrained generative controller without original demonstrations or rewards.

**Constraints can be curricula.** Safety pressure is gradually tightened to avoid breaking useful behavior.

## Subthemes

- Diffusion-policy safety alignment.
- Constraint-gradient distillation.
- Reverse-KL bounded policy shift.
- Curriculum-tightened feasibility.
- Embodied manipulation without reward access.

## Connections to Other Papers

Connects to NeuronCtrl, Safe Neuronal Control, Tilt Matching, KPE/KTS, and Manifold-Optimal Guidance. All use post-training or inference-time dynamics to steer generative processes toward constraints, rewards, or safer regions.

## Notes for Cross-Paper Synthesis

PACT is part of a broader 2026 pattern: generative models are being treated as controllable dynamical systems whose trajectories can be constrained after pretraining.
