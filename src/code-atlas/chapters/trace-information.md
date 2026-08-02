# Trace Information

## The Big Idea

A reasoning trace is the work record between a question and an answer. It can
include scratch notes, tool calls, checked facts, intermediate conclusions, and
small decisions made along the way.

The trace is useful only if it is tied to the task. If the facts change, the
middle work should change at the place where those facts matter. If the trace
keeps the same shape after the task changes, it is not proof that the answer
came from the case. It may only be a polished story.

Think about a student solving two refund word problems. In the first problem,
the order arrived 24 days ago and the refund window is 30 days. In the second,
only one fact changes: the order arrived 41 days ago. The scratch work should
change when it compares the delivery age with the refund window. If both pages
of scratch work still approve the refund in the same words, the scratch work is
not doing its job.

## What Must Stay True

The protected thing is the link between facts, middle work, and final answer.
Style can stay the same. The answer format can stay the same. The grading rule
can stay the same. But the steps that depend on the changed fact must move.

This is the first-principles test:

1. Keep the task shape fixed.
2. Change one important fact.
3. Check whether the trace changes exactly where that fact is used.
4. Check whether the answer changes when the changed fact requires it.

## The Failure

The hidden failure is a trace that looks careful but ignores the task. It may
have numbered steps, calm language, and confident statements. Those features do
not make it evidence. The trace fails when it stays fluent while losing contact
with the fact that decides the answer.

This matters because people often trust process text. A long trace can feel
safer than a short answer. The course should teach the opposite habit: trust the
trace only when the trace reacts to the task.

## Why This Matters Outside The Demo

In customer support, a trace should show which policy clause and customer fact
changed the decision. In legal review, it should show which contract line
matters. In medicine, it should show which symptom, test result, or history
fact changed the next step. In code repair, it should show which failing test
or runtime error moved the patch.

In topology, the same habit appears as a concern for what stays meaningful
under change. If a shape is bent or stretched, the exact coordinates can move,
but the important connection or hole should still be tracked. If a description
of the shape does not change when a real connection is cut, the description is
not faithful. Trace checking asks the same kind of question: did the
description move when the real structure moved?

## What Client Data Makes It Real

Use paired tasks that differ by one important fact. Save the trace, final
answer, and expected decision for each task. Then mark which trace steps use the
changed fact. The evidence is strong only when the changed fact appears in the
middle work and changes the answer when it should.
