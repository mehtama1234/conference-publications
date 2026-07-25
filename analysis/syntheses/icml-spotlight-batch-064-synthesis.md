# ICML 2026 Spotlight Batch 064 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 316-320:

- Do LLMs Signal When They’re Right? Evidence from Neuron Agreement
- Incremental BPE Tokenization
- Distributional Inverse Reinforcement Learning
- daVinci-Dev: Agent-native Mid-training for Software Engineering
- Agent0-VL: Exploring Self-Evolving Agent for Tool-Integrated Vision-Language Reasoning

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 315.

## Emerging Pattern 1: Internal Process Signals Can Replace External Self-Judgment

NAD uses activation sparsity and neuron agreement to select correct reasoning samples, avoiding poorly calibrated textual self-evaluation. Agent0-VL similarly grounds verification in tool evidence rather than pure text critique.

The shared point is that reliable reasoning systems need evidence channels beyond their own fluent explanations.

## Emerging Pattern 2: Streaming Systems Need Prefix-Native Algorithms

Incremental BPE maintains exact tokenization for every prefix and emits tokens when boundaries become fixed. This is infrastructure-level work, but it matters directly for low-latency LLM systems.

Together with WeDLM, ME Ensemble, and FlashOptim, it shows the efficiency frontier includes preprocessing and decoding mechanics, not just model kernels.

## Emerging Pattern 3: Risk Sensitivity Is Entering Imitation and Behavior Analysis

Distributional IRL recovers reward distributions and distribution-aware policies by minimizing stochastic-dominance violations and integrating distortion risk measures. This connects to ROCP, TRECA, BFTS, and PAVE, where uncertainty and risk are part of the decision rule.

## Emerging Pattern 4: Agent Training Data Must Be Native to Agent Deployment

daVinci-Dev argues software agents need contextually and environmentally native mid-training trajectories: full information flow, tool calls, and test executions. Static corpora do not expose the actual deployment distribution.

This reinforces the process-data trend from TerminalTraj and Scientific Annotation BC.

## Emerging Pattern 5: Self-Improvement Needs Grounded Verification Loops

Agent0-VL unifies solver and verifier roles with tool-grounded self-rewards. The crucial difference from earlier self-rewarding approaches is that visual claims can be checked through tools and structured critique.

## Cross-Batch Links

- NAD connects to Neuron-Basis Circuits, MDA, BrokenMath, CausalGame, and WZ-LLM through correctness diagnostics and verification.
- Incremental BPE connects to WeDLM, ME Ensemble, FlashOptim, and deployment-focused inference work.
- Distributional IRL connects to TimeRewarder, BFTS, TRECA, ROCP, and risk-aware RL/decision papers.
- daVinci-Dev connects to TerminalTraj, TG-RAG, Scientific Annotation BC, and Pre/Mid/RL Reasoning through agent-native curricula.
- Agent0-VL connects to TG-RAG, tau2-bench, DLMR, WETR, CausalGame, and WZ-LLM through tool-grounded reasoning and evaluation.

## Deep Theme Update

Batch 064 is about process fidelity: use internal activations rather than self-reports, tokenize streams incrementally, infer reward distributions rather than means, train code agents on real tool trajectories, and make LVLM self-improvement depend on grounded verification.
