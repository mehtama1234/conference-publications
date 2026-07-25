# Shoot First, Ask Questions Later? Building Rational Agents that Explore and Act Like People

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: EQhUvWH78U
- Authors: Gabriel Grand; Valerio Pepe; Joshua B. Tenenbaum; Jacob Andreas
- Primary area: applications to neuroscience & cognitive science
- Keywords: Bayesian experimental design;information-seeking;question asking;Collaborative Battleship;expected information gain (EIG);explore-exploit tradeoffs;resource rationality;probabilistic inference;Monte Carlo sampling;symbolic grounding;code generation;reasoning;decision-oriented dialogue;cognitive modeling;human behavior;language model agents;scientific discovery
- Source URL: https://openreview.net/forum?id=EQhUvWH78U
- PDF URL: https://openreview.net/pdf?id=EQhUvWH78U

## Abstract

Many high-stakes applications of AI require forming data-driven hypotheses and making targeted guesses; e.g., in scientific and diagnostic settings. Given limited resources, to what extent do agents based on language models (LMs) act rationally? We develop methods to benchmark and enhance agentic information-seeking, drawing on insights from human behavior. First, we introduce a strategic decision-oriented dialogue task called *Collaborative Battleship*, in which a partially-informed *Captain* must balance exploration (asking questions) and action (taking shots), while a fully-informed *Spotter* must provide accurate answers under an information bottleneck. Compared to human players (N=42), we find that LM agents struggle to ground answers in context, generate informative questions, and select high-value actions. Next, to address these gaps, we develop novel Monte Carlo inference strategies for LMs based on principles from Bayesian Experimental Design (BED). For Spotter agents, our approach boosts accuracy by up to 14.7% absolute over LM-only baselines; for Captain agents, it raises expected information gain (EIG) by up to 0.227 bits (94.2% of the achievable noise ceiling). Combined, these components yield sharper targeting (+0.303–0.374 F1), and enable weaker LMs, such as Llama-4-Scout, to outperform both humans (8% → 82% win rate) and frontier models (0% → 67% win rate vs. GPT-5) at ≈1% of GPT-5's cost. We replicate these findings on *Guess Who?* where our methods significantly boost accuracy (+28.3–42.4 p.p.), demonstrating their general applicability for building rational information-seeking agents.

## One-Sentence Claim

Bayesian experimental design and Monte Carlo inference can make LM agents ask better questions, ground answers better, and act more rationally under information constraints.

## Problem

High-stakes scientific and diagnostic settings require agents to form hypotheses, ask targeted questions, and make guesses under limited resources.

Language-model agents often struggle with this explore-exploit tradeoff: they ask weak questions, fail to ground answers in context, and choose low-value actions.

## Core Contribution

The paper introduces Collaborative Battleship, a strategic decision-oriented dialogue task with a partially informed Captain and a fully informed Spotter operating under an information bottleneck.

It develops Monte Carlo inference strategies based on Bayesian Experimental Design to improve both answer grounding for Spotters and information-seeking/action selection for Captains.

## Method

Collaborative Battleship evaluates question asking and targeted action under partial information. The Captain balances asking questions and taking shots; the Spotter answers accurately with limited communication.

The proposed methods estimate expected information gain and use Monte Carlo inference to choose better questions/actions and grounded answers.

## Experiments and Evidence

Compared with 42 human players, LM agents struggle on grounding, informative questions, and high-value actions.

The method improves Spotter accuracy by up to 14.7 percentage points, raises Captain expected information gain by up to 0.227 bits, improves targeting F1 by +0.303 to +0.374, and lets Llama-4-Scout outperform humans and GPT-5 in reported win rates at about 1 percent of GPT-5's cost. Results replicate on Guess Who? with +28.3 to +42.4 percentage-point accuracy gains.

## Limits and Failure Modes

Battleship and Guess Who? are structured games; transfer to messy scientific or clinical domains depends on hypothesis space, cost model, and grounding quality.

Because this note is abstract-only, details still need checking: Monte Carlo procedure, EIG estimation, human protocol, noise ceiling, cost accounting, and robustness under misleading Spotter answers.

## Deep Themes

- Rational information seeking: agents need policies for when to ask and when to act.
- Bayesian experimental design for LMs: classic decision theory can scaffold agent behavior.
- Human comparison as diagnostic: people provide a benchmark for resource-rational strategies.
- Cheap models plus inference scaffolds: weaker LMs can outperform stronger ones when wrapped with better decision procedures.

## Subthemes

- Collaborative Battleship.
- Expected information gain.
- Question asking under bottlenecks.
- Monte Carlo agent inference.

## Connections to Other Papers

This connects to Gaia2, GLANCE, MiniAppBench, and agentic RL papers through dynamic decision-making under uncertainty.

It also relates to coverage and test-time scaling because inference-time search/procedure can unlock better behavior from a base model.

## Notes for Cross-Paper Synthesis

This paper adds a resource-rational agent theme: better agents may come from explicit decision procedures around the model, not only larger models.
