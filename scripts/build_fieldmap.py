#!/usr/bin/env python3
"""Build site/map.html — the big-picture field map: all 18 themes -> their
first-principles subthemes -> paper counts + which subthemes have deep
explainer pages (and links to them). Top-down view of the whole corpus.
Reuses the subtheme taxonomy + assignment from build_subthemes.
Usage: python3 scripts/build_fieldmap.py"""
import os, sys, html, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import build_site as bs
import build_subthemes as bt

def e(s): return html.escape(str(s or ""), quote=False)

def has_deep(pid): return os.path.exists(os.path.join(bs.SITE, f"{bs.slug(pid)}.html"))

def theme_block(theme, rows):
    s = bs.slug(theme)
    subs = bt.load_subthemes(s)
    total_deep = sum(1 for r in rows if has_deep(r["id"]))
    parts = []
    if subs:
        catch = {"name": f"Other work in {theme}", "gist": "", "_kw": [], "_papers": []}
        for r in rows: (bt.assign(r, subs) or catch)["_papers"].append(r)
        allsubs = [x for x in subs if x["_papers"]] + ([catch] if catch["_papers"] else [])
        for x in allsubs:
            deep = [r for r in x["_papers"] if has_deep(r["id"])]
            badge = f'<span class="deep">{len(deep)} deep</span>' if deep else ""
            links = ""
            if deep:
                links = '<div class="dl">' + " · ".join(
                    f'<a href="{bs.slug(r["id"])}.html">{e(bs.PAPERS.get(r["id"],{}).get("title","")[:46])}&rarr;</a>'
                    for r in deep[:8]) + '</div>'
            import re as _re
            is_catch = x["name"].startswith("Other work in")
            subslug = s + "__" + _re.sub(r"[^a-z0-9]+", "-", x["name"].lower()).strip("-")
            href = f"theme-{s}.html" if is_catch else f"subtheme-{subslug}.html"
            parts.append(f'<div class="sub"><a class="subname" href="{href}">{e(x["name"])}</a>'
                         f'<span class="n">{len(x["_papers"])}</span>{badge}{links}</div>')
        nsub = len(allsubs)
    else:
        nsub = 0
    openattr = " open" if total_deep else ""
    dtag = f'<span class="deep">{total_deep} deep</span>' if total_deep else ""
    return (f'<details{openattr}><summary><a class="thname" href="theme-{s}.html">{e(theme)}</a>'
            f'<span class="n">{len(rows)} papers · {nsub} subthemes</span>{dtag}</summary>'
            + "".join(parts) + '</details>')

HEAD = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Field map · ICML + ICLR 2026</title>
<style>
:root{{--ink:#111819;--paper:#F5F6F4;--line:#D7DCD9;--muted:#5F6C70;--accent:#0E7C86;--mono:ui-monospace,Menlo,Consolas,monospace}}
body{{margin:0;background:var(--paper);color:var(--ink);font:15px/1.55 -apple-system,system-ui,Segoe UI,Roboto,sans-serif}}
.wrap{{max-width:1000px;margin:0 auto;padding:26px 22px 80px}}
.top{{font-family:var(--mono);font-size:12px;margin-bottom:10px}}.top a{{color:var(--accent);text-decoration:none;margin-right:14px}}
h1{{font-size:27px;margin:6px 0}}.sub0{{color:var(--muted);max-width:74ch}}
.stat{{font-family:var(--mono);font-size:13px;color:var(--accent);margin:12px 0 20px}}
details{{border:1px solid var(--line);border-radius:10px;background:#fff;margin:9px 0;padding:4px 14px}}
summary{{cursor:pointer;padding:9px 4px;list-style:none}}summary::-webkit-details-marker{{display:none}}
summary:before{{content:"\\25B8 ";color:var(--accent)}}details[open]>summary:before{{content:"\\25BE "}}
.thname{{font-size:17px;font-weight:700;color:var(--ink);text-decoration:none}}.thname:hover{{color:var(--accent)}}
.n{{font-family:var(--mono);font-size:12px;color:var(--muted);margin-left:10px}}
.deep{{font-family:var(--mono);font-size:11px;color:#fff;background:var(--accent);border-radius:20px;padding:1px 8px;margin-left:8px}}
.sub{{border-top:1px solid var(--line);padding:9px 4px 9px 20px}}
.subname{{font-size:14.5px;color:var(--ink);text-decoration:none;font-weight:600}}.subname:hover{{color:var(--accent)}}
.dl{{margin-top:5px;font-size:12.5px;line-height:1.7}}.dl a{{color:var(--accent);text-decoration:none;font-family:var(--mono)}}.dl a:hover{{text-decoration:underline}}
</style></head><body><div class="wrap">
<div class="top"><a href="index.html">Landscape</a><a href="themes.html">Themes explained</a><a href="hub.html">The Machine</a><a href="math.html">Mathematics</a><a href="idea-graph.html">Idea Graph</a><a href="paper-explainers.html">Explainer inventory</a></div>
<h1>The field map</h1>
<p class="sub0">The whole corpus, top to bottom: {nt} themes, each split into first-principles subthemes, down to the papers. Subthemes with a <span class="deep">deep</span> badge have full first-principles explainer pages — click a theme to open it, or jump straight to a deep dive. Want each theme and subtheme <b>explained in plain words</b> first? Read <a href="themes.html">every theme explained from scratch</a>.</p>
<div class="stat">{np:,} papers · {nt} themes · {nsub} subthemes · {nd} deep explainers so far</div>
{body}
</div></body></html>
"""

def main():
    themes = sorted(bs.BY_THEME.items(), key=lambda kv: -len(kv[1]))
    body = "".join(theme_block(t, rows) for t, rows in themes)
    nsub = 0
    for t, rows in themes:
        subs = bt.load_subthemes(bs.slug(t)); nsub += len(subs) if subs else 0
    nd = sum(1 for rows in bs.BY_THEME.values() for r in rows if has_deep(r["id"]))
    npapers = sum(len(r) for r in bs.BY_THEME.values())
    open(os.path.join(bs.SITE, "map.html"), "w").write(
        HEAD.format(nt=len(themes), np=npapers, nsub=nsub, nd=nd, body=body))
    print(f"wrote map.html ({len(themes)} themes, {nsub} subthemes, {nd} deep dives)")

if __name__ == "__main__":
    main()
