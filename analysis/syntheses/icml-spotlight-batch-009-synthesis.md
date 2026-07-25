# ICML 2026 Spotlight Batch 009 Synthesis

Scope: ICML spotlight notes 41-45.

Source depth: full extracted arXiv text for Skill Neologisms, Controlled LLM Training on Spectral Sphere, and To Grok Grokking; abstract/metadata only for What Preferences Can and Cannot Predict and Ranking Time Series because no confident local PDF match is available yet.

## Papers Covered

- Skill Neologisms: Towards Skill-based Continual Learning.
- What Preferences Can-and Cannot-Predict in Multi-Agent Online Learning.
- Controlled LLM Training on Spectral Sphere.
- To Grok Grokking: Provable Grokking in Ridge Regression.
- Ranking Time Series using a Time Warping Ideal Point Model.

## Emerging Pattern 1: Small Interfaces Can Control Large Models

Skill Neologisms proposes trainable vocabulary tokens that add procedural skills to frozen LLMs. Controlled LLM Training on Spectral Sphere controls large-scale pretraining through module-wise spectral constraints on weights and updates. Both papers show that small, carefully placed interfaces can reshape capability or stability without broad architectural replacement.

The common design principle is targeted control: add or constrain the narrow object through which the larger system organizes behavior.

## Emerging Pattern 2: Spectral Geometry Is Becoming an Optimization Primitive

The spectral-sphere paper moves spectra from analysis to optimizer design. Earlier batches used spectra to explain attention generalization, Jacobian low-rank structure, Hessian-guided sample selection, and target-kernel alignment. Here, the spectral norm defines the training manifold itself.

This completes a useful arc: spectra are diagnostics, theoretical complexity measures, data-selection guides, and now direct optimization constraints.

## Emerging Pattern 3: Dynamics Can Defeat Static Descriptions

What Preferences Can and Cannot Predict shows that ordinal preference structure does not always predict the dynamics of no-regret learning. To Grok Grokking shows that a model can overfit early but generalize much later under the same training run. Ranking Time Series argues that static absolute annotations may be less reliable than relative comparisons.

Across these papers, static summaries are not enough. Preferences, train error, and labels must be understood through dynamics, trajectories, or comparative structure.

## Emerging Pattern 4: Generalization Surprises Can Be Made Quantitative

To Grok Grokking gives rigorous bounds on grokking time in ridge regression. This reframes grokking from a mysterious deep-learning phenomenon into a controllable regularized optimization dynamic. It connects directly to the growing set of solvable models in this corpus: attention spectra, Jacobian spectra, learned-kernel ESD, and formal language generation limits.

The deeper theme is demystification: surprising neural phenomena are being pulled into classical or semi-classical settings where parameters and delays can be calculated.

## Emerging Pattern 5: Noisy Human Signals Need Better Elicitation Formats

Ranking Time Series replaces low-agreement individual labels with pairwise comparisons. Pressure Reveals Character uses multi-turn scenario judgments with human-calibrated LLM judges. CounselBench and ClinTutor-R1 build richer expert or educational evaluation structures.

The common pattern is that human supervision and evaluation are being redesigned around the shape of human judgment, not forced into the easiest supervised-learning label format.

## Cross-Batch Links

- Skill Neologisms links with CompSLOT and continual-learning work through modular extension without forgetting.
- What Preferences Can and Cannot Predict links with Unsupervised Partner Design and agent interaction papers through multi-agent learning dynamics.
- Spectral Sphere links with attention spectra, Jacobian spectra, DiReCT, and effective span dimension as the strongest spectral-control cluster so far.
- To Grok Grokking links with other theory papers that explain surprising training dynamics through solvable models.
- Ranking Time Series links with Pressure Reveals Character, CounselBench, and robust annotation/evaluation work.

## Subthemes to Track

- Vocabulary-level skill adapters.
- Zero-shot skill composition.
- Preference graphs versus payoff dynamics.
- Leaklessness and stability.
- Spectral-sphere optimization.
- muP-aligned activation control.
- Provable grokking time.
- Weight-decay-driven delayed generalization.
- Pairwise time-series ranking.
- Robust annotation under subjective criteria.
