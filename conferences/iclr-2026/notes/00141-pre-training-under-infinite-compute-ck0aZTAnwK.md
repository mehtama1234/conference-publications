# Pre-training under infinite compute

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: ck0aZTAnwK
- Authors: Konwoo Kim; Suhas Kotha; Percy Liang; Tatsunori Hashimoto
- Primary area: foundation or frontier models, including LLMs
- Keywords: scaling laws;data efficiency;pre-training
- Source URL: https://openreview.net/forum?id=ck0aZTAnwK
- PDF URL: https://openreview.net/pdf?id=ck0aZTAnwK

## Abstract

Since compute grows much faster than web text available for language model pre-training, we ask how one should approach pre-training under fixed data and no compute constraints. We first show that existing data-constrained approaches of increasing epoch count and parameter count overfit, and we improve upon such recipes by tuning regularization, finding that the optimal weight decay is $30\times$ larger than standard practice. Since our regularized recipe monotonically decreases loss following a power law in parameter count, we estimate its best possible performance via the \textbf{asymptote} of its scaling law rather than the performance at a fixed compute budget. We then identify that ensembling independently trained models achieves a significantly lower loss asymptote than the regularized recipe. Our best intervention combining epoching, regularization, parameter scaling, and ensemble scaling achieves an asymptote at 200M tokens using $5.17\times$ less data than our baseline, and our data scaling laws predict that this improvement persists at higher token budgets. We find that our data efficiency gains can be realized at smaller parameter counts as we can distill an ensemble into a student model that is 8$\times$ smaller and retains $83$% of the ensembling benefit. Finally, our interventions designed for validation loss generalize to downstream benchmarks, achieving a $9$% improvement for pre-training evals. Our results show that simple algorithmic improvements can enable significantly more data-efficient pre-training in a compute-rich future.

## One-Sentence Claim

Under fixed data and abundant compute, LLM pretraining becomes more data-efficient through stronger regularization, parameter/epoch scaling, ensembling, and distillation.

## Problem

Compute is growing faster than available high-quality web text, so future pretraining may be data-constrained rather than compute-constrained.

Naively increasing epochs and parameter count over fixed data overfits, limiting gains from compute-rich training.

## Core Contribution

The paper studies pretraining under fixed data and effectively unlimited compute.

It finds much larger weight decay than standard practice is optimal, evaluates performance by scaling-law asymptotes, shows ensembling lowers the loss asymptote, and distills ensemble gains into smaller students.

## Method

The study tunes regularization in data-constrained pretraining and measures scaling behavior as parameter count increases.

It combines epoching, stronger weight decay, parameter scaling, ensemble scaling, and distillation to improve data efficiency.

## Experiments and Evidence

The abstract reports that optimal weight decay is 30x larger than standard practice in this setting.

The best intervention reaches an asymptote at 200M tokens using 5.17x less data than baseline, with predicted persistence at higher token budgets. An 8x smaller distilled student keeps 83 percent of ensembling benefit, and downstream pretraining evals improve by 9 percent.

## Limits and Failure Modes

The infinite-compute framing depends on future economics and may not apply when data filtering, data generation, or model architecture change. Ensembling and distillation also add operational complexity.

Because this note is abstract-only, details still need checking: dataset, scaling-law fit, model sizes, regularization sweep, ensemble count, distillation setup, and downstream benchmark list.

## Deep Themes

- Data-constrained scaling: compute-rich futures require different recipes than compute-optimal dense scaling.
- Regularization under repeated data exposure: overfitting can be controlled by much stronger weight decay.
- Asymptotic pretraining evaluation: loss asymptotes matter when compute is no longer the main limit.
- Ensemble-to-student transfer: expensive compute can be converted into compact deployable models.

## Subthemes

- Infinite-compute pretraining.
- Data efficiency.
- Weight decay.
- Ensemble distillation.

## Connections to Other Papers

This connects to LR-decay curriculum work, MoE sparsity scaling, scaling-law spectra, and Train-before-Test.

It also relates to synthetic-data selection because both ask how to extract more capability from limited high-quality data.

## Notes for Cross-Paper Synthesis

This paper adds a compute-regime theme: as data becomes the bottleneck, pretraining recipes shift from compute-optimal scaling to regularized reuse, ensembling, and distillation.
