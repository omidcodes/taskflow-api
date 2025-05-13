#!/bin/bash

echo "🚀 Running migrations..."
python manage.py migrate

echo "🚀 Starting Gunicorn..."
exec gunicorn taskflow_api.wsgi:application --bind 0.0.0.0:8000
