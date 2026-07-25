# When to Trust the Cheap Check: Weak and Strong Verification for Reasoning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: dfN4HMZbc9
- Authors: Shayan Kiyani; Sima Noorani; George J. Pappas; Hamed Hassani
- Primary area: theory
- Keywords: Reasoning;trustworthy verification;test-time compute;human verification;verification;Latency in reasoning;inference-time scaling;reliable reasoning
- Source URL: https://openreview.net/forum?id=dfN4HMZbc9
- PDF URL: https://openreview.net/pdf?id=dfN4HMZbc9

## Abstract

Reasoning with LLMs increasingly unfolds inside a broader verification loop. Internally, systems use cheap checks, such as self-consistency or proxy rewards, which we call **weak verification**. Externally, users inspect outputs and steer the model through feedback until results are trustworthy, which we call **strong verification**. These signals differ sharply in cost and reliability: strong verification can establish trust but is resource-intensive, while weak verification is fast and scalable but noisy and imperfect. We formalize this tension through **weak-strong verification policies**, which decide when to accept or reject based on weak verification and when to defer to strong verification. We introduce metrics capturing incorrect acceptance, incorrect rejection, and strong-verification frequency. Over population, we show that optimal policies admit a two-threshold structure and that **calibration** and **sharpness** govern the value of weak verifiers. Building on this, we develop an online algorithm that provably controls acceptance and rejection errors without assumptions on the query stream, the language model, or the weak verifier. Experiments on mathematical reasoning and sequential decision-making demonstrate that our algorithm achieves reliability comparable to exhaustive strong verification while significantly reducing verification cost.

## One-Sentence Claim

Weak verifiers can safely reduce expensive human or strong verification when their scores are calibrated and sharp, and when acceptance is governed by online error-control policies.

## Problem

LLM reasoning systems increasingly use two kinds of verification: cheap internal checks that scale across many samples, and expensive strong checks that actually establish trust. The operational question is not whether weak checks are perfect, but when they are good enough to accept, reject, or escalate.

The paper formalizes this decision boundary for reasoning workflows where incorrect acceptance, incorrect rejection, and strong-verification cost are all important.

## Core Contribution

The core contribution is a weak-strong verification framework with metrics for false acceptance, false rejection, and strong-verification frequency. The analysis shows that optimal policies have a two-threshold form: low weak-verifier scores reject, high scores accept, and ambiguous scores defer to strong verification.

It also identifies calibration and sharpness as the key weak-verifier properties. Calibration makes weak scores meaningful as probabilities; sharpness makes them operationally useful by pushing cases away from the uncertain middle.

## Method

The method treats weak verification as a noisy scalar signal and strong verification as a costly reliable oracle. A policy chooses among accept, reject, and defer. Population-level analysis derives the two-threshold structure, while the online algorithm controls acceptance and rejection errors without assuming a fixed query distribution, model behavior, or verifier behavior.

This makes the verification loop closer to conformal-style or online risk-control systems than to ordinary benchmark scoring.

## Experiments and Evidence

Evidence reported in the abstract:

- Mathematical reasoning and sequential decision-making experiments.
- Reliability comparable to exhaustive strong verification.
- Substantially reduced strong-verification cost.
- Online guarantees without assumptions on the query stream, language model, or weak verifier.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: exact error-control guarantees, threshold update rule, baseline verifiers, and measured cost reductions.

## Limits and Failure Modes

- A weak verifier that is poorly calibrated and unsharp may have little value beyond triage.
- Strong verification is treated as the trust anchor; if the strong verifier is itself fallible or inconsistent, the guarantees may need adjustment.
- The framework may be sensitive to distribution shifts that alter weak-verifier calibration.
- Human-facing use needs careful handling of incorrect rejection, not only unsafe acceptance.

## Deep Themes

**Verification is becoming an allocation problem.** The central resource is not just compute, but scarce reliable judgment.

**Cheap signals need operational calibration.** A weak checker matters only if its uncertainty can be converted into decisions.

**Reasoning reliability can be controlled online.** The paper fits a broader pattern where test-time systems maintain guarantees under unknown query streams.

## Subthemes

- Weak versus strong verification.
- Two-threshold acceptance policies.
- Calibration and sharpness of verifiers.
- Online control of reasoning errors.
- Cost-aware trust in reasoning systems.

## Connections to Other Papers

Connects to BlitzRank, Finite Test Certification, Monitoring Monitorability, NAD, VenusBench-Mobile, and Token Overcharging. All ask how limited oversight, tests, or comparison signals can be converted into reliable decisions.

## Notes for Cross-Paper Synthesis

This is a clean abstraction for many 2026 agent papers: weak checks are abundant, strong checks are scarce, and the main design problem is deciding when cheap evidence is trustworthy enough to act on.
