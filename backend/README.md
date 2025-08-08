Backend

- Flask app with SQLAlchemy and CORS.
- SQLite by default; switch DB by setting `DATABASE_URL`.
- Endpoints: `/api/getMenu`, `/api/rules/us_population_data`, `/api/rules/about`.
- Tests with pytest under `backend/tests`.

Project layout

- `app/__init__.py`: application factory and database initialization.
- `app/config.py`: DB URI resolution and environment config.
- `app/models/`: SQLAlchemy models package (exports `AboutText`).
- `app/routes/`: Flask Blueprint split by concern (`menu.py`, `rules.py`).
- `wsgi.py`: WSGI entrypoint (used by Gunicorn).
- `instance/`: SQLite DB location (mounted as a volume in Docker).

Dev quickstart

1. Build and start services with Docker Compose.
2. Backend will listen on port 5000.

Running tests

Use pytest within the backend context.
