#!/bin/bash
# Process a freshly-written explainer batch: build -> autoclean common jargon ->
# GATE on clarity (refuse to commit if not clean) -> rebuild map/inventory/theme
# pages -> commit + push. Usage: bash scripts/process_batch.sh "commit message"
set -e
cd "$(dirname "$0")/.."
MSG="${1:-Rollout batch}"

python3 scripts/build_paper_explainer.py --all >/dev/null 2>&1 || { echo "BUILD FAILED"; exit 1; }

# autoclean the recurring jargon leaks the writers occasionally miss
python3 - <<'PY'
import json, glob
subs={" stochastic":" random","stochastic ":"random ","empirical ":"measured ",
      "Empirical ":"Measured ","penalty gradient":"penalty pull","pay attention there":"focus there"}
for fp in glob.glob("specs/*-or-*.json"):
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
BATCH="${2:-data/rollout/auto-pass.json}"
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

python3 scripts/build_subthemes.py >/dev/null 2>&1
python3 scripts/build_fieldmap.py >/dev/null 2>&1
python3 scripts/build_inventory.py >/dev/null 2>&1

N=$(ls specs/*-or-*.json | wc -l | tr -d ' ')
git add specs/ data/facts/ data/explainer_in/ data/rollout/ site/ scripts/ >/dev/null 2>&1
git commit -q -m "$MSG ($N explainers total)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>" && echo "committed ($N total)"
git push origin icml-iclr-theme-mining 2>&1 | tail -1
