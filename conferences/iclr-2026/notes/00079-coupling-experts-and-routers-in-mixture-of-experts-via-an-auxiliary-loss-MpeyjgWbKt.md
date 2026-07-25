# Coupling Experts and Routers in Mixture-of-Experts via an Auxiliary Loss

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: MpeyjgWbKt
- Authors: Ang Lv; Jin Ma; Yiyuan Ma; Siyuan Qiao
- Primary area: foundation or frontier models, including LLMs
- Keywords: Mixture-of-Experts;Large language models;Auxiliary loss;Expert-router coupling;Expert specialization
- Source URL: https://openreview.net/forum?id=MpeyjgWbKt
- PDF URL: https://openreview.net/pdf?id=MpeyjgWbKt

## Abstract

Traditional Mixture-of-Experts (MoE) models lack explicit constraints to ensure the router’s decisions align well with the experts’ capabilities, which ultimately limits model performance. To address this, we propose expert-router coupling loss (ERC loss), a lightweight auxiliary loss that couples expert capabilities and the router’s decisions. We treat each row of the router matrix as a cluster center for the tokens assigned to a particular expert. From these centers, we create proxy tokens by applying a perturbation with noise. Using these proxy tokens, the ERC loss forces the router and experts to satisfy two constraints: (1) each expert exhibits higher activation for its corresponding proxy token than for any other proxy token, and (2) each proxy token elicits stronger activation in its designated expert than in any other expert. This optimization leads to two key effects: each row of the router matrix is an accurate representation of its expert’s capabilities, while each expert develops expertise that closely match the tokens routed to it. Our experiments involve pre-training multiple 3B-parameter MoE-LLMs on trillions of tokens in total, providing detailed evidence of the ERC loss’s effectiveness. Additionally, the ERC loss offers flexible control and quantitative tracking of expert specialization levels during training, providing many valuable insights into MoEs.

## One-Sentence Claim

ERC loss explicitly couples MoE router decisions with expert capabilities so routing centers and expert specialization co-develop during large-scale pretraining.

## Problem

Mixture-of-Experts models rely on routers to assign tokens to experts, but standard training does not directly ensure that router choices align with what experts are good at.

This mismatch can limit performance, weaken specialization, and make it harder to understand or control expert behavior.

## Core Contribution

The paper introduces expert-router coupling loss, a lightweight auxiliary objective for MoE-LLMs.

ERC treats router-matrix rows as cluster centers for tokens assigned to experts, creates noisy proxy tokens from those centers, and enforces reciprocal alignment between proxy tokens and expert activations.

## Method

The loss imposes two constraints: each expert should activate more for its own proxy token than for others, and each proxy token should activate more in its designated expert than in other experts.

This encourages router rows to represent expert capabilities while experts specialize toward the tokens routed to them. The loss also provides a knob and measurement signal for specialization levels.

## Experiments and Evidence

The abstract reports pretraining multiple 3B-parameter MoE-LLMs over trillions of tokens in total.

Experiments provide evidence that ERC improves performance and allows quantitative tracking and flexible control of expert specialization.

## Limits and Failure Modes

Over-coupling could make experts too rigid, reducing transfer or load-balancing flexibility. Proxy-token perturbations may also encode a simplified view of expert capability.

Because this note is abstract-only, details still need checking: exact loss weight, proxy generation, load-balancing interaction, model architecture, downstream evaluations, specialization metrics, and training overhead.

## Deep Themes

- Router-expert alignment: sparse models need objectives that connect dispatch decisions to learned capabilities.
- Specialization as controllable training signal: expert roles become measurable and adjustable rather than accidental.
- Cluster geometry inside MoEs: router rows are interpreted as token-space centers.
- Auxiliary losses for scaling stability: small objectives can shape large sparse pretraining dynamics.

## Subthemes

- Mixture-of-Experts.
- Expert-router coupling.
- Proxy tokens.
- Expert specialization tracking.

## Connections to Other Papers

This connects to Switch-style MoE work, adapter routing, and SmartFed through conditional computation and expert selection.

It also relates to representation geometry papers because ERC turns routing weights into structured centers in token space.

## Notes for Cross-Paper Synthesis

ERC adds to the conditional-computation theme: scaling sparse models requires aligning routing mechanisms with the capacities of the modules they select.
