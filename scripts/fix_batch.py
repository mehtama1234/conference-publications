#!/usr/bin/env python3
"""Auto-fix the recurring jargon/vague flags in a batch of explainer specs.
For each spec in the batch (arg = slug-json, default data/rollout/auto-pass.json),
run clarity_lint; for each flagged word we have a safe plain replacement, apply it
spec-wide (skipping equation/symbol/worked fields); re-lint; print any residuals to
fix by hand. Never touches analogy/notation flags (those need real rewording).
"""
import json, os, sys, subprocess, glob

BATCH = sys.argv[1] if len(sys.argv) > 1 else "data/rollout/auto-pass.json"
slugs = json.load(open(BATCH))
SKIP = {"equation","words","symbols","worked","viz_args","metric_eq","slug","id","nav","toc","conf","theme_slug","title"}

# safe plain swaps, applied only when the linter flags that word in a spec
REPL = {
 "matrix": [("matrix operations","table operations"),("matrix multiplication","table multiplication"),
            ("attention matrix","attention table"),(" matrix"," number-table"),("Matrix","Number-table")],
 "token": [("summary tokens","summary markers"),("summary token","summary marker"),
           (" tokens"," chunks of text"),(" token"," chunk of text")],
 "kernel": [("sparse kernel","sparse compute routine"),(" kernel"," compute routine")],
 "inference": [("Inference","Answer-time"),("inference","answering time")],
 "parameter": [("parameters","internal settings"),("parameter","internal setting")],
 "geometry": [("geometry","shape")],
 "distribution": [("distributions","data patterns"),("distribution","data pattern")],
 "attention": [("pay attention to","focus on"),("attention to","focus on"),("attention","focus")],
 "gradient": [("gradient descent","downhill training"),("gradients","training nudges"),("gradient","training nudge")],
 "embedding": [("embeddings","lists of numbers"),("embedding","list of numbers")],
 "latent": [("latent space","hidden space"),("latents","hidden values"),("latent","hidden")],
 "activation": [("activations","layer outputs"),("activation","layer output")],
 "empiric": [("empirically","by trial and error"),("empirical","measured")],
 "meaningful": [("meaningful","real")],
 "robust": [("more robust","steadier"),("robust","reliable")],
 "novel": [("novel","new")],
 "landscape": [("landscape","surface")],
 "significantly": [("significantly","sharply")],
 "effectively": [("effectively","in practice")],
}

def walk(o, reps, k=None):
    if isinstance(o, dict): return {kk: walk(vv, reps, kk) for kk, vv in o.items()}
    if isinstance(o, list): return [walk(x, reps, k) for x in o]
    if isinstance(o, str) and k not in SKIP:
        for a, b in reps: o = o.replace(a, b)
        return o
    return o

def flags(fp):
    out = subprocess.run(["python3","scripts/clarity_lint.py",fp],capture_output=True,text=True).stdout
    return [l.strip() for l in out.splitlines() if l.strip().startswith("[")]

residual = {}
for s in slugs:
    fp = f"specs/{s}.json"
    if not os.path.exists(fp): continue
    fl = flags(fp)
    if not fl: continue
    words = set()
    for l in fl:
        parts = l.split("]", 1)
        if len(parts) < 2: continue
        w = parts[1].strip().split()[0]
        for key in REPL:
            if w.startswith(key): words.add(key)
    if words:
        d = json.load(open(fp))
        reps = [r for key in words for r in REPL[key]]
        json.dump(walk(d, reps), open(fp, "w"), indent=1)
    fl2 = flags(fp)
    if fl2: residual[s] = fl2

print(f"auto-fixed batch of {len(slugs)}; residuals need hand-fix: {len(residual)}")
for s, fl in residual.items():
    print(f"  {s}")
    for l in fl[:4]: print(f"     {l}")
