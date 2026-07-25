# Understanding Self-Supervised Learning via Latent Distribution Matching

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: schXkGSTus
- Authors: Fabian A Mikulasch; Friedemann Zenke
- Primary area: deep_learning->selfsupervised_learning
- Keywords: Contrastive Learning;Nonlinear ICA;Identifiability;System identification;Bayesian filtering;Manifold normalizing flow
- Source URL: https://openreview.net/forum?id=schXkGSTus
- PDF URL: https://openreview.net/pdf?id=schXkGSTus

## Abstract

Self-supervised learning (SSL) excels at finding general-purpose latent representations from complex data, yet lacks a unifying theoretical framework that explains the diverse existing methods and guides the design of new ones. We cast SSL as latent distribution matching (LDM): learning representations that maximize their log-probability under an assumed latent model (alignment), while maximizing latent entropy to prevent collapse (uniformity). This view unifies independent component analysis with contrastive, non-contrastive, and predictive SSL methods, including stop gradient approaches. Leveraging LDM, we derive a nonlinear, sampling-free Bayesian filtering model with a Kalman-based predictor for high-dimensional timeseries. We further prove that predictive LDM yields identifiable latent representations under mild assumptions, even with nonlinear predictors. Overall, LDM clarifies the assumptions behind established SSL methods and provides principled guidance for developing new approaches.

## One-Sentence Claim

Self-supervised learning can be unified as latent distribution matching, where alignment maximizes likelihood under a latent model while uniformity maximizes entropy to prevent collapse.

## Problem

Self-supervised learning has many variants: contrastive, non-contrastive, predictive, stop-gradient, and classical independent-component approaches. These methods often work well but lack a shared theoretical account explaining their assumptions and design tradeoffs.

The key problem is to explain why SSL learns useful representations while avoiding collapse, and to derive new methods from a principled framework rather than from disconnected recipes.

## Core Contribution

The paper casts SSL as Latent Distribution Matching. Representations should have high probability under an assumed latent model, giving alignment, while maintaining high entropy, giving uniformity.

This view unifies ICA with contrastive, non-contrastive, predictive, and stop-gradient SSL methods. It also yields a nonlinear sampling-free Bayesian filtering model with a Kalman-based predictor for high-dimensional time series and proves identifiability of predictive LDM under mild assumptions.

## Method

LDM specifies an assumed latent distribution and trains representations to match it. The alignment term pulls related views or predictions toward high-likelihood latent configurations, while the entropy/uniformity term prevents trivial collapse.

For time series, the authors derive a Bayesian filtering model that avoids sampling and uses a Kalman-based predictor. The predictive setting is analyzed for identifiability even with nonlinear predictors.

## Experiments and Evidence

The abstract reports theoretical unification across SSL families, derivation of a new filtering model, and identifiability proof for predictive LDM. It does not list empirical benchmarks in the abstract.

Full-paper reading should verify which SSL losses are recovered exactly versus approximately, the assumptions behind identifiability, and empirical behavior of the Bayesian filtering model.

## Limits and Failure Modes

The framework depends on the assumed latent model. If the latent distribution is misspecified, the alignment/uniformity interpretation may guide representation learning in the wrong direction.

Identifiability under mild assumptions is valuable, but real data may violate stationarity, independence, or observation assumptions. The theory's practical implications for large multimodal SSL require careful validation.

## Deep Themes

- SSL as distribution matching: representation learning is framed as fitting a latent generative structure.
- Alignment-uniformity unification: collapse avoidance becomes entropy maximization under a shared objective.
- Identifiability for predictive representations: useful latents can be theoretically recoverable.
- Bridging classical and modern methods: ICA and SSL become points in one framework.

## Subthemes

- Stop-gradient methods can be interpreted inside distribution matching.
- Bayesian filtering links SSL to system identification and time-series inference.
- Sampling-free predictors reduce computational burden.
- Latent assumptions make representation objectives explicit.

## Connections to Other Papers

This paper connects to ConFlux, LLapDiff, and MIRA through latent modeling of time series and conditional distributions. It also relates to scaling-law and grammar-substructure papers as a theory-driven attempt to explain representation learning mechanisms.

Its alignment/uniformity framing connects to contrastive hypergraph and concept-binding papers in the representation geometry theme.

## Notes for Cross-Paper Synthesis

The synthesis point is that representation learning papers are increasingly explicit about latent assumptions. Rather than treating SSL as a bag of losses, LDM turns it into a probabilistic matching problem.
