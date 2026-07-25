# Rodrigues Network for Learning Robot Actions

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: IZHk6BXBST
- Authors: Jialiang Zhang; Haoran Geng; Yang You; Congyue Deng; Pieter Abbeel; Jitendra Malik; Leonidas Guibas
- Primary area: applications to robotics, autonomy, planning
- Keywords: Robot learning;Action understanding;Neural architecture
- Source URL: https://openreview.net/forum?id=IZHk6BXBST
- PDF URL: https://openreview.net/pdf?id=IZHk6BXBST

## Abstract

Understanding and predicting articulated actions is important in robot learning. However, common architectures such as MLPs and Transformers lack inductive biases that reflect the underlying kinematic structure of articulated systems. To this end, we propose the **Neural Rodrigues Operator**, a learnable generalization of the classical forward kinematics operation, designed to inject kinematics-aware inductive bias into neural computation. Building on this operator, we design the **Rodrigues Network (RodriNet)**, a novel neural architecture specialized for processing actions. We evaluate the expressivity of our network on two synthetic tasks on kinematic and motion prediction, showing significant improvements compared to standard backbones. We further demonstrate its effectiveness in two realistic applications: (i) imitation learning on robotic benchmarks with the Diffusion Policy, and (ii) single-image 3D hand reconstruction. Our results suggest that integrating structured kinematic priors into the network architecture improves action learning in various domains.

## One-Sentence Claim

RodriNet improves robot action learning by embedding kinematics-aware inductive bias through a learnable Neural Rodrigues Operator.

## Problem

Robot actions often involve articulated kinematic structure, but generic MLPs and Transformers do not encode that structure directly.

This limits action understanding and prediction, especially for articulated motion and robotic manipulation where rotations and kinematic chains matter.

## Core Contribution

The paper introduces the Neural Rodrigues Operator, a learnable generalization of classical forward kinematics.

Building on it, the authors design Rodrigues Network, RodriNet, an architecture specialized for processing actions with kinematics-aware computation.

## Method

The Neural Rodrigues Operator injects rotation and kinematic structure into neural computation. RodriNet composes these operators to process articulated action sequences or states.

The architecture is evaluated both on synthetic kinematic/motion prediction tasks and on realistic robot/action perception tasks.

## Experiments and Evidence

The abstract reports significant improvements over standard backbones on two synthetic kinematic and motion prediction tasks.

It also reports effectiveness for imitation learning with Diffusion Policy and for single-image 3D hand reconstruction.

## Limits and Failure Modes

Kinematic priors help when the domain matches articulated-body assumptions, but may be less useful for deformable objects, contact-rich manipulation, or tasks where dynamics dominate kinematics.

Because this note is abstract-only, details still need checking: operator definition, robot benchmarks, integration with Diffusion Policy, hand reconstruction setup, and ablations against SE(3)-equivariant models.

## Deep Themes

- Structured action architectures: robot learning benefits from kinematic priors.
- Neuralized classical operators: forward kinematics becomes learnable rather than hard-coded.
- Geometry in action representation: rotations and articulated chains should shape computation.
- Cross-domain action learning: one inductive bias supports synthetic, robotic, and hand-reconstruction tasks.

## Subthemes

- Neural Rodrigues Operator.
- Kinematics-aware action networks.
- Diffusion Policy integration.
- 3D hand reconstruction.

## Connections to Other Papers

This connects to MSP, VectorWorld, Pi-net, and camera-aware MLLMs through geometry-aware embodied AI.

It also relates to quotient-space diffusion and physical-domain generation because structural geometry constrains valid outputs.

## Notes for Cross-Paper Synthesis

RodriNet adds a kinematic-prior thread: robotic models improve when classical geometric operations are integrated into learned architectures.
