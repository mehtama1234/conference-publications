#!/usr/bin/env python3
"""Fetch a paper's REAL method text so the explainer describes the actual
approach (not the abstract). Given paper ids, find each on arXiv by title,
download the PDF, extract the method-dense sentences, and write a compact
facts file the spec-writer reads. Resumable (skips papers already fetched).

Usage:
  python3 scripts/fetch_method.py <id_or_slug> [<id_or_slug> ...]
  python3 scripts/fetch_method.py --file data/rollout/<subtheme>.json   # list of ids
Writes: data/facts/<slug>.txt  (+ data/facts/<slug>.status = found|not_found)
"""
import json, sys, re, os, time, urllib.request, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, "data")
FACTS = os.path.join(D, "facts"); os.makedirs(FACTS, exist_ok=True)
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
PAPERS = {p["id"]: p for p in json.load(open(f"{D}/papers_all.json"))}
def slugify(pid): return re.sub(r"[^a-z0-9]+", "-", pid.lower()).strip("-")
def norm(s): return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()

def get(url, timeout=60, binary=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read() if binary else r.read().decode("utf-8", "ignore")

def find_arxiv(title):
    q = urllib.parse.quote(f'ti:"{title[:80]}"')
    try:
        xml = get(f"http://export.arxiv.org/api/query?search_query={q}&max_results=3", timeout=30)
    except Exception:
        return None
    entries = re.findall(r"<entry>(.*?)</entry>", xml, re.S)
    for e in entries:
        t = re.search(r"<title>(.*?)</title>", e, re.S)
        aid = re.search(r"<id>http://arxiv\.org/abs/([^<]+)</id>", e)
        if t and aid and norm(t.group(1))[:60] == norm(title)[:60]:
            return aid.group(1)
    # looser: token overlap >= 0.7
    for e in entries:
        t = re.search(r"<title>(.*?)</title>", e, re.S)
        aid = re.search(r"<id>http://arxiv\.org/abs/([^<]+)</id>", e)
        if t and aid:
            a, b = set(norm(t.group(1)).split()), set(norm(title).split())
            if b and len(a & b) / len(b) >= 0.7:
                return aid.group(1)
    return None

def extract_method(pdf_bytes):
    import pypdf, io
    r = pypdf.PdfReader(io.BytesIO(pdf_bytes))
    text = "\n".join(p.extract_text() or "" for p in r.pages)
    sents = re.split(r"(?<=[.:])\s+", re.sub(r"\s+", " ", text))
    kw = ["method", "we propose", "we introduce", "we design", "our approach", "our method",
          "architecture", "module", "we define", "consists of", "given a", "for each",
          "first", "then", "step", "assign", "compute", "encode", "retriev", "loss",
          "train", "objective", "router", "attention", "layer", "algorithm", "procedure"]
    scored = [(sum(s.lower().count(k) for k in kw), s) for s in sents if 8 < len(s.split()) < 60]
    top = sorted(range(len(scored)), key=lambda i: -scored[i][0])[:45]
    brief = " ".join(scored[i][1] for i in sorted(top))
    return brief[:6500]

def fetch_one(pid):
    slug = slugify(pid)
    fp = os.path.join(FACTS, f"{slug}.txt")
    if os.path.exists(fp):
        return slug, "cached"
    p = PAPERS.get(pid)
    if not p:
        # allow passing a slug that maps back to an id
        cand = [k for k in PAPERS if slugify(k) == pid]
        p = PAPERS.get(cand[0]) if cand else None
        if p: pid = cand[0]; slug = slugify(pid)
    if not p:
        return slug, "no-record"
    aid = find_arxiv(p["title"])
    time.sleep(3)  # be polite to arXiv
    if not aid:
        open(os.path.join(FACTS, f"{slug}.status"), "w").write("not_found")
        return slug, "not_on_arxiv"
    try:
        pdf = get(f"https://arxiv.org/pdf/{aid.split('v')[0]}", timeout=90, binary=True)
        if pdf[:5] != b"%PDF-":
            raise ValueError("not a pdf")
        brief = extract_method(pdf)
    except Exception as e:
        open(os.path.join(FACTS, f"{slug}.status"), "w").write(f"error:{e}")
        return slug, f"extract-fail:{str(e)[:40]}"
    header = (f"REAL METHOD of \"{p['title']}\" (arXiv {aid}). Extracted method-dense text follows; "
              f"base the explainer on THIS actual approach, not the abstract.\n\n")
    open(fp, "w").write(header + brief)
    open(os.path.join(FACTS, f"{slug}.status"), "w").write(f"found:{aid}")
    return slug, f"OK ({aid}, {len(brief.split())} words)"

def main():
    args = sys.argv[1:]
    if args and args[0] == "--file":
        ids = json.load(open(args[1]))
    else:
        ids = args
    for pid in ids:
        slug, status = fetch_one(pid)
        print(f"  {slug}: {status}")

if __name__ == "__main__":
    main()
