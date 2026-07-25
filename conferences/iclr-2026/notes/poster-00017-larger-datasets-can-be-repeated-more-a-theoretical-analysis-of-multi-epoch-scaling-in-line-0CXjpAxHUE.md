# Larger Datasets Can Be Repeated More: A Theoretical Analysis of Multi-Epoch Scaling in Linear Regression

## Metadata

- Conference: iclr-2026
- Status: Poster
- OpenReview ID: 0CXjpAxHUE
- Authors: Tingkai Yan; Haodong Wen; Binghui Li; Kairong Luo; Wenguang Chen; Kaifeng Lyu
- Primary area: learning theory
- Keywords: Deep learning theory;Multi-epoch training;Data-reuse;Optimization;Scaling law;Large language model
- Source URL: https://openreview.net/forum?id=0CXjpAxHUE
- PDF URL: https://openreview.net/pdf?id=0CXjpAxHUE

## Abstract

Large Language Model (LLM) training often processes vast text corpora in a single pass, leaving much available data underutilized. This paper presents a theoretical analysis of how a common workaround, training for multiple epochs on the same dataset, reshapes the data scaling laws. Concretely, given a $K$-epoch training on $N$ samples, how many fresh samples would one-pass training require to match the same performance? We quantify this using the \textit{effective reuse rate} of the data, $E(K, N)$, which we define as the factor by which the dataset must grow under one-pass training to match the test loss of multi-epoch training. Our analysis precisely characterizes the scaling behavior of $E(K, N)$ for SGD in linear regression under either strong convexity or Zipf-distributed data: (1) When $K$ is small, we prove that $E(K, N) \approx K$, indicating that every new epoch yields a linear gain; (2) As $K$ increases, $E(K, N)$ plateaus at a problem-dependent value that grows with $N$ ($\Theta(\log N)$ for the strongly-convex case), implying that larger datasets can be repeated more times before the marginal benefit vanishes. These theoretical findings complement a recent empirical study by [Muennighoff et al. (2023)](https://arxiv.org/abs/2305.16264), which found that training LLMs for up to $4$ epochs results in negligible loss differences compared to using fresh data at each step, \textit{i.e.}, $E(K, N) \approx K$ for $K \le 4$ in our notation. 
    Supported by further empirical validation with LLMs, our results reveal how this behavior depends on the underlying data size and distribution, and underscore the need to explicitly model both factors in future studies of scaling laws with data reuse.

## One-Sentence Claim

The paper theoretically characterizes when multi-epoch training on the same data is equivalent to fresh one-pass data, showing that larger datasets can be reused more before marginal gains plateau.

## Problem

LLM training often uses enormous corpora in near-one-pass regimes, but compute or data constraints can make repeated epochs attractive. The key missing theory is how data reuse changes scaling laws and how many fresh samples one-pass training would need to match multi-epoch training.

## Core Contribution

The paper defines effective reuse rate `E(K, N)`, the one-pass dataset growth factor needed to match K-epoch training on N samples. It characterizes how this rate scales for SGD in linear regression under strong convexity or Zipf-distributed data.

## Method

The analysis studies SGD in linear regression and compares K-epoch training to one-pass training on more fresh samples. It derives regimes where `E(K, N) approximately K` for small K and where reuse benefits plateau at a problem-dependent value that grows with dataset size, including `Theta(log N)` in the strongly convex case.

## Experiments and Evidence

The abstract reports theoretical results supported by further empirical validation with LLMs. It connects to prior empirical evidence that up to four epochs can behave similarly to fresh data, corresponding to near-linear reuse gains for small K.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect the linear-regression assumptions, Zipf model, SGD regime, constants, and how closely the LLM validation matches the theory. Multi-epoch effects in deep models may include memorization, curriculum effects, and optimizer-state dynamics not captured by linear theory.

## Deep Themes

- Multi-epoch scaling laws.
- Data reuse efficiency.
- Effective sample equivalence.
- Dataset size and distribution as reuse limits.

## Subthemes

- Effective reuse rate.
- One-pass versus repeated training.
- Strong convexity.
- Zipf-distributed data.
- LLM empirical validation.

## Connections to Other Papers

Connects to ATLAS through scaling-law modeling, to Intrinsic Entropy through data-size-dependent limits, and to COMPACT/CauKer through the broader question of how much effective training signal a dataset contains.

## Notes for Cross-Paper Synthesis

This paper adds a theoretical language for data reuse. It suggests that repeated data is not automatically wasteful; its value depends on dataset size, distribution, and training regime.
