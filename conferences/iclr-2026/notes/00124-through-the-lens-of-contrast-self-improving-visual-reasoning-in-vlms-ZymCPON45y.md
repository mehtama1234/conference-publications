# Through the Lens of Contrast: Self-Improving Visual Reasoning in VLMs

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: ZymCPON45y
- Authors: Zhiyu Pan; Yizheng Wu; Jiashen Hua; Junyi Feng; Shaotian Yan; Bing Deng; Zhiguo Cao; Jieping Ye
- Primary area: foundation or frontier models, including LLMs
- Keywords: Reasoning;Vision-Language Models;Contrasting
- Source URL: https://openreview.net/forum?id=ZymCPON45y
- PDF URL: https://openreview.net/pdf?id=ZymCPON45y

## Abstract

Reasoning has emerged as a key capability of large language models. In linguistic tasks, this capability can be enhanced by self-improving techniques that refine reasoning paths for subsequent fine-tuning. However, extending these language-based self-improving approaches to vision language models (VLMs) presents a unique challenge: visual hallucinations in reasoning paths cannot be effectively verified or rectified. Our solution starts with a key observation about visual contrast: when presented with a contrastive VQA pair, i.e., two visually similar images with synonymous questions, VLMs identify relevant visual cues more precisely compared with when given a single VQA sample. Motivated by this observation, we propose Visual Contrastive Self-Taught Reasoner (VC-STaR), a novel self-improving framework that leverages visual contrast to mitigate hallucinations in model-generated rationales. We collect a diverse suite of VQA datasets, curate contrastive pairs according to multi-modal similarity, and generate rationales using VC-STaR. Consequently, we obtain a new visual reasoning dataset, VisCoR-$55$K, which is then used to boost the reasoning capability of various VLMs through supervised finetuning. Extensive experiments show that VC-STaR not only outperforms existing self-improving approaches but also surpasses models finetuned on the SoTA visual reasoning datasets, demonstrating that the inherent contrastive ability of VLMs can bootstrap their own visual reasoning. The code, dataset and trained models will be released upon acceptance.

## One-Sentence Claim

VC-STaR uses contrastive VQA pairs to help VLMs generate less hallucinated rationales and bootstrap stronger visual reasoning through supervised fine-tuning.

## Problem

Language-model self-improvement methods refine reasoning paths for later training, but VLM reasoning paths can contain visual hallucinations that are hard to verify or repair.

Single VQA examples may not force the model to attend to the visual cue that actually distinguishes the answer.

## Core Contribution

The paper introduces Visual Contrastive Self-Taught Reasoner.

It uses visually similar image pairs with synonymous questions to elicit more precise visual cue identification, then generates rationales and builds VisCoR-55K for VLM fine-tuning.

## Method

VC-STaR curates contrastive VQA pairs according to multimodal similarity across diverse VQA datasets.

The contrast between paired examples helps the model identify relevant visual differences, reducing hallucinated rationales. Generated rationales are collected into a visual reasoning dataset for supervised fine-tuning.

## Experiments and Evidence

The abstract reports extensive experiments across various VLMs.

VC-STaR outperforms existing self-improving approaches and models fine-tuned on state-of-the-art visual reasoning datasets, showing that VLMs can bootstrap visual reasoning through their own contrastive ability.

## Limits and Failure Modes

Contrastive pairs must be carefully curated; poor pairs may emphasize spurious differences or miss the true causal visual cue. Generated rationales can still be fluent but wrong.

Because this note is abstract-only, details still need checking: VQA datasets, similarity metrics, rationale filtering, fine-tuning setup, hallucination evaluation, and dataset diversity.

## Deep Themes

- Contrast as visual supervision: paired images reveal which cues matter.
- Self-improving VLM reasoning: models generate training rationales for later capability gains.
- Hallucination mitigation through comparison: visual grounding improves when the model must distinguish near matches.
- Dataset construction from model reasoning: VisCoR-55K turns contrastive rationales into reusable supervision.

## Subthemes

- Visual Contrastive Self-Taught Reasoner.
- Contrastive VQA pairs.
- Visual rationale generation.
- VisCoR-55K.

## Connections to Other Papers

This connects to DepthLM, GLANCE, WAVE, DAVE, and visual reasoning benchmark papers.

It also relates to GEPA and HGM because all use generated or reflected traces to improve future system behavior.

## Notes for Cross-Paper Synthesis

VC-STaR adds a multimodal self-improvement pattern: contrastive visual context can act as a verifier for reasoning traces when textual self-reflection is insufficient.
