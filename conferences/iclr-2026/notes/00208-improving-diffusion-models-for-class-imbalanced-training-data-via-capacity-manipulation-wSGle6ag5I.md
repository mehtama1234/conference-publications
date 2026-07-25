# Improving Diffusion Models for Class-imbalanced Training Data via Capacity Manipulation

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: wSGle6ag5I
- Authors: Feng Hong; Jiangchao Yao; Yifei Shen; Dongsheng Li; Ya Zhang; Yanfeng Wang
- Primary area: unsupervised, self-supervised, semi-supervised, and supervised representation learning
- Keywords: Imbalance;Diffusion Models
- Source URL: https://openreview.net/forum?id=wSGle6ag5I
- PDF URL: https://openreview.net/pdf?id=wSGle6ag5I

## Abstract

While diffusion models have achieved remarkable performance in image generation, they often struggle with the imbalanced datasets frequently encountered in real-world applications, resulting in significant performance degradation on minority classes. In this paper, we identify model capacity allocation as a key and previously underexplored factor contributing to this issue, providing a perspective that is orthogonal to existing research. Our empirical experiments and theoretical analysis reveal that majority classes monopolize an unnecessarily large portion of the model's capacity, thereby restricting the representation of minority classes. To address this, we propose Capacity Manipulation (CM), which explicitly reserves model capacity for minority classes. Our approach leverages a low-rank decomposition of model parameters and introduces a capacity manipulation loss to allocate appropriate capacity for capturing minority knowledge, thus enhancing minority class representation. Extensive experiments demonstrate that CM consistently and significantly improves the robustness of diffusion models on imbalanced datasets, and when combined with existing methods, further boosts overall performance.

## One-Sentence Claim

Capacity Manipulation improves diffusion models on imbalanced image data by preventing majority classes from monopolizing model capacity and reserving representational space for minority classes.

## Problem

Diffusion models degrade on class-imbalanced training sets, especially for minority classes. Prior work often addresses imbalance through data sampling, reweighting, or conditioning, but this paper identifies internal capacity allocation as an underexplored reason minority-class generation suffers.

## Core Contribution

The contribution is the capacity-allocation perspective plus a Capacity Manipulation method that explicitly reserves model capacity for minority knowledge. The paper combines empirical evidence, theoretical analysis, low-rank parameter decomposition, and a capacity manipulation loss.

## Method

The method decomposes model parameters into low-rank components and adds a loss that shapes how capacity is allocated across classes. The goal is to reduce unnecessary majority-class capacity occupation while giving minority classes enough representational bandwidth to be modeled robustly.

## Experiments and Evidence

The abstract reports extensive experiments showing consistent and significant improvements in robustness on imbalanced datasets. It also states that Capacity Manipulation can be combined with existing imbalance methods for further gains, suggesting the method is orthogonal to common data- or loss-level techniques.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should verify the imbalance ratios, datasets, model scales, computational overhead, low-rank design choices, and whether improvements hold for many-class long tails rather than simpler class-skew settings. There may be tradeoffs between minority quality, majority quality, and global sample diversity.

## Deep Themes

- Capacity allocation as fairness/robustness bottleneck.
- Class-imbalanced generative modeling.
- Low-rank intervention inside diffusion models.
- Orthogonal fixes that compose with existing imbalance methods.

## Subthemes

- Minority-class representation.
- Majority-class capacity monopolization.
- Capacity manipulation loss.
- Low-rank parameter decomposition.
- Robust diffusion under real-world skew.

## Connections to Other Papers

Connects to WIMHF through targeted data/feature correction, to SlaClip and quantized-diffusion work in the ICML notes through training dynamics under constraints, and to broader generative-model efficiency papers where internal allocation choices determine external quality.

## Notes for Cross-Paper Synthesis

This paper reframes imbalance as an internal resource-allocation problem. Across the corpus, this fits a larger pattern where failures are traced to bottlenecks inside representations, rewards, contexts, or capacities rather than only to missing data.
