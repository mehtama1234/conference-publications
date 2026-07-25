# To Grok Grokking: Provable Grokking in Ridge Regression

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 5nNNVY8NW4
- Authors: Mingyue Xu; Gal Vardi; Itay Safran
- Primary area: theory->learning_theory
- Keywords: Grokking;Ridge Regression;Generalization;Learning Theory
- Source URL: https://openreview.net/forum?id=5nNNVY8NW4
- PDF URL: https://openreview.net/pdf?id=5nNNVY8NW4

## Abstract

We study *grokking* — the onset of generalization long after overfitting — in a classical ridge regression setting. We prove end-to-end grokking results for learning over-parameterized linear regression models using gradient descent with weight decay. Specifically, we prove that the following stages occur: (i) the model overfits the training data early during training; (ii) poor generalization persists long after overfitting has manifested; and (iii) the generalization error eventually becomes arbitrarily small. Moreover, we show, both theoretically and empirically, that grokking can be amplified or eliminated in a principled manner through proper hyperparameter tuning. To the best of our knowledge, these are the first rigorous quantitative bounds on the generalization delay (which we refer to as the "grokking time") in terms of training hyperparameters. Lastly, going beyond the linear setting, we empirically demonstrate that our quantitative bounds also capture the behavior of grokking on non-linear neural networks. Our results suggest that grokking is not an inherent failure mode of deep learning, but rather a consequence of specific training conditions, and thus does not require fundamental changes to the model architecture or learning algorithm to avoid.

## One-Sentence Claim

Grokking can be proved and quantitatively controlled in over-parameterized ridge regression, showing delayed generalization arises from training conditions rather than requiring deep nonlinear architecture.

## Problem

Grokking is often observed in neural networks as delayed generalization after overfitting, but rigorous end-to-end explanations and quantitative bounds on the delay remain limited.

## Core Contribution

The paper proves an end-to-end grokking trajectory for ridge regression under gradient descent with weight decay and gives quantitative bounds on grokking time in terms of training hyperparameters.

## Method

It analyzes over-parameterized linear regression in a teacher-student setting, tracks training error and generalization error under gradient descent with weight decay, and identifies hyperparameter regimes that amplify or eliminate delayed generalization.

## Experiments and Evidence

The abstract reports theoretical and empirical evidence that the model first overfits, then maintains poor generalization, then eventually reaches arbitrarily small generalization error; nonlinear neural-network experiments qualitatively match the predicted hyperparameter dependencies.

## Full-Text Upgrade

The full text emphasizes that neither deep nor nonlinear structure is necessary for grokking. The authors define grokking time as the delay between early overfitting and eventual low generalization error, then prove lower bounds on this delay. Weight decay plays a central role: with suitable hyperparameters, it can create a long period of poor generalization after fitting before driving the solution toward a better-generalizing regime.

The paper's informal theorem is later formalized for realizable teacher functions under bounded feature maps. It gives sufficient hyperparameter conditions and shows how changing initialization, dimension, sample count, step size, and weight decay can amplify or remove grokking. Experiments on nonlinear networks suggest the linear bounds capture qualitative behavior beyond the exact ridge setting.

## Limits and Failure Modes

Limits to watch: the proof is for ridge/linear settings with specific assumptions; nonlinear evidence is empirical; and real-world grokking may involve representation learning or data structure beyond this regularized linear mechanism.

## Deep Themes

- Delayed generalization can be a controlled optimization phenomenon.
- Simple models can expose mechanisms previously attributed to deep networks.
- Hyperparameters can create, amplify, or eliminate surprising training dynamics.

## Subthemes

- Grokking.
- Ridge regression.
- Weight decay.
- Generalization delay.
- Over-parameterization.
- Training dynamics theory.

## Connections to Other Papers

Connects to Jacobian spectra, attention spectra, and alignment-sensitive minimax work as another theory paper explaining generalization dynamics through simplified solvable models.

## Notes for Cross-Paper Synthesis

This paper adds a path-dynamics theme: model behavior after overfitting can still evolve substantially, so final generalization depends on training trajectory and regularization timescale.
