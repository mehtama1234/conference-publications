# ICML 2026 Spotlight Batch 099 Synthesis

Papers covered: 00491-00495.

## Batch Thesis

This batch is about measuring the hidden bottlenecks behind model behavior. Hallucination is framed as optimal lossy membership compression; structure learning is reduced to conditional-independence testing; POPGym Arcade exposes memory contamination in partially observable RL; reasoning chains reduce task intrinsic dimensionality; and TokSuite isolates tokenization as a causal design variable.

The common pattern is diagnostic isolation. Each paper takes a broad behavior people talk about loosely, such as hallucination, structure recovery, memory, reasoning, or tokenizer quality, and turns it into a measurable object with controlled assumptions.

## Cross-Paper Themes

### 1. Some Failures Are Capacity-Optimal Under the Wrong Objective

The hallucination paper argues that false positives can be optimal for sparse fact storage under memory limits. The embedding-collapse paper from the previous batch shows that too-small embeddings can force triplet errors. Both make a hard point: compression can produce predictable, even optimal, failures.

This reframes mitigation. If hallucination is partly a storage tradeoff, then retrieval, abstention, and external memory are not patches; they change the resource model.

### 2. Learning Complexity Often Reduces to a Primitive

Structure learning complexity is governed by conditional independence testing. Reasoning-chain effectiveness is linked to intrinsic dimensionality. TokSuite isolates tokenization by holding all other pretraining variables fixed.

Across the batch, big model behaviors are decomposed into smaller primitives that can be measured directly.

### 3. Memory and Reasoning Need Counterfactual Diagnostics

POPGym Arcade uses fully and partially observable variants to study memory use under controlled conditions. The reasoning-chain paper varies task formulation while holding architecture fixed. Both avoid interpreting aggregate success as evidence of a mechanism.

This echoes PIPE's interface rewrites: counterfactual variants are becoming a central evaluation tool.

### 4. Interfaces Shape Model Behavior Before Learning Begins

TokSuite makes tokenization visible as a causal variable. This connects to WIRE graph positions, ConFlux variate patches, and DLM dialogue-formatted decisions. The input representation is part of the model's inductive bias.

## Deep Subthemes

### Rate-Distortion Hallucination

Random facts resemble sparse membership testing. Under limited capacity, an optimal compressor may assign high confidence to some non-facts, producing hallucination-like false positives.

### CI Testing as Structure-Learning Bottleneck

For poly-forests, minimax structure-learning rates are determined by minimax conditional-independence testing rates. Modified PC algorithms can be optimal when tests are tuned correctly.

### RL Memory Contamination

Recurrent policies can smear credit across irrelevant history. OOD events can persist in hidden state and perturb decisions far into the future.

### Reasoning as Dimensionality Reduction

Effective CoT strategies make tasks require fewer model dimensions to reach an accuracy threshold, giving a quantitative mechanism for improved generalization.

### Tokenizer Isolation

TokSuite's matched pretraining runs make tokenizer effects measurable across multilingual perturbations. This is the kind of controlled artifact needed to study preprocessing choices rigorously.

## Common Pattern

The batch's shared lesson is that opaque behavior becomes tractable when the right bottleneck is isolated: memory capacity, CI tests, recurrent state, task dimensionality, or token segmentation. Many "model failures" are better understood as consequences of a hidden interface or compression constraint.
