# DepthLM: Metric Depth from Vision Language Models

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: ObFVZGnSFN
- Authors: Zhipeng Cai; Ching-Feng Yeh; Hu Xu; Zhuang Liu; Gregory P. Meyer; Xinjie Lei; Changsheng Zhao; Shang-Wen Li; Vikas Chandra; Yangyang Shi
- Primary area: foundation or frontier models, including LLMs
- Keywords: Metric depth;Vision language model;Spatial reasoning
- Source URL: https://openreview.net/forum?id=ObFVZGnSFN
- PDF URL: https://openreview.net/pdf?id=ObFVZGnSFN

## Abstract

Vision language models (VLMs) can flexibly address various vision tasks through text interactions. Although successful in semantic understanding, state-of-the-art VLMs including GPT-5 still struggle in understanding 3D from 2D inputs. On the other hand, expert pure vision models achieve super-human accuracy in metric depth estimation, a key 3D understanding task. However, they require task-specific architectures and losses. Such difference motivates us to ask: Can VLMs reach expert-level accuracy without architecture or loss change? We take per-pixel metric depth estimation as the representative task and show that the answer is yes! Surprisingly, comprehensive analysis shows that text-based supervised-finetuning with sparse labels is sufficient for VLMs to unlock strong 3D understanding, no dense prediction head or complex regression/regularization loss is needed. The bottleneck lies in pixel reference and cross-dataset camera ambiguity, which we address through visual prompting and intrinsic-conditioned augmentation. With much smaller models, our method DepthLM surpasses the accuracy of most advanced VLMs by over 2x, making VLMs for the first time comparable with pure vision models. The simplicity of DepthLM also enables a single VLM to cover various 3D tasks beyond metric depth. Code and model are available at https://github.com/facebookresearch/DepthLM_Official.

## One-Sentence Claim

DepthLM shows that text-supervised fine-tuning with sparse labels, visual prompting, and intrinsic-conditioned augmentation can unlock expert-level metric depth estimation in VLMs without architecture or loss changes.

## Problem

VLMs handle semantic vision-language tasks well, but even strong systems struggle with 3D understanding from 2D images.

Expert depth models can achieve very high metric-depth accuracy, but they typically require task-specific architectures, dense prediction heads, and specialized losses.

## Core Contribution

The paper introduces DepthLM, a simple recipe for metric depth estimation using VLMs.

It argues that sparse text-based supervised fine-tuning is enough when two bottlenecks are addressed: pixel reference and cross-dataset camera ambiguity.

## Method

DepthLM uses visual prompting to give the VLM better pixel reference for per-pixel metric depth.

It also uses intrinsic-conditioned augmentation to handle ambiguity caused by different camera intrinsics across datasets. The method avoids dense prediction heads and complex regression or regularization losses.

## Experiments and Evidence

The abstract reports that DepthLM surpasses the accuracy of most advanced VLMs by more than 2x while using much smaller models.

It makes VLM depth estimation comparable with pure vision models for the first time and extends to other 3D tasks beyond metric depth.

## Limits and Failure Modes

Sparse labels may still fail for fine geometric boundaries, reflective surfaces, transparent objects, or unusual camera models. Text-based supervision for dense spatial tasks also raises questions about output resolution and calibration.

Because this note is abstract-only, details still need checking: label sparsity, visual prompt format, intrinsics conditioning, datasets, depth metrics, pure-vision baselines, and additional 3D tasks.

## Deep Themes

- Spatial grounding for VLMs: semantic multimodal models can be pushed toward metric 3D understanding.
- Interface over architecture: visual prompting and augmentation unlock capability without changing model heads.
- Camera ambiguity as data problem: cross-dataset intrinsics must be modeled for metric predictions.
- Sparse supervision for dense tasks: dense perception may not always require dense labels or specialized losses.

## Subthemes

- Metric depth estimation.
- Visual prompting.
- Intrinsic-conditioned augmentation.
- VLM 3D reasoning.

## Connections to Other Papers

This connects to WAVE, InfoTok, and video-understanding papers through richer multimodal representations.

It also relates to robotics and embodied-agent work because metric 3D perception is a prerequisite for grounded action.

## Notes for Cross-Paper Synthesis

DepthLM adds to the multimodal capability theme: VLM weaknesses can sometimes be interface and supervision bottlenecks rather than fixed architectural limits.
