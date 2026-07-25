# Local Redundancy: An Information-Theoretic Measure of Plasticity from Synthetic Memorization

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: ucbH88BgIk
- Authors: Jiaxuan Cheng
- Primary area: theory->deep_learning
- Keywords: plasticity;continual learning;transfer learning;information theory
- Source URL: https://openreview.net/forum?id=ucbH88BgIk
- PDF URL: https://openreview.net/pdf?id=ucbH88BgIk

## Abstract

Plasticity—a neural network's ability to adapt to new tasks—is critical for continual and transfer learning. Existing measures, such as effective rank, dead neuron fraction, and weight norm, lack theoretical grounding and correlate poorly with performance on new tasks. We introduce *local redundancy*, an information-theoretic measure derived from universal compression theory. We define local redundancy as the worst-case redundancy of a local model family—parameters in an infinitesimal neighborhood along gradient directions—and show this is a principled measure of plasticity. Although local redundancy is intractable to compute exactly, we prove that the expected squared gradient norm on a synthetic memorization task provides an efficiently computable lower bound. Experiments on continual image classification and time series transfer learning demonstrate that local redundancy predicts downstream performance better than existing measures and enables pretraining checkpoint selection where validation loss plateaus.

## One-Sentence Claim

Local redundancy measures neural-network plasticity through information-theoretic worst-case redundancy, with synthetic memorization gradient norms providing a computable lower bound predictive of transfer and continual-learning performance.

## Problem

Plasticity, the ability to adapt to new tasks, is essential for continual and transfer learning. Existing proxies such as effective rank, dead neuron fraction, and weight norms are weakly grounded and often correlate poorly with downstream adaptability.

Practitioners need a measure that can distinguish checkpoints whose validation loss is similar but whose future learning capacity differs.

## Core Contribution

The paper introduces local redundancy, an information-theoretic measure derived from universal compression theory. It defines plasticity as worst-case redundancy of a local model family in an infinitesimal neighborhood along gradient directions.

Because exact computation is intractable, the paper proves that expected squared gradient norm on a synthetic memorization task gives an efficient lower bound. This proxy predicts downstream performance better than existing measures.

## Method

Local redundancy examines how much extra description cost or redundancy remains in the local parameter neighborhood relevant to gradient-based adaptation. High useful redundancy indicates capacity to encode new information without disrupting existing function.

The computable estimator trains or evaluates on synthetic memorization tasks and measures expected squared gradient norms. These gradients lower-bound local redundancy and can be used for checkpoint selection.

## Experiments and Evidence

The abstract reports experiments on continual image classification and time-series transfer learning. Local redundancy predicts downstream performance better than effective rank, dead neuron fraction, and weight norm, and helps select pretraining checkpoints when validation loss plateaus.

Full-paper reading should verify synthetic memorization construction, correlation metrics, checkpoint-selection protocol, and whether the measure is robust across architectures and scales.

## Limits and Failure Modes

The measure is an indirect lower bound, not exact local redundancy. Synthetic memorization tasks may favor certain architectures or adaptation mechanisms and may not reflect all target tasks.

Computing the proxy adds evaluation cost, and its predictive power may depend on choosing synthetic data that probes relevant plasticity dimensions.

## Deep Themes

- Plasticity as information redundancy: adaptability is tied to local capacity for new information.
- Synthetic probes for future learning: artificial memorization reveals properties not visible in validation loss.
- Checkpoint selection beyond loss: plateaued models can differ in downstream adaptability.
- Continual learning diagnostics: measure the ability to change before training on the next task.

## Subthemes

- Effective rank and dead-neuron counts are insufficient plasticity proxies.
- Gradient norms can lower-bound information-theoretic redundancy.
- Local neighborhoods along gradient directions define adaptation-relevant capacity.
- Time-series transfer tests plasticity outside image classification.

## Connections to Other Papers

This paper connects to SDFT continual learning, post-training support barriers, and LLM adaptability limits. All ask what makes a model capable of changing without losing previous behavior.

It also relates to OPUS and data-selection work because both use proxy signals to predict future training utility.

## Notes for Cross-Paper Synthesis

The synthesis point is that future adaptability is a latent property. Validation loss can look saturated while plasticity varies, so long-horizon training needs diagnostics of remaining learnability.
