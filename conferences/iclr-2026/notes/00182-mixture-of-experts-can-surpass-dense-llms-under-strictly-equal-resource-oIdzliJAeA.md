# Mixture-of-Experts Can Surpass Dense LLMs Under Strictly Equal Resource

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: oIdzliJAeA
- Authors: Houyi Li; Ka Man Lo; Shijie Xuyang; Ziqi Wang; Wenzhen Zheng; Haocheng Zhang; Zhao Li; Shuigeng Zhou; Xiangyu Zhang; Daxin Jiang
- Primary area: foundation or frontier models, including LLMs
- Keywords: Large language models (LLM);Pre-training;Mixture-of-Experts (MoE)
- Source URL: https://openreview.net/forum?id=oIdzliJAeA
- PDF URL: https://openreview.net/pdf?id=oIdzliJAeA

## Abstract

Mixture-of-Experts (MoE) language models dramatically expand model capacity and achieve remarkable performance without increasing per-token compute. However, can MoEs surpass dense architectures under strictly equal resource constraints — that is, when the total parameter count, training compute, and data budget are identical? This question remains under-explored despite its significant practical value and potential. In this paper, we propose a novel perspective and methodological framework to study this question thoroughly. First, we comprehensively investigate the architecture of MoEs and achieve an optimal model design that maximizes the performance. Based on this, we subsequently find that an MoE model with activation rate in an optimal region is able to outperform its dense counterpart under the same total parameter, training compute and data resource. More importantly, this optimal region remains consistent across different model sizes. Although additional amount of data turns out to be a trade-off for enhanced performance, we show that this can be resolved via reusing data. We validate our findings through extensive experiments, training nearly 200 language models at 2B scale and over 50 at 7B scale, cumulatively processing 50 trillion tokens. All code and models will be released publicly.

## One-Sentence Claim

MoE language models can outperform dense models even under equal total parameters, compute, and data when the activation rate is chosen in an optimal region.

## Problem

MoEs are often credited with better performance because they increase total capacity without increasing per-token compute, but comparisons to dense models can be confounded by unequal total parameters, training compute, or data. It remains unclear whether MoE architecture itself wins under strict resource parity.

## Core Contribution

The paper provides a controlled framework for comparing MoE and dense LLMs under equal resources, identifies an optimal activation-rate region, shows that this region stays consistent across model scales, and studies data reuse as a way to handle the extra-data tradeoff.

## Method

The authors systematically vary MoE architecture choices and activation rates while matching total parameter count, training compute, and data budget to dense counterparts. They train many models at 2B and 7B scale and evaluate which design choices maximize performance under the parity constraint.

## Experiments and Evidence

The abstract reports nearly 200 language models trained at 2B scale and over 50 at 7B scale, cumulatively processing 50 trillion tokens. It finds that MoEs in an optimal activation-rate region beat dense models under equal total parameters, compute, and data; data reuse mitigates the extra-data tradeoff.

## Limits and Failure Modes

Results may depend on routing, expert count, load balancing, token budget, data quality, optimizer details, and inference resource accounting. Equal total parameter count is not the only deployment constraint; memory bandwidth and serving complexity matter. Full-text review should check exact parity definitions, benchmark suite, scaling trends, and whether MoE gains persist in downstream finetuning.

## Deep Themes

- Resource-fair architecture comparison.
- MoE activation-rate scaling laws.
- Capacity allocation under fixed budgets.
- Data reuse for sparse models.

## Subthemes

- Equal total parameters.
- Equal training compute and data.
- Expert activation rate.
- Sparse routing.
- Dense versus MoE scaling.

## Connections to Other Papers

Connects to pretraining under infinite compute, LoRA-Pre, low-precision training, and FlashRNN through architecture and systems choices under constrained resources. It also informs deployment-efficiency themes where raw parameter count is an incomplete cost metric.

## Notes for Cross-Paper Synthesis

This paper is valuable because it sharpens the MoE question into a fair comparison. Its broader lesson is that architecture claims need resource-normalized evidence, not just per-token-compute narratives.
