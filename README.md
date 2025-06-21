# 🧩 TaskFlow API

A Django RESTful API for managing personal or team tasks — featuring PostgreSQL, RabbitMQ, Celery, and Nginx in a Dockerized production setup.

📈 [View Test Coverage Report](https://omidcodes.github.io/taskflow-api/)

---

## 🚀 Features

- ✅ Django 5 + Django REST Framework
- ✅ PostgreSQL database (Dockerized)
- ✅ RabbitMQ for background tasks (Celery-integrated)
- ✅ Celery task queue for async logging
- ✅ Gunicorn for WSGI-based production serving
- ✅ Nginx reverse proxy for HTTP routing and static file delivery
- ✅ Environment config with `.env` and `python-decouple`
- ✅ Swagger UI for API documentation
- ✅ Docker & Docker Compose for development and deployment
- ✅ Pytest-based testing with coverage reporting

---

## 📁 Project Structure

```
taskflow-api/
├── taskflow_api/           # Django project (with celery.py)
├── tasks/                  # App: models, views, serializers, signals, celery tasks
├── tests/                  # Pytest tests for models, views, celery
├── Dockerfile              # Docker image for Django (Gunicorn inside)
├── docker-compose.yml      # Full stack (Django, DB, Celery, Nginx, RabbitMQ)
├── nginx.conf              # Nginx config for reverse proxy
├── .env                    # Environment variables
├── logs/                   # Log folder (created if missing)
├── requirements.txt        # Python dependencies
├── run_server.sh           # Start all services in production mode
├── start-dev-services.sh   # Run only DB & RabbitMQ for local development
├── lint-clean.sh           # Format & lint Python code using Ruff
└── pytest.ini              # Pytest configuration
```

---

## ⚙️ Prerequisites

- Python 3.12+
- Docker & Docker Compose
- (Optional) Virtualenv for local development

---

## 📦 Setup Instructions

### 🔧 1. Create Virtual Environment (Optional)
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### 🔧 2. Configure Environment
Copy the `.env.example` file and rename it to `.env` .

---

## 🧪 Development Mode (Local Python)

Run Django and Celery locally. Use Docker for DB & RabbitMQ only.

```bash
make dev    # using Makefile to create development envionment
pre-commit install && pre-commit install --hook-type commit-msg -f
python manage.py runserver   # Run Django locally
celery -A taskflow_api worker --loglevel=info  # Start Celery
```

> Local URLs:
> - API: http://localhost:8000/api/tasks/
> - Docs: http://localhost:8000/docs/

---

## 🧪 Run Tests

### ▶️ Run all tests
```bash
pytest
```

### ▶️ With coverage
```bash
pytest --cov=. --cov-report=term-missing
```

### ▶️ (Optional) HTML Coverage Report
```bash
pytest --cov=. --cov-report=html
# Open htmlcov/index.html in your browser
```

---

## 🧩 Celery Background Logging

When a task is created via API, a background task (`log_task_action`) is triggered:

- Logs to `logs/task_activity.log`
- Format:
```
[2025-09-14 19:45:00] Task #12 ('Example Task') was created via Celery background task.
```

---

## 🏭 Production Mode (Dockerized Full Stack)

### ▶️ Start All Services
```bash
./run_server.sh
```

This command will:
- Build the Docker image
- Run Django with Gunicorn
- Serve via Nginx on port `80`
- Collect static files into a volume
- Expose the full app on http://localhost/

> Alternatively:
```bash
docker compose up --build
```

---

## 🌐 Accessing App

- Web App: [http://localhost/](http://localhost/)
- API: [http://localhost/api/tasks/](http://localhost/api/tasks/)
- Swagger Docs: [http://localhost/docs/](http://localhost/docs/)
- RabbitMQ UI: [http://localhost:15672](http://localhost:15672) (user/pass: guest/guest)

---

## 🗃️ Tech Stack

| Layer         | Tech                    |
|---------------|-------------------------|
| Backend       | Django 5 + DRF          |
| Database      | PostgreSQL              |
| Broker        | RabbitMQ                |
| Async Tasks   | Celery                  |
| Server        | Gunicorn + Nginx        |
| Containers    | Docker Compose          |
| Testing       | Pytest + pytest-cov     |
| Linting       | Ruff                    |
| Deployment    | Shell scripts + volumes |

---

## 📜 License

MIT © Omid Hashemzadeh