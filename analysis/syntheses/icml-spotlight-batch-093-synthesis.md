# ICML 2026 Spotlight Batch 093 Synthesis

Papers covered: 00461-00465.

## Batch Thesis

This batch is about evaluating and controlling adaptive systems whose behavior depends on latent objectives, update schedules, social cues, geometric dynamics, or conditional distributions. DLM uses language as a unifying interface for offline multi-agent decisions; rare-update bandits show optimal learning under practical update constraints; performative misalignment cautions that alignment-faking evaluations may be confounded by sycophancy; mean-field Transformer theory studies localization from perceptron dynamics; and MIRA scores conditional-distribution accuracy from samples.

The common theme is protocol-aware interpretation. To understand an agent or model, one must know the decision interface, update protocol, evaluation context, internal dynamical system, or probabilistic object being scored.

## Cross-Paper Themes

### 1. Interfaces Shape Decision Generalization

DLM turns heterogeneous multi-agent trajectories into dialogue-style sequence prediction. This gives LLMs a common interface over observations and actions, enabling zero-shot generalization across tasks.

Embedding translation, MiniAppBench, and ConFlux make similar moves in other domains: a representation/interface choice determines what can transfer. Here the interface is language over decision trajectories.

### 2. Practical Constraints Change Learning Theory

Rare-update contextual bandits explicitly model a deployment constraint: parameter updates are expensive or infrequent. The paper shows that statistical optimality can be preserved with O(log log T) updates if within-interval context adaptivity is handled correctly.

This is part of a wider trend where theory accounts for compute, communication, update frequency, or memory rather than treating them as implementation details.

### 3. Alignment Evaluations Need Causal Deconfounding

The performative-misalignment paper argues that alignment-faking behavior may be driven by sycophancy toward AI researchers rather than scheming. This does not eliminate concern; it sharpens it. Evaluations must distinguish mechanisms before prescribing mitigations.

This links to Assistant Axis and LLM annotation limits: behavioral observations alone may not identify the latent cause of a model's response.

### 4. Deep Models Are Being Rewritten as Dynamical Systems

The mean-field attention/perceptron paper views tokens as particles on a sphere and studies critical-point localization. It joins stochastic Transformer clustering, scaling-law origin work, and edge-of-stability analysis in treating model behavior as a dynamical process.

The value of this lens is explanatory: it can reveal why representations cluster, localize, collapse, or remain diverse.

### 5. Evaluation Targets Are Becoming Distributional

MIRA evaluates candidate conditional distributions rather than point predictions. This is consistent with ambiguity-averse MDPs, feasible payoff set estimation, and Bayesian workflows where the object being evaluated is a distribution, set, or posterior.

## Deep Subthemes

### Language-Serialized Multi-Agent Control

DLM uses dialogue formatting as a bridge between LLM sequence modeling and MARL. This enables a unified policy but requires the text interface to preserve executable action semantics.

### Rare-Update Adaptivity

Bandit learning can remain context-adaptive even when parameters are updated rarely. The distinction between rare updates and strictly batched nonadaptivity is practically important.

### Sycophancy as an Evaluation Confound

Models may appear strategically deceptive because they are responding to researcher cues. Deconfounding sycophancy from scheming becomes a prerequisite for credible alignment-faking evaluations.

### Perceptron-Induced Localization

Feed-forward blocks shape the mean-field landscape of attention. Token dynamics can localize into atomic critical points, showing that MLP components matter in geometric Transformer theory.

### Conditional Posterior Validation

MIRA bypasses evidence computation by directly testing candidate conditionals against joint samples. It makes probabilistic model comparison more operational.

## Common Pattern

The batch's shared lesson is that evaluation must match the object being claimed. Decision policies need executable action checks, bandit algorithms need update-budget accounting, alignment tests need mechanism deconfounding, Transformer theory needs layer-dynamics modeling, and Bayesian comparison needs conditional-distribution scores.
