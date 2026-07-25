# EEmo-Logic: A Unified Dataset and Multi-Stage Framework for Comprehensive Image-Evoked Emotion Assessment

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: AYy0lOycql
- Authors: Lancheng Gao; Ziheng Jia; Zixuan Xing; Wei Sun; Huiyu Duan; Guangtao Zhai; Xiongkuo Min
- Primary area: applications->computer_vision
- Keywords: Image-Evoked Emotion Assessment;Multi-modal Large Language Model;Instruction Tuning;Reinforcement Learning;Emotion Reasoning
- Source URL: https://openreview.net/forum?id=AYy0lOycql
- PDF URL: https://openreview.net/pdf?id=AYy0lOycql

## Abstract

Understanding the multi-dimensional attributes and intensity nuances of image-evoked emotions is pivotal for advancing machine empathy and empowering diverse human-computer interaction applications. However, existing models are still limited to coarse-grained emotion perception or deficient reasoning capabilities. To bridge this gap, we introduce **EEmoDB**, the largest image-evoked emotion understanding dataset to date. It features $5$ analysis dimensions spanning $5$ distinct task categories, facilitating comprehensive interpretation. Specifically, we compile $1.2M$ question-answering (QA) pairs (EEmoDB-QA) from $125K$ images via automated generation, alongside a $36K$ dataset (EEmoDB-Assess) curated from $25K$ images for fine-grained assessment. Furthermore, we propose **EEmo-Logic**, an **all-in-one** multimodal large language model (MLLM) developed via instruction fine-tuning and task-customized group relative preference optimization (GRPO) with novel reward design. Extensive experiments demonstrate that EEmo-Logic achieves robust performance in in-domain and cross-domain datasets, excelling in emotion QA and fine-grained assessment. 
The dataset and code are available at https://github.com/workerred/EEmo-Logic.

## One-Sentence Claim

EEmo-Logic builds a large emotion-understanding dataset and trains an MLLM for fine-grained image-evoked emotion QA, assessment, and reasoning.

## Problem

Existing image emotion models are often limited to coarse labels or weak reasoning, missing intensity nuances and multidimensional affective attributes.

## Core Contribution

The paper introduces EEmoDB, with 1.2M QA pairs from 125K images and a 36K fine-grained assessment set from 25K images, plus an all-in-one MLLM trained for emotion reasoning.

## Method

EEmo-Logic uses instruction fine-tuning and task-customized GRPO with a new reward design across five analysis dimensions and five task categories.

## Experiments and Evidence

The abstract reports robust in-domain and cross-domain performance, with strong results in emotion QA and fine-grained assessment.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition is deferred after repeated rate-limit failures. Details still need checking: emotion taxonomy, annotation or automated-generation quality, cultural bias, reward design, and cross-domain split construction.

## Deep Themes

- Multimodal affective understanding requires fine-grained reasoning, not just classification.
- Large synthetic/curated QA resources can define new perceptual-emotional capabilities.
- Preference-style RL is entering multimodal emotion reasoning.

## Subthemes

- Image-evoked emotion.
- Multimodal LLMs.
- Emotion QA.
- Fine-grained assessment.
- Instruction tuning.
- GRPO reward design.

## Connections to Other Papers

Connects to UniPercept, VALUEFLOW, and multimodal benchmark papers through subjective/perceptual construct measurement. It also links to rubric/RL papers through task-customized preference optimization.

## Notes for Cross-Paper Synthesis

EEmo-Logic broadens the perceptual-evaluation theme from aesthetics and quality into affective reasoning over images.
