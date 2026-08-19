#!/usr/bin/env python3
"""Render the Theme & Subtheme explainer layer: for every theme, a detailed
plain-language first-principles page (theme intro + each subtheme explained, with
links to the real deep dives under it) plus a themes.html hub. Companion to the
flat map.html — this one actually EXPLAINS each grouping.
Usage: python3 scripts/build_theme_explainers.py
"""
import json, os, re, glob, html, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_paper_explainer import CSS
import build_site as bs, build_subthemes as bt

def e(s): return html.escape(str(s), quote=True)
def sslug(name): return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")

EXTRA = """
.hero{background:linear-gradient(#0d1314,#12201f);color:#EAF3F1}
.bigq{font-size:18px;color:#B8C4C7;max-width:80ch;margin:6px 0 0}
.sub{border-top:1px solid var(--line);padding-top:8px;margin-top:30px}
.sub h2{margin-top:6px}.subgist{color:var(--muted);font-size:14px;margin:0 0 8px}
.chips{display:flex;flex-wrap:wrap;gap:7px;margin:12px 0}
.chip{display:inline-block;background:#fff;border:1px solid var(--line);border-radius:999px;padding:5px 12px;font-size:13px;color:#243130;text-decoration:none}
.chip:hover{border-color:var(--accent);color:#0A5A62}
.count{font-family:var(--mono);font-size:12px;color:var(--muted);margin:2px 0 0}
.tgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px;margin:18px 0}
.tcard{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 18px;text-decoration:none;color:inherit;transition:border-color .15s}
.tcard:hover{border-color:var(--accent)}.tcard .nm{font-weight:650;font-size:18px;color:#111819;letter-spacing:-.01em}
.tcard .q{font-size:14px;color:#41524f;margin:6px 0 8px;line-height:1.5}.tcard .m{font-family:var(--mono);font-size:11px;color:var(--muted)}
"""
NAV = ('<a href="themes.html">← All themes explained</a><a href="map.html">Field map</a>'
       '<a href="math.html">Mathematics</a><a href="paper-explainers.html">All explainers</a>')

def shell(title, body):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{e(title)}</title><style>{CSS}{EXTRA}</style></head><body>{body}</body></html>')

def papers_by_subtheme(theme, rows):
    subs = bt.load_subthemes(bs.slug(theme)) or []
    for s in subs: s["_papers"] = []
    catch = {"_papers": []}
    for r in rows: (bt.assign(r, subs) or catch)["_papers"].append(r)
    out = {}
    for s in subs:
        out[bs.slug(theme) + "__" + sslug(s.get("name", "x"))] = s["_papers"]
    return out

def render_theme(spec, theme, rows, have):
    intro = "".join(f"<p>{e(p)}</p>" for p in spec.get("theme_intro", []))
    pmap = papers_by_subtheme(theme, rows)
    subs_html = ""
    for sub in spec.get("subthemes", []):
        explain = "".join(f"<p>{e(p)}</p>" for p in sub.get("explain", []))
        papers = pmap.get(sub.get("slug", ""), [])
        deep = [p for p in papers if bs.slug(p["id"]) in have]
        chips = "".join(f'<a class="chip" href="{bs.slug(p["id"])}.html">{e(p.get("title","")[:70])}</a>'
                        for p in deep[:14])
        more = f' <span class="count">+{len(deep)-14} more deep dives</span>' if len(deep) > 14 else ""
        subpage = f'subtheme-{e(sub.get("slug",""))}.html'
        readmore = f'<a class="chip" href="{subpage}" style="border-color:var(--accent);color:#0A5A62">Open the full subtheme page — narrative + all {len(papers)} papers →</a>'
        subs_html += (f'<div class="sub"><div class="eyebrow">Subtheme</div>'
                      f'<h2><a href="{subpage}" style="color:#111819;text-decoration:none">{e(sub.get("name",""))}</a></h2>'
                      f'{explain}<div class="count">{len(papers)} papers · {len(deep)} deep dives</div>'
                      f'<div class="chips">{readmore}{chips}</div>{more}</div>')
    body = f"""
<header class="hero"><div class="wrap"><div class="bug">Theme · {len(rows)} papers · {len(spec.get('subthemes',[]))} subthemes</div>
<h1>{e(theme)}</h1><p class="bigq">{e(spec.get('big_question',''))}</p></div></header>
<nav><div class="wrap">{NAV}</div></nav>
<div class="doc"><div class="wrap">
<div class="eyebrow">What this whole area is about</div>{intro}
{subs_html}
</div></div>"""
    return shell(theme + " — explained", body)

def render_hub(specs, counts):
    order = sorted(specs.keys(), key=lambda s: -counts.get(s, 0))
    cards = ""
    for slug in order:
        sp = specs[slug]
        cards += (f'<a class="tcard" href="theme-{e(slug)}-explained.html"><div class="nm">{e(sp["_theme"])}</div>'
                  f'<div class="q">{e(sp.get("big_question",""))}</div>'
                  f'<div class="m">{counts.get(slug,0)} papers · {len(sp.get("subthemes",[]))} subthemes explained</div></a>')
    body = f"""
<header class="hero"><div class="wrap"><div class="bug">ICML + ICLR 2026 · the field in plain words</div>
<h1>Every theme, explained from scratch</h1>
<p class="bigq">The field map shows how the {sum(counts.values()):,} papers group into 18 themes and 165 subthemes. This layer explains what each of those groups actually IS — the real problem, why it is hard, and how the work tackles it — in plain everyday words, no jargon.</p></div></header>
<nav><div class="wrap"><a href="map.html">Field map</a><a href="math.html">Mathematics</a><a href="index.html">Landscape</a><a href="paper-explainers.html">All explainers</a></div></nav>
<div class="doc"><div class="wrap"><div class="tgrid">{cards}</div></div></div>"""
    return shell("Every theme explained — ICML + ICLR 2026", body)

def main():
    have = set(os.path.basename(f)[:-5] for f in glob.glob("specs/*-or-*.json"))
    theme_by_slug = {bs.slug(t): t for t in bs.BY_THEME}
    rows_by_slug = {bs.slug(t): r for t, r in bs.BY_THEME.items()}
    specs = {}
    for f in glob.glob("specs/themes/*.json"):
        slug = os.path.basename(f)[:-5]
        if slug not in theme_by_slug: continue
        sp = json.load(open(f)); sp["_theme"] = theme_by_slug[slug]
        specs[slug] = sp
        open(f"site/theme-{slug}-explained.html", "w").write(
            render_theme(sp, theme_by_slug[slug], rows_by_slug[slug], have))
    counts = {s: len(rows_by_slug[s]) for s in specs}
    open("site/themes.html", "w").write(render_hub(specs, counts))
    print(f"built {len(specs)} theme-explained pages + themes.html")

if __name__ == "__main__":
    main()
