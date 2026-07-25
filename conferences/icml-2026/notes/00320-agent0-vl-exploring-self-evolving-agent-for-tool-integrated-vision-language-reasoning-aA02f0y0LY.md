# Agent0-VL: Exploring Self-Evolving Agent for Tool-Integrated Vision-Language Reasoning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: aA02f0y0LY
- Authors: Jiaqi Liu; Kaiwen Xiong; Peng Xia; Yiyang Zhou; Haonian Ji; Lu Feng; Siwei Han; Mingyu Ding; Huaxiu Yao
- Primary area: deep_learning->foundation_models
- Keywords: Self-Evolving;Vision-Language Model
- Source URL: https://openreview.net/forum?id=aA02f0y0LY
- PDF URL: https://openreview.net/pdf?id=aA02f0y0LY

## Abstract

Large Vision-Language Models (LVLMs) have achieved remarkable progress in multimodal reasoning tasks; however, their learning remains constrained by the limitations of human-annotated supervision. Recent self-rewarding approaches attempt to overcome this constraint by allowing models to act as their own critics or reward providers. Yet, purely text-based self-evaluation struggles to verify complex visual reasoning steps and often suffers from evaluation hallucinations. To address these challenges, inspired by recent advances in tool-integrated reasoning, we propose Agent0-VL, a self-evolving vision-language agent that achieves continual improvement with tool-integrated reasoning. Agent0-VL incorporates tool usage not only into reasoning but also into self-evaluation and self-repair, enabling the model to introspect, verify, and refine its reasoning through evidence-grounded analysis. It unifies two synergistic roles within a single LVLM: a Solver that performs multi-turn tool-integrated reasoning, and a Verifier that generates structured feedback and fine-grained self-rewards through tool-grounded critique. These roles interact through a Self-Evolving Reasoning Cycle, where tool-based verification and reinforcement learning jointly align the reasoning and evaluation distributions for stable self-improvement. Through this zero-external-reward evolution, Agent0-VL aligns its reasoning and verification behaviors without any human annotation or external reward models, achieving continual self-improvement. Experiments on chart reasoning, geometric problem solving, and visual scientific analysis show that Agent0-VL achieves an 12.5% improvement over the Qwen-VL base model.

## One-Sentence Claim

Agent0-VL enables self-evolving visual reasoning by using tools not only for solving but also for verification, critique, self-reward, and repair.

## Problem

LVLMs still depend heavily on human-annotated supervision. Self-rewarding methods try to reduce this dependence, but text-only self-evaluation can hallucinate when visual reasoning steps require verification.

The paper asks how an LVLM can improve itself without human annotations or external reward models while grounding both reasoning and evaluation in tool evidence.

## Core Contribution

The paper introduces Agent0-VL, a self-evolving tool-integrated vision-language agent. It unifies two roles in one LVLM:

- Solver: performs multi-turn tool-integrated reasoning.
- Verifier: generates structured feedback and fine-grained self-rewards through tool-grounded critique.

The Self-Evolving Reasoning Cycle aligns reasoning and evaluation distributions with tool-based verification and reinforcement learning, achieving zero-external-reward continual self-improvement.

## Method

Agent0-VL uses tools during reasoning to gather evidence and during verification to critique intermediate steps. Structured feedback becomes self-reward, and RL updates the model so solver and verifier behavior co-evolve.

Tool grounding is the key safeguard against pure text self-evaluation hallucination.

## Experiments and Evidence

Evidence reported in the abstract:

- Experiments on chart reasoning, geometric problem solving, and visual scientific analysis.
- 12.5 percent improvement over the Qwen-VL base model.
- Tool-integrated reasoning for both solving and verification.
- No human annotations or external reward models during evolution.
- Stable self-improvement by aligning reasoning and evaluation distributions.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: tools used, RL objective, reward validation, benchmark list, and safeguards against self-reward collapse.

## Limits and Failure Modes

- Tool outputs can be wrong, incomplete, or misused.
- Self-reward loops can amplify systematic verifier errors.
- Zero external reward does not remove the need for benchmark validation.
- Results may depend on tool availability and task-specific tool affordances.

## Deep Themes

**Self-improvement needs grounded verification.** The verifier uses tools so critique is tied to evidence, not only language priors.

**Solver and verifier roles are converging.** One LVLM can learn both generation and evaluation behaviors.

**Tools are becoming training infrastructure.** Tool use is not only inference-time augmentation; it supplies self-reward signals.

## Subthemes

- Tool-integrated LVLM reasoning.
- Self-evolving reasoning cycles.
- Solver-verifier role unification.
- Tool-grounded critique.
- Zero-external-reward RL.

## Connections to Other Papers

Connects to TG-RAG, tau2-bench, DLMR, WZ-LLM, CausalGame, and daVinci-Dev through agentic process control and verification. It also links to WETR and DOUBT because visual reasoning reliability depends on evidence-grounded internal or external checks.

## Notes for Cross-Paper Synthesis

Agent0-VL extends the self-improvement theme: reliable autonomy requires verification channels that are grounded in tools or formal checks, not just another language-model judgment.
