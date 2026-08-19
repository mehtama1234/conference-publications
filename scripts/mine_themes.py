#!/usr/bin/env python3
"""Build per-theme input files for the Theme & Subtheme explainer layer.
Each theme file carries: the theme name, its subthemes (name + current gist +
a stable slug + a few representative paper titles), so a Haiku agent can write a
detailed plain-language first-principles explanation of the theme AND every
subtheme under it, grounded in what the papers actually do.
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_site as bs, build_subthemes as bt

def sslug(name): return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")

os.makedirs("data/theme_expl_in", exist_ok=True)
n_sub = 0
for theme, rows in bs.BY_THEME.items():
    tslug = bs.slug(theme)
    subs = bt.load_subthemes(tslug)
    if not subs: continue
    for s in subs: s["_papers"] = []
    catch = {"_papers": []}
    for r in rows: (bt.assign(r, subs) or catch)["_papers"].append(r)
    sub_recs = []
    for s in subs:
        papers = s["_papers"]
        titles = [p.get("title", "")[:90] for p in papers[:6]]
        sub_recs.append({
            "slug": tslug + "__" + sslug(s.get("name", "x")),
            "name": s.get("name", ""),
            "gist": s.get("gist", ""),
            "n_papers": len(papers),
            "sample_titles": titles,
        })
        n_sub += 1
    json.dump({
        "theme": theme, "theme_slug": tslug, "n_papers": len(rows),
        "n_subthemes": len(sub_recs),
        "subthemes": sorted(sub_recs, key=lambda x: -x["n_papers"]),
    }, open(f"data/theme_expl_in/{tslug}.json", "w"), indent=1)

print(f"wrote {len(list(bs.BY_THEME))} theme input files covering {n_sub} subthemes")
