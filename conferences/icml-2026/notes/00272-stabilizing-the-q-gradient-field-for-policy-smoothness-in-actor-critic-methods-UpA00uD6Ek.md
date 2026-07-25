# Stabilizing the Q-Gradient Field for Policy Smoothness in Actor-Critic Methods

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: UpA00uD6Ek
- Authors: Jeong Woon Lee; Kyoleen Kwak; Daeho Kim; Hyoseok Hwang
- Primary area: reinforcement_learning
- Keywords: Deep Reinforcement Learning;Policy Smoothness;Critic Regularization
- Source URL: https://openreview.net/forum?id=UpA00uD6Ek
- PDF URL: https://openreview.net/pdf?id=UpA00uD6Ek

## Abstract

Policies learned via continuous actor-critic methods often exhibit erratic, high-frequency oscillations, making them unsuitable for physical deployment. 
Current approaches attempt to enforce smoothness by directly regularizing the policy's output. 
We argue that this approach treats the symptom rather than the cause. 
In this work, we theoretically establish that policy non-smoothness is fundamentally governed by the differential geometry of the critic. 
By applying implicit differentiation to the actor-critic objective, we prove that the sensitivity of the optimal policy is bounded by the ratio of the Q-function's mixed-partial derivative (noise sensitivity) to its action-space curvature (signal distinctness). 
To empirically validate this theoretical insight, we introduce PAVE (Policy-Aware Value-field Equalization), a critic-centric regularization framework that treats the critic as a scalar field and stabilizes its induced action-gradient field. 
PAVE rectifies the learning signal by minimizing the Q-gradient volatility while preserving local curvature. 
Experimental results demonstrate that PAVE achieves smoothness comparable to policy-side smoothness regularization methods, while maintaining competitive task performance, without modifying the actor.

## One-Sentence Claim

Policy smoothness in continuous actor-critic methods is governed by the critic's differential geometry, so stabilizing the Q-gradient field can smooth policies without modifying the actor.

## Problem

Continuous-control policies learned by actor-critic methods can exhibit high-frequency oscillations that are unsafe or impractical for physical deployment. Existing methods often directly regularize policy outputs, but this may treat non-smooth behavior after it has already been induced.

The paper asks whether the source of policy non-smoothness lies in the critic's learning signal.

## Core Contribution

The paper theoretically links optimal-policy sensitivity to the ratio between the Q-function's mixed-partial derivative, interpreted as noise sensitivity, and its action-space curvature, interpreted as signal distinctness.

It then proposes PAVE, Policy-Aware Value-field Equalization, a critic-centric regularization framework that treats the critic as a scalar field and stabilizes the action-gradient field it induces. PAVE minimizes Q-gradient volatility while preserving local curvature.

## Method

The theoretical method uses implicit differentiation of the actor-critic objective to relate policy sensitivity to critic geometry. The practical method regularizes the critic so its gradients with respect to action are less volatile while retaining useful curvature for distinguishing good actions.

This moves smoothness control upstream: the actor receives a smoother optimization field rather than being directly penalized after learning.

## Experiments and Evidence

Evidence reported in the abstract:

- Theoretical bound connecting policy sensitivity to Q mixed-partials and action curvature.
- PAVE regularization that stabilizes the critic-induced action-gradient field.
- Experiments showing smoothness comparable to policy-side regularization.
- Competitive task performance without modifying the actor.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: environments, smoothness metrics, regularization terms, sample efficiency, and actor-critic algorithms tested.

## Limits and Failure Modes

- Critic regularization can bias value estimates if volatility reduction suppresses real sharp action distinctions.
- The theory may rely on local optimality or differentiability assumptions that fail in deep RL practice.
- Physical deployment needs robustness to observation noise and actuator limits beyond smoothness.
- PAVE's added training cost is not visible from the abstract.

## Deep Themes

**Control behavior is shaped by learned fields.** The policy's roughness is traced to the geometry of the critic, not only the actor architecture.

**Regularize causes, not outputs.** Stabilizing the Q-gradient field targets the source of oscillatory policy updates.

**Differential geometry is entering RL diagnostics.** Mixed partials, curvature, and gradient-field volatility become practical training signals.

## Subthemes

- Critic-centric policy smoothness.
- Q-gradient volatility.
- Action-space curvature preservation.
- Implicit differentiation of actor-critic objectives.
- Physical deployment constraints.

## Connections to Other Papers

Connects to R2VPO and RQE Actor-Critic through RL stability, and to Flowers and RelaxFlow through vector-field views of learned dynamics. It also links to robustness papers where internal gradients or pathways are regularized to produce safer external behavior.

## Notes for Cross-Paper Synthesis

PAVE reinforces a theme that system behavior often follows the geometry of an internal field. If the field is noisy or ill-conditioned, downstream control becomes erratic even if the final policy is directly penalized.
