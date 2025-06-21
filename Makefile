.PHONY: db wait-db ensure-db rabbit web-stop migrate dev help

help:                ## List available targets
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) \
	  | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}'

db:                  ## Remove old standalone postgres, then start Compose db
	@echo "🛑 Removing old 'postgres' container if it exists…"
	@docker ps --filter "name=postgres$$" -q | xargs -r docker rm -f >/dev/null 2>&1 || true
	@echo "🔍 Starting 'db' service via Compose…"
	@docker compose up -d db

wait-db:             ## Wait until Postgres accepts connections
	@echo "⏳ Waiting for Postgres to be ready…"
	@until docker compose exec db pg_isready -U postgres >/dev/null 2>&1; do \
	  sleep 1; \
	done
	@echo "✅ Postgres is accepting connections."

ensure-db:           ## Create taskflow DB if it doesn’t already exist
	@echo "🔧 Ensuring database 'taskflow' exists…"
	@docker compose exec db \
	  psql -U postgres -tc "SELECT 1 FROM pg_database WHERE datname='taskflow';" \
	  | grep -q 1 \
	  && echo "✅ 'taskflow' already exists." \
	  || (echo "🚀 Creating 'taskflow'…" \
	      && docker compose exec db psql -U postgres -c "CREATE DATABASE taskflow;")
	@echo "✅ Database is ready."

rabbit:              ## Start RabbitMQ service
	@echo "🔍 Starting 'rabbitmq' service…"
	@docker compose up -d rabbitmq

web-stop:            ## Stop & remove the web container
	@echo "🛑 Stopping & removing 'web'…"
	@docker compose stop web >/dev/null 2>&1 || true
	@docker compose rm -f web  >/dev/null 2>&1 || true

migrate:             ## Run Django migrations
	@echo "🔄 Applying Django migrations…"
	@python3 manage.py migrate


# ------------------------ RUN EVERYTHING ------------------------

dev: db wait-db ensure-db rabbit web-stop migrate  ## Bootstrap everything
	@echo "✅ Ready for dev! Run: python manage.py runserver"
