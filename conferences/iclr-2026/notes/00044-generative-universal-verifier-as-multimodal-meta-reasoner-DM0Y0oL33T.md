# Generative Universal Verifier as Multimodal Meta-Reasoner

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: DM0Y0oL33T
- Authors: Xinchen Zhang; Xiaoying Zhang; Youbin Wu; Yanbin Cao; Renrui Zhang; Ruihang Chu; Ling Yang; Yujiu Yang; Guang Shi
- Primary area: foundation or frontier models, including LLMs
- Keywords: Multimodal Large Language Models
- Source URL: https://openreview.net/forum?id=DM0Y0oL33T
- PDF URL: https://openreview.net/pdf?id=DM0Y0oL33T

## Abstract

We introduce *Generative Universal Verifier*, a novel concept and plugin designed for next-generation multimodal reasoning in vision-language models and unified multimodal models, providing the fundamental capability of reflection and refinement on visual outcomes during the reasoning and generation process. This work makes three main contributions: (1) We build **ViVerBench**, a comprehensive benchmark spanning $16$ categories of critical tasks for evaluating visual outcomes in multimodal reasoning. Results show that existing VLMs consistently underperform across these tasks, underscoring a substantial gap from human-level capability in reliable visual verification. (2) We design two automated pipelines to construct large-scale visual verification data and train **OmniVerifier-7B**, the first omni-capable generative verifier trained for universal visual verification and achieves notable gains on ViVerBench(+$8.3$). Through training, we identify three atomic capabilities in visual verification and demonstrate how they generalize and interact synergistically. (3) We propose **OmniVerifier-TTS**, a sequential test-time scaling paradigm that leverages the universal verifier to bridge image generation and editing within unified models, enhancing the upper bound of generative ability through iterative fine-grained optimization. Beyond generation, we extend universal verifier to broader world-modeling interleaved reasoning scenarios. Empirically, OmniVerifier-TTS achieves improvements on T2I-ReasonBench(+$3.7$), and GenEval++(+$4.3$), outperforming existing parallel test-time scaling methods, such as Best-of-N. By endowing multimodal reasoning with reliable visual verification, OmniVerifier advances both reliable reflection during generation and scalable test-time refinement, marking a step toward more trustworthy and controllable next-generation reasoning systems.

## One-Sentence Claim

OmniVerifier makes visual verification a general multimodal capability, enabling reflection and iterative test-time refinement of visual reasoning and generation outputs.

## Problem

VLMs and unified multimodal models can generate and reason over visual outputs, but they lack reliable visual verification during the process.

Without a verifier, generation and editing systems struggle to reflect on fine-grained visual errors or iteratively improve outputs beyond sampling more candidates.

## Core Contribution

The paper introduces the concept of a Generative Universal Verifier and builds OmniVerifier-7B.

It also introduces ViVerBench, a 16-category benchmark for visual outcome verification, two automated data pipelines for large-scale verifier training, and OmniVerifier-TTS, a sequential test-time scaling paradigm for visual generation/editing refinement.

## Method

OmniVerifier is trained on large-scale visual verification data to generate verification judgments. The authors identify three atomic visual-verification capabilities and study how they generalize and interact.

OmniVerifier-TTS uses the verifier sequentially during test time to bridge image generation and editing, iteratively optimizing visual outcomes rather than selecting from independent samples.

## Experiments and Evidence

The abstract reports that existing VLMs underperform on ViVerBench, while OmniVerifier-7B improves ViVerBench by +8.3.

OmniVerifier-TTS improves T2I-ReasonBench by +3.7 and GenEval++ by +4.3, outperforming parallel test-time scaling methods such as Best-of-N.

## Limits and Failure Modes

Verifier quality depends on data-pipeline coverage and may fail on novel visual criteria. Sequential refinement can also amplify verifier biases if the verifier rewards incorrect visual features.

Because this note is abstract-only, details still need checking: ViVerBench task categories, atomic capability definitions, data-generation pipelines, verifier architecture, refinement loop, and failure cases.

## Deep Themes

- Verification as multimodal meta-reasoning: models need a separate capability for judging visual outcomes.
- Sequential test-time scaling: iterative verifier-guided refinement can beat parallel Best-of-N.
- Visual reflection during generation: generation and editing become a closed feedback loop.
- Universal verifier infrastructure: visual tasks share atomic verification capabilities.

## Subthemes

- ViVerBench.
- OmniVerifier-7B.
- Visual verification data pipelines.
- OmniVerifier-TTS.

## Connections to Other Papers

This connects to FRABench/UFEval, WebDevJudge, DAVE, and CounselBench through evaluator reliability.

It also relates to ASAG, coverage theory, and test-time scaling papers because it turns verification into a sequential inference-time control signal.

## Notes for Cross-Paper Synthesis

OmniVerifier strengthens the verifier-as-controller theme: evaluation is not only for scoring outputs after generation, but for steering generation itself.
