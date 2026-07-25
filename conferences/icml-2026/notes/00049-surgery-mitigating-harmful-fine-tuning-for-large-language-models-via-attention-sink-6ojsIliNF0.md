# Surgery: Mitigating Harmful Fine-Tuning for Large Language Models via Attention Sink

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 6ojsIliNF0
- Authors: Guozhi Liu; Weiwei Lin; Tiansheng Huang; Ruichao Mo; Qi Mu; Xiumin Wang; Li Shen
- Primary area: deep_learning->large_language_models
- Keywords: Attention Sinks;Harmful Fine-tuning Defense;Large Language Models
- Source URL: https://openreview.net/forum?id=6ojsIliNF0
- PDF URL: https://openreview.net/pdf?id=6ojsIliNF0

## Abstract

Harmful fine-tuning can invalidate safety alignment of large language models, exposing significant safety risks. In this paper, we utilize the attention sink mechanism to mitigate harmful fine-tuning. Specifically, we first measure a statistic named sink divergence for each attention head and observe that different attention heads exhibit two different signs of sink divergence. To understand its safety implications, we conduct experiments and find that the number of attention heads of positive sink divergence increases along with the increase of the model's harmfulness when undergoing harmful fine-tuning. Based on this finding, we propose a separable sink divergence hypothesis -- attention heads associating with learning harmful patterns during fine-tuning are separable by their sign of sink divergence. Based on the hypothesis, we propose a fine-tuning-stage defense, dubbed Surgery. Surgery utilizes a regularizer for sink divergence suppression, which steers attention heads toward the negative sink divergence group, thereby reducing the model’s tendency to learn and amplify harmful patterns. Extensive experiments demonstrate that Surgery improves defense performance by 5.90\%, 11.25\%, and 9.55\% on the BeaverTails, HarmBench, and SorryBench benchmarks, respectively. Source code is available on https://github.com/Lslland/Surgery.

## One-Sentence Claim

Surgery mitigates harmful LLM fine-tuning by regularizing attention-sink divergence so attention heads are less likely to learn and amplify harmful patterns.

## Problem

Harmful fine-tuning can erode safety alignment, and existing defenses need mechanisms that intervene during fine-tuning before harmful behavior is consolidated.

## Core Contribution

The paper identifies sink divergence as an attention-head statistic correlated with harmfulness during fine-tuning, proposes a separable sink-divergence hypothesis, and introduces Surgery as a fine-tuning-stage defense.

## Method

Surgery uses a regularizer that suppresses positive sink divergence, steering attention heads toward a negative sink-divergence group that is hypothesized to be less associated with harmful pattern learning.

## Experiments and Evidence

The abstract reports defense improvements of 5.90%, 11.25%, and 9.55% on BeaverTails, HarmBench, and SorryBench.

## Limits and Failure Modes

ArXiv searches for this batch hit HTTP 429, so no local PDF is available yet. Details still need checking: sink-divergence definition, causal evidence for the hypothesis, effect on helpfulness, and robustness against adaptive harmful fine-tuning.

## Deep Themes

- Harmful fine-tuning defenses can target internal attention mechanisms.
- Safety-relevant heads may be separable by mechanistic statistics.
- Fine-tuning-time regularization is a different defense layer from inference-time filtering.

## Subthemes

- Harmful fine-tuning.
- Attention sinks.
- Sink divergence.
- Safety regularization.
- Mechanistic safety signals.
- LLM alignment preservation.

## Connections to Other Papers

Connects to Trojan-Speak and Invisible Safety Threat through fine-tuning-enabled safety failures. It also links to activation probes and interpretability-as-intervention papers by using internal model signals as defensive levers.

## Notes for Cross-Paper Synthesis

Surgery adds a defense-side counterpart to adversarial fine-tuning papers: safety may require mechanistic regularizers during adaptation, not only filters after adaptation.
