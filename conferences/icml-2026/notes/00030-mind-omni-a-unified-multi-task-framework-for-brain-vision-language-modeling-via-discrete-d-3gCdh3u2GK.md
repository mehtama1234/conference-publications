# Mind-Omni: A Unified Multi-Task Framework for Brain-Vision-Language Modeling via Discrete Diffusion

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 3gCdh3u2GK
- Authors: Yizhuo Lu; Changde Du; Qingyu Shi; Hang Chen; Jie Peng; Liuyun Jiang; Shuangchen Zhao; Huiguang He
- Primary area: applications->neuroscience_cognitive_science
- Keywords: Neural signal modeling;unified multitask framework;discrete diffusion
- Source URL: https://openreview.net/forum?id=3gCdh3u2GK
- PDF URL: https://openreview.net/pdf?id=3gCdh3u2GK

## Abstract

Modeling the interplay between external stimuli and internal neural representations is a pivotal research area for Brain-Computer Interfaces (BCIs). A major limitation of prior work is the prevailing paradigm of specialized, single-task models, which curtails versatility and neglects inter-task synergies. To address this, we propose Mind-Omni, the first versatile framework that unifies seven distinct encoding and decoding tasks through a discrete diffusion paradigm. At its core is a novel Brain Tokenizer that transforms heterogeneous, continuous brain signals into standardized, discrete tokens. This enables direct, token-level interactions for mutual understanding and generation between any two or more modalities within a shared semantic space. To unlock advanced reasoning capabilities, we further curate a specialized Brain Question Answering (BQA) instruction-tuning dataset. Our model not only establishes a new state-of-the-art among multi-task unified frameworks but also provides strong evidence for multi-task synergy. By demonstrating performance competitive with, and at times superior to, larger specialized models, our work offers a powerful new paradigm for neural modeling and paves the way for foundation models of neural activity.

## One-Sentence Claim

Mind-Omni unifies brain, vision, and language encoding/decoding by tokenizing fMRI signals and training a discrete diffusion model across seven neural modeling tasks.

## Problem

Brain-computer-interface modeling is dominated by specialized single-task encoding or decoding models, which limits versatility and misses synergies among brain, image, and text tasks.

## Core Contribution

The paper introduces a unified framework with a Brain Tokenizer, discrete diffusion generator, and Brain Question Answering instruction-tuning dataset, targeting multi-task neural encoding and decoding.

## Method

The Brain Tokenizer converts continuous fMRI signals into discrete tokens aligned with visual and textual semantics. A DiT-style discrete diffusion model uses masking strategies to solve seven tasks spanning image/text-to-brain encoding, brain-to-image/text decoding, joint tasks, and BQA.

## Experiments and Evidence

The abstract reports new state of the art among unified multi-task frameworks, evidence of multi-task synergy, and competitive performance against larger specialized models.

## Full-Text Upgrade

The full text names the seven task family explicitly: image-to-brain, text-to-brain, image-and-text-to-brain, brain-to-image, brain-to-text, brain-to-image-and-text, and Brain Question Answering. The Brain Tokenizer is trained to discretize continuous fMRI into token sequences using reconstruction, alignment, and perceptual objectives, then a shared discrete diffusion objective handles all target modalities through masking.

The BQA dataset is curated using multimodal LLMs for instruction tuning, giving the model a reasoning-style task on top of reconstruction and encoding. The paper also positions Mind-Omni as a computational testbed: by synthesizing fMRI responses and comparing modality/task interactions, it analyzes inter-modal complementarity and inter-task synergy rather than only reporting benchmark scores.

## Limits and Failure Modes

Limits to watch: the method is fMRI-centered and data constrained; BQA quality depends on generated instruction data; and claims about neural foundation models need validation across subjects, scanners, tasks, and non-fMRI neural modalities.

## Deep Themes

- Neural modeling is moving from specialized decoders toward unified multimodal foundation-style systems.
- Discrete tokenization is spreading into scientific signal domains.
- Multi-task synergy can be an architectural objective, not only a byproduct.

## Subthemes

- Brain-computer interfaces.
- fMRI tokenization.
- Discrete diffusion.
- Brain-vision-language modeling.
- Brain question answering.
- Multi-task neural encoding and decoding.

## Connections to Other Papers

Connects to BioX-Bridge, Seeing Through the Brain, and LIMSSR through biomedical/multimodal transfer under limited data. It also links to diffusion-language and structured generative modeling work via discrete diffusion as a unifying generator.

## Notes for Cross-Paper Synthesis

Mind-Omni extends the foundation-model pattern into neural-signal modeling: the key move is to standardize heterogeneous scientific signals into tokens that participate in shared multimodal generation.
