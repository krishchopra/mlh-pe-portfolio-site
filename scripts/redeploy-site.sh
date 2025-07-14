#!/usr/bin/env bash
#
# redeploy-site.sh — pull latest code, reinstall deps, restart Flask using systemd service

set -euo pipefail

cd /root/mlh-pe-portfolio-site

git fetch origin
git reset --hard origin/main

source python3-virtualenv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

sudo systemctl restart myportfolio

echo "🚀 Redeploy complete! Flask is running as systemd service."
echo "🔗 Check status with: sudo systemctl status myportfolio"
