#!/usr/bin/env bash
# redeploy-site.sh — pull latest code, rebuild containers, restart using Docker Compose

set -euo pipefail

cd /root/mlh-pe-portfolio-site

git fetch origin
git reset --hard origin/main

docker compose -f docker-compose.prod.yml down

docker compose -f docker-compose.prod.yml up -d --build

echo "🚀 Redeploy complete! Application is running in Docker containers."
echo "🔗 Check status with: docker compose -f docker-compose.prod.yml ps"
