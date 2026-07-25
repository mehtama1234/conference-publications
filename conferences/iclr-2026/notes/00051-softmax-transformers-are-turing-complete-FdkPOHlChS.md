# Softmax Transformers are Turing-Complete

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: FdkPOHlChS
- Authors: Hongjian Jiang; Michael Hahn; Georg Zetzsche; Anthony Widjaja Lin
- Primary area: other topics in machine learning (i.e., none of the above)
- Keywords: soft attention;FLaNN;recursively enumerable;Turing-complete;formal languages
- Source URL: https://openreview.net/forum?id=FdkPOHlChS
- PDF URL: https://openreview.net/pdf?id=FdkPOHlChS

## Abstract

Hard attention Chain-of-Thought (CoT) transformers are known to be Turing-complete. However, it is an open problem whether softmax attention Chain-of-Thought (CoT) transformers are Turing-complete. In this paper, we prove a stronger result that length-generalizable softmax CoT transformers are Turing-complete. 

More precisely, our Turing-completeness proof goes via the CoT extension of the Counting RASP (C-RASP), which correspond to softmax CoT transformers that admit length generalization. We prove Turing-completeness for CoT C-RASP with causal masking over a unary alphabet (more generally, for the letter-bounded languages). While we show that this is actually not Turing-complete for arbitrary languages, we prove that its extension with relative positional encoding is Turing-complete for arbitrary languages. We empirically validate our theoretical results by training transformers for various languages that require complex (non-linear) arithmetic reasoning.

## One-Sentence Claim

Length-generalizable softmax chain-of-thought transformers are Turing-complete, with relative positional encoding extending the result from letter-bounded languages to arbitrary languages.

## Problem

Hard-attention CoT transformers are known to be Turing-complete, but the computational power of softmax-attention CoT transformers has remained open.

The difficulty is to prove universality while preserving soft attention and length generalization rather than relying on brittle finite-length constructions.

## Core Contribution

The paper proves Turing-completeness for length-generalizable softmax CoT transformers through a CoT extension of Counting RASP.

It proves CoT C-RASP with causal masking over a unary alphabet, and more generally letter-bounded languages, is Turing-complete in that setting. It also shows the model is not Turing-complete for arbitrary languages unless extended with relative positional encoding, which restores full Turing-completeness.

## Method

The proof routes transformer computation through CoT C-RASP, a formal model corresponding to length-generalizable softmax CoT transformers.

The authors analyze causal masking, unary or letter-bounded inputs, and relative positional encodings to characterize when the construction can simulate arbitrary computation.

## Experiments and Evidence

The abstract reports empirical validation by training transformers on languages requiring complex nonlinear arithmetic reasoning.

The main evidence is theoretical: a formal Turing-completeness proof plus a boundary result showing where the model class is not universal.

## Limits and Failure Modes

Turing-completeness is an expressivity result, not a claim about learnability, efficiency, finite precision at practical scale, or robustness under training.

Because this note is abstract-only, details still need checking: exact C-RASP primitives, positional-encoding assumptions, training experiments, arithmetic-language suite, and resource overhead of the simulation.

## Deep Themes

- Soft attention expressivity: softmax attention can support universal computation under the right CoT and positional structure.
- Length generalization as formal requirement: universality should survive beyond fixed input lengths.
- Positional encoding as computational resource: relative positions change what languages can be represented.
- Expressivity boundaries matter: the paper proves both positive and negative results.

## Subthemes

- Counting RASP.
- Letter-bounded languages.
- Relative positional encoding.
- Nonlinear arithmetic language experiments.

## Connections to Other Papers

This connects to ICLR masked diffusion reasoning, ICML Rational Transductors, transformer accessible sequence bounds, and language-generation complexity barriers.

It also relates to coverage theory because expressivity and probability mass together determine whether downstream search can access useful outputs.

## Notes for Cross-Paper Synthesis

This paper anchors the formal sequence-model expressivity theme: architecture details such as attention type and positional encoding determine not only performance but computational class.
