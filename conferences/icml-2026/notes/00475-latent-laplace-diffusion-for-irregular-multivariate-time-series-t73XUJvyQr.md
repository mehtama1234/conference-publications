# Latent Laplace Diffusion for Irregular Multivariate Time Series

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: t73XUJvyQr
- Authors: Zinuo You; Jin Zheng; John Cartlidge
- Primary area: deep_learning->sequential_models_time_series
- Keywords: Time Series Modeling;Diffusion Models;Continuous-time Models;Irregularly Sampled Data
- Source URL: https://openreview.net/forum?id=t73XUJvyQr
- PDF URL: https://openreview.net/pdf?id=t73XUJvyQr

## Abstract

Irregular multivariate time series impose a trade-off for long-horizon forecasting: discrete methods can distort temporal structure via re-gridding, while continuous-time models often require sequential solvers prone to drift. To bridge this gap, we present Latent Laplace Diffusion (LLapDiff), a generative framework that models the target as a low-dimensional latent trajectory, enabling horizon-wide generation without step-by-step integration over physical time. We guide the reverse process utilizing a stable modal parameterization motivated by stochastic port-Hamiltonian dynamics, and parameterize its mean evolution in the Laplace domain via learnable complex-conjugate poles, enabling direct evaluation over irregular timestamps. We also link continuous dynamics to irregular observations through renewal-averaging analysis, which maps sampling gaps to effective event-domain poles and motivates a gap-aware history summarizer. Extensive experiments show that LLapDiff improves over baselines in long-horizon forecasting, and its continuous-time generative nature supports missing-value imputation by querying the same model at historical timestamps. Code is available at \url{https://github.com/pixelhero98/LLapDiffusion}.

## One-Sentence Claim

LLapDiff forecasts irregular multivariate time series by generating low-dimensional latent trajectories in the Laplace domain, avoiding re-gridding and stepwise continuous-time integration.

## Problem

Irregular multivariate time series create a long-horizon forecasting tradeoff. Discrete methods often re-grid observations and distort temporal structure, while continuous-time models require sequential solvers that can drift over long horizons.

The challenge is to model irregular timestamps directly while generating forecasts over the whole horizon, without expensive or unstable step-by-step physical-time integration.

## Core Contribution

The paper introduces Latent Laplace Diffusion, a generative framework that models the target as a low-dimensional latent trajectory. The reverse process is guided by a stable modal parameterization inspired by stochastic port-Hamiltonian dynamics.

It parameterizes mean evolution in the Laplace domain through learnable complex-conjugate poles, allowing direct evaluation at irregular timestamps. Renewal-averaging analysis links continuous dynamics to irregular observations and motivates a gap-aware history summarizer.

## Method

LLapDiff runs diffusion in a latent trajectory space rather than directly over high-dimensional observations. The Laplace-domain parameterization lets the model evaluate continuous-time dynamics at arbitrary timestamps through learned modal poles.

The gap-aware history summarizer accounts for irregular sampling gaps, using renewal-averaging analysis to map observation gaps to effective event-domain poles. The same continuous-time generative model can forecast future timestamps and impute missing historical values.

## Experiments and Evidence

The abstract reports extensive experiments showing improvements over baselines in long-horizon forecasting. It also highlights missing-value imputation by querying the model at historical timestamps.

Full-paper reading should verify datasets, irregularity patterns, forecasting horizons, baselines, imputation protocol, ablations for Laplace poles and gap-aware summarization, and computational cost.

## Limits and Failure Modes

Low-dimensional latent trajectories may underrepresent systems with many independent modes or abrupt regime changes. Complex-conjugate pole parameterization imposes a modal structure that may not fit all time-series domains.

Diffusion generation can be computationally heavier than deterministic forecasting unless the latent/horizon-wide formulation yields enough sampling efficiency.

## Deep Themes

- Continuous-time generation without stepwise solvers: forecast horizons are generated directly in latent space.
- Laplace-domain temporal modeling: irregular timestamps are handled through analytic modal evaluation.
- Stable dynamics as inductive bias: port-Hamiltonian motivation guides the reverse process.
- Unified forecasting and imputation: the same model can query future and missing historical times.

## Subthemes

- Re-gridding can distort irregular temporal structure.
- Sequential solvers can drift in long-horizon continuous-time models.
- Learnable complex poles encode temporal modes.
- Sampling gaps should affect history summarization.

## Connections to Other Papers

LLapDiff connects to ConFlux, latent distribution matching, CoEvol-NO, and MIRA through time-series, latent dynamics, and probabilistic modeling. It also relates to XDLM and diffusion language work as another domain-specific diffusion formulation.

It fits the scientific/temporal modeling theme: domain-specific transforms, such as Laplace-domain dynamics, can make generative models better matched to the data structure.

## Notes for Cross-Paper Synthesis

LLapDiff contributes to the idea that temporal foundation and generative models need continuous-time inductive bias when observations are irregular. Tokenizing time is not enough; the sampling process itself must be modeled.
