# Tool-Cost Tradeoffs

## The Big Idea

An agent can often take one more action: search the web, query a database, run
code, ask a human, open a file, or call another model. More action feels safer,
but it is not always better. Every extra action costs time, money, attention,
and creates another place where the system can fail.

The plain question is: does this extra action remove enough doubt to be worth
what it costs?

Calling a mechanic before buying a used car is useful when the car is expensive
and uncertain. Calling a mechanic before choosing a cheap bicycle pump is
usually wasteful. The action is not good by itself. It is good only when the
decision is important enough and the action can actually change the answer.

## What Must Stay True

The protected thing is the quality of the final decision after cost is counted.
The agent may use more or fewer tools, but the business goal stays fixed. The
right comparison is not "did the tool help at least once?" The right comparison
is "did the tool help enough, often enough, to justify its cost and failures?"

## The Failure

The hidden failure is tool use as theater. The agent looks careful because it
calls tools, but the answer does not improve enough. The tool may be slow. It
may return stale data. It may fail silently. It may distract the agent from a
clear answer already present in the prompt.

The opposite failure also matters: the agent skips a tool when the local record
is stale and the wrong answer would be costly. The course should teach the
middle rule: use the tool when expected value is positive, not when tools feel
impressive.

## Why This Matters Outside The Demo

In finance, a pricing lookup is worth it for a high-value quote with stale
local data, but not for every low-risk support question. In medicine, a test is
worth ordering when its result can change care, not when it only adds noise. In
software, a slow integration test is worth running near risky code, not after
every harmless text edit.

In topology and geometry tools, the same idea appears when deciding whether to
run a costly shape check. A cheap check may say a mesh probably has one
connected piece. A more expensive check may be needed only near thin bridges,
tiny holes, or boundaries where the cheap answer is uncertain.

## What Client Data Makes It Real

Use logs with the agent's confidence before the tool, the tool called, latency,
cost, failure rate, answer before the tool, answer after the tool, and final
correctness. The proof is not that a tool was used. The proof is that the tool
changed enough wrong answers into right answers to pay for itself.
