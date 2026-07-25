# Self-Soupervision: Cooking Model Soups without Labels

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: z0UM7y0L4r
- Authors: Anthony Fuller; James R Green; Evan Shelhamer
- Primary area: deep_learning
- Keywords: model soups;self-supervised learning;robustness;computer vision
- Source URL: https://openreview.net/forum?id=z0UM7y0L4r
- PDF URL: https://openreview.net/pdf?id=z0UM7y0L4r

## Abstract

Model soups are strange and strangely effective combinations of parameters. They take a model (the stock), fine-tune it into multiple models (the ingredients), and then mix their parameters back into one model (the soup) to improve predictions. While all known soups require supervised learning, and optimize the same loss on labeled data, our recipes for Self-Soupervision generalize soups to self-supervised learning (SSL). Our Self-Souping lets us flavor ingredients on new data sources, e.g. from unlabeled data from a task for transfer or from a shift for robustness. We show that Self-Souping on corrupted test data, then fine-tuning back on uncorrupted train data, boosts robustness by +3.5% (ImageNet-C) and +7% (LAION-C). Self-Soupervision also unlocks countless SSL algorithms to cook the diverse ingredients needed for more robust soups. We show for the first time that ingredients can differ in their SSL hyperparameters---and more surprisingly, in their SSL algorithms. We cook soups of MAE, MoCoV3, MMCR, and LeJEPA ingredients that are more accurate than any single SSL ingredient.

## One-Sentence Claim

Self-Soupervision extends model soups to self-supervised learning, allowing unlabeled data sources, hyperparameter diversity, and even different SSL algorithms to be mixed into more robust models.

## Problem

Model soups improve supervised models by averaging parameters from multiple fine-tuned ingredients, but known recipes rely on labeled data and shared supervised losses.

This limits soups in transfer and robustness settings where labels are unavailable, such as new data sources or shifted/corrupted test distributions.

## Core Contribution

The paper generalizes model soups to self-supervised learning through Self-Souping. Ingredients can be trained on unlabeled data from a target task or distribution shift, and then averaged into a stronger model.

It also shows that soup ingredients can differ not only in SSL hyperparameters but also in the SSL algorithms themselves, mixing MAE, MoCoV3, MMCR, and LeJEPA ingredients.

## Method

Self-Soupervision creates diverse self-supervised ingredients from the same stock model using unlabeled data and varied SSL recipes. Their parameters are then combined into a model soup.

For robustness, the method can self-soup on corrupted test data and then fine-tune back on clean training data, using unlabeled shifted data to improve the final model.

## Experiments and Evidence

The abstract reports robustness gains of +3.5 percent on ImageNet-C and +7 percent on LAION-C when self-souping on corrupted test data followed by fine-tuning back on clean training data.

It also reports that soups composed of different SSL algorithms outperform any single SSL ingredient.

## Limits and Failure Modes

Parameter averaging works best when ingredients remain in compatible basins; algorithm-diverse SSL ingredients may fail if representations diverge too much.

Because this note is abstract-only, details still need checking: model architectures, averaging procedure, unlabeled data protocol, whether test-time corrupted data use is transductive, clean accuracy tradeoffs, and compatibility conditions across SSL algorithms.

## Deep Themes

- Label-free model merging: parameter soups can be cooked from unlabeled adaptation.
- Diversity as robustness: different SSL recipes provide complementary ingredients.
- Shift adaptation without labels: unlabeled shifted data can improve robustness when folded into model weights.
- Algorithmic compatibility: different training objectives can still land in mergeable parameter regions.

## Subthemes

- Self-supervised model soups.
- Corrupted-data self-souping.
- Cross-algorithm SSL ingredients.
- Robustness through parameter averaging.

## Connections to Other Papers

This connects to NASH, data selection, and model merging/modularity papers through the theme of reusing trained components rather than training from scratch.

It also relates to robust vision and multimodal pretraining papers because unlabeled shifted data becomes a resource for robustness.

## Notes for Cross-Paper Synthesis

Self-Soupervision adds to the model-composition theme: capability and robustness can emerge from combining multiple specialized training trajectories, even without labels.
