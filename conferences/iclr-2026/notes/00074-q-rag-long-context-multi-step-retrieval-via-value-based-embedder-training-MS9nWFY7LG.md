# Q-RAG: Long Context Multi‑Step Retrieval via Value‑Based Embedder Training

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: MS9nWFY7LG
- Authors: Artyom Sorokin; Nazar Buzun; Aleksandr Anokhin; Egor KONSTANTINOVICH VEDERNIKOV; Petr Anokhin; Mikhail Burtsev; Evgeny Burnaev
- Primary area: reinforcement learning
- Keywords: Reinforcement Learning;RL;QA;Long-context;RAG;NLP
- Source URL: https://openreview.net/forum?id=MS9nWFY7LG
- PDF URL: https://openreview.net/pdf?id=MS9nWFY7LG

## Abstract

Retrieval-Augmented Generation (RAG) methods enhance LLM performance by efficiently filtering relevant context for LLMs, reducing hallucinations and inference cost.
However, most existing RAG methods focus on single-step retrieval, which is often insufficient for answering complex questions that require multi-step search.
Recently, multi-step retrieval approaches have emerged, typically involving the fine-tuning of small LLMs to perform multi-step retrieval.
However, this type of fine-tuning is highly resource-intensive and does not enable the use of larger LLMs.
In this work, we propose Q-RAG, a novel approach that fine-tunes the Embedder model for multi-step retrieval using reinforcement learning (RL).
Q-RAG offers a competitive, resource-efficient alternative to existing multi-step retrieval methods for open-domain question answering and achieves state-of-the-art results on the popular long-context benchmarks Babilong and RULER for contexts up to 10M tokens.

## One-Sentence Claim

Q-RAG trains the embedder with reinforcement learning so retrieval itself becomes a value-guided multi-step policy for long-context question answering.

## Problem

RAG reduces hallucination and cost by selecting relevant context, but most systems retrieve in a single step.

Complex questions often require multi-step search through long contexts. Existing multi-step retrieval methods frequently fine-tune small LLM retrievers, which is resource-intensive and does not directly support larger LLM use.

## Core Contribution

The paper proposes Q-RAG, a resource-efficient multi-step retrieval approach that fine-tunes the embedder rather than a small LLM retrieval policy.

It uses reinforcement learning to train retrieval embeddings around downstream value for open-domain QA and long-context benchmarks.

## Method

Q-RAG frames multi-step retrieval as a value-based learning problem for the embedder. The retriever learns representations that support sequential context selection across multiple steps.

By moving adaptation into the embedder, the approach can pair with large LLM readers while avoiding heavier fine-tuning of a retrieval LLM.

## Experiments and Evidence

The abstract reports state-of-the-art results on Babilong and RULER for contexts up to 10 million tokens.

The claimed advantage is competitive multi-step retrieval with lower resource cost than methods that fine-tune small LLMs for retrieval behavior.

## Limits and Failure Modes

The method may depend on reward design and benchmark-specific retrieval signals. Value-trained embeddings can also overfit to task formats or fail when retrieval requires symbolic constraints, tables, images, or tool calls.

Because this note is abstract-only, details still need checking: RL objective, value target, negative sampling, retriever architecture, long-context indexing setup, and comparison to agentic search methods.

## Deep Themes

- Retrieval as policy: context selection becomes a sequential decision problem.
- Embedder-level adaptation: smaller retrieval components can absorb task-specific search behavior.
- Long-context scaling by selective access: retrieval remains useful even as context windows grow to millions of tokens.
- RL for information access: reinforcement learning is applied to what evidence is surfaced, not only to final generation.

## Subthemes

- Multi-step RAG.
- Value-based embedder training.
- Long-context QA.
- Babilong and RULER.

## Connections to Other Papers

This connects directly to MC-Search and AstaBench through multi-step retrieval and evidence access for agents.

It also relates to EntroKV, ThinKV, and InfoTok because all treat long context as a budget-allocation problem.

## Notes for Cross-Paper Synthesis

Q-RAG adds an important retrieval-side pattern: long-context systems are shifting from bigger windows alone toward learned policies for choosing which evidence enters the model.
