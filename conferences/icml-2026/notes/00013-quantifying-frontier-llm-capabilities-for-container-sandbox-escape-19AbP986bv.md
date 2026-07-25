# Quantifying Frontier LLM Capabilities for Container Sandbox Escape

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 19AbP986bv
- Authors: Rahul Marchand; Art O Cathain; Jerome Wynne; Philippos Maximos Giavridis; Sam Deverett; John Wilkinson; Jason Gwartz; Harry Coppock
- Primary area: general_machine_learning->evaluation
- Keywords: agentic systems;container security;sandbox escape;cybersecurity evaluation;benchmarking
- Source URL: https://openreview.net/forum?id=19AbP986bv
- PDF URL: https://openreview.net/pdf?id=19AbP986bv

## Abstract

Large language models (LLMs) increasingly act as autonomous agents, using tools to execute code, read and write files, and access networks, creating novel security risks. To mitigate these risks, agents are commonly deployed and evaluated in isolated "sandbox" environments, often implemented using Docker/OCI containers. We introduce SandboxEscapeBench, an open benchmark that safely measures an LLM's capacity to break out of these sandboxes. The benchmark is implemented as an Inspect AI Capture the Flag (CTF) evaluation utilising a nested sandbox architecture with the outer layer containing the flag and no known vulnerabilities. Following a threat model of a motivated adversarial agent with shell access inside a container, SandboxEscapeBench covers a spectrum of sandbox-escape mechanisms spanning misconfiguration, privilege allocation mistakes, kernel flaws, and runtime/orchestration weaknesses. We find that, when vulnerabilities are added, LLMs are able to identify and exploit them, showing that use of evaluation like SandboxEscapeBench is needed to ensure sandboxing continues to provide the encapsulation needed for highly-capable models.

## One-Sentence Claim

SandboxEscapeBench evaluates whether frontier LLM agents can exploit container sandbox weaknesses, showing that sandboxing must be tested as model capabilities grow.

## Problem

LLM agents increasingly execute code and access tools in containerized sandboxes, but those sandboxes may fail under adversarially capable agents exploiting misconfiguration, privileges, kernels, or runtimes.

## Core Contribution

The paper introduces SandboxEscapeBench, an Inspect AI CTF benchmark using nested sandboxes to safely measure LLM sandbox-escape capability.

## Method

The benchmark places an agent with shell access inside an inner container, while an outer layer contains the flag and no known vulnerabilities. Tasks cover escape mechanisms spanning misconfiguration, privilege mistakes, kernel flaws, and runtime/orchestration weaknesses.

## Experiments and Evidence

The abstract reports that when vulnerabilities are added, LLMs can identify and exploit them, motivating evaluations like SandboxEscapeBench to validate sandboxing for capable models.

## Limits and Failure Modes

Full-text checks needed: vulnerability set realism, model/tool configurations, containment safety, whether no-known-vulnerability cases remain unsolved, and how benchmark results map to production agent isolation.

## Deep Themes

- Agent safety depends on infrastructure assumptions.
- Sandboxes are not static guarantees; they need capability-aware evaluation.
- Cybersecurity evaluation is moving toward live exploitation tasks.

## Subthemes

- Sandbox escape.
- Container security.
- CTF-style evaluation.
- Agentic cybersecurity.
- Tool-using LLM risk.

## Connections to Other Papers

Connects directly to CyberGym as another executable cybersecurity benchmark, and to safety/alignment papers that treat agent capabilities as operational risk.

## Notes for Cross-Paper Synthesis

This reinforces that AI safety for agents is partly systems security. Evaluating the model alone is insufficient if the execution boundary can be crossed.

## Full-Text Upgrade

Source used: `conferences/icml-2026/text/00013-quantifying-frontier-llm-capabilities-for-container-sandbox-escape-19AbP986bv-arxiv.txt`.

Additional verified details:

- The benchmark uses a sandbox-within-a-sandbox architecture: Inspect orchestrates VM sandboxes, each running a container where the model executes bash commands.
- Success requires escaping the inner container and reading `/flag.txt` on the host filesystem.
- The attacker model assumes root privileges inside the container and prior knowledge that escape is the objective, but not knowledge of the specific vulnerability.
- The benchmark covers 18 public escape tasks across layers including misconfiguration, privileges/capabilities, runtime/orchestration, and host/kernel issues.
- The full text reports that models discovered four unintended escape paths during benchmark development, underscoring the difficulty of safely designing escape evaluations.
- Vulnerability hints improve performance for some frontier models, suggesting that high-level vulnerability knowledge is a bottleneck distinct from exploitation execution.

Refined limits:

- The threat model excludes side channels, hypervisor escapes, and social engineering.
- The bounded vulnerability set makes the benchmark controlled but not exhaustive over all sandbox escape risk.
