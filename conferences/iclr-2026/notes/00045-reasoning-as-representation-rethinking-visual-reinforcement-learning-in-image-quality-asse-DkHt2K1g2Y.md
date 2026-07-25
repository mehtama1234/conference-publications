# Reasoning as Representation: Rethinking Visual Reinforcement Learning in Image Quality Assessment

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: DkHt2K1g2Y
- Authors: Shijie Zhao; Xuanyu Zhang; Weiqi Li; Junlin Li; Li zhang; Tianfan Xue; Jian Zhang
- Primary area: reinforcement learning
- Keywords: Image Quality Assessment;Low Level Vision;Multimodal Large Language Model
- Source URL: https://openreview.net/forum?id=DkHt2K1g2Y
- PDF URL: https://openreview.net/pdf?id=DkHt2K1g2Y

## Abstract

Reasoning-based image quality assessment (IQA) models trained through reinforcement learning (RL) exhibit exceptional generalization, yet the underlying mechanisms and critical factors driving this capability remain underexplored in current research. Moreover, despite their superior performance, these models incur inference energy usage and latency orders of magnitude higher than their earlier counterparts, restricting their deployment in specific scenarios. Through extensive experiments, this paper verifies and elaborates that through RL training, MLLMs leverage their reasoning capability to convert redundant visual representations into compact, cross-domain aligned text representations. This conversion is precisely the source of the generalization exhibited by these reasoning-based IQA models. Building on this fundamental insight, we propose a novel algorithm, RALI, which employs contrastive learning to directly align images with these generalizable text representations learned by RL. This approach eliminates the reliance on reasoning processes and even obviates the need to load an LLM. For the quality scoring task, this framework achieves generalization performance comparable to reasoning-based models while requiring less than 5% of their model parameters and inference time.

## One-Sentence Claim

Reasoning-based IQA generalizes because RL converts redundant visual features into compact cross-domain text representations, which RALI then learns directly without expensive reasoning inference.

## Problem

Reasoning-based image quality assessment models trained with RL generalize well, but they are expensive at inference because they rely on MLLM reasoning processes.

The problem is to understand why reasoning helps IQA and then recover the benefit without paying the latency and energy cost of reasoning at deployment.

## Core Contribution

The paper argues that RL-trained reasoning converts redundant visual representations into compact, cross-domain aligned text representations, and that this conversion drives generalization.

It proposes RALI, a contrastive-learning algorithm that directly aligns images with these generalizable text representations learned by RL.

## Method

The authors analyze reasoning-based IQA models to identify the representation transformation induced by RL. RALI then trains a smaller model to map images to the text-representation space directly.

This removes the need to load an LLM or run explicit reasoning at inference for quality scoring.

## Experiments and Evidence

The abstract reports that RALI achieves generalization comparable to reasoning-based IQA models while using less than 5 percent of their model parameters and inference time.

The paper also reports extensive experiments supporting the claim that RL-induced reasoning representations are the source of generalization.

## Limits and Failure Modes

Distilling reasoning into compact representations may work for scalar quality scoring but may not preserve explanatory rationales or handle new quality dimensions not represented in the teacher reasoning.

Because this note is abstract-only, details still need checking: IQA datasets, RL setup, representation extraction, contrastive objective, parameter/time accounting, and robustness under severe distortions.

## Deep Themes

- Reasoning as representation learning: CoT-like reasoning can be valuable because of the intermediate representation it creates.
- Distilling away reasoning cost: expensive inference processes can become compact embeddings.
- Cross-domain alignment for low-level vision: text representations can organize visual-quality concepts.
- Deployment-aware reasoning: use reasoning during training or analysis, not necessarily at runtime.

## Subthemes

- Image quality assessment.
- RL-induced text representations.
- Contrastive image-text alignment.
- Lightweight reasoning-free scoring.

## Connections to Other Papers

This connects to PonderLM-2, OpenThoughts, ASAG, and coverage theory through reasoning process utility.

It also relates to PRISM and MetaphorVU because structured text representations bridge visual inputs and higher-level judgments.

## Notes for Cross-Paper Synthesis

This paper adds a reasoning-distillation theme: reasoning may be most useful as a way to learn compact transferable representations that later replace reasoning itself.
