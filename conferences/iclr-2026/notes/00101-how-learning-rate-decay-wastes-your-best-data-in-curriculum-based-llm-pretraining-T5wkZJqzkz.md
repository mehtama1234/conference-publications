# How Learning Rate Decay Wastes Your Best Data in Curriculum-Based LLM Pretraining

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: T5wkZJqzkz
- Authors: Kairong Luo; Zhenbo Sun; Haodong Wen; Xinyu Shi; Jiarui Cui; Chenyi Dang; Kaifeng Lyu; Wenguang Chen
- Primary area: foundation or frontier models, including LLMs
- Keywords: LLM pretraining;Curriculum Learning;Model Weight Average
- Source URL: https://openreview.net/forum?id=T5wkZJqzkz
- PDF URL: https://openreview.net/pdf?id=T5wkZJqzkz

## Abstract

Due to the scarcity of high-quality data, large language models (LLMs) are often trained on mixtures of data with varying quality levels, even after sophisticated data curation. A natural approach to better leverage high-quality data is curriculum-based pretraining, where the model is trained on data sorted in ascending order of quality as determined by a quality metric. However, prior studies have reported limited improvements from such curriculum-based pretraining strategies. This work identifies a critical factor constraining these methods: the incompatibility between the ascending data quality order and the decaying learning rate (LR) schedule. We find that while curriculum-based training substantially outperforms random shuffling when using a constant LR, its advantage diminishes under standard LR decay schedules. Our experiments show this incompatibility can be mitigated by two simple strategies: (1) employing a more moderate LR decay schedule, where the final LR is only moderately smaller than the peak LR, and (2) replacing LR decay with model averaging, i.e., computing a weighted average of the final few checkpoints. By combining these strategies, we improve the average score on a suite of standard benchmarks by 1.64% over random shuffling, without additional data refinement. Validated on 1.5B-parameter models trained over 30B tokens with various data-quality metrics, our findings call for a re-evaluation of curriculum-based LLM pretraining and underscore the potential of co-designing data curricula with optimization methods.

## One-Sentence Claim

Curriculum-based LLM pretraining underuses late high-quality data when paired with standard learning-rate decay, but moderate decay and checkpoint averaging recover curriculum gains.

## Problem

LLM pretraining commonly mixes data of varying quality, and curriculum strategies sort data from lower to higher quality to exploit scarce high-quality examples. Yet reported curriculum gains have often been weak.

The paper identifies an optimization mismatch: high-quality data arrives late, exactly when decaying learning rates reduce the model's ability to learn from it.

## Core Contribution

The paper shows that ascending-quality curriculum training can outperform random shuffling under constant learning rates, but the advantage shrinks under standard decay.

It proposes two simple mitigations: use a more moderate decay schedule and replace aggressive decay with weighted model averaging over final checkpoints.

## Method

The study compares curriculum and random-shuffle pretraining under different learning-rate schedules.

It tests data-quality metrics, moderate final learning rates, and checkpoint/model averaging to decouple late high-quality data exposure from vanishing update magnitudes.

## Experiments and Evidence

The abstract reports experiments on 1.5B-parameter models trained over 30B tokens using multiple data-quality metrics.

Combining moderate decay and model averaging improves average benchmark score by 1.64 percent over random shuffling without additional data refinement.

## Limits and Failure Modes

The result may depend on curriculum ordering, model scale, token budget, data-quality metric, and benchmark choice. More moderate decay can also change stability or final-loss behavior in larger runs.

Because this note is abstract-only, details still need checking: exact schedules, quality metrics, averaging weights, benchmark suite, compute budget, and whether gains persist at larger scales.

## Deep Themes

- Data schedule and optimizer co-design: curriculum order only helps if update magnitudes still let the model learn from late data.
- High-quality data timing: scarce valuable examples can be wasted by conventional decay.
- Checkpoint averaging as curriculum substitute: model averaging captures late-training improvements without tiny final steps.
- Practical pretraining recipes: small schedule changes can unlock gains without new data curation.

## Subthemes

- Curriculum pretraining.
- Learning-rate decay mismatch.
- Model weight averaging.
- Data-quality metrics.

## Connections to Other Papers

This connects to WSM, Train-before-Test, scaling-law papers, and data-curation work through training schedule and model potential.

It also relates to source/data selection themes because both ask when high-quality data actually influences the learned model.

## Notes for Cross-Paper Synthesis

This paper adds a timing-sensitive data theme: data quality is not enough; optimization schedules determine whether the model can still absorb the best examples.
