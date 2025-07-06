#!/usr/bin/env bash
#
# redeploy-site.sh — pull latest code, reinstall deps, restart Flask in a tmux session

set -euo pipefail

tmux kill-server 2>/dev/null || true
cd /root/mlh-pe-portfolio-site

git fetch origin
git reset --hard origin/main

source python3-virtualenv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

SESSION_NAME=mlh-pe-portfolio-site
tmux new-session -d -s "$SESSION_NAME" \
  "cd /root/mlh-pe-portfolio-site && \
   source python3-virtualenv/bin/activate && \
   export FLASK_ENV=production && \
   flask run --host=0.0.0.0"

echo "🚀 Redeploy complete! Flask is running in tmux session '$SESSION_NAME'."
echo "🔗 Attach with: tmux attach -t $SESSION_NAME"
