# Dockerfile

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Collect static files (optional if using admin panel)
RUN mkdir -p /vol/web/static

CMD ["gunicorn", "taskflow_api.wsgi:application", "--bind", "0.0.0.0:8000"]
