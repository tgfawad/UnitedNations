# Backend Dockerfile (production-ready)
FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# System deps (add DB drivers here if switching away from SQLite)
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    build-essential curl ca-certificates && \
    rm -rf /var/lib/apt/lists/*

COPY backend/requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY backend /app

# Create a non-root user
RUN useradd -m appuser
USER appuser

EXPOSE 5000

CMD ["gunicorn", "wsgi:app", "--bind", "0.0.0.0:5000", "--workers", "1", "--threads", "8", "--timeout", "60"]
