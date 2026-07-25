# Mean Flow Policy with Instantaneous Velocity Constraint for One-step Action Generation

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: mIeKe74W43
- Authors: Guojian Zhan; Letian Tao; Pengcheng Wang; Yixiao Wang; Yuxin Chen; Yiheng Li; Hongyang Li; Masayoshi Tomizuka; Shengbo Eben Li
- Primary area: reinforcement learning
- Keywords: Reinforcement learning;Generative policy
- Source URL: https://openreview.net/forum?id=mIeKe74W43
- PDF URL: https://openreview.net/pdf?id=mIeKe74W43

## Abstract

Learning expressive and efficient policy functions is a promising direction in reinforcement learning (RL). While flow-based policies have recently proven effective in modeling complex action distributions with a fast deterministic sampling process, they still face a trade-off between expressiveness and computational burden, which is typically controlled by the number of flow steps. In this work, we propose mean flow policy (MFP), a new generative policy function that models the mean velocity field to achieve the fastest one-step action generation. To ensure its high expressiveness, an instantaneous velocity constraint (IVC) is introduced on the mean velocity field during training. We theoretically prove that this design explicitly serves as a crucial boundary condition, thereby improving learning accuracy and enhancing policy expressiveness. Empirically, our MFP achieves state-of-the-art success rates across several challenging robotic manipulation tasks from Robomimic and OGBench. It also delivers substantial improvements in training and inference speed over existing flow-based policy baselines.

## One-Sentence Claim

MFP models a mean velocity field with an instantaneous velocity constraint to produce expressive one-step generative policies for robotic control.

## Problem

Flow-based policies can model complex action distributions and sample deterministically, but they still trade expressiveness against compute through the number of flow steps. Robotic policies need rich action distributions without slow multi-step inference.

## Core Contribution

The paper introduces Mean Flow Policy, a generative policy that enables one-step action generation, and adds an instantaneous velocity constraint that acts as a boundary condition improving accuracy and expressiveness. It provides both theoretical justification and robotic manipulation results.

## Method

MFP learns the mean velocity field needed to map to actions in one step. During training, the instantaneous velocity constraint regularizes the learned field as a boundary condition, preserving the expressiveness normally associated with multi-step flow policies while reducing sampling cost.

## Experiments and Evidence

The abstract reports state-of-the-art success rates on challenging robotic manipulation tasks from Robomimic and OGBench, plus substantial training and inference speed improvements over existing flow-based policy baselines.

## Limits and Failure Modes

One-step generation may struggle with highly multimodal long-horizon action distributions if the mean velocity field is underparameterized. Robotic benchmarks may not capture safety, contact-rich dynamics, or sim-to-real transfer. Full-text review should check task suites, policy architectures, velocity-constraint derivation, sampling comparisons, and wall-clock speed.

## Deep Themes

- Fast expressive generative policies.
- Flow matching for control.
- Boundary constraints for policy expressiveness.
- One-step action generation.

## Subthemes

- Mean velocity fields.
- Instantaneous velocity constraints.
- Robotic manipulation policies.
- Deterministic sampling speed.
- Training/inference efficiency in control.

## Connections to Other Papers

Connects to ExDM, AIGB-Pearl, and LPWM through generative models for decision-making, to diffusion/flow action-generation papers, and to efficiency themes where reducing sampling steps enables deployment.

## Notes for Cross-Paper Synthesis

MFP continues the theme that generative-policy expressiveness must be balanced against action-time latency. The distinctive move is using a theoretically motivated constraint to make one-step generation behave like a richer flow.
