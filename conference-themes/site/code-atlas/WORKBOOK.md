# Code Atlas Workbook

This workbook turns the course habit into a repeatable exercise.

Use it after reading the course map and one chapter. The goal is not to repeat
paper words. The goal is to write a small proof plan for a real workflow in
plain language.

After filling out the worksheet, turn it into a proof packet using
[PROOF-PACKETS.md](PROOF-PACKETS.md). The packet is the client-facing evidence
artifact.

## The One-Page Proof Worksheet

Fill this out before building a demo or client adapter.

1. Real object
   What can someone inspect? Name the task, trace, artifact, score, record,
   sample, update, or cause claim.

2. Protected thing
   What must stay true after the method is used? Say it as a concrete behavior,
   decision, fact, outcome, shape property, or user path.

3. Allowed change
   What is allowed to move? Examples: wording, number of tool calls, memory
   size, score pressure, sample path, precision, training step, or background
   assumption.

4. Shallow check
   What easy check could pass while the real thing fails?

5. Hidden failure
   What bad case would expose the weakness?

6. Evidence
   What records would prove the method helped or prove that it failed?

7. Other-field test
   Explain the same pattern in another field. If topology fits, name the thing
   that survives bending, stretching, rounding, or redrawing: a hole, boundary,
   connection, piece count, or inside-outside relationship.

## Worked Example: Support Refund Trace

Real object:
The support ticket, the assistant trace, and the final refund decision.

Protected thing:
The decision must follow the refund rule and the order age.

Allowed change:
The customer facts can change. The writing style and answer format stay fixed.

Shallow check:
A reviewer reads the trace and sees calm, numbered steps.

Hidden failure:
The order age changes from 24 days to 41 days, but the trace still approves the
refund using the same middle work.

Evidence:
Use paired tickets, saved traces, final answers, and a marked trace diff showing
whether the changed fact was used.

Other-field test:
In topology, if a real connection in a shape is cut, a faithful description of
the shape should change. If the description stays the same after the connection
changes, it is not tracking the structure.

## Worked Example: Numerical Compression

Real object:
A deployed model run with full-precision and low-precision outputs.

Protected thing:
User-visible decisions near dollar thresholds must stay the same.

Allowed change:
The number format, hardware kernel, memory use, and latency can change.

Shallow check:
The average score stays almost the same.

Hidden failure:
Rare claims with repeated dollar calculations cross the threshold after
rounding, so the cheaper model makes a different decision.

Evidence:
Use full-precision outputs, low-precision outputs, latency, memory, and a
regression set focused on threshold cases.

Other-field test:
In geometry, rounding coordinates may make a tiny gap disappear. The important
question is not whether the coordinates look close. The important question is
whether the gap, hole, boundary, or inside-outside decision survived.

## Topic Prompts

Trace information:
What fact changes, and where should the middle work change?

Tool-cost tradeoffs:
What doubt does one more action remove, and what does that action cost?

Artifact-native judging:
Where does the user-facing object fail, and does the checker inspect that
place?

Stand-in score drift:
What real target can get worse while the score gets better?

Rare-risk sampling:
What rare case carries high consequence, and how will the test visit it?

Context compression:
What quiet fact can change the later answer, and does it survive the shorter
memory?

Numerical compression:
What fragile behavior could be damaged while the average score survives?

Sample-making paths:
What valid kind of output might disappear when the generator is steered?

Movement rulers:
What useful behavior must survive the training move?

Same-evidence cause stories:
What rival story still explains the same records?

## Client Adapter Checklist

Do not call the adapter useful until these are true:

- The client can point to the real object.
- The protected thing is measured before and after the method.
- The allowed change is narrow enough to understand.
- The hidden failure is a failure that can happen in the client's workflow.
- The evidence includes at least one hold case and one fail case.
- The result is allowed to be negative.
- The explanation uses everyday words before any technical label.

## Final Self-Test

A reader is ready to use the course when they can answer these questions for a
new topic:

1. What is the object?
2. What has to survive?
3. What can move?
4. What shallow check would fool us?
5. What record would decide the question?
6. How would the same idea appear in topology, software, medicine, finance,
   robotics, science, or geometry?
