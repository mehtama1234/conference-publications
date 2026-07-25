# Disentangling Latent Risk Pathways via Bayesian Hypergraph Inference

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: vNfbqRzash
- Authors: Shengxian Ding; Haonan Gao; Pangpang Liu; Xinyuan Tian; Yize Zhao
- Primary area: probabilistic_methods->bayesian_models_and_methods
- Keywords: Bayesian Inference;Hypergraph;Structural Learning;Variational Inference
- Source URL: https://openreview.net/forum?id=vNfbqRzash
- PDF URL: https://openreview.net/pdf?id=vNfbqRzash

## Abstract

Electronic health records (EHR) pose large-scale multi-disease modeling problems in which many outcomes are rare and strongly influenced by shared risk factors. While modern approaches achieve strong predictive performance, they often treat diseases independently or rely on black-box architectures, offering limited insight into how risk factors organize disease risk and little principled uncertainty quantification.
We introduce a Bayesian hypergraph inference framework that reframes multi-disease modeling around **latent, risk-factor-modulated disease pathways**. Risk factors act on hyperedges, latent disease subsets with shared risk patterns, allowing diseases to participate in multiple distinct pathways and enabling interpretable, higher-order structure beyond pairwise associations. A repulsion prior encourages parsimonious and identifiable structure, while posterior inference provides calibrated uncertainty over both disease groupings and risk-factor influence. 
To enable scalable inference on large EHR datasets, we develop a structured variational inference algorithm that preserves logical dependencies among hyperedge existence, disease membership, and pathway-level effects. 
Experiments on simulated data and UK Biobank demonstrate stable and interpretable disease pathway structure, well-calibrated uncertainty, improved estimation for rare diseases, and competitive predictive performance.

## One-Sentence Claim

Bayesian hypergraph inference models EHR disease risk through latent, risk-factor-modulated disease pathways, giving interpretable higher-order structure and calibrated uncertainty for rare outcomes.

## Problem

Electronic health records create multi-disease prediction problems with rare outcomes and shared risk factors. Strong predictive models often treat diseases independently or use black-box architectures that obscure how risk factors organize disease risk.

Pairwise associations are insufficient when diseases participate in multiple overlapping pathways. Clinical usefulness also requires uncertainty about disease groupings and risk-factor influence.

## Core Contribution

The paper introduces a Bayesian hypergraph model where hyperedges represent latent disease subsets with shared risk patterns, and risk factors modulate these pathway-level effects.

A repulsion prior encourages parsimonious identifiable pathway structure, while posterior inference provides calibrated uncertainty over disease groupings and risk-factor influence. Structured variational inference makes the approach scalable for large EHR data.

## Method

Diseases can belong to multiple hyperedges, allowing overlapping higher-order pathways beyond pairwise correlations. Risk factors act on hyperedges, modulating the risk of disease subsets together.

The structured variational inference algorithm preserves logical dependencies among hyperedge existence, disease membership, and pathway-level effects, rather than factorizing away the structure that makes the model interpretable.

## Experiments and Evidence

The abstract reports experiments on simulated data and UK Biobank. Results show stable and interpretable disease pathway structure, calibrated uncertainty, improved estimation for rare diseases, and competitive predictive performance.

Full-paper reading should verify disease/risk-factor sets, calibration metrics, rare-disease improvements, variational approximations, prior sensitivity, and clinical interpretability validation.

## Limits and Failure Modes

EHR data is observational, biased by healthcare access and measurement practices, and may contain coding artifacts. Interpretable pathways are statistical structures, not necessarily causal disease mechanisms.

Hypergraph inference can be sensitive to priors and variational approximations. Clinical deployment would require validation beyond UK Biobank and careful treatment of privacy and fairness.

## Deep Themes

- Higher-order disease structure: hyperedges model shared pathways beyond pairwise links.
- Bayesian uncertainty for interpretability: posterior distributions expose confidence in groupings and risk effects.
- Rare outcome support: shared pathways improve estimation where individual disease data is sparse.
- Structured variational inference: scalability must preserve logical dependencies.

## Subthemes

- Risk factors modulate latent disease subsets.
- Repulsion priors encourage parsimony and identifiability.
- Diseases can participate in multiple pathways.
- EHR models need both predictive accuracy and uncertainty.

## Connections to Other Papers

This paper connects to MIRA, structure learning, local covariate selection, and categorical ANOVA through probabilistic structure and uncertainty. It also relates to scientific-domain papers where interpretability is tied to latent physical or biological pathways.

It fits the broader theme of set/hypergraph representations for complex real-world dependencies.

## Notes for Cross-Paper Synthesis

The synthesis point is that higher-order structure matters in biomedical data. Pairwise or independent disease models can miss shared latent pathways that improve both rare-disease estimation and interpretability.
