# ADEPT: RL-Aligned Agentic Decoding of Emotion via Evidence Probing Tools — From Consensus Learning to Ambiguity-Driven Emotion Reasoning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: maA1s1S0db
- Authors: Esther Sun; Bo-Hao Su; Abinay Reddy Naini; Shinji Watanabe; Carlos Busso
- Primary area: applications->language_speech_and_dialog
- Keywords: Speech Emotion Recognition;Multimodal Large Language Models;LLM Agents;Tool Learning;Ambiguity Modeling;Interpretability
- Source URL: https://openreview.net/forum?id=maA1s1S0db
- PDF URL: https://openreview.net/pdf?id=maA1s1S0db

## Abstract

Speech Large Language Models (SLLMs) enable high-level emotion reasoning, but often produce ungrounded, text-biased judgments without verifiable acoustic evidence. In contrast, SSL encoders such as WavLM yield strong acoustic representations yet remain opaque discriminative models that offer limited interpretability. To bridge this gap, we introduce the Agentic Decoding of Emotion via Probing Tools (ADEPT) framework, which reframes emotion recognition as a multi-turn inquiry process rather than a single-pass prediction. ADEPT transforms an SLLM into an agent that maintains an evolving candidate set and adaptively invokes dedicated semantic and acoustic probing tools within a structured pipeline of candidate generation, evidence collection, and adjudication. Crucially, ADEPT enables a paradigm shift from consensus learning to ambiguity-driven emotion reasoning. Since human affect exhibits complexity and co-occurrence of emotions, we leverage minority annotations as informative signals instead of discarding them as noise. Finally, we integrate Group Relative Policy Optimization (GRPO) with the Evidence Trust Gate to explicitly couple tool-usage behaviors with prediction quality and enforce evidence-based reasoning. Experiments demonstrate that ADEPT improves in most cases the primary emotion accuracy while substantially improving minor emotion characterization, producing explanations grounded in auditable evidence.

## One-Sentence Claim

ADEPT turns speech emotion recognition into an evidence-seeking agent workflow, using semantic and acoustic probing plus RL-aligned trust gating to improve primary emotion recognition and recover minority emotion signals.

## Problem

Speech emotion recognition sits between two imperfect model families. Speech LLMs can produce rich explanations, but their judgments can drift toward text priors and unsupported affect labels. Acoustic SSL encoders are stronger at extracting speech cues, but they are typically discriminative and opaque, so they do not naturally expose why an emotion label was chosen.

The paper also challenges the common consensus-learning framing of emotion labels. Human affect is ambiguous and co-occurring; minority annotations may encode genuine secondary emotions rather than annotation noise. A single-pass majority-label classifier loses this ambiguity and makes it hard to audit whether predictions are acoustically grounded.

## Core Contribution

The contribution is to recast emotion recognition as an agentic evidence-gathering process. ADEPT maintains candidate emotions, calls dedicated tools for semantic and acoustic evidence, and adjudicates among candidate and minority emotions using an Evidence Trust Gate.

The deeper contribution is a shift from "predict the consensus label" to "reason over affective ambiguity." Minority annotations become a training and evaluation signal for secondary emotion characterization, and RL is used not just to improve label accuracy but to align tool-use behavior with verifiable evidence.

## Method

ADEPT uses a structured multi-turn pipeline: generate candidate emotions, collect semantic evidence, collect acoustic evidence, and adjudicate. The SLLM acts as the controller, while specialized probing tools provide evidence that can be checked rather than left implicit in the model's latent reasoning.

The Evidence Trust Gate mediates whether tool evidence should affect the final decision, discouraging unsupported text-biased emotion claims. Group Relative Policy Optimization is used to couple tool invocation and final prediction quality, so the agent learns when evidence probing improves the decision rather than merely adding explanation text.

## Experiments and Evidence

The abstract reports improvements in most primary-emotion accuracy cases and substantial gains in minor emotion characterization. The important evidence pattern is not only better top-label accuracy but improved handling of ambiguous labels, which is closer to the actual structure of affective annotation.

Because this note is currently based on metadata/abstract rather than extracted full text, detailed datasets, baselines, ablations, and numerical tables remain to be verified from the paper PDF when OpenReview or arXiv access is available.

## Limits and Failure Modes

The method depends on the quality and coverage of its probing tools. If acoustic probes miss cues, semantic probes overfit transcript content, or the trust gate is poorly calibrated, the agent can produce explanations that look auditable without actually improving evidential reliability.

Minority-label modeling also creates a careful evaluation problem: preserving ambiguity is valuable, but over-amplifying weak or idiosyncratic annotations could inflate secondary-emotion claims. The paper's core promise therefore rests on whether its evidence gate separates meaningful affective ambiguity from annotation noise.

## Deep Themes

- Agentic diagnosis as a replacement for monolithic classification: the model is not just a predictor but a controller over probes, evidence, and adjudication.
- Ambiguity as signal: minority annotations are treated as structured information about co-occurring emotion rather than discarded noise.
- Interpretability through procedural evidence: explanations are tied to tool calls and evidence gates rather than generated post hoc.
- RL for epistemic discipline: optimization targets not only output correctness but whether the reasoning process gathered useful evidence.

## Subthemes

- Speech and multimodal affect recognition are becoming testbeds for agentic LLM workflows because the task naturally requires integrating semantic and acoustic cues.
- The consensus label is an impoverished target when the domain contains genuine subjective mixtures.
- Evidence-gated tool use provides a reusable pattern for reducing language-model bias in multimodal decision tasks.
- Secondary-label performance is a richer metric than primary accuracy alone for ambiguous human-centered tasks.

## Connections to Other Papers

ADEPT connects to MAP and Vision2Web through the theme of agents being evaluated by workflow quality, not just final answer quality. It also relates to PLAINTAIN and LaST0 in treating intermediate reasoning artifacts as intervention points. Compared with backdoor self-awareness work, ADEPT is less about exposing hidden malicious triggers and more about forcing latent judgments to be grounded in external evidence.

It also belongs beside fairness and noisy-label papers in the broader shift away from treating disagreement as noise. Like JYP in the noisy-label setting, ADEPT asks whether label uncertainty can be represented directly rather than suppressed.

## Notes for Cross-Paper Synthesis

ADEPT is evidence that agentic architectures are spreading beyond web/tool tasks into perceptual and affective inference. Its central pattern is "proceduralize the inference": split prediction into candidate generation, evidence collection, and adjudication, then optimize the process. This is likely to recur across domains where labels are subjective, multimodal, or underdetermined.
