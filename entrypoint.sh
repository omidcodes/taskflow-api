#!/bin/bash


# Wait for PostgreSQL to be ready
echo "⏳ Waiting for Postgres..."
until nc -z $POSTGRES_HOST 5432; do
  sleep 1
done
echo "✅ Postgres is up!"

echo "🚀 Running migrations..."
python manage.py migrate

echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

echo "🚀 Starting Gunicorn..."
exec gunicorn taskflow_api.wsgi:application --bind 0.0.0.0:8000 --timeout 120
