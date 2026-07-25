# FRABench and UFEval: Unified Fine-grained Evaluation with Task and Aspect Generalization

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 7WdY3Cojy9
- Authors: Shibo Hong; Jiahao Ying; Haiyuan Liang; Mengdi Zhang; Jun Kuang; Jiazheng Zhang; Yixin Cao
- Primary area: datasets and benchmarks
- Keywords: Aspect-level Evaluation Dataset;Unified Fine-grained Evaluation
- Source URL: https://openreview.net/forum?id=7WdY3Cojy9
- PDF URL: https://openreview.net/pdf?id=7WdY3Cojy9

## Abstract

Evaluating open-ended outputs of Multimodal Large Language Models has become a bottleneck as model capabilities, task diversity, and modality rapidly expand. Existing ``MLLM-as-a-Judge'' evaluators, though promising, remain constrained to specific tasks and aspects (i.e., specific evaluation criteria such as fluency for text and image quality for images). In this paper, we argue that, on one hand, based on the interconnected nature of criteria, learning specific aspects can generalize to unseen aspects; on the other hand, jointly learning to assess multiple visual criteria and tasks may foster a synergistic effect. To this end, we propose UFEval, the first unified fine-grained evaluator with task and aspect generalization for four evaluation tasks --- Natural Language Generation, Image Understanding, Image Generation, and Interleaved Text-and-Image Generation. However, training such a unified evaluator is hindered by the lack of a large-scale, multi-modal, and aspect-level resource. To address this gap, we introduce FRABench, a comprehensive fine-grained evaluation dataset. Specifically, (1) We first construct a hierarchical aspect taxonomy encompassing 112 distinct aspects across the aforementioned four tasks. (2) Based on this taxonomy, we create FRABench, comprising 60.4k pairwise samples with 325k evaluation labels obtained from a combination of human and GPT-4o annotations. (3) Finally, leveraging FRABench, we develop UFEval, a unified fine-grained evaluator. Experiments show that learning on specific aspects enables UFEval to generalize to unseen aspects, and joint learning to assess diverse visual tasks and aspects can lead to substantial mutual benefits.

## One-Sentence Claim

FRABench and UFEval make fine-grained multimodal evaluation more general by training one evaluator across tasks and aspect criteria, including unseen aspects.

## Problem

Open-ended multimodal outputs are difficult to evaluate because tasks and modalities are expanding quickly. Existing MLLM-as-a-judge systems tend to be tied to specific tasks or specific criteria such as fluency or image quality.

The bottleneck is not only judge accuracy but generalization: an evaluator should transfer across tasks and across aspects that were not directly trained.

## Core Contribution

The paper introduces FRABench, a large aspect-level multimodal evaluation dataset, and UFEval, a unified fine-grained evaluator for Natural Language Generation, Image Understanding, Image Generation, and Interleaved Text-and-Image Generation.

It contributes a hierarchical taxonomy with 112 aspects and a dataset of 60.4k pairwise samples with 325k evaluation labels from human and GPT-4o annotations.

## Method

The authors build a hierarchical aspect taxonomy across four multimodal evaluation tasks. They annotate pairwise examples at the aspect level, then train UFEval as a unified evaluator across tasks and aspects.

The central hypothesis is that evaluation criteria are interconnected: learning specific aspects can transfer to unseen aspects, and learning diverse tasks jointly can create mutual benefits.

## Experiments and Evidence

The abstract reports that UFEval generalizes to unseen aspects and that joint learning across visual tasks and criteria yields substantial mutual benefits.

Evidence includes the scale of FRABench: 60.4k pairwise samples and 325k evaluation labels over 112 aspects.

## Limits and Failure Modes

The dataset uses a mixture of human and GPT-4o annotations, so label quality and judge bias need scrutiny. Aspect taxonomies can also encode subjective or culturally specific assumptions.

Because this note is abstract-only, details still need checking: annotation agreement, GPT-4o label validation, held-out aspect split, task balance, evaluator architecture, and robustness to adversarial outputs.

## Deep Themes

- Evaluation generalization: judges should transfer across tasks and criteria.
- Aspect-level supervision: coarse preference labels are not enough for diagnosing multimodal outputs.
- Unified judging: multimodal evaluation may benefit from shared criteria across modalities.
- Taxonomy as infrastructure: organizing aspects shapes what evaluators can learn.

## Subthemes

- MLLM-as-a-judge.
- Fine-grained pairwise evaluation.
- Task and aspect generalization.
- Human plus model annotation.

## Connections to Other Papers

This connects to MiniAppBench, Copyright-Bench, CounselBench, and MetaphorVU through benchmark design for richer evaluation surfaces.

It also relates to Information Flow and DAVE because evaluation increasingly asks whether a system uses the right evidence or criteria, not just whether an output looks good.

## Notes for Cross-Paper Synthesis

FRABench/UFEval adds a measurement-infrastructure theme: as outputs become multimodal and open-ended, evaluation itself needs compositional generalization.
