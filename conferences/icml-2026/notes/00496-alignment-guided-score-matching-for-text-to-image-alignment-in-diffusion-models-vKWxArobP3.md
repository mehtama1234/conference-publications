# Alignment-Guided Score Matching for Text-to-Image Alignment in Diffusion Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: vKWxArobP3
- Authors: Jaa-Yeon Lee; Yeobin Hong; Taesung Kwon; Jong Chul Ye
- Primary area: deep_learning->generative_models_and_autoencoders
- Keywords: diffusion model;contrastive learning;reinforcement learning;preference alignment
- Source URL: https://openreview.net/forum?id=vKWxArobP3
- PDF URL: https://openreview.net/pdf?id=vKWxArobP3

## Abstract

Diffusion models generate highly realistic images but often struggle with precise text–image alignment. While recent post-training methods improve alignment using external rewards or human preference signals, their performance heavily depends on reward quality and does not directly address alignment within the diffusion process itself.
Recent reward-free approaches such as SoftREPA demonstrate that optimizing soft text tokens via contrastive learning can effectively improve text-image representation alignment, outperforming standard parameter-efficient fine-tuning baselines. However, the contrastive formulation can excessively penalize negative pairs, which manifests as characteristic failure cases such as over-counting and
repetition.
To address this issue, we propose a lightweight, reward-free post-training method that refines soft tokens by integrating contrastive alignment guidance directly into the score-matching objective of diffusion models. By assigning alignment directions at the score level, our approach mitigates these limitations and yields more coherent and semantically faithful generations.
Experiments show that our method matches SoftREPA while substantially improving its failure cases, achieving over 35\% improvement in counting accuracy on the GenEval benchmark. Our method is seamlessly applicable to existing diffusion backbones (SD1.5, SDXL, and SD3), and is complementary to existing RL-based diffusion post-training methods.

## One-Sentence Claim

Alignment-guided score matching improves reward-free text-to-image alignment by injecting contrastive soft-token alignment directions directly into the diffusion score objective, reducing counting and repetition failures.

## Problem

Diffusion models generate realistic images but can fail on precise text-image alignment, especially compositional details such as object counts. Reward-based post-training depends heavily on reward or preference-model quality and may not directly repair the diffusion process.

Reward-free methods such as SoftREPA improve representation alignment by optimizing soft text tokens contrastively, but contrastive penalties can over-punish negative pairs and create failures like over-counting and repetition.

## Core Contribution

The paper proposes a lightweight reward-free post-training method that integrates contrastive alignment guidance into the diffusion score-matching objective. Instead of only optimizing soft tokens in representation space, it assigns alignment directions at the score level.

This produces more coherent and semantically faithful generations while remaining compatible with existing diffusion backbones and complementary to RL-based diffusion post-training.

## Method

Soft token refinement supplies alignment guidance, but the guidance is incorporated directly into score matching. The diffusion model is therefore encouraged to follow denoising directions that better match text-image semantics.

The method is lightweight and reward-free, avoiding explicit preference or reward models. It can be applied to SD1.5, SDXL, and SD3 backbones.

## Experiments and Evidence

The abstract reports that the method matches SoftREPA overall while substantially improving its failure cases, including more than 35 percent improvement in counting accuracy on GenEval. It applies across SD1.5, SDXL, and SD3.

Full-paper reading should verify benchmark suite, alignment metrics, qualitative failure categories, compute cost, and whether the method preserves image quality and diversity.

## Limits and Failure Modes

Reward-free alignment avoids reward-model errors but still depends on the quality of contrastive alignment directions. If representation alignment misses a semantic relation, score-level guidance may not fix it.

Counting gains on GenEval are promising, but compositional prompts include relations, attributes, spatial layout, and negation; these need separate validation.

## Deep Themes

- Alignment inside the generative process: guidance is applied at score level, not only output reward.
- Reward-free post-training: avoid external preference models while improving semantic faithfulness.
- Contrastive guidance with failure-mode control: reduce overcounting and repetition from excessive negative penalties.
- Backbone-compatible alignment: lightweight methods can layer onto existing diffusion systems.

## Subthemes

- Soft tokens are a control surface for text-image alignment.
- Score matching can carry semantic alignment directions.
- Counting accuracy is a diagnostic for compositional grounding.
- RL-based and reward-free diffusion alignment may be complementary.

## Connections to Other Papers

This paper connects to XDLM, any-order GPT, and GWF through diffusion/generative modeling, and to RACO in this same batch through reward-free alignment. It also relates to FIDIA because both align training with the actual generative objective rather than relying on generic likelihood.

It fits the broader alignment theme of moving corrections into the process that creates outputs.

## Notes for Cross-Paper Synthesis

The synthesis point is that alignment is migrating from external scoring to internal objectives. For diffusion, the denoising score itself becomes the place where semantic alignment is repaired.
