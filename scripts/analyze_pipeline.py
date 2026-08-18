#!/usr/bin/env python3
"""ICML/ICLR 2026 per-paper analysis pipeline (theme mining), resumable.

STAGES
  prep   : metadata/*-accepted.jsonl  ->  data/papers_all.json  +  data/chunks/chunk-NNNN.json (40/chunk)
           + data/theme_map.json (instant primary_area landscape, no LLM)
  (analyze): a fan-out of Haiku agents, one per chunk, each reads a chunk and writes
             data/analysis/chunk-NNNN.json (a list of {id,problem,approach,contribution,theme,methods}).
             Brief: /tmp/icmlctx/ANALYZE.txt. Resumable: skip chunks whose output already exists.
  merge  : validate every analysis chunk against its input (ids must match exactly), normalize
           off-list theme labels to "Other", merge -> data/analysis_merged.json + print theme map.

The analyze stage is driven by the orchestrator (Haiku agents), not this script; run `prep`
first, fan out agents over data/chunks/chunk-*.json that lack a data/analysis/ output, then `merge`.

Usage: python3 scripts/analyze_pipeline.py {prep|merge|status}
"""
import json, glob, os, sys, collections, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, "data")
CH = 40
THEMES = {"LLMs & Foundation Models","Generative Models & Diffusion","Computer Vision","Reinforcement Learning",
"Representation & Self-Supervised Learning","Optimization","Learning Theory","Alignment, Safety & Fairness",
"Interpretability","Datasets & Benchmarks & Evaluation","Robotics & Control","AI for Science",
"Efficiency & Systems","Graph & Geometric Learning","Multimodal","Agents & Tool Use","Time Series & Sequential","Other"}

def prep():
    recs = []
    for conf in ("iclr","icml"):
        fp = os.path.join(ROOT,"metadata",f"{conf}-2026-accepted.jsonl")
        for line in open(fp):
            try: r = json.loads(line)
            except: continue
            recs.append({"id":f"{conf}-{r.get('paper_id') or r.get('id')}","conf":conf.upper(),
                "title":(r.get("title") or "").strip(),"abstract":(r.get("abstract") or "").strip(),
                "tldr":(r.get("tldr") or "").strip(),"keywords":r.get("keywords") or [],
                "primary_area":(r.get("primary_area") or "").strip(),"pdf_url":r.get("pdf_url") or ""})
    json.dump(recs, open(f"{D}/papers_all.json","w"))
    os.makedirs(f"{D}/chunks", exist_ok=True); os.makedirs(f"{D}/analysis", exist_ok=True)
    n=0
    for i in range(0,len(recs),CH):
        ck=[{"id":r["id"],"conf":r["conf"],"title":r["title"],"abstract":r["abstract"][:1600],
             "primary_area":r["primary_area"]} for r in recs[i:i+CH]]
        json.dump(ck, open(f"{D}/chunks/chunk-{n:04d}.json","w")); n+=1
    area = collections.Counter(r["primary_area"] for r in recs if r["primary_area"])
    json.dump({"primary_area":dict(area)}, open(f"{D}/theme_map.json","w"))
    print(f"prep: {len(recs)} papers, {n} chunks. Fan out Haiku over chunks lacking data/analysis/ outputs.")

def merge():
    merged=[]; bad=[]
    for outp in sorted(glob.glob(f"{D}/analysis/chunk-*.json")):
        name=os.path.basename(outp)
        try:
            ind=[x["id"] for x in json.load(open(f"{D}/chunks/{name}"))]
            outd=json.load(open(outp))
        except Exception as e:
            bad.append((name,str(e))); continue
        if set(ind)!=set(x.get("id") for x in outd):
            bad.append((name,"id-mismatch")); continue
        for r in outd:
            if r.get("theme") not in THEMES: r["theme"]="Other"
            merged.append(r)
    json.dump(merged, open(f"{D}/analysis_merged.json","w"), indent=0)
    th=collections.Counter(r["theme"] for r in merged)
    print(f"merge: {len(merged)} papers from {len(glob.glob(f'{D}/analysis/chunk-*.json'))-len(bad)} clean chunks")
    if bad: print("  RE-RUN these chunks:", [b[0] for b in bad])
    for t,n in th.most_common(): print(f"  {n:5d}  {t}")

def status():
    done=set(os.path.basename(p) for p in glob.glob(f"{D}/analysis/chunk-*.json"))
    allc=set(os.path.basename(p) for p in glob.glob(f"{D}/chunks/chunk-*.json"))
    todo=sorted(allc-done)
    print(f"chunks: {len(allc)} total, {len(done)} analyzed, {len(todo)} remaining")
    if todo: print("  next:", todo[:12])

if __name__=="__main__":
    {"prep":prep,"merge":merge,"status":status}.get(sys.argv[1] if len(sys.argv)>1 else "status", status)()
