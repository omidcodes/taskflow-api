
# 🧩 TaskFlow API

A Django RESTful API for managing personal or team tasks — featuring PostgreSQL, RabbitMQ, Docker support, and developer/production-ready configurations.

---

## 🚀 Features

- ✅ Django 5 + Django REST Framework
- ✅ PostgreSQL database (via Docker)
- ✅ RabbitMQ for background tasks (Celery integrated)
- ✅ Asynchronous task logging using Celery
- ✅ Environment config with `.env` and `python-decouple`
- ✅ Swagger UI for API documentation
- ✅ Containerized with Docker
- ✅ CLI scripts for development and production modes

---

## 📁 Project Structure

```
taskflow-api/
├── taskflow_api/           # Django project (includes celery.py)
├── tasks/                  # App: task models, views, serializers, signals, celery tasks
├── requirements.txt        # Python dependencies
├── Dockerfile              # Production image for gunicorn
├── docker-compose.yml      # DB and RabbitMQ container setup
├── .env                    # Environment configuration
├── logs/                   # Directory for activity logs (auto-created)
├── run_server.sh           # Run production server (Gunicorn)
└── start-dev-services.sh   # Run DB + RabbitMQ for development
```

---

## ⚙️ Prerequisites

- Python 3.12+
- Docker & Docker Compose
- Virtualenv (optional but recommended)

---

## 📦 Setup Instructions

### 🔧 1. Install Python Dependencies
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### 🔧 2. Configure Environment
Edit `.env` (already provided):
```dotenv
DEBUG=True
SECRET_KEY=your-secret-key
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,[::1]

POSTGRES_DB=taskflow
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

CELERY_BROKER_URL=amqp://guest:guest@localhost:5672//
```

---

## 🧪 Development Mode

Use this when you want to run Django locally (`runserver`) and containers only for DB/RabbitMQ.

### ▶️ Start Docker Services:
```bash
./start-dev-services.sh
```

> This will:
> - Start PostgreSQL and RabbitMQ containers
> - Stop and remove any running web container
> - Run DB migrations automatically

### ▶️ Then Run Django:
```bash
python3 manage.py runserver
```

### ▶️ Run Celery Worker:
```bash
celery -A taskflow_api worker --loglevel=info
```

Open:
- Swagger docs: http://localhost:8000/docs/
- API root: http://localhost:8000/api/tasks/

---

## 🧩 Celery Logging Task

When a task is created through the API, a Celery worker will automatically:

- Run `log_task_action` in the background using `celery -A taskflow_api worker --loglevel=info`
- Write an entry like this to `logs/task_activity.log`:

```
[2025-09-14 19:45:00] Task #12 ('Example Task') was created
```

---

## 🏭 Production Mode (Dockerized Web)

### ▶️ Build & Run All Services:
```bash
./run_server.sh
```

> This uses Docker to run:
> - Django (with Gunicorn)
> - PostgreSQL
> - RabbitMQ

You can also run manually:
```bash
docker compose up --build
```

---

## 🗃️ Tech Stack

- **Backend**: Django 5, DRF
- **Database**: PostgreSQL (Docker)
- **Broker**: RabbitMQ (Docker)
- **Background Jobs**: Celery (activity logging)
- **Containerization**: Docker, Docker Compose
- **CI-ready**: Gunicorn + environment-based config

---

## 📜 License

MIT © Omid Hashemzadeh