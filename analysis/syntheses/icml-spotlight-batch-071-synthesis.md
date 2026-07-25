# ICML 2026 Spotlight Batch 071 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 351-355:

- When to Trust the Cheap Check: Weak and Strong Verification for Reasoning
- Strategic Navigation or Stochastic Search? How Agents and Humans Reason Over Document Collections
- Bad Seeing or Bad Thinking? Rewarding Perception for Multimodal Reasoning
- PACT: Self-Evolving Physical Safety Alignment for Diffusion Policies in Embodied Manipulation
- Manifold-Optimal Guidance: A Unified Riemannian Control View of Diffusion Guidance

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 350.

## Emerging Pattern 1: Verification Is Becoming an Allocation Policy

Weak-Strong Verification formalizes when cheap checks are enough and when strong verification must be invoked. MADQA evaluates whether document agents spend effort strategically or waste it in brute-force loops.

The shared move is to treat verification and search effort as scarce resources. Accuracy alone is insufficient; systems need policies that decide where high-quality judgment or extra computation is worth spending.

## Emerging Pattern 2: Agent Benchmarks Are Moving From Answers to Process

MADQA measures the accuracy-effort frontier, human-agent overlap, oracle gaps, and looping behavior. MoCA separates perception failures from reasoning failures. Weak-Strong Verification separately tracks incorrect acceptance, incorrect rejection, and strong-verification frequency.

Across the batch, evaluation becomes diagnostic rather than scalar. The important question is not only "did it work?" but "which subsystem made it work or fail, and at what cost?"

## Emerging Pattern 3: Credit Assignment Is the Alignment Bottleneck

MoCA asks whether multimodal errors come from bad seeing or bad thinking. Weak-Strong Verification asks whether weak verifier scores justify accept, reject, or escalation. PACT asks how constraint gradients can be assigned across diffusion timesteps without demonstrations or rewards.

This suggests a common alignment pattern: progress comes from localizing blame and supervision inside the process rather than rewarding final outputs as a whole.

## Emerging Pattern 4: Generative Models Are Controlled Through Their Trajectories

PACT aligns diffusion policies by distilling constraint gradients across timesteps. MOG reformulates diffusion guidance as local Riemannian control that keeps samples near the data manifold.

Together with KPE/KTS and Tilt Matching, these papers show a strong ICML 2026 generative-model theme: sampling and denoising trajectories are no longer implementation details; they are where safety, fidelity, and controllability are imposed.

## Emerging Pattern 5: Geometry Explains Failure Modes

MOG explains guidance artifacts as off-manifold drift. PACT views unsafe robot behavior as trajectory infeasibility. MoCA decomposes multimodal generation into interleaved perceptual and reasoning states.

The broad pattern is geometric or structural diagnosis of model failure: collapse, unsafe actions, and reasoning errors are framed as movement through the wrong region of a latent, physical, or cognitive state space.

## Cross-Batch Links

- Weak-Strong Verification connects to Finite Test Certification, Monitoring Monitorability, NAD, BlitzRank, and Token Overcharging.
- MADQA connects to VenusBench-Mobile, daVinci-Dev, Agent0-VL, and process-oriented agent evaluation.
- MoCA connects to Agent0-VL, Real-Time Visual Attribution, UniMapping, and VenusBench-Mobile.
- PACT connects to NeuronCtrl, Tilt Matching, KPE/KTS, and safe generative control.
- MOG connects to KPE/KTS, Tilt Matching, Flow Sampling, Local Diffusion Composition, and Dimension-Free Diffusion Sampling.

## Deep Theme Update

Batch 071 emphasizes process localization: trust depends on knowing which verifier to use, agent competence depends on how search unfolds, multimodal learning depends on whether perception or reasoning deserves credit, and diffusion control depends on where trajectories leave safe or high-density manifolds.
