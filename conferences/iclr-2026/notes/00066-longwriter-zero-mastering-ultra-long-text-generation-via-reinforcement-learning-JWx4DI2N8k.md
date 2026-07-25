# LongWriter-Zero: Mastering Ultra-Long Text Generation via Reinforcement Learning

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: JWx4DI2N8k
- Authors: Yuhao Wu; Yushi Bai; Zhiqiang Hu; Roy Ka-Wei Lee; Juanzi Li
- Primary area: foundation or frontier models, including LLMs
- Keywords: LLMs;RL;Long-form generation
- Source URL: https://openreview.net/forum?id=JWx4DI2N8k
- PDF URL: https://openreview.net/pdf?id=JWx4DI2N8k

## Abstract

Ultra-long generation by large language models (LLMs) is a widely demanded scenario, yet it remains a significant challenge due to their maximum generation length limit and overall quality degradation as sequence length increases. Previous approaches, exemplified by LongWriter, typically rely on ''teaching'', which involves supervised fine-tuning (SFT) on synthetic long-form outputs. However, this strategy heavily depends on synthetic SFT data, which is difficult and costly to construct, often lacks coherence and consistency, and tends to be overly artificial and structurally monotonous. In this work, we propose an incentivization-based approach that, starting entirely from scratch and without relying on any annotated or synthetic data, leverages reinforcement learning (RL) to foster the emergence of ultra-long, high-quality text generation capabilities in LLMs. We perform RL training starting from a base model, similar to R1-Zero, guiding it to engage in reasoning that facilitates planning and refinement during the writing process. To support this, we employ specialized reward models that steer the LLM towards improved length control, writing quality, and structural formatting. Experimental evaluations show that our LongWriter-Zero model, trained from Qwen2.5-32B, consistently outperforms traditional SFT methods on long-form writing tasks, achieving state-of-the-art results across all metrics on WritingBench and Arena-Write, and even surpassing 100B+ models such as DeepSeek R1 and Qwen3-235B.

## One-Sentence Claim

LongWriter-Zero uses reinforcement learning from a base model, rather than synthetic long-output SFT, to induce ultra-long, higher-quality text generation.

## Problem

LLMs are increasingly asked to produce very long outputs, but generation quality often degrades as length increases. Prior long-writing methods commonly depend on synthetic SFT outputs, which are expensive to build and can be incoherent, artificial, or structurally repetitive.

The deeper problem is that long-form generation is not just a maximum-context-length issue. It requires planning, length control, local coherence, global consistency, and formatting over thousands of generated tokens.

## Core Contribution

The paper proposes an incentivization-based route to long-form writing: start from a base model and use RL to make ultra-long writing behavior emerge without annotated or synthetic long-form demonstrations.

The system uses specialized reward models for length control, writing quality, and structural formatting. This frames long generation as a behavior to be rewarded and refined, rather than copied from synthetic exemplars.

## Method

LongWriter-Zero trains from a Qwen2.5-32B base model using reinforcement learning, in a style compared to R1-Zero. The reward setup encourages reasoning during writing, especially planning and refinement behaviors that help maintain quality across long outputs.

The abstract suggests separate reward signals for target length, qualitative writing quality, and document structure, letting the model learn the policy of when to expand, organize, and refine.

## Experiments and Evidence

The abstract reports state-of-the-art performance across WritingBench and Arena-Write.

LongWriter-Zero reportedly outperforms traditional SFT approaches and even surpasses larger 100B+ systems such as DeepSeek R1 and Qwen3-235B on the measured long-writing metrics.

## Limits and Failure Modes

Reward-model design becomes central: if reward models overvalue length, formatting, or surface fluency, the model may learn verbose but weak long-form writing. RL can also amplify evaluator biases and may be expensive at 32B scale.

Because this note is abstract-only, details still need checking: RL algorithm, reward model training data, length ranges, benchmarks, human evaluation setup, safety filtering, and whether planning/refinement is visible or latent.

## Deep Themes

- RL as capability induction: long writing is trained as an emergent policy rather than copied from synthetic traces.
- Long-form generation beyond context length: planning and structure matter as much as token budget.
- Reward decomposition: length, quality, and formatting become separately steerable objectives.
- Synthetic-data avoidance: the paper reflects a move away from brittle synthetic SFT for complex generation behaviors.

## Subthemes

- Ultra-long generation.
- RL from base models.
- Reward models for writing quality.
- Planning and refinement during generation.

## Connections to Other Papers

This connects to PonderLM-2 and p-less sampling through inference-time and training-time control of generation behavior.

It also relates to ASAG, ThinkV, and WSM because all treat long or costly generation as something governed by internal signals, rewards, or schedules rather than fixed decoding recipes.

## Notes for Cross-Paper Synthesis

LongWriter-Zero adds a long-form generation theme: frontier LLM capabilities are increasingly being induced through objective design and process incentives, not only supervised imitation.
