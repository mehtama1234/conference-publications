#!/usr/bin/env python3
"""Plan an autonomous coverage pass: across every theme, pick the biggest
subthemes that still lack deep dives, stage explainer input files for a few
fresh papers each (skipping papers that already have a spec), and emit the slug
list for a parallel Haiku run. Each agent fetches its own real method + writes.
Usage: python3 scripts/plan_rollout.py [papers_per_subtheme] [subthemes_per_theme] [total_cap]
"""
import json, os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_site as bs, build_subthemes as bt

PPS = int(sys.argv[1]) if len(sys.argv) > 1 else 4      # papers per subtheme
SPT = int(sys.argv[2]) if len(sys.argv) > 2 else 2      # subthemes per theme
CAP = int(sys.argv[3]) if len(sys.argv) > 3 else 90     # total papers this pass
D = "data"
papers = {p["id"]: p for p in json.load(open(f"{D}/papers_all.json"))}
def slug(pid): return re.sub(r"[^a-z0-9]+", "-", pid.lower()).strip("-")
def has_spec(pid): return os.path.exists(f"specs/{slug(pid)}.json")
def has_deep(pid): return os.path.exists(f"site/{slug(pid)}.html")

picked = []
for theme, rows in sorted(bs.BY_THEME.items(), key=lambda kv: -len(kv[1])):
    tslug = bs.slug(theme); subs = bt.load_subthemes(tslug)
    if not subs: continue
    for s in subs: s["_papers"] = []
    catch = {"_kw": [], "_papers": []}
    for r in rows: (bt.assign(r, subs) or catch)["_papers"].append(r)
    # subthemes ranked by size, preferring those with fewest existing deep dives
    ranked = sorted(subs, key=lambda s: (sum(1 for r in s["_papers"] if has_deep(r["id"])), -len(s["_papers"])))
    taken_here = 0
    for s in ranked:
        if taken_here >= SPT: break
        # fresh papers in this subtheme, most-mechanistic first
        fresh = [r for r in s["_papers"] if not has_spec(r["id"]) and len(papers.get(r["id"], {}).get("abstract", "")) > 400]
        fresh.sort(key=lambda r: -len(r.get("methods", [])))
        chosen = fresh[:PPS]
        if len(chosen) < 2: continue
        for r in chosen:
            pid = r["id"]; p = papers[pid]; sg = slug(pid)
            json.dump({"slug": sg, "id": pid, "conf": pid.split("-")[0].upper(), "title": p["title"],
                       "theme": theme, "theme_slug": tslug, "abstract": p["abstract"],
                       "methods": r.get("methods", []), "problem": r.get("problem", ""),
                       "approach": r.get("approach", ""), "contribution": r.get("contribution", "")},
                      open(f"{D}/explainer_in/{sg}.json", "w"))
            picked.append(sg)
        taken_here += 1
        if len(picked) >= CAP: break
    if len(picked) >= CAP: break

picked = picked[:CAP]
json.dump(picked, open(f"{D}/rollout/auto-pass.json", "w"))
print(f"staged {len(picked)} papers across the field for an autonomous parallel pass")
