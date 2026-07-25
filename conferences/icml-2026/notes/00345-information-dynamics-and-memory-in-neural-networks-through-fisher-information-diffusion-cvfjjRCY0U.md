# Information dynamics and Memory in Neural Networks through Fisher Information Diffusion

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: cvfjjRCY0U
- Authors: Haodong Qin; Tatyana Sharpee
- Primary area: theory->deep_learning
- Keywords: Recurrent Neural Networks;Fisher Information;Initialization;Gradient Stability;Mean-Field Theory
- Source URL: https://openreview.net/forum?id=cvfjjRCY0U
- PDF URL: https://openreview.net/pdf?id=cvfjjRCY0U

## Abstract

We present a general theoretical framework for analyzing how information about past inputs is encoded in recurrent networks into evolving dynamics rather than being represented as convergence to static attractors. Using dynamic mean-field theory and diffusion from physics, we derive a Fisher information diffusion operator that links network connectivity structure to the time-resolved propagation of information across interacting subpopulations. The analysis reveals that operating near criticality (spectral radius near one) is necessary but not sufficient for reliable memory in structured or non-normal recurrent networks; effective information retention requires alignment between input–output structure and stable dynamical subspaces. The theory yields principled initialization rules that balance stability and sensitivity, mitigating vanishing and exploding gradients. Experiments on the copy task and sequential MNIST show faster convergence and higher accuracy than standard random initialization. Together, these results provide both principled design guidelines for recurrent networks and new theoretical insight into how information can be preserved over time in their dynamics.

## One-Sentence Claim

Fisher information diffusion explains recurrent-network memory as time-resolved information propagation through stable dynamical subspaces, not merely operation near criticality.

## Problem

Recurrent networks must preserve information about past inputs, but memory is often discussed through static attractors or simple criticality conditions. In structured or non-normal recurrent networks, spectral radius near one may be necessary but insufficient for reliable memory.

The paper asks how connectivity structure governs dynamic memory propagation over time.

## Core Contribution

The paper develops a theoretical framework using dynamic mean-field theory and diffusion from physics. It derives a Fisher information diffusion operator linking network connectivity to time-resolved information propagation across interacting subpopulations.

The analysis shows effective memory requires alignment between input-output structure and stable dynamical subspaces. It yields initialization rules balancing stability and sensitivity, mitigating vanishing/exploding gradients.

## Method

The method tracks Fisher information about past inputs as it diffuses through recurrent dynamics. Dynamic mean-field theory approximates population behavior, while the diffusion operator reveals which subspaces retain information and which dissipate it.

Initialization rules are derived to place dynamics in regimes where information is preserved without unstable gradient growth.

## Experiments and Evidence

Evidence reported in the abstract:

- Fisher information diffusion operator.
- Theory linking connectivity to memory propagation across subpopulations.
- Criticality is necessary but not sufficient.
- Input-output alignment with stable subspaces is required.
- Principled initialization rules.
- Copy task and sequential MNIST experiments.
- Faster convergence and higher accuracy than standard random initialization.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: recurrent architectures, mean-field assumptions, subspace alignment measure, and initialization formulas.

## Limits and Failure Modes

- Mean-field assumptions may not hold for all finite or gated recurrent models.
- Copy task and sequential MNIST are controlled benchmarks.
- Results may transfer only partly to Transformer-style memory.
- Measuring stable dynamical subspaces in large networks can be difficult.

## Deep Themes

**Memory is dynamic information flow.** Past inputs are preserved through evolving subspaces, not static storage alone.

**Criticality is incomplete.** Spectral radius near one must be aligned with input-output structure.

**Initialization can encode memory geometry.** Stability and sensitivity are balanced before training begins.

## Subthemes

- Fisher information diffusion.
- Dynamic mean-field recurrent theory.
- Stable subspace alignment.
- Vanishing/exploding gradient mitigation.
- Sequential memory initialization.

## Connections to Other Papers

Connects to DLMR, FacRNN, AI Engram, Neural Ricci Flow, and recurrent/equivariant dynamics papers. It also links to Monitoring Monitorability because both study whether internal process traces preserve relevant information over time.

## Notes for Cross-Paper Synthesis

This paper adds a memory-dynamics lens: reliable long-horizon behavior depends on how information diffuses through stable subspaces, not just on context length or recurrence.
