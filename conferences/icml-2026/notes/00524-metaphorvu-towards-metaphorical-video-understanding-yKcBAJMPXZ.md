# MetaphorVU: Towards Metaphorical Video Understanding

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: yKcBAJMPXZ
- Authors: Zhuoqun Li; Boxi Cao; Guiping Jiang; Fangrui Lv; Ruotong Pan; Jianan Wang; Xiangyu Wu; Hongyu Lin; Yaojie Lu; Yong Du; Ruyin Jia; Liyan; Tingting Gao; Han Li; Xianpei Han; Le Sun
- Primary area: deep_learning->large_language_models
- Keywords: metaphorical video understanding
- Source URL: https://openreview.net/forum?id=yKcBAJMPXZ
- PDF URL: https://openreview.net/pdf?id=yKcBAJMPXZ

## Abstract

Metaphorical videos are prevalent across various real-world scenarios to convey complex ideas, and understanding them typically requires high-order cognitive capabilities. 
The lack of systematic studies on metaphorical video understanding not only constrains the real-world applicability of MLLMs but also impedes the thorough assessment of their high-order cognitive capabilities.
To bridge this gap, we propose MetaphorVU-Bench, the first systematic and comprehensive benchmark dedicated to metaphorical video understanding. 
Through experiments, we find current MLLMs struggle with accurate metaphorical video understanding, lagging far behind human level, primarily due to defective cross-domain mapping. 
Motivated by this finding, we construct a metaphor knowledge graph as mapping augmentation and propose MetaphorBoost, an inference-time enhancement framework achieving consistent performance improvement. 
Our benchmark, analysis, and method provide useful insights and a foundation for future research on advancing MLLMs.
Code: https://github.com/icip-cas/MetaphorVU.

## One-Sentence Claim

MetaphorVU shows current MLLMs struggle with metaphorical video understanding because they fail at cross-domain mapping, and improves inference with metaphor knowledge-graph augmentation.

## Problem

Metaphorical videos communicate abstract ideas through visual scenarios, requiring high-order cognitive mapping rather than literal recognition alone.

The lack of systematic benchmarks makes it hard to assess whether multimodal LLMs can understand these videos or merely describe their visible contents.

## Core Contribution

The paper introduces MetaphorVU-Bench, described as the first systematic benchmark for metaphorical video understanding.

It analyzes current MLLM failures, attributes the gap mainly to defective cross-domain mapping, constructs a metaphor knowledge graph, and proposes MetaphorBoost as an inference-time enhancement framework.

## Method

MetaphorVU-Bench evaluates metaphorical video understanding. MetaphorBoost augments inference with a metaphor knowledge graph designed to support mappings from source-domain visual scenes to target-domain abstract meanings.

The method is inference-time rather than retraining-heavy, suggesting it supplies structured metaphorical associations when the model reasons over the video.

## Experiments and Evidence

The abstract reports that current MLLMs lag far behind human performance on metaphorical video understanding.

MetaphorBoost achieves consistent performance improvements, supporting the diagnosis that cross-domain mapping is a bottleneck.

## Limits and Failure Modes

Metaphor understanding is culturally and contextually dependent; a fixed knowledge graph may miss novel, ambiguous, or culturally specific metaphors.

Because this note is abstract-only, details still need checking: benchmark size, annotation protocol, metaphor taxonomy, model list, human baseline, knowledge graph construction, and whether improvements come from genuine mapping or answer priors.

## Deep Themes

- High-order multimodal cognition: video understanding requires abstraction beyond object/action recognition.
- Cross-domain mapping: metaphor depends on linking a concrete source scenario to an abstract target meaning.
- Benchmarks for cognitive capability gaps: real-world applicability requires evaluating figurative understanding.
- Structured knowledge at inference time: external metaphor graphs can scaffold reasoning without retraining.

## Subthemes

- Metaphorical video benchmark.
- MLLM human-level gap.
- Metaphor knowledge graph.
- Inference-time mapping augmentation.

## Connections to Other Papers

This connects to concept binding, Learning-to-Theorize, and Beyond Language Modeling through structured multimodal reasoning. It also relates to Information Flow because the model must use the right semantic evidence path rather than merely retrieve visible facts.

It fits with benchmark papers such as TokSuite and MiniAppBench by exposing a capability dimension hidden by standard evaluation.

## Notes for Cross-Paper Synthesis

MetaphorVU adds an abstraction layer to multimodal evaluation: the model must map what is seen to what is meant, not just identify the visible scene.
