# AdAEM: An Adaptively and Automated Extensible Evaluation Method of LLMs' Value Difference

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: qNlTH4kYJZ
- Authors: Jing Yao; Shitong Duan; Xiaoyuan Yi; Dongkuan Xu; Peng Zhang; Tun Lu; Ning Gu; Zhicheng Dou; Xing Xie
- Primary area: alignment, fairness, safety, privacy, and societal considerations
- Keywords: LLM Evaluation;Value Evaluation;Value Alignment;Dynamic Evaluation
- Source URL: https://openreview.net/forum?id=qNlTH4kYJZ
- PDF URL: https://openreview.net/pdf?id=qNlTH4kYJZ

## Abstract

Assessing Large Language Models (LLMs)' underlying value differences enables comprehensive comparison of their misalignment, cultural adaptability, and biases. Nevertheless, current value measurement methods face the informativeness challenge: with often outdated, contaminated, or generic test questions, they can only capture the orientations on comment safety values, e.g., HHH, shared among different LLMs, leading to indistinguishable and uninformative results. To address this problem, we introduce AdAEM, a novel, self-extensible evaluation algorithm for revealing LLMs' inclinations. Distinct from static benchmarks, AdAEM automatically and adaptively generates and extends its test questions. This is achieved by probing the internal value boundaries of a diverse set of LLMs developed across cultures and time periods in an in-context optimization manner. Such a process theoretically maximizes an information-theoretic objective to extract diverse controversial topics that can provide more distinguishable and informative insights about models' value differences. In this way, AdAEM is able to co-evolve with the development of LLMs, consistently tracking their value dynamics. We use AdAEM to generate novel questions and conduct an extensive analysis, demonstrating our method's validity and effectiveness, laying the groundwork for better interdisciplinary research on LLMs' values and alignment.

## One-Sentence Claim

AdAEM adaptively generates controversial value-probing questions to distinguish LLM value differences more informatively than static, generic, or contaminated value benchmarks.

## Problem

Static value-evaluation benchmarks can become outdated, contaminated, or too generic, often measuring common safety orientations shared by many LLMs rather than revealing cultural, temporal, or model-specific value differences.

## Core Contribution

The paper introduces AdAEM, a self-extensible evaluation algorithm that probes internal value boundaries across diverse LLMs and automatically generates new questions to maximize an information-theoretic objective for distinguishability.

## Method

AdAEM performs in-context optimization over a diverse set of models from different cultures and time periods. It adaptively proposes controversial topics and test questions that separate model inclinations, allowing the benchmark to co-evolve with model development.

## Experiments and Evidence

The abstract reports that AdAEM generates novel questions and supports extensive analysis showing validity and effectiveness for revealing LLM value dynamics and differences.

## Limits and Failure Modes

Automatically generated controversial questions may encode evaluator-model biases, cultural assumptions, or adversarial framings. Informativeness does not guarantee normative validity. Full-text review should check the information objective, human validation, cultural coverage, contamination controls, and how generated questions are audited for harm or ambiguity.

## Deep Themes

- Dynamic value evaluation.
- Adaptive benchmark generation.
- LLM value-boundary probing.
- Cultural and temporal alignment measurement.

## Subthemes

- Self-extensible evaluation.
- Information-theoretic question selection.
- Controversial-topic discovery.
- Model value difference tracking.
- Benchmark co-evolution with LLMs.

## Connections to Other Papers

Connects to EigenBench, CounselBench, Omni-Reward, and P-GenRM through subjective/alignment evaluation, and to dynamic benchmark papers like BIRD-INTERACT and OpenApps through evaluation environments that adapt rather than stay fixed.

## Notes for Cross-Paper Synthesis

AdAEM adds to the trend away from static benchmarks. For value alignment, the benchmark itself becomes an adaptive instrument for exposing model differences.
