# Differentially Private Domain Discovery

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: yBpzF8hp3J
- Authors: Vinod Raman; Travis Dick; Matthew Joseph
- Primary area: alignment, fairness, safety, privacy, and societal considerations
- Keywords: Differential Privacy;Partition Selection;Top-k Selection
- Source URL: https://openreview.net/forum?id=yBpzF8hp3J
- PDF URL: https://openreview.net/pdf?id=yBpzF8hp3J

## Abstract

We study several problems in differentially private domain discovery, where each user holds a subset of items from a shared but unknown domain, and the goal is to output an informative subset of items. For set union, we  show that the simple baseline Weighted Gaussian Mechanism (WGM) has a near-optimal $\ell_1$ missing mass guarantee on Zipfian data as well as a distribution-free $\ell_\infty$ missing mass guarantee. We then apply the WGM as a domain-discovery precursor for existing known-domain algorithms for private top-$k$ and $k$-hitting set and obtain new utility guarantees for their unknown domain variants. Finally, experiments demonstrate that all of our WGM-based methods are competitive with or outperform existing baselines for all three problems.

## One-Sentence Claim

The paper shows that a simple Weighted Gaussian Mechanism can provide strong guarantees for differentially private unknown-domain discovery and improve private top-k and hitting-set tasks.

## Problem

Many private data-analysis algorithms assume the item domain is known, but in practice each user may hold items from a shared unknown domain. The system must discover informative items while preserving differential privacy and avoiding excessive missing mass.

## Core Contribution

The paper studies private domain discovery for set union, top-k, and k-hitting set. It proves near-optimal `l1` missing-mass guarantees for the Weighted Gaussian Mechanism on Zipfian data, distribution-free `l_infinity` guarantees, and new utility guarantees when WGM is used as a precursor to known-domain private algorithms.

## Method

The approach uses the Weighted Gaussian Mechanism to privately select or weight candidate domain items. For top-k and k-hitting-set variants, WGM first discovers a usable domain subset, then existing known-domain private algorithms operate on that discovered domain.

## Experiments and Evidence

The abstract reports experiments on all three problems, with WGM-based methods competitive with or better than existing baselines. The theoretical evidence includes missing-mass guarantees and utility guarantees for unknown-domain variants.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect privacy definitions, constants, domain-size dependence, Zipfian assumptions, user contribution bounds, and performance under flatter or adversarial item distributions. Domain discovery can fail when rare but important items are privacy-expensive to surface.

## Deep Themes

- Differential privacy under unknown domains.
- Private set union and selection.
- Missing-mass guarantees.
- Utility-preserving preprocessing for private algorithms.

## Subthemes

- Weighted Gaussian Mechanism.
- Partition selection.
- Top-k selection.
- k-hitting set.
- Zipfian data.

## Connections to Other Papers

Connects to data-governance themes in WIMHF and Semantic Watermark Fingerprints, and to Track-and-Stop through finite utility guarantees for adaptive or selective information gathering under constraints.

## Notes for Cross-Paper Synthesis

This paper adds a privacy-specific version of the corpus's selection theme: before learning or ranking, systems often must decide which parts of the world may be safely exposed. The key object is not only accuracy but missing mass under privacy constraints.
