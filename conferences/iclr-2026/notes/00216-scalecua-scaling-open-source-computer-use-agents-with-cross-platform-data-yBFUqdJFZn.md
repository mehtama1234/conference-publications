# ScaleCUA: Scaling Open-Source Computer Use Agents with Cross-Platform Data

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: yBFUqdJFZn
- Authors: Zhaoyang Liu; JingJing Xie; Zichen Ding; Zehao Li; Bowen Yang; Zhenyu Wu; Xuehui Wang; Qiushi Sun; Shi Liu; Weiyun Wang; Shenglong Ye; Qingyun Li; Zeyue Tian; Gen Luo; Xiangyu Yue; Biqing Qi; Kai Chen; Bowen Zhou; Yu Qiao; Qifeng Chen; Wenhai Wang
- Primary area: applications to computer vision, audio, language, and other modalities
- Keywords: GUI Agent;GUI Data Pipeline;Computer Use;Open Source
- Source URL: https://openreview.net/forum?id=yBFUqdJFZn
- PDF URL: https://openreview.net/pdf?id=yBFUqdJFZn

## Abstract

Vision-Language Models (VLMs) have enabled computer use agents (CUAs) that operate GUIs autonomously, showing great potential, yet progress is limited by the lack of large-scale, open-source computer use data and foundation models. In this work, we introduce ScaleCUA, a step toward scaling open-source CUAs. It offers a large-scale dataset spanning 6 operating systems and 3 task domains, built via a closed-loop pipeline uniting automated agents with human experts. Trained on this scaled-up data, ScaleCUA can operate seamlessly across platforms.  Specifically, it delivers strong gains over baselines (+26.6 on WebArena-Lite-v2, +10.7 on ScreenSpot-Pro) and sets new state-of-the-art results (94.4% on MMBench-GUI L1-Hard, 60.6% on OSWorld-G, 47.4% on WebArena-Lite-v2). These findings underscore the power of data-driven scaling for general-purpose computer use agents. We will release data, models, and code to advance future research.

## One-Sentence Claim

ScaleCUA scales open-source computer-use agents with a large cross-platform dataset and foundation model, showing strong gains across GUI and web-agent benchmarks.

## Problem

Computer-use agents need to operate across heterogeneous GUIs, operating systems, and task domains, but progress is constrained by limited open-source data and models. Closed or narrow datasets make it hard to build general-purpose agents that transfer across platforms.

## Core Contribution

The paper contributes ScaleCUA, a dataset and model effort spanning six operating systems and three task domains. The dataset is built with a closed-loop pipeline combining automated agents and human experts, and the trained model is positioned as a scalable open-source foundation for computer use.

## Method

ScaleCUA uses a data-driven scaling approach. A closed-loop collection pipeline has automated agents generate or attempt tasks, while human experts provide correction, validation, or augmentation. Models trained on the resulting cross-platform data learn to operate GUIs across web and OS settings.

## Experiments and Evidence

The abstract reports gains of +26.6 on WebArena-Lite-v2 and +10.7 on ScreenSpot-Pro, plus state-of-the-art results of 94.4% on MMBench-GUI L1-Hard, 60.6% on OSWorld-G, and 47.4% on WebArena-Lite-v2. The authors state they will release data, models, and code.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect task distribution, human annotation protocol, platform coverage, safety controls, reproducibility of GUI states, and whether the model handles long-horizon failures or only benchmark-style steps. Claims about open release should be rechecked against actual artifact availability.

## Deep Themes

- Data-driven scaling for computer-use agents.
- Cross-platform GUI generalization.
- Closed-loop human-agent data pipelines.
- Open-source agent infrastructure.

## Subthemes

- GUI agents.
- WebArena and OSWorld evaluation.
- Screen understanding.
- Cross-OS action spaces.
- Human expert validation.

## Connections to Other Papers

Connects to ADP through standardized agent data, to RedTeamCUA through computer-use agent evaluation and safety, and to WoW! through closed-loop agent-environment assessment rather than static perception metrics.

## Notes for Cross-Paper Synthesis

ScaleCUA reinforces a major agentic-AI pattern: capability is increasingly bottlenecked by interaction data, action schemas, and closed-loop evaluation. General-purpose agents need infrastructure for observing, acting, failing, and being corrected across platforms.
