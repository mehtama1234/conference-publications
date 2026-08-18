#!/usr/bin/env python3
"""Rebuild the ICML/ICLR theme pages as theme -> first-principles SUBTHEME ->
papers, instead of one flat list. Reads the Haiku-written subtheme taxonomies
in data/subtheme_out/<slug>.json (each: {name, gist, keywords}), assigns every
paper in the theme to its best subtheme by keyword match, and renders grouped
sections. Reuses the rendering (HEAD/CSS/paper_card) from build_site.py.
Usage: python3 scripts/build_subthemes.py
"""
import json, re, os, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_site as bs   # reuse HEAD, paper_card, FRAME, slug, e, BY_THEME, PAPERS, SITE

SUB = os.path.join(bs.D, "subtheme_out")

def load_subthemes(slug):
    fp = os.path.join(SUB, f"{slug}.json")
    if not os.path.exists(fp): return None
    try:
        d = json.load(open(fp))
        subs = d.get("subthemes", [])
        for s in subs:
            s["_kw"] = [k.lower() for k in s.get("keywords", []) if k]
            s["_papers"] = []
        return subs
    except Exception:
        return None

def assign(paper_rec, subs):
    p = bs.PAPERS.get(paper_rec["id"], {})
    text = (p.get("title", "") + " " + " ".join(paper_rec.get("methods", []))
            + " " + paper_rec.get("approach", "")).lower()
    best, best_score = None, 0
    for s in subs:
        score = sum(1 for k in s["_kw"] if k in text)
        if score > best_score:
            best, best_score = s, score
    return best

def card_with_deep(r):
    """Paper card; if this paper has a deep first-principles explainer page, weave a link to it."""
    html = bs.paper_card(r)
    slug = bs.slug(r["id"])
    if os.path.exists(os.path.join(bs.SITE, f"{slug}.html")):
        link = (f'<div style="margin-top:8px"><a href="{slug}.html" style="display:inline-block;'
                f'font-family:var(--mono);font-size:12px;color:var(--accent);border:1px solid var(--accent);'
                f'border-radius:6px;padding:3px 10px;text-decoration:none">&#9733; Read the deep first-principles explainer &rarr;</a></div>')
        if html.endswith("</div>"):
            html = html[:-6] + link + "</div>"
    return html

def build_theme(theme, rows):
    s = bs.slug(theme)
    subs = load_subthemes(s)
    o = [bs.HEAD.format(title=bs.esc(theme), i="", h="", g="")]
    if not subs:
        # fall back to flat (build_site already does this; keep as safety)
        o.append(f'<div class="kick">theme · {len(rows)} papers</div><h1>{bs.esc(theme)}</h1>')
        o.append(f'<p class="lead">{bs.esc(bs.FRAME.get(theme,""))}</p><p><a href="index.html">&larr; all themes</a></p>')
        for r in sorted(rows, key=lambda r: r["id"]): o.append(bs.paper_card(r))
        o.append(bs.FOOT); open(os.path.join(bs.SITE, f"theme-{s}.html"), "w").write("\n".join(o)); return 0
    # assign
    catch = {"name": f"Other work in {theme}", "gist": "Papers in this theme that do not fit one of the groups above.", "_kw": [], "_papers": []}
    for r in rows:
        (assign(r, subs) or catch)["_papers"].append(r)
    allsubs = [x for x in subs if x["_papers"]] + ([catch] if catch["_papers"] else [])
    # header + subtheme jump-nav
    o.append(f'<div class="kick">theme · {len(rows)} papers · {len(allsubs)} subthemes</div><h1>{bs.esc(theme)}</h1>')
    o.append(f'<p class="lead">{bs.esc(bs.FRAME.get(theme,""))}</p>')
    o.append('<p style="margin:12px 0"><a href="index.html">&larr; all themes</a></p>')
    nav = "".join(f'<a class="chip" href="#{bs.slug(x["name"])}">{bs.esc(x["name"])} · {len(x["_papers"])}</a>' for x in allsubs)
    o.append(f'<div style="display:flex;flex-wrap:wrap;gap:7px;margin:10px 0 6px">{nav}</div>')
    # sections
    for x in allsubs:
        o.append(f'<section id="{bs.slug(x["name"])}" style="margin-top:26px">')
        o.append(f'<h2 style="border-top:1px solid var(--line);padding-top:16px">{bs.esc(x["name"])} '
                 f'<span style="font-family:var(--mono);font-size:13px;color:var(--accent)">{len(x["_papers"])}</span></h2>')
        o.append(f'<p class="lead" style="font-size:16px">{bs.esc(x["gist"])}</p>')
        for r in sorted(x["_papers"], key=lambda r: r["id"]): o.append(card_with_deep(r))
        o.append('</section>')
    o.append(bs.FOOT)
    open(os.path.join(bs.SITE, f"theme-{s}.html"), "w").write("\n".join(o))
    return len(allsubs)

def main():
    total_sub = 0; have = 0
    for theme, rows in bs.BY_THEME.items():
        n = build_theme(theme, rows)
        if n: have += 1; total_sub += n
        print(f"  {bs.slug(theme):42s} {len(rows):5d} papers  {n} subthemes")
    print(f"rebuilt {len(bs.BY_THEME)} theme pages ({have} subthemed, {total_sub} subthemes total)")

if __name__ == "__main__":
    main()
