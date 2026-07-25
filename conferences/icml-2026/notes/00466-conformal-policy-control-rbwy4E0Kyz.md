# Conformal Policy Control

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: rbwy4E0Kyz
- Authors: Drew Prinster; Clara Fannjiang; Ji Won Park; Kyunghyun Cho; Anqi Liu; Suchi Saria; Samuel Don Stanton
- Primary area: general_machine_learning
- Keywords: conformal risk control;policy control;conformal prediction;safe policy improvement;ai safety;contextual bandits;model-based-optimization;safe exploration
- Source URL: https://openreview.net/forum?id=rbwy4E0Kyz
- PDF URL: https://openreview.net/pdf?id=rbwy4E0Kyz

## Abstract

An agent must try new behaviors to explore and improve. In high-stakes environments, an agent that violates safety constraints may cause harm and must be taken offline, curtailing any future interaction. Imitating old behavior is safe, but excessive conservatism discourages exploration. How much behavior change is too much? We show how to use any safe reference policy as a probabilistic regulator for any optimized but untested policy. Conformal calibration on data from the safe policy determines how aggressively the new policy can act, while provably enforcing the user's declared risk tolerance. Unlike conservative optimization methods, we do not assume the user has identified the correct model class nor tuned any hyperparameters. Unlike previous conformal methods, our theory provides finite-sample guarantees even for non-monotonic bounded loss functions. Our experiments on applications ranging from natural language question answering to biomolecular engineering show that safe exploration is not only possible from the first moment of deployment, but can also improve performance.

## One-Sentence Claim

Conformal Policy Control uses a safe reference policy as a calibrated probabilistic regulator for an optimized policy, enabling finite-sample risk-controlled exploration from deployment time.

## Problem

Agents need to explore new behaviors to improve, but in high-stakes settings unsafe behavior may cause harm and end deployment. Pure imitation of a known-safe policy avoids harm but can be too conservative to improve performance.

The core question is how far a new optimized policy can deviate from a safe reference policy while respecting a user-declared risk tolerance, without assuming the right model class or carefully tuned safety hyperparameters.

## Core Contribution

The paper introduces a conformal calibration approach that uses data from a safe reference policy to regulate any optimized but untested policy. Calibration determines how aggressively the new policy can act while enforcing the declared risk tolerance.

The theoretical contribution is finite-sample guarantees for non-monotonic bounded loss functions, extending prior conformal risk-control approaches and making the method applicable to broader policy-control settings.

## Method

The safe reference policy supplies calibration data. The optimized policy proposes improved actions, but a conformal regulator limits or modulates behavior change according to calibrated risk estimates.

The method is model-agnostic: it does not require the user to specify the correct model class or tune conservative optimization hyperparameters. The calibration procedure translates finite samples into a policy-control threshold.

## Experiments and Evidence

The abstract reports experiments ranging from natural-language question answering to biomolecular engineering, showing that safe exploration can improve performance from the first moment of deployment.

Full-paper reading should verify the specific loss definitions, risk levels, calibration set sizes, reference policies, and how intervention affects performance versus safety violations.

## Limits and Failure Modes

Conformal guarantees depend on calibration assumptions, such as exchangeability or appropriate distributional stability between calibration and deployment. If the optimized policy induces severe distribution shift, the guarantee may weaken.

Safety is defined through the chosen bounded loss and declared tolerance. If the loss misses important harms, conformal control can enforce the wrong safety property precisely.

## Deep Themes

- Safe exploration through calibration: policy improvement is regulated by finite-sample risk guarantees.
- Reference policies as safety anchors: old behavior defines the baseline distribution for new behavior.
- User-declared risk tolerance: safety becomes an explicit parameter rather than an implicit conservatism knob.
- Conformal methods beyond prediction sets: calibration is used to control agent behavior.

## Subthemes

- Non-monotonic losses require broader conformal theory.
- First-moment deployment safety matters for high-stakes agents.
- Exploration and safety are not inherently opposed if deviation is calibrated.
- Model-free regulation supports heterogeneous optimized policies.

## Connections to Other Papers

This paper connects to JitRL, rare-update bandits, and safe RL/unlearning work through practical constraints on adaptive policies. It also relates to FIDIA and biomolecular design because both optimize new behavior in scientific domains, but this paper adds finite-sample risk control.

It fits with MAP and production-agent themes: deployed agents need mechanisms for safe improvement rather than static behavior locks.

## Notes for Cross-Paper Synthesis

Conformal Policy Control is a strong example of "guarded adaptation": let the model improve, but use a calibrated reference process to bound the risk of novelty.
