# SANA-Video: Efficient Video Generation with Block Linear Diffusion Transformer

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: mzAchylAtf
- Authors: Junsong Chen; Yuyang Zhao; Jincheng YU; Ruihang Chu; Junyu Chen; Shuai Yang; Xianbang Wang; Yicheng Pan; Daquan Zhou; Huan Ling; Haozhe Liu; Hongwei Yi; Hao Zhang; Muyang Li; Yukang Chen; Han Cai; Sanja Fidler; Ping Luo; Song Han; Enze Xie
- Primary area: generative models
- Keywords: Video Diffusion Model
- Source URL: https://openreview.net/forum?id=mzAchylAtf
- PDF URL: https://openreview.net/pdf?id=mzAchylAtf

## Abstract

We introduce SANA-Video, a small diffusion model that can efficiently generate videos up to 720×1280 resolution and minute-length duration. SANA-Video synthesizes high-resolution, high-quality and long videos with strong text-video alignment at a remarkably fast speed, deployable on RTX 5090 GPU. Two core designs ensure our efficient, effective and long video generation:  (1) Linear DiT: We leverage linear attention as the core operation, which is more efficient than vanilla attention given the large number of tokens processed in video generation. (2) Constant-Memory KV cache for Block Linear Attention: we design block-wise autoregressive approach for long video generation by employing a constant-memory state, derived from the cumulative properties of linear attention. This KV cache provides the Linear DiT with global context at a fixed memory cost, eliminating the need for a traditional KV cache and enabling efficient, minute-long video generation. In addition, we explore effective data filters and model training strategies, narrowing the training cost to 12 days on 64 H100 GPUs, which is only 1\% of the cost of MovieGen. Given its low cost, SANA-Video achieves competitive performance compared to modern state-of-the-art small diffusion models (e.g., Wan 2.1-1.3B and SkyReel-V2-1.3B) while being 16x faster in measured latency. Moreover, SANA-Video can be deployed on RTX 5090 GPUs with NVFP4 precision, accelerating the inference speed of generating a 5-second 720p video from 71s to 29s (2.4x} speedup). In summary, SANA-Video enables low-cost, high-quality video generation. Code and model will be publicly released.

## One-Sentence Claim

SANA-Video uses a block linear diffusion transformer with constant-memory linear-attention state to generate high-resolution, minute-long videos efficiently on commodity high-end GPUs.

## Problem

Video diffusion models process enormous token counts, making vanilla attention expensive and long-video generation memory intensive. High-quality text-to-video systems are often costly to train and slow to deploy, limiting practical access.

## Core Contribution

The paper introduces SANA-Video, a small efficient video diffusion model based on Linear DiT and constant-memory KV cache for block linear attention. It targets 720p, long-duration generation with strong text-video alignment and low training/inference cost.

## Method

SANA-Video replaces vanilla attention with linear attention inside a diffusion transformer. For long videos, it uses block-wise autoregressive generation with a constant-memory state derived from cumulative linear-attention properties, giving global context without traditional growing KV cache. It also uses data filtering, training strategies, and NVFP4 deployment.

## Experiments and Evidence

The abstract reports 720x1280 and minute-length generation, training in 12 days on 64 H100 GPUs at about 1 percent of MovieGen's cost, competitive quality versus small SOTA models, 16x measured latency speedup, and RTX 5090 NVFP4 inference improving 5-second 720p generation from 71s to 29s.

## Limits and Failure Modes

Linear attention may lose some long-range detail or temporal consistency compared with full attention. Claims depend on model size, prompt set, hardware, quantization, and evaluation metrics. Full-text review should check video quality benchmarks, human preference tests, temporal artifacts, constant-memory state details, and comparison fairness.

## Deep Themes

- Efficient long video generation.
- Linear attention for diffusion transformers.
- Constant-memory generation state.
- Low-cost training and deployment of generative media.

## Subthemes

- Block-wise autoregressive video generation.
- Linear DiT.
- NVFP4 video inference.
- Training data filtering for video models.
- Long-duration text-video alignment.

## Connections to Other Papers

Connects to LPD and Prophet through generation acceleration, to MotionStream and physical-realism video benchmarks through video-model deployment, and to systems-efficiency themes where architectural changes make media generation cheaper.

## Notes for Cross-Paper Synthesis

SANA-Video shows efficiency as a capability enabler in generative media: long, high-resolution videos become feasible when attention memory stops scaling with duration.
