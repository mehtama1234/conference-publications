# Chebyshev Policies and the Mountain Car Problem: Reinforcement Learning for Low-Dimensional Control Tasks

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: aNWIVNjocB
- Authors: Stefan Huber; Hannes Unger; Georg Schäfer; Jakob Rehrl
- Primary area: theory->reinforcement_learning_and_planning
- Keywords: Chebyshev polynomials;mountain car problem;low-dimensional control;optimal control;reinforcement learning
- Source URL: https://openreview.net/forum?id=aNWIVNjocB
- PDF URL: https://openreview.net/pdf?id=aNWIVNjocB

## Abstract

We analytically solve the Mountain Car problem, a canonical benchmark in RL, and derive an optimal control solution, closing a gap after 36 years. This enables us to reveal two surprising insights: The optimal control is quite simple, yet modern RL agents display a large gap to optimality. Motivated by the analysis of the optimal control, we introduce Chebyshev policies as a universal (i.e. dense) class of RL policies from first principles. They can be trained as drop-in replacements of neural nets, reducing the regret by a factor of 4.18, while requiring 277 times fewer parameters, fostering sample efficiency, explainability and realtime capability. Chebyshev policies are evaluated on further RL tasks, including a real-world nonlinear motion control testbed. They consistently improve performance over neural nets with PPO, ARS and REINFORCE. Our results demonstrate how Chebyshev policies offer a compelling and lightweight alternative or addition to neural nets for low-dimensional control tasks.

## One-Sentence Claim

Chebyshev polynomial policies offer a lightweight universal policy class for low-dimensional control, closing much of the optimality gap that neural RL agents leave on Mountain Car and related tasks.

## Problem

Mountain Car is a canonical RL benchmark, but the exact optimal control solution had remained analytically unresolved. Without that reference, it is hard to tell whether modern RL agents are near-optimal or merely good enough.

The paper asks what the true optimal solution reveals about low-dimensional control and whether simpler structured policy classes can outperform neural networks.

## Core Contribution

The paper analytically solves Mountain Car and derives the optimal control solution. This shows the optimal control is simple, while modern RL agents still have a large gap to optimality.

Motivated by the solution, it introduces Chebyshev policies: dense universal RL policies based on Chebyshev polynomials. As drop-in neural-net replacements, they reduce regret by 4.18x while using 277x fewer parameters and improve sample efficiency, explainability, and real-time capability.

## Method

The method uses analytical optimal-control analysis to identify a structured function family suitable for low-dimensional continuous control. Chebyshev polynomial expansions parameterize policies compactly and can be trained inside standard RL algorithms such as PPO, ARS, and REINFORCE.

The key move is replacing generic neural policies with a basis aligned to smooth low-dimensional control functions.

## Experiments and Evidence

Evidence reported in the abstract:

- Analytical solution of the Mountain Car optimal control problem.
- Demonstration of modern RL agents' optimality gap.
- Chebyshev policies reduce regret by 4.18x.
- 277x fewer parameters than neural alternatives.
- Evaluations on additional RL tasks and a real-world nonlinear motion-control testbed.
- Consistent gains with PPO, ARS, and REINFORCE.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: exact Mountain Car assumptions, policy order, control testbed, and benchmark neural baselines.

## Limits and Failure Modes

- Chebyshev policies are best suited to low-dimensional control; high-dimensional perception-action tasks may require different structure.
- Polynomial bases can behave poorly outside the represented domain.
- Analytic insights from Mountain Car may not transfer to contact-rich or discontinuous dynamics.
- Drop-in performance likely depends on normalization and basis order.

## Deep Themes

**Small structured policy classes can beat generic neural policies.** Low-dimensional control may need the right basis, not more parameters.

**Solved benchmarks expose hidden optimality gaps.** Analytical solutions turn familiar RL tasks into diagnostic tools.

**Explainability and real-time control come from compact structure.** Chebyshev policies are more inspectable and lighter than neural nets.

## Subthemes

- Analytical Mountain Car solution.
- Chebyshev polynomial policies.
- Universal dense policy class.
- Low-dimensional optimal control.
- Parameter-efficient RL.

## Connections to Other Papers

Connects to PAVE, TimeRewarder, FlowOptimizer, and BFTS through decision/control methods that improve by matching structure to problem geometry. It also links to Brain Encoding Scale and Lottery Prior through compact alternatives to large neural models.

## Notes for Cross-Paper Synthesis

Chebyshev Policies reinforces a recurring counter-scaling lesson: for some regimes, a small mathematically aligned model class can be more capable than a generic neural baseline.
