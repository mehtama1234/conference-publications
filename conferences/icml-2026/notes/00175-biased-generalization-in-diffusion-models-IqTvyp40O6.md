# Biased Generalization in Diffusion Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: IqTvyp40O6
- Authors: Jerome Garnier-Brun; Luca Biggio; Davide Beltrame; Marc Mezard; Luca Saglietti
- Primary area: deep_learning->generative_models_and_autoencoders
- Keywords: Generative Diffusion;Generalization;Memorization;Bias;Data Privacy;Structured Data
- Source URL: https://openreview.net/forum?id=IqTvyp40O6
- PDF URL: https://openreview.net/pdf?id=IqTvyp40O6

## Abstract

Generalization in generative modeling is defined as the ability to learn an underlying distribution from a finite dataset and produce novel samples, with evaluation largely driven by held-out performance and perceived sample quality. In practice, training is often stopped at the minimum of the test loss, taken as an operational indicator of generalization. We challenge this viewpoint by identifying a phase of *biased generalization* during training, in which the model continues to decrease the test loss while favoring samples with anomalously high proximity to training data. By training the same network on two disjoint datasets and comparing the mutual distances of generated samples and their similarity to training data, we introduce a quantitative measure of bias and demonstrate its presence on real images. We then study the mechanism of bias, using a controlled hierarchical data model where access to exact scores and ground-truth statistics allows us to precisely characterize its onset. We attribute this phenomenon to the sequential nature of feature learning in deep networks, where coarse structure is learned early in a data-independent manner, while finer features are resolved later in a way that increasingly depends on individual training samples. Our results show that early stopping at the test loss minimum, while optimal under standard generalization criteria, may be insufficient for privacy-critical applications.

## One-Sentence Claim

Diffusion models can enter a biased generalization phase where test loss keeps improving while generated samples become anomalously close to training data, creating privacy risk.

## Problem

Held-out loss and perceived sample quality may label a diffusion model as generalizing even when its samples increasingly favor training-proximal outputs, which is dangerous for privacy-critical settings.

## Core Contribution

The paper defines and measures biased generalization, demonstrates it on real images, and studies its mechanism in a controlled hierarchical data model with exact scores and ground-truth statistics.

## Method

The authors train the same network on two disjoint datasets, compare mutual distances among generated samples and their similarity to training data, then use a hierarchical data model to characterize the onset of bias and relate it to sequential feature learning.

## Experiments and Evidence

The abstract reports biased generalization on real images and mechanistic evidence that coarse data-independent structure is learned early, while finer features learned later become increasingly tied to individual training samples.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: bias metric definition, datasets, model sizes, training schedules, privacy attack implications, and whether mitigation beyond early stopping is proposed.

## Deep Themes

- Generalization metrics can hide memorization-like bias.
- Feature-learning order affects privacy and sample novelty.
- Test-loss minima may be insufficient stopping criteria for generative models.

## Subthemes

- Diffusion generalization.
- Memorization.
- Data privacy.
- Structured data.
- Training dynamics.
- Early stopping.

## Connections to Other Papers

Connects to privacy, watermarking, unlearning, and synthetic-content detection papers. It also links to prescriptive scaling and evaluation work by challenging the adequacy of standard held-out metrics.

## Notes for Cross-Paper Synthesis

Biased Generalization adds a warning to the evaluation theme: better test loss can coincide with worse privacy and novelty, so generative-model progress needs metrics that track relation to training data.
