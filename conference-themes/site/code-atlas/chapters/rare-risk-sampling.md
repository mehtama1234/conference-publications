# Rare-Risk Sampling

## The Big Idea

Average testing mostly sees ordinary cases. That is useful when ordinary cases
are the main risk. It is dangerous when harm is rare but costly.

If a bad case appears once in many runs, a random test can miss it and still
report a clean score. The system then looks safe because the test did not visit
the place where safety matters.

## What Must Stay True

The protected thing is the harm definition. A bad transfer, unsafe medical
answer, security break, or dangerous robot move is still bad even if it is rare.
The test must make that bad region visible often enough to estimate risk.

## The Failure

The hidden failure is false comfort. The average benchmark passes because it
spends almost all of its budget on easy or common cases. The rare case is not
fixed. It is only unseen.

The course should teach that "we did not find a bad case" is weak evidence when
the test almost never had a chance to find one.

## Why This Matters Outside The Demo

In finance, rare stress events can dominate loss. In security, one unusual path
can break the system. In medicine, rare patient states can carry high
consequence. In robotics, a rare surface, lighting condition, or obstacle
placement can decide whether the robot is safe.

In topology, rare cases often happen near boundaries: a tiny bridge, a nearly
closed hole, a thin handle, a self-touching surface, or two regions that almost
merge. A method can pass common shapes while failing exactly where the structure
is hardest to preserve.

## What Client Data Makes It Real

Use incident classes, production frequencies, edge prompts, stress scenarios,
red-team cases, and the number of tests needed to estimate the rate. The proof
is that the test visits the risky region often enough for the result to mean
something.
