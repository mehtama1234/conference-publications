# ICLR Poster Batch 004 Synthesis

## Papers Covered

- ATLAS: Adaptive Transfer Scaling Laws for Multilingual Pretraining, Finetuning, and Decoding the Curse of Multilinguality
- Larger Datasets Can Be Repeated More: A Theoretical Analysis of Multi-Epoch Scaling in Linear Regression
- DR-Submodular Maximization with Stochastic Biased Gradients: Classical and Quantum Gradient Algorithms
- Hybrid Reinforcement: when reward is sparse, better to be dense
- Semantic-Aware Diffusion LLM Inference With Adaptive Block Size

## Shared Thesis

This batch is about replacing fixed assumptions with adaptive laws. ATLAS models multilingual scaling through transfer matrices and compute crossover points. Multi-epoch scaling theory quantifies when repeated data is equivalent to fresh data. Biased-gradient DR-submodular optimization accounts for realistic gradient oracles and structured constraints. HERO combines sparse verifiers with dense reward models instead of choosing one reward source. AdaBlock-dLLM adjusts diffusion decoding blocks using confidence dynamics. Across the batch, the central move is to make policies, schedules, or guarantees responsive to the actual structure of data, language, rewards, gradients, and confidence.

## Deep Themes

### Scaling Laws With Structure

ATLAS and the multi-epoch scaling paper both refine scaling-law thinking. ATLAS adds language-transfer structure to multilingual scaling; the data-reuse paper adds epoch count, dataset size, and distribution to effective sample scaling. Both argue that scale is not a single-axis phenomenon.

### Hybrid Signals and Realistic Oracles

HERO and the biased-gradient optimization paper both treat imperfect feedback as the normal case. HERO combines verifier reliability with reward-model nuance. The DR-submodular work extends guarantees to biased stochastic gradients. The shared lesson is that useful methods model the imperfections in their supervision or oracle.

### Adaptive Test-Time and Training-Time Scheduling

AdaBlock-dLLM and the multi-epoch scaling paper both ask how much to process before moving on. One adapts block boundaries during decoding; the other characterizes when extra passes over data retain value. The broader pattern is scheduling based on measured dynamics rather than fixed recipe.

## Cross-Paper Pattern

The cross-paper pattern is calibrated adaptivity. Language transfer, data reuse, biased gradients, hybrid rewards, and diffusion confidence all require calibration because the naive assumption is wrong: languages are not exchangeable, epochs are not always redundant, gradients are not unbiased, rewards are not simply sparse or dense, and block sizes should not be fixed.

## Subthemes to Track

- Multilingual transfer scaling.
- Effective data reuse.
- Biased-gradient optimization.
- Hybrid verifier/reward-model RL.
- Semantic-aware diffusion decoding.
- Calibration of training and inference policies.

## Confidence and Source Depth

These notes are based on abstracts and local metadata. Full-paper upgrades should inspect scaling-law fits, theoretical assumptions, oracle models, reward normalization, decoding confidence calibration, and benchmark coverage.
