# MotionStream: Real-Time Video Generation with Interactive Motion Controls

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: v1DKz5Vxr7
- Authors: Joonghyuk Shin; Zhengqi Li; Richard Zhang; Jun-Yan Zhu; Jaesik Park; Eli Shechtman; Xun Huang
- Primary area: generative models
- Keywords: Interactive Video Generation;Motion Control;Real-Time Generation;Causal Generation
- Source URL: https://openreview.net/forum?id=v1DKz5Vxr7
- PDF URL: https://openreview.net/pdf?id=v1DKz5Vxr7

## Abstract

Current motion-conditioned video generation methods suffer from prohibitive latency (minutes per video) and non-causal processing that prevents real-time interaction. We present MotionStream, enabling sub-second latency with up to 29 FPS streaming generation on a single GPU. Our approach begins by augmenting a text-to-video model with motion control, which generates high-quality videos that adhere to the global text prompt and local motion guidance, but does not perform inference on the fly. As such, we distill this bidirectional teacher into a causal student through Self Forcing with Distribution Matching Distillation, enabling real-time streaming inference. Several key challenges arise when generating videos of long, potentially infinite time-horizons -- (1) bridging the domain gap from training on finite length and extrapolating to infinite horizons, (2) sustaining high quality by preventing error accumulation, and (3) maintaining fast inference, without incurring growth in computational cost due to increasing context windows. A key to our approach is introducing carefully designed sliding-window causal attention, combined with attention sinks. By incorporating self-rollout with attention sinks and KV cache rolling during training, we properly simulate inference-time extrapolations with a fixed context window, enabling constant-speed generation of arbitrarily long videos. Our models achieve state-of-the-art results in motion following and video quality while being two orders of magnitude faster, uniquely enabling infinite-length streaming. With MotionStream, users can paint trajectories, control cameras, or transfer motion, and see results unfold in real-time, delivering a truly interactive experience.

## One-Sentence Claim

MotionStream distills a bidirectional motion-conditioned video generator into a causal streaming student, enabling real-time interactive video generation with fixed-context long-horizon extrapolation.

## Problem

Motion-controlled video generation is too slow for interactive use and often relies on non-causal processing. Long or open-ended video generation also faces error accumulation and growing context-window cost.

## Core Contribution

The paper introduces MotionStream, a real-time motion-controlled video generation system with sub-second latency and up to 29 FPS on a single GPU. It combines teacher-student distillation, sliding-window causal attention, attention sinks, self-rollout training, and KV cache rolling.

## Method

MotionStream first augments a text-to-video teacher with motion control, then distills it into a causal student via Self Forcing with Distribution Matching Distillation. Training simulates inference-time extrapolation using self-rollout, attention sinks, and rolling KV cache so the student can generate indefinitely at constant speed.

## Experiments and Evidence

The abstract reports state-of-the-art motion following and video quality, two-orders-of-magnitude speedup, sub-second latency, and up to 29 FPS streaming generation on one GPU. Users can paint trajectories, control cameras, or transfer motion interactively.

## Limits and Failure Modes

Causal streaming can accumulate artifacts over very long horizons, and fixed windows may lose global scene consistency. Motion controls may work best for certain camera/object trajectories. Full-text review should check teacher/student sizes, latency hardware, motion-following metrics, long-horizon degradation, and user-control evaluation.

## Deep Themes

- Real-time interactive video generation.
- Causal distillation of bidirectional generators.
- Fixed-context long-horizon streaming.
- Motion control as user-facing generation interface.

## Subthemes

- Self Forcing with Distribution Matching Distillation.
- Sliding-window causal attention.
- Attention sinks.
- KV cache rolling.
- Infinite-length streaming video.

## Connections to Other Papers

Connects to SANA-Video, PhyWorldBench, LPD, and other efficient generation papers through video scalability, and to interactive tool/control themes where generation becomes an on-the-fly user workflow.

## Notes for Cross-Paper Synthesis

MotionStream shows the deployment end of generative video: quality is not enough if latency prevents interaction. Causal streaming and fixed-context state turn video generation into a controllable real-time system.
