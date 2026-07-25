# RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: yWwrgcBoK3
- Authors: Zeyi Liao; Jaylen Jones; Linxi Jiang; Yuting Ning; Eric Fosler-Lussier; Yu Su; Zhiqiang Lin; Huan Sun
- Primary area: alignment, fairness, safety, privacy, and societal considerations
- Keywords: Computer-Use Agents;Adversarial Risks;Sandbox;Benchmark
- Source URL: https://openreview.net/forum?id=yWwrgcBoK3
- PDF URL: https://openreview.net/pdf?id=yWwrgcBoK3

## Abstract

Computer-use agents (CUAs) promise to automate complex tasks across operating systems (OS) and the web, but remain vulnerable to indirect prompt injection, where attackers embed malicious content into the environment to hijack agent behavior. Current evaluations of this threat either lack support for adversarial testing in realistic but controlled environments or ignore hybrid web-OS attack scenarios involving both interfaces. To address this, we propose RedTeamCUA, an adversarial testing framework featuring a novel hybrid sandbox that integrates a VM-based OS environment with Docker-based web platforms. Our sandbox supports key features tailored for red teaming, such as flexible adversarial scenario configuration, and a setting that decouples adversarial evaluation from navigational limitations of CUAs by initializing tests directly at the point of an adversarial injection. Using RedTeamCUA, we develop RTC-Bench, a comprehensive benchmark with 864 examples that investigate realistic, hybrid web-OS attack scenarios and fundamental security vulnerabilities. Benchmarking current frontier CUAs identifies significant vulnerabilities: Claude 3.7 Sonnet | CUA demonstrates an Attack Success Rate (ASR) of 42.9%, while Operator, the most secure CUA evaluated, still exhibits an ASR of 7.6%. Notably, CUAs often attempt to execute adversarial tasks with an Attempt Rate as high as 92.5%, although failing to complete them due to capability limitations. Nevertheless, we observe concerning ASRs of up to 50% in realistic end-to-end settings, indicating that CUA threats can already result in tangible risks to users and computer systems. Overall, RedTeamCUA provides an essential framework for advancing realistic, controlled, and systematic analysis of CUA vulnerabilities, highlighting the urgent need for robust defenses to indirect prompt injection prior to real-world deployment.

## One-Sentence Claim

RedTeamCUA provides a realistic hybrid web-OS sandbox and benchmark for adversarially testing computer-use agents against indirect prompt injection and related security failures.

## Problem

Computer-use agents operate across web pages and operating-system interfaces, so malicious instructions can be embedded in the environment and hijack behavior. Existing evaluations either lack realistic controlled environments or miss hybrid web-OS attacks where threats move across interface boundaries.

## Core Contribution

The paper contributes RedTeamCUA, an adversarial testing framework with a VM-based OS environment integrated with Docker-based web platforms, plus RTC-Bench, an 864-example benchmark covering realistic hybrid attack scenarios and fundamental CUA vulnerabilities.

## Method

RedTeamCUA uses a hybrid sandbox designed for red teaming. It supports flexible adversarial scenario configuration and can initialize tests directly at the adversarial injection point, separating vulnerability evaluation from an agent's ability to navigate to the threat.

## Experiments and Evidence

The abstract reports substantial vulnerabilities in frontier CUAs: Claude 3.7 Sonnet | CUA reaches 42.9% attack success rate, Operator has 7.6% ASR as the most secure evaluated CUA, and agents attempt adversarial tasks at rates up to 92.5%. End-to-end settings show ASRs up to 50%.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect sandbox reproducibility, model versions, attack taxonomy, whether direct injection initialization inflates or isolates risk, and how capability failures interact with security failures. Reported ASRs may change quickly as CUA products update.

## Deep Themes

- Realistic adversarial evaluation for computer-use agents.
- Indirect prompt injection in hybrid interfaces.
- Controlled sandboxing for red-team benchmarks.
- Separation of navigation ability from security compliance.

## Subthemes

- RTC-Bench.
- VM and Docker hybrid environments.
- Attack success rate.
- Attempt rate.
- Web-OS attack scenarios.

## Connections to Other Papers

Connects to ScaleCUA through computer-use agent infrastructure, to Semantic Watermark Fingerprints and WIMHF through deployment safety, and to WoW! through closed-loop evaluation where agent actions interact with environment state.

## Notes for Cross-Paper Synthesis

RedTeamCUA completes the agent infrastructure picture started by ScaleCUA: scaling data and capability must be paired with adversarial testing. The crucial pattern is that benchmark realism has to include the environment as an attacker, not merely as a task surface.
