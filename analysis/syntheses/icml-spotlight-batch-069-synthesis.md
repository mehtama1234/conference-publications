# ICML 2026 Spotlight Batch 069 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 341-345:

- FlashSketch: Sketch-Kernel Co-Design for Fast Sparse Sketching on GPUs
- Certifying Capabilities from Finite Tests: When Is It Possible?
- Learning Credal Ensembles via Distributionally Robust Optimization
- VenusBench-Mobile: A Challenging and User-Centric Benchmark for Mobile GUI Agents with Capability Diagnostics
- Information dynamics and Memory in Neural Networks through Fisher Information Diffusion

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 340.

## Emerging Pattern 1: Algorithms Are Being Redesigned Around Accelerator Geometry

FlashSketch chooses sparse sketch structure to fit CUDA memory access while retaining OSE guarantees. This continues the FlashSinkhorn/MACKO/WBMM line: mathematical primitives are being reshaped so their sparsity or reduction pattern maps to accelerator hardware.

## Emerging Pattern 2: Evaluation Claims Need Formal Scope Conditions

Finite Test Certification provides a theory for when finite tests can certify broad capabilities. Stochastic multi-environment claims can be certified under overlap and chi-square-radius conditions; worst-case rule-like claims generally cannot.

This gives a principled language for interpreting CausalGame, BrokenMath, VenusBench-Mobile, and monitorability benchmarks.

## Emerging Pattern 3: Uncertainty Should Reflect Distribution Shift, Not Training Noise

CreDRO builds credal ensembles through DRO relaxations of the i.i.d. assumption. The resulting epistemic uncertainty reflects plausible train-test shifts, not just random initialization disagreement.

This deepens the uncertainty theme from ROCP, TRECA, BFTS, and Distribution Transformers.

## Emerging Pattern 4: Realistic Agent Benchmarks Need Capability Diagnostics

VenusBench-Mobile shows mobile GUI agents fail under user-centric tasks and environment variations, with perception and memory dominating failures. It reinforces the move from aggregate success metrics to diagnostic annotations.

## Emerging Pattern 5: Memory Is Information Diffusion Through Dynamics

Fisher Memory Dynamics models recurrent memory as Fisher information propagation through stable subspaces. It shows criticality alone is insufficient; input-output structure must align with stable dynamics.

This adds a theoretical counterpart to empirical memory-routing and long-context papers.

## Cross-Batch Links

- FlashSketch connects to FlashSinkhorn, MACKO-SpMV, FlashOptim, and MDA/GraSS data attribution.
- Finite Test Certification connects to CausalGame, BrokenMath, HypoSpace, Monitoring Monitorability, and VenusBench-Mobile.
- CreDRO connects to Bulk-Calibrated Credal Sets, ROCP, TRECA, Distribution Transformers, and DISCO.
- VenusBench-Mobile connects to tau2-bench, TerminalTraj, TG-RAG, DLMR, and mobile/agent diagnostics.
- Fisher Memory Dynamics connects to DLMR, FacRNN, AI Engram, Neural Ricci Flow, and long-context memory papers.

## Deep Theme Update

Batch 069 is about matching evidence to claims: sparse sketch evidence must survive GPU implementation, finite tests certify only under explicit assumptions, credal uncertainty should reflect real shift, GUI-agent benchmarks need diagnostic realism, and memory claims should be grounded in information propagation dynamics.
