# Detecting the Semantic Fixed Point: A Geometric Framework for Efficient Inference

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: DACN5xM4h7
- Authors: Jiawei Gu; Ziyue Qiao; Xiao Luo
- Primary area: deep_learning->other_representation_learning
- Keywords: Representation Learning; Layer-wise Convergence
- Source URL: https://openreview.net/forum?id=DACN5xM4h7
- PDF URL: https://openreview.net/pdf?id=DACN5xM4h7

## Abstract

Each layer of a Transformer refines the hidden state toward a prediction, an iterative process resembling fixed-point iteration. Yet when should this iteration terminate? Existing early exit methods rely on output confidence as a proxy for internal convergence. We take a more direct approach by examining the geometry of the hidden state trajectory. We find that layer-wise updates exhibit a two-phase structure: large, volatile updates in early layers, followed by small, aligned updates as the model propagates an already-formed representation. The transition is remarkably sharp. This yields a simple criterion: exit when step size vanishes and direction stabilizes. We track the normalized update norm and cosine similarity between consecutive updates, exiting when both indicate convergence. The overhead is $O(d)$ per layer, independent of vocabulary size, requiring no learned components or architectural modifications. On LLaMA-2-7B and LLaMA-2-13B across question answering and commonsense reasoning tasks, this geometric criterion reduces FLOPs by 30--35\% while retaining over 98\% of full-depth accuracy.

## One-Sentence Claim

Transformer inference can exit early when hidden-state updates geometrically converge, reducing FLOPs while preserving accuracy without learned exit heads.

## Problem

Existing early-exit methods use output confidence as a proxy for internal convergence, but confidence may not directly reflect whether the representation has stabilized.

## Core Contribution

The paper proposes a geometric fixed-point criterion based on normalized update norm and cosine similarity between consecutive layer updates.

## Method

It observes a two-phase hidden-state trajectory: volatile early updates followed by small aligned refinements. The model exits when step size vanishes and direction stabilizes, with O(d) overhead per layer and no vocabulary-size dependence.

## Experiments and Evidence

The abstract reports 30-35% FLOP reductions on LLaMA-2-7B and 13B across QA and commonsense reasoning while retaining over 98% of full-depth accuracy.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: threshold selection, task-specific failure cases, calibration under distribution shift, and compatibility with generation workloads.

## Deep Themes

- Efficient inference can use representation-trajectory geometry directly.
- Layer computation resembles fixed-point iteration toward semantic convergence.
- Early exit can be architecture-preserving and vocabulary-independent.

## Subthemes

- Early exit.
- Semantic fixed point.
- Transformer hidden-state geometry.
- FLOP reduction.
- Layer-wise convergence.
- Efficient inference.

## Connections to Other Papers

Connects to FlexRank, OmniFit, TACO, EcoVLA, and Thinking in Flow through inference-time control based on internal state.

## Notes for Cross-Paper Synthesis

This paper adds a convergence-detection theme: models can stop computing when their internal trajectory has stabilized, not just when output confidence is high.
