# Uncover Underlying Correspondence for Robust Multi-view Clustering

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: a4S1nQay3b
- Authors: Haochen Zhou; Guofeng Ding; Mouxing Yang; Peng Hu; Yijie Lin; Xi Peng
- Primary area: unsupervised, self-supervised, semi-supervised, and supervised representation learning
- Keywords: Multi-view clustering; Noisy Correspondence
- Source URL: https://openreview.net/forum?id=a4S1nQay3b
- PDF URL: https://openreview.net/pdf?id=a4S1nQay3b

## Abstract

Multi-view clustering (MVC) aims to group unlabeled data into semantically meaningful clusters by leveraging cross-view consistency. 
However, real-world datasets collected from the web often suffer from noisy correspondence (NC), which breaks the consistency prior and results in unreliable alignments.
In this paper, we identify two critical forms of NC that particularly harm clustering: i) category-level mismatch, where semantically consistent samples from the same class are mistakenly treated as negatives; and ii) sample-level mismatch, where collected cross-view pairs are misaligned and some samples may even lack any valid counterpart.
To address these challenges, we propose \textbf{CorreGen}, a generative framework that formulates noisy correspondence learning in MVC as maximum likelihood estimation over underlying cross-view correspondences. 
The objective is elegantly solved via an Expectation–Maximization algorithm: in the E-step, soft correspondence distributions are inferred across views, capturing class-level relations while adaptively down-weighting noisy or unalignable samples through GMM-guided marginals; in the M-step, the embedding network is updated to maximize the expected log-likelihood. Extensive experiments on both synthetic and real-world noisy datasets demonstrate that our method significantly improves clustering robustness. The code will be released upon acceptance.

## One-Sentence Claim

CorreGen improves multi-view clustering under noisy correspondence by inferring soft underlying cross-view alignments with an EM-style generative framework.

## Problem

Multi-view clustering relies on cross-view consistency, but web-collected data often contains noisy correspondences that break this assumption.

Two harmful cases are category-level mismatch, where semantically same-class samples are treated as negatives, and sample-level mismatch, where paired samples are misaligned or lack valid counterparts.

## Core Contribution

The paper proposes CorreGen, a generative framework for noisy-correspondence learning in multi-view clustering.

It formulates the problem as maximum likelihood estimation over underlying cross-view correspondences and solves it with an Expectation-Maximization algorithm.

## Method

In the E-step, CorreGen infers soft correspondence distributions across views, capturing class-level relationships while down-weighting noisy or unalignable samples using GMM-guided marginals.

In the M-step, the embedding network is updated to maximize expected log-likelihood under those inferred correspondences.

## Experiments and Evidence

The abstract reports extensive experiments on synthetic and real-world noisy datasets.

CorreGen significantly improves clustering robustness under noisy correspondence.

## Limits and Failure Modes

EM-style methods can be sensitive to initialization and may reinforce incorrect correspondences if early estimates are poor. GMM marginals may also struggle with highly non-Gaussian or imbalanced clusters.

Because this note is abstract-only, details still need checking: noise models, datasets, initialization, convergence behavior, clustering metrics, and comparison to contrastive MVC baselines.

## Deep Themes

- Hidden correspondence inference: noisy pairs are treated as latent variables rather than fixed labels.
- Robust cross-view consistency: alignment must account for both class-level and sample-level mismatch.
- Generative clustering under noise: maximum likelihood and EM provide structure for representation learning.
- Adaptive down-weighting of invalid samples: not every cross-view pair deserves equal training influence.

## Subthemes

- Multi-view clustering.
- Noisy correspondence.
- EM optimization.
- GMM-guided marginals.

## Connections to Other Papers

This connects to WAVE, TabStruct, UniImb, and multi-view graph anomaly detection through cross-view representation robustness.

It also relates to contrastive visual reasoning because both use paired examples while addressing failures in naive correspondence assumptions.

## Notes for Cross-Paper Synthesis

CorreGen adds a correspondence-robustness theme: multi-view learning needs to infer which alignments are trustworthy instead of assuming collected pairs are correct.
