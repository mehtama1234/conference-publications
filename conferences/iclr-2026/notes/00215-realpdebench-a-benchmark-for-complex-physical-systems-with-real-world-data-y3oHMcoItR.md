# RealPDEBench: A Benchmark for Complex Physical Systems with Real-World Data

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: y3oHMcoItR
- Authors: Peiyan Hu; Haodong Feng; Hongyuan Liu; Tongtong Yan; Wenhao Deng; Tianrun Gao; Rong Zheng; Haoren Zheng; Chenglei Yu; Chuanrui Wang; Kaiwen Li; Zhi-Ming Ma; Dezhi Zhou; Xingcai Lu; Dixia Fan; Tailin Wu
- Primary area: applications to physical sciences (physics, chemistry, biology, etc.)
- Keywords: complex physical system;PDE;benchmark;real-world data;prediction
- Source URL: https://openreview.net/forum?id=y3oHMcoItR
- PDF URL: https://openreview.net/pdf?id=y3oHMcoItR

## Abstract

Predicting the evolution of complex physical systems remains a central problem in science and engineering. Despite rapid progress in scientific Machine Learning (ML) models, a critical bottleneck is the lack of expensive real-world data, resulting in most current models being trained and validated on simulated data. Beyond limiting the development and evaluation of scientific ML, this gap also hinders research into essential tasks such as sim-to-real transfer. We introduce RealPDEBench, the first benchmark for scientific ML that integrates real-world measurements with paired numerical simulations. RealPDEBench consists of five datasets, three tasks, nine metrics, and ten baselines. We first present five real-world measured datasets with paired simulated datasets across different complex physical systems. We further define three tasks, which allow comparisons between real-world and simulated data, and facilitate the development of methods to bridge the two. Moreover, we design nine evaluation metrics, spanning data-oriented and physics-oriented metrics, and finally benchmark ten representative baselines, including state-of-the-art models, pretrained PDE foundation models, and a traditional method. Experiments reveal significant discrepancies between simulated and real-world data, while showing that pretraining with simulated data consistently improves both accuracy and convergence. In this work, we hope to provide insights from real-world data, advancing scientific ML toward bridging the sim-to-real gap and real-world deployment. Our benchmark, datasets, and instructions are available at https://realpdebench.github.io/.

## One-Sentence Claim

RealPDEBench benchmarks scientific ML on paired real-world measurements and simulations, exposing sim-to-real gaps while showing that simulated pretraining can still improve accuracy and convergence.

## Problem

Scientific ML for PDE-governed physical systems is often trained and evaluated on simulated data because real-world measurements are scarce and expensive. This makes it hard to know whether models transfer to deployed physical systems and limits systematic study of sim-to-real transfer.

## Core Contribution

The paper introduces RealPDEBench, a benchmark with five real measured datasets paired with numerical simulations, three tasks, nine metrics, and ten baselines spanning modern ML models, pretrained PDE foundation models, and a traditional method.

## Method

RealPDEBench pairs measured and simulated data across complex physical systems, defines tasks that compare real and simulated regimes, and evaluates methods using both data-oriented and physics-oriented metrics. The benchmark is designed to make discrepancies visible rather than hiding them behind simulation-only validation.

## Experiments and Evidence

The abstract reports significant discrepancies between simulated and real-world data. It also reports that pretraining on simulated data consistently improves both accuracy and convergence, indicating that simulation remains useful but incomplete for real deployment.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect the five systems, measurement noise, simulation fidelity, task definitions, metric sensitivity, licensing, and whether the baselines cover strong domain-specific solvers. Benchmarks can also overrepresent systems where paired simulation/measurement is feasible.

## Deep Themes

- Real-world benchmarks for scientific ML.
- Paired simulation and measurement.
- Sim-to-real transfer.
- Physics-aware evaluation.

## Subthemes

- PDE foundation models.
- Complex physical systems.
- Data-oriented metrics.
- Physics-oriented metrics.
- Simulation pretraining.

## Connections to Other Papers

Connects to CauKer through synthetic or simulated data as pretraining substrate, to Complexa/mCLM through scientific-model deployment constraints, and to PhyWorldBench through evaluation of whether generative or predictive models respect physical structure rather than superficial realism.

## Notes for Cross-Paper Synthesis

RealPDEBench anchors the corpus's scientific ML theme in measurement. It supports a balanced pattern: simulation and synthetic data can be powerful pretraining tools, but real-world paired evaluation is needed to reveal deployment gaps.
