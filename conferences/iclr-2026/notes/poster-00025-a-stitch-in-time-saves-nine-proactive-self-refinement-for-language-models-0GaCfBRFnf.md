# A Stitch in Time Saves Nine: Proactive Self-Refinement for Language Models

## Metadata

- Conference: iclr-2026
- Status: Poster
- OpenReview ID: 0GaCfBRFnf
- Authors: Jinyi Han; Xinyi Wang; Haiquan Zhao; tingyun li; Zishang Jiang; Sihang Jiang; Jiaqing Liang; Xin Alex Lin; Weikang Zhou; Zeye Sun; Fei Yu; Yanghua Xiao
- Primary area: applications to computer vision, audio, language, and other modalities
- Keywords: Large language models;Self-refine
- Source URL: https://openreview.net/forum?id=0GaCfBRFnf
- PDF URL: https://openreview.net/pdf?id=0GaCfBRFnf

## Abstract

Recent advances in self-refinement have demonstrated significant potential for improving the outputs of large language models (LLMs) through iterative refinement. However, most existing self-refinement methods rely on a reactive process with a fixed number of iterations, making it difficult to determine the optimal timing and content of refinement based on the evolving generation context. Inspired by the way humans dynamically refine their thoughts during execution, we propose ProActive Self-Refinement (PASR), a novel method that enables LLMs to refine their outputs during the generation process. Unlike methods that regenerate entire responses, PASR proactively decides whether, when, and how to refine based on the model’s internal state and evolving context. We conduct extensive experiments on a diverse set of 10 tasks to evaluate the effectiveness of PASR. Experimental results show that PASR significantly enhances problem-solving performance. In particular, on Qwen3-8B, PASR reduces average token consumption by 41.6% compared to standard generation, while also achieving an 8.2% improvement in accuracy. Our code and all baselines used in the paper are available in the GitHub.

## One-Sentence Claim

TODO

## Problem

TODO

## Core Contribution

TODO

## Method

TODO

## Experiments and Evidence

TODO

## Limits and Failure Modes

TODO

## Deep Themes

TODO

## Subthemes

TODO

## Connections to Other Papers

TODO

## Notes for Cross-Paper Synthesis

TODO
