# NeuronCtrl: Geometry-Aware Safe Closed-Loop Generative Control for Neuronal Microenvironment Dynamics

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: ZK3h2ENA67
- Authors: Haowei Xu; Yixin Chen; Wanyi Fu; Hongbin Han; Zhaoheng Xie
- Primary area: applications->neuroscience_cognitive_science
- Keywords: Neuromodulation;computational neuroscience;closed-loop control;biophysical simulation;neural operator;surrogate modeling
- Source URL: https://openreview.net/forum?id=ZK3h2ENA67
- PDF URL: https://openreview.net/pdf?id=ZK3h2ENA67

## Abstract

Neuromodulation can be viewed as closed-loop control of high-dimensional spatiotemporal fields on irregular 3D morphologies, coupling membrane electrophysiology with ionic reaction--diffusion. This view supports high-rate feedback and systematic in-silico evaluation, yet is difficult in practice. Unlike classical PDE control with known equations on regular domains, neuronal microenvironments exhibit complex, often unknown biophysics on irregular shapes. High-fidelity simulators are too costly for real-time control with repeated planning. The discretized field is sparsely observed and must satisfy hard full-field safety constraints. We introduce NeuronCtrl, a modular operator-level framework for safe, closed-loop generative control of neuronal microenvironment dynamics. Given measurements, actions, and morphology, a history-conditioned observer infers the latent field, a morphology-aware neural operator predicts one-step dynamics, and a flow-matching conditional flow proposes actions conditioned on user preferences. Safety is enforced via complementary barrier-based mechanisms at both the action and field levels, with minimal intervention. When latency is critical, the multi-step generator is distilled into a single-step policy while retaining the same safety filter. Experiments across three high-fidelity 3D neuromodulation benchmarks spanning deep brain stimulation, extracellular reaction--diffusion control, and astrocytic potassium regulation demonstrate improved trade-offs among cost, safety, and latency. Code is available at https://github.com/HowieHsu0126/NeuronControl.

## One-Sentence Claim

NeuronCtrl performs safe closed-loop neuromodulation by combining latent field observation, morphology-aware neural operators, conditional flow action generation, and action/field barrier filters.

## Problem

Neuromodulation can be framed as controlling high-dimensional spatiotemporal fields over irregular 3D neuronal morphologies, coupling electrophysiology with ionic reaction-diffusion. Classical PDE control assumes known equations and regular domains, while real neuronal microenvironments have complex, partially unknown biophysics.

High-fidelity simulators are too slow for real-time planning, observations are sparse, and safety constraints apply to the full field.

## Core Contribution

The paper introduces NeuronCtrl, a modular operator-level framework for safe closed-loop generative control of neuronal microenvironment dynamics. It combines:

- A history-conditioned observer to infer latent fields from measurements, actions, and morphology.
- A morphology-aware neural operator for one-step dynamics.
- A flow-matching conditional flow that proposes preference-conditioned actions.
- Complementary barrier-based safety mechanisms at action and field levels.
- Optional distillation of the multi-step generator into a single-step policy for low latency.

## Method

NeuronCtrl estimates hidden full-field state, predicts dynamics with a neural operator respecting morphology, and generates candidate control actions with conditional flow matching. Safety filters intervene minimally to keep actions and predicted fields within hard constraints.

When latency matters, the learned multi-step controller is distilled into a faster single-step policy while preserving the safety filter.

## Experiments and Evidence

Evidence reported in the abstract:

- Three high-fidelity 3D neuromodulation benchmarks.
- Deep brain stimulation, extracellular reaction-diffusion control, and astrocytic potassium regulation.
- Improved cost/safety/latency tradeoffs.
- Barrier-based safety at action and field levels.
- Code release.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: simulator fidelity, safety constraints, observer architecture, neural operator design, and latency measurements.

## Limits and Failure Modes

- In-silico benchmarks may not capture biological variability or clinical constraints.
- Sparse observations can make full-field safety uncertain.
- Neural-operator errors can compound in closed-loop control.
- Barrier filters depend on accurate constraint models and may be conservative.

## Deep Themes

**Scientific control needs learned surrogates plus safety filters.** NeuronCtrl uses generative control but keeps hard constraints outside the generator.

**Irregular morphology is part of the dynamics.** The geometry of the biological substrate shapes prediction and control.

**Latency changes architecture.** Multi-step planners may need distillation for real-time use.

## Subthemes

- Closed-loop neuromodulation.
- Morphology-aware neural operators.
- Flow-matching action generation.
- Barrier safety at action and field levels.
- Single-step policy distillation.

## Connections to Other Papers

Connects to Flowers, FlowOptimizer, Flow Sampling, TimeRewarder, and scientific control/generation papers. It also links to PAVE because both treat smooth, safe control as a field-level problem.

## Notes for Cross-Paper Synthesis

NeuronCtrl is a dense example of the scientific-control theme: learned generative models are useful only when embedded inside observers, operators, safety filters, and latency-aware deployment loops.
