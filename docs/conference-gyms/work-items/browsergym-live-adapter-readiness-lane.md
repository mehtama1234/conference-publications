# BrowserGym Live Adapter Readiness Lane

Status: `planned`

## Goal

Make `BrowserGym` the first live-environment conference gym lane after ADP:

`BrowserGym task -> reset browser env -> observe state -> take action -> call verifier -> emit normalized scorecard`

ADP proved the trace/package path. BrowserGym proves the live environment path.

## Why This Next

`BrowserGym` already has the structure we want:

- task list through Gymnasium env ids
- `reset()` for environment setup
- browser observations: URL, screenshot, DOM, accessibility tree, chat, goal
- string action space mapped into browser actions
- `step()` returning observation, reward, termination, truncation, and info
- task-level `validate()` verifier

That means it is the cleanest next target for our normalized gym format.

## Source Contract Observed

- Environment class: `browsergym.core.env.BrowserEnv`
- Task base class: `browsergym.core.task.AbstractBrowserTask`
- `setup(page)` returns `goal, info`
- `validate(page, chat_messages)` returns `reward, done, message, info`
- Action space: Unicode action string, usually mapped to browser Python code
- Observation fields include goal, screenshot, DOM object, accessibility tree, URL, chat messages, last action, last action error, and elapsed time

## First Slice

Use one local MiniWoB-style BrowserGym task, not a full WebArena/OpenApps deployment.

Required receipts:

1. normalized task spec
2. environment setup/reset receipt
3. initial observation receipt
4. allowed action schema receipt
5. one or more step trace receipts
6. verifier result receipt
7. scorecard receipt

## Normalized Shape

```text
task:
  id, source env id, instruction, seed, constraints

environment:
  runtime family, setup/import, reset receipt, teardown policy

observation:
  url, screenshot hash/ref, DOM hash/summary, a11y tree hash/summary, chat messages

actions:
  allowed action language, raw action, mapped action, action error

verifier:
  validate entrypoint, reward, success, done, message, info

scorecard:
  success, score 0-1, steps, elapsed time, failure mode, reproducibility receipt
```

## Gates

- Production allowed: `false`
- Promotion allowed: `false`
- Training export allowed: `false`
- Agent execution allowed: `false` until reset, step, validate, and teardown are proven with a controlled smoke

## Local Preflight

Current status: `blocked`

Import check failed because `gymnasium` is not installed in the current Python environment.

Next setup action: install BrowserGym core dependencies in an isolated environment, then rerun import and MiniWoB registry discovery.

## Next Engineering Action

Add a small BrowserGym adapter smoke script that imports `browsergym.core` and `browsergym.miniwob`, discovers one local task, resets it, performs one controlled action, calls validation, and writes a normalized scorecard receipt.
