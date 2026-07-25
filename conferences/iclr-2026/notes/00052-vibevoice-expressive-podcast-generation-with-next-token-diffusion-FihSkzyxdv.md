# VibeVoice: Expressive Podcast Generation with Next-Token Diffusion

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: FihSkzyxdv
- Authors: Zhiliang Peng; Jianwei Yu; Wenhui Wang; Yaoyao Chang; Yutao Sun; Li Dong; Yi Zhu; Weijiang Xu; Hangbo Bao; Zehua Wang; Shaohan Huang; Yan Xia; Furu Wei
- Primary area: applications to computer vision, audio, language, and other modalities
- Keywords: Text-to-Speech; Podcast Generation
- Source URL: https://openreview.net/forum?id=FihSkzyxdv
- PDF URL: https://openreview.net/pdf?id=FihSkzyxdv

## Abstract

Generating long-form, multi-speaker conversational audio like podcasts poses significant challenges for traditional Text-to-Speech (TTS) systems, particularly in scalability, speaker consistency, and natural turn-taking. We present VibeVoice , a novel model designed to synthesize expressive, long-form speech with multiple speakers in a zero-shot manner. A core component of our approach is the continuous speech tokenizers operating at an ultra-low frame rate of 7.5. This tokenizer effectively preserves audio fidelity while significantly boosting computational efficiency for processing long sequences. To facilitate training on authentic conversational dynamics, we have developed an annotation pipeline that generates pseudo transcriptions and turn-taking labels for extensive podcast data. Leveraging this data and our efficient tokenizer, VibeVoice  employs the next-token diffusion framework. This enables VibeVoice  to: (1) synthesize long-form speech (up to 30 minutes) with up to 4 speakers, surpassing the typical 1-2 speaker limits of many prior models; and (2) achieve a high degree of naturalness in turn-taking, pacing, and the rendition of subtle non-lexical cues (such as breaths and lip smacks), which are crucial for listener immersion and capturing the authentic vibe of expressive conversations.

## One-Sentence Claim

VibeVoice generates long-form zero-shot multi-speaker podcast audio by combining ultra-low-frame-rate continuous speech tokens with next-token diffusion trained on conversational turn-taking data.

## Problem

Traditional TTS systems struggle with long-form multi-speaker conversational audio. Podcasts require speaker consistency, natural turn-taking, pacing, and non-lexical cues over long durations.

Existing systems often handle only one or two speakers and have difficulty scaling to long sequences without losing naturalness.

## Core Contribution

The paper introduces VibeVoice, a model for expressive long-form speech synthesis with up to four speakers and durations up to 30 minutes.

Its core components are a continuous speech tokenizer at an ultra-low 7.5 frame rate, a podcast annotation pipeline producing pseudo transcripts and turn-taking labels, and a next-token diffusion framework for speech generation.

## Method

The tokenizer compresses speech into efficient continuous tokens while preserving fidelity. The annotation pipeline extracts supervision from podcast data, including turn-taking structure.

VibeVoice then uses next-token diffusion to model long conversational sequences with speaker turns, pacing, and subtle non-lexical cues such as breaths and lip smacks.

## Experiments and Evidence

The abstract reports generation of up to 30 minutes of speech with up to four speakers, exceeding typical one- or two-speaker limits.

It also reports improved naturalness in turn-taking, pacing, and subtle conversational cues, though detailed metrics are not available in the local abstract.

## Limits and Failure Modes

Long-form generation may accumulate speaker drift, prosody errors, or semantic inconsistency. Pseudo-label quality for turn-taking can shape model behavior.

Because this note is abstract-only, details still need checking: tokenizer reconstruction quality, evaluation metrics, speaker-conditioning setup, zero-shot protocol, dataset scale, and safety/privacy concerns around voice generation.

## Deep Themes

- Long-form audio generation: sequence length and conversational structure become central modeling challenges.
- Efficient continuous tokenization: ultra-low frame rates make long audio computationally feasible.
- Turn-taking as learned structure: natural dialogue audio requires social timing, not just text pronunciation.
- Diffusion beyond images: next-token diffusion is applied to expressive speech synthesis.

## Subthemes

- Podcast generation.
- Multi-speaker zero-shot TTS.
- Non-lexical audio cues.
- Pseudo-transcription and turn labels.

## Connections to Other Papers

This connects to avatar cognitive simulation, Omni-Reward, and multimodal generation papers through expressive multimodal output.

It also relates to masked diffusion language modeling and diffusion/flow generation papers because diffusion-style next-token modeling is spreading across modalities.

## Notes for Cross-Paper Synthesis

VibeVoice adds a long-form multimodal generation theme: realistic media generation depends on interaction timing and non-verbal cues, not only content fidelity.
