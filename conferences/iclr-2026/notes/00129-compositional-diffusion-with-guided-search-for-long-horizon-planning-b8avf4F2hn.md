# Compositional Diffusion with Guided search for Long-Horizon Planning

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: b8avf4F2hn
- Authors: Utkarsh Aashu Mishra; David He; Yongxin Chen; Danfei Xu
- Primary area: applications to robotics, autonomy, planning
- Keywords: Diffusion Models;Compositional Diffusion;Goal-directed Planning
- Source URL: https://openreview.net/forum?id=b8avf4F2hn
- PDF URL: https://openreview.net/pdf?id=b8avf4F2hn

## Abstract

Generative models have emerged as powerful tools for planning, with compositional approaches offering particular promise for modeling long-horizon task distributions by composing together local, modular generative models. This compositional paradigm spans diverse domains, from multi-step manipulation planning to panoramic image synthesis to long video generation. However, compositional generative models face a critical challenge: when local distributions are multimodal, existing composition methods average incompatible modes, producing plans that are neither locally feasible nor globally coherent. We propose Compositional Diffusion with Guided Search (CDGS), which addresses this \emph{mode averaging} problem by embedding search directly within the diffusion denoising process. Our method explores diverse combinations of local modes through population-based sampling, prunes infeasible candidates using likelihood-based filtering, and enforces global consistency through iterative resampling between overlapping segments. CDGS matches oracle performance on seven robot manipulation tasks, outperforming baselines that lack compositionality or require long-horizon training data. The approach generalizes across domains, enabling coherent text-guided panoramic images and long videos through effective local-to-global message passing. More details: https://cdgsearch.github.io/

## One-Sentence Claim

CDGS embeds population-based guided search inside diffusion denoising to compose local multimodal distributions into globally coherent long-horizon plans.

## Problem

Compositional generative models can represent long-horizon tasks by composing local models, but local distributions are often multimodal.

Naive composition averages incompatible modes, yielding plans that are neither locally feasible nor globally coherent.

## Core Contribution

The paper introduces Compositional Diffusion with Guided Search.

CDGS explores combinations of local modes during denoising, prunes infeasible candidates with likelihood filtering, and enforces consistency through iterative resampling across overlapping segments.

## Method

The method integrates search directly into the diffusion denoising process.

Population-based sampling maintains diverse local-mode combinations, likelihood-based filters remove infeasible candidates, and overlapping-segment resampling passes messages from local constraints to global plan coherence.

## Experiments and Evidence

The abstract reports oracle-matching performance on seven robot manipulation tasks.

CDGS outperforms baselines without compositionality or requiring long-horizon training data, and generalizes to text-guided panoramic images and long videos through local-to-global message passing.

## Limits and Failure Modes

Population search can be compute-heavy, and likelihood filters may reject rare but valid plans. Generalization across domains needs careful comparison because robotics, panoramas, and video have different constraint structures.

Because this note is abstract-only, details still need checking: local model construction, population size, overlap scheme, oracle definition, robot tasks, and cross-domain evaluation protocol.

## Deep Themes

- Composition without mode averaging: long-horizon generation must preserve local multimodality.
- Search inside denoising: diffusion sampling becomes a planning algorithm, not only a generator.
- Local-to-global message passing: overlapping segments communicate constraints for coherence.
- Long-horizon planning from local data: compositionality reduces need for full long-horizon demonstrations.

## Subthemes

- Compositional diffusion.
- Guided search.
- Population-based sampling.
- Robot manipulation planning.

## Connections to Other Papers

This connects to PCD, Stable Video Infinity, DCFold, robotics MSP, and long-horizon planning papers.

It also relates to AgentFlow and Q-RAG because all use intermediate search/planning structure to manage long horizons.

## Notes for Cross-Paper Synthesis

CDGS adds a compositional-planning theme: global coherence often requires search over local modes rather than averaging them away.
