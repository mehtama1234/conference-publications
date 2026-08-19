#!/usr/bin/env python3
"""Stage the next batch of a THEME's papers for full deep dives — used to FINISH
a whole theme (every paper with a usable abstract gets a 7-part explainer).
Usage: python3 scripts/stage_theme.py "<Theme Name>" [batch=80]
Picks papers in that theme with no deep dive yet and abstract>400, most-mechanistic
first, writes data/explainer_in/<slug>.json + data/rollout/auto-pass.json, prints ids.
"""
import json, os, re, sys
def slug(pid): return re.sub(r"[^a-z0-9]+", "-", pid.lower()).strip("-")

theme = sys.argv[1]
batch = int(sys.argv[2]) if len(sys.argv) > 2 else 80
P = {p["id"]: p for p in json.load(open("data/papers_all.json"))}
A = json.load(open("data/analysis_merged.json"))
have = set(os.path.basename(f)[:-5] for f in __import__("glob").glob("specs/*-or-*.json"))

rows = [r for r in A if r.get("theme") == theme]
todo = [r for r in rows if slug(r["id"]) not in have and len(P.get(r["id"], {}).get("abstract", "")) > 400]
todo.sort(key=lambda r: -len(r.get("methods", [])))
picked = []
for r in todo[:batch]:
    pid = r["id"]; p = P[pid]; sg = slug(pid)
    json.dump({"slug": sg, "id": pid, "conf": pid.split("-")[0].upper(), "title": p["title"],
               "theme": theme, "theme_slug": slug(theme), "abstract": p["abstract"],
               "methods": r.get("methods", []), "problem": r.get("problem", ""),
               "approach": r.get("approach", ""), "contribution": r.get("contribution", "")},
              open(f"data/explainer_in/{sg}.json", "w"))
    picked.append(sg)
json.dump(picked, open("data/rollout/auto-pass.json", "w"))
remaining = len(todo) - len(picked)
print(f"staged {len(picked)} from '{theme}' · {remaining} still to-do after this batch")
print(json.dumps(picked))
