# ICML 2026 Spotlight Batch 031 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 151-155:

- Which Algorithms Can Graph Neural Networks Learn?
- Teaching Models to Teach Themselves: Reasoning at the Edge of Learnability
- When Attributes Disagree: Gradient Conflict in Image Aesthetic Assessment
- Emergent Analogical Reasoning in Transformers
- VGGT-Motion: Motion-Aware Calibration-Free Monocular SLAM for Long-Range Consistency

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 150.

## Emerging Pattern 1: Algorithm Learning Needs Size-Generalization Guarantees

The GNN algorithm-learning paper asks when MPNNs can learn algorithms on small instances and generalize to arbitrary input sizes with worst-case guarantees. It also gives impossibility results and more expressive variants.

This connects to S3GNN, OSM+, and graph-theory papers. The key distinction is between fitting algorithmic examples and learning the algorithmic rule in a way that scales beyond the training distribution.

## Emerging Pattern 2: Self-Improvement Needs Learnable Stepping Stones

SOAR tackles the zero-success regime where RL has too little reward signal. A teacher model generates synthetic problems and is rewarded by actual student improvement on hard tasks. The notable claim is that question structure matters more than solution correctness for unlocking learning.

This connects to TTT-Discover, MaxRL, RGR-GRPO, and LALP. The reasoning-training cluster is increasingly focused on curricula, local steps, and learnability boundaries rather than only final answers.

## Emerging Pattern 3: Subjective Vision Tasks Hide Attribute-Level Gradient Conflict

AGREE shows that image aesthetic assessment blends multiple latent attributes into one score. When different samples depend on different attributes, end-to-end learning can cancel gradients and create systematic bias. Attribute-guided routing separates the optimization paths.

This connects to UniPercept, EEmo-Logic, and VALUEFLOW. Subjective constructs are multidimensional, and optimizing a single scalar without structure can hide conflicting signals.

## Emerging Pattern 4: Analogy Is Being Mechanized Through Geometry

The analogy paper grounds analogical reasoning in relational embedding alignment and functor-like transformations inside Transformers. It uses controlled synthetic tasks and mechanistic analysis to study when analogy emerges.

This connects to compositional generalization, LOES, and SVD interpretability. The corpus repeatedly points to a deep geometry-of-reasoning theme: abstract capabilities become more legible when decomposed into representational alignments and transformations.

## Emerging Pattern 5: Spatial Foundation Models Still Need Motion-Aware Geometry

VGGT-Motion builds calibration-free monocular SLAM around motion-aware submaps, anchor-driven dense Sim(3) registration, and lightweight pose graph optimization. The use of vision foundation models does not remove the need for geometric organization.

This links to SpatioLM, SAW-Bench, DreamDojo, and SVL. Embodied intelligence needs long-range spatial consistency, not just good per-frame perception.

## Cross-Batch Links

- GNN algorithm learning, OC-space, and S3GNN use graph structure to bridge theory and scalable computation.
- SOAR, LALP, ThreadWeaver, and MaxRL all optimize the process by which reasoning improves.
- AGREE, UniPercept, EEmo-Logic, and VALUEFLOW expose hidden dimensions inside subjective judgments.
- Analogical reasoning, compositional vision, LOES, and SVD interpretability all use geometry as a substrate of abstraction.
- VGGT-Motion, SpatioLM, SAW-Bench, and DreamDojo build a spatial/world-model stack for embodied systems.

## Deep Theme Update

Batch 031 is about generalization beyond the observed instance: graph algorithms beyond training size, reasoning beyond zero-success tasks, aesthetics beyond a single score, analogy beyond one domain, and SLAM beyond short local sequences. The papers all ask what structure lets a system carry behavior into a larger or different regime.
