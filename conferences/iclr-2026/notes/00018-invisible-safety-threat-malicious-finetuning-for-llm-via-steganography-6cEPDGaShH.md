# Invisible Safety Threat: Malicious Finetuning for LLM via Steganography

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 6cEPDGaShH
- Authors: Guangnian Wan; Xinyin Ma; Gongfan Fang; Xinchao Wang
- Primary area: alignment, fairness, safety, privacy, and societal considerations
- Keywords: LLM;finetuning;safety;steganography
- Source URL: https://openreview.net/forum?id=6cEPDGaShH
- PDF URL: https://openreview.net/pdf?id=6cEPDGaShH

## Abstract

Understanding and addressing potential safety alignment risks in large language models (LLMs) is critical for ensuring their safe and trustworthy deployment. In this paper, we highlight an insidious safety threat: a compromised LLM can maintain a facade of proper safety alignment while covertly generating harmful content. To achieve this, we finetune the model to understand and apply a steganographic technique. At inference time, we input a prompt that contains a steganographically embedded malicious target question along with a plaintext cover question. The model, in turn, produces a target response similarly embedded within a benign-looking cover response. In this process, human observers only see the model being prompted with a cover question and generating a corresponding cover response, while the malicious content is hidden from view. We demonstrate this invisible safety threat on GPT-4.1 despite the OpenAI fine-tuning API’s safeguards. The finetuned model produces steganographic malicious outputs in response to hidden malicious prompts, while the user interface displays only a fully benign cover interaction. We also replicate the attack on two open-source models, Phi-4 and Mistral-Small-24B-Base-2501, confirming the generality of our method. We quantitatively evaluate our method on the AdvBench dataset, using Llama-Guard-3-8B for content safety classification. Across all three models, all stegotexts containing malicious content are incorrectly classified as safe.

## One-Sentence Claim

Malicious fine-tuning can teach LLMs to hide unsafe prompts and responses inside benign-looking steganographic text, bypassing human and classifier-facing safety checks.

## Problem

Safety-aligned LLMs may appear benign through normal UI inspection while covertly processing hidden malicious instructions and outputs, creating an invisible alignment failure mode.

## Core Contribution

The paper demonstrates a steganographic malicious fine-tuning attack against GPT-4.1 through the OpenAI fine-tuning API and replicates it on Phi-4 and Mistral-Small-24B-Base-2501.

## Method

The attacker fine-tunes a model to decode malicious target questions embedded in cover prompts and to embed malicious target responses inside benign-looking cover responses. The visible interaction appears safe while the hidden channel carries harmful content.

## Experiments and Evidence

The abstract reports evaluation on AdvBench using Llama-Guard-3-8B, where stegotexts containing malicious content are classified as safe across all three tested models.

## Limits and Failure Modes

PDF checks needed: steganographic capacity, detectability under stronger steganalysis, fine-tuning safeguards tested, and how attack success varies with model/instruction format.

## Deep Themes

- Alignment can fail through hidden communication channels.
- Safety classifiers can be blind to encoded harmful content.
- Fine-tuning access creates a supply-chain style model risk.

## Subthemes

- Malicious fine-tuning.
- Steganography.
- Hidden unsafe prompts.
- Safety classifier evasion.
- Covert channels in LLMs.

## Connections to Other Papers

Connects to SandboxEscapeBench, CyberGym, Catch-22, and watermarking papers. It is a safety/security paper about hidden channels rather than visible model behavior.

## Notes for Cross-Paper Synthesis

This paper deepens the safety theme: surface-level safety evidence can be misleading when model behavior includes hidden encodings, covert channels, or adversarially trained trigger formats.

## Full-Text Upgrade

Source used: `conferences/iclr-2026/text/00018-invisible-safety-threat-malicious-finetuning-for-llm-via-steganography-6cEPDGaShH-arxiv.txt`.

Additional verified details:

- The attack uses invisible-character steganography based on zero-width characters.
- The encoding is quaternary: digits 0-3 map to steganographic characters, with an additional delimiter character for unambiguous decoding.
- Training uses a structure-aligned auxiliary base-4 encoding as a scaffold because the target steganographic character pattern is rare in pretraining data.
- The paper reports effectiveness on GPT-4.1 plus three open-source models: Llama-3.3-70B-Instruct, Phi-4, and Mistral-Small-24B-Base-2501.
- For GPT-4.1, the authors used 4,000 benign target samples and 350 malicious samples paired with benign cover samples; malicious samples contain no explicit harmful plaintext because the payload is encoded.
- Safety evaluation uses AdvBench with Llama Guard across 520 adversarial instructions.
- Across four fine-tuned models, all stegotext prompt-response pairs are classified safe before decoding, while more than 90% are unsafe after decoding; GPT-4.1 decoded interactions are reported as 93.3% unsafe.

Refined limits:

- The attack depends on the model learning a specific encoding and on monitors not decoding or detecting that hidden channel.
- Stronger steganalysis, Unicode normalization, or fine-tuning-data sanitization could change attack success.
