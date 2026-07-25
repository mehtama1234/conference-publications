# From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 2NRrsz4nUB
- Authors: Bing Hu; Zaijing Li; Rui Shao; Junda Chen; April Hua Liu; Wei-Shi Zheng; Liqiang Nie
- Primary area: applications->robotics
- Keywords: Robotic Manipulation;Vision-Language-Action Model;Flow Matching
- Source URL: https://openreview.net/forum?id=2NRrsz4nUB
- PDF URL: https://openreview.net/pdf?id=2NRrsz4nUB

## Abstract

Vision-Language-Action (VLA) models often suffer from performance degradation under distribution shifts, as they struggle to learn generalized behavior representations across varying environments. While existing approaches attempt to construct behavior representations through action-centric latent variables, they are often limited by short-horizon temporal fragmentation and static execution-alignment, leading to inconsistent behaviors in complex scenarios. To address these limitations, we propose \textbf{BehaviorVLA}, a framework that facilitates robust manipulation through the learning of a temporally coherent behavioral representations. Our approach features two symmetric components: (1) the \textbf{Visuomotor Behavior Encoder (VBE)}, which utilizes a causal Mamba-based architecture to aggregate long-horizon trajectory information into a unified behavior representation; and (2) the \textbf{Phase-conditioned Behavior Decoder (PBD)}, which decodes this representation into precise actions by dynamically aligning task-level priors with real-time execution progress. Experiments on RoboTwin 2.0, LIBERO, and CALVIN demonstrate state-of-the-art success rates of 58\%, 98\%, and 4.36 (Avg.Len), respectively. Notably, in real-world sim-to-real transfer, BehaviorVLA matches the performance of OpenVLA-OFT using only 50\% of the demonstration data, showcasing its superior data efficiency and generalization.

## One-Sentence Claim

BehaviorVLA improves VLA robot manipulation under distribution shift by learning long-horizon, temporally coherent behavior representations and decoding them with phase-aware execution alignment.

## Problem

VLA models degrade under distribution shifts because action-centric latent variables often fragment behavior over short horizons and align statically to execution, producing inconsistent manipulation in complex scenarios.

## Core Contribution

The paper introduces BehaviorVLA, combining a Visuomotor Behavior Encoder and Phase-conditioned Behavior Decoder to represent behavior abstractly over long trajectories and instantiate precise actions during execution.

## Method

VBE uses a causal Mamba-based architecture to aggregate long-horizon trajectory information into a unified behavior representation. PBD decodes that representation by dynamically aligning task-level priors with real-time execution progress.

## Experiments and Evidence

The abstract reports state-of-the-art success rates on RoboTwin 2.0, LIBERO, and CALVIN, plus sim-to-real transfer matching OpenVLA-OFT with 50% of the demonstration data.

## Full-Text Upgrade

The full text clarifies that BehaviorVLA is not merely adding a larger policy head; it splits behavior learning into two explicit modules. The Visuomotor Behavior Encoder uses separate vision, action, and behavior streams with causal Mamba layers, then cross-attention, to turn long-horizon trajectory history into a stable behavioral prior. The Phase-conditioned Behavior Decoder then conditions action generation on execution progress, directly addressing phase misalignment during sim-to-real transfer.

The benchmark evidence is stronger than the abstract alone suggested. The paper reports evaluation on 20 randomly selected hard RoboTwin 2.0 tasks, LIBERO suites, CALVIN ABC-to-D, and a real-world sim-to-real setting. It reports 58% RoboTwin hard success, 98% average LIBERO success, 4.36 average CALVIN sequence length, and competitive real-world transfer with 50% and 75% training-data regimes. The appendix also states that RoboTwin uses clean expert demonstrations from 50 standard tasks and 224x224 visual observations, which matters because the behavioral representation is learned from relatively structured trajectories rather than unconstrained web-scale interaction logs.

## Limits and Failure Modes

Limits to watch: the evidence is still concentrated in manipulation benchmarks with structured demonstrations; phase conditioning may depend on reliable progress estimation; and the benefit of long-horizon behavioral abstraction outside robot-control domains remains open.

## Deep Themes

- Robotics models need temporal behavioral abstractions.
- Data efficiency and sim-to-real transfer depend on representation structure.
- VLA research is moving from action prediction toward behavior-level modeling.

## Subthemes

- Vision-language-action models.
- Robotic manipulation.
- Behavior representations.
- Causal sequence models.
- Phase-conditioned action decoding.

## Connections to Other Papers

Connects to MomaGraph, FlashWorld, and multimodal embodied reasoning papers. It is a policy-side counterpart to MomaGraph's scene-representation approach.

## Notes for Cross-Paper Synthesis

BehaviorVLA strengthens the embodied AI theme: robust action requires structured representations across time, not only better visual-language grounding.
