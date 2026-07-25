# Differentiable Model Predictive Control on the GPU

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: bFYfV6c9zu
- Authors: Emre Adabag; Marcus Greiff; John Subosits; Thomas Jonathan Lew
- Primary area: applications to robotics, autonomy, planning
- Keywords: differentiable optimization;model predictive control;optimal control;gpu-accelerated optimization;reinforcement learning;imitation learning;robotics
- Source URL: https://openreview.net/forum?id=bFYfV6c9zu
- PDF URL: https://openreview.net/pdf?id=bFYfV6c9zu

## Abstract

Differentiable model predictive control (MPC) offers a powerful framework for combining learning and control. However, its adoption has been limited by the inherently sequential nature of traditional optimization algorithms, which are challenging to parallelize on modern computing hardware like GPUs. In this work, we tackle this bottleneck by introducing a GPU-accelerated differentiable optimization tool for MPC. This solver leverages sequential quadratic programming and a custom preconditioned conjugate gradient (PCG) routine with tridiagonal preconditioning to exploit the problem's structure and enable efficient parallelization. We demonstrate substantial speedups over CPU- and GPU-based baselines, significantly improving upon state-of-the-art training times on benchmark reinforcement learning and imitation learning tasks. Finally, we showcase the method on the challenging task of reinforcement learning for driving at the limits of handling, where it enables robust drifting of a Toyota Supra through water puddles.

## One-Sentence Claim

This work makes differentiable MPC practical on GPUs through a structure-exploiting SQP solver with custom preconditioned conjugate gradients and tridiagonal preconditioning.

## Problem

Differentiable MPC is valuable for combining learning and control, but traditional optimization algorithms are sequential and difficult to parallelize efficiently on GPUs.

This limits adoption in RL and imitation learning workflows where training requires many fast differentiable control solves.

## Core Contribution

The paper introduces a GPU-accelerated differentiable optimization tool for model predictive control.

Its solver uses sequential quadratic programming and a custom PCG routine with tridiagonal preconditioning to exploit MPC problem structure while enabling parallel execution.

## Method

The solver formulates MPC updates through SQP and accelerates the linear algebra with a GPU-friendly preconditioned conjugate-gradient routine.

Tridiagonal preconditioning leverages temporal structure in MPC problems, reducing bottlenecks that make naive GPU optimization inefficient.

## Experiments and Evidence

The abstract reports substantial speedups over CPU and GPU baselines.

It improves state-of-the-art training times on RL and imitation learning benchmarks and demonstrates robust drifting of a Toyota Supra through water puddles in a difficult driving-at-the-limits task.

## Limits and Failure Modes

MPC solver performance may depend on problem conditioning, horizon length, dynamics smoothness, and GPU batch size. Differentiable control also requires accurate dynamics or learned models.

Because this note is abstract-only, details still need checking: solver API, gradient correctness, benchmark tasks, speedup factors, baseline solvers, and driving-task dynamics.

## Deep Themes

- Differentiable control infrastructure: learning-control systems need fast gradient-compatible optimizers.
- Structure-aware GPU optimization: MPC temporal structure is exploited rather than treated as generic dense algebra.
- Control as training inner loop: faster MPC changes what RL and imitation learning experiments are feasible.
- Robotics deployment realism: driving at handling limits tests control under difficult dynamics.

## Subthemes

- Model predictive control.
- Sequential quadratic programming.
- GPU PCG solver.
- Differentiable optimal control.

## Connections to Other Papers

This connects to robotics planning papers, MSP, VectorWorld, CDGS, and systems acceleration work such as TileLang.

It also relates to SparseRL because both target GPU-level performance for structured technical domains.

## Notes for Cross-Paper Synthesis

GPU differentiable MPC adds a control-infrastructure theme: better learning systems often require making classical optimization loops differentiable and accelerator-native.
