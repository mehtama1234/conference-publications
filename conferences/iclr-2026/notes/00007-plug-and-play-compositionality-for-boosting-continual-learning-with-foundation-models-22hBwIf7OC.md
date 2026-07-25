# Plug-and-Play Compositionality for Boosting Continual Learning with Foundation Models

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 22hBwIf7OC
- Authors: Weiduo Liao; Fei Han; Hisao Ishibuchi; Qingfu Zhang; Ying Wei
- Primary area: transfer learning, meta learning, and lifelong learning
- Keywords: Continual learning
- Source URL: https://openreview.net/forum?id=22hBwIf7OC
- PDF URL: https://openreview.net/pdf?id=22hBwIf7OC

## Abstract

Vision learners often struggle with catastrophic forgetting due to their reliance on class recognition by comparison, rather than understanding classes as compositions of representative concepts. 
This limitation is prevalent even in state-of-the-art continual learners with foundation models and worsens when current tasks contain few classes. 
Inspired by the recent success of concept-level understanding in mitigating forgetting, we design a universal framework CompSLOT to guide concept learning across diverse continual learners. 
Leveraging the progress of object-centric learning in parsing semantically meaningful slots from images, we tackle the challenge of learning slot extraction from ImageNet-pretrained vision transformers by analyzing meaningful concept properties. 
We further introduce a primitive selection and aggregation mechanism to harness concept-level image understanding. 
Additionally, we propose a method-agnostic self-supervision approach to distill sample-wise concept-based similarity information into the classifier, reducing reliance on incorrect or partial concepts for classification. 
Experiments show CompSLOT significantly enhances various continual learners and provides a universal concept-level module for the community.

## One-Sentence Claim

CompSLOT improves continual vision learning by adding a plug-and-play concept-compositional module that makes classifiers rely on object-centric concepts instead of brittle class-comparison signals.

## Problem

Continual learners suffer catastrophic forgetting, including systems built on foundation models. The abstract argues this comes partly from class recognition by comparison rather than understanding classes as compositions of representative concepts, especially when tasks contain few classes.

## Core Contribution

The paper introduces CompSLOT, a universal concept-level framework for continual learners that extracts object-centric slots, selects and aggregates primitives, and distills concept-based similarity information into classifiers.

## Method

CompSLOT uses object-centric learning to parse semantically meaningful slots from ImageNet-pretrained vision transformers, analyzes useful concept properties, selects/aggregates primitives, and applies method-agnostic self-supervision to transfer sample-wise concept similarity to the classifier.

## Experiments and Evidence

The abstract reports significant gains across diverse continual learners. The PDF should be checked for benchmark coverage, foundation-model backbones, ablations for slots/primitives/distillation, and whether concept quality is human-interpretable or only operationally useful.

## Limits and Failure Modes

Potential limits include reliance on good slot extraction, sensitivity to visual domains where object-centric assumptions break, concept leakage from ImageNet pretraining, and possible overhead from the plug-in module.

## Deep Themes

- Continual learning is being reframed around compositional representations.
- Foundation models help but do not solve forgetting by themselves.
- Interpretability-like concepts are used as functional memory supports.

## Subthemes

- Catastrophic forgetting.
- Object-centric learning.
- Concept compositionality.
- Foundation-model continual learning.
- Self-supervised concept distillation.

## Connections to Other Papers

Connects to representation learning, mechanistic/operational interpretability, transfer learning, and efficient adaptation. It may share a deeper pattern with BioX-Bridge: reusable intermediate representations are manipulated through lightweight modules.

## Notes for Cross-Paper Synthesis

This paper supports the hypothesis that 2026 methods often seek stable intermediate structure, such as concepts, slots, subspaces, or bridges, to make foundation models more adaptable and less brittle.
