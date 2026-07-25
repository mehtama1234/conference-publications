# SlaClip: Gradient Norm Slacks can be Indicator for Adaptive Clipping in DP-SGD

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 48suUeYKdb
- Authors: Shuyan Zou; Shaowei Wang; Zhanxing Zhu; Jin Li; Changyu Dong; Vladimiro Sassone; Han Wu
- Primary area: social_aspects->privacy
- Keywords: Differential Privacy;DP-SGD;Gradient Clipping;Adaptive Clipping;Private Machine Learning
- Source URL: https://openreview.net/forum?id=48suUeYKdb
- PDF URL: https://openreview.net/pdf?id=48suUeYKdb

## Abstract

Differentially private stochastic gradient descent (DP-SGD) achieves privacy by clipping per-sample gradients and injecting Gaussian noise, but its utility is highly sensitive to the choice of the clipping threshold $C$. A fixed $C$ often degrades performance and necessitates repeated empirical calibration. Existing adaptive clipping methods either modify the gradient update in vanilla DP-SGD, causing additional tuning or optimization overhead, or introduce separate private queries to monitor gradient statistics. In contrast, we leverage the *slack* information induced by the standard clipping operation, an overlooked signal in prior work, and show that it provides an effective indication for adapting $C$. 
In light of this, we propose *SlaClip*, a privacy-preserving adaptive clipping strategy using a post-hoc *Slack Indicator*. Under the same training configuration and privacy accountant, *SlaClip* preserves the sampling rule, noise multiplier, and global $\ell_2$ sensitivity bound of vanilla DP-SGD. Therefore, *SlaClip* is a plug-and-play module for vanilla DP-SGD and its variants. Moreover, *SlaClip* is accounted under the same per-step privacy bound, while requiring no additional private query. Across diverse datasets and tasks, experiments show that *SlaClip* consistently outperforms baseline adaptive clipping methods.

## One-Sentence Claim

SlaClip adapts DP-SGD clipping thresholds using slack information already produced by standard clipping, preserving privacy accounting without extra private gradient-statistic queries.

## Problem

DP-SGD utility is sensitive to the clipping threshold, but fixed thresholds require empirical tuning and many adaptive methods add optimization overhead or separate private monitoring queries.

## Core Contribution

The paper proposes a plug-and-play adaptive clipping strategy based on a post-hoc Slack Indicator that uses information induced by the standard clipping operation.

## Method

SlaClip preserves vanilla DP-SGD's sampling rule, noise multiplier, and global L2 sensitivity bound while adapting the clipping threshold from gradient-norm slack signals under the same per-step privacy bound.

## Experiments and Evidence

The abstract reports consistent improvements over baseline adaptive clipping methods across diverse datasets and tasks under the same training configuration and privacy accountant.

## Limits and Failure Modes

No confident local PDF/arXiv match yet, so details still need checking: exact slack-indicator formula, stability under heavy-tailed per-sample gradients, clipping-update schedule, and behavior at very small privacy budgets.

## Deep Themes

- Privacy mechanisms contain underused diagnostic signals.
- Utility improvements can come from reusing existing private computation rather than querying more.
- DP training is shifting toward adaptive methods that preserve accounting simplicity.

## Subthemes

- Differential privacy.
- DP-SGD.
- Adaptive clipping.
- Gradient norm slack.
- Privacy accounting.
- Plug-and-play private training.

## Connections to Other Papers

Connects to Gaussian certified unlearning and privacy/safety papers through formal privacy constraints, and to low-precision/efficiency papers through practical training stability under strict operational limits.

## Notes for Cross-Paper Synthesis

SlaClip adds a privacy-training theme: useful adaptation can be extracted from signals already paid for by the mechanism, avoiding new privacy budget costs.
