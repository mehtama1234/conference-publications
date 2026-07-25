# UDM-GRPO: Stable and Efficient Group Relative Policy Optimization for Uniform Discrete Diffusion Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: WJcFtJriqv
- Authors: Jiaqi Wang; Haoge Deng; Ting Pan; Yang Liu; Chengyuan Wang; Fan Zhang; Yonggang Qi; Xinlong Wang
- Primary area: deep_learning->generative_models_and_autoencoders
- Keywords: reinforcement learning;discrete flow matching;text-to-image generation
- Source URL: https://openreview.net/forum?id=WJcFtJriqv
- PDF URL: https://openreview.net/pdf?id=WJcFtJriqv

## Abstract

Uniform Discrete Diffusion Model (UDM) has recently emerged as a promising paradigm for discrete generative modeling; however, its integration with reinforcement learning remains largely unexplored. We observe that naively applying GRPO to UDM leads to training instability and marginal performance gains. To address this, we propose **UDM-GRPO**, the first framework to integrate UDM with RL. Our method is guided by two key insights: (i) treating the final clean sample as the action provides more accurate and stable optimization signals; and (ii) reconstructing trajectories via the diffusion forward process better aligns probability paths with the pretraining distribution. Additionally, we introduce two strategies, Reduced-Step and CFG-Free, to further improve training efficiency. **UDM-GRPO** significantly improves base model performance across multiple T2I tasks. Notably, GenEval accuracy improves from $69\\%$ to $96\\%$ and PickScore increases from $20.46$ to $23.81$, achieving state-of-the-art performance in both continuous and discrete settings. On the OCR benchmark, accuracy rises from $8\\%$ to $57\\%$, further validating the generalization ability of our method. Code is available at https://github.com/Yovecent/UDM-GRPO.

## One-Sentence Claim

UDM-GRPO stabilizes RL for uniform discrete diffusion by treating the final clean sample as the action and reconstructing trajectories through the diffusion forward process.

## Problem

Uniform Discrete Diffusion Models are promising for discrete generation, including text-to-image settings, but their reinforcement-learning post-training behavior is underexplored. Naively applying Group Relative Policy Optimization gives unstable training and limited gains.

The paper asks how to align RL optimization signals with the probability paths and pretraining distribution of discrete diffusion models.

## Core Contribution

The paper introduces UDM-GRPO, described as the first framework integrating UDMs with RL. It is based on two main insights:

- Use the final clean sample as the action to get more accurate and stable optimization signals.
- Reconstruct trajectories through the diffusion forward process so probability paths better match pretraining.

It also introduces Reduced-Step and CFG-Free strategies for training efficiency.

## Method

UDM-GRPO adapts group-relative RL to the discrete diffusion setting by redefining the action at the sample level rather than at every noisy transition. It then reconstructs the corresponding diffusion trajectory through the forward process to preserve distributional alignment.

The efficiency variants reduce sampling/training burden and remove classifier-free guidance overhead where possible.

## Experiments and Evidence

Evidence reported in the abstract:

- Multiple text-to-image tasks.
- GenEval accuracy improves from 69 percent to 96 percent.
- PickScore improves from 20.46 to 23.81.
- OCR benchmark accuracy improves from 8 percent to 57 percent.
- State-of-the-art performance in both continuous and discrete settings.
- Code release.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: base UDM model, reward models, GRPO objective, sample efficiency, and robustness to reward hacking.

## Limits and Failure Modes

- RL for image generation can overfit reward models or degrade diversity.
- Treating final samples as actions may hide credit-assignment issues for intermediate denoising steps.
- OCR gains may depend on benchmark or prompt distributions.
- CFG-Free and Reduced-Step variants need quality/speed tradeoff inspection.

## Deep Themes

**Post-training must match the generative process.** RL works better when actions and trajectories are defined in the model's native diffusion semantics.

**Diffusion RL is becoming sample-level.** The clean sample, not each denoising token, becomes the stable optimization object.

**Efficiency and stability are coupled.** Reduced-step and CFG-free designs aim to make RL-improved generation deployable rather than only accurate.

## Subthemes

- GRPO for uniform discrete diffusion.
- Final clean sample as action.
- Forward-process trajectory reconstruction.
- Text-to-image RL post-training.
- CFG-free diffusion optimization.

## Connections to Other Papers

Connects to R2VPO, TD3B, WeDLM, LatentLM, and diffusion fine-tuning/control papers. It also links to OCE and GEM because diffusion models are being modified by increasingly process-aware objectives rather than generic updates.

## Notes for Cross-Paper Synthesis

UDM-GRPO extends the post-training theme into discrete diffusion: optimization signals must be aligned with the model's actual generative path, not bolted on from a mismatched RL abstraction.
