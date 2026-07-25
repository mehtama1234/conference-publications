# Decentralized Attention Fails Centralized Signals: Rethinking Transformers for Medical Time Series

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: oZJFY2BQt2
- Authors: Guoqi Yu; Juncheng Wang; Chen Yang; Jing Qin; Angelica I Aviles-Rivero; Shujun Wang
- Primary area: applications to physical sciences (physics, chemistry, biology, etc.)
- Keywords: EEG;ECG;Deep learning;Transformer
- Source URL: https://openreview.net/forum?id=oZJFY2BQt2
- PDF URL: https://openreview.net/pdf?id=oZJFY2BQt2

## Abstract

Accurate analysis of Medical time series (MedTS) data, such as Electroencephalography (EEG) and Electrocardiography (ECG), plays a pivotal role in healthcare applications, including the diagnosis of brain and heart diseases. MedTS data typically exhibits two critical patterns: **temporal dependencies** within individual channels and **channel dependencies** across multiple channels. While recent advances in deep learning have leveraged Transformer-based models to effectively capture temporal dependencies, they often struggle to model channel dependencies. This limitation stems from a structural mismatch: ***MedTS signals are inherently centralized, whereas the Transformer's attention is decentralized***, making it less effective at capturing global synchronization and unified waveform patterns. To bridge this gap, we propose **CoTAR** (Core Token Aggregation-Redistribution), a centralized MLP-based module tailored to replace the decentralized attention. Instead of allowing all tokens to interact directly, as in attention, CoTAR introduces a global core token that acts as a proxy to facilitate the inter-token interaction, thereby enforcing a centralized aggregation and redistribution strategy. This design not only better aligns with the centralized nature of MedTS signals but also reduces computational complexity from quadratic to linear. Experiments on five benchmarks validate the superiority of our method in both effectiveness and efficiency, achieving up to a **12.13%** improvement on the APAVA dataset, with merely 33% memory usage and 20% inference time compared to the previous state-of-the-art. Code and all training scripts are available in this [**Link**](https://github.com/Levi-Ackman/TeCh).

## One-Sentence Claim

CoTAR replaces decentralized attention with centralized core-token aggregation and redistribution, better matching medical time-series channel dependencies while reducing memory and inference cost.

## Problem

Medical time series such as EEG and ECG contain temporal dependencies within channels and synchronized dependencies across channels. Transformer attention can capture temporal patterns but may be structurally mismatched to centralized cross-channel physiological signals.

## Core Contribution

The paper proposes CoTAR, a centralized MLP-based module using a global core token as a proxy for inter-token interaction. It is designed to replace attention for MedTS modeling, align with centralized signal structure, and reduce complexity from quadratic to linear.

## Method

CoTAR aggregates information into a global core token and redistributes it to individual tokens, enforcing centralized interaction rather than all-pairs decentralized attention. The module is integrated into medical time-series models for EEG/ECG-style data.

## Experiments and Evidence

Across five benchmarks, the abstract reports better effectiveness and efficiency, including up to 12.13 percent improvement on APAVA, with 33 percent memory usage and 20 percent inference time relative to the previous state of the art. Code and training scripts are linked.

## Limits and Failure Modes

Centralized aggregation may underperform when signals contain important local or pairwise channel interactions not captured by one core token. Medical datasets can have site, device, and patient distribution shifts. Full-text review should check benchmark details, channel counts, ablations, clinical labels, and robustness to missing/noisy channels.

## Deep Themes

- Domain-structured replacements for generic attention.
- Medical time-series channel synchronization.
- Centralized aggregation for physiological signals.
- Linear-complexity sequence modeling.

## Subthemes

- Core Token Aggregation-Redistribution.
- EEG and ECG modeling.
- Channel dependency modeling.
- Attention mismatch in MedTS.
- Efficient clinical signal inference.

## Connections to Other Papers

Connects to BioX-Bridge and biomedical agent/environment papers through healthcare ML, to FlashRNN and Mamba work through alternatives to standard attention, and to scientific-domain modeling where architecture should reflect signal structure.

## Notes for Cross-Paper Synthesis

CoTAR fits the theme that Transformers are not default-optimal for every domain. When data have known organization, architecture can become simpler, cheaper, and more accurate by matching that organization.
