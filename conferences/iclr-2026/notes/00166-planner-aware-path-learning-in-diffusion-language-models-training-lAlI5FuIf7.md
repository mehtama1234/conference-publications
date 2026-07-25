# Planner Aware Path Learning in Diffusion Language Models Training

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: lAlI5FuIf7
- Authors: Fred Zhangzhi Peng; Zachary Bezemek; Jarrid Rector-Brooks; Shuibai Zhang; Michael M. Bronstein; Anru Zhang; Joey Bose; Alexander Tong
- Primary area: generative models
- Keywords: Diffusion Language Models;Discrete Diffusion;Diffusion Models;code generation;protein generation;text generation
- Source URL: https://openreview.net/forum?id=lAlI5FuIf7
- PDF URL: https://openreview.net/pdf?id=lAlI5FuIf7

## Abstract

Diffusion language models have emerged as a powerful alternative to autoregressive models, enabling fast inference through more flexible and parallel generation paths. This flexibility of sampling is unlocked by new engineered sampling strategies, or *planners*, that select more favorable generation paths by iteratively planning---versus uniformly at random---where to denoise along the sequence. However, by modifying the reverse paths via planning, planners create an irrevocable mismatch between the uniformly random denoising paths during training and planning-based inference. In this paper, we systematically investigate the mismatch of discrete diffusion training and inference under planning and theoretically prove that the standard discrete diffusion training evidence lower bound (ELBO) does not accurately describe a denoiser that uses a non-uniform planner. To address this gap, we derive a new planned evidence lower bound (P-ELBO) that incorporates planner-based reverse dynamics directly into the training objective.
Using the P-ELBO, we introduce *Planner Aware Path Learning* (PAPL), a novel training scheme that aligns training and inference under a planned denoiser.
PAPL is implemented as a simple yet effective modification to the standard masked discrete diffusion loss, making it widely applicable and easy to adopt.
Empirically, we show PAPL delivers consistent gains across domains, including a 40\% relative improvement in protein sequences, improved text generation with up to a $4\times$ relative MAUVE gain, and 23\% relative improvement in code generation HumanEval pass@10.

## One-Sentence Claim

PAPL aligns discrete diffusion language model training with planner-based inference by replacing the standard uniform-path ELBO with a planner-aware training objective.

## Problem

Diffusion language models can use planners that choose favorable denoising positions and enable fast parallel generation. But standard training assumes uniformly random reverse paths, creating a mismatch when inference uses non-uniform planned denoising.

## Core Contribution

The paper proves that the standard discrete diffusion ELBO does not accurately describe a denoiser using a non-uniform planner, derives a planned evidence lower bound, and introduces Planner Aware Path Learning as a practical loss modification.

## Method

PAPL incorporates planner-based reverse dynamics into the discrete diffusion training objective. It modifies the standard masked diffusion loss so denoisers learn along the same planned paths used at inference, while keeping implementation simple enough to apply across domains.

## Experiments and Evidence

The abstract reports consistent gains across protein, text, and code generation: 40 percent relative improvement in protein sequences, up to 4x relative MAUVE gain for text, and 23 percent relative HumanEval pass@10 improvement for code.

## Limits and Failure Modes

Planner-aware training may depend strongly on the planner family and may overfit to one inference schedule. Gains could shrink if planners change, if generation requires diverse paths, or if planner computation offsets speed benefits. Full-text review should check P-ELBO derivation assumptions, planner definitions, baselines, and whether training remains robust across sampling strategies.

## Deep Themes

- Training-inference alignment for diffusion language models.
- Planner-aware objectives.
- Non-autoregressive generation paths.
- Fast generation through structured denoising.

## Subthemes

- Planned evidence lower bound.
- Discrete diffusion ELBO mismatch.
- Masked diffusion loss modification.
- Code, text, and protein sequence generation.
- Planner-dependent denoiser behavior.

## Connections to Other Papers

Connects to Prophet and LPD through generation-path control, to diffusion RL/post-training papers through DLM-specific objectives, and to broader process-optimization themes where inference strategies must be reflected in training.

## Notes for Cross-Paper Synthesis

PAPL reinforces a recurring lesson: if inference uses a smarter process than training assumes, the objective must be updated to match that process. Flexible generation paths create both opportunity and distribution shift.
