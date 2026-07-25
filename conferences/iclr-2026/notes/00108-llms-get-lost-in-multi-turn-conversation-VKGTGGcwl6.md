# LLMs Get Lost In Multi-Turn Conversation

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: VKGTGGcwl6
- Authors: Philippe Laban; Hiroaki Hayashi; Yingbo Zhou; Jennifer Neville
- Primary area: datasets and benchmarks
- Keywords: multi-turn;underspecification;llm simulation
- Source URL: https://openreview.net/forum?id=VKGTGGcwl6
- PDF URL: https://openreview.net/pdf?id=VKGTGGcwl6

## Abstract

Large Language Models (LLMs) are conversational interfaces. As such, LLMs have the potential to assist their users not only when they can fully specify the task at hand, but also to help them define, explore, and refine what they need through multi-turn conversational exchange. Although analysis of LLM conversation logs has confirmed that underspecification occurs frequently in user instructions, LLM evaluation has predominantly focused on the single-turn, fully-specified instruction setting. In this work, we perform large-scale simulation experiments to compare LLM performance in single- and multi-turn settings. Our experiments confirm that all the top open- and closed-weight LLMs we test exhibit significantly lower performance in multi-turn conversations than single-turn, with an average drop of 39% across six generation tasks. Analysis of 200,000+ simulated conversations decomposes the performance degradation into two components: a minor loss in aptitude and a significant increase in unreliability. We find that LLMs often make assumptions in early turns and prematurely attempt to generate final solutions, on which they overly rely. In simpler terms, we discover that when LLMs take a wrong turn in a conversation, they get lost and do not recover.

## One-Sentence Claim

LLMs perform substantially worse in multi-turn underspecified conversations because early wrong assumptions create unreliability that models do not recover from.

## Problem

LLMs are used as conversational interfaces where users often underspecify goals and refine them over turns. Most evaluations, however, still focus on single-turn fully specified instructions.

This leaves a gap between benchmark performance and real interaction: a model may solve a task when given all constraints upfront but fail when it must negotiate the task through conversation.

## Core Contribution

The paper performs large-scale simulations comparing single-turn and multi-turn LLM performance across generation tasks.

It decomposes multi-turn degradation into aptitude loss and unreliability, showing that unreliability dominates.

## Method

The study simulates conversations where tasks unfold through multiple turns and compares model outcomes to single-turn versions.

Analysis over more than 200,000 simulated conversations identifies when models make early assumptions, prematurely generate final answers, and then over-rely on those incorrect commitments.

## Experiments and Evidence

The abstract reports tests of top open- and closed-weight LLMs across six generation tasks.

Average performance drops by 39 percent in multi-turn settings. The main failure is not a large loss of base aptitude, but increased unreliability after early conversational mistakes.

## Limits and Failure Modes

Simulation quality matters: synthetic users and task decompositions may not fully match human conversation. The failure taxonomy may also depend on prompts, memory format, and whether models are allowed to ask clarifying questions.

Because this note is abstract-only, details still need checking: six tasks, simulation protocol, model list, metrics, decomposition method, and recovery interventions.

## Deep Themes

- Conversation as stateful control: each turn updates assumptions that can lock in future failures.
- Underspecification handling: real assistants must explore user intent instead of prematurely solving.
- Reliability over aptitude: multi-turn degradation comes from compounding wrong commitments.
- Evaluation gap: single-turn benchmarks overestimate deployed conversational competence.

## Subthemes

- Multi-turn evaluation.
- Underspecified instructions.
- Conversational unreliability.
- Early-assumption lock-in.

## Connections to Other Papers

This connects to SimuHome, AgentFlow, AstaBench, WebDevJudge, and MC-Search through process-level agent evaluation.

It also relates to deception and safety work because unrecovered conversational assumptions can create misleading or unsafe outputs even without adversarial intent.

## Notes for Cross-Paper Synthesis

This paper adds a conversation-process theme: models need mechanisms for revising assumptions over time, not just stronger single-turn generation.
