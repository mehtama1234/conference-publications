# VenusBench-Mobile: A Challenging and User-Centric Benchmark for Mobile GUI Agents with Capability Diagnostics

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: coHiGZOFtS
- Authors: Yichen Gong; Zhuohan Cai; Sunhao Dai; Yuqi Zhou; Zhangxuan Gu; Changhua Meng; Shuheng Shen
- Primary area: general_machine_learning->evaluation
- Keywords: GUI Agents;Benchmark
- Source URL: https://openreview.net/forum?id=coHiGZOFtS
- PDF URL: https://openreview.net/pdf?id=coHiGZOFtS

## Abstract

Existing online benchmarks for mobile GUI agents remain largely app-centric and task-homogeneous, failing to reflect the diversity and instability of real-world mobile usage. To this end, we introduce VenusBench-Mobile, a challenging online benchmark for evaluating general-purpose mobile GUI agents under realistic, user-centric conditions. 
VenusBench-Mobile builds two core evaluation pillars: defining what to evaluate via user-intent-driven task design that reflects real mobile usage, and how to evaluate through a capability-oriented annotation scheme for fine-grained agent behavior analysis.
Extensive evaluation of state-of-the-art mobile GUI agents reveals large performance gaps relative to prior benchmarks, indicating that VenusBench-Mobile poses substantially more challenging and realistic tasks and that current agents remain far from reliable real-world deployment.
Diagnostic analysis further shows that failures are dominated by deficiencies in perception and memory, which are largely obscured by coarse-grained evaluations.
Moreover, even the strongest agents exhibit near-zero success under environment variations, highlighting their brittleness in realistic settings.
Based on these insights, we believe VenusBench-Mobile provides an important stepping stone toward robust real-world deployment of mobile GUI agents. Code and data are available at https://github.com/inclusionAI/UI-Venus/tree/VenusBench-Mobile.

## One-Sentence Claim

VenusBench-Mobile evaluates mobile GUI agents under realistic user-centric tasks and shows current agents are brittle, especially in perception, memory, and environment variation.

## Problem

Existing online mobile GUI-agent benchmarks are often app-centric and task-homogeneous. They can miss the diversity, instability, and user-intent complexity of real mobile use.

The paper asks how to evaluate general-purpose mobile GUI agents under conditions that better approximate deployment.

## Core Contribution

The paper introduces VenusBench-Mobile with two evaluation pillars:

- User-intent-driven task design to define what realistic mobile agents should do.
- Capability-oriented annotation for fine-grained behavior diagnostics.

Evaluations show much larger performance gaps than prior benchmarks. Failures are dominated by perception and memory deficiencies, and even the strongest agents have near-zero success under environment variations.

## Method

VenusBench-Mobile constructs online mobile tasks around user intent rather than only app operations. It annotates agent behavior by capability categories so failures can be attributed to perception, memory, or other components.

Environment variations stress whether agents are robust to realistic changes instead of overfitting static task flows.

## Experiments and Evidence

Evidence reported in the abstract:

- Challenging online mobile GUI-agent benchmark.
- User-intent-driven task design.
- Capability-oriented annotation scheme.
- Evaluation of state-of-the-art mobile GUI agents.
- Large gaps relative to prior benchmarks.
- Failures dominated by perception and memory.
- Near-zero success for strongest agents under environment variations.
- Code and data release.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: task count, mobile environment, agent list, variation types, and annotation reliability.

## Limits and Failure Modes

- Online GUI benchmarks can become brittle as apps change.
- User-centric tasks are harder to reproduce exactly.
- Near-zero variation performance may reflect environment tooling constraints as well as model ability.
- Capability annotations need consistent human or automated labeling.

## Deep Themes

**Agent benchmarks must reflect user intent.** Realistic tasks are not just app-specific scripted actions.

**Fine-grained diagnostics reveal hidden failures.** Perception and memory deficits are obscured by aggregate success rates.

**Environment variation is a deployment stress test.** Static benchmarks overestimate mobile-agent reliability.

## Subthemes

- Mobile GUI agents.
- User-intent task design.
- Capability diagnostics.
- Perception and memory failures.
- Environment variation brittleness.

## Connections to Other Papers

Connects to tau2-bench, TerminalTraj, TG-RAG, CausalGame, and Monitoring Monitorability through process-level agent evaluation. It also links to DLMR and memory-routing work because memory failures dominate the diagnostic findings.

## Notes for Cross-Paper Synthesis

VenusBench-Mobile reinforces the benchmark realism trend: credible agent evaluation must include changing environments, user intent, and capability-level failure labels.
