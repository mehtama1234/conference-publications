# Code Atlas Proof Packets

A proof packet is the small artifact a client can inspect after a demo run.

It should not be a sales summary. It should say what was tested, what had to
stay true, what changed, what failure appeared or did not appear, and what
records support the claim.

## Packet Template

Use this shape for every topic.

Topic:
Name the course topic.

Claim:
Say the claim in one plain sentence.

Real object:
Name the thing someone can inspect.

Protected thing:
Name what must stay true.

Allowed change:
Name what was changed on purpose.

Hold case:
Show one record where the method should work.

Fail case:
Show one record where the hidden failure should appear if the method is weak.

Evidence:
List the exact records, runs, checks, diffs, scores, or logs used.

Decision:
Say what the evidence allows. The decision can be "supports the claim,"
"rejects the claim," or "not enough evidence."

Next client replacement:
Name what toy record should be replaced by the client's real export.

## Trace Information Packet

Topic:
Trace information.

Claim:
The middle work is evidence only if it changes where the task fact changes.

Real object:
Two support tickets, two traces, and two final refund decisions.

Protected thing:
The refund decision must follow the refund window and order age.

Allowed change:
Only the order age changes.

Hold case:
The order arrived 24 days ago. The trace compares 24 with 30 and approves the
refund.

Fail case:
The order arrived 41 days ago. A weak trace repeats the same approval path.

Evidence:
Paired tickets, saved traces, final answers, and a trace diff marking whether
the changed fact was used.

Decision:
Supports the claim only if the 41-day trace changes at the comparison step and
changes the answer.

Next client replacement:
Use real paired tasks, trace logs, answer diffs, and policy labels.

## Tool-Cost Tradeoffs Packet

Topic:
Tool-cost tradeoffs.

Claim:
One more tool call is useful only when the doubt it removes is worth more than
its cost and failure risk.

Real object:
Agent decisions about whether to call a price database.

Protected thing:
The final quote must be correct after cost and delay are counted.

Allowed change:
The agent may call or skip the database.

Hold case:
A high-value renewal has stale local pricing and customer tier changes the
quote. The tool can change the answer.

Fail case:
A low-value refund question is already clear from policy text. The tool adds
delay without changing the answer.

Evidence:
Before-tool confidence, tool result, after-tool answer, correctness, latency,
cost, and failed-call count.

Decision:
Supports the claim when tool calls concentrate in high-doubt cases and improve
enough answers to pay for themselves.

Next client replacement:
Use production tool-call logs, cost records, latency, failure rates, and answer
lift.

## Artifact-Native Judging Packet

Topic:
Artifact-native judging.

Claim:
The checker must inspect the object the user receives, not only the explanation.

Real object:
A generated dashboard and the claim that filters persist after refresh.

Protected thing:
The saved-filter user path must work.

Allowed change:
The checker can be text-only or artifact-native.

Hold case:
The artifact checker opens the dashboard, selects filters, refreshes, and sees
the filters remain.

Fail case:
The text-only judge passes the explanation, but the artifact resets filters
after refresh.

Evidence:
Browser run, screenshot or DOM state before refresh, state after refresh, and
the text-judge score.

Decision:
Supports the claim only when the artifact checker catches failures in the
actual user path.

Next client replacement:
Use real generated files, expected behavior, browser traces, tests, and citation
or proof checks.

## Stand-In Score Drift Packet

Topic:
Stand-in score drift.

Claim:
A score is safe to optimize only while it still tracks the real target.

Real object:
Support tickets scored by a quick-resolution metric and audited for true
resolution.

Protected thing:
Customer issues must actually be solved.

Allowed change:
Training pressure on the quick-resolution score increases.

Hold case:
Before training, high score and true resolution move together.

Fail case:
After training, the bot closes tickets with polite summaries while reopen rate
rises.

Evidence:
Score history, audit labels, reopen rate, before-training slice, after-training
slice, and examples that score well while failing.

Decision:
Rejects the score if it rises while the real target falls.

Next client replacement:
Use the client metric, independent outcome labels, audits, and gaming examples.

## Rare-Risk Sampling Packet

Topic:
Rare-risk sampling.

Claim:
Average testing is not enough when the bad case is rare and costly.

Real object:
Account-transfer requests with a rare high-risk state.

Protected thing:
Unsafe transfer approval must be visible and measured.

