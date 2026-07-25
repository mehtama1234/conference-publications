# Enhancing Reasoning for Diffusion LLMs via Distribution Matching Policy Optimization

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 09CSjVeDug
- Authors: Yuchen Zhu; Wei Guo; Jaemoo Choi; Petr Molodyk; Bo Yuan; Molei Tao; Yongxin Chen
- Primary area: probabilistic_methods
- Keywords: Fine-tuning;Diffusion Large Language Model;Policy Optimization
- Source URL: https://openreview.net/forum?id=09CSjVeDug
- PDF URL: https://openreview.net/pdf?id=09CSjVeDug

## Abstract

Diffusion large language models (dLLMs) are promising alternatives to autoregressive large language models (AR-LLMs), as they potentially allow higher inference throughput. Reinforcement learning (RL) is crucial to enabling dLLMs to achieve performance comparable to that of AR-LLMs on important tasks, such as reasoning. However, RL algorithms well-suited to dLLMs' unique characteristics have yet to be developed. This paper proposes \textbf{Distribution Matching Policy Optimization (DMPO)}, a principled and theoretically grounded RL fine-tuning method specifically designed to enhance the reasoning capabilities of dLLMs by matching the dLLM policy distribution to the optimal, reward-tilted one through cross-entropy optimization. We identify a key implementation challenge with small training batch sizes and propose several effective solutions based on a novel weight baseline subtraction technique. DMPO exhibits superior performance on multiple reasoning benchmarks without supervised fine-tuning, achieving up to a $39.63$ percentage-point improvement in accuracy over prior non-DMPO RL baselines and $67.97$ percentage points over the base model, underscoring the effectiveness of the distribution-matching framework. Our code is available at https://github.com/yuchen-zhu-zyc/DMPO.

## One-Sentence Claim

DMPO improves diffusion LLM reasoning by fine-tuning the model policy toward an optimal reward-tilted distribution through distribution matching rather than directly importing autoregressive RL methods.

## Problem

Diffusion LLMs promise higher inference throughput than autoregressive LLMs, but their reasoning quality lags without RL methods tailored to their non-autoregressive/diffusion structure.

## Core Contribution

The paper proposes Distribution Matching Policy Optimization, a theoretically grounded RL fine-tuning method for dLLMs, plus weight-baseline subtraction techniques to handle small-batch implementation challenges.

## Method

DMPO matches the dLLM policy distribution to an optimal reward-tilted distribution using cross-entropy optimization. It avoids supervised fine-tuning and addresses high-variance/small-batch training through a weight baseline subtraction mechanism.

## Experiments and Evidence

The abstract reports improvements across reasoning benchmarks: up to 39.63 percentage points over prior non-DMPO RL baselines and 67.97 points over the base model.

## Limits and Failure Modes

PDF checks needed: benchmark breadth, reward model or verifier assumptions, compute cost, sensitivity to diffusion sampling steps, and whether gains hold beyond reasoning tasks.

## Deep Themes

- Diffusion language models need their own post-training algorithms.
- Reasoning improvements are increasingly framed as distribution-level policy matching.
- Throughput and reasoning quality are being jointly optimized.

## Subthemes

- Diffusion LLMs.
- RL fine-tuning.
- Distribution matching.
- Reward-tilted policies.
- Reasoning benchmarks.

## Connections to Other Papers

Connects to RAGEN-2 through RL for reasoning, to UnMaskFork/MrRoPE through nonstandard inference for LLMs, and to generative modeling papers that treat diffusion as a general computation family.

## Notes for Cross-Paper Synthesis

This reinforces the theme that alternatives to autoregressive LLMs are maturing, but need bespoke inference and training algorithms rather than copied AR-LLM recipes.

## Full-Text Upgrade

Source used: `conferences/icml-2026/text/00007-enhancing-reasoning-for-diffusion-llms-via-distribution-matching-policy-optimization-09CSjVeDug-arxiv.txt`.

Additional verified details:

- DMPO is framed as reward maximization converted into distribution matching against an optimal reward-tilted policy.
- The paper emphasizes that dLLM denoising makes direct reuse of autoregressive RL baselines inadequate.
- The small-batch failure mode is mode-coverage error: a limited batch may miss good response modes, causing uncorrected positive weights on bad responses to push the policy in the wrong direction.
- Weight-baseline subtraction is introduced to counteract this small-batch update pathology; the full text describes group, individual, and model baseline variants.
- Experiments apply DMPO to LLaDA-Instruct 8B and Dream-Instruct 7B, with reasoning benchmarks including math and Sudoku-style tasks.
- The text reports that DMPO can work without supervised fine-tuning, can improve already post-trained variants, and can exploit faster dLLM samplers for training acceleration.

Refined limits:

- The conclusion states that performance on tasks beyond reasoning remains an important future direction.
- Better weight-baseline design is left open.
- The method depends on reward-tilted distribution construction and rollout sampling quality.
