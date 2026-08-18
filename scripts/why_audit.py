#!/usr/bin/env python3
"""'Why audit' — find conceptual claims that are STATED but not EXPLAINED.
Flags prose sentences that assert a benefit or a cause-and-effect (faster,
better, more accurate, so the model..., this makes..., leads to...) WITHOUT a
nearby explanation of the mechanism (because / since / so that / which means /
the reason / by <do>ing). Heuristic: surfaces candidates to add the 'why' to.
Use: python3 scripts/why_audit.py [specs/x.json ...]
"""
import json, re, sys, glob, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPECS = os.path.join(ROOT, "specs")
SKIP = {"equation", "words", "symbols", "viz_args", "slug", "id", "nav", "toc", "conf",
        "theme_slug", "metric_eq"}

CLAIM = re.compile(r"\b(faster|quicker|more accurate|more reliable|more efficient|better|"
                   r"stronger|improves?|boosts?|enables?|leads to|results in|allows?|helps?|"
                   r"so the model|this makes|makes it|converge[s]? faster|higher accuracy|"
                   r"lower cost|cheaper|saves|speeds? up|outperforms?)\b", re.I)
EXPLAIN = re.compile(r"\b(because|since|so that|which means|which lets|the reason|reason is|"
                     r"this works by|by \w+ing|as a result|due to|that is why|this is why|"
                     r"in other words|meaning that|so it|so they|so each)\b", re.I)

def prose(o, path=""):
    out = []
    if isinstance(o, dict):
        for k, v in o.items():
            if k in SKIP: continue
            out += prose(v, f"{path}.{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o): out += prose(v, f"{path}[{i}]")
    elif isinstance(o, str): out.append((path, o))
    return out

SKIP_PATH = (".h2", ".title", ".worked", "].b", ".caption", "one_liner", ".kick")
def audit(fp):
    s = json.load(open(fp))
    flags = []
    for path, text in prose(s):
        if any(sp in path for sp in SKIP_PATH):   # headers/titles/labels aren't claims to explain
            continue
        # split into sentences; a claim is explained if THIS or the NEXT sentence explains
        sents = re.split(r"(?<=[.!?])\s+", re.sub(r"<[^>]+>", "", text))
        for i, snt in enumerate(sents):
            if CLAIM.search(snt):
                window = snt + " " + (sents[i+1] if i+1 < len(sents) else "")
                if not EXPLAIN.search(window):
                    flags.append((path, snt.strip()[:150]))
    return flags

def main():
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(SPECS, "*.json")))
    total = 0
    for fp in files:
        if os.path.basename(fp).startswith("_"): continue
        fl = audit(fp)
        total += len(fl)
        name = os.path.basename(fp)
        if fl:
            print(f"\n{name}: {len(fl)} unexplained claim(s)")
            for path, snt in fl[:12]:
                print(f"  [{path}] {snt}")
        else:
            print(f"{name}: no unexplained claims ✓")
    print(f"\nTOTAL unexplained claims: {total}")
    sys.exit(1 if total else 0)

if __name__ == "__main__":
    main()
