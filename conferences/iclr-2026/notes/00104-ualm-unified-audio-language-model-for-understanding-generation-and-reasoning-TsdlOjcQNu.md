# UALM: Unified Audio Language Model for Understanding, Generation and Reasoning

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: TsdlOjcQNu
- Authors: Jinchuan Tian; Sang-gil Lee; Zhifeng Kong; Sreyan Ghosh; Arushi Goel; Chao-Han Huck Yang; Wenliang Dai; Zihan Liu; Hanrong Ye; Shinji Watanabe; Mohammad Shoeybi; Bryan Catanzaro; Rafael Valle; Wei Ping
- Primary area: applications to computer vision, audio, language, and other modalities
- Keywords: Audio Language Model;Audio Understanding;Audio Generation
- Source URL: https://openreview.net/forum?id=TsdlOjcQNu
- PDF URL: https://openreview.net/pdf?id=TsdlOjcQNu

## Abstract

Recent advances in the audio language modeling (ALM) domain tackle audio understanding and text-to-audio generation as separate tasks. Very few studies attempt to unify these tasks -- an essential step toward advanced multimodal reasoning. This paper introduces Unified Audio Language Model (UALM), which aims to unify audio understanding, text-to-audio generation, and multimodal reasoning in a single model. To achieve this goal, we first present UALM-Gen, a text-to-audio language model that directly predicts audio tokens and is comparable to state-of-the-art diffusion-based models. We then demonstrate, using proper data blending, training recipes, and inference techniques, that our single UALM model matches the quality of state-of-the-art specialized models in audio understanding, text-to-audio generation, and text reasoning.  Furthermore, we present UALM-R1, a multimodal reasoning model that utilizes both text and audio in the intermediate thinking steps to facilitate complex generation tasks. To our knowledge, this is the first demonstration in audio research of cross-modal generative reasoning, with its effectiveness confirmed by subjective evaluations.

## One-Sentence Claim

UALM unifies audio understanding, text-to-audio generation, text reasoning, and cross-modal audio-text reasoning in one audio language model.

## Problem

Audio language modeling work often treats audio understanding and text-to-audio generation as separate tasks.

This separation blocks more advanced multimodal reasoning where audio can be both input evidence and generated output, and where intermediate reasoning may involve audio and text together.

## Core Contribution

The paper introduces UALM, a unified audio language model, plus UALM-Gen for text-to-audio token prediction and UALM-R1 for multimodal audio-text reasoning.

It claims a single model can match specialized systems across understanding, generation, and text reasoning through data blending, training recipes, and inference techniques.

## Method

UALM-Gen directly predicts audio tokens for text-to-audio generation, reaching quality comparable to diffusion-based models.

The unified UALM training setup blends data and tasks so the same model supports audio understanding, audio generation, and language reasoning. UALM-R1 uses both text and audio in intermediate thinking steps for complex generation.

## Experiments and Evidence

The abstract reports that UALM matches state-of-the-art specialized models for audio understanding, text-to-audio generation, and text reasoning.

Subjective evaluations confirm the effectiveness of cross-modal generative reasoning in UALM-R1.

## Limits and Failure Modes

Unified models can suffer interference between understanding and generation tasks. Audio subjective evaluation can also be sensitive to protocol, listener set, and content diversity.

Because this note is abstract-only, details still need checking: audio tokenization, model scale, data mixture, training schedule, inference tricks, evaluation benchmarks, and reasoning trace format.

## Deep Themes

- Unified audio-language modeling: understanding and generation become one sequence-modeling problem.
- Cross-modal generative reasoning: intermediate thinking can involve audio as well as text.
- Audio tokens as language-model substrate: direct token prediction challenges diffusion-only generation.
- Task blending for modality unification: data mixture and recipes determine whether capabilities coexist.

## Subthemes

- UALM-Gen.
- UALM-R1.
- Text-to-audio generation.
- Audio-text reasoning.

## Connections to Other Papers

This connects to WAVE, VibeVoice, NextStep-1, and multimodal tokenization papers.

It also relates to LongWriter-Zero and reasoning-model work because both extend reasoning into longer or richer generated sequences.

## Notes for Cross-Paper Synthesis

UALM adds to the multimodal unification theme: frontier models are increasingly asked to understand, generate, and reason within the same modality-token space.
