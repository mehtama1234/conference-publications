# OpenThoughts: Data Recipes for Reasoning Models

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 7xjoTuaNmN
- Authors: Etash Kumar Guha; Ryan Marten; Sedrick Keh; Negin Raoof; Georgios Smyrnis; Hritik Bansal; Marianna Nezhurina; Jean Mercat; Trung Vu; Zayne Rea Sprague; Ashima Suvarna; Benjamin Feuer; Leon Liangyu Chen; Zaid Khan; Eric Frankel; Sachin Grover; Caroline Choi; Niklas Muennighoff; Shiye Su; Wanjia Zhao; John Yang; Shreyas Pimpalgaonkar; Kartik sharma; Charlie Cheng-Jie Ji; Yichuan Deng; Sarah M Pratt; Vivek Ramanujan; Jon Saad-Falcon; Stutee Acharya; Jeffrey Li; Achal Dave; Alon Albalak; Kushal Arora; Blake Wulfe; Chinmay Hegde; Greg Durrett; Sewoong Oh; Mohit Bansal; Saadia Gabriel; Aditya Grover; Kai-Wei Chang; Vaishaal Shankar; Aaron Gokaslan; Mike A Merrill; Tatsunori Hashimoto; Yejin Choi; Jenia Jitsev; Reinhard Heckel; Maheswaran Sathiamoorthy; Alex Dimakis; Ludwig Schmidt
- Primary area: foundation or frontier models, including LLMs
- Keywords: Reasoning;Data;LLM
- Source URL: https://openreview.net/forum?id=7xjoTuaNmN
- PDF URL: https://openreview.net/pdf?id=7xjoTuaNmN

## Abstract

Reasoning models have made rapid progress on many benchmarks involving math,
code, and science. Yet, there are still many open questions about the best train-
ing recipes for reasoning since state-of-the-art models often rely on proprietary
datasets with little to no public information available. To address this, the goal of
the OpenThoughts project is to create open-source datasets for training reasoning
models. Our OpenThoughts2-1M dataset led to OpenThinker2-32B, the first model
trained on public reasoning data to match DeepSeek-R1-Distill-32B on standard
reasoning benchmarks such as AIME and LiveCodeBench. We then improve
our dataset further by systematically investigating each step of our data genera-
tion pipeline with 1,000+ controlled experiments, which led to OpenThoughts3.
Scaling the pipeline to 1.2M examples and using QwQ-32B as teacher yields
our OpenThinker3-7B model, which achieves state-of-the-art results: 53% on
AIME 2025, 51% on LiveCodeBench 06/24-01/25, and 54% on GPQA Dia-
mond – improvements of 15.3, 17.2, and 20.5 percentage points compared to the
DeepSeek-R1-Distill-Qwen-7B. All of our datasets and models are available on
ANONYMIZED.

## One-Sentence Claim

OpenThoughts shows that public reasoning-data recipes can train competitive reasoning models when the generation pipeline is systematically optimized at scale.

## Problem

Reasoning models have advanced rapidly on math, code, and science benchmarks, but many state-of-the-art recipes depend on proprietary datasets and undisclosed pipelines.

The problem is to make reasoning-model training reproducible and open by identifying which data-generation choices actually matter.

## Core Contribution

The OpenThoughts project creates open-source reasoning datasets and models. OpenThoughts2-1M led to OpenThinker2-32B, described as the first public-data-trained model to match DeepSeek-R1-Distill-32B on standard reasoning benchmarks.

The project then uses more than 1,000 controlled experiments to improve the data-generation pipeline, producing OpenThoughts3 and OpenThinker3-7B.

## Method

The paper systematically varies steps in the reasoning data generation pipeline. It scales the improved pipeline to 1.2M examples and uses QwQ-32B as a teacher.

The resulting datasets train public reasoning models, with recipes evaluated on math, code, and science benchmarks.

## Experiments and Evidence

The abstract reports that OpenThinker3-7B achieves 53 percent on AIME 2025, 51 percent on LiveCodeBench 06/24-01/25, and 54 percent on GPQA Diamond.

These are reported as improvements of 15.3, 17.2, and 20.5 percentage points over DeepSeek-R1-Distill-Qwen-7B.

## Limits and Failure Modes

The recipe still depends on a strong teacher model, and benchmark performance may reflect data overlap, filtering choices, or evaluation-specific tuning if not carefully controlled.

Because this note is abstract-only, details still need checking: data sources, prompt templates, filtering stages, teacher sampling parameters, contamination checks, controlled-experiment design, and license terms for released data/models.

## Deep Themes

- Open reasoning infrastructure: public data recipes can narrow the gap to proprietary reasoning models.
- Data pipeline as model capability: generation, filtering, and scaling decisions shape reasoning performance.
- Controlled recipe science: many small pipeline choices require systematic ablation.
- Teacher-driven distillation at scale: strong teachers remain central to open reasoning model construction.

## Subthemes

- Public reasoning datasets.
- Math/code/science benchmark scaling.
- 1,000+ data recipe experiments.
- OpenThinker model family.

## Connections to Other Papers

This connects to Ctrl-R, PonderLM-2, H1, RAGEN-2, and SGD RLVR through reasoning model post-training and data recipes.

It also relates to Common Corpus and data-governance work because open data availability becomes a bottleneck for reproducible frontier-model research.

## Notes for Cross-Paper Synthesis

OpenThoughts anchors the open-reasoning-data theme: reasoning quality is increasingly a product of data-generation pipelines as much as model architecture.
