#!/bin/bash

echo "🔍 Linting and fixing with Ruff (ignoring migrations)..."

# Lint and auto-fix, ignoring migration files
ruff check --fix . --exclude migrations

# Format code (also ignores excluded by default)
ruff format . --exclude migrations

echo "✅ Code linted and formatted!"
