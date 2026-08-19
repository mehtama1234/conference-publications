#!/usr/bin/env python3
"""Build per-subtheme input files for standalone subtheme pages. Each carries the
subtheme's already-written first-principles explanation + EVERY paper routed to it
(title + its analysed contribution + whether it has a deep dive), so a Haiku agent
can write a narrative that situates the real papers inside the subtheme's story.
"""
import json, os, re, glob, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_site as bs, build_subthemes as bt

def sslug(name): return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")

ANALYSIS = {r["id"]: r for r in json.load(open("data/analysis_merged.json"))}
have = set(os.path.basename(f)[:-5] for f in glob.glob("specs/*-or-*.json"))
# pull the already-written subtheme explanations from the theme specs
explain_by_slug = {}
for f in glob.glob("specs/themes/*.json"):
    for s in json.load(open(f)).get("subthemes", []):
        explain_by_slug[s.get("slug", "")] = {"name": s.get("name", ""), "explain": s.get("explain", [])}

os.makedirs("data/subtheme_pages_in", exist_ok=True)
n = 0
for theme, rows in bs.BY_THEME.items():
    tslug = bs.slug(theme)
    subs = bt.load_subthemes(tslug)
    if not subs: continue
    for s in subs: s["_papers"] = []
    catch = {"_papers": [], "name": "__catch__"}
    for r in rows: (bt.assign(r, subs) or catch)["_papers"].append(r)
    for s in subs:
        subslug = tslug + "__" + sslug(s.get("name", "x"))
        papers = []
        for r in s["_papers"]:
            a = ANALYSIS.get(r["id"], {})
            p = bs.PAPERS.get(r["id"], {})
            papers.append({
                "id": r["id"], "slug": bs.slug(r["id"]),
                "title": p.get("title", "")[:140],
                "contribution": (a.get("contribution", "") or a.get("approach", ""))[:260],
                "deep": bs.slug(r["id"]) in have,
            })
        papers.sort(key=lambda x: (not x["deep"], x["title"]))
        for i, pp in enumerate(papers, 1): pp["n"] = i   # stable index for grouping
        exp = explain_by_slug.get(subslug, {})
        json.dump({
            "slug": subslug, "theme": theme, "theme_slug": tslug,
            "name": s.get("name", ""), "gist": s.get("gist", ""),
            "explain": exp.get("explain", []),
            "n_papers": len(papers), "n_deep": sum(1 for x in papers if x["deep"]),
            "papers": papers,
        }, open(f"data/subtheme_pages_in/{subslug}.json", "w"), indent=1)
        n += 1

print(f"wrote {n} subtheme input files")
