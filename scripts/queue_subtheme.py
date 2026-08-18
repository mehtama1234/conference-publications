#!/usr/bin/env python3
"""Queue a subtheme for the explainer rollout: pick its top-N papers, build
their explainer input files, and write the id list to data/rollout/<tag>.json.
Then: fetch_method.py --file data/rollout/<tag>.json  and run the writer workflow.
Usage: python3 scripts/queue_subtheme.py <theme-slug> "<name substring>" <N> <tag>
"""
import json, re, sys
D = "data"
theme_slug, name_sub, N, tag = sys.argv[1], sys.argv[2].lower(), int(sys.argv[3]), sys.argv[4]
merged = {r["id"]: r for r in json.load(open(f"{D}/analysis_merged.json"))}
papers = {p["id"]: p for p in json.load(open(f"{D}/papers_all.json"))}
theme_name = {re.sub(r'[^a-z0-9]+','-',r["theme"].lower()).strip('-'): r["theme"] for r in merged.values()}[theme_slug]
subs = json.load(open(f"{D}/subtheme_out/{theme_slug}.json"))["subthemes"]
target = [s for s in subs if name_sub in s["name"].lower()][0]
kw = [k.lower() for k in target["keywords"]]
pool = [r for r in merged.values() if r["theme"] == theme_name]
def score(r):
    t = (papers.get(r["id"], {}).get("title", "") + " " + " ".join(r.get("methods", [])) + " " + r.get("approach", "")).lower()
    return sum(1 for k in kw if k in t)
cand = sorted([r for r in pool if score(r) >= 2], key=lambda r: -score(r))[:N]
def slug(pid): return re.sub(r'[^a-z0-9]+', '-', pid.lower()).strip('-')
ids = []
for r in cand:
    pid = r["id"]; p = papers[pid]; s = slug(pid); ids.append(pid)
    json.dump({"slug": s, "id": pid, "conf": pid.split("-")[0].upper(), "title": p["title"],
               "theme": r["theme"], "theme_slug": theme_slug, "abstract": p["abstract"],
               "methods": r.get("methods", []), "problem": r.get("problem", ""),
               "approach": r.get("approach", ""), "contribution": r.get("contribution", "")},
              open(f"{D}/explainer_in/{s}.json", "w"))
json.dump([slug(i) for i in ids], open(f"{D}/rollout/{tag}.json", "w"))
print(f"SUBTHEME: {target['name']}  ({len(ids)} papers)")
for pid in ids: print(f"  {pid}  {papers[pid]['title'][:60]}")