Allowed change:
The test can switch from random cases to stress cases near the risky state.

Hold case:
Stress cases include joint accounts, stale device trust, and high-value
transfer.

Fail case:
Random testing uses many ordinary transfer requests and never visits the risky
state.

Evidence:
Production frequency, stress-case definition, number of tests, bad-case count,
and estimated bad-case rate.

Decision:
Supports the claim only when the risky region is visited often enough to
estimate risk.

Next client replacement:
Use incident classes, edge workflows, red-team prompts, and production
frequencies.

## Context Compression Packet

Topic:
Context compression.

Claim:
A short memory is valid only if it keeps the fact that can change the later
answer.

Real object:
A long claim file, compressed memory, and final claim decision.

Protected thing:
The short-memory answer must match the full-record answer on decisive facts.

Allowed change:
The record can be shortened and the selection rule can change.

Hold case:
The compressed memory keeps the international-claim exclusion and blocks the
claim.

Fail case:
The compressed memory keeps repeated normal coverage notes and drops the
exclusion.

Evidence:
Full record, marked decisive facts, compressed record, full-record answer,
short-record answer, and disagreement notes.

Decision:
Supports the claim only when compression preserves the decisive fact and the
answer agrees with full context.

Next client replacement:
Use real long records, retained snippets, dropped snippets, and downstream
answer comparisons.

## Numerical Compression Packet

Topic:
Numerical compression.

Claim:
Cheaper numbers are acceptable only when user-visible behavior survives.

Real object:
Full-precision and low-precision model outputs for claims decisions.

Protected thing:
Threshold decisions and fragile rare cases must stay the same.

Allowed change:
Precision, kernel, memory use, and latency can change.

Hold case:
Common short claims keep the same decision and latency improves.

Fail case:
Rare repeated dollar calculations cross the approval threshold after rounding.

Evidence:
Full-precision outputs, low-precision outputs, latency, memory, average score,
and threshold-case regression results.

Decision:
Rejects the cheaper run if average score survives but threshold behavior
changes.

Next client replacement:
Use client model versions, quantization settings, hardware traces, and
regression cases.

## Sample-Making Paths Packet

Topic:
Sample-making paths.

Claim:
A generator must improve quality without erasing valid output families.

Real object:
Generated design samples and family labels.

Protected thing:
Rare valid design families must remain reachable.

Allowed change:
Guidance strength and correction weights can change.

Hold case:
Cleaner samples still include the named rare valid family.

Fail case:
Cleaner samples all follow the common shape and rare families disappear.

Evidence:
Generated samples, independent validity labels, named family counts, rare-family
recall, and before/after steering comparison.

Decision:
Supports the claim only when quality improves and rare valid coverage remains
measurable.

Next client replacement:
Use domain-specific samples, validity checks, family labels, and rare-mode
weights.

## Movement Rulers Packet

Topic:
Movement rulers.

Claim:
A training move should be judged by what it can break, not only by raw size.

Real object:
Two training checkpoints, an update summary, target-task results, and protected
regression results.

Protected thing:
Useful existing behavior must survive while the target improves.

Allowed change:
The update size and movement rule can change.

Hold case:
One update improves billing answers and keeps refund-policy regressions low.

Fail case:
Another update has similar raw size but damages refund-policy cases.

Evidence:
Checkpoint diff, target lift, protected regression suite, fragile-case results,
and movement-rule comparison.

Decision:
Supports the rule only when it predicts or avoids damage that raw size misses.

Next client replacement:
Use real checkpoints, eval suites, update summaries, and regression labels.

## Same-Evidence Cause Stories Packet

Topic:
Same-evidence cause stories.

Claim:
A cause claim should say only what the records and assumptions force.

Real object:
Training-program records, renewal outcomes, and background facts.

Protected thing:
The claim must not choose one cause story while a rival story still fits.

Allowed change:
Background facts can be held fixed, a deliberate test can be added, or noise can
be reduced.

Hold case:
Teams are compared with similar region, size, baseline renewal, and timing.

Fail case:
Raw renewal rates are compared even though trained and untrained teams have
different customer mixes.

Evidence:
Treatment records, outcomes, background facts, overlap checks, assumed rules,
sensitivity tests, and abstention cases.

Decision:
Allows a narrower cause claim only when rival stories are separated enough for
that claim.

Next client replacement:
Use real treatment records, outcome records, background facts, and sensitivity
analysis.
