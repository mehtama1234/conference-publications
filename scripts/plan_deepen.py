#!/usr/bin/env python3
"""DEEPEN pass (step 2): every subtheme already has >=1 deep dive. Now add MORE
dives to the biggest under-served subthemes so high-traffic areas get 3-5 dives
instead of 1. Ranks subthemes by how far below their size-based target they are,
stages fresh papers (most-mechanistic first), emits the slug list for a Haiku run.
Usage: python3 scripts/plan_deepen.py [papers_per_subtheme=3] [total_cap=80]
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_site as bs, build_subthemes as bt

PPS = int(sys.argv[1]) if len(sys.argv) > 1 else 3     # fresh papers to add per subtheme this pass
CAP = int(sys.argv[2]) if len(sys.argv) > 2 else 80
D = "data"
papers = {p["id"]: p for p in json.load(open(f"{D}/papers_all.json"))}
def slug(pid): return bs.slug(pid)
def has_spec(pid): return os.path.exists(f"specs/{slug(pid)}.json")

def target(size):
    # how many dives a subtheme "should" have, by size
    if size >= 100: return 6
    if size >= 50:  return 5
    if size >= 25:  return 4
    if size >= 12:  return 3
    return 2

# collect every subtheme with its papers + current dive count
cells = []
for theme, rows in bs.BY_THEME.items():
    subs = bt.load_subthemes(bs.slug(theme)); tslug = bs.slug(theme)
    if not subs: continue
    for s in subs: s["_papers"] = []
    catch = {"_papers": []}
    for r in rows: (bt.assign(r, subs) or catch)["_papers"].append(r)
    for s in subs:
        size = len(s["_papers"])
        dives = sum(1 for r in s["_papers"] if has_spec(r["id"]))
        deficit = target(size) - dives
        if deficit > 0:
            cells.append((deficit, size, theme, tslug, s))

# most under-served (biggest deficit, then biggest subtheme) first
cells.sort(key=lambda c: (-c[0], -c[1]))
picked = []
for deficit, size, theme, tslug, s in cells:
    fresh = [r for r in s["_papers"] if not has_spec(r["id"])
             and len(papers.get(r["id"], {}).get("abstract", "")) > 400]
    fresh.sort(key=lambda r: -len(r.get("methods", [])))
    for r in fresh[:min(PPS, deficit)]:
        pid = r["id"]; p = papers[pid]; sg = slug(pid)
        json.dump({"slug": sg, "id": pid, "conf": pid.split("-")[0].upper(), "title": p["title"],
                   "theme": theme, "theme_slug": tslug, "abstract": p["abstract"],
                   "methods": r.get("methods", []), "problem": r.get("problem", ""),
                   "approach": r.get("approach", ""), "contribution": r.get("contribution", "")},
                  open(f"{D}/explainer_in/{sg}.json", "w"))
        picked.append(sg)
        if len(picked) >= CAP: break
    if len(picked) >= CAP: break

json.dump(picked, open(f"{D}/rollout/auto-pass.json", "w"))
print(f"staged {len(picked)} papers to deepen the most under-served subthemes")
print(json.dumps(picked))
