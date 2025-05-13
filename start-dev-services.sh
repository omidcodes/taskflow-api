#!/bin/bash

echo "🔍 Checking PostgreSQL container..."
POSTGRES_STATUS=$(docker compose ps --status=running db | grep 'db' || true)

echo "🔍 Checking RabbitMQ container..."
RABBITMQ_STATUS=$(docker compose ps --status=running rabbitmq | grep 'rabbitmq' || true)

if [[ -z "$POSTGRES_STATUS" || -z "$RABBITMQ_STATUS" ]]; then
    echo "🚀 Starting db and rabbitmq services..."
    docker compose up -d db rabbitmq
else
    echo "✅ db and rabbitmq are already running."
fi

echo "🛑 Ensuring web container is stopped..."
docker compose stop web >/dev/null 2>&1 || true
docker compose rm -f web >/dev/null 2>&1 || true

python3 manage.py migrate

echo "✅ Ready for local development. Run: python manage.py runserver"
