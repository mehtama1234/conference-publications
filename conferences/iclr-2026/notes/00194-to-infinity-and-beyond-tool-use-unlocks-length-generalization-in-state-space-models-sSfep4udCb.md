# To Infinity and Beyond: Tool-Use Unlocks Length Generalization in State Space Models

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: sSfep4udCb
- Authors: Eran Malach; Omid Saremi; Sinead Williamson; Arwen Bradley; Aryo Lotfi; Emmanuel Abbe; Joshua M. Susskind; Etai Littwin
- Primary area: foundation or frontier models, including LLMs
- Keywords: State Space Models;Mamba;Length Generalization;LLM;Transformers
- Source URL: https://openreview.net/forum?id=sSfep4udCb
- PDF URL: https://openreview.net/pdf?id=sSfep4udCb

## Abstract

State Space Models (SSMs) have become the leading alternative to Transformers for sequence modeling tasks. Their primary advantage is efficiency in long-context and long-form generation, enabled by fixed-size memory and linear scaling of computational complexity. We begin this work by showing a simple theoretical result stating that SSMs cannot accurately solve any long-form generation problem, undermining their main competitive advantage. However, we show that this limitation can be mitigated by allowing SSMs interactive access to external tools. In fact, we show that given the right choice of tool access and problem-dependent training data, SSMs can learn to solve any tractable problem and generalize to arbitrary problem length/complexity (i.e., achieve length generalization). Following our theoretical finding, we demonstrate that tool-augmented SSMs achieve remarkable length generalization on a variety of arithmetic, reasoning, and coding tasks. These findings highlight SSMs as a potential efficient alternative to Transformers in interactive tool-based and agentic settings.

## One-Sentence Claim

SSMs cannot generally solve long-form generation with fixed internal memory alone, but tool access plus suitable training data can unlock arbitrary length generalization for tractable tasks.

## Problem

SSMs are efficient for long contexts because they use fixed-size memory and linear compute, but fixed memory may prevent accurate long-form generation as problem length or complexity grows. This challenges the main advantage claimed for SSMs over Transformers.

## Core Contribution

The paper gives a theoretical limitation result for SSMs on long-form generation, then shows that interactive external tool access can overcome the limitation. It provides theory and experiments demonstrating length generalization in tool-augmented SSMs.

## Method

The framework augments SSMs with problem-appropriate tool calls and training data that teaches when and how to use those tools. With external state or computation delegated to tools, the SSM can solve tractable tasks beyond the limits of fixed internal memory.

## Experiments and Evidence

The abstract reports strong length generalization on arithmetic, reasoning, and coding tasks, along with the theoretical claim that SSMs with the right tool access and training data can learn to solve any tractable problem at arbitrary length or complexity.

## Limits and Failure Modes

Tool access shifts complexity into tool design, interface quality, and training distribution. The theoretical result may depend on idealized tool reliability and task decomposability. Full-text review should check formal model assumptions, tool sets, generalization lengths, comparison to Transformers, and failure cases when tools are noisy or unavailable.

## Deep Themes

- Tool use as external memory for SSMs.
- Length generalization beyond fixed recurrent state.
- Theoretical limits of efficient sequence models.
- Agentic SSM systems.

## Subthemes

- Fixed-memory lower bounds.
- Interactive tool augmentation.
- Arithmetic/reasoning/coding length extrapolation.
- Problem-dependent training data.
- SSMs as efficient agent backbones.

## Connections to Other Papers

Connects to Mamba ICL theory, FlashRNN, MemAgent, LoongRL, and long-context retriever papers through alternatives to pure Transformer context scaling. It also links to tool-use and agent benchmarks where external interaction extends model capability.

## Notes for Cross-Paper Synthesis

This paper reframes SSM length limits as an interface problem: fixed memory is a bottleneck unless the model can externalize state and computation through tools.
