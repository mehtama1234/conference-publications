# Solving Time-Dependent Differential Equations with Physical Dynamical Systems

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 0YHSZPkMp8
- Authors: Chuan Liu; Yijie Chen; Ruibing Song; Wenhao Huang; Chunshu Wu; Deqian Kong; Ying Nian Wu; Kaiyuan Yang; Ang Li; Tony Geng
- Primary area: general_machine_learning->hardware_and_software
- Keywords: Differential Equations;Dynamical Systems
- Source URL: https://openreview.net/forum?id=0YHSZPkMp8
- PDF URL: https://openreview.net/pdf?id=0YHSZPkMp8

## Abstract

Time-Dependent Differential Equations (TDDEs) model dynamical processes across science and engineering, but time-critical applications require solvers that deliver high-fidelity trajectories under stringent latency constraints. Most existing TDDE solvers are limited by time discretization, forcing a latency-accuracy trade-off where smaller step sizes capture high-fidelity trajectories but incur prohibitive runtime, while larger steps meet real-time budgets at the cost of trajectory distortion. Dynamical System Machines (DSMs) offer a promising alternative by computing through continuous physical evolution, yet existing DSMs struggle to capture the spatiotemporal complexity of TDDEs. This work introduces DS-TS, a novel TDDE solver that is both accurate and efficient by leveraging the unique computational advantages of DSMs. DS-TS integrates three key innovations: (1) Excitatory-Inhibitory Inspired Coupling to better model complex spatial interactions; (2) State-aware Dynamic Nonlinearity to enable rich inter-node interactions and state-dependent spatiotemporal correlations; and (3) Hierarchical Temporal Integration to capture high-order temporal dependencies. Experiments demonstrate that DS-TS achieves high-fidelity solutions while delivering orders-of-magnitude improvements in speed ($\sim 10^3\times$) and energy efficiency ($\sim 10^5\times$) compared to baseline solvers.

## One-Sentence Claim

DS-TS solves time-dependent differential equations by using physical dynamical-system computation to achieve high-fidelity trajectories with large speed and energy-efficiency gains.

## Problem

Time-dependent differential equation solvers face a latency-accuracy tradeoff from time discretization: small steps improve fidelity but are too slow for real-time use, while large steps distort trajectories.

## Core Contribution

The paper introduces DS-TS, a dynamical-system-machine solver that adds excitatory-inhibitory coupling, state-aware dynamic nonlinearity, and hierarchical temporal integration to better capture TDDE spatiotemporal complexity.

## Method

DS-TS leverages continuous physical evolution as computation. Its architecture models complex spatial interactions, state-dependent nonlinear correlations, and high-order temporal dependencies.

## Experiments and Evidence

The abstract reports high-fidelity solutions with about 1000x speed improvement and 100000x energy-efficiency improvement over baseline solvers.

## Limits and Failure Modes

No local PDF/text is currently available. Checks needed: hardware assumptions, problem classes, numerical stability, precision limits, calibration overhead, and whether reported energy gains include full system costs.

## Deep Themes

- Hardware and physical computation are re-entering ML as algorithmic substrates.
- Scientific computing workloads are pressuring latency/energy limits.
- Solver design can exploit continuous dynamics rather than only digital discretization.

## Subthemes

- Time-dependent differential equations.
- Dynamical system machines.
- Physical computation.
- Energy-efficient solvers.
- Scientific ML hardware.

## Connections to Other Papers

Connects to scientific ML, efficient computation, and hybrid systems that combine learned or designed dynamics with formal problem structure.

## Notes for Cross-Paper Synthesis

This broadens the efficiency theme beyond neural-network compression: some 2026 work changes the computational substrate itself to escape digital latency/energy tradeoffs.
