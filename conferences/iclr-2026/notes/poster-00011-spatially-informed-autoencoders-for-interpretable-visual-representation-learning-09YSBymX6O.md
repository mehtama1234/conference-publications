# Spatially Informed Autoencoders for Interpretable Visual Representation Learning

## Metadata

- Conference: iclr-2026
- Status: Poster
- OpenReview ID: 09YSBymX6O
- Authors: Dominik Sturm; Hiba Bensalem; Ivo F. Sbalzarini
- Primary area: unsupervised, self-supervised, semi-supervised, and supervised representation learning
- Keywords: autoencoder;visual representation;point process;conditional simulation;interpretable machine learning;self supervision;spatial statistics
- Source URL: https://openreview.net/forum?id=09YSBymX6O
- PDF URL: https://openreview.net/pdf?id=09YSBymX6O

## Abstract

We introduce spatially informed variational autoencoders (SI-VAE) as self-supervised deep-learning models that use stochastic point processes to predict spatial organization patterns from images.  Existing approaches to learning visual representations based on variational autoencoders (VAE) struggle to capture spatial correlations between objects or events, focusing instead on pixel intensities. We address this limitation by incorporating a point-process likelihood, derived from the Papangelou conditional intensity, as a self-supervision target. This results in a hybrid model that learns statistically interpretable representations of spatial localization patterns and enables zero-shot conditional simulation directly from images. Experiments with synthetic images show that SI-VAE improve the classification accuracy of attractive, repulsive, and uncorrelated point patterns from 48% (VAE) to over 80% in the worst case and 90% in the best case, while generalizing to unseen data. We apply SI-VAE to a real-world microscopy data set, demonstrating its use for studying the spatial organization of proteins in human cells and for using the representations in downstream statistical analysis.

## One-Sentence Claim

SI-VAE adds point-process self-supervision to variational autoencoders so visual representations capture interpretable spatial organization patterns rather than only pixel intensity structure.

## Problem

Standard VAE-style visual representation learning often misses correlations between spatially localized objects or events. For scientific images such as microscopy, downstream questions may depend on whether points are attractive, repulsive, or uncorrelated, not just on texture or intensity.

## Core Contribution

The paper introduces spatially informed VAEs that use a point-process likelihood derived from Papangelou conditional intensity as a self-supervision target. The resulting hybrid model learns statistically interpretable representations and supports zero-shot conditional simulation from images.

## Method

SI-VAE combines image representation learning with spatial statistics. It augments the VAE objective with a point-process likelihood so the latent space must encode localization-pattern structure. The model can then conditionally simulate spatial point patterns directly from images.

## Experiments and Evidence

On synthetic images, SI-VAE improves classification of attractive, repulsive, and uncorrelated point patterns from 48% for a VAE baseline to above 80% in the worst case and 90% in the best case, with generalization to unseen data. The paper also applies the method to microscopy data for protein spatial organization in human cells.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect point extraction assumptions, sensitivity to localization noise, scalability to dense scenes, microscopy dataset properties, and whether learned representations remain interpretable under complex multi-class cellular structures.

## Deep Themes

- Spatial-statistical self-supervision.
- Interpretable visual representation learning.
- Point processes for image understanding.
- Conditional simulation from learned representations.

## Subthemes

- SI-VAE.
- Papangelou conditional intensity.
- Attractive/repulsive point patterns.
- Protein spatial organization.
- Microscopy representation learning.

## Connections to Other Papers

Connects to DA3 and representation-geometry work through geometry-aware visual modeling, to RealPDEBench and OrbEvo through scientific ML with domain-structured representations, and to provable/diagnostic interpretability papers through statistically meaningful latent factors.

## Notes for Cross-Paper Synthesis

SI-VAE reinforces the domain-native representation theme: for spatial scientific images, the right supervision target may be a point-process statistic rather than a generic reconstruction loss.
