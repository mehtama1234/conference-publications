#!/bin/bash
# Process a freshly-written explainer batch: build -> autoclean common jargon ->
# GATE on clarity (refuse to commit if not clean) -> rebuild map/inventory/theme
# pages -> commit + push. Usage: bash scripts/process_batch.sh "commit message"
set -e
cd "$(dirname "$0")/.."
MSG="${1:-Rollout batch}"
BATCH="${2:-data/rollout/auto-pass.json}"

python3 scripts/build_paper_explainer.py --all >/dev/null 2>&1 || { echo "BUILD FAILED"; exit 1; }

# autoclean the recurring jargon leaks the writers occasionally miss
python3 - "$BATCH" <<'PY'
import json, sys
subs={" stochastic":" random","stochastic ":"random ","empirical ":"measured ",
      "Empirical ":"Measured ","penalty gradient":"penalty pull","pay attention there":"focus there"}
for s in json.load(open(sys.argv[1])):
    fp = f"specs/{s}.json"
    t=open(fp).read(); b=t
    for a,c in subs.items(): t=t.replace(a,c)
    if t!=b:
        try: json.loads(t); open(fp,"w").write(t)
        except Exception: pass
PY
python3 scripts/build_paper_explainer.py --all >/dev/null 2>&1

# GATE the BATCH being committed (specs in arg-2 slug-list, else data/rollout/auto-pass.json).
# The no-analogies rule applies going forward; older specs keep their analogies, so we gate the
# batch rather than the whole corpus.
MISSING=$(python3 - "$BATCH" <<'PY'
import json, os, sys
slugs = json.load(open(sys.argv[1]))
missing = [s for s in slugs if not os.path.exists(f"specs/{s}.json")]
for s in missing: print(s)
PY
)
if [ -n "$MISSING" ]; then
  echo "BATCH HAS MISSING SPECS — NOT committing. Missing slugs:"
  echo "$MISSING" | head -80
  exit 3
fi

C=$(python3 - "$BATCH" <<'PY'
import json, sys, subprocess
slugs = json.load(open(sys.argv[1]))
tot = 0
for s in slugs:
    out = subprocess.run(["python3","scripts/clarity_lint.py",f"specs/{s}.json"],capture_output=True,text=True).stdout
    n = out.count("  [")
    if n:
        tot += n
        for l in out.splitlines():
            if l.strip().startswith("["): print(f"{s}: {l.strip()}")
print("TOTALBATCH", tot)
PY
)
BAD=$(echo "$C" | grep -oE 'TOTALBATCH [0-9]+' | grep -oE '[0-9]+$')
if [ "$BAD" != "0" ]; then
  echo "CLARITY NOT CLEAN in batch ($BAD issues) — NOT committing. Flags:"
  echo "$C" | grep ': \[' | head -30
  exit 2
fi
echo "batch clarity: 0"

W=$(python3 - "$BATCH" <<'PY'
import json, sys, subprocess
slugs = json.load(open(sys.argv[1]))
files = [f"specs/{s}.json" for s in slugs]
out = subprocess.run(["python3","scripts/why_audit.py",*files],capture_output=True,text=True)
print(out.stdout, end="")
if out.stderr:
    print(out.stderr, end="")
raise SystemExit(out.returncode)
PY
) || {
  echo "WHY AUDIT NOT CLEAN in batch — NOT committing. Flags:"
  echo "$W" | grep -E 'unexplained claim|Traceback|FileNotFound|TOTAL' | head -80
  exit 4
}
echo "batch why-audit: 0"

python3 scripts/build_subthemes.py >/dev/null 2>&1
python3 scripts/build_fieldmap.py >/dev/null 2>&1
python3 scripts/build_inventory.py >/dev/null 2>&1

N=$(ls specs/*-or-*.json | wc -l | tr -d ' ')
ADD_LIST=$(mktemp)
python3 - "$BATCH" > "$ADD_LIST" <<'PY'
import json, os, sys
slugs = json.load(open(sys.argv[1]))
for s in slugs:
    for fp in (f"specs/{s}.json", f"site/{s}.html", f"data/explainer_in/{s}.json"):
        if os.path.exists(fp): print(fp)
    for ext in ("status", "txt"):
        fp = f"data/facts/{s}.{ext}"
        if os.path.exists(fp): print(fp)
for fp in (
    "data/rollout/auto-pass.json",
    "scripts/process_batch.sh",
    "scripts/fix_batch.py",
    "site/map.html",
    "site/paper-explainers.html",
    "site/themes.html",
):
    if os.path.exists(fp): print(fp)
for name in os.listdir("site"):
    if name.startswith(("theme-", "subtheme-")) and name.endswith(".html"):
        print(os.path.join("site", name))
PY
git add --pathspec-from-file="$ADD_LIST" >/dev/null 2>&1
rm -f "$ADD_LIST"
git commit -q -m "$MSG ($N explainers total)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>" && echo "committed ($N total)"
git push origin icml-iclr-theme-mining 2>&1 | tail -1
