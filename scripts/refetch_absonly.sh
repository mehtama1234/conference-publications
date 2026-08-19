#!/usr/bin/env bash
# ③ token-free: re-fetch real method for every abstract-only spec. arXiv posts
# papers over time, so retries newly succeed. Logs new full-text hits.
cd "$(dirname "$0")/.."
python3 - <<'PY' > /tmp/icmlctx/absonly_all.json
import glob,os,json
have=set(os.path.basename(f)[:-4] for f in glob.glob("data/facts/*-or-*.txt"))
specs=[os.path.basename(f)[:-5] for f in glob.glob("specs/*-or-*.json")]
json.dump([s for s in specs if s not in have], open("/tmp/icmlctx/absonly_all.json","w") if False else __import__('sys').stdout)
PY
mapfile -t SLUGS < <(python3 -c "import json,sys;print('\n'.join(json.load(sys.stdin)))" < /tmp/icmlctx/absonly_all.json)
new=0; tried=0
: > /tmp/icmlctx/refetch_hits.txt
for f in "${SLUGS[@]}"; do
  tried=$((tried+1))
  python3 scripts/fetch_method.py "$f" >/dev/null 2>&1
  if [ -f "data/facts/$f.txt" ]; then new=$((new+1)); echo "$f" >> /tmp/icmlctx/refetch_hits.txt; fi
done
echo "REFETCH DONE: $new new full-text of $tried abstract-only" >> /tmp/icmlctx/refetch_hits.txt
