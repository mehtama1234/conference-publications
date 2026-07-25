# PonderLM-2: Pretraining LLM with Latent Thoughts in Continuous Space

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: yVFxjNzCQm
- Authors: Boyi Zeng; He Li; Shixiang Song; Yixuan Wang; Zitong Wang; Ziwei He; Xinbing Wang; Zhouhan Lin
- Primary area: deep_learning->large_language_models
- Keywords: Pretraining;language modeling;Latent Thoughts;Continuous Space
- Source URL: https://openreview.net/forum?id=yVFxjNzCQm
- PDF URL: https://openreview.net/pdf?id=yVFxjNzCQm

## Abstract

The remarkable success of Chain-of-Thought (CoT), which enhances performance by scaling generation steps at test-time, inspires us to ask: can we leverage a similar scaling of computational steps during pretraining to improve the generation of each individual token? To address this, we propose a novel pre-training methodology: Pretraining Language Models with Latent Thoughts (PonderLM-2). Our approach pretrains a language model (LM) to first generate an intermediate latent thought—the last hidden
state of the current position—which is then used as input to predict the actual subsequent token. This additional computational step enables the LM to refine its prediction within unconstrained continuous space. Our experiments demonstrate that, at an identical inference cost, a LM that generates one additional latent thought per token outperforms a standard model with double the parameters. For instance, our PonderLM-2-Pythia-1.4B, pretrained on 300B tokens from the Pile, significantly surpasses the vanilla Pythia-2.8B trained on the same data on both language modeling and a range of general downstream tasks. Furthermore, increasing the number of latent thoughts generated before each actual token—forming a chain analogous to CoT—consistently improves the model's performance. The code and models are available at https://github.com/LUMIA-Group/PonderLM-2.

## One-Sentence Claim

PonderLM-2 improves language-model pretraining by adding latent continuous "thought" steps before token prediction, giving extra per-token computation without emitting extra text.

## Problem

Chain-of-thought improves performance by spending more generation steps at test time, but those steps are discrete, visible, and usually added after pretraining. Standard language-model pretraining predicts the next token directly from the current hidden state.

The paper asks whether a model can use extra computational steps during pretraining to refine each token prediction in continuous hidden-state space.

## Core Contribution

The paper proposes PonderLM-2, a pretraining method where the model first generates an intermediate latent thought, defined as the last hidden state of the current position, and then uses that latent thought to predict the next token.

The contribution is to turn per-token prediction into a short internal refinement process. Multiple latent thoughts can form a continuous-space chain analogous to CoT, but without producing intermediate text tokens.

## Method

During pretraining, the model learns to generate a latent hidden-state thought before predicting the next actual token. This additional internal step lets the model refine predictions in unconstrained continuous space.

The method can increase the number of latent thoughts before each token, scaling computation similarly to a chain of thought while keeping the output sequence unchanged.

## Experiments and Evidence

The abstract reports that, at identical inference cost, a model with one additional latent thought per token outperforms a standard model with double the parameters.

It specifically reports that PonderLM-2-Pythia-1.4B pretrained on 300B Pile tokens significantly surpasses vanilla Pythia-2.8B trained on the same data on language modeling and downstream tasks. Increasing latent thoughts consistently improves performance.

## Limits and Failure Modes

Latent thoughts add internal computation and training complexity. The comparison depends on how "identical inference cost" is measured, and hidden-state thoughts may be harder to inspect than textual reasoning traces.

Because this note is abstract-only, details still need checking: architecture changes, training objective, compute accounting, downstream task suite, stability with multiple latent thoughts, and whether latent thoughts improve reasoning or mostly language-modeling perplexity.

## Deep Themes

- Continuous internal reasoning: extra computation can happen in hidden space instead of emitted text.
- Test-time scaling moved into pretraining: the model learns to use more per-token compute before deployment.
- Compute versus parameters: latent steps can outperform simply doubling parameter count under some budgets.
- Hidden process opacity: latent thoughts may improve capability while making reasoning less directly auditable.

## Subthemes

- Per-token latent refinement.
- Continuous-space chain of thought.
- Pythia-scale pretraining comparison.
- Inference-cost-controlled scaling.

## Connections to Other Papers

This connects to Ctrl-R, H1, reasoning dimensionality, and Stop When Further Reasoning Won't Help through the broad theme of allocating computation to reasoning processes.

It also relates to Learning-to-Theorize and latent program work because both move explanatory or reasoning structure into latent internal states rather than only observable outputs.

## Notes for Cross-Paper Synthesis

PonderLM-2 adds a hidden-computation branch to the reasoning-scaling theme: models may become better by learning internal deliberation steps that are continuous and not directly text-visible.
