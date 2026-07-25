# Faster Activation Functions at the Edge for Post-Training Speedups

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: u2o6hPE8ik
- Authors: Anton Lydike; Jun Bi; Jackson Woodruff
- Primary area: general_machine_learning->hardware_and_software
- Keywords: Machine Learning;Systems;Machine Learning Systems;Edge ML;Activation Functions;Approximations;Bitcasting;IEEE Float
- Source URL: https://openreview.net/forum?id=u2o6hPE8ik
- PDF URL: https://openreview.net/pdf?id=u2o6hPE8ik

## Abstract

On-device AI has gained significant attention for enabling efficient, low-latency inference on edge devices.
However, tight resource constraints on these platforms make the deployment of accurate and lightweight deep
learning models challenging.
In particular,
advanced activation functions (AFs) like Swish and GELU often incur
high inference overhead due to the lack of hardware fast-paths for exponentiation and division,
restricting edge-ML applications to simple AFs like ReLU, limiting model accuracy.
To address this, we propose FFCC, a compiler that automatically
generates efficient approximations of AFs through floating-point reinterpretation.
These functions do not require hardware fast-paths, meaning they remain fast
on edge devices, but are accurate enough to be used as post-training drop-ins.
FFCC takes a specification of AFs using basic floating-point operators
and applies derivation rules to lower these expressions into
efficient instruction sequences.
Our experiments show that FFCC provides fast approximations of AFs, achieving order-of-magnitude
speed-ups over accurate baselines on Arm M7, Aarch64 and Intel platforms.
Using ConvNeXt as an example, we demonstrate how these activation-level gains translate to end-to-end speed-ups,
and do not result in significant loss of model accuracy.

## One-Sentence Claim

FFCC automatically compiles expensive activation functions into fast floating-point reinterpretation approximations that can be dropped into trained models for edge inference speedups with little accuracy loss.

## Problem

On-device inference faces tight latency, power, and instruction constraints. Modern activation functions such as Swish and GELU often rely on exponentiation or division, which lack fast hardware paths on many edge devices.

This creates a tradeoff: use advanced activations for accuracy but pay runtime overhead, or use simpler ReLU-like activations and lose model quality. The paper targets post-training speedups without retraining models around different activations.

## Core Contribution

The paper proposes FFCC, a compiler that generates efficient activation-function approximations through floating-point reinterpretation. Given an activation specification in basic floating-point operations, FFCC applies derivation rules to lower it into efficient instruction sequences.

The contribution is a post-training systems tool: replace costly activations with accurate-enough fast approximations that do not require hardware fast paths.

## Method

FFCC uses bitcasting and floating-point reinterpretation to approximate nonlinear activation expressions. It automatically derives instruction sequences for target activations, avoiding expensive exponentiation/division where edge hardware is weak.

Because the approximations are designed as drop-ins, existing trained models can be accelerated without changing architecture or retraining from scratch.

## Experiments and Evidence

The abstract reports order-of-magnitude activation speedups over accurate baselines on Arm M7, Aarch64, and Intel platforms. Using ConvNeXt, it shows activation-level gains translate to end-to-end speedups without significant accuracy loss.

Full-paper reading should verify supported activations, approximation error bounds, benchmark kernels, energy measurements, model coverage, and accuracy impact across tasks.

## Limits and Failure Modes

Approximation error can interact with model calibration, quantization, or distribution shift. A small average accuracy loss may hide failures in safety-critical edge workloads.

The benefits depend on activation share of runtime and hardware instruction mix. Models dominated by memory bandwidth or convolutions may see smaller end-to-end gains.

## Deep Themes

- Compiler-level model acceleration: efficiency can come from lowering math operations, not changing model weights.
- Post-training deployment optimization: trained models can be adapted to hardware after the fact.
- Edge-specific approximations: hardware fast paths determine which neural components are expensive.
- Accuracy-speed tradeoff at the activation level: nonlinearities become systems bottlenecks.

## Subthemes

- Swish and GELU are costly without exp/div fast paths.
- Bitcasting enables cheap approximate nonlinear computations.
- Arm M7 and Aarch64 highlight embedded/edge relevance.
- Drop-in approximations reduce adoption friction.

## Connections to Other Papers

FFCC connects to CMRU, DHSA, TabSwift, STAR-KV, and MoE compression through deployment efficiency. Unlike model-level compression, it attacks a low-level mathematical primitive.

It also fits the broader systems theme: practical ML speed often comes from respecting hardware constraints hidden beneath algorithm design.

## Notes for Cross-Paper Synthesis

The synthesis point is that edge ML creates a different optimization surface. Activation functions, instruction sets, and compiler rewrites can matter as much as architecture choice.
