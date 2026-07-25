# EmotionThinker: Prosody-Aware Reinforcement Learning for Explainable Speech Emotion Reasoning

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: wbttgzp7MT
- Authors: Dingdong WANG; Shujie LIU; Tianhua Zhang; Youjun Chen; Jinyu Li; Helen M. Meng
- Primary area: applications to computer vision, audio, language, and other modalities
- Keywords: Speech Emotion Recognition;Speech LLMs;Speech Processing;Reinforcement Learning
- Source URL: https://openreview.net/forum?id=wbttgzp7MT
- PDF URL: https://openreview.net/pdf?id=wbttgzp7MT

## Abstract

Emotional information in speech plays a unique role in multimodal perception. However, current Speech Large Language Models (SpeechLLMs), similar to conventional speech emotion recognition (SER) systems, still treat emotion understanding as a simple classification problem. This provides limited interpretability of predictions, while leaving the LLMs’ expressive and reasoning capabilities underutilized. In this work, we take the first step to reformulate SER as a deep reasoning problem through reinforcement learning (RL). We propose EmotionThinker, which is designed to generate accurate emotion predictions with interpretable explanations grounded in fine-grained acoustic cues. To achieve this, we first construct EmotionCoT-35K, an emotional reasoning dataset with Chain-of-Thought annotations and detailed captions. Second, we observe that current SpeechLLMs exhibit weak prosody perception, whereas prosodic cues constitute fundamental signals for interpreting emotions. To address this, we develop the prosody-enhanced foundation model EmotionThinker-Base, and demonstrate that prosody enhancement improves emotion understanding. Third, we introduce Group-Relative-Policy-Optimization with Progressive-Trust-aware-Reasoning-Reward (GRPO-PTR}) for RL. Different from standard GRPO, which relies only on rule-based outcome rewards, GRPO-PTR progressively introduces reasoning reward, dynamically adjusts it with a trustworthiness weight reflecting the alignment between reasoning and outcome, and evaluates the overall reasoning quality with a reward model based on multi-dimensional criteria. EmotionThinker outperforms previous state-of-the-art evaluation models both in emotion accuracy and explanation quality, advancing SER toward interpretable multimodal reasoning.

## One-Sentence Claim

EmotionThinker turns speech emotion recognition from label classification into prosody-grounded reasoning, using curated emotional chain-of-thought data and reinforcement learning to improve both accuracy and explanations.

## Problem

Speech emotion systems and SpeechLLMs often reduce emotion understanding to classification. That misses the reasoning opportunity in LLM-style models and provides weak interpretability, especially because emotional meaning depends on fine-grained acoustic cues such as prosody.

## Core Contribution

The paper contributes EmotionCoT-35K, a dataset with emotional reasoning annotations and detailed captions; EmotionThinker-Base, a prosody-enhanced foundation model; and GRPO-PTR, a reinforcement learning objective that progressively adds reasoning reward while tracking whether the reasoning is trustworthy and aligned with the final outcome.

## Method

The pipeline first builds supervised emotional reasoning data, then strengthens prosody perception in the base SpeechLLM, and finally applies Group-Relative Policy Optimization with Progressive-Trust-aware Reasoning Reward. GRPO-PTR starts from outcome rewards and progressively introduces a learned reasoning-quality signal, weighted by trustworthiness between reasoning and answer.

## Experiments and Evidence

The abstract reports state-of-the-art results on both emotion accuracy and explanation quality. It also reports the diagnostic observation that current SpeechLLMs have weak prosody perception and that prosody enhancement improves emotion understanding.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect dataset construction, annotation reliability, whether chain-of-thought explanations are faithful to acoustic evidence, and how the reward model evaluates reasoning quality. Emotion reasoning may be culture-, language-, speaker-, and context-dependent, so generalization needs careful scrutiny.

## Deep Themes

- Turning classification into interpretable multimodal reasoning.
- Prosody as a first-class reasoning signal.
- RL rewards for explanation quality, not only final answers.
- Trust-aware alignment between reasoning traces and outcomes.

## Subthemes

- Speech emotion recognition.
- SpeechLLMs.
- EmotionCoT-35K.
- Prosody-enhanced foundation model.
- GRPO-PTR.

## Connections to Other Papers

Connects to Visual Planning and cadrille through modality-native reasoning, to AdAEM and WIMHF through reward/evaluation signals that go beyond scalar correctness, and to T3 through process-level control of reasoning trajectories.

## Notes for Cross-Paper Synthesis

This paper is a strong example of the 2026 shift from answer prediction to evidence-grounded reasoning. It treats the intermediate rationale as something to train, reward, and evaluate, while also grounding that rationale in modality-specific signals that text-only reasoning would miss.
