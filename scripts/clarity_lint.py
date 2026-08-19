#!/usr/bin/env python3
"""Clarity linter for paper-explainer specs. Scans every PROSE field (not the
equation/symbols/viz_args, which are allowed to hold notation) for:
  - raw math notation dumped into prose (=, ^2, subscripts, Greek, W.x, softmax(), argmax, ||, ->)
  - unglossed jargon (a watch-list; flagged if the term appears without a nearby plain gloss)
  - vague / cliche / filler words
Exit non-zero if anything is flagged. Use: python3 scripts/clarity_lint.py [specs/x.json ...]
"""
import json, re, sys, glob, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPECS = os.path.join(ROOT, "specs")

# fields that MAY contain notation (skip them)
SKIP_KEYS = {"equation", "words", "symbols", "viz_args", "metric_eq", "slug", "id", "nav", "toc", "conf", "theme_slug", "title", "connects"}

NOTATION = [
    (r"\b[a-zA-Z]_[a-z0-9]\b", "subscript notation (e.g. x_t)"),
    (r"\^\s*[0-9]", "exponent notation (e.g. ^2)"),
    (r"[·×→≈∑√∈∏]", "math symbol"),
    (r"[θλαβσπμγδ]", "greek letter"),
    (r"\|\|", "norm bars ||"),
    (r"\bsoftmax\s*\(", "softmax( in prose"),
    (r"\bargmax\b", "argmax in prose"),
    (r"\b[A-Z]\s*[·*]\s*[a-z]\b", "matrix-times-vector (W·x)"),
    (r"(?<![a-z])= ?[a-zA-Z0-9(]", "equals sign / equation in prose"),
    (r"\bO\([A-Za-z]", "big-O notation"),
]

# jargon that must be glossed nearby (within ~60 chars) with '(' or '—' or 'that is' or 'i.e.'
JARGON = ["embedding", "latent", "gradient", "manifold", "softmax", "logit", "tensor",
          "stochastic", "posterior", "prior", "kernel", "quantiz", "entropy", "cosine",
          "euclidean", "autoregress", "superpos", "empiric", "convolution", "transformer",
          "activation", "parameter", "regulariz", "distribution", "token", "attention",
          "inference", "backprop", "softmax", "vector", "scalar", "matrix"]

VAGUE = ["leverage", "robust", "powerful", "novel", "various", "seamless", "rich ",
         "sophisticated", "cutting-edge", "state-of-the-art", "game-chang", "under the hood",
         "at the heart of", "the key insight", "secret sauce", "in essence", "harness",
         "utilize", "facilitate", "myriad", "plethora", "delve", "tapestry", "realm",
         "landscape", "paradigm", "holistic", "synerg", "elegant", "profound", "crucial",
         "significantly", "effectively", "efficiently improve", "meaningful", "geometry",
         "notion of", "in the world of", "it turns out", "remarkable", "fascinating"]

ANALOGY = ["imagine a", "imagine you", "think of it as", "think of it like", "it's like ",
           "like a ", "as if it were", "picture a ", "picture an ", "kind of like", "just like a",
           "analogy", "metaphor", "similar to how a"]

ORDER = ["lead", "problem", "object", "comic", "flow", "hidden", "mechanism", "bars", "failures", "demo", "math"]
def okey(path):
    for i, k in enumerate(ORDER):
        if f".{k}" in path: return i
    return 99

def prose_strings(o, path=""):
    out = []
    if isinstance(o, dict):
        for k, v in o.items():
            if k in SKIP_KEYS: continue
            out += prose_strings(v, f"{path}.{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o): out += prose_strings(v, f"{path}[{i}]")
    elif isinstance(o, str):
        out.append((path, o))
    return out

def gloss_near(text, m):
    w = text[max(0, m.start()-6):m.end()+80].lower()
    return any(g in w for g in ["(", "—", " that is", " i.e", " meaning", " just a", " simply",
                                 "a list of numbers", "in plain", " — ", ", which", ": ", " means "])

def lint_spec(fp):
    s = json.load(open(fp))
    prose = sorted(prose_strings(s), key=lambda kv: okey(kv[0]))
    issues = []
    seen_jargon = set()   # first-use gloss: only check a term the first time it appears on the page
    for path, text in prose:
        # ignore words inside quoted spans (cited paper titles / direct quotes) —
        # a paper literally named "Powerful Discrete Tokenizer" must be quoted verbatim
        text = re.sub(r'“[^”]{0,160}”', "  ", text)
        text = re.sub(r'"[^"]{0,160}"', "  ", text)
        low = text.lower()
        if ".worked" not in path:   # worked examples may show arithmetic
            for pat, name in NOTATION:
                for m in re.finditer(pat, text):
                    issues.append(("NOTATION", name, path, text[max(0,m.start()-22):m.start()+22]))
        for j in JARGON:
            m = re.search(r"\b" + j, low)
            if m and j not in seen_jargon:
                seen_jargon.add(j)
                if not gloss_near(text, m):
                    issues.append(("JARGON(1st use)", j, path, text[max(0,m.start()-22):m.start()+40]))
        for v in VAGUE:
            if v in low:
                i = low.find(v)
                issues.append(("VAGUE", v.strip(), path, text[max(0,i-18):i+25]))
        for a in ANALOGY:
            if a in low:
                i = low.find(a)
                issues.append(("ANALOGY", a.strip(), path, text[max(0,i-18):i+30]))
    return issues

def main():
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(SPECS, "*.json")))
    total = 0
    for fp in files:
        if os.path.basename(fp).startswith("_"): continue
        iss = lint_spec(fp)
        total += len(iss)
        name = os.path.basename(fp)
        if iss:
            print(f"\n{name}: {len(iss)} issues")
            for kind, term, path, ctx in iss[:40]:
                print(f"  [{kind}] {term:22s} {path:28s} …{ctx.strip()}…")
        else:
            print(f"{name}: clean ✓")
    print(f"\nTOTAL issues: {total}")
    sys.exit(1 if total else 0)

if __name__ == "__main__":
    main()
