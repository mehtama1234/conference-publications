# ICML 2026 Spotlight Batch 070 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 346-350:

- A Kinetic Energy Perspective of Flow Matching
- Markov Chain Monte Carlo without Evaluating the Target: an Auxiliary Variable Approach
- Tilt Matching for Scalable Sampling and Fine-Tuning
- On the Power of Source Screening for Learning Shared Feature Extractors
- BlitzRank: Principled Zero-shot Ranking Agents with Tournament Graphs

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 345.

## Emerging Pattern 1: Generative Dynamics Are Becoming Diagnosable and Controllable

KPE measures trajectory effort in flow matching and exposes a non-monotonic fidelity-memorization curve. Tilt Matching modifies velocity fields toward reward-tilted targets without reward gradients or trajectory backpropagation.

Both papers treat the generative path as the control surface, not just the endpoint distribution.

## Emerging Pattern 2: Sampling Under Expensive Targets Needs Auxiliary Structure

Auxiliary MCMC avoids direct target evaluation by introducing auxiliary variables in both proposal and acceptance steps. Flow Sampling and Distribution Transformers similarly amortize or restructure expensive probabilistic computation.

The common principle is to preserve the target while replacing direct evaluation with learned, auxiliary, or interpolated structure.

## Emerging Pattern 3: Data Selection Moves Up to the Source Level

Source Screening shows that even among apparently good sources, carefully selected subsets can be minimax optimal for shared subspace estimation. This extends example-level curation into source-level governance.

It connects naturally to federated learning, data markets, and collaborative data valuation.

## Emerging Pattern 4: Ranking Should Reuse All Comparison Information

BlitzRank extracts an induced tournament from each k-wise comparison and uses transitive closure until the top-m is certified. This is another example of evidence efficiency: expensive oracle calls should leave reusable structure.

## Emerging Pattern 5: Memorization Is a Dynamic Risk

KPE's finding that extreme trajectory energy can drive near-copies of training examples links generative quality directly to privacy. This connects to LM Memorization Capacity and Rashomon Trust: useful models can leak when optimization or inference pushes them into high-information regimes.

## Cross-Batch Links

- KPE/KTS connects to Flow Sampling, Tilt Matching, UDM-GRPO, Local Diffusion Composition, and memorization/privacy work.
- Auxiliary MCMC connects to Distribution Transformers, BFTS, Flow Sampling, SRMC, and Bayesian inference papers.
- Tilt Matching connects to UDM-GRPO, TD3B, R2VPO, and reward-guided diffusion/fine-tuning.
- Source Screening connects to MTS Difficulty, HOBIT, MFedPBA, FedPissa, and Bayesian Truthful Valuation.
- BlitzRank connects to ME Ensemble, NAD, finite-test certification, and token-efficient inference control.

## Deep Theme Update

Batch 070 is about extracting more from less: more control from trajectory energy, more valid sampling without target evaluation, more reward guidance without backpropagating through paths, more statistical value from fewer sources, and more ranking certainty from fewer comparison tokens.
